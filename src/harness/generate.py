"""The calling layer: prompts in, `generations[]` records out.

THIS MODULE DOES NOT KNOW WHICH BACKEND IT HOLDS. It calls
`backend.generate(...)` and `backend.describe()`; the only branch on backend
kind in the codebase is `config.build_backend`. A test in
`tests/test_harness.py` re-checks that by reading this file.

Defect mapping, stated where the code does the work:

  OA-3   `model_served` / `model_revision_served` / `quantisation` are copied
         onto EVERY record from what the backend reports, not from the request.
  OA-8   one `SanitisePolicy` governs a run and is stamped on every record, so
         asymmetric application across arms is visible in the data rather than
         hidden in a call site.
  OA-15  `enable_thinking` comes from `GenerationParams`, defaults True, and the
         transcript is stored exactly as returned -- this module never slices,
         strips, trims or summarises `raw_text`.
  OA-16  `finish_reason` and `finish_reason_source` are copied from the backend
         response. There is no default and no fallback to "stop".

  NO SILENT RETRIES. `BackendError` is caught once, per generation, recorded as
  `status: "backend_error"` with `finish_reason: "error"`, and the loop CONTINUES
  to the next generation. Nothing resubmits, repairs-and-retries, or sleeps.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any, Iterable

from emit import constants as K

from .backends import BackendError
from .config import CellSpec, GenerationParams, SanitisePolicy
from .parse import run_pipeline

#: D-004. Injective over the registered ranges (S[b] <= 7016, index < 20), so no
#: two E1 generations share a seed, and each one replays on its own.
SEED_DERIVATION = "batch_seed * 1000 + index_in_batch"


def generation_seed(batch_seed: int, index_in_batch: int) -> int:
    return batch_seed * 1000 + index_in_batch


def generation_id(cell_id: str, batch: int, index_in_batch: int) -> str:
    """§5.5's form: `E1.CELL_ID.b03.g07`."""
    return f"E1.{cell_id}.b{batch:02d}.g{index_in_batch:02d}"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


