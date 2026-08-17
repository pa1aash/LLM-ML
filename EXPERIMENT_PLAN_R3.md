# EXPERIMENT PLAN — pre-registered — **REVISION 3**

**Revision:** 3 — **the last pre-data revision**
**Written:** 2026-08-17
**Supersedes:** `EXPERIMENT_PLAN_R2.md` (revision 2),
SHA-256 `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1`
**Chain:** revision 1 `aeb174ff…bad3d` → revision 2 `a9954ba3…1df1` → **revision 3**

Revisions 1 and 2 remain in the repository **byte-identical**. Neither was
edited, amended in place, or deleted. Both hashes were re-verified immediately
before this revision was written and again after it was committed. This file is
the governing document from the moment its own hash is recorded in
`PREREGISTRATION.md`.

**Authority for writing a successor rather than editing:** revision 2 §5.6
rule 4 — *"This plan is not edited after its hash is taken. Changes go in
`DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
written as a new file, hashed separately, and cites the prior hash it supersedes;
every superseded plan file stays in the repository byte-identical to the version
that was hashed."* That rule is carried forward unchanged as §5.6 rule 4 below.

**After G2 is signed, this plan is not superseded again.** Every subsequent
change is a `DEVIATIONS.md` entry logged before the affected analysis runs. The
revision mechanism exists for the pre-data period and closes when the gate is
signed.

**Status at time of writing:** no data collected. Re-verified independently at
2026-08-17T09:39:26Z — see `PREREGISTRATION.md`. Nothing in any revision has been
run: no model served, no generation produced, no benchmark queried, no analysis
script written, no hardware provisioned, no ML dependency installed.

**Section numbering is preserved** from revisions 1 and 2. Every cross-reference
elsewhere in the repository resolves to the same content. Amendments extend
sections; they do not renumber them.

---

## Amendment record — revision 2 → revision 3

| ID | Amendment | Sections touched |
|---|---|---|
| **R3-1** | E1 batches per cell 10 → **16** (n = 320 per cell, **9,600** E1 generations). Seed vector extended to `[7001…7016]`. | §2.3, §2.7, §3.5, §5.5 |
| **R3-2** | The permutation floor becomes **FATAL**: the emitter computes `min_attainable_p` for every confirmatory test at **plan-load time, before any data is read**, and **aborts** if any confirmatory test has `min_attainable_p ≥ alpha`. | §5.2 |
| **R3-3** | **R is redefined**: `R_final = max(20, the value scripts/power_e2.py confirms at S3)`. An increase from that simulation is **compliance, not a deviation**. A decrease below 20 remains forbidden. Budget stated as a function of R. | §3.4, §3.5, §8.2 |
| **R3-4** | Confirmatory family **unchanged: FAMILY_SIZE = 16, ALPHA = 0.003125**. | §5.2 |

**R3-4 verification, performed before this revision was written.**

| Amendment | Adds a confirmatory test? | Why not |
|---|---|---|
| R3-1 | No | More batches per cell changes the *resolution* of X1–X4, not their number. Same four contrasts, same three models. |
| R3-2 | No | A pre-flight assertion. It emits no statistic and no p-value; it can only halt the emitter. |
| R3-3 | No | R is a sample size, not a test count. Y1–Y4 remain four contrasts on the primary task only; the secondary tasks stay exploratory (§5.1 row A12). |

**FAMILY_SIZE remains 16. ALPHA remains 0.05/16 = 0.003125.** The STOP condition
(any amendment changing the family size) was not triggered.

---

# 1. Thesis and claim set

*(Unchanged from revisions 1 and 2.)*

## 1.1 Thesis

> **In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.**

"Measurement apparatus" means, concretely and exhaustively for this paper: the
prompt's format demand, the output parser, the schema-repair / sanitiser stage,
the decoding constraint, the sampling temperature, and the weight precision at
which the generator is served. It does not mean the training data, the model
architecture, or the model's scale.

## 1.2 Novelty framing — binding constraint on all downstream writing

**We claim the APPLICATION of an established mechanism to LLM-guided NAS. We do
NOT claim to discover that structured decoding or output repair distorts
measurement.**

The general mechanism — that structured-output requirements and constrained
decoding distort what is measured about a model, independent of the model's own
distribution — is already published and active 2024–2026 literature. Four
sources establish it (§6, rows 8–11), one of them from the month before this plan
was written. A paper asserting only the general mechanism would read as
confirmatory, not novel.

What is not published anywhere the S1 corpus critic could find, across a vault
sweep and a targeted arXiv wave (`abs:"neural architecture search" AND
abs:"constrained decoding"` → 0 hits; `abs:"neural architecture search" AND
abs:"parser"` → 1 irrelevant hit; `abs:"evaluation harness" AND abs:"confound"`
→ 0 hits), is the NAS-scoped instantiation: that parser / sanitiser /
schema-repair artifacts in an LLM-guided NAS pipeline are responsible for an
observed "collapse to a single template" or an observed feedback-degradation
effect.

**Defect rule.** Any sentence in any downstream artifact — manuscript, abstract,
figure caption, rebuttal, README, talk — that claims the *mechanism* rather than
the *application* is a defect and must be rewritten. Concretely, these are
defects:

- "We show that constrained decoding distorts LLM output distributions." (claims
  the mechanism)
- "We introduce the idea that the harness, not the model, produces the measured
  effect." (claims the mechanism)
- "Prior work has not considered that output repair can confound measurement."
  (false, and claims the mechanism by implication)

These are correct:

- "We apply a mechanism established for reasoning and code benchmarks
  [format-tax, grammar-aligned-decoding] to architecture search, where it has not
  been tested."
- "The distortion mechanism is known; its magnitude in an LLM-guided NAS pipeline
  is not, and it has not previously been separated from the model's own prior in
  this setting."

A pre-submission grep for the defect pattern is a G7 requirement.

## 1.3 Claims abandoned

Each row states the claim as the current manuscript makes it, and the finding
that killed it. All are abandoned permanently: OA-1 is CLOSED — the original
data is unrecoverable and will be regenerated, so no ORPHAN claim can be
re-grounded in the original run.

| Abandoned claim | Killed by |
|---|---|
| **"Iterative feedback degrades LLM-guided NAS"** (unqualified thesis) | S1 / L1. Refuted by two controlled ablations running the other way: RZ-NAS (ICML 2025) reflection ablation, and EvoPrompting's feedback ablation. Further, GENIUS's own per-trial Appendix A.3 tables show feedback beating zero-shot in every reported trajectory — the paper's strongest cited ally does not support it. The mechanism-specific version that survives is SCOOPED by CoLLM-NAS (CVPR 2026 NAS Workshop, Oral), whose Generator-memory ablation reports that retaining the generator's uncurated in-context history "induces progressive noise accumulation, leading to performance degradation." |
| **"The LLM encodes a strong narrow prior"** | S0 / OA-8, `audit/FORENSICS.md` F1. `sanitize_config` ([run_v2.py:52-67](src/run_v2.py#L52)) coerces every out-of-vocabulary field to the first legal value — `standard_3x3` / `relu` / `batchnorm` / `identity` / `maxpool` — and fills every *absent* field with the same defaults. That template is exactly the reported "narrow prior." The function runs on the LLM arms only, never the random arms, so the two arms were not measured with the same instrument. The claim has an unexcluded instrumental explanation and is not separable from it in the surviving evidence. |
| **"Parameter std = 0K"** | S0 / OA-4. ORPHAN. Quoted in abstract, Results, Discussion and Conclusion; no artifact contains it and no code in `src/` computes a parameter standard deviation. |
| **"Zero causal attributions reflects model capacity"** (Limitation iv) | S0 / OA-15. `enable_thinking=False` ([llm_server_small.py:43](src/llm_server_small.py#L43)) suppresses reasoning, and transcripts are truncated to 2000 characters ([run_v2.py:194](src/run_v2.py#L194)). A causal attribution that the model did emit could not have survived either step. The result is a harness property, not a capacity measurement. Compounded by OA-16: `finish_reason` is hardcoded to `"stop"`, so truncated generations are indistinguishable from complete ones. |
| **The seed-137 replication** (all six numbers) | S0 / OA-24. All six are ORPHAN. The replication subsection has no evidentiary basis in the repository. |
| **"Pre-specified" for the seven comparisons** | S0 / OA-23. `deep_analysis_v2.py` computes all C(6,2)=15 pairs exhaustively; no pre-registration artifact exists or ever existed. The word is false as used. |
| **"Evaluates it on the test set only once"** ([main.tex:334](paper/main.tex#L334)) | S0 / OA-20. Contradicted by Algorithm 1 line 7 and by the code, which evaluate test accuracy for all 20 architectures. Compounded by OA-11: top-5 retraining selects on `test_acc` ([run_v2.py:340](src/run_v2.py#L340)), inside the block labelled as the v2 "no leakage" fix. |
| **Every number in the current Tables 1–6** | S0 data census. 0 RAW / 0 SPEC / 0 TRANSCRIPT across all 24 cells; every analysis entry point reads a directory that is absent. No inferential statistic in the manuscript is recomputable. Specifically also: the significance stars in Table 3 were computed at α=0.05/15=0.00333 and reported against a stated α=0.05/7=0.0071 (OA-5), and the load-bearing B-vs-C cell sits inside the rounding interval of its own decision threshold and cannot be resolved (OA-6). |

Two further manuscript statements are abandoned as a consequence rather than on
their own evidence, and are listed so they are not silently carried forward:
the prose claim of "20 structurally identical designs" (self-contradicted by the
Jaccard 0.022 quoted in the same sentence, and by the 50/50 skip split 20 lines
later — `audit/CLAIM_TRACE.md` §5.1), and the framing that condition D's
feedback "hurts" (condition D holds the best single architecture on both
datasets — §5.3).

## 1.4 Claims proposed

Each claim is falsifiable, is tested by a named experiment, and states the
observation that refutes it. Thresholds referenced here are defined numerically
in §2.6 and §5.

**C1 — Repair concentrates the design distribution.**
*In the subject pipeline's configuration (Qwen3-1.7B, NF4, schema-requesting
prompt), the post-repair design-choice distribution is materially more
concentrated than the pre-repair distribution over the same generations.*
- Tested by: E1, contrast **X2** (schema pre-repair vs schema post-repair),
  paired at the generation level.
- Refuted by: `D_post ≥ D_pre − 0.10·D_rand` — the repair stage moves diversity
  by less than the pre-registered "no change" band.

**C2 — An apparatus factor dominates the model's own prior.**
*At least one measurement-apparatus factor (prompt format, repair, precision,
decoding temperature) accounts for more of the observed design-choice
concentration than the residual attributable to the model.*
- Tested by: E1, five-rival signature match (§2.5).
- Refuted by: the **genuine prior** row wins the signature match, **or** no rival
  matches ≥4 of 5 cells (in which case attribution is reported as mixed and C2
  is not asserted).

**C3 — The effect is not an artifact of model scale.**
*The direction of the free-prose → schema-constrained concentration effect is the
same at Qwen3-1.7B, Qwen3-8B, and a frontier API model.*
- Tested by: E1, model factor.
- Refuted by: the free-prose → schema contrast is classified "no change" at
  Qwen3-8B or at the frontier model while being classified "collapsed" at
  Qwen3-1.7B.

**C4 — Uncurated accumulation does not beat curation.**
*Under a run-level estimand, the uncurated in-context accumulation arm does not
outperform the curated-summary arm.*
- Tested by: E2, contrast **Y4**, primary outcome, primary task (CIFAR-100).
- Refuted by: uncurated > curated with p < 0.003125 and Cliff's δ > 0.
- Note: this is directionally the same finding as CoLLM-NAS's Generator-memory
  ablation, in a regime CoLLM-NAS did not test (small, quantised, single model).
  It is a **replication-in-a-new-regime claim, not a discovery claim**, and must
  be written as one.

**C5 — Measurement configuration changes the arm ordering.**
*The ordering of the four feedback arms observed at the original paper's
configuration is not stable when the same experiment is run at the
least-artifactual configuration E1 identifies.*
- Tested by: E2 primary + E2 conditional replicate (§3.3).
- Refuted by: identical arm ordering by mean in both configurations, with
  overlapping 95% CIs on every pairwise difference.
- This is the claim that carries the thesis. If C5 fails, the paper's
  contribution reduces to C1–C3 plus E3, and the thesis in §1.1 must be
  weakened to a statement about the *generation* stage only, not about
  *reported effects of feedback*.

**C6 — RZ-NAS's proxy menu is size-tracking off NAS-Bench-201.**
*For at least two of {GraSP, Gradnorm, Synflow, Zen-Score}, the rank correlation
with parameter count on benchmarks outside NAS-Bench-201 is at least as large as
the rank correlation with validation accuracy on those benchmarks.*
- Tested by: E3, on NAS-Bench-Suite-Zero's public 1.5M-evaluation release.
- Refuted by: fewer than two proxies meet the condition.
- Bounded scope: this is a **validation-practice finding**, not a takedown of
  RZ-NAS. See the mandatory caveats in §4.4, which are binding.

**Thesis-level.** The thesis of §1.1 is asserted only if C2 holds **and** C5
holds. If C2 holds and C5 fails, the paper reports a generation-stage
instrumentation result and states plainly that it did not establish the
feedback-level consequence. If C2 fails, the thesis is withdrawn and the paper
reports the null: the apparatus was interrogated and the model's own prior
survived it.

---

# 2. Experiment E1 — the discrimination factorial

**Inference-only. Generation and structural measurement. No training, no
architecture is ever evaluated for accuracy in E1.**

E1 exists to answer one question: when an LLM-guided NAS pipeline reports a
collapsed design distribution, which part of the apparatus produced it?

## 2.1 Factors

*(Unchanged.)*

| Factor | Levels | Notes |
|---|---|---|
| **prompt format** | free-prose description \| schema-constrained JSON request | The free-prose prompt describes the search space in sentences and asks for a design in whatever form the model likes. The schema prompt supplies the JSON schema and demands conformance. Both prompts are frozen verbatim in `prompts/E1/` before any run and hashed into the results file. |
| **precision** | NF4 4-bit \| bf16 | Applies to the two locally-served models only. **Not manipulable on a hosted API** — see §2.2. |
| **temperature** | 0.3 \| 0.7 \| 1.0 | top_p fixed at 1.0, top_k disabled, no repetition penalty, `enable_thinking` **True** (the original's `False` is itself under test and is not carried forward as a default). |
| **model** | Qwen3-1.7B (anchor) \| Qwen3-8B (scale control) \| one frontier API model (ceiling) | The anchor reproduces the original paper's *stated* configuration. The frontier model is selected at S3 and its exact model ID and served revision are recorded in the results file; the choice is recorded in `DEVIATIONS.md` if it differs from the S3 selection. |

**Repair stage is not a factor.** Every generation is logged and scored twice —
once pre-repair and once post-repair — so the pre/post contrast is *paired within
generation*. Parse-failure rate therefore cannot confound it: both stages are
computed over the identical set of generations.

Three stages exist and all three are logged:
1. **raw** — the model's response text, untruncated, with the true `finish_reason`
   from the server (fixing OA-16).
2. **pre-repair** — the parsed JSON object, before `sanitize_config`. May not
   exist (parse failure).
3. **post-repair** — after `sanitize_config`. Exists whenever pre-repair exists.

## 2.2 Cell grid

*(Unchanged.)*

| Model | format × precision × temperature | Cells |
|---|---|---|
| Qwen3-1.7B | 2 × 2 × 3 | 12 |
| Qwen3-8B | 2 × 2 × 3 | 12 |
| Frontier API | 2 × — × 3 | 6 |
| **Total** | | **30** |

**The frontier model has no precision factor.** Weight precision is not
controllable on a hosted API. Its six cells record `precision: "provider_default
(unknown)"`. The quantisation rival's prediction is therefore evaluated on the
two local models only, and the frontier model contributes to the format, repair
and temperature columns and to C3 alone. This is a limit of the factorial as
briefed, not a choice, and it is stated as a limitation in the manuscript.

