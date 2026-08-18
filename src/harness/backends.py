"""The three generation backends, plus the stub Block D drives.

ONE INTERFACE. `Backend.generate(prompt, params, seed) -> BackendResponse`, and
`Backend.describe() -> dict`. The calling layer in `generate.py` holds a
`Backend` and never asks which one; `config.build_backend` is the single site
that branches on kind.

Each non-negotiable below closes a named S0 defect, and the mapping is stated
where the code does the work:

  OA-3   the model ACTUALLY SERVED is queried from the backend and recorded --
         per response, not once in a header. `describe()` and
         `BackendResponse.served_*`.
  OA-15  `enable_thinking=True` is passed through, and the transcript is stored
         UNTRUNCATED. No backend slices, strips, or post-processes text.
  OA-16  `finish_reason` is computed from what the backend actually did, or
         passed through verbatim from the provider, and is tagged with its
         source. It is never defaulted to "stop".

  no retries.  A failed generation raises BackendError exactly once. Nothing in
  this module catches it, sleeps, or resubmits; `generate.py` records the
  failure and moves to the next generation.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Callable

from .config import BackendConfig, GenerationParams


class BackendError(RuntimeError):
    """A generation that did not happen. Raised once, never retried."""


#: The only finish_reason emitted when the backend does not tell us and we
#: cannot compute one. OA-16: the original hardcoded "stop", which made a
#: truncated generation indistinguishable from a complete one.
UNKNOWN_FINISH_REASON = "unknown"


def compute_finish_reason(n_new_tokens: int, max_new_tokens: int,
                          last_token_id: int | None,
                          eos_token_ids: set[int]) -> str:
    """OA-16, as a pure function so the rule is testable without a GPU.

    A generation that reached the token budget is `length` -- it was cut off,
    and the record must say so. One that ended on an end-of-sequence token is
    `stop`. Anything else is `unknown`: silence about why generation stopped is
    reported as silence, never as a completed generation.

    The budget test comes FIRST. A model that emits its EOS token exactly at the
    budget is indistinguishable from one truncated there, and calling that case
    `stop` is precisely the error OA-16 names.
    """
    if n_new_tokens >= max_new_tokens:
        return "length"
    if last_token_id is not None and last_token_id in eos_token_ids:
        return "stop"
    return UNKNOWN_FINISH_REASON


@dataclass
class BackendResponse:
    text: str
    finish_reason: str
    finish_reason_source: str           # computed_from_token_ids | provider | stub
    served_model: str                   # what ANSWERED, not what was asked for
    served_revision: str | None
    quantisation: str
    n_generated_tokens: int | None = None
    n_prompt_tokens: int | None = None
    provider_fields: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        return {
            "finish_reason": self.finish_reason,
            "finish_reason_source": self.finish_reason_source,
            "model_served": self.served_model,
            "model_revision_served": self.served_revision,
            "quantisation": self.quantisation,
            "n_generated_tokens": self.n_generated_tokens,
            "n_prompt_tokens": self.n_prompt_tokens,
            "provider_fields": self.provider_fields,
        }


# --------------------------------------------------------------- local backends

class LocalTransformersBackend:
    """`transformers` in bf16, or the same in bitsandbytes NF4.

    The two are one class because they differ only in the quantisation config
    handed to `from_pretrained`; making them two would put a second branch on
    precision into the codebase for no gain.
    """

    def __init__(self, cfg: BackendConfig, model: Any = None, tokenizer: Any = None):
        self.cfg = cfg
        self.kind = cfg.kind
        self._model = model
        self._tokenizer = tokenizer
        self._torch = None

    # -- loading ------------------------------------------------------------

    def load(self) -> None:
        """Import torch/transformers and materialise the model.

        Deliberately not called from __init__: constructing a backend must be
        free, so a dry run can build the whole harness without a GPU.
        """
        import torch  # noqa: PLC0415
        from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: PLC0415

        self._torch = torch
        kwargs: dict[str, Any] = {
            "trust_remote_code": self.cfg.trust_remote_code,
        }
        if self.cfg.revision:
            kwargs["revision"] = self.cfg.revision

        if self.kind == "local_nf4":
            from transformers import BitsAndBytesConfig  # noqa: PLC0415

            kwargs["quantization_config"] = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
        else:
            kwargs["dtype"] = torch.bfloat16

        self._tokenizer = AutoTokenizer.from_pretrained(
            self.cfg.model_id, revision=self.cfg.revision,
            trust_remote_code=self.cfg.trust_remote_code)
        self._model = AutoModelForCausalLM.from_pretrained(
            self.cfg.model_id, device_map=self.cfg.device, **kwargs)
        self._model.eval()

    # -- OA-3 ---------------------------------------------------------------

    def describe(self) -> dict[str, Any]:
        """What is ACTUALLY loaded, read off the object, not off the config.

        OA-3: the original recorded nothing, and its servers ignored the
        requested model name, so no artifact can say which model produced the
        proposals. Here the requested id and the served id are separate fields
        and a mismatch is visible in the results file.
        """
        served, revision, dtype, quant = None, None, None, self.cfg.quantisation
        if self._model is not None:
            conf = getattr(self._model, "config", None)
            served = (getattr(conf, "_name_or_path", None)
                      or getattr(self._model, "name_or_path", None))
            revision = getattr(conf, "_commit_hash", None)
            dtype = str(getattr(self._model, "dtype", "")) or None
            qc = getattr(conf, "quantization_config", None)
            if qc is not None:
                quant = json.dumps(qc.to_dict() if hasattr(qc, "to_dict") else str(qc),
                                   sort_keys=True)
        return {
            "backend": self.kind,
            "requested": self.cfg.model_id,
            "requested_revision": self.cfg.revision,
            "served": served or "UNLOADED",
            "served_revision": revision,
            "dtype": dtype,
            "quantisation": quant,
            "loaded": self._model is not None,
        }

    # -- generation ---------------------------------------------------------

    def generate(self, prompt: str, params: GenerationParams, seed: int) -> BackendResponse:
        if self._model is None or self._tokenizer is None:
            raise BackendError("backend not loaded: call load() first")
        torch = self._torch
        tok = self._tokenizer

        # OA-15: reasoning is ENABLED. `enable_thinking` is a Qwen chat-template
        # keyword; templates that do not take it must not fail silently, so the
        # fallback is recorded on the response rather than swallowed.
        template_kwargs: dict[str, Any] = {"add_generation_prompt": True,
                                           "tokenize": False}
        thinking_applied = True
        try:
            text = tok.apply_chat_template(
                [{"role": "user", "content": prompt}],
                enable_thinking=params.enable_thinking, **template_kwargs)
        except TypeError:
            thinking_applied = False
            text = tok.apply_chat_template(
                [{"role": "user", "content": prompt}], **template_kwargs)

        inputs = tok([text], return_tensors="pt").to(self._model.device)
        n_prompt = int(inputs["input_ids"].shape[-1])

        # Deterministic per-generation seeding (§2.3, D-004).
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

        gen_kwargs: dict[str, Any] = {
            "max_new_tokens": params.max_new_tokens,
            "do_sample": True,
            "temperature": params.temperature,
            "top_p": params.top_p,
            "top_k": 0 if params.top_k is None else params.top_k,  # §2.1: disabled
        }
        if params.repetition_penalty is not None:
            gen_kwargs["repetition_penalty"] = params.repetition_penalty

        try:
            with torch.no_grad():
                out = self._model.generate(**inputs, **gen_kwargs)
        except Exception as exc:                     # no retry, no repair
            raise BackendError(f"{type(exc).__name__}: {exc}") from exc

        new_ids = out[0][n_prompt:]
        n_new = int(new_ids.shape[-1])

        # OA-16: computed, never assumed. A generation that ran to the token
        # budget is `length`; one that stopped on an end-of-sequence token is
        # `stop`; anything else is `unknown` and says so.
        eos_ids = set()
        for cand in (getattr(self._model.generation_config, "eos_token_id", None),
                     getattr(tok, "eos_token_id", None)):
            if isinstance(cand, int):
                eos_ids.add(cand)
            elif isinstance(cand, (list, tuple)):
                eos_ids.update(int(c) for c in cand)
        last = int(new_ids[-1]) if n_new else None
        finish = compute_finish_reason(n_new, params.max_new_tokens, last, eos_ids)

        # OA-15: UNTRUNCATED. Special tokens are kept so the thinking trace and
        # its delimiters survive verbatim; nothing here slices the string.
        raw = tok.decode(new_ids, skip_special_tokens=False)

        d = self.describe()
        return BackendResponse(
            text=raw,
            finish_reason=finish,
            finish_reason_source="computed_from_token_ids",
            served_model=d["served"],
            served_revision=d["served_revision"],
            quantisation=d["quantisation"],
            n_generated_tokens=n_new,
            n_prompt_tokens=n_prompt,
            provider_fields={"thinking_kwarg_accepted": thinking_applied,
                             "dtype": d["dtype"]},
        )


# --------------------------------------------------------------- hosted backend

class HostedAPIBackend:
    """An OpenAI-shaped `/chat/completions` endpoint.

    Built against the same interface as the local backends and exercised by the
    stub, so it is complete without a key: the operator input it still needs is
    the model choice and the key itself, not code.

    The key is read from the environment at call time and never stored on the
    object, never logged, and never written to a results file.
    """

    def __init__(self, cfg: BackendConfig, opener: Callable[..., Any] | None = None):
        self.cfg = cfg
        self.kind = cfg.kind
        self._opener = opener or urllib.request.urlopen
        self._last_served: str | None = None
        self._last_fingerprint: str | None = None

    def _key(self) -> str:
        key = os.environ.get(self.cfg.api_key_env, "")
        if not key:
            raise BackendError(
                f"no API key in ${self.cfg.api_key_env}; hosted backend cannot run"
            )
        return key

    def describe(self) -> dict[str, Any]:
        """OA-3 for a hosted model: `served` is whatever the last response said
        answered, which is the only thing a provider actually tells us."""
        return {
            "backend": self.kind,
            "requested": self.cfg.model_id,
            "requested_revision": self.cfg.revision,
            "served": self._last_served or "UNQUERIED",
            "served_revision": self._last_fingerprint,
            "dtype": None,
            "quantisation": self.cfg.quantisation,
            "api_base": self.cfg.api_base,
            "api_key_present": bool(os.environ.get(self.cfg.api_key_env, "")),
        }

    def generate(self, prompt: str, params: GenerationParams, seed: int) -> BackendResponse:
        if not self.cfg.api_base:
            raise BackendError("hosted backend has no api_base configured")

        body: dict[str, Any] = {
            "model": self.cfg.model_id,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": params.temperature,
            "top_p": params.top_p,
            "max_tokens": params.max_new_tokens,
            "seed": seed,                      # honoured or not; recorded either way
        }
        # OA-15 on a hosted model: providers spell reasoning differently, so the
        # request is built from configuration and the request's own thinking
        # fields are echoed into the record rather than assumed.
        body.update(self.cfg.extra_body)

        req = urllib.request.Request(
            self.cfg.api_base.rstrip("/") + "/chat/completions",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json",
                     "Authorization": f"Bearer {self._key()}"},
            method="POST",
        )
        try:
            with self._opener(req, timeout=self.cfg.api_timeout_s) as resp:
                payload = json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:      # no retry
            raise BackendError(f"HTTP {exc.code}: {_redact(exc.read())}") from exc
        except Exception as exc:                   # no retry
            raise BackendError(f"{type(exc).__name__}: {exc}") from exc

        try:
            choice = payload["choices"][0]
            message = choice["message"]
        except (KeyError, IndexError) as exc:
            raise BackendError(f"malformed response: {list(payload)}") from exc

        # OA-15: reasoning text, where the provider returns it separately, is
        # concatenated in rather than dropped. Nothing is truncated.
        parts = []
        for key in ("reasoning_content", "reasoning", "thinking"):
            val = message.get(key)
            if isinstance(val, str) and val:
                parts.append(val)
        content = message.get("content")
        if isinstance(content, str):
            parts.append(content)
        elif isinstance(content, list):            # content-block shaped replies
            parts.extend(b.get("text", "") for b in content if isinstance(b, dict))
        text = "".join(parts)

        # OA-16: verbatim from the provider. Absent means unknown, not "stop".
        finish = choice.get("finish_reason") or choice.get("stop_reason")
        if not finish:
            finish = UNKNOWN_FINISH_REASON

        # OA-3: what answered.
        self._last_served = payload.get("model") or "UNREPORTED"
        self._last_fingerprint = payload.get("system_fingerprint")
        usage = payload.get("usage") or {}

        return BackendResponse(
            text=text,
            finish_reason=finish,
            finish_reason_source="provider",
            served_model=self._last_served,
            served_revision=self._last_fingerprint,
            quantisation=self.cfg.quantisation,
            n_generated_tokens=usage.get("completion_tokens"),
            n_prompt_tokens=usage.get("prompt_tokens"),
            provider_fields={"id": payload.get("id"),
                             "system_fingerprint": self._last_fingerprint,
                             "seed_sent": seed,
                             "request_thinking_fields":
                                 {k: v for k, v in self.cfg.extra_body.items()}},
        )


def _redact(raw: bytes | str) -> str:
    text = raw.decode(errors="replace") if isinstance(raw, bytes) else raw
    return text[:400].replace("\n", " ")


# ------------------------------------------------------------------ stub backend

class StubBackend:
    """Scripted outputs, so every path is exercised without a model.

    A script entry is either a `BackendResponse` or an exception instance; an
    exception is raised, which is how D6 drives the backend-failure path. The
    script is a callable `(prompt, params, seed) -> entry`, or a list consumed in
    order.

    Determinism (D8) is the caller's: the same seed must produce the same entry.
    The default script honours that by keying on the seed.
    """

    def __init__(self, cfg: BackendConfig, script: Any = None,
                 served_model: str | None = None):
        self.cfg = cfg
        self.kind = "stub"
        self.script = script
        self.calls: list[dict[str, Any]] = []
        self.served_model = served_model or f"stub::{cfg.model_id}"

    def describe(self) -> dict[str, Any]:
        return {"backend": "stub", "requested": self.cfg.model_id,
                "requested_revision": self.cfg.revision,
                "served": self.served_model, "served_revision": "stub-revision",
                "dtype": None, "quantisation": self.cfg.quantisation,
                "loaded": True}

    def generate(self, prompt: str, params: GenerationParams, seed: int) -> BackendResponse:
        self.calls.append({"prompt": prompt, "seed": seed,
                           "temperature": params.temperature})
        entry = self.script
        if callable(entry):
            entry = entry(prompt, params, seed)
        elif isinstance(entry, list):
            entry = entry[(len(self.calls) - 1) % len(entry)]
        if isinstance(entry, BaseException):
            raise entry
        if isinstance(entry, BackendResponse):
            return entry
        if isinstance(entry, str):
            entry = {"text": entry}
        if not isinstance(entry, dict):
            raise BackendError(f"stub script produced {type(entry).__name__}")
        return BackendResponse(
            text=entry["text"],
            finish_reason=entry.get("finish_reason", "stop"),
            finish_reason_source="stub",
            served_model=entry.get("served_model", self.served_model),
            served_revision=entry.get("served_revision", "stub-revision"),
            quantisation=self.cfg.quantisation,
            n_generated_tokens=entry.get("n_generated_tokens"),
            n_prompt_tokens=entry.get("n_prompt_tokens"),
            provider_fields=entry.get("provider_fields", {}),
        )
