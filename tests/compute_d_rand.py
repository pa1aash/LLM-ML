"""Block C6-C7 — D_rand and the model-free batch-variance probe.

D_rand is the reference the plan's six classification thresholds are fractions of
(§2.6). It comes from the repository's own uniform sampler and involves no model
of any kind.

C7 reports the across-batch standard deviation of D on those same random draws.
It is a MODEL-FREE reference point for how much batch-to-batch variability the
paired tests must tolerate. It is NOT a pilot of the model's behaviour and must
not be described as one: random architectures are the maximum-diversity case, and
LLM output will differ.
"""

from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emit import constants as K  # noqa: E402
from emit.metrics import batch_diversity, pooled_diversity  # noqa: E402
from emit.sampler import extract_sampler, sample_batches, sample_flat, source_sha256  # noqa: E402


def main() -> int:
    _, _, extracted, extract_digest = extract_sampler()

    print("PROVENANCE")
    print(f"  sampler source          : src/search_space.py")
    print(f"  whole-file sha256       : {source_sha256()}")
    print(f"  extracted-nodes sha256  : {extract_digest}")
    print(f"  extracted bytes         : {len(extracted)}")
    print(f"  registered D_rand seed  : {K.D_RAND_SEED}  (not specified by the plan)")
    print()

    # ---------------------------------------------------- C6a: the plan's literal
    flat = sample_flat(K.D_RAND_N_PLAN, K.D_RAND_SEED)
    d_rand_plan = pooled_diversity(flat)
    print(f"C6a  plan literal (§2.6): pooled D over C({K.D_RAND_N_PLAN},2) pairs")
    print(f"     D_rand = {d_rand_plan:.6f}")
    print()

    # ------------------------------- C6b: the E1 batch structure, 16 x 20 = 320
    batches = sample_batches(K.N_BATCHES_PER_CELL, K.N_GENERATIONS_PER_BATCH, K.D_RAND_SEED)
    per_batch = [batch_diversity(b) for b in batches]
    d_rand_batchmean = statistics.fmean(per_batch)
    d_rand_batchstd = statistics.stdev(per_batch)
    flat_320 = [cfg for b in batches for cfg in b]
    d_rand_pooled320 = pooled_diversity(flat_320)

    print(f"C6b  E1 batch structure: {K.N_BATCHES_PER_CELL} x {K.N_GENERATIONS_PER_BATCH} = {len(flat_320)}")
    print(f"     mean of within-batch D  = {d_rand_batchmean:.6f}   <- thresholds apply to this form")
    print(f"     pooled D over all pairs = {d_rand_pooled320:.6f}   <- bootstrap targets this form")
    print(f"     difference              = {abs(d_rand_batchmean - d_rand_pooled320):.6f}")
    print()

    # ----------------------------------------------------------- C7: batch spread
    print("C7   across-batch spread of D on random draws (MODEL-FREE reference)")
    print(f"     std across {K.N_BATCHES_PER_CELL} batches = {d_rand_batchstd:.6f}")
    print(f"     min / max               = {min(per_batch):.6f} / {max(per_batch):.6f}")
    print(f"     range as fraction of mean = {(max(per_batch)-min(per_batch))/d_rand_batchmean:.4%}")
    print(f"     no-change band (0.10*D_rand) = {K.THRESHOLD_NO_CHANGE * d_rand_batchmean:.6f}")
    print(f"     band / batch-std          = "
          f"{K.THRESHOLD_NO_CHANGE * d_rand_batchmean / d_rand_batchstd:.2f} std")
    print(f"     std of a 16-batch mean    = {d_rand_batchstd / (K.N_BATCHES_PER_CELL ** 0.5):.6f}")
    print(f"     std of a paired DeltaD    = "
          f"{d_rand_batchstd * (2 ** 0.5) / (K.N_BATCHES_PER_CELL ** 0.5):.6f}  (unpaired worst case)")
    print()

    # -------------------------------------------------- thresholds and sanity gate
    lo, hi = K.D_RAND_SANITY_RANGE
    ref = d_rand_batchmean
    print("C6c  the six threshold constants implied (applied to the batch-mean form)")
    rows = [
        ("collapsed", f"D < {K.THRESHOLD_COLLAPSED} * D_rand", K.THRESHOLD_COLLAPSED * ref),
        ("reduced/partial lower", f"D >= {K.THRESHOLD_COLLAPSED} * D_rand", K.THRESHOLD_COLLAPSED * ref),
        ("diverse", f"D >= {K.THRESHOLD_DIVERSE} * D_rand", K.THRESHOLD_DIVERSE * ref),
        ("no chg", f"|dD| < {K.THRESHOLD_NO_CHANGE} * D_rand", K.THRESHOLD_NO_CHANGE * ref),
        ("recovers", f"dD >= {K.THRESHOLD_RECOVERS} * D_rand", K.THRESHOLD_RECOVERS * ref),
        ("D_rand itself", "reference", ref),
    ]
    for name, rule, val in rows:
        print(f"     {name:<24} {rule:<34} {val:.6f}")
    print()

    in_range = lo <= ref <= hi
    print(f"SANITY GATE (§2.6): halt E1 if D_rand outside [{lo}, {hi}]")
    print(f"     batch-mean form  = {ref:.6f}  -> {'INSIDE' if in_range else 'OUTSIDE -- WOULD HALT E1'}")
    p_in = lo <= d_rand_plan <= hi
    print(f"     plan-literal form= {d_rand_plan:.6f}  -> {'INSIDE' if p_in else 'OUTSIDE -- WOULD HALT E1'}")
    print(f"     analytic anchor the plan cites: ~0.74, derived for a FIXED block count")
    print()

    # ------------------------------------ why the anchor and the measurement differ
    counts: dict[int, int] = {}
    for cfg in flat_320:
        counts[len(cfg["blocks"])] = counts.get(len(cfg["blocks"]), 0) + 1
    print("DIAGNOSIS of the anchor gap: the sampler does not hold block count fixed")
    print(f"     num_blocks distribution over {len(flat_320)} draws: "
          + ", ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
    same_bc = [
        batch_diversity([c for c in flat_320 if len(c["blocks"]) == n])
        for n in sorted(counts) if counts[n] > 1
    ]
    print(f"     D within fixed-block-count subsets: "
          + ", ".join(f"B={n}:{d:.4f}" for n, d in zip(sorted(counts), same_bc)))
    print(f"     -> the ~0.74 anchor matches the fixed-block-count case, not the sampler's")
    print()

    pooling_vals: dict[str, int] = {}
    for cfg in flat_320:
        for b in cfg["blocks"]:
            pooling_vals[b["pooling"]] = pooling_vals.get(b["pooling"], 0) + 1
    tot = sum(pooling_vals.values())
    print("     second non-uniformity: `pooling` is not sampled uniformly over its 4 values")
    for k, v in sorted(pooling_vals.items(), key=lambda kv: -kv[1]):
        print(f"       {k:<14} {v:>6}  {v/tot:6.2%}   (uniform would be 25.00%)")
    print()

    out = {
        "generated_by": "tests/compute_d_rand.py",
        "sampler_source": "src/search_space.py",
        "sampler_file_sha256": source_sha256(),
        "sampler_extract_sha256": extract_digest,
        "seed": K.D_RAND_SEED,
        "plan_literal": {"n": K.D_RAND_N_PLAN, "form": "pooled", "D_rand": d_rand_plan},
        "e1_batch_structure": {
            "n_batches": K.N_BATCHES_PER_CELL,
            "n_per_batch": K.N_GENERATIONS_PER_BATCH,
            "D_rand_batch_mean": d_rand_batchmean,
            "D_rand_batch_std": d_rand_batchstd,
            "D_rand_pooled": d_rand_pooled320,
            "per_batch": per_batch,
        },
        "thresholds_from_batch_mean": {
            "collapsed_below": K.THRESHOLD_COLLAPSED * ref,
            "diverse_at_or_above": K.THRESHOLD_DIVERSE * ref,
            "no_change_band": K.THRESHOLD_NO_CHANGE * ref,
            "recovers_at_or_above": K.THRESHOLD_RECOVERS * ref,
        },
        "sanity_range": list(K.D_RAND_SANITY_RANGE),
        "sanity_pass_batch_mean": in_range,
        "sanity_pass_plan_literal": p_in,
        "num_blocks_distribution": {str(k): v for k, v in sorted(counts.items())},
        "pooling_distribution": pooling_vals,
        "NOTE": (
            "C7's across-batch std is a MODEL-FREE reference on random draws. It is "
            "not a pilot of model behaviour."
        ),
    }
    dest = ROOT / "results" / "E1_reference.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    print(f"written: {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
