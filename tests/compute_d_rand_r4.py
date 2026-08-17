"""R4-3 — D_rand from a CORRECTED uniform sampler, plus D_repo_sampler.

R3 §2.6 called the repository's sampler "uniform" and anchored the six
classification thresholds on ~0.74. S3a showed neither holds (defects D-09,
D-10, D-13). This computes:

  D_rand            — a corrected uniform draw over the DECLARED search space,
                      at fixed block count, which is what the thresholds anchor to
  D_rand_pooled     — the same corrected sampler with block count free, for
                      comparison only
  D_repo_sampler    — the repository's own sampler, reported separately so the
                      original paper's random arm stays comparable

No model of any kind is involved.
"""

from __future__ import annotations

import json
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.metrics import batch_diversity  # noqa: E402
from emit.sampler import extract_sampler, sample_batches, source_sha256  # noqa: E402

BLOCK_COUNTS = (3, 4, 5, 6)
N_BATCHES = K.N_BATCHES_PER_CELL          # 16
N_PER_BATCH = K.N_GENERATIONS_PER_BATCH   # 20
SEED = K.D_RAND_SEED                      # 20260817


def uniform_arch(rng: random.Random, n_blocks: int) -> dict:
    """Genuinely uniform over the declared vocabulary of every field.

    Differs from the repository sampler in exactly two ways, both of which S3a
    identified as defects in calling that sampler uniform:
      1. `pooling` is drawn uniformly over ALL FOUR declared values, including
         "none" at 25% (the repository sampler forces "none" on non-pool blocks
         and draws from only three values elsewhere -> 48.21% none).
      2. block count is a parameter here, not a draw, so the 6*|Kx-Ky| term is
         never exercised.
    `dropout` is sampled but excluded from the design-choice vector by §2.4.1.
    """
    return {
        "blocks": [
            {f: rng.choice(K.FIELD_VOCAB[f]) for f in K.PER_BLOCK_FIELDS}
            for _ in range(n_blocks)
        ],
        "global_pool": rng.choice(["avg", "max"]),
        "fc_layers": rng.choice([1, 2]),
    }


def analytic_fixed_k(n_blocks: int) -> float:
    """E[d] for two independent uniform draws at fixed block count.

    Per-block expected mismatches = sum over the six fields of (1 - 1/|vocab|):
      conv 3/4, channels 3/4, activation 3/4, normalization 3/4,
      skip 2/3, pooling 3/4  ->  53/12 per block
    Arch-level: global_pool 1/2 + fc_layers 1/2 = 1.
    Denominator: 6*K + 2.
    """
    per_block = sum(1 - 1 / len(K.FIELD_VOCAB[f]) for f in K.PER_BLOCK_FIELDS)
    return (per_block * n_blocks + 1.0) / (6 * n_blocks + 2)


def measure(sampler_fn, label: str) -> dict:
    batches = [
        [sampler_fn(random.Random(SEED + b)) for _ in range(N_PER_BATCH)]
        for b in range(N_BATCHES)
    ]
    # one Random per batch, drawn fresh so the stream is reproducible per batch
    batches = []
    for b in range(N_BATCHES):
        rng = random.Random(SEED + b)
        batches.append([sampler_fn(rng) for _ in range(N_PER_BATCH)])
    per_batch = [batch_diversity(x) for x in batches]
    flat = [c for x in batches for c in x]
    return {
        "label": label,
        "batch_mean": statistics.fmean(per_batch),
        "batch_std": statistics.stdev(per_batch),
        "pooled": batch_diversity(flat),
        "min": min(per_batch),
        "max": max(per_batch),
        "per_batch": per_batch,
    }


