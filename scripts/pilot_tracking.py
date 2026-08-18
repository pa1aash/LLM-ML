"""Anchor-tracking width pilot -- sets B_tracking (plan 2.8).

PILOT ONLY. Simulation over synthetic draws. No model, no training. The output
sets a design parameter and nothing else: quarantined from analysis, never in the
confirmatory corpus.

THE REGISTERED CRITERION IS MISCALIBRATED AND IS CORRECTED HERE.

Plan revision 5 2.8 asks for "the smallest batch count whose 95% interval
half-width at a true rate of 0.40 is below 0.15". That yields [0.25, 0.55] --
which CONTAINS the field-weighted chance rate 0.263889, so the registered
one-sided rule (2.6) reads it as `no tracking`. **The criterion would certify a
width that cannot detect the effect the column exists to detect.**

Corrected, and this is what is simulated:

    B_tracking = the smallest B >= 16 at which the BCa lower bound EXCEEDS the
    field-weighted chance rate, at a simulated true tracking rate of 0.40, in
    >= 0.80 of simulated cells.

Both quantities are simulated separately and will not agree: `tracks_first` runs
over up to six fields, `tracks_exemplar` over at most three, so the latter's
per-batch proportion is confined to {0, 1/3, 2/3, 1}. B_tracking is set from the
binding one.
"""

from __future__ import annotations

import json
import random
import sys

import numpy as np
from scipy.stats import norm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.anchor import EXEMPLAR_FIELDS, chance_rate  # noqa: E402

SEED = 20260818
N_CELLS = 400            # simulated cells per B
N_BOOT = 2000            # bootstrap resamples per cell (pilot; production 10,000)
# Vectorised with numpy. The BCa below is the same estimator as
# src/emit/anchor._bca, which the unit fixtures pin; it is reimplemented here
# only so 400 cells x 10 batch counts x 2 quantities finishes in seconds.
TRUE_RATE = 0.40
TARGET_COVERAGE = 0.80
P_FIELD_COLLAPSED = 0.80  # post-repair schema cells collapse most fields
B_GRID = (16, 18, 20, 22, 24, 28, 32, 40, 48, 64)


def bca_lower(vals: np.ndarray, gen) -> float:
    """BCa 95% lower bound on the mean -- same estimator as emit.anchor._bca."""
    n = vals.size
    point = vals.mean()
    if n < 2:
        return point
    idx = gen.integers(0, n, size=(N_BOOT, n))
    boots = np.sort(vals[idx].mean(axis=1))
    n_less = int((boots < point).sum())
    if n_less in (0, N_BOOT):
        return float(boots[int(0.025 * (N_BOOT - 1))])
    z0 = norm.ppf(n_less / N_BOOT)
    total = vals.sum()
    jack = (total - vals) / (n - 1)
    jbar = jack.mean()
    num = ((jbar - jack) ** 3).sum()
    den = 6.0 * (((jbar - jack) ** 2).sum() ** 1.5)
    a = num / den if den != 0 else 0.0
    z = norm.ppf(0.025)
    adj = z0 + (z0 + z) / (1 - a * (z0 + z))
    q = min(max(float(norm.cdf(adj)), 0.0), 1.0)
    return float(boots[min(int(q * (N_BOOT - 1)), N_BOOT - 1)])


