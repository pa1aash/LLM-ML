"""E2 power pilot — sets R_final (plan 3.4).

PILOT ONLY. Simulation over synthetic draws. No model is called, nothing is
trained, and the output sets a design parameter and nothing else: it is
quarantined from analysis and never enters the confirmatory corpus.

TWO SUBSTRATES.

  default        SIMULATED -- Beta(8,2) scaled to [0.10, 0.74], the pool used at
                 S3c when the benchmark tables were absent from the repository.
                 Reproduces the record revision 6 cites, byte for byte.

  --table PATH   THE REAL TABLE. NATS-Bench topology search space, 15,625
                 architectures, validation and test accuracy by lookup. Closes
                 S3C-01. See DEVIATIONS.md D-012 for the arm model: a run is 20
                 proposals drawn from the table, selection is by validation
                 accuracy with the registered lowest-index tie rule (plan 3.4),
                 the outcome is the selected architecture's test accuracy, and
                 the treated arm differs by drawing from the top-f fraction of
                 the table by validation accuracy, with f calibrated to the
                 registered MDE of Cliff's delta = 0.62.

PILOT ONLY under either substrate. Simulation over draws; no model is called and
nothing is trained. The output sets a design parameter and nothing else: it is
quarantined from analysis and never enters the confirmatory corpus.
"""

from __future__ import annotations

import argparse
import json
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
R_GRID = (20, 22, 24, 26, 28, 30, 34, 38, 44, 50)


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


class TableSubstrate:
    """Pure table sampling from the real benchmark (D-012).

    Nothing here is simulated: every draw is an architecture that exists, and
    every accuracy is a lookup. The one free parameter is `f`, the fraction of
    the table an arm proposes from, ranked by validation accuracy -- which is
    what differs between two search arms.
    """

    def __init__(self, path: Path, task: str):
        doc = json.loads(Path(path).read_text())
        self.task = task
        self.valid = np.asarray(doc["tasks"][task]["valid"], dtype=float)
        self.test = np.asarray(doc["tasks"][task]["test"], dtype=float)
        self.n = int(self.valid.size)
        self.source = doc.get("source")
        # Descending validation accuracy; `stable` keeps ties in benchmark-index
        # order so the top-f pool is deterministic.
        self.rank = np.argsort(-self.valid, kind="stable")

    def run_outcomes(self, gen, n_runs: int, f: float) -> np.ndarray:
        k = max(1, int(round(f * self.n)))
        pool = self.rank[:k]
        idx = gen.choice(pool, size=(n_runs, K_PROPOSALS), replace=True)
        # Sorting the proposals by benchmark index makes argmax return the
        # LOWEST-index architecture among validation ties -- plan 3.4's
        # registered tie-break (D-20), not numpy's incidental behaviour.
        idx = np.sort(idx, axis=1)
        sel = np.argmax(self.valid[idx], axis=1)
        return self.test[idx[np.arange(n_runs), sel]]


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


def calibrate_fraction(sub: TableSubstrate, target: float, gen) -> tuple[float, float]:
    """Find the top-fraction f whose run outcomes sit at Cliff's delta ~= target
    against the whole-table arm. delta decreases as f grows."""
    # 4,000 runs per side at every step: at 800 the sampling noise in delta
    # dominates the late bisection steps and the calibrated f lands short of the
    # target, which would understate power.
    lo, hi = 1e-4, 1.0
    for _ in range(24):
        mid = (lo + hi) / 2
        d = delta_np(sub.run_outcomes(gen, 4000, mid), sub.run_outcomes(gen, 4000, 1.0))
        if d > target:
            lo = mid
        else:
            hi = mid
    f = (lo + hi) / 2
    d = delta_np(sub.run_outcomes(gen, 20000, f), sub.run_outcomes(gen, 20000, 1.0))
    return f, d


def power_at_table(sub: TableSubstrate, r: int, f: float, gen) -> float:
    hits = 0
    for _ in range(N_SIM):
        a = sub.run_outcomes(gen, r, f)
        b = sub.run_outcomes(gen, r, 1.0)
        if perm_p_batch(a, b, gen, N_PERM) < K.ALPHA:
            hits += 1
    return hits / N_SIM


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


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--table", type=Path, default=None,
                    help="path to the real NATS-Bench accuracy table (S3C-01)")
    ap.add_argument("--task", default="cifar100",
                    help="primary task; plan 3.1 fixes CIFAR-100")
    ap.add_argument("--secondary", action="store_true",
                    help="also sweep the two secondary tasks on a coarse grid")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)

    return main_table(args) if args.table else main_simulated(args)


def main_simulated(args) -> int:
    gen = np.random.default_rng(SEED)
    print("E2 POWER PILOT  (plan 3.4 / 3.5)  --  SIMULATED POOL")
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
    for r in R_GRID:
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
    dest = args.out or (ROOT / "results" / "pilots" / "power_e2.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  written: {_rel(dest)}")
    return 0