@dataclass
class Harness:
    """One backend, one decoding configuration, one sanitiser policy, one run."""

    backend: Any
    params: GenerationParams
    sanitise_policy: SanitisePolicy = SanitisePolicy()
    experiment: str = "E1"

    # ---------------------------------------------------------------- one call

    def generate_one(self, *, cell: CellSpec, batch: int, index_in_batch: int,
                     prompt: str) -> dict[str, Any]:
        """One generation, one record. Never raises for a failed generation."""
        batch_seed = K.SEEDS[batch % len(K.SEEDS)]
        seed = generation_seed(batch_seed, index_in_batch)

        record: dict[str, Any] = {
            "generation_id": generation_id(cell.cell_id, batch, index_in_batch),
            "cell_id": cell.cell_id,
            "batch": batch,
            "index_in_batch": index_in_batch,
            "seed": batch_seed,                      # §2.3's registered batch seed
            "generation_seed": seed,                 # D-004
            "seed_derivation": SEED_DERIVATION,      # D-004
            "enumeration_order": cell.enumeration_order,
            "exemplar": cell.exemplar,
            "prompt_sha256": sha256_text(prompt),
            "backend": self.backend.kind,
            "enable_thinking": self.params.enable_thinking,
            "max_new_tokens": self.params.max_new_tokens,
            "temperature": self.params.temperature,
            "sanitiser_enabled": self.sanitise_policy.enabled,
            "sanitiser_applies_to": self.sanitise_policy.applies_to,
        }

        try:
            resp = self.backend.generate(prompt, self.params, seed)
        except BackendError as exc:
            # No retry. No repair-and-resubmit. The failure IS the datum.
            record.update({
                "status": "backend_error",
                "error": f"{type(exc).__name__}: {exc}",
                "raw_text": None,
                "raw_text_sha256": None,
                "finish_reason": "error",
                "finish_reason_source": "harness",
                "model_served": None,
                "model_revision_served": None,
                "quantisation": None,
                "n_generated_tokens": None,
                "parse_outcome": "not_attempted",
                "parse_error": None,
                "extraction_method": None,
                "spec_pre_repair": None,
                "spec_post_repair": None,
                "repair_channels": {},
                "repair_destinations": {},
                "sanitiser_applied": False,
                "metrics_computed_at": _metrics_stub(),
            })
            return record

        # OA-15: stored exactly as returned. No slicing anywhere in this method.
        raw = resp.text
        record.update({
            "status": "ok",
            "error": None,
            "raw_text": raw,
            "raw_text_sha256": sha256_text(raw),
            # OA-16: the backend's answer, with its provenance.
            "finish_reason": resp.finish_reason,
            "finish_reason_source": resp.finish_reason_source,
            # OA-3: what ANSWERED, recorded per generation so a mid-run swap shows.
            "model_served": resp.served_model,
            "model_revision_served": resp.served_revision,
            "quantisation": resp.quantisation,
            "n_generated_tokens": resp.n_generated_tokens,
            "n_prompt_tokens": resp.n_prompt_tokens,
            "provider_fields": resp.provider_fields,
        })

        pipeline = run_pipeline(raw, cell.enumeration_order,
                                sanitiser_enabled=self.sanitise_policy.enabled)
        record.update(pipeline.to_record_fields())
        record["enumeration_order_applied"] = cell.enumeration_order
        record["metrics_computed_at"] = _metrics_stub()
        return record

    # ------------------------------------------------------------- one batch

    def generate_batch(self, *, cell: CellSpec, batch: int,
                       prompt: str) -> list[dict[str, Any]]:
        return [self.generate_one(cell=cell, batch=batch, index_in_batch=i,
                                  prompt=prompt)
                for i in range(cell.n_per_batch)]

    # -------------------------------------------------------------- one cell

    def generate_cell(self, *, cell: CellSpec, prompt: str) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for b in range(cell.n_batches):
            out.extend(self.generate_batch(cell=cell, batch=b, prompt=prompt))
        return out

    # ------------------------------------------------------------- provenance

    def run_manifest(self) -> dict[str, Any]:
        """What the §5.5 `model` header needs, taken from the backend itself."""
        d = self.backend.describe()
        return {
            "requested": d.get("requested"),
            "served": d.get("served"),
            "revision": d.get("served_revision"),
            "quantisation": d.get("quantisation"),
            "backend": d.get("backend"),
            "enable_thinking": self.params.enable_thinking,
            "max_new_tokens": self.params.max_new_tokens,
            # OA-15: no transcript is truncated anywhere in this harness, and the
            # header says so with a number rather than a promise.
            "truncation_chars": None,
            "decoding": self.params.to_json(),
            "sanitiser": self.sanitise_policy.to_json(),
        }


def _metrics_stub() -> dict[str, list[str]]:
    """§5.5 `metrics_computed_at`: which stages each metric is computed at."""
    return {"D": ["pre_repair", "post_repair"],
            "S": ["raw"],
            "field_entropy": ["pre_repair", "post_repair"],
            "anchor_tracking": ["pre_repair", "post_repair"]}


# --------------------------------------------------------------- OA-8 symmetry

def assert_symmetric(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """OA-8, checked from the DATA rather than trusted from the call site.

    The original applied `sanitize_config` to the LLM arms and never to the
    random arms, so any difference between them was uninterpretable. Here every
    record carries the policy that produced it; if a run contains more than one,
    the arms are not comparable and the check fails loudly.
    """
    settings = {(bool(r.get("sanitiser_enabled")), r.get("sanitiser_applies_to"))
                for r in records}
    if len(settings) > 1:
        raise AssertionError(
            "sanitiser applied asymmetrically across the run (OA-8): "
            f"{sorted(settings)}"
        )
    enabled, applies_to = next(iter(settings)) if settings else (None, None)
    return {"symmetric": True, "enabled": enabled, "applies_to": applies_to}
