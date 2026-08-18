"""The results-file emitter (plan §5.5, schema 1.5.0).

This is the only path by which a number reaches a results file. Nothing writes to
`results/` except `ResultsEmitter.write`, and `write` runs the three fatal gates
first. A file that exists is a file whose gates passed.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from . import constants as K
from .gates import (
    apply_runtime_discreteness,
    check_alpha,
    check_discreteness_planload,
    check_family,
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _git_commit() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
            cwd=os.path.dirname(os.path.abspath(__file__)),
        )
        return out.stdout.strip() if out.returncode == 0 else "UNKNOWN"
    except Exception:
        return "UNKNOWN"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _module_version(name: str) -> str:
    try:
        mod = __import__(name)
        return getattr(mod, "__version__", "present")
    except Exception:
        return "absent"


def default_environment() -> dict[str, str]:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "torch": _module_version("torch"),
        "transformers": _module_version("transformers"),
        "bitsandbytes": _module_version("bitsandbytes"),
        "numpy": _module_version("numpy"),
        "scipy": _module_version("scipy"),
        "cuda": os.environ.get("CUDA_VERSION", "unrecorded"),
        "gpu": os.environ.get("GPU_NAME", "unrecorded"),
        "driver": os.environ.get("NVIDIA_DRIVER", "unrecorded"),
    }


@dataclass
class ResultsEmitter:
    """Accumulates a results file and writes it only if every gate passes.

    Usage:
        em = ResultsEmitter(experiment="E1")
        em.declare_confirmatory_design([...])   # gate 2, plan-load: BEFORE data
        ... read data, add cells and statistics ...
        em.write("results/E1.json")             # gate 1 + runtime arm
    """

    experiment: str
    plan_sha256: str = K.PLAN_SHA256
    plan_supersedes_sha256: str = K.PLAN_SUPERSEDES_SHA256
    plan_chain_sha256: list[str] = field(default_factory=lambda: list(K.PLAN_CHAIN_SHA256))
    schema_version: str = K.SCHEMA_VERSION
    plan_revision: int = K.PLAN_REVISION
    alpha: float = K.ALPHA
    family_size: int = K.FAMILY_SIZE
    seeds: list[int] = field(default_factory=lambda: list(K.SEEDS))
    n_batches_per_cell: int = K.N_BATCHES_PER_CELL

    environment: dict[str, Any] = field(default_factory=default_environment)
    model: dict[str, Any] = field(default_factory=dict)
    prompts: dict[str, str] = field(default_factory=dict)

    #: §5.5's `d_rand` block. Measured at revision 4 (tests/compute_d_rand_r4.py)
    #: and restated here so a results file carries the reference its thresholds
    #: are fractions of.
    d_rand: dict[str, Any] = field(default_factory=lambda: {
        "value": K.D_RAND,
        "definition": "corrected uniform sampler, block count FIXED, "
                      "mean over K in {3,4,5,6}",
        "seed": K.D_RAND_SEED,
        "structure": {"n_batches": K.N_BATCHES_PER_CELL,
                      "n_per_batch": K.N_GENERATIONS_PER_BATCH},
        "analytic": 0.718872,
        "sanity_range": list(K.D_RAND_SANITY_RANGE),
        "sanity_pass": K.D_RAND_SANITY_RANGE[0] <= K.D_RAND <= K.D_RAND_SANITY_RANGE[1],
        "d_repo_sampler": K.D_REPO_SAMPLER,
    })

    generations: list[dict[str, Any]] = field(default_factory=list)
    deltas: list[dict[str, Any]] = field(default_factory=list)
    cells: list[dict[str, Any]] = field(default_factory=list)
    runs: list[dict[str, Any]] = field(default_factory=list)
    correlations: list[dict[str, Any]] = field(default_factory=list)
    statistics: list[dict[str, Any]] = field(default_factory=list)
    signature_match: dict[str, Any] = field(default_factory=dict)
    na_counts: dict[str, Any] = field(default_factory=dict)
    failures: list[Any] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)

    _gate_record: dict[str, Any] | None = None
    _data_read: bool = False

    # ------------------------------------------------------------- gate 2 (pre)

    def declare_confirmatory_design(self, test_specs: list[dict[str, Any]]) -> dict[str, Any]:
        """Run gate 2's plan-load arm. MUST be called before any data is read.

        Aborts with GateViolation if any confirmatory test's floor >= alpha.
        """
        if self._data_read:
            raise RuntimeError(
                "declare_confirmatory_design() called after data was added; the "
                "plan-load arm of gate 2 must run before any data is read (§5.2)"
            )
        self._gate_record = check_discreteness_planload(test_specs, alpha=self.alpha)
        return self._gate_record

    # ------------------------------------------------------------------ intake

    def add_cell(self, cell: dict[str, Any]) -> None:
        self._data_read = True
        self.cells.append(cell)

    def add_generation(self, record: dict[str, Any]) -> None:
        """§5.5 `generations[]` (D-21). Every pooled, bootstrapped or entropy
        quantity must be recomputable from these records alone."""
        self._data_read = True
        self.generations.append(record)

    def add_generations(self, records: list[dict[str, Any]]) -> None:
        for r in records:
            self.add_generation(r)

    def add_delta(self, delta: dict[str, Any]) -> None:
        """§5.5 `deltas[]` (S3B-15): a change column with its own field."""
        self._data_read = True
        self.deltas.append(delta)

    def add_run(self, run: dict[str, Any]) -> None:
        self._data_read = True
        self.runs.append(run)

    def add_correlation(self, corr: dict[str, Any]) -> None:
        self._data_read = True
        self.correlations.append(corr)

    def add_statistic(self, stat: dict[str, Any]) -> dict[str, Any]:
        """Register a statistic. Stamps alpha_applied and applies the run-time
        discreteness arm to confirmatory permutation tests."""
        self._data_read = True
        stat.setdefault("alpha_applied", self.alpha)
        stat.setdefault("status", "ok")
        stat.setdefault("confirmatory", False)
        if stat.get("confirmatory") and "permutation_mode" in stat:
            apply_runtime_discreteness(stat, alpha=self.alpha)
        self.statistics.append(stat)
        return stat

    # ------------------------------------------------------------------ output

    def _header(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "experiment": self.experiment,
            "plan_revision": self.plan_revision,
            "plan_sha256": self.plan_sha256,
            "plan_supersedes_sha256": self.plan_supersedes_sha256,
            "plan_chain_sha256": self.plan_chain_sha256,
            "code_commit": _git_commit(),
            "generated_at": _utc_now(),
            "environment": self.environment,
            "model": self.model,
            "prompts": self.prompts,
            "seeds": self.seeds,
            "n_batches_per_cell": self.n_batches_per_cell,
            # --- registered 1.4.0 / 1.5.0 header fields (D-009) ---------------
            "b_tracking": {
                "value": K.B_TRACKING,
                "floor": K.B_TRACKING_FLOOR,
                "source": "results/pilots/pilot_tracking.json",
                "binding_quantity": "cross_level_exemplar",
            },
            "r_final": {
                "value": K.R_FINAL,
                "floor": K.R_FLOOR,
                "source": "results/pilots/power_e2.json",
                "power_at_floor": 0.702,
            },
            "field_collapse_entropy_threshold": K.FIELD_COLLAPSE_ENTROPY_THRESHOLD,
            "exemplar_values": K.EXEMPLAR_VALUES,
            "chance_rates": K.CHANCE_RATES,
            "tracking_label_rule": K.TRACKING_LABEL_RULE,
            "d_rand": self.d_rand,
            "bootstrap": {
                "resamples": K.BOOTSTRAP_RESAMPLES,
                "method": K.BOOTSTRAP_METHOD,
                "seed": K.BOOTSTRAP_SEED,
                # §2.4.5 R5-10: the unit is per statistic, not global.
                "resampling_unit_pooled": "generation",
                "resampling_unit_delta": "batch_index_pair",
                "resampling_unit_tracking": "batch",
                "resampling_unit_cliffs_delta": "run",
            },
            "confirmatory_family_size": self.family_size,
            "alpha": self.alpha,
        }

    def build(self) -> dict[str, Any]:
        """Run every fatal gate, then assemble the document."""
        # Gate 1.
        check_family(self.statistics, family_size=self.family_size)
        check_alpha(self.statistics, alpha=self.alpha)

        # Gate 2 must have run before data intake.
        if self._gate_record is None:
            raise RuntimeError(
                "declare_confirmatory_design() was never called: gate 2's "
                "plan-load arm did not run, so the discreteness floors were "
                "never checked (§5.2)"
            )

        doc = self._header()
        doc["discreteness_gate"] = self._gate_record
        if self.generations:
            doc["generations"] = self.generations
        if self.cells:
            doc["cells"] = self.cells
        if self.deltas:
            doc["deltas"] = self.deltas
        if self.runs:
            doc["runs"] = self.runs
        if self.correlations:
            doc["correlations"] = self.correlations
        doc["statistics"] = self.statistics
        if self.signature_match:
            doc["signature_match"] = self.signature_match
        doc["na_counts"] = self.na_counts
        doc["failures"] = self.failures
        doc.update(self.extra)
        return doc

    def write(self, path: str) -> dict[str, Any]:
        doc = self.build()
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w") as fh:
            json.dump(doc, fh, indent=2, sort_keys=False)
            fh.write("\n")
        return doc


def not_applicable_slot(test_id: str, reason: str) -> dict[str, Any]:
    """A family slot that cannot be evaluated but must not shrink the family.

    §5.2: X3 is undefined for the frontier model (no precision factor). Its slot
    is retained so the emitted count stays exactly FAMILY_SIZE.
    """
    return {
        "id": test_id,
        "kind": "permutation",
        "permutation_mode": "not_applicable",
        "status": "not_applicable",
        "reason": reason,
        "p": None,
        "significant": None,
        "confirmatory": True,
        "alpha_applied": K.ALPHA,
    }