## 2.3 Generations per cell, batching, seeding — **AMENDED (R3-1)**

- **20 generations per batch, 16 batches per cell, 320 generations per cell.**
  *(Revision 1: 5 batches / 100. Revision 2: 10 batches / 200.)*
- **30 cells × 320 = 9,600 generations.** No architecture is trained.
- Batch size 20 matches the original paper's per-condition *n*, so E1's within-
  batch diversity statistic is directly comparable in scale to the original's.
- Diversity is computed **within batch**; a cell reports **mean ± std across its
  16 batches**.

### Why 16 — the paired permutation test's discreteness ceiling

The five rivals are separated primarily by the two **change** columns (`bf16`,
`high temp`). ΔD is a difference of two cell means and carries roughly √2 the
noise of a single cell mean, so the change columns set the batch-count
requirement. But the binding constraint is not variance — it is the **discrete
geometry of the test itself**, and it is what drove both this amendment and the
previous one.

A paired sign-flip permutation test over *B* paired batch differences has exactly
2^*B* equally likely sign assignments. Its two-sided p-value is

```
    p  =  #{assignments with |T| ≥ |T_observed|}  /  2^B
```

and, by mirror symmetry, that count is always even — assignments come in
complementary pairs. Rejection at ALPHA = 0.05/16 = 0.003125 = 1/320 therefore
requires

```
    #{as-or-more-extreme assignment pairs}  <  2^B / 640
```

**The ceiling table.** How many assignment-pairs may be as extreme as the
observation and still permit rejection:

| *B* | 2^*B* | **Ceiling** (as-or-more-extreme assignment **pairs**) | Smallest attainable two-sided *p* | Discordant batches tolerated (equal-magnitude worst case) | *p* at one discordant |
|---:|---:|---:|---:|---:|---:|
| **10** | 1,024 | **1** | 0.00195313 | **0** | 0.021484 |
| **12** | 4,096 | **6** | 0.00048828 | **0** | 0.006348 |
| **14** | 16,384 | **25** | 0.00012207 | **1** | 0.001831 |
| **16** | 65,536 | **102** | 0.00003052 | **1** | **0.000519** |

*Ceiling* = largest even count *M* with *M*/2^*B* < ALPHA, expressed in mirror
pairs (*M*/2). *Discordant batches tolerated* is the equal-magnitude worst case:
with all |*d*ᵢ| equal and *k* differences opposing the majority, the
as-or-more-extreme count is 2·Σ₀ᵏ C(*B*,*s*), and the table reports the largest
*k* for which that count stays under the ceiling. Equal magnitudes maximise ties
and so give the pessimistic bound; unequal magnitudes with a small discordant
difference do better.

**What the table shows, and what the choice rests on.**

- **At *B* = 10 the ceiling is 1.** Only the observed assignment and its mirror
  may be as extreme — the observation must be the strictly unique maximum of the
  permutation distribution. That happens only when **all ten** paired differences
  share a sign. **A single discordant batch makes the all-same-sign assignment
  strictly more extreme than the observation, and the contrast can no longer
  reject at any effect size whatsoever.** X1–X4 at *B* = 10 are all-or-nothing
  checks, not tests: a 15-of-16 clean result and a pure-noise result are reported
  identically.
- **At *B* = 12 the ceiling rises to 6, but the discordance tolerance is still
  0** — one discordant batch needs 13 pairs, more than 6. Twelve buys margin
  against ties, not against a single dissenting batch.
- **At *B* = 14 the tolerance first becomes 1**, at *p* = 0.001831 — 59% of
  ALPHA. It clears, but with little headroom, and two discordant batches are far
  out of reach.
- **At *B* = 16 the ceiling is 102** and one discordant batch lands at
  *p* = 0.000519, **17% of ALPHA**. This is the first batch count at which the
  test has real headroom rather than sitting against its own floor, and at which
  a contrast can fail for evidential reasons rather than arithmetic ones.

