"""E2 power pilot — sets R_final (plan 3.4).

PILOT ONLY. Simulation over synthetic draws. No model is called, nothing is
trained, and the output sets a design parameter and nothing else: it is
quarantined from analysis and never enters the confirmatory corpus.

SUBSTRATE CAVEAT, recorded rather than papered over. Plan 3.5 says the pilot
variance is "drawn from the benchmark's own best-of-20 distribution by pure table
sampling". **The NAS-Bench-201 tables are not present in this repository and
fetching them is outside a no-compute session.** The pool is therefore SIMULATED
with a shape chosen to mimic a tabular NAS benchmark's accuracy distribution --
bounded, left-skewed, dense near the top -- and the run outcome is the max of
k=20 draws, exactly as a run is defined. Recorded as S3C-01.

This weakens the calibration less than it might: the registered test statistic is
a difference of sample means over R runs, and the effect size is Cliff's delta, a
RANK statistic. Power at a fixed delta is driven by distributional overlap, which
the simulation controls directly by construction.
"""

from __future__ import annotations

import json
import random
import statistics
import sys

import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.stats import cliffs_delta  # noqa: E402

SEED = 20260818
N_SIM = 2000              # simulated experiments per R
N_PERM = 2000             # permutations per simulated experiment
# Vectorised with numpy; the permutation logic is identical to the scalar form
# in src/emit/stats.py, which the unit fixtures pin.
TARGET_DELTA = 0.62       # plan 3.5 MDE
TARGET_POWER = 0.80
K_PROPOSALS = K.E2_PROPOSALS_PER_RUN   # 20


def run_outcomes(gen, n: int, shift: float) -> np.ndarray:
    """n run outcomes. One run = best of k draws from the simulated pool.

    Beta(8, 2) scaled to [0.10, 0.74] -- bounded, left-skewed, dense near the
    top, which is the shape a NAS benchmark's accuracy table has. See the
    substrate caveat above.
    """
    pool = 0.10 + 0.64 * gen.beta(8.0, 2.0, size=(n, K_PROPOSALS))
    return (pool + shift).max(axis=1)


def delta_np(a: np.ndarray, b: np.ndarray) -> float:
    """Cliff's delta; ties contribute 0 to the numerator (plan 3.4)."""
    gt = (a[:, None] > b[None, :]).sum()
    lt = (a[:, None] < b[None, :]).sum()
    return float(gt - lt) / (a.size * b.size)


def perm_p_batch(a: np.ndarray, b: np.ndarray, gen, n_perm: int) -> float:
    """Two-sided Monte-Carlo permutation p on the DIFFERENCE OF SAMPLE MEANS
    (plan 3.4), with the standard (1 + #extreme)/(1 + N) estimator."""
    obs = abs(a.mean() - b.mean())
    pooled = np.concatenate([a, b])
    n1 = a.size
    idx = np.argsort(gen.random((n_perm, pooled.size)), axis=1)
    perm = pooled[idx]
    stat = np.abs(perm[:, :n1].mean(axis=1) - perm[:, n1:].mean(axis=1))
    return (1 + int((stat >= obs).sum())) / (1 + n_perm)


def calibrate_shift(target: float, gen) -> tuple[float, float]:
    """Find the pool shift giving Cliff's delta ~= target between run outcomes."""
    lo, hi = 0.0, 0.30
    for _ in range(30):
        mid = (lo + hi) / 2
        d = delta_np(run_outcomes(gen, 800, mid), run_outcomes(gen, 800, 0.0))
        if d < target:
            lo = mid
        else:
            hi = mid
    shift = (lo + hi) / 2
    d = delta_np(run_outcomes(gen, 4000, shift), run_outcomes(gen, 4000, 0.0))
    return shift, d


def power_at(r: int, shift: float, gen) -> float:
    hits = 0
    for _ in range(N_SIM):
        a = run_outcomes(gen, r, shift)
        b = run_outcomes(gen, r, 0.0)
        if perm_p_batch(a, b, gen, N_PERM) < K.ALPHA:
            hits += 1
    return hits / N_SIM


def main() -> int:
    gen = np.random.default_rng(SEED)
    print("E2 POWER PILOT  (plan 3.4 / 3.5)")
    print(f"  ALPHA          = {K.ALPHA!r}   (0.05/{K.FAMILY_SIZE})")
    print(f"  statistic      = difference of sample means, two-sided (plan 3.4)")
    print(f"  effect size    = Cliff's delta, ties 0 to delta / 0.5 to U")
    print(f"  target         = power >= {TARGET_POWER} at |delta| >= {TARGET_DELTA}")
    print(f"  k per run      = {K_PROPOSALS} (run outcome = best of k)")
    print(f"  seed           = {SEED}, {N_SIM} sims x {N_PERM} permutations\n")

    shift, achieved = calibrate_shift(TARGET_DELTA, gen)
    print(f"  calibrated pool shift = {shift:.6f} -> Cliff's delta = {achieved:.4f}\n")

    print(f"  {'R':>4} {'power':>8}  {'meets 0.80':>11}")
    curve = []
    chosen = None
    for r in (20, 22, 24, 26, 28, 30, 34, 38, 44, 50):
        p = power_at(r, shift, gen)
        curve.append({"R": r, "power": p})
        mark = "yes" if p >= TARGET_POWER else ""
        print(f"  {r:>4} {p:>8.3f}  {mark:>11}")
        if chosen is None and p >= TARGET_POWER:
            chosen = r
    print()

    r_final = max(K.R_FLOOR, chosen if chosen else max(c["R"] for c in curve))
    print(f"  smallest R meeting the target : {chosen}")
    print(f"  R_FLOOR (plan 3.4)            : {K.R_FLOOR}")
    print(f"  R_final = max(floor, pilot)   : {r_final}")
    if chosen is None:
        print("  WARNING: target not met inside the swept range")

    out = {
        "pilot": True, "confirmatory": False, "quarantined_from_analysis": True,
        "name": "power_e2", "generated_by": "scripts/power_e2.py",
        "plan_sha256": K.PLAN_SHA256, "alpha": K.ALPHA,
        "seed": SEED, "n_sim": N_SIM, "n_perm": N_PERM,
        "test_statistic": "difference_of_means",
        "target_delta": TARGET_DELTA, "target_power": TARGET_POWER,
        "calibrated_shift": shift, "achieved_delta": achieved,
        "substrate": "SIMULATED Beta(8,2) pool scaled to [0.10,0.74]; "
                     "NAS-Bench-201 tables absent from the repository (S3C-01)",
        "curve": curve, "smallest_R_meeting_target": chosen,
        "R_floor": K.R_FLOOR, "R_final": r_final,
    }
    dest = ROOT / "results" / "pilots" / "power_e2.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  written: {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
