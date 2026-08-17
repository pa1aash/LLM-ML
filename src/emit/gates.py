"""The three fatal gates and the run-time discreteness arm (plan §5.2).

Gate 1 (G-family, G-alpha) and gate 2 (G-discreteness, plan-load arm) abort. The
run-time arm does not abort — it refuses to let a degraded contrast be read as a
null, which is the actual hazard.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from . import constants as K
from .discreteness import min_attainable_p


class GateViolation(RuntimeError):
    """Raised by a fatal gate. Carries the gate name for test assertions."""

    def __init__(self, gate: str, message: str):
        self.gate = gate
        super().__init__(f"[{gate}] {message}")


# --------------------------------------------------------------------- gate 1

def check_family(statistics: list[dict[str, Any]], family_size: int = K.FAMILY_SIZE) -> int:
    """G-family: the emitted confirmatory count must equal FAMILY_SIZE exactly."""
    confirmatory = [s for s in statistics if s.get("confirmatory") is True]
    n = len(confirmatory)
    if n != family_size:
        ids = ", ".join(sorted(str(s.get("id", "<no id>")) for s in confirmatory))
        raise GateViolation(
            "G-family",
            f"confirmatory count is {n}, expected exactly {family_size}. "
            f"ALPHA = 0.05/{family_size} = {0.05 / family_size!r} is only correct "
            f"for a family of {family_size}. Emitted confirmatory ids: [{ids}]. "
            f"Shrinking or growing the family after registration is the defect "
            f"this gate exists to prevent (OA-5).",
        )
    return n


def check_alpha(statistics: list[dict[str, Any]], alpha: float = K.ALPHA) -> None:
    """G-alpha: every emitted alpha_applied must equal the top-level alpha."""
    for s in statistics:
        applied = s.get("alpha_applied")
        if applied is None:
            raise GateViolation(
                "G-alpha",
                f"statistic {s.get('id', '<no id>')!r} carries no alpha_applied. "
                f"Every emitted statistic must record the alpha it was judged "
                f"against.",
            )
        if applied != alpha:
            raise GateViolation(
                "G-alpha",
                f"statistic {s.get('id', '<no id>')!r} has alpha_applied="
                f"{applied!r} but the top-level alpha is {alpha!r}. The declared "
                f"threshold and the applied threshold must be the same number "
                f"(OA-5: the manuscript declared 0.05/7 while the code applied "
                f"0.05/15).",
            )


# --------------------------------------------------------- gate 2, plan-load arm

@dataclass
class FloorRecord:
    id: str
    mode: str
    n_planned: int | None
    min_attainable_p: float | None
    passes: bool
    exempt: bool = False

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "mode": self.mode,
            "n_planned": self.n_planned,
            "min_attainable_p": self.min_attainable_p,
            "pass": self.passes,
            "exempt": self.exempt,
        }


def _planned_n(spec: dict[str, Any]) -> int | None:
    mode = spec["permutation_mode"]
    if mode == "paired_exact":
        return spec.get("n_pairs_planned")
    if mode == "unpaired_exact":
        n1, n2 = spec.get("n1"), spec.get("n2")
        return None if n1 is None or n2 is None else n1 + n2
    if mode == "monte_carlo":
        return spec.get("n_permutations")
    return None


def check_discreteness_planload(
    test_specs: list[dict[str, Any]], alpha: float = K.ALPHA
) -> dict[str, Any]:
    """G-discreteness, plan-load arm.

    Runs BEFORE any data is read. Each spec describes a confirmatory test's
    design only: its id, its permutation_mode, and the counts that mode implies.
    Aborts if any test's floor is at or above alpha.
    """
    records: list[FloorRecord] = []
    failures: list[FloorRecord] = []

    for spec in test_specs:
        mode = spec["permutation_mode"]
        floor = min_attainable_p(
            mode,
            n_pairs=spec.get("n_pairs_planned"),
            n1=spec.get("n1"),
            n2=spec.get("n2"),
            n_permutations=spec.get("n_permutations"),
        )
        exempt = mode == "not_applicable"
        passes = True if exempt else floor < alpha
        rec = FloorRecord(
            id=spec["id"],
            mode=mode,
            n_planned=_planned_n(spec),
            min_attainable_p=floor,
            passes=passes,
            exempt=exempt,
        )
        records.append(rec)
        if not passes:
            failures.append(rec)

    if failures:
        lines = []
        for r in failures:
            unit = {
                "paired_exact": "B (paired batches)",
                "unpaired_exact": "n1+n2",
                "monte_carlo": "N (permutations)",
            }.get(r.mode, "n")
            lines.append(
                f"  test {r.id!r}: mode={r.mode}, {unit}={r.n_planned}, "
                f"min_attainable_p={r.min_attainable_p!r} >= alpha={alpha!r}"
            )
        raise GateViolation(
            "G-discreteness",
            "the following confirmatory tests cannot reach alpha on any data, so "
            "they are undecidable by construction and must not be run:\n"
            + "\n".join(lines)
            + "\nRaise the design's count until the floor clears alpha, or remove "
            "the test from the confirmatory family. This is the defect class that "
            "made revision 1's X1-X4 undecidable (floor 0.0625 at B=5).",
        )

    return {
        "checked_at": "plan_load",
        "verdict": "pass",
        "alpha": alpha,
        "per_test": [r.to_json() for r in records],
    }


# ---------------------------------------------------------- gate 2, run-time arm

UNDECIDABLE = "undecidable_by_discreteness"


def apply_runtime_discreteness(
    statistic: dict[str, Any], alpha: float = K.ALPHA
) -> dict[str, Any]:
    """Gate 2, run-time arm. Mutates and returns the statistic in place.

    Null batches (§2.7) and failed runs (§3.5) shrink the realised count after
    the plan-load gate has already passed, raising the floor. Where the realised
    floor is at or above alpha, the contrast is marked undecidable and its
    `significant` is set to None — never False. This arm does not abort: one
    degraded cell should not destroy an otherwise valid analysis. What it
    prevents is a discreteness artifact being read as evidence of no effect.
    """
    mode = statistic.get("permutation_mode")
    if mode == "not_applicable":
        return statistic

    floor = min_attainable_p(
        mode,
        n_pairs=statistic.get("n_pairs_realised"),
        n1=statistic.get("n1_realised"),
        n2=statistic.get("n2_realised"),
        n_permutations=statistic.get("n_permutations"),
    )
    statistic["min_attainable_p_realised"] = floor

    if floor is not None and floor >= alpha:
        statistic["status"] = UNDECIDABLE
        statistic["significant"] = None  # never False
        statistic["undecidable_reason"] = (
            f"realised permutation floor {floor!r} >= alpha {alpha!r}; the test "
            f"could not have rejected at the realised count, so this is not "
            f"evidence of no effect"
        )
    return statistic