Sixteen is chosen on the headroom, not on the tolerance count alone: *B* = 14 and
*B* = 16 both tolerate exactly one discordant batch in the pessimistic
equal-magnitude case, but *B* = 14 does so at 59% of ALPHA and *B* = 16 at 17%,
and only *B* = 16 leaves the ceiling (102 pairs) far enough above the
single-discordant requirement (17 pairs) that realistic tie structure does not
consume the margin. **This table is recorded so the choice is auditable and so
that any future proposal to reduce *B* has to argue against these numbers.**

The unpaired form used for a frontier cell whose seeds are not honoured does not
have this problem: a two-sample permutation over 32 values split 16/16 has
C(32,16) = 601,080,390 assignments and a smallest attainable two-sided *p* of
about 3.3 × 10⁻⁹.

### Seeding scheme — **AMENDED (R3-1)**

A single frozen seed vector

```
S = [7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
     7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016]
```

is shared by **every** cell. Batch *b* of every cell uses `S[b]` for the sampler.
Cross-cell contrasts are therefore **paired at the batch index**, which removes
seed variance from every between-cell comparison. The seed vector is written into
the results file. The first ten entries are unchanged from revision 2 and the
first five from revision 1, so no earlier planning against them is disturbed.

For the frontier API, if the provider does not honour a seed parameter, the cell
records `seed_honoured: false` and its sixteen batches are treated as unpaired
replicates. Contrasts involving that cell use the unpaired form of the test, and
the results file flags which form was used per contrast.

## 2.4 Outcomes

### 2.4.1 The design-choice vector

*(Unchanged.)*

For a configuration with *B* blocks, the design-choice vector concatenates, over
block positions *b* = 1…*B*, the six per-block categorical fields taken from the
repository's own search space ([run_v2.py:52-58](src/run_v2.py#L52)):

`conv_type` ∈ {standard_3x3, depthwise_separable, dilated_3x3, bottleneck}
`channels` ∈ {32, 64, 128, 256} — **treated as categorical**, because repair
snaps it to the nearest legal value, making the post-repair variable categorical
by construction
`activation` ∈ {relu, gelu, silu, mish}
`normalization` ∈ {batchnorm, layernorm, groupnorm, none}
`skip_connection` ∈ {identity, projection, none}
`pooling` ∈ {maxpool, avgpool, strided_conv, none}

plus the architecture-level fields `n_blocks` = *B*, `global_pool`, `fc_layers`.

*(Note: *B* denotes block count in this subsection and batch count in §2.3. The
two never appear in the same expression.)*

### 2.4.2 Primary outcome — mean pairwise structural diversity

*(Unchanged.)*

Pairwise distance between two configurations *x*, *y*:

```
                Σ_{b=1..min(Bx,By)} Σ_{f∈F} 1[x_bf ≠ y_bf]  +  6·|Bx − By|  +  Σ_{g∈G} 1[x_g ≠ y_g]
   d(x,y)  =   ────────────────────────────────────────────────────────────────────────────────────
                                    6·max(Bx,By)  +  |G|
```

where **F** is the six per-block fields and **G** = {`global_pool`, `fc_layers`}.
Blocks present in only one architecture count as six field mismatches each.
`d ∈ [0,1]`, and **d = 0 if and only if the two design-choice vectors are
identical**.

**D(batch)** = mean of *d* over all C(n,2) unordered pairs of parseable
generations in the batch.

*Why not the original's Jaccard.* `mean_jaccard_distance` operates on
position-tagged block *signature sets*, so a block differing in one field and a
block differing in all six contribute equally. That coarseness is part of why the
manuscript could assert "20 identical designs" and "Jaccard 0.022" in one
sentence (`audit/CLAIM_TRACE.md` §5.1). Field-level Hamming has the resolution
the per-field collapse profile requires, and preserves the d=0 ⟺ identical
property the original's interpretation assumed.

### 2.4.3 Secondary outcome — parse-failure rate

Fraction of the batch's 20 generations that produce no parseable JSON object
containing a `blocks` key. Reported for every cell, always adjacent to that
cell's diversity number.

### 2.4.4 Secondary outcome — per-field collapse profile

For each field *f* and each batch, at each stage, the **normalised Shannon
entropy** of *f*'s realised values pooled across all block positions and all
parseable generations, in bits, divided by log₂|vocab_f|. A field that has gone
constant has normalised entropy exactly 0.

And, separately, the three repair channels counted per field —
`sanitize_config` has two distinct collapse mechanisms and the manuscript
conflated them:

| Channel | Meaning |
|---|---|
| `passthrough` | field present, value already legal, unchanged by repair |
| `coerced` | field present, value out-of-vocabulary, rewritten to `valid_vals[0]` |
| `filled` | field **absent** from the model's output, inserted at `valid_vals[0]` |

`filled` is a collapse the model never had a chance to avoid: `block.get(key,
valid_vals[0])` supplies the default for any field the model simply did not emit.
If the collapse profile is dominated by `filled` rather than `coerced`, the
mechanism is "the model wrote a partial config and the harness completed it,"
which is a different finding from "the model wrote an illegal value and the
harness overwrote it," and the paper must say which.

### 2.4.5 Secondary outcome — within-cell bootstrap interval on D

*(Unchanged from revision 2.)*

The paired batch-index contrast (§5.1 X1–X4) remains the **primary** inferential
device. The bootstrap defined here is a **resolution check**: it answers "is this
cell's diversity, and this contrast's ΔD, estimated tightly enough to sit on one
side of a threshold?" — a question the discrete paired test cannot answer.

**Pooled cell statistic.** `D_cell_pooled` = mean of *d* over all C(N, 2)
unordered pairs of the cell's *N* parseable generations, pooling across all
sixteen batches. This is a **different estimand** from `D_mean` (the mean of the
sixteen within-batch D values): it additionally includes cross-batch pairs, and
because batches differ only by sampler seed, those pairs are legitimate. Both are
reported. `D_mean ± D_std` remains the quantity the classification thresholds in
§2.6 are applied to; `D_cell_pooled` is the bootstrap target.

**Resampling unit: the generation, not the pair.** Resample *N* generations with
replacement from the cell's parseable generations, recompute the mean pairwise
*d* over the resample, repeat. **Pairs are not resampled directly.** The C(N,2)
pairwise distances are strongly dependent — each generation appears in *N*−1 of
them — so resampling pairs as if independent would understate the interval width,
which is the opposite of what a resolution check is for.

**Parameters, fixed here and not tuned later:**
- `B_boot = 10,000` resamples
- `BCa` intervals (bias-corrected and accelerated), 95%
- `bootstrap_seed = 90210`, a single constant for every bootstrap in E1, written
  into the results file
- Computed separately at each stage (pre-repair, post-repair)

**Bootstrap on ΔD for the change columns.** The two change columns carry the
discriminating load (§2.3), so they get the same treatment: for the `bf16` and
`high temp` contrasts, resample generations **independently within each of the
two cells**, recompute `ΔD_pooled` per resample, and report the BCa 95% interval
on ΔD.

**Status.** Descriptive. `confirmatory: false`. Emits an interval, never a
p-value. It cannot change a rival's signature match, which is decided by the
§2.6 thresholds applied to `D_mean`. If the bootstrap interval straddles a
classification boundary, the cell's label is reported **with the interval shown**
and the signature match for that cell is scored `indeterminate` — this can only
ever move a cell **toward** `indeterminate`, never toward a match.

### 2.4.6 Secondary outcome — parse-free surface diversity **S**

*(Unchanged from revision 2.)*

**Purpose, and its only purpose.** Free-prose pre-repair diversity is conditioned
on the generation having parsed at all, a non-random subset, and free-prose is
the condition most likely to fail parsing. That makes the cell most load-bearing
for separating `format tax` from `genuine prior` also the least reliable. **S
bounds that selection effect by measuring diversity over the full generation set,
including the failures.** It exists for nothing else.

**Definition.** On the **raw generated text**, before any parsing:

1. **Normalisation** — lowercase; collapse every run of whitespace to a single
   space; strip leading and trailing whitespace. **Nothing else.** No punctuation
   stripping, no code-fence removal, no JSON-aware handling. The measure must
   treat both prompt formats identically and must not be tuned to either; any
   format-aware normalisation would build the answer into the instrument.
2. **Tokenisation** — split on whitespace.
3. **Feature set** — G₃(x) = the set of contiguous token 3-grams of generation x.
4. **Pairwise distance** — Jaccard distance:
   `d_S(x, y) = 1 − |G₃(x) ∩ G₃(y)| / |G₃(x) ∪ G₃(y)|`
5. **Batch statistic** — `S(batch)` = mean of `d_S` over all C(20, 2) pairs,
   **including generations that failed to parse**. Every generation in the batch
   is included, without exception. `S ∈ [0, 1]`.
6. **Cell statistic** — `S_mean ± S_std` across the sixteen batches, plus
   `S_cell_pooled` with a BCa 95% bootstrap interval under the same parameters as
   §2.4.5 (10,000 resamples, `bootstrap_seed = 90210`, resampling generations).

**Why token 3-gram Jaccard, and not the alternatives.** Jaccard over n-gram sets
is symmetric, bounded in [0,1], parameter-free beyond the choice of *n*, and
structurally parallel to a mean-pairwise-distance diversity, so S and D are the
same *kind* of quantity even though they are not the same quantity. Self-BLEU is
asymmetric and carries a brevity penalty that would reward the terse schema
condition for the wrong reason. Distinct-*n* is a corpus-level ratio rather than
a pairwise mean and cannot be compared batch-to-batch on the same footing.
*n* = 3 is fixed in advance and not tuned: bigrams over-fire on shared function
words, and 4-grams and above get sparse on short generations.

**Interpretation — how S is read when it agrees or disagrees with D.** Fixed
here, before data:

| Observation | Reading |
|---|---|
| **S high, D_pre collapsed** (free-prose) | The full generation set carries surface variety while the parseable subset does not. **The parsed-subset collapse is therefore not explained by parse-selection alone** — this is the bound S exists to provide, and it is reported in exactly those terms. |
| **S low, D_pre collapsed** | Consistent. S adds no information about selection: text and structure are both concentrated. **S does not distinguish "the model repeats itself" from "the parseable subset is unrepresentative"** in this case, and the free-prose column's reliability caveat stands undiminished. |
| **S low, D_pre diverse** | Near-duplicate text yielding varied parsed configurations. This is not a substantively interpretable pattern; treat it as an **instrument fault**, halt, and investigate the parser or the normalisation before proceeding. |
| **S high, D_pre diverse** | Consistent. No additional information. |

**Hard constraints on S, so it cannot become a backdoor confirmatory measure:**
- **S is never substituted into D**, in any cell, under any circumstance.
- **S never enters a confirmatory test.** It has no p-value.
- **S has no pre-registered classification threshold** and is never described
  using the words `collapsed` / `diverse` / `partial` / `reduced`, which are
  reserved for D. S is reported as a number with its interval, and described only
  in relative terms (S for free-prose versus S for schema, at matched model,
  precision and temperature).
- **S cannot alter a rival's signature match**, and in particular **cannot rescue
  the free-prose column from `indeterminate` status** when the §2.6 parse-rate
  rule has triggered. A column ruled `indeterminate` stays `indeterminate`.

## 2.5 Pre-registered prediction table — the falsifier set

*(Unchanged.)*

Five rivals. Five signatures. Every cell is a directional prediction fixed before
data.

| Rival | free-prose | schema pre-repair | post-repair | bf16 | high temp |
|---|---|---|---|---|---|
| **repair artifact** | diverse | diverse | collapsed | no chg | no chg |
| **format tax** | diverse | collapsed | collapsed | no chg | no chg |
| **quantisation** | partial | partial | partial | recovers | partial |
| **decoding** | reduced | reduced | reduced | no chg | recovers |
| **genuine prior** | collapsed | collapsed | collapsed | no chg | no chg |

Column definitions, so the table is unambiguous:
- **free-prose** — D at (free-prose, post-repair, NF4, T=0.7)
- **schema pre-repair** — D at (schema, pre-repair, NF4, T=0.7)
- **post-repair** — D at (schema, post-repair, NF4, T=0.7)
- **bf16** — the change in D from (schema, post-repair, NF4, T=0.7) to (schema,
  post-repair, bf16, T=0.7)
- **high temp** — the change in D from (schema, post-repair, NF4, T=0.3) to
  (schema, post-repair, NF4, T=1.0)

The first three columns are **levels**; the last two are **changes**.

**Why the format-tax row is present.** "The Format Tax" (§6, row 8) argues that
the structure-**requesting prompt**, not the decoder-side repair, causes most of
the degradation: *"The dominant cost enters at the prompt: format-requesting
instructions alone cause most of the accuracy loss, before any decoder constraint
is applied."* The original manuscript attributed collapse to `sanitize_config`, a
repair step. If E1 cannot separate a prompt-side cause from a repair-side cause,
the attribution is unfalsifiable and the paper has no result. The schema
pre-repair column is the cell that separates them, and it exists for that reason
alone.

**What we conclude if the format-tax row wins.** Stated now, in advance, in the
words that will be used:

> The original manuscript's attribution was wrong. Template collapse is caused by
> the prompt asking for a fixed JSON schema, upstream of any repair step;
> `sanitize_config` is a downstream amplifier, not the cause. The instrumentation
> thesis survives — the apparatus is still responsible for the reported effect —
> but the specific component the original paper named is exonerated, and the
> paper states that its own prior attribution was incorrect.

That last clause is not optional. The paper carries the correction explicitly.

## 2.6 Classification thresholds

*(Unchanged.)*

The labels above are meaningless without numeric definitions fixed before data.
They are anchored to a random-sampling reference.

**D_rand** — mean pairwise structural diversity of 200 architectures drawn from
the repository's own uniform random sampler over the same search space, computed
with the same *d*. This involves **no LLM at all**, so it is computed at S3
*before any generation runs*, and written to `results/E1_reference.json`. Its
analytic anchor for a fixed block count is ≈0.74 (mean over the six fields of
1 − Σp² under uniform sampling); a measured value outside [0.65, 0.80] indicates
a sampler bug and halts E1.

| Label | Definition |
|---|---|
| **collapsed** | D < 0.15 · D_rand |
| **reduced** / **partial** | 0.15 · D_rand ≤ D < 0.60 · D_rand |
| **diverse** | D ≥ 0.60 · D_rand |
| **no chg** | \|ΔD\| < 0.10 · D_rand |
| **recovers** | ΔD ≥ +0.25 · D_rand **and** the destination cell is not *collapsed* |

`reduced` and `partial` are the same numeric band; the two words appear in the
prediction table because the two rivals mean different things by it, and the
distinction between them is carried by the other four columns, not by this one.

**Signature scoring.** Each rival scores the number of its five cells that match
the observation. The rival with the strictly highest score wins.
- A tie at the top → **"no clean winner — mixed attribution."**
- A winner scoring ≤3 of 5 → **"no clean winner — mixed attribution."**
- **No rival matching ≥4** is a permitted, reportable outcome: we then publish the
  observed signature verbatim and state that the five-rival set was incomplete.
  This is a result, not a failure.

**Free-prose selection effect — pre-registered handling.** Two-part:

1. **The rule.** The free-prose parse rate is reported adjacent to every
   free-prose diversity number, and **if the free-prose parse rate is below 50%,
   that cell's diversity estimate is declared unreliable and the free-prose
   column is scored `indeterminate` for every rival** — neither matched nor
   unmatched — with the maximum achievable signature score dropping to 4 and the
   ≥4-of-5 rule reading ≥3-of-4 accordingly.
2. **The bound.** `S` (§2.4.6) is computed on the full generation set including
   parse failures, and is reported alongside. It *characterises* how much of the
   observed concentration could be a selection artifact. **It does not change
   rule 1.** A column ruled `indeterminate` by the parse-rate test stays
   `indeterminate` whatever S shows; a column not so ruled is not re-opened by S
   either.

A permissive prose-to-fields extractor was considered and rejected: it is a
second instrument with its own artifact and would defeat the purpose of the
experiment.

**Bootstrap straddling a boundary.** Where the §2.4.5 BCa interval on a cell's D,
or on a contrast's ΔD, straddles the classification boundary that decides its
label, that cell is scored `indeterminate` for signature-matching purposes and
the interval is reported. This can only reduce the number of matched cells; it
can never create a match.

## 2.7 Ties and degenerate outputs — **threshold rescaled (R3-1)**

- A generation that fails to parse contributes to the parse-failure rate and is
  excluded from **both** stages' diversity (it never reaches repair). The pre/post
  contrast therefore always runs over an identical generation set. **It is
  included in S** (§2.4.6), which is the point of S.
- A batch with fewer than 2 parseable generations yields `D = null`. It is
  recorded as null, **never imputed**. The cell's mean is taken over the defined
  batches and the null count is reported beside it. A cell with **≥10 null
  batches out of 16** is reported as `insufficient` and contributes no signature
  match. *(Revision 1: ≥3 of 5. Revision 2: ≥6 of 10. The 0.6 proportion is
  unchanged across all three.)*
- **Null batches reduce the usable pair count and therefore raise the paired
  test's discreteness floor.** This interacts with the fatal gate in §5.2 and is
  handled by its run-time arm: a contrast whose *realised* usable pair count *B*
  gives `min_attainable_p ≥ ALPHA` is emitted with
  `status: "undecidable_by_discreteness"` and `significant: null`, and the
  manuscript reports it as undecidable rather than as a null result.
- An all-identical batch yields D = 0.000 exactly. **This is a legal measurement,
  not a missing value**, and is the single most likely observation in the
  post-repair schema cells.
- Duplicate generations within a batch are retained, not deduplicated —
  duplication *is* the collapse being measured.
- **S degenerate cases.** A generation of fewer than 3 tokens after normalisation
  has an empty 3-gram set. A pair of two empty sets is defined as `d_S = 0` (both
  identical and empty); a pair of one empty and one non-empty set is `d_S = 1`.
  The count of empty-3-gram generations is recorded per batch, and a batch in
  which more than half the generations have empty 3-gram sets yields `S = null`,
  recorded and never imputed.

---

# 3. Experiment E2 — feedback curation on a tabular benchmark

E2 positions the paper against CoLLM-NAS by testing the variable CoLLM-NAS
identified, in the regime CoLLM-NAS did not test: **small, quantised, single
model.** Every prior ablation in the corpus uses frontier-scale or fine-tuned
research-scale models (GPT-4o, 62B PaLM, purpose-fine-tuned GPT).

## 3.1 Substrate

*(Unchanged from revision 2.)*

**NAS-Bench-201 / NATS-Bench topology search space (TSS).** 15,625
architectures; validation and test accuracy are **table lookups**, so no training
occurs and *n* is limited by generation cost alone. Tasks: CIFAR-10, CIFAR-100,
ImageNet16-120.

**All three tasks are retained.**

- **Primary task: CIFAR-100.** Chosen as the conservative middle. CoLLM-NAS
  reports its noise-accumulation effect scaling with task difficulty and largest
  on ImageNet16-120; selecting ImageNet16-120 as primary would be selecting the
  task most likely to produce the effect we expect. It is not the primary.
- **Secondary tasks: CIFAR-10 and ImageNet16-120.** Reported, **not** in the
  confirmatory family, analysed as exploratory (§5.1 row A12, §5.4). If the
  effect appears only on ImageNet16-120, it is reported as a secondary finding
  consistent with CoLLM-NAS's difficulty-scaling and is **not** stated as a
  confirmatory result.

**Why all three are retained.** The substrate is a table lookup: adding a task
adds **no training and no evaluation cost whatsoever**, only generation on a
locally-served model. Under that cost structure, multi-task coverage is **the
cheapest external validity available anywhere in this design** — the difference
between a claim about CIFAR-100 and a claim about a search space's three standard
tasks, bought with local GPU hours and nothing else. A single-task result invites
precisely the generalisation objection that Yang et al. and Li & Talwalkar press
on the NAS literature, and answering it later would cost far more than running it
now. Dropping the secondary tasks is **not** a scope reduction this plan
recognises; see §8.