def coverage_cross_level(b: int, seed: int) -> tuple[float, float]:
    """Coverage for the cross-level exemplar delta (plan 2.5a).

    Null is EXACTLY 0 -- a modal that does not move with the exemplar gives
    delta = 0 identically -- so the target is simply BCa lower bound > 0.
    Simulated at the same true response rate as the other two quantities.
    """
    gen = np.random.default_rng(seed)
    nf = len(EXEMPLAR_FIELDS)
    hits, los, used = 0, [], 0
    for _ in range(N_CELLS):
        coll = gen.random((b, nf)) < P_FIELD_COLLAPSED
        # In each cell the modal follows the exemplar shown there with prob
        # TRUE_RATE; otherwise it lands on some other vocabulary value, which
        # coincides with the OTHER cell's exemplar only by chance (1/3 of the
        # three remaining values for a 4-value field).
        own_m = (gen.random((b, nf)) < TRUE_RATE) & coll
        own_n = (gen.random((b, nf)) < TRUE_RATE) & coll
        oth_m = (~own_m) & coll & (gen.random((b, nf)) < 1.0 / 3.0)
        oth_n = (~own_n) & coll & (gen.random((b, nf)) < 1.0 / 3.0)
        n_used = coll.sum(axis=1) * 2
        keep = n_used > 0
        if keep.sum() < 2:
            continue
        own = (own_m.sum(axis=1) + own_n.sum(axis=1))[keep]
        oth = (oth_m.sum(axis=1) + oth_n.sum(axis=1))[keep]
        deltas = (own - oth) / n_used[keep]
        lo = bca_lower(deltas.astype(float), gen)
        used += 1
        los.append(lo)
        if lo > 0.0:
            hits += 1
    if used == 0:
        return 0.0, float("nan")
    return hits / used, float(np.mean(los))


def coverage_at(b: int, quantity: str, seed: int) -> tuple[float, float, float]:
    """Fraction of simulated cells whose BCa lower bound clears the chance rate."""
    gen = np.random.default_rng(seed)
    fields = list(K.PER_BLOCK_FIELDS) if quantity == "tracks_first" else list(EXEMPLAR_FIELDS)
    nf = len(fields)
    inv = np.array([1.0 / len(K.FIELD_VOCAB[f]) for f in fields])

    hits, los, rates, used = 0, [], [], 0
    for _ in range(N_CELLS):
        coll = gen.random((b, nf)) < P_FIELD_COLLAPSED        # which fields collapsed
        hit = (gen.random((b, nf)) < TRUE_RATE) & coll        # which of those track
        ncol = coll.sum(axis=1)
        keep = ncol > 0                                       # plan 2.4.7
        if keep.sum() < 2:
            continue
        props = hit.sum(axis=1)[keep] / ncol[keep]
        cr = float((coll[keep] * inv).sum() / ncol[keep].sum())
        lo = bca_lower(props.astype(float), gen)
        used += 1
        los.append(lo); rates.append(cr)
        if lo > cr:
            hits += 1
    if used == 0:
        return 0.0, float("nan"), float("nan")
    return hits / used, float(np.mean(los)), float(np.mean(rates))


