"""Configuration objects for the generation harness (plan §2.1, §2.3, §5.5).

The backend is selected here and nowhere else. `src/harness/generate.py` -- the
calling layer -- receives a `Backend` and never asks what kind it is; the single
`if` on backend kind in this codebase is `build_backend` below.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from emit import constants as K

#: The three real backends plus the stub Block D drives.
BACKEND_KINDS = ("local_bf16", "local_nf4", "hosted_api", "stub")

#: Plan §2.1: precision is a factor on local models only. The frontier model
#: records `provider_default (unknown)` (§2.2, D-04).
QUANTISATION_BY_KIND = {
    "local_bf16": "bf16",
    "local_nf4": "nf4_bitsandbytes",
    "hosted_api": "provider_default (unknown)",
    "stub": "stub",
}


@dataclass(frozen=True)
class GenerationParams:
    """Decoding parameters. Plan §2.1's factor row, verbatim.

    `enable_thinking` is TRUE and is not a configurable default: the original
    harness suppressed reasoning (`enable_thinking=False`,
    llm_server_small.py:43) and the paper attributed a null result to model size
    without disclosing it (OA-15). The suppression is itself under test here, so
    it is not inherited. A caller may set it False only by saying so explicitly,
    and the value is recorded in the results header either way.
    """

    temperature: float
    top_p: float = 1.0
    top_k: int | None = None          # disabled (§2.1)
    repetition_penalty: float | None = None   # none (§2.1)
    max_new_tokens: int = 4096        # D-010
    enable_thinking: bool = True      # OA-15

    def to_json(self) -> dict[str, Any]:
        return {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "repetition_penalty": self.repetition_penalty,
            "max_new_tokens": self.max_new_tokens,
            "enable_thinking": self.enable_thinking,
        }


@dataclass(frozen=True)
class BackendConfig:
    """What to talk to. `api_key_env` names an environment variable; no key,
    token or secret is ever stored in this object, printed, or written to a
    results file."""

    kind: str
    model_id: str
    revision: str | None = None
    device: str = "cuda"
    dtype: str = "bfloat16"
    api_base: str | None = None
    api_key_env: str = "LLM_API_KEY"
    api_timeout_s: float = 300.0
    extra_body: dict[str, Any] = field(default_factory=dict)
    trust_remote_code: bool = False

    def __post_init__(self) -> None:
        if self.kind not in BACKEND_KINDS:
            raise ValueError(f"unknown backend kind {self.kind!r}; "
                             f"have {BACKEND_KINDS}")

    @property
    def quantisation(self) -> str:
        return QUANTISATION_BY_KIND[self.kind]

    def to_json(self) -> dict[str, Any]:
        return {"kind": self.kind, "model_requested": self.model_id,
                "revision_requested": self.revision, "device": self.device,
                "quantisation": self.quantisation,
                "api_base": self.api_base,
                "api_key_env": self.api_key_env,
                "api_key_present": None,   # filled by the backend, never the key
                "extra_body": self.extra_body}


@dataclass(frozen=True)
class SanitisePolicy:
    """Plan §2.1 stage 3, and OA-8.

    The sanitiser confound is what the paper is about: the original applied
    `sanitize_config` to the LLM arms and never to the random arms, so a
    difference between them could not be attributed. Two invariants follow, and
    both are enforced rather than documented:

      * `enabled` may be False -- the pre-repair stage is a first-class output,
        not a debug mode;
      * one policy object governs a whole run, so it is applied SYMMETRICALLY
        across arms. `Harness` holds exactly one and stamps it on every record;
        `assert_symmetric` re-checks it from the records themselves.
    """

    enabled: bool = True
    applies_to: str = "all_arms"

    def to_json(self) -> dict[str, Any]:
        return {"enabled": self.enabled, "applies_to": self.applies_to,
                "closes": "OA-8"}


@dataclass(frozen=True)
class CellSpec:
    """One cell of the §2.2 grid, main or anchor."""

    cell_id: str
    model: str
    prompt_format: str                     # "schema" | "freeprose"
    precision: str                         # "nf4" | "bf16" | "provider_default (unknown)"
    temperature: float
    enumeration_order: str = "canonical"   # §2.8
    exemplar: str = "absent"               # §2.8: modal | non_modal | absent
    n_batches: int = K.N_BATCHES_PER_CELL
    n_per_batch: int = K.N_GENERATIONS_PER_BATCH

    def to_factors(self) -> dict[str, Any]:
        """§5.5 `cells[].factors`. Null on the two sub-design factors for a
        main-grid cell, as the schema shows."""
        anchor = self.exemplar != "absent"
        return {"model": self.model, "format": self.prompt_format,
                "precision": self.precision, "temperature": self.temperature,
                "enumeration_order": self.enumeration_order if anchor else None,
                "exemplar": self.exemplar if anchor else None}


def build_backend(cfg: BackendConfig, **kwargs: Any):
    """THE ONLY BRANCH ON BACKEND KIND.

    Everything downstream -- prompt composition, seeding, parsing, sanitising,
    record building, emission -- sees one `Backend` interface and cannot tell
    which of the four it holds.
    """
    from . import backends

    if cfg.kind in ("local_bf16", "local_nf4"):
        return backends.LocalTransformersBackend(cfg, **kwargs)
    if cfg.kind == "hosted_api":
        return backends.HostedAPIBackend(cfg, **kwargs)
    if cfg.kind == "stub":
        return backends.StubBackend(cfg, **kwargs)
    raise ValueError(f"unknown backend kind {cfg.kind!r}")