This substrate also closes the objection the manuscript itself concedes
([main.tex:757](paper/main.tex#L757)): the original search space was custom, not
tabular.

## 3.2 Arms

*(Unchanged.)*

| Arm | Definition |
|---|---|
| **zero-shot** | Each of the *k* proposals is generated in a fresh context from the task description alone. No outcome is ever shown to the model. |
| **uncurated in-context accumulation** | Proposal *i*+1 is generated in a context containing every prior proposal and its measured validation accuracy, verbatim, appended. The context grows monotonically. This is the CoLLM-NAS Generator-memory-retained condition, and the structural design the original manuscript instantiated. |
| **curated summary** | After each proposal, the history is distilled into a bounded natural-language strategy statement. **The context is reset each round** and re-seeded with the task description plus the current strategy statement only. Raw history never accumulates. |
| **external archive** | Population state (the top-*m* proposals and scores) is held **outside** the model in a data structure, and the *m* entries are injected into a fresh context each round. No natural-language history, no growth. |

The curation prompt and the archive's *m* are frozen in `prompts/E2/` before any
run and hashed into the results file.

**Generator configuration (primary):** Qwen3-1.7B, NF4, schema-constrained JSON
prompt, post-repair, temperature 0.7 — i.e. the original paper's stated
configuration, so E2's primary result is measured in the regime E1
characterises. `enable_thinking` is **True** and transcripts are stored
untruncated (fixing OA-15).

## 3.3 Conditional replicate — pre-registered so it is not an unplanned analysis

*(Unchanged.)*

After E1 reports, E2's **primary contrast set is re-run once** at the
configuration E1 identifies as least artifactual — defined in advance as the
cell, among those available to a locally-served model, with the highest
post-repair D. If that cell is the primary configuration itself, the replicate is
not run and that fact is reported. The replicate's arms, R, outcome, and tests
are identical to the primary; only the generator configuration differs. This
replicate is the sole test of **C5** and its result is evaluated descriptively
(§5.3), so it does not enter the 16-test family.

## 3.4 Unit of analysis, estimand, inference — **R redefined (R3-3)**

**Unit of analysis: THE RUN, not the architecture.**

One **run** = one search of *k* = 20 proposals, under one arm, at one seed, on
one task. Selection within a run uses **validation** accuracy only. The run's
outcome is the **test** accuracy of the architecture the run selected — test
accuracy never enters selection, which fixes OA-11.

### Definition of R

> **R_final = max(20, the value `scripts/power_e2.py` confirms at S3).**
> **R_floor = 20.**

R is no longer a fixed number written into the plan. It is a **floor plus a
procedure**:

- The floor of **20** is binding and pre-registered. R may never go below it.
- `scripts/power_e2.py` runs at S3, before any E2 run executes, against a pilot
  variance estimate drawn from the benchmark's own best-of-20 distribution
  (obtainable by pure table sampling, with no generation and no training). It
  returns the smallest R giving power ≥ 0.80 for |δ| ≥ 0.62 at ALPHA.
- **If that value exceeds 20, R_final takes it, and doing so is COMPLIANCE with
  this plan, not a deviation.** No `DEVIATIONS.md` entry is required, because the
  plan registered the procedure rather than the number. The confirmed value and
  the simulation's output are recorded in `results/E2.json` as `R_final`,
  `R_floor` and `R_source`.
- **If that value is below 20, R_final is 20.** A decrease below the floor is
  forbidden outright by §8.2 and is not available on any grounds, including a
  power simulation that says fewer runs suffice.
- R_final is fixed once, before the first run, and never revised afterwards. An
  increase discovered *after* data collection has begun is a deviation, not
  compliance, and is logged as one.

This closes an asymmetry that revision 2 left open: §8.2 forbade *reducing* R
below the confirmed value, but the plan stated R = 20 as a fixed number, so a
simulation demanding more would have put compliance and the registered number in
conflict. Registering the procedure removes the conflict without loosening the
floor.

### Estimand

**Primary estimand: mean ± standard deviation of the run outcome across the
R_final runs.** This is the standard the corpus actually supports. Verbatim,
Lindauer & Hutter: *"we recommend that, if possible in terms of compute budgets,
all methods should be repeated several times with different seeds and the authors
should report mean and standard deviation (or median and quartiles if the noise
is not symmetric) across the repetitions."* Verbatim, Yang et al.: *"Report mean
and standard deviation of the top-1 test accuracy… for both the randomly sampled
and the searched architectures."*

**Best-of-k curves are reported descriptively as a secondary view only.**

> **We do NOT claim expected-best-of-*k* as a community reporting standard.** The
> S1 corpus critic (C2) checked this directly and found no source supporting it.
> The claim previously recorded in this project — that the NAS 1000-papers survey
> establishes expected-best-of-*k* as the correct estimand — is **NOT IN CORPUS**.
> The sentence that survey actually contains (*"random search with a budget of k
> evaluations will, in expectation, find architectures in the top 100/k% of the
> search space"*) is a justification for why random search is a strong baseline,
> not a reporting-standard recommendation. No downstream artifact may cite it as
> one.

Note that mean-and-std across R repeated runs **is** an empirical estimate of
E[best-of-*k*] obtained by averaging R independent best-of-*k* realisations. The
estimand is not abandoned; the *claim about what the community requires* is.

### Inference

**Permutation tests over runs.** Two-sided, exact where C(2R,R) is tractable,
otherwise 100,000 random permutations with a fixed seed recorded in the results
file. Runs are the exchangeable unit. This is the correct response to OA-12 — the
original applied Welch, Mann–Whitney and a bootstrap to *n*=20 proposals
generated with serial dependence inside one growing context. Runs are independent
by construction; proposals within a run are not, and are never treated as the
unit.

> Serial-dependence-within-one-context inference is **NOT IN CORPUS** (S1 corpus
> critic, C3). All four candidate sources address between-run / between-seed
> independence, not intra-context serial dependence. No downstream artifact may
> attribute a serial-dependence inference standard to any of them. Making the run
> the unit sidesteps the problem rather than solving it, and the paper says so.

**Effect sizes: rank-based. Cliff's δ**, with a bootstrap 95% CI (10,000
resamples, BCa). **Not** pooled-SD Cohen's *d* — OA-13 records that the original
paired Welch's *t* (unequal variances) with a pooled-SD *d* (equal variances) on
the same comparison, against a 1000:1 variance ratio. Mann–Whitney *U* is
persisted this time so δ is recoverable (fixing OA-9).

## 3.5 Power / MDE, stopping rule, budget — **AMENDED (R3-1, R3-3)**

**Confirmatory contrasts in E2 (per §5.3): 4.**

| ID | Contrast |
|---|---|
| Y1 | uncurated vs zero-shot |
| Y2 | curated vs zero-shot |
| Y3 | external archive vs zero-shot |
| Y4 | uncurated vs curated |

**MDE anchor at the floor R = 20**, α = 0.003125, two-sided permutation test:
power ≥ 0.80 for |δ| ≥ 0.62, equivalently a location shift of ≈1.05 pooled SDs.
**This is a provisional anchor, not the registered value** — the registered
quantity is the procedure in §3.4, and `scripts/power_e2.py` sets R_final.

E2's permutation test is the **unpaired** two-sample form. At R = 20 that is
C(40,20) ≈ 1.4 × 10¹¹ assignments, giving a smallest attainable two-sided *p* of
about 1.5 × 10⁻¹¹; run by Monte Carlo at 100,000 permutations the floor is
1/(1+100,000) ≈ 9.9999 × 10⁻⁶. Both clear ALPHA by orders of magnitude, so E2
carries none of the discreteness constraint that sets E1's batch count (§2.3).
The §5.2 gate checks it anyway.

The MDE is stated in standardised units only. Translating it into accuracy points
requires the benchmark's best-of-20 variance, which is not verified in the corpus
as of this writing; that translation is produced at S3 by the same script and is
not asserted here.

**Stopping rule.** R_final per arm per task, fixed before the first run. **No
interim analyses. No extension on a near-miss. No adaptive stopping.** A run that
crashes is re-executed once at the same seed; if it crashes twice it is recorded
as a failure, the arm reports R_effective < R_final, and the failure count
appears in the results file and in the manuscript's table footnote.

**Generation budget — stated as a function of R.**

| Component | Generations |
|---|---|
| E1 — 30 cells × 16 batches × 20 | **9,600** (fixed) |
| E2 primary — 4 arms × R × 20 proposals × 3 tasks | **240·R** |
| E2 conditional replicate — 4 arms × R × 20 proposals × 1 task | **80·R** |
| E3 | **0** |
| **Total** | **9,600 + 320·R generations, zero training runs** |

At the floor R = 20 that is **16,000 generations**. At R = 30 it is 19,200; at
R = 40, 22,400. **The budget is a function of a quantity the S3 simulation sets,
and this plan does not cap it.** §8 governs what may and may not be traded away
if that number comes back large.

*(Revision 1: 9,400 fixed. Revision 2: 12,400 fixed. Revision 3: 16,000 at the
floor.)*

---

# 4. Experiment E3 — the proxy size-confound replication (Case B)

*(Unchanged from revisions 1 and 2 in its entirety.)*

**Bounded scope: a validation-practice finding, not a takedown of RZ-NAS.**
Zero training. This is table computation on public data.

## 4.1 Substrate

**NAS-Bench-Suite-Zero** (Krishnakumar, White, Zela, Tu, Safari, Hutter; NeurIPS
2022 Datasets & Benchmarks). Public release: 13 zero-cost proxies × 28 tasks,
**1,526,216 pre-computed proxy evaluations** over **44,798 architectures**,
spanning NAS-Bench-101, NAS-Bench-201, NAS-Bench-301 (DARTS surrogate), and
TransNAS-Bench-101 Micro/Macro.

RZ-NAS's proxy menu is GraSP, Gradnorm, Synflow, Zen-Score, ZiCo (plus MAE-DET
for COCO detection). **Four of these five are among NAS-Bench-Suite-Zero's 13**
(grasp, grad_norm, synflow, zen-score). ZiCo is not, and cannot be — ZiCo is
ICLR 2023, the suite is 2022.

## 4.2 What E3 computes

For each proxy *p* ∈ {grasp, grad_norm, synflow, zen-score}, plus the reference
baselines {params, flops}, and for **every** (benchmark, task) pair the release
covers:

| Statistic | Definition |
|---|---|
| `rho_size` | Spearman ρ between proxy score and **parameter count** — **primary** |
| `tau_size` | Kendall τ-b, same pair |
| `pearson_size` | Pearson *r*, same pair — computed solely for comparability with NAS-Bench-Suite-Zero's own Table 3, which reports Pearson |
| `rho_cellsize` | Spearman ρ between proxy score and **cell size** (count of non-`none` operations), the suite's second size measure |
| `rho_acc` | Spearman ρ between proxy score and validation accuracy |
| `rho_acc_partial` | Spearman **partial** correlation of proxy with validation accuracy, controlling for parameter count |

Every one of these carries a bootstrap 95% CI (10,000 resamples, BCa).

`rho_acc_partial` is the quantity that actually answers the question C6 asks —
how much of a proxy's apparent validity survives removing size. A proxy whose
`rho_acc` is high and whose `rho_acc_partial` is near zero is measuring size.

**The comparison that matters** is between the benchmarks where RZ-NAS validated
(NAS-Bench-201 only, across its three built-in tasks — which are three *tasks
inside one search space*, not three benchmarks) and the benchmarks where its
headline claims live and where it never validated (DARTS / NAS-Bench-301,
TransNAS-Bench-101 Micro and Macro, NAS-Bench-101). NAS-Bench-Suite-Zero's own
RQ1 answer is the reason this matters, verbatim: *"Several methods, such as snip
and grasp, perform well on the NAS-Bench-201 tasks, but on average are
outperformed by params and flops on the other benchmarks… on the widely used
NAS-Bench-201 benchmarks, almost all of them perform well."*

## 4.3 ZiCo — handled separately, transcription only

ZiCo postdates the suite, so it is **not recomputed**. Its numbers are
**transcribed** from its own published tables: Table 1 (NATS-Bench-TSS =
NAS-Bench-201) and Table 3 (NATS-Bench-SSS, the 32,768-architecture space that
varies **only** channel width and is therefore the cleanest available isolation
of size).

Every transcribed number carries, in the results file, its source table number,
its source note ID, and a `transcribed: true` flag. **No transcribed number is
ever presented as a recomputation.** No ZiCo statistic enters any inferential
test.

## 4.4 MANDATORY CAVEATS — carried verbatim into every downstream artifact

These four paragraphs are copied verbatim into the manuscript, into any slide
deck, and into any rebuttal that raises E3. They are not paraphrased and not
compressed.

> **No size-matched ablation exists for RZ-NAS in either direction.** No published
> experiment reports RZ-NAS's search-space parameter-count distribution before
> versus after reflection, and none reports an accuracy-versus-FLOPs-matched
> comparison of its outputs. RZ-NAS's own appendix ablations cover in-context
> examples, reflection-module removal, prompt rephrasing, and selection strategy,
> and never a size-matched control. The claim that RZ-NAS's *reported gains* are
> confound-driven is therefore not established by this work or any other; what is
> established is that the proxies it optimises against carry a size confound, and
> that it never tested whether that confound is load-bearing for its results.

> **The FLOPs budget on the MobileNet-space experiments genuinely mitigates the
> flagship ImageNet claim.** RZ-NAS's MobileNet-space experiments — the source of
> its 79.0% Top-1 ImageNet number — are explicitly constrained to 450M / 600M /
> 1000M FLOPs. That rules out the crude version of "the reflection module just
> learns to propose bigger models." It constrains *total* size; it does not
> constrain the depth/width *shape* bias that ZiCo-BC documents in
> latency-and-FLOPs-matched comparisons. The mitigation is real and is stated as
> real.

> **GraSP is not size-confounded. It is only weak.** NAS-Bench-Suite-Zero's own
> bias table puts GraSP near zero on every size metric (−0.03 to 0.24 with
> parameter count; −0.01 to 0.01 with cell size), and ZiCo's independent
> NATS-Bench-SSS numbers confirm its accuracy correlation collapses toward zero or
> negative on the size-isolated benchmark — the opposite of a size-riding proxy.
> GraSP's problem is a different and less damaging one: it is a weak proxy
> (Kendall τ 0.36–0.40 on NAS-Bench-201, below even the naive #Params baseline's
> 0.52–0.57). E3 must not report GraSP as confounded.

> **MAE-DET's size-confound status is UNKNOWN, not clean.** RZ-NAS's COCO
> detection proxy is evaluated by no source in the corpus — not
> NAS-Bench-Suite-Zero, not ZiCo, not ZiCo-BC, where its only appearance is a
> bibliography entry. It is outside E3's scope and must not be characterised in
> either direction.

## 4.5 Prohibited

> **The Zen-Score Kendall-tau self-report discrepancy is UNUSABLE and must not
> appear in any artifact.** Zen-NAS's self-reported τ = 0.91 / 0.88 is computed
> over **n = 16** structures sampled from a single ResNet-50 parent; the 0.28–0.29
> figures are computed over **n = 15,625** NAS-Bench-201 architectures. Different
> populations, different scales, incomparable point estimates. Further, the two
> low figures are **not independent reproductions**: RZ-NAS reused ZiCo's
> published table verbatim, matching to two decimals across every cell, so
> "two independent sources agree" is also false. The finding is struck. It does
> not appear as evidence, as an aside, or in an appendix.

E3 runs **no inferential tests** and is **not** in the confirmatory family. It
reports point estimates with confidence intervals. C6's threshold
(`rho_size ≥ rho_acc` for ≥2 proxies off NAS-Bench-201) is evaluated by comparing
point estimates and their CIs, and is reported as met or not met, with the CIs
shown.

---

# 5. Analysis protocol and deviation rules

## 5.1 Every statistic to be computed, named in advance

| ID | Experiment | Statistic | Kind |
|---|---|---|---|
| A1 | E1 | D per batch (mean pairwise structural diversity) | descriptive |
| A2 | E1 | D per cell: mean ± std across **16** batches | descriptive |
| A3 | E1 | parse-failure rate per cell | descriptive |
| A4 | E1 | normalised per-field entropy, per field × stage × cell | descriptive |
| A5 | E1 | repair-channel counts (passthrough / coerced / filled) per field × cell | descriptive |
| A6 | E1 | D_rand (random-sampler reference) | descriptive |
| A7 | E1 | rival signature score, 5 rivals × 3 models | classification |
| **X1** | E1 | free-prose vs schema, post-repair, NF4, T=0.7 — paired permutation over batch index | **confirmatory** |
| **X2** | E1 | schema pre-repair vs post-repair — paired permutation over batch index | **confirmatory** |
| **X3** | E1 | NF4 vs bf16, schema post-repair, T=0.7 — paired permutation | **confirmatory** |
| **X4** | E1 | T=0.3 vs T=1.0, schema post-repair, NF4 — paired permutation | **confirmatory** |
| A8 | E2 | run outcome: mean ± std per arm × task | descriptive |
| A9 | E2 | best-of-*k* curve per arm × task | descriptive, secondary view |
| A10 | E2 | Mann–Whitney *U* per contrast (persisted, fixing OA-9) | descriptive |
| A11 | E2 | Cliff's δ + BCa 95% CI per contrast | effect size |
| **Y1** | E2 | uncurated vs zero-shot, primary task, permutation | **confirmatory** |
| **Y2** | E2 | curated vs zero-shot, primary task, permutation | **confirmatory** |
| **Y3** | E2 | external archive vs zero-shot, primary task, permutation | **confirmatory** |
| **Y4** | E2 | uncurated vs curated, primary task, permutation | **confirmatory** |
| A12 | E2 | all four contrasts on the two secondary tasks | exploratory, no p-values reported |
| A13 | E2 replicate | arm ordering + pairwise CIs at the E1-identified configuration | descriptive |
| A14 | E3 | rho_size, tau_size, pearson_size, rho_cellsize, rho_acc, rho_acc_partial, each with BCa 95% CI, per proxy × benchmark × task | descriptive |
| A15 | E3 | C6 threshold evaluation | classification |
| A16 | E1 | `D_cell_pooled` + BCa 95% bootstrap interval, per cell × stage | descriptive |
| A17 | E1 | BCa 95% bootstrap interval on ΔD for the `bf16` and `high temp` contrasts | descriptive |
| A18 | E1 | `S` per batch and `S_mean ± S_std` per cell, plus `S_cell_pooled` with BCa interval | descriptive |
| A19 | E1 | boundary-straddle flags: which cells were scored `indeterminate` by §2.6's bootstrap rule | classification |
| **A20** | all | `min_attainable_p` per confirmatory test, planned and realised, plus the §5.2 gate verdicts *(new, R3-2)* | gate / audit |

**Confirmatory tests: X1–X4 across 3 models = 12, plus Y1–Y4 = 4. Total 16.**
A16–A20 are descriptive, classification, or gate records and carry no p-value.
**The count is unchanged from revisions 1 and 2.**

## 5.2 Multiplicity correction and the pre-flight gates — **AMENDED (R3-2)**

- **Family:** the 16 confirmatory tests named in §5.1 — X1, X2, X3, X4 (each
  evaluated once per model: Qwen3-1.7B, Qwen3-8B, frontier) and Y1, Y2, Y3, Y4
  (each evaluated once, on the primary task only).
- **Procedure:** Bonferroni.
- **FAMILY_SIZE = 16.**
- **ALPHA = 0.05 / 16 = 0.003125.**

No amendment in revision 3 adds, removes, or reclassifies a confirmatory test.
The per-amendment check is tabulated in the amendment record at the head of this
file.

Holm–Bonferroni was considered and rejected. It is uniformly more powerful at the
same FWER, but it yields a step-down sequence rather than a single number, and
the defect this plan exists to prevent (OA-5: the manuscript declared 0.05/7
while the code applied 0.05/15) is a *number-matching* defect. A single stated
constant that a script can assert against is worth more here than the power.

### Gate 1 — family and alpha (unchanged)

The analysis emitter:
1. reads `FAMILY_SIZE = 16` and `ALPHA = 0.003125` from a single module-level
   constant, which is the same constant this document states;
2. writes `alpha_applied` onto **every** emitted statistic;
3. asserts that the count of emitted statistics with `confirmatory: true` is
   exactly 16 — and **aborts** otherwise;
4. asserts that every `alpha_applied` equals the top-level `alpha` — and
   **aborts** otherwise.

X3 is undefined for the frontier model (no precision factor). Its slot in the
family is retained and emitted as `{"status": "not_applicable", "confirmatory":
true, "p": null}` so the count stays exactly 16 and the family size stated here
matches the family size the code enforces. Shrinking the family after the fact is
the failure mode being guarded against.

### Gate 2 — the permutation floor is FATAL — **NEW (R3-2)**

**Defect class being closed.** Revision 1 registered E1 at 5 batches per cell.
A paired sign-flip permutation test over 5 differences admits a smallest
two-sided p-value of 2/2⁵ = **0.0625**, twenty times ALPHA. Contrasts X1–X4 were
**structurally incapable of rejecting, whatever the data showed** — a
confirmatory test set that was undecidable by construction, registered and
hashed without the defect being visible. Revision 2 fixed the instance by raising
the batch count; revision 3 closes the **class**, so that no future revision, no
deviation, and no run-time degradation can reintroduce an undecidable
confirmatory test silently.

**The plan-load arm — hard abort, before any data is read.**

At emitter start-up, before a single results file, generation log or benchmark
table is opened, the emitter:

5. computes `min_attainable_p` for **every** confirmatory test in the family,
   from the plan's declared design alone:
   - **paired exact:** `2 / 2^B`, where *B* is the planned paired count (16 for
     E1's X-contrasts);
   - **unpaired exact:** `2 / C(n₁+n₂, n₁)`;
   - **Monte-Carlo:** `1 / (1 + n_permutations)`, the floor of the standard
     `(1 + #extreme) / (1 + N)` estimator;
   - **`not_applicable` slots:** exempt, and recorded as exempt;
6. **ABORTS if any confirmatory test has `min_attainable_p ≥ ALPHA`**, naming the
   offending test, its *B* or *n*, its floor, and ALPHA;
7. records every computed floor and the gate verdict in the results file
   (`discreteness_gate`, §5.5), pass or fail, so the check is auditable after the
   fact rather than only in a log.

Gate 2 sits alongside gates 1.3 and 1.4 and has the same standing: an assertion
that halts the emitter, not a warning. **Its planned values at this revision:**

| Test class | Design | `min_attainable_p` | vs ALPHA |
|---|---|---|---|
| E1 X1–X4, paired | *B* = 16 | 0.0000305 | 0.98% of ALPHA — pass |
| E1 X-contrasts, unpaired fallback | 16 vs 16 | 3.33 × 10⁻⁹ | pass |
| E2 Y1–Y4, exact at R = 20 | 20 vs 20 | 1.45 × 10⁻¹¹ | pass |
| E2 Y1–Y4, Monte Carlo | N = 100,000 | 9.9999 × 10⁻⁶ | 0.32% of ALPHA — pass |

**The run-time arm — no silent degradation.**

Null batches (§2.7) and failed runs (§3.5) reduce the *realised* count below the
planned one, which raises the floor after the plan-load gate has already passed.
So the emitter also:

8. recomputes `min_attainable_p` from the **realised** usable count for every
   confirmatory test, and emits it as `min_attainable_p_realised` beside the
   planned value;
9. where `min_attainable_p_realised ≥ ALPHA`, emits that contrast with
   `status: "undecidable_by_discreteness"` and `significant: null` — **never
   `significant: false`** — and the manuscript reports it as undecidable rather
   than as evidence of no effect.

The run-time arm does not abort: a single degraded cell should not destroy an
otherwise valid analysis. It refuses to let a degraded cell be *read as a null*,
which is the actual hazard. The plan-load arm aborts, because a floor violation
there is a design error and there is nothing to salvage.

**Reporting.** Every paired p-value that reaches the manuscript is accompanied by
its `min_attainable_p`. A9–A20 are descriptive, classification, or gate records
and carry no p-value.

## 5.3 Confirmatory vs exploratory

E2's conditional replicate (§3.3) tests C5 through **A13**, which is descriptive
(arm ordering plus pairwise CIs), not a null-hypothesis test. C5 is therefore
evaluated by CI overlap and ordering, not by a p-value, and does not enter the
16-test family. This is stated so that adding a test for it later would be a
visible deviation.

The same applies to A16–A20: they emit intervals, flags and gate verdicts, never
p-values. Adding a p-value to any of them would be a deviation requiring a
`DEVIATIONS.md` entry **and** — because it would change FAMILY_SIZE — would have
required a further revision, which after G2 is signed is no longer available.

## 5.4 No-unplanned-analyses rule

**Any analysis not named in §5.1 is exploratory.** An exploratory analysis:
- must be labelled "exploratory" at every point of use;
- **may not** carry a p-value or a significance marker;
- **may not** appear in the abstract, in the contributions list, or in the
  conclusions;
- must be logged in `DEVIATIONS.md` before it is run.

This includes subgroup breakdowns, alternative metrics, alternative thresholds,
re-analysis at a different alpha, and any comparison suggested by looking at the
data.

## 5.5 Results-file schema

Every number destined for the manuscript is emitted by a script into a versioned
results file. **No number is transcribed by hand.** One file per experiment:
`results/E1.json`, `results/E2.json`, `results/E3.json`, plus
`results/E1_reference.json`.

**`schema_version` is `1.2.0` in revision 3** (revision 1: `1.0.0`; revision 2:
`1.1.0`). All changes are additive — every earlier key is retained with the same
meaning.

```json
{
  "schema_version": "1.2.0",
  "experiment": "E1",
  "plan_revision": 3,
  "plan_sha256": "<SHA-256 of EXPERIMENT_PLAN_R3.md at freeze>",
  "plan_supersedes_sha256": "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1",
  "plan_chain_sha256": [
    "aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d",
    "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1"
  ],
  "code_commit": "<git rev-parse HEAD>",
  "generated_at": "<ISO-8601 UTC>",
  "environment": {
    "python": "", "torch": "", "transformers": "",
    "bitsandbytes": "", "cuda": "", "gpu": "", "driver": ""
  },
  "model": {
    "requested": "", "served": "", "revision": "",
    "quantisation": "", "enable_thinking": true,
    "max_new_tokens": 0, "truncation_chars": null
  },
  "prompts": { "<name>": "<sha256 of frozen prompt file>" },
  "seeds": [7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
            7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016],
  "n_batches_per_cell": 16,
  "bootstrap": { "resamples": 10000, "method": "BCa", "seed": 90210,
                 "resampling_unit": "generation" },
  "confirmatory_family_size": 16,
  "alpha": 0.003125,
  "discreteness_gate": {
    "checked_at": "plan_load",
    "verdict": "pass",
    "alpha": 0.003125,
    "per_test": [
      {"id": "X2.qwen3-1.7b", "mode": "paired_exact", "n_planned": 16,
       "min_attainable_p": 0.000030518, "pass": true}
    ]
  },
  "cells": [
    {
      "cell_id": "",
      "factors": {"model": "", "format": "", "precision": "", "temperature": 0.0},
      "seed_honoured": true,
      "batches": [
        {"batch": 0, "seed": 7001, "n": 20,
         "parse_failures": 0,
         "D_pre": null, "D_post": null,
         "S": null, "empty_trigram_count": 0,
         "field_entropy_pre": {}, "field_entropy_post": {},
         "repair_channels": {"<field>": {"passthrough": 0, "coerced": 0, "filled": 0}}}
      ],
      "D_pre_mean": null, "D_pre_std": null,
      "D_post_mean": null, "D_post_std": null,
      "D_pre_pooled": null, "D_pre_pooled_ci95": [null, null],
      "D_post_pooled": null, "D_post_pooled_ci95": [null, null],
      "S_mean": null, "S_std": null,
      "S_pooled": null, "S_pooled_ci95": [null, null],
      "null_batches": 0, "null_S_batches": 0,
      "label_pre": "", "label_post": "",
      "boundary_straddle": false,
      "status": "ok"
    }
  ],
  "statistics": [
    {
      "id": "X2.qwen3-1.7b",
      "kind": "paired_permutation",
      "contrast": "schema_pre_repair vs schema_post_repair",
      "paired": true,
      "permutation_mode": "exact",
      "n_pairs_planned": 16, "n_pairs_realised": 16,
      "n_permutations": 65536,
      "min_attainable_p_planned": 0.000030518,
      "min_attainable_p_realised": 0.000030518,
      "estimate": null, "ci95": [null, null],
      "delta_ci95_boot": [null, null],
      "p": null, "alpha_applied": 0.003125,
      "confirmatory": true, "significant": null,
      "effect": {"metric": "cliffs_delta", "value": null,
                 "ci95": [null, null], "u_stat": null},
      "status": "ok"
    }
  ],
  "signature_match": {
    "<model>": {"repair_artifact": 0, "format_tax": 0, "quantisation": 0,
                "decoding": 0, "genuine_prior": 0,
                "indeterminate_columns": [],
                "winner": "", "verdict": ""}
  },
  "na_counts": {},
  "failures": []
}
```

New in `1.2.0`: `plan_chain_sha256`, `discreteness_gate` (with `per_test[]`),
`permutation_mode`, `n_pairs_planned`, `n_pairs_realised`,
`min_attainable_p_planned`, `min_attainable_p_realised`, and the
`undecidable_by_discreteness` value for `status`. `n_batches_per_cell` is 16 and
`seeds` has sixteen entries.

`results/E2.json` additionally carries `R_floor`, `R_final`, `R_source` (the
`scripts/power_e2.py` output that set it) and `R_effective` per arm. It and
`results/E3.json` share `schema_version`, the header block, `statistics[]`,
`discreteness_gate`, `na_counts` and `failures`, and replace `cells[]` with
`runs[]` and `correlations[]` respectively. E3's entries additionally carry
`transcribed: true|false`, `source_table`, and `source_note_id`.

**Manuscript binding rule.** No numeric literal is typed into the `.tex`. Every
number resolves to a `results/<exp>.json` key through a lookup macro, and a
checker script verifies at build time that every numeric token in the manuscript
body has a resolvable key. This is the G5 criterion and it is stated here so the
results-file layer is designed before the data exists rather than after.

## 5.6 DEVIATIONS.md protocol

*(Unchanged. Rule 4 is the authority under which this revision was written, and
it closes when G2 is signed — see the masthead.)*

`DEVIATIONS.md` carries no deviation entries as of revision 3's hash.

1. **Any departure from this plan is logged in `DEVIATIONS.md` BEFORE the
   analysis it affects is run.** Not after. Not at write-up.
2. Each entry carries: date, plan section affected, what changed, why, and
   **whether data had already been collected for the affected analysis at the
   time of the entry.**
3. An entry added *after* the affected analysis has run is itself a protocol
   violation, and must be labelled `LATE — PROTOCOL VIOLATION` in its own
   heading. It is not deleted or quietly backdated.
4. **This plan is not edited after its hash is taken.** Changes go in
   `DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
   written as a new file, hashed separately, and cites the prior hash it
   supersedes; every superseded plan file stays in the repository byte-identical
   to the version that was hashed. **This revision route closes when G2 is
   signed**; thereafter every change is a deviation entry.
5. Every deviation entry is committed before the run it governs, so git history
   independently timestamps the ordering.

---

# 6. Citations the paper is obliged to carry

*(Unchanged.)*

Sourced from `audit/references_verified.bib`, never from memory.

**Eight of the thirteen named works are not in that file** — ten of fifteen once
the four structured-decoding papers and ZiCo/ZiCo-BC are counted separately. They
post-date the S0 bibliography audit, which verified the *manuscript's existing* 47
entries and did not add new ones. Their metadata below is taken from vault notes
— fetched source records, not recall — with the note ID given so each is
traceable. **They must be added to `audit/references_verified.bib`, verified
against an academic API, before S6 writing.** That is logged as OA-38.

| # | Work | Status | Key / source |
|---|---|---|---|
| 1 | **EvoPrompting** — Chen, Dohan, So | in bib | `chen2023evoprompting` |
| 2 | **GENIUS** — Zheng et al., "Can GPT-4 Perform Neural Architecture Search?" | in bib | `zheng2023genius` |
| 3 | **LLMatic** — Nasir et al. | in bib | `nasir2024llmatic` |
| 4 | **Li & Talwalkar** — Random Search and Reproducibility for NAS, UAI 2019 | in bib | `li2020random` |
| 5 | **Yang et al.** — NAS Evaluation is Frustratingly Hard, ICLR 2020 | in bib | `yang2020evaluating` |
| 6 | **CoLLM-NAS** — Collaborative LLMs for Efficient Knowledge-Guided NAS. **Accepted as Oral, CVPR 2026 Workshop on NAS.** | **ABSENT** | arXiv:2509.26037v2 — note `250926037v2-collm-nas-collaborative-large-language-models-for-efficient-knowledg` |
| 7 | **RZ-NAS** — Ji et al., Enhancing LLM-guided NAS via Reflective Zero-Cost Strategy, **ICML 2025, PMLR v267** | **ABSENT** | `https://proceedings.mlr.press/v267/ji25a.html` — note `icml-poster-rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflectiv` (full text, 11,395 words) |
| 8 | **The Format Tax** (structured decoding, prompt-vs-decoder split) | **ABSENT** | arXiv:2604.03616 — note `260403616-the-format-tax` |
| 9 | **Let Me Speak Freely?** — Tam et al., format restrictions degrade reasoning | **ABSENT** | arXiv:2408.02442 — note `240802442-let-me-speak-freely-a-study-on-the-impact-of-format-restrictions-on-pe` |
| 10 | **Grammar-Aligned Decoding** — GCD distorts the LLM distribution | **ABSENT** | arXiv:2405.21047 — note `240521047-grammar-aligned-decoding` |
| 11 | **The Parser Already Knows** — lightweight bias correction in constrained decoding | **ABSENT** | arXiv:2608.10137 — note `260810137-the-parser-already-knows-lightweight-bias-correction-in-constrained-de` |
| 12 | **NAS-Bench-Suite-Zero** — Krishnakumar, White, Zela, Tu, Safari, Hutter; NeurIPS 2022 D&B | **ABSENT** | arXiv:2210.03230 — note `221003230-nas-bench-suite-zero-accelerating-research-on-zero-cost-proxies` |
| 13 | **ZiCo** — Li et al., ICLR 2023 Spotlight | **ABSENT** | arXiv:2301.11300 — full-text note `zico-zero-shot-nas-via-inverse-coefficient-of-variation-on-gradients-full-text` |
| 14 | **ZiCo-BC** — Bhardwaj et al., ICCV Workshop 2023 | **ABSENT** | arXiv:2309.14666 — full-text note `zico-bc-a-bias-corrected-zero-shot-nas-for-vision-tasks-full-text` |
| 15 | **Lindauer & Hutter** — Best Practices for Scientific Research on NAS | **ABSENT** | arXiv:1909.02453v3 — note `190902453v3-best-practices-for-scientific-research-on-neural-architecture-search` |

Every one is load-bearing: rows 8–11 establish the mechanism this paper applies
(and therefore establish what it may *not* claim, §1.2); rows 12–14 are E3's
entire evidence base; row 15 is the only citable source in the corpus for E2's
estimand.

**Also obliged, though not on the original list**, because the plan leans on them
directly: **NAS-Bench-201** (Dong & Yang, `dong2020nasbench201`, in bib) as E2's
substrate, **NAS-Bench-101** (`ying2019nasbench101`, in bib) and the **NAS
1000-papers survey** (`white2023nas`, in bib) — the latter cited *only* for its
random-search-baseline point, never as an estimand recommendation (§3.4).

---

# 7. What this plan does not do

*(Unchanged.)*

Recorded so the boundary is explicit and cannot be quietly crossed.

- **It does not recover the original data.** OA-1 is closed. Every ORPHAN finding
  in `audit/CLAIM_TRACE.md` is permanent. Nothing in E1–E3 re-establishes any
  number in the current manuscript.
- **It does not train anything.** E1 is generation and structural measurement.
  E2 is generation plus table lookup. E3 is table computation. Total training
  runs: zero.
- **It does not settle whether CoLLM-NAS's noise-accumulation ablation has been
  independently replicated.** Five candidate citing papers are unverified leads
  (OA-37 in `audit/OPEN_ACTIONS.md`). None may be cited as corroboration until
  fetched and read.
- **It does not resolve the generating model of the original run.** OA-3 stands
  and is unresolvable; the manuscript will say the original generating model is
  unknowable and that E1–E3 use models recorded in metadata at generation time.
- **It does not test MAE-DET**, the DARTS-space parameter-range question L5 left
  open, or the GENIUS Appendix A.3 tables L1 sampled only partially (seam S3 —
  a full pass could still surface a trajectory where the final iteration nets
  worse than zero-shot, which would restore GENIUS as an independent second
  scoop; that pass is an S3 task).

---

# 8. Scope protection

## 8.1 The calendar consideration: CONSIDERED AND REJECTED

*(Unchanged from revision 2.)*

At the time revision 1 was written, the nearest workshop deadline was twelve days
away, and the runway was flagged as a risk. **That consideration has been
examined and rejected as an input to scope.**

**This project plans on merit and scope. It does not plan around submission
dates. The venue follows the artifact, not the reverse.**

1. **The chosen venue is non-archival** (`VENUE.md`). Missing a cycle costs
   **nothing** — no priority, no publication window, no claim to the result.
2. **Workshop cycles recur.** A design weakened to fit a date is permanent; a
   date missed is not.
3. **The failure this whole project exists to correct was produced by exactly
   this pressure.** The original manuscript's defects — an unrecoverable dataset,
   a declared correction that did not match the applied one, "pre-specified"
   comparisons that were computed exhaustively, a replication subsection with no
   evidentiary basis — are the signature of work shaped by a deadline rather than
   by a design.
4. **Every revision so far has raised the budget, not lowered it** — 9,400 →
   12,400 → 16,000 at the floor — because each raise was what made a confirmatory
   test decidable. That is the precedent this section fixes: **when rigour and the
   calendar conflict, rigour wins, and the budget moves.**

## 8.2 What this forecloses — **R clause amended (R3-3)**

The following are **not** available as scope reductions and may not be proposed
at S4, or at any later stage, on schedule or budget grounds:

- dropping E1 cells, batches, or generations per batch — **including any
  reduction of *B* below 16**, which must argue against the ceiling table in
  §2.3 and against the fatal gate in §5.2, not against the cost;
- dropping E2's secondary tasks (§3.1);
- dropping E2's conditional replicate (§3.3), which is the sole test of C5;
- **reducing R below `R_final = max(20, the S3-confirmed value)`.** The floor of
  20 binds independently: a power simulation returning a value *below* 20 does
  not license going below 20. A simulation returning a value *above* 20 raises
  R_final, and complying with that raise is compliance, not a deviation (§3.4);
- narrowing the confirmatory family, which would change ALPHA (§5.2).

A genuine scope change on **methodological** grounds remains available — this
section constrains the *reason*, not the possibility. Before G2 is signed such a
change is a further revision; after G2 is signed it is a `DEVIATIONS.md` entry
logged before the affected work, and the revision route is closed.

## 8.3 What is legitimately schedule-sensitive

Nothing in the experimental design. Two things outside it are, and are handled at
their own stages: fetching and byte-verifying `neurips_2026.sty` from two mirrors
(S6), and closing OA-37 and OA-38 before S6 writing. Neither touches E1, E2 or
E3.