def main() -> int:
    print("ANCHOR-TRACKING WIDTH PILOT  (plan 2.8, criterion CORRECTED)")
    print(f"  true tracking rate simulated : {TRUE_RATE}")
    print(f"  per-field collapse prob      : {P_FIELD_COLLAPSED}")
    print(f"  target                       : BCa lower bound > chance in "
          f">= {TARGET_COVERAGE:.0%} of cells")
    print(f"  chance, all six fields       : {chance_rate(list(K.PER_BLOCK_FIELDS)):.6f}")
    print(f"  chance, three exemplar fields: {chance_rate(list(EXEMPLAR_FIELDS)):.6f}")
    print(f"  seed {SEED}, {N_CELLS} cells/B, {N_BOOT} bootstrap resamples\n")

    print("  REJECTED registered criterion (half-width < 0.15 at rate 0.40):")
    print("    interval [0.25, 0.55] CONTAINS chance 0.263889 -> reads `no tracking`.")
    print("    A width certified by that rule cannot detect the effect.\n")

    print(f"  {'B':>4} | {'tracks_first':>19} | {'tracks_exemplar':>19} | "
          f"{'cross-level delta':>19}")
    print(f"  {'':>4} | {'coverage':>9} {'meets':>8} | {'coverage':>9} {'meets':>8} "
          f"| {'coverage':>9} {'meets':>8}")
    curve = []
    first_ok = exemplar_ok = cross_ok = None
    for b in B_GRID:
        cf, lof, crf = coverage_at(b, "tracks_first", SEED + b)
        ce, loe, cre = coverage_at(b, "tracks_exemplar", SEED + 1000 + b)
        cx, lox = coverage_cross_level(b, SEED + 2000 + b)
        curve.append({"B": b,
                      "tracks_first": {"coverage": cf, "mean_lower_bound": lof,
                                       "mean_chance": crf},
                      "tracks_exemplar": {"coverage": ce, "mean_lower_bound": loe,
                                          "mean_chance": cre},
                      "cross_level_exemplar": {"coverage": cx,
                                               "mean_lower_bound": lox,
                                               "mean_chance": 0.0}})
        mk = lambda c: "yes" if c >= TARGET_COVERAGE else ""
        print(f"  {b:>4} | {cf:>9.3f} {mk(cf):>8} | {ce:>9.3f} {mk(ce):>8} "
              f"| {cx:>9.3f} {mk(cx):>8}")
        if first_ok is None and cf >= TARGET_COVERAGE:
            first_ok = b
        if exemplar_ok is None and ce >= TARGET_COVERAGE:
            exemplar_ok = b
        if cross_ok is None and cx >= TARGET_COVERAGE:
            cross_ok = b
    print()
    print(f"  smallest B for tracks_first            : {first_ok}")
    print(f"  smallest B for tracks_exemplar (single): {exemplar_ok}")
    print(f"  smallest B for cross-level delta       : {cross_ok}")
    print()
    print("  At revision 6 the RIVAL PREDICATES read tracks_first and the")
    print("  cross-level delta. Single-cell tracks_exemplar is reported but no")
    print("  predicate reads it, so it does not bind B_tracking.")

    binding_set = {"tracks_first": first_ok, "cross_level_exemplar": cross_ok}
    live = {k: v for k, v in binding_set.items() if v is not None}
    if len(live) < len(binding_set):
        missing = [k for k, v in binding_set.items() if v is None]
        b_needed, binding = max(B_GRID), ",".join(missing)
        note = f"{binding} did not reach {TARGET_COVERAGE:.0%} up to B={max(B_GRID)}"
    else:
        binding = max(live, key=live.get)
        b_needed = live[binding]
        note = (f"binding quantity is {binding}; single-cell tracks_exemplar would "
                f"have needed B={exemplar_ok} but no predicate reads it")
    b_final = max(K.B_TRACKING_FLOOR, b_needed)
    print(f"  {note}")
    print(f"  B_TRACKING_FLOOR (plan 2.8)    : {K.B_TRACKING_FLOOR}")
    print(f"  B_tracking = max(floor, pilot) : {b_final}")

    out = {
        "pilot": True, "confirmatory": False, "quarantined_from_analysis": True,
        "name": "pilot_tracking", "generated_by": "scripts/pilot_tracking.py",
        "plan_sha256": K.PLAN_SHA256, "seed": SEED,
        "n_cells_per_B": N_CELLS, "n_boot": N_BOOT,
        "true_rate": TRUE_RATE, "target_coverage": TARGET_COVERAGE,
        "p_field_collapsed": P_FIELD_COLLAPSED,
        "rejected_criterion": "half-width < 0.15 at rate 0.40 -> [0.25,0.55] "
                              "contains chance 0.263889 -> reads `no tracking`",
        "corrected_criterion": "smallest B >= 16 with BCa lower bound > "
                               "field-weighted chance rate in >= 80% of cells",
        "curve": curve,
        "smallest_B_tracks_first": first_ok,
        "smallest_B_tracks_exemplar_single_cell": exemplar_ok,
        "smallest_B_cross_level_exemplar": cross_ok,
        "predicates_read": ["tracks_first", "cross_level_exemplar"],
        "binding_quantity": binding, "note": note,
        "B_tracking_floor": K.B_TRACKING_FLOOR, "B_tracking": b_final,
    }
    dest = ROOT / "results" / "pilots" / "pilot_tracking.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  written: {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
