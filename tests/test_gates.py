"""Block B — adversarial gate tests.

A gate is worthless unless it fires. Each fixture is built to trigger (or to
deliberately NOT trigger) one gate, and the outcome is checked against arithmetic
computed here rather than against the outcome we expect.

B4 is the trap case: 2/2**10 = 0.001953125, which is BELOW alpha = 0.003125, so
B=10 must NOT abort even though it is a batch count the plan rejected on other
grounds (its ceiling of 1 assignment-pair, §2.3). The gate tests decidability,
not adequacy. These are different properties and the fixture proves the gate does
not conflate them.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from emit import constants as K  # noqa: E402
from emit.discreteness import (  # noqa: E402
    ceiling_pairs,
    discordance_tolerance,
    min_attainable_p,
)
from emit.emitter import ResultsEmitter, not_applicable_slot  # noqa: E402
from emit.gates import GateViolation, UNDECIDABLE  # noqa: E402

ALPHA = K.ALPHA
RESULTS: list[dict] = []


# --------------------------------------------------------------------- helpers

def paired_spec(test_id: str, b: int = 16) -> dict:
    return {"id": test_id, "permutation_mode": "paired_exact", "n_pairs_planned": b}


def paired_stat(test_id: str, b_planned: int = 16, b_realised: int | None = None) -> dict:
    if b_realised is None:
        b_realised = b_planned
    return {
        "id": test_id,
        "kind": "paired_permutation",
        "contrast": "fixture",
        "paired": True,
        "permutation_mode": "paired_exact",
        "n_pairs_planned": b_planned,
        "n_pairs_realised": b_realised,
        "n_permutations": 2 ** b_realised,
        "estimate": 0.1,
        "p": 0.02,
        "confirmatory": True,
        "significant": False,
    }


def full_family(n: int = 16, b: int = 16) -> tuple[list[dict], list[dict]]:
    specs = [paired_spec(f"T{i}", b) for i in range(n)]
    stats = [paired_stat(f"T{i}", b) for i in range(n)]
    return specs, stats


def run_fixture(name: str, expected: str, fn) -> None:
    try:
        detail = fn()
        actual = "no abort"
        message = detail or ""
    except GateViolation as exc:
        actual = f"abort [{exc.gate}]"
        message = str(exc).splitlines()[0][:140]
    except Exception as exc:  # an unexpected failure is itself a finding
        actual = f"UNEXPECTED {type(exc).__name__}"
        message = str(exc)[:140]
    RESULTS.append(
        {
            "fixture": name,
            "expected": expected,
            "actual": actual,
            "match": expected == actual,
            "detail": message,
        }
    )


# ----------------------------------------------------------------- B1 .. B8

def b1_family_15():
    specs, stats = full_family(15)
    em = ResultsEmitter(experiment="FIXTURE")
    em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    em.build()
    return "built with 15 confirmatory"


def b2_family_17():
    specs, stats = full_family(17)
    em = ResultsEmitter(experiment="FIXTURE")
    em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    em.build()
    return "built with 17 confirmatory"


def b3_hand_edited_alpha():
    specs, stats = full_family(16)
    em = ResultsEmitter(experiment="FIXTURE")
    em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    # Hand-edit one statistic's alpha_applied after the fact, exactly as a
    # careless re-analysis at a different threshold would.
    em.statistics[7]["alpha_applied"] = 0.05 / 7
    em.build()
    return "built with a mismatched alpha_applied"


def b4_paired_b10():
    floor = min_attainable_p("paired_exact", n_pairs=10)
    assert floor == 2 / 1024, floor
    specs, stats = full_family(16, b=10)
    em = ResultsEmitter(experiment="FIXTURE")
    rec = em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    em.build()
    return (
        f"floor={floor!r} < alpha={ALPHA!r} -> decidable; "
        f"ceiling={ceiling_pairs(10, ALPHA)} pair(s), "
        f"discordance tolerance={discordance_tolerance(10, ALPHA)}; verdict={rec['verdict']}"
    )


def b5_paired_b5():
    floor = min_attainable_p("paired_exact", n_pairs=5)
    assert floor == 0.0625, floor
    specs, stats = full_family(16, b=5)
    em = ResultsEmitter(experiment="FIXTURE")
    em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    em.build()
    return "built with an undecidable B=5 family"


def b6_monte_carlo_1000():
    floor = min_attainable_p("monte_carlo", n_permutations=1000)
    specs = [
        {"id": f"MC{i}", "permutation_mode": "monte_carlo", "n_permutations": 1000}
        for i in range(16)
    ]
    stats = []
    for i in range(16):
        stats.append(
            {
                "id": f"MC{i}",
                "kind": "permutation",
                "permutation_mode": "monte_carlo",
                "n_permutations": 1000,
                "n1_realised": 20,
                "n2_realised": 20,
                "p": 0.01,
                "confirmatory": True,
                "significant": False,
            }
        )
    em = ResultsEmitter(experiment="FIXTURE")
    rec = em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    em.build()
    return f"floor={floor!r} < alpha={ALPHA!r}; verdict={rec['verdict']}"


def b7_realised_degraded():
    specs, stats = full_family(16, b=16)
    # One contrast degrades from 16 usable pairs to 5 through null batches.
    stats[3] = paired_stat("T3", b_planned=16, b_realised=5)
    stats[3]["significant"] = False  # what a naive emitter would have written
    em = ResultsEmitter(experiment="FIXTURE")
    em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    doc = em.build()
    degraded = next(s for s in doc["statistics"] if s["id"] == "T3")
    assert degraded["status"] == UNDECIDABLE, degraded["status"]
    assert degraded["significant"] is None, degraded["significant"]
    assert degraded["min_attainable_p_realised"] == 0.0625
    healthy = next(s for s in doc["statistics"] if s["id"] == "T0")
    assert healthy["status"] == "ok"
    return (
        f"T3 status={degraded['status']}, significant={degraded['significant']!r}, "
        f"realised floor={degraded['min_attainable_p_realised']!r}; "
        f"others unaffected (T0 status={healthy['status']})"
    )


def b8_not_applicable_slot():
    specs = [paired_spec(f"T{i}") for i in range(15)]
    specs.append({"id": "X3.frontier", "permutation_mode": "not_applicable"})
    stats = [paired_stat(f"T{i}") for i in range(15)]
    stats.append(
        not_applicable_slot("X3.frontier", "frontier API has no precision factor")
    )
    em = ResultsEmitter(experiment="FIXTURE")
    rec = em.declare_confirmatory_design(specs)
    for s in stats:
        em.add_statistic(s)
    doc = em.build()
    n_conf = sum(1 for s in doc["statistics"] if s.get("confirmatory"))
    assert n_conf == 16, n_conf
    na = next(s for s in doc["statistics"] if s["id"] == "X3.frontier")
    assert na["p"] is None and na["significant"] is None
    exempt = [r for r in rec["per_test"] if r["exempt"]]
    return (
        f"confirmatory count={n_conf}, slot p={na['p']!r}, "
        f"exempt-from-floor entries={len(exempt)}"
    )


FIXTURES = [
    ("B1  family of 15", "abort [G-family]", b1_family_15),
    ("B2  family of 17", "abort [G-family]", b2_family_17),
    ("B3  hand-edited alpha_applied", "abort [G-alpha]", b3_hand_edited_alpha),
    ("B4  paired contrast at B=10", "no abort", b4_paired_b10),
    ("B5  paired contrast at B=5", "abort [G-discreteness]", b5_paired_b5),
    ("B6  Monte Carlo at N=1000", "no abort", b6_monte_carlo_1000),
    ("B7  realised B degraded 16->5", "no abort", b7_realised_degraded),
    ("B8  not_applicable slot", "no abort", b8_not_applicable_slot),
]


def main() -> int:
    for name, expected, fn in FIXTURES:
        run_fixture(name, expected, fn)

    width = max(len(r["fixture"]) for r in RESULTS)
    print(f"{'FIXTURE'.ljust(width)}  {'EXPECTED':<24} {'ACTUAL':<24} OK")
    print("-" * (width + 60))
    for r in RESULTS:
        flag = "yes" if r["match"] else "NO  <-- FINDING"
        print(f"{r['fixture'].ljust(width)}  {r['expected']:<24} {r['actual']:<24} {flag}")
    print()
    for r in RESULTS:
        if r["detail"]:
            print(f"  {r['fixture']}: {r['detail']}")

    print()
    print("Ceiling table (plan §2.3), recomputed here:")
    print(f"  {'B':>3} {'2^B':>8} {'ceiling(pairs)':>15} {'min_p':>13} {'k_max':>6}")
    for b in (10, 12, 14, 16):
        print(
            f"  {b:>3} {2**b:>8} {ceiling_pairs(b, ALPHA):>15} "
            f"{min_attainable_p('paired_exact', n_pairs=b):>13.9f} "
            f"{discordance_tolerance(b, ALPHA):>6}"
        )

    failed = [r for r in RESULTS if not r["match"]]
    print()
    print(f"{len(RESULTS) - len(failed)}/{len(RESULTS)} fixtures behaved as required.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