def main() -> int:
    print("R4-3  D_rand from a corrected uniform sampler")
    print(f"      seed={SEED}, structure={N_BATCHES} x {N_PER_BATCH}\n")

    # ---------------------------------------------- corrected uniform, fixed K
    fixed = {}
    print("A. CORRECTED UNIFORM, block count FIXED  <- the registered anchor")
    print(f"   {'K':>3} {'analytic':>10} {'measured':>10} {'batch std':>10} {'pooled':>10}")
    for k in BLOCK_COUNTS:
        m = measure(lambda r, k=k: uniform_arch(r, k), f"uniform_K{k}")
        fixed[k] = m
        print(f"   {k:>3} {analytic_fixed_k(k):>10.6f} {m['batch_mean']:>10.6f} "
              f"{m['batch_std']:>10.6f} {m['pooled']:>10.6f}")
    d_rand = statistics.fmean([fixed[k]["batch_mean"] for k in BLOCK_COUNTS])
    d_rand_std = statistics.fmean([fixed[k]["batch_std"] for k in BLOCK_COUNTS])
    analytic_mean = statistics.fmean([analytic_fixed_k(k) for k in BLOCK_COUNTS])
    print(f"   {'mean':>3} {analytic_mean:>10.6f} {d_rand:>10.6f} {d_rand_std:>10.6f}")
    print(f"   -> D_rand (registered) = {d_rand:.6f}")
    print(f"      analytic agreement  = {abs(d_rand - analytic_mean):.6f}\n")

    # ------------------------------------------ corrected uniform, K free
    def uniform_free(rng):
        return uniform_arch(rng, rng.choice(list(BLOCK_COUNTS)))
    freed = measure(uniform_free, "uniform_Kfree")
    print("B. CORRECTED UNIFORM, block count FREE  (comparison only)")
    print(f"   batch mean = {freed['batch_mean']:.6f}, pooled = {freed['pooled']:.6f}")
    print(f"   inflation over the fixed-K anchor = "
          f"{freed['batch_mean'] - d_rand:+.6f} "
          f"({(freed['batch_mean'] / d_rand - 1):+.2%})\n")

    # ------------------------------------------------- the repository's sampler
    repo_batches = sample_batches(N_BATCHES, N_PER_BATCH, SEED)
    repo_per_batch = [batch_diversity(b) for b in repo_batches]
    repo_flat = [c for b in repo_batches for c in b]
    d_repo = statistics.fmean(repo_per_batch)
    _, _, extracted, extract_digest = extract_sampler()

    counts: dict[int, int] = {}
    pooling: dict[str, int] = {}
    for c in repo_flat:
        counts[len(c["blocks"])] = counts.get(len(c["blocks"]), 0) + 1
        for b in c["blocks"]:
            pooling[b["pooling"]] = pooling.get(b["pooling"], 0) + 1
    tot_pool = sum(pooling.values())

    print("C. THE REPOSITORY'S OWN SAMPLER  -> D_repo_sampler (reported, NOT the anchor)")
    print(f"   batch mean = {d_repo:.6f}, batch std = {statistics.stdev(repo_per_batch):.6f}, "
          f"pooled = {batch_diversity(repo_flat):.6f}")
    print(f"   excess over D_rand = {d_repo - d_rand:+.6f} ({(d_repo/d_rand - 1):+.2%})")
    print(f"   pooling distribution: " +
          ", ".join(f"{k}={pooling[k]/tot_pool:.2%}" for k in sorted(pooling, key=lambda x: -pooling[x])))
    print(f"   num_blocks distribution: " +
          ", ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
    fixed_k_repo = {
        k: batch_diversity([c for c in repo_flat if len(c["blocks"]) == k])
        for k in sorted(counts) if counts[k] > 1
    }
    print(f"   repo sampler at fixed K: " +
          ", ".join(f"K={k}:{v:.4f}" for k, v in fixed_k_repo.items()))
    print()

    # --------------------------------------------------- the tightened range
    lo, hi = 0.705, 0.735
    print(f"D. TIGHTENED SANITY RANGE  [{lo}, {hi}]  (R3 had [0.65, 0.80])")
    checks = [
        ("D_rand, corrected uniform fixed-K (registered)", d_rand),
        ("corrected uniform, K free", freed["batch_mean"]),
        ("repository sampler (the R3 defect)", d_repo),
        ("R3's stated analytic anchor", 0.74),
    ]
    for name, v in checks:
        inside = lo <= v <= hi
        print(f"   {name:<48} {v:.6f}  {'INSIDE' if inside else 'OUTSIDE -> would halt'}")
    print(f"   -> the range now catches the repository sampler AND R3's own anchor,")
    print(f"      both of which R3's [0.65, 0.80] admitted.\n")

    # ------------------------------------------------------------- thresholds
    print("E. THE SIX THRESHOLD CONSTANTS, anchored to the fixed-K uniform D_rand")
    rows = [
        ("collapsed", "D < 0.15*D_rand", K.THRESHOLD_COLLAPSED * d_rand),
        ("reduced/partial (level) lower", "D >= 0.15*D_rand", K.THRESHOLD_COLLAPSED * d_rand),
        ("diverse", "D >= 0.60*D_rand", K.THRESHOLD_DIVERSE * d_rand),
        ("no chg", "|dD| < 0.10*D_rand", K.THRESHOLD_NO_CHANGE * d_rand),
        ("partial / worsens (change)", "0.10*D_rand <= |dD| < 0.25*D_rand", K.THRESHOLD_NO_CHANGE * d_rand),
        ("recovers", "dD >= 0.25*D_rand", K.THRESHOLD_RECOVERS * d_rand),
    ]
    for name, rule, val in rows:
        print(f"   {name:<30} {rule:<38} {val:.6f}")
    print()

    out = {
        "generated_by": "tests/compute_d_rand_r4.py",
        "plan_revision": 4,
        "seed": SEED,
        "structure": {"n_batches": N_BATCHES, "n_per_batch": N_PER_BATCH},
        "D_rand": {
            "value": d_rand,
            "definition": "corrected uniform sampler, block count FIXED, mean over K in {3,4,5,6}",
            "per_block_count": {str(k): fixed[k]["batch_mean"] for k in BLOCK_COUNTS},
            "analytic": {str(k): analytic_fixed_k(k) for k in BLOCK_COUNTS},
            "analytic_mean": analytic_mean,
            "mean_batch_std": d_rand_std,
        },
        "D_rand_block_free": {
            "value": freed["batch_mean"],
            "note": "comparison only; block-count variation inflates d via the 6*|Kx-Ky| term",
        },
        "D_repo_sampler": {
            "value": d_repo,
            "pooled": batch_diversity(repo_flat),
            "batch_std": statistics.stdev(repo_per_batch),
            "fixed_k": {str(k): v for k, v in fixed_k_repo.items()},
            "pooling_distribution": pooling,
            "num_blocks_distribution": {str(k): v for k, v in sorted(counts.items())},
            "note": "reported for comparability with the original paper's random arm; NOT the anchor",
            "sampler_file_sha256": source_sha256(),
            "sampler_extract_sha256": extract_digest,
            "sampler_extract_bytes": len(extracted),
            "extraction_method": "ast source extraction; search_space.py imports torch at module level (D-11)",
        },
        "sanity_range": [lo, hi],
        "thresholds": {
            "collapsed_below": K.THRESHOLD_COLLAPSED * d_rand,
            "diverse_at_or_above": K.THRESHOLD_DIVERSE * d_rand,
            "no_change_band": K.THRESHOLD_NO_CHANGE * d_rand,
            "partial_change_lower": K.THRESHOLD_NO_CHANGE * d_rand,
            "recovers_at_or_above": K.THRESHOLD_RECOVERS * d_rand,
        },
    }
    for dest in (ROOT / "results" / "E1_reference.json",
                 ROOT / "audit" / "E1_reference_R4.json"):
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(json.dumps(out, indent=2) + "\n")
        print(f"written: {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