def main_table(args) -> int:
    """S3C-01, closed: the same pilot against the real benchmark table."""
    gen = np.random.default_rng(SEED)
    sub = TableSubstrate(args.table, args.task)
    print("E2 POWER PILOT  (plan 3.4 / 3.5)  --  REAL TABLE  [S3C-01, D-012]")
    print(f"  table          = {args.table}")
    print(f"  source         = {sub.source}")
    print(f"  primary task   = {args.task}   ({sub.n} architectures)")
    print(f"  ALPHA          = {K.ALPHA!r}   (0.05/{K.FAMILY_SIZE})")
    print(f"  statistic      = difference of sample means, two-sided (plan 3.4)")
    print(f"  selection      = validation accuracy, lowest benchmark index on a "
          f"tie (plan 3.4 D-20)")
    print(f"  outcome        = TEST accuracy of the selected architecture")
    print(f"  arm model      = treated arm proposes from the top-f fraction by "
          f"validation accuracy (D-012)")
    print(f"  target         = power >= {TARGET_POWER} at |delta| >= {TARGET_DELTA}")
    print(f"  k per run      = {K_PROPOSALS}")
    print(f"  seed           = {SEED}, {N_SIM} sims x {N_PERM} permutations\n")

    null_runs = sub.run_outcomes(gen, 20000, 1.0)
    print(f"  null-arm run outcome: mean {null_runs.mean():.3f}  "
          f"sd {null_runs.std(ddof=1):.3f}  "
          f"min {null_runs.min():.3f}  max {null_runs.max():.3f}")

    f, achieved = calibrate_fraction(sub, TARGET_DELTA, gen)
    treated = sub.run_outcomes(gen, 20000, f)
    print(f"  calibrated top-fraction f = {f:.6f} "
          f"({max(1, int(round(f * sub.n)))} architectures) "
          f"-> Cliff's delta = {achieved:.4f}")
    print(f"  treated-arm run outcome: mean {treated.mean():.3f}  "
          f"sd {treated.std(ddof=1):.3f}\n")

    print(f"  {'R':>4} {'power':>8}  {'meets 0.80':>11}")
    curve = []
    chosen = None
    for r in R_GRID:
        p = power_at_table(sub, r, f, gen)
        curve.append({"R": r, "power": p})
        mark = "yes" if p >= TARGET_POWER else ""
        print(f"  {r:>4} {p:>8.3f}  {mark:>11}")
        if chosen is None and p >= TARGET_POWER:
            chosen = r
    print()

    # Plan 3.4: R_final is fixed once, and a pilot may raise it but never lower
    # it. The registered value is K.R_FINAL; the floor is K.R_FLOOR.
    needed = chosen if chosen else max(c["R"] for c in curve)
    moves = needed > K.R_FINAL
    r_final = max(K.R_FLOOR, K.R_FINAL, needed)
    print(f"  smallest R meeting the target : {chosen}")
    print(f"  R_FLOOR (plan 3.4)            : {K.R_FLOOR}")
    print(f"  R_FINAL registered at rev 6   : {K.R_FINAL}")
    print(f"  R_final after this pilot      : {r_final}"
          f"{'   *** MOVED — log before any E2 run ***' if moves else '   (unchanged)'}")

    secondary = {}
    if args.secondary:
        for task in ("cifar10", "ImageNet16-120"):
            sub2 = TableSubstrate(args.table, task)
            f2, d2 = calibrate_fraction(sub2, TARGET_DELTA, gen)
            rows = []
            print(f"\n  secondary task {task}: f = {f2:.6f}, delta = {d2:.4f}")
            for r in (20, 24, 28, 34):
                p = power_at_table(sub2, r, f2, gen)
                rows.append({"R": r, "power": p})
                print(f"  {r:>4} {p:>8.3f}")
            secondary[task] = {"calibrated_fraction": f2, "achieved_delta": d2,
                               "curve": rows}

    out = {
        "pilot": True, "confirmatory": False, "quarantined_from_analysis": True,
        "name": "power_e2_real_table", "generated_by": "scripts/power_e2.py --table",
        "closes": "S3C-01", "deviation": "DEVIATIONS.md D-012",
        "plan_sha256": K.PLAN_SHA256, "alpha": K.ALPHA,
        "seed": SEED, "n_sim": N_SIM, "n_perm": N_PERM,
        "test_statistic": "difference_of_means",
        "target_delta": TARGET_DELTA, "target_power": TARGET_POWER,
        "substrate": {
            "kind": "REAL TABLE — pure table sampling",
            "table": str(args.table),
            "source": sub.source,
            "n_architectures": sub.n,
            "primary_task": args.task,
            "k_proposals_per_run": K_PROPOSALS,
            "selection": "validation accuracy; lowest benchmark index on a tie",
            "outcome": "test accuracy of the selected architecture",
            "arm_model": "treated arm draws from the top-f fraction by "
                         "validation accuracy; f calibrated to the registered MDE",
        },
        "null_arm": {"mean": float(null_runs.mean()),
                     "sd": float(null_runs.std(ddof=1)),
                     "min": float(null_runs.min()),
                     "max": float(null_runs.max())},
        "treated_arm": {"mean": float(treated.mean()),
                        "sd": float(treated.std(ddof=1))},
        "calibrated_fraction": f, "achieved_delta": achieved,
        "curve": curve, "smallest_R_meeting_target": chosen,
        "R_floor": K.R_FLOOR, "R_final_registered": K.R_FINAL,
        "R_final": r_final, "R_final_moves": moves,
        "secondary_tasks": secondary,
    }
    dest = args.out or (ROOT / "results" / "pilots" / "power_e2_real_table.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  written: {_rel(dest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
