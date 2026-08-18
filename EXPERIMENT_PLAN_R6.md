# EXPERIMENT PLAN — pre-registered — **REVISION 6**

**Revision:** 6 — **the last revision before G2**
**Written:** 2026-08-18
**Supersedes:** `EXPERIMENT_PLAN_R5.md` (revision 5),
SHA-256 `e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201`
**Chain:** rev 1 `aeb174ff…bad3d` → rev 2 `a9954ba3…1df1` → rev 3 `be61bda9…df03`
→ rev 4 `738601db…cc9d` → rev 5 `e3206e71…b201` → **rev 6**

Revisions 1–5 remain in the repository **byte-identical**. All five hashes were
re-verified immediately before this revision was written and again after it was
committed.

**Authority:** revision 5 §5.6 rule 4 — a wholesale supersession is a numbered
revision written as a new file, hashed separately, citing the prior hash; every
superseded plan file stays byte-identical.

**Why there is a revision 6, and why it is the last.** S3c ran the two registered
pilots and specified the cross-level exemplar predicate. Its scope is **closed by
construction**: it carries the two pilot-confirmed design parameters, the
cross-level predicate, and the corrected pilot criterion. **Nothing else.** Five
revisions in two days each added machinery that generated further defects; that
growth is what this revision stops. Every other ambiguity S3c found is recorded in
`audit/S3C_DEFECTS.md` and, after G2, is handled as a `DEVIATIONS.md`
implementation decision rather than a plan change.

**Status:** no data collected. The pilots are **simulation over synthetic draws**
— no model, no training, no benchmark query — and their output sets design
parameters only. Both are marked `pilot: true`, `confirmatory: false`,
`quarantined_from_analysis: true`, and neither may be analysed for any claim or
enter the confirmatory corpus.

**Section numbering is preserved** from revisions 1–5. §2.5a is new.

---

## Amendment record — revision 5 → revision 6

| ID | Amendment | Sections |
|---|---|---|
| **R6-1** | **`R_final = 24`** and **`B_tracking = 28`**, both confirmed by the registered pilots (§3.4, §2.8). Power at the R floor of 20 is **0.702**, below the 0.80 target, so raising R is **compliance**, not a deviation. | §2.8, §3.4, §3.5 |
| **R6-2** | **The cross-level exemplar predicate** (new §2.5a). The rival predicates now read `tracks_first` at both stages plus the cross-level delta; single-cell `tracks_exemplar` is still emitted but **no predicate reads it**. Registered as **descriptive** — it adds no confirmatory test. | §2.5, §2.5a, §2.6, §5.1, §5.5 |
| **R6-3** | **The B_tracking pilot criterion is corrected.** Revision 5 asked for a half-width below 0.15 at a true rate of 0.40 — an interval of [0.25, 0.55], which **contains** the chance rate 0.263889 and therefore reads `no tracking`. The criterion would have certified a width that cannot detect the effect it exists to detect. | §2.8 |

**Family check. FAMILY_SIZE = 17; ALPHA = 0.05/17 = 0.0029411764705882353 —
unchanged.** R6-2 adds a column entry that is classified **descriptively by CI
position**, exactly as the other tracking labels are, so it adds no confirmatory
test. R6-1 changes sample sizes, not test counts. Every floor was re-run (§5.2)
and every one clears.

**The S3b defects are dispositioned in §9; the S3a defects in §10.** Revisions 4
and 5 keep their own amendment records in their own files, which remain
byte-identical.

---
# 1. Thesis and claim set

## 1.1 Thesis

*(Unchanged.)*

> **In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.**

"Measurement apparatus" means, concretely and exhaustively: the prompt's format
demand, the output parser, the schema-repair / sanitiser stage, the decoding
constraint, the sampling temperature, the weight precision at which the generator
is served, and — new at revision 4 — **the order in which the search space is
enumerated to the model, and the exemplar shown in context**. It does not mean
the training data, the model architecture, or the model's scale.

## 1.2 Novelty framing — binding constraint on all downstream writing

*(Unchanged from revisions 1–3.)*

**We claim the APPLICATION of an established mechanism to LLM-guided NAS. We do
NOT claim to discover that structured decoding or output repair distorts
measurement.**

The general mechanism is already published and active 2024–2026 literature; four
sources establish it (§6, rows 8–11). What is not published anywhere the S1
corpus critic could find — across a vault sweep and a targeted arXiv wave
(`abs:"neural architecture search" AND abs:"constrained decoding"` → 0 hits;
`abs:"neural architecture search" AND abs:"parser"` → 1 irrelevant hit;
`abs:"evaluation harness" AND abs:"confound"` → 0 hits) — is the NAS-scoped
instantiation: that parser / sanitiser / schema-repair artifacts in an LLM-guided
NAS pipeline are responsible for an observed "collapse to a single template" or an
observed feedback-degradation effect.

**Defect rule.** Any sentence in any downstream artifact that claims the
*mechanism* rather than the *application* is a defect. Defects:

- "We show that constrained decoding distorts LLM output distributions."
- "We introduce the idea that the harness, not the model, produces the measured effect."
- "Prior work has not considered that output repair can confound measurement."

Correct:

- "We apply a mechanism established for reasoning and code benchmarks
  [format-tax, grammar-aligned-decoding] to architecture search, where it has not
  been tested."
- "The distortion mechanism is known; its magnitude in an LLM-guided NAS pipeline
  is not, and it has not previously been separated from the model's own prior in
  this setting."

A pre-submission grep for the defect pattern is a G7 requirement.

**New at revision 4, and it strengthens the constraint.** The anchor-tracking
manipulation (§2.8) is an *enumeration-order and exemplar* probe. Order effects
and in-context exemplar effects on LLM output are themselves established
literature. **We claim neither.** What we claim is that in an LLM-guided NAS
pipeline the observed "narrow prior" can be shown to track the *harness's*
enumeration order rather than the model's preference — an application, on the same
footing as the rest.

## 1.3 Claims abandoned

*(Unchanged from revisions 1–3.)*

| Abandoned claim | Killed by |
|---|---|
| **"Iterative feedback degrades LLM-guided NAS"** (unqualified) | S1 / L1. Refuted by two controlled ablations running the other way: RZ-NAS (ICML 2025) reflection ablation, and EvoPrompting's feedback ablation. GENIUS's own per-trial Appendix A.3 tables show feedback beating zero-shot in every reported trajectory. The mechanism-specific survivor is SCOOPED by CoLLM-NAS (CVPR 2026 NAS Workshop, Oral), whose Generator-memory ablation reports uncurated in-context history "induces progressive noise accumulation, leading to performance degradation." |
| **"The LLM encodes a strong narrow prior"** | S0 / OA-8, `audit/FORENSICS.md` F1. `sanitize_config` ([run_v2.py:52-67](src/run_v2.py#L52)) coerces every out-of-vocabulary field to the first legal value — `standard_3x3` / `relu` / `batchnorm` / `identity` / `maxpool` — and fills every *absent* field with the same defaults. That template is exactly the reported "narrow prior." It runs on the LLM arms only, never the random arms, so the two arms were not measured with the same instrument. |
| **"Parameter std = 0K"** | S0 / OA-4. ORPHAN. Quoted in abstract, Results, Discussion and Conclusion; no artifact contains it and no code computes it. |
| **"Zero causal attributions reflects model capacity"** | S0 / OA-15. `enable_thinking=False` ([llm_server_small.py:43](src/llm_server_small.py#L43)) and 2000-character transcript truncation ([run_v2.py:194](src/run_v2.py#L194)). A causal attribution the model did emit could not have survived either step. Compounded by OA-16: `finish_reason` hardcoded `"stop"`. |
| **The seed-137 replication** (all six numbers) | S0 / OA-24. All ORPHAN. |
| **"Pre-specified" for the seven comparisons** | S0 / OA-23. The script computes all C(6,2)=15 pairs exhaustively; no pre-registration artifact ever existed. |
| **"Evaluates it on the test set only once"** | S0 / OA-20. Contradicted by Algorithm 1 line 7 and by the code. Compounded by OA-11: top-5 retraining selects on `test_acc` inside the block labelled the "no leakage" fix. |
| **Every number in the current Tables 1–6** | S0 data census. 0 RAW / 0 SPEC / 0 TRANSCRIPT across all 24 cells. Stars computed at α=0.05/15 and reported against α=0.05/7 (OA-5); the B-vs-C cell is unresolvable inside its own rounding interval (OA-6). |

Also abandoned as consequences: the prose claim of "20 structurally identical
designs" (self-contradicted by the Jaccard 0.022 in the same sentence), and the
framing that condition D's feedback "hurts" (D holds the best architecture on both
datasets).

## 1.4 Claims proposed

**C1 — Repair concentrates the design distribution.**
*At the anchor configuration, the post-repair design-choice distribution is
materially more concentrated than the pre-repair distribution over the same
generations.*
- Tested by: E1 contrast **X2**, paired within generation.
- Refuted by: `D_post ≥ D_pre − 0.10·D_rand`.

**C2 — An apparatus factor dominates the model's own prior.**
*At least one measurement-apparatus factor (prompt format, repair, precision,
decoding temperature, **enumeration order, in-context exemplar**) accounts for
more of the observed concentration than the residual attributable to the model.*
- Tested by: E1 six-column signature match (§2.5–2.6), of which the
  anchor-tracking column (§2.8) is the one that does **not** depend on free prose
  parsing.
- Refuted by: the **genuine prior** row wins the signature match, **or** the
  winner fails the §2.6 scoring threshold.

**C3 — The effect is not an artifact of model scale.**
*The direction of the free-prose → schema concentration effect is the same at
Qwen3-1.7B, Qwen3-8B and a frontier API model.*
- Refuted by: that contrast is "no change" at 8B or frontier while "collapsed" at
  1.7B.

**C4 — Uncurated accumulation does not beat curation.**
- Tested by: E2 contrast **Y4**, primary task (CIFAR-100).
- Refuted by: uncurated > curated with p < ALPHA and Cliff's δ > 0.
- **A replication-in-a-new-regime claim, not a discovery claim.** CoLLM-NAS has
  the finding; the regime (small, quantised, single model) is what is new.

**C5 — Measurement configuration changes the arm ordering.**
- Tested by: E2 primary + conditional replicate (§3.3), evaluated descriptively.
- Refuted by: identical arm ordering with overlapping 95% CIs on every pairwise
  difference.
- **This claim carries the thesis.** If C5 fails, the contribution reduces to
  C1–C3 plus E3 and §1.1 must be weakened to a generation-stage statement.

**C6 — RZ-NAS's proxy menu is size-tracking off NAS-Bench-201.**
- Tested by: E3 on NAS-Bench-Suite-Zero's public release.
- Refuted by: fewer than two of {GraSP, Gradnorm, Synflow, Zen-Score} meet the
  condition.
- A **validation-practice finding**, not a takedown. §4.4's caveats bind.

**Thesis-level.** Asserted only if **C2 ∧ C5**. If C2 holds and C5 fails, the
paper reports a generation-stage result and says plainly it did not establish the
feedback-level consequence. If C2 fails, the thesis is withdrawn and the null
reported.

---

# 2. Experiment E1 — the discrimination factorial

**Inference-only. No training. No architecture is evaluated for accuracy in E1.**

## 2.1 Factors

*(Unchanged. §2.8 adds a separate sub-design at the anchor configuration only.)*

| Factor | Levels | Notes |
|---|---|---|
| **prompt format** | free-prose \| schema-constrained JSON | Both prompts frozen in `prompts/E1/` and hashed into the results file. |
| **precision** | NF4 4-bit \| bf16 | Local models only; not manipulable on a hosted API (§2.2, D-04). |
| **temperature** | 0.3 \| 0.7 \| 1.0 | top_p 1.0, top_k disabled, no repetition penalty, `enable_thinking` **True**. |
| **model** | Qwen3-1.7B (anchor) \| Qwen3-8B (scale) \| frontier API (ceiling) | Frontier model ID and served revision recorded in the results file. |

**Repair stage is not a factor.** Every generation is scored twice — pre-repair
and post-repair — paired within generation. Three stages are logged:

1. **raw** — response text, untruncated, with the server's true `finish_reason`.
2. **pre-repair** — the parsed JSON object, before `sanitize_config`. May not exist.
3. **post-repair** — after `sanitize_config`.

A generation that fails to parse is excluded from **both** stages, so the pre/post
contrast always runs over an identical set and the parse-selection effect is
identical at both stages (**D-05**).

## 2.2 Cell grid

| Model | format × precision × temperature | Cells |
|---|---|---|
| Qwen3-1.7B | 2 × 2 × 3 | 12 |
| Qwen3-8B | 2 × 2 × 3 | 12 |
| Frontier API | 2 × — × 3 | 6 |
| **Main grid** | | **30** |
| Anchor-tracking sub-design (§2.8) | 2 orders × 2 exemplars × **3 models** | **12** |
| **Total** | | **42** |

**R5-2: the tracking sub-design runs at all three models.** Revision 4 scoped it
to the anchor configuration only, which meant the sixth prediction column existed
for one model and `n_s` fell to 5 automatically for the other two — so
`format tax` versus `genuine prior` reverted to depending on free-prose there
(S3B-17). It now runs everywhere the main grid runs.

**X5 remains ONE confirmatory contrast, at the anchor model.** The reasoning,
registered so it is not relitigated: **column classification is descriptive, by CI
position against the chance rate (§2.6), not by hypothesis test.** Scoring the
tracking column at Qwen3-8B and the frontier model therefore requires no
contrast of its own. Tripling X5 to three tests would take FAMILY_SIZE to 19 and
ALPHA to 0.05/19, **tightening the threshold for all sixteen other tests to buy
nothing the scored columns do not already give.**

**Frontier precision substitution — D-04, resolved.** The frontier model has no
precision factor; its cells record `precision: "provider_default (unknown)"`.
**Registered rule:** wherever a column definition names the NF4 coordinate,
`provider_default` substitutes for it on the frontier model, and the **bf16 column
is `not_applicable`** for that model (the X3.frontier slot, §5.2). No other
substitution is permitted.

## 2.3 Generations per cell, batching, seeding

**Notation — D-22, resolved.** From here on **`B_batch`** is the paired batch
count and **`K`** is the architecture's block count. The two never share a symbol.

- **20 generations per batch, 16 batches per cell, 320 per cell.**
- **34 cells × 320 = 10,880 generations.** No architecture is trained.
- Diversity is computed **within batch**; a cell reports **mean ± std across its
  16 batches**.

### Why B_batch = 16 — the discreteness ceiling, recomputed at ALPHA = 0.05/17

A paired sign-flip permutation test over `B_batch` differences has 2^`B_batch`
sign assignments; the as-or-more-extreme count is even by mirror symmetry, so
rejection needs the count of as-or-more-extreme **assignment pairs** to fall below
2^`B_batch` · ALPHA / 2.

| `B_batch` | 2^`B_batch` | Ceiling at α=0.05/16 | **Ceiling at α=0.05/17** | Smallest attainable *p* | Discordant tolerated | *p* at one discordant | as % of ALPHA |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 1,024 | 1 | **1** | 0.00195313 | **0** | 0.021484 | 730% |
| 12 | 4,096 | 6 | **6** | 0.00048828 | **0** | 0.006348 | 216% |
| 14 | 16,384 | 25 | **24** | 0.00012207 | **1** | 0.001831 | 62.3% |
| **16** | 65,536 | 102 | **96** | **0.00003052** | **1** | **0.000519** | **17.6%** |
| 32 (X5)† | 4,294,967,296 | 6,710,886 | **6,316,128** | 4.657e-10 | **7** | 1.5e-8 | ~0% |

Raising the family from 16 to 17 tightens ALPHA by 5.9% and costs `B_batch = 16`
six ceiling pairs (102 → 96) and 1.0 percentage point of headroom on the
one-discordant case (16.6% → 17.6% of ALPHA). **The discordance tolerance is
unchanged at 1, and 16 remains the smallest count with real headroom.** No change
to `B_batch` is required.

At `B_batch` = 10 a single discordant batch still makes the contrast unable to
reject at any effect size. At 12 the same holds. That is why 16 stands.

† X5's row is the *exact* geometry at 32 pairs, shown for comparability. X5 does
not run exactly — 2³² exceeds the §3.4 tractability cut, so it runs by Monte Carlo
at N = 100,000 with a floor of 9.99990 × 10⁻⁶ (§2.8, §5.2).

The unpaired form used for a frontier cell whose seeds are not honoured has
C(32,16) = 601,080,390 assignments — also past the cut, so that fallback likewise
runs by Monte Carlo, floor 9.99990 × 10⁻⁶, not the exact 3.33 × 10⁻⁹.

### Seeding scheme

```
S = [7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
     7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016]
```

shared by **every** cell including the four in §2.8. Batch *b* uses `S[b]`.
Cross-cell contrasts are therefore paired at the batch index. Unchanged from
revision 3; the first ten entries are unchanged from revision 2 and the first five
from revision 1.

A frontier cell whose provider does not honour a seed records
`seed_honoured: false`, its 16 batches are treated as unpaired replicates, and the
results file flags which test form was used.

## 2.4 Outcomes

### 2.4.1 The design-choice vector

For a configuration with **K** blocks, the vector concatenates over block
positions *b* = 1…K the six per-block categorical fields
([run_v2.py:52-58](src/run_v2.py#L52)):

`conv_type` ∈ {standard_3x3, depthwise_separable, dilated_3x3, bottleneck}
`channels` ∈ {32, 64, 128, 256} — **categorical**, because repair snaps to the
nearest legal value
`activation` ∈ {relu, gelu, silu, mish}
`normalization` ∈ {batchnorm, layernorm, groupnorm, none}
`skip_connection` ∈ {identity, projection, none}
`pooling` ∈ {maxpool, avgpool, strided_conv, none}

plus the architecture-level fields `n_blocks` = K, `global_pool`, `fc_layers`.

**D-24, resolved.** `n_blocks` is a member of the design-choice **vector** but is
deliberately **not** a member of *G* in §2.4.2's distance formula: block-count
difference is carried by the separate `6·|K_x − K_y|` term, and including
`n_blocks` in *G* as well would double-count it.

### 2.4.2 Primary outcome — mean pairwise structural diversity D

```
                Σ_{b=1..min(Kx,Ky)} Σ_{f∈F} 1[x_bf ≠ y_bf] + 6·|Kx − Ky| + Σ_{g∈G} 1[x_g ≠ y_g]
   d(x,y)  =   ─────────────────────────────────────────────────────────────────────────────
                                    6·max(Kx,Ky) + |G|
```

*F* is the six per-block fields; *G* = {`global_pool`, `fc_layers`}, |G| = 2.
Blocks present in only one architecture count as six field mismatches each.
`d ∈ [0,1]`, and **d = 0 iff the two design-choice vectors are identical**.

**D(batch)** = mean of *d* over all C(n,2) unordered pairs of parseable
generations in the batch.

*Why not the original's Jaccard:* it operates on position-tagged block signature
*sets*, so a block differing in one field and one differing in all six contribute
equally — part of why the manuscript could assert "20 identical designs" and
"Jaccard 0.022" in one sentence. Field-level Hamming has the resolution the
per-field collapse profile needs and preserves d = 0 ⟺ identical.

### 2.4.3 Secondary — parse-failure rate

Fraction of the batch's 20 generations producing no parseable JSON object with a
`blocks` key. Reported for every cell, always adjacent to that cell's D.

### 2.4.4 Secondary — per-field collapse profile

Per field *f*, per batch, per stage: **normalised Shannon entropy** of *f*'s
realised values pooled across block positions and generations, divided by
log₂|vocab_f|. A constant field has entropy exactly 0.

And the three repair channels per field — `sanitize_config` has two distinct
collapse mechanisms and the manuscript conflated them:

| Channel | Meaning |
|---|---|
| `passthrough` | present, legal, unchanged |
| `coerced` | present, out-of-vocabulary, rewritten to `valid_vals[0]` |
| `filled` | **absent** from the model's output, inserted at `valid_vals[0]` |

`filled` is a collapse the model never had a chance to avoid. If the profile is
dominated by `filled` rather than `coerced`, the mechanism is "the model wrote a
partial config and the harness completed it," a different finding from "the model
wrote an illegal value and the harness overwrote it," and the paper must say which.

### When a FIELD is collapsed — REGISTERED (R5-4, fixes S3B-01)

Revision 4 said §2.4.7's tracking proportions are taken "over the fields collapsed
in that batch" while defining `collapsed` only for **D**, a batch-level diversity.
No rule classified a *field*. The denominator of both tracking quantities was
undefined.

> **A field *f* is `collapsed` in a batch at a stage when its normalised Shannon
> entropy at that stage is < 0.15.**

The constant mirrors `D < 0.15·D_rand` exactly, and the mirror is principled:
**both quantities are normalised so that 1.0 is the uniform reference** — D
against `D_rand`, entropy against log₂|vocab_f|. The same fraction therefore means
the same thing on both scales.

*Alternative rejected:* "entropy exactly 0", i.e. constant. That is the limiting
case, not the phenomenon; a field taking one value in 19 of 20 generations is
collapsed in every sense the paper cares about and would have been excluded.

### 2.4.5 Secondary — within-cell bootstrap intervals

The paired batch-index contrast remains **primary**. The bootstrap is a
**resolution check**.

**D-07, resolved.** Both the point estimate and its interval are now computed on
the **same estimand**:

- **Classification and ΔD use the batch-mean form.** `D_mean` for levels;
  ΔD = `D_mean(dest) − D_mean(src)` for changes.
- **The ΔD interval is a paired bootstrap over the 16 batch indices**, resampling
  batch-index pairs with replacement — the same quantity being classified.
- `D_cell_pooled` (mean of *d* over all C(N,2) generation pairs, cross-batch pairs
  included) and its generation-level bootstrap are **still reported**, as an
  additional view, and are explicitly *not* what any threshold is applied to.

**Resampling unit for the pooled interval: the generation, not the pair.** The
C(N,2) pairwise distances are strongly dependent — each generation appears in
N−1 of them — so resampling pairs as independent would understate the width,
which is the opposite of what a resolution check is for.

**Parameters, fixed and not tuned:** 10,000 resamples; **BCa**; 95%;
`bootstrap_seed = 90210`; computed separately per stage.

**Resampling units, registered per statistic (R5-10, fixes S3B-03).** Revision 4
registered "the generation" globally, which is wrong for a statistic whose
replicates are batches:

| Statistic | Resampling unit | Why |
|---|---|---|
| `D_cell_pooled` | **generation** | the pooled mean is over generation pairs |
| ΔD (change columns) | **batch-index pair** | the point estimate is a difference of batch means |
| `tracks_first`, `tracks_exemplar` | **batch** | the statistic is a per-batch proportion over fields; generations are not its sampling unit |
| Cliff's δ (E2) | **run**, leave-one-run-out jackknife | §3.4 |

**Boundary-straddle rule.** Where the batch-level BCa interval on a cell's
`D_mean`, or on a contrast's ΔD, straddles the classification boundary that
decides its label, that cell is scored `indeterminate` and the interval is
reported. This can only reduce matched cells; it can never create a match.

### 2.4.6 Secondary — parse-free surface diversity S

**Purpose.** To bound the free-prose parse-selection effect by measuring diversity
over the **full** generation set, including failures. **At revision 4 this is
corroborating rather than load-bearing**, because §2.8 supplies a discriminator
that does not depend on free prose parsing at all.

**Definition.** On the **raw generated text**, before any parsing:

1. **Normalisation** — lowercase; collapse whitespace runs to one space; strip.
   **Nothing else.** No punctuation stripping, no code-fence removal, no
   JSON-aware handling: any format-aware normalisation would build the answer into
   the instrument.
2. **Tokenisation** — split on whitespace.
3. **Feature set** — G₃(x) = the set of contiguous token 3-grams.
4. **Distance** — `d_S(x,y) = 1 − |G₃(x) ∩ G₃(y)| / |G₃(x) ∪ G₃(y)|`.
5. **Batch statistic** — mean over all C(20,2) pairs, **including generations that
   failed to parse**. `S ∈ [0,1]`.
6. **Cell statistic** — `S_mean ± S_std` across 16 batches, plus `S_cell_pooled`
   with a BCa interval under the §2.4.5 parameters.

*Why token 3-gram Jaccard:* symmetric, bounded, parameter-free beyond *n*, and
structurally parallel to a mean-pairwise-distance diversity. Self-BLEU is
asymmetric with a brevity penalty that would reward the terse schema condition for
the wrong reason; distinct-*n* is a corpus-level ratio and cannot be compared
batch-to-batch on the same footing. *n* = 3 is fixed in advance: bigrams over-fire
on shared function words, 4-grams and above get sparse on short generations.

**Interpretation, fixed before data:**

| Observation | Reading |
|---|---|
| S high, D collapsed (free-prose) | The full set carries surface variety while the parseable subset does not. **The collapse is not explained by parse-selection alone.** |
| S low, D collapsed | Consistent. **S does not distinguish "the model repeats itself" from "the parseable subset is unrepresentative"**; the free-prose reliability caveat stands undiminished. |
| S low, D diverse | Not substantively interpretable. **Instrument fault** — halt and investigate the parser or the normalisation. |
| S high, D diverse | Consistent. No additional information. |

**Hard constraints.** S is never substituted into D; never enters a confirmatory
test; has no classification threshold and is never described as
`collapsed`/`diverse`/`partial`/`reduced`; and **cannot rescue a column from
`indeterminate`**.

### 2.4.7 Primary outcome of the anchor-tracking sub-design — `anchor_tracking`

*(Introduced at revision 4; denominators, bootstrap unit and stage coverage all
registered at revision 5.)*

For each field *f* **collapsed** in a batch at a stage — per the threshold
registered in §2.4.4 — let `modal(f)` be its most frequent realised value. Two
indicator quantities, **kept separate and never merged**:

| Quantity | Definition | Denominator |
|---|---|---|
| `tracks_first(f)` | 1 if `modal(f)` equals the **first-enumerated** value of *f* under that cell's enumeration order | **all** collapsed fields in the batch |
| `tracks_exemplar(f)` | 1 if `modal(f)` equals the **in-context exemplar's** value for *f* | the collapsed fields **among the three the exemplar names** |

**The two denominators differ, and this is registered rather than incidental
(R5-4, fixes S3B-02).** §2.8's exemplar specifies `conv_type`, `activation` and
`normalization` — three of the six per-block fields. It has no value for
`channels`, `skip_connection` or `pooling`, so `tracks_exemplar` is a **three-field
statistic** and its base is stated separately in the results file
(`n_exemplar` alongside `n_first`). *Alternative rejected: extending the exemplar
to all six fields, which would change the manipulation §2.8 registers rather than
document it.*

Both quantities are computed **per batch, at BOTH stages** (pre-repair and
post-repair), and aggregated to the cell as a mean over batches with a BCa 95%
interval, **resampling batches** (§2.4.5). **All four cell aggregates —
{`tracks_first`, `tracks_exemplar`} × {pre, post} — are registered fields**
(§5.5, R5-3); revision 4 stored only the post-repair pair, which made the
`repair artifact` and `format tax` rows unscoreable from the results file.

- **Zero collapsed fields in a batch → that batch contributes `no_collapse`,
  which aggregates to `no tracking`** — NOT to `null`. Registered here because
  the implementation showed the alternative breaks the `repair artifact` row
  (see below). The count is recorded separately as `n_no_collapse_batches` so a
  no-collapse batch is never confused with a measured low rate.
- **Modal ties:** if two values tie, `modal(f)` is the one appearing **earlier in
  that cell's enumeration order**, and the tie is recorded in `modal_tie_count`.
  *This deliberately biases the statistic toward finding tracking, so a `no
  tracking` result is conservative and a `tracks` result must be read with the tie
  count.*
- **`modal(f)` itself is emitted** per (field, stage, batch), so a reader can
  check the indicator without recomputing it from raw specs (§5.5, R5-9).

### No collapse means no tracking — REGISTERED (found by implementation)

`repair artifact` predicts that **pre-repair does not track**. But in the world
where that rival is true, the pre-repair distribution is *diverse* — no field is
collapsed — so there is no modal value to compare against the first-enumerated
one, and a rule mapping "zero collapsed fields" to `null` would make the
prediction **unmeasurable in exactly the case it describes**. The column would go
`indeterminate` whenever the rival it was added to test is correct.

> **A batch with zero collapsed fields at a stage contributes `no tracking` for
> that stage.** Tracking is a property of *what a collapsed distribution collapsed
> onto*; if nothing collapsed, nothing tracked. The batch is counted in
> `n_no_collapse_batches` and is **excluded from the BCa interval** — the label
> comes from the collapse profile, not from a proportion.
>
> A cell in which **the majority of batches show no collapse** at a stage is
> labelled `no tracking` at that stage, with `reason: "no_collapse"` recorded.
> `indeterminate` remains reserved for cells that are unusable for some *other*
> reason.

*Alternative rejected: treating zero collapsed fields as `null` and letting the
column go `indeterminate`. That is what revision 4 implied, and it makes the
`repair artifact` row untestable — the fixture that should confirm it instead
returns "insufficient data".*

The confirmatory contrast **X5** is defined on `tracks_first` at post-repair, at
the anchor model (§2.8, §5.1). Every other use of these quantities is
**descriptive, by CI position** against the chance rate registered in §2.6.


## 2.5 Pre-registered prediction table — the falsifier set

**Six columns.** The sixth exists because S3a proved the original five could not
separate `format tax` from `genuine prior` except through free-prose — the very
column §2.6 is most likely to rule unreliable.

| Rival | free-prose | schema pre-repair | post-repair | bf16 | high temp | **anchor tracking** |
|---|---|---|---|---|---|---|
| **repair artifact** | diverse | diverse | collapsed | no chg | no chg | **R-A** |
| **format tax** | diverse | collapsed | collapsed | no chg | no chg | **F-T** |
| **quantisation** | partial | partial | partial | recovers | partial | **NONE** |
| **decoding** | reduced | reduced | reduced | no chg | recovers | **NONE** |
| **genuine prior** | collapsed | collapsed | collapsed | no chg | no chg | **NONE** |

Column definitions:

- **free-prose** — D at (free-prose, post-repair, NF4, T=0.7)
- **schema pre-repair** — D at (schema, pre-repair, NF4, T=0.7)
- **post-repair** — D at (schema, post-repair, NF4, T=0.7)
- **bf16** — ΔD from (schema, post, NF4, 0.7) to (schema, post, bf16, 0.7)
- **high temp** — ΔD from (schema, post, NF4, 0.3) to (schema, post, NF4, 1.0)
- **anchor tracking** — the §2.8 predicate below, evaluated on the 2×2 grid

Columns 1–3 are **levels**; 4–5 are **changes**; 6 is a **predicate**.

### The tracking predicates — REGISTERED (revision 6)

The observation the predicates read is a **three-entry grid**:

```
    pre_first      tracks_first at PRE-repair
    post_first     tracks_first at POST-repair
    cross_level    the cross-level exemplar delta (§2.5a)
```

**Single-cell `tracks_exemplar` is emitted (A21) but NO PREDICATE READS IT.**
Revision 5 had it in the grid; S3c showed it cannot do the job. A format tax
tracks *whichever* exemplar is shown, so it is high in **both** exemplar cells;
a genuine prior's fixed modal coincides with the shown exemplar at chance in
each. The two are not separable by a level reading. §2.5a asks the
discriminating question instead — **does the modal MOVE when the exemplar
changes** — and is identically zero for every rival whose modal is stable.

| ID | Rival | Predicate | Why |
|---|---|---|---|
| **R-A** | repair artifact | `pre_first = no tracking` **AND** `post_first = tracks` **AND** `cross_level = no response` | `sanitize_config` coerces and fills to `valid_vals[0]` — the first-enumerated value — so reversing the enumeration reverses the repair target. It never sees the exemplar, which is a prompt object, so the modal cannot move with it. The model's own pre-repair output is untouched. |
| **F-T** | format tax | ( `pre_first = tracks` **OR** `cross_level = responds` ) **AND** `post_first = pre_first` | The prompt drives the model's own choice **before** any repair, through **either** channel the prompt carries — the enumeration order or the exemplar — and repair, which only coerces illegal values, leaves a legal choice unchanged. The disjunction is **necessary, not vague**: the two channels compete for one modal value, so a conjunction would be unsatisfiable. |
| **NONE** | quantisation, decoding, genuine prior | all three entries at their null: `pre_first = no tracking`, `post_first = no tracking`, `cross_level = no response` | Precision, temperature and the weights are all invariant to how the harness presents the options. |

**Mutually exclusive**, checked by construction and by fixture: R-A requires
`post_first = tracks` with no cross-level response; F-T requires at least one
prompt-side channel live; NONE requires all three null.

**Evaluation rule.** A predicate is `indeterminate` **only if a grid entry it
reads is indeterminate**. All three predicates read all three entries.

### The degenerate cell — REGISTERED (found by implementation, R5-5)

Under `canonical` order the first-enumerated values of the three exemplar fields
are `standard_3x3` / `relu` / `batchnorm` — **exactly the `modal` exemplar's
values**. In the **(canonical, modal)** cell, therefore,
`tracks_first` and `tracks_exemplar` are numerically identical on every field the
exemplar names, and the two sub-quantities **cannot be dissociated there**. The
other three cells are clean:

| Cell | first-enumerated == exemplar value on | Status |
|---|---|---|
| (canonical, modal) | conv_type, activation, normalization — **all three** | **DEGENERATE** |
| (canonical, non-modal) | none | dissociable |
| (reversed, modal) | none | dissociable |
| (reversed, non-modal) | none | dissociable |

> **Registered rule: `tracks_exemplar` is scored only in cells where at least one
> exemplar field has `first-enumerated ≠ exemplar value`.** In the
> (canonical, modal) cell `tracks_exemplar` is emitted with
> `dissociable: false` and is **excluded from the grid**, so a predicate reading
> it takes the value from the dissociable cells of the same model.

Without this, `repair artifact` — which predicts `post_exemplar = no tracking` —
would be unsatisfiable in the (canonical, modal) cell for a *genuine* repair
artifact, because collapsing onto the first-enumerated value automatically also
hits the exemplar value there. The 2×2 factorial exists precisely so the two
sub-quantities can be separated; this rule stops the one degenerate corner from
contaminating the predicate.

*Alternative rejected: changing the `modal` exemplar to values that are not
first-enumerated. That would make the exemplar no longer modal, which is the
property §2.8 needs it to have — the point of the `modal` level is that it shows
the model the template the original paper reported.*

**What the sixth column buys.** `format tax` and `genuine prior` differ in **two**
columns — free-prose and anchor tracking — and anchor tracking is measured at the
**schema-constrained** configuration, so it **does not require free prose to
parse**. Free-prose is corroborating, not load-bearing, for C2. The same holds for
`repair artifact` versus `format tax`, which previously differed only in
schema-pre-repair: R-A and F-T disagree on all four grid entries.

Verified by implementation: S3b fixture **C15** forces free-prose
`indeterminate` and both rivals still resolve, `repair artifact` at 4/4 and
`format tax` at 5/5.

## 2.5a The cross-level exemplar predicate — NEW (R6-2)

**The question a single cell cannot answer.** `tracks_exemplar` asks "does the
modal value equal the exemplar shown here". Under a format tax it is high in the
modal cell *and* in the non-modal cell, because the model follows whichever is
shown. Under a genuine prior the fixed modal coincides with the shown exemplar at
chance in each — and with only **three** exemplar fields, the smallest non-zero
proportion (⅓) already exceeds the chance rate (0.25), so a single coincidence
reads as tracking. A level reading cannot separate them.

**The statistic.** At a fixed enumeration order and stage, pooled over **both**
exemplar cells at the same batch index:

```
    own    = modal equals the exemplar shown in ITS OWN cell
    other  = modal equals the exemplar shown in the OTHER cell

    Δ_exemplar = mean(own) − mean(other)
```

over every collapsed exemplar field in both cells.

**Why the pairing makes the null EXACT, not merely expected.** If the modal value
*v* is the same in both cells — which is what `genuine prior`, `repair artifact`,
`quantisation` and `decoding` all imply — then

```
    Σ own  = [v = e_modal] + [v = e_non-modal] = Σ other
```

so **Δ = 0 identically**, for every *v*, with no chance-rate estimate required.
Verified exhaustively over the full exemplar-field vocabulary (fixture C19: max
|Δ| = 0.0 across every modal combination). Only a modal that **moves with the
exemplar** makes Δ positive; a modal that follows the shown exemplar exactly gives
**Δ = 1** (fixture C19b).

**Labelling — the one-sided rule at a chance rate of exactly zero:**

| Label | Definition |
|---|---|
| **responds** | the BCa 95% interval excludes 0 from above — its lower bound > 0 |
| **no response** | the interval contains 0 or lies below it |
| **indeterminate** | **insufficient data only**: fewer than 0.4·B_tracking usable batch pairs |

**Every rival's value:**

| Rival | `cross_level` | Reasoning |
|---|---|---|
| repair artifact | **no response** | the repair stage never sees the exemplar |
| **format tax** | **responds** | the prompt carries the exemplar and the model follows it |
| quantisation | **no response** | precision does not read the prompt's exemplar |
| decoding | **no response** | temperature rescales; it does not relabel the mode |
| genuine prior | **no response** | the weights are invariant to what the prompt shows |

**This column separates `format tax` from every other rival**, on a
schema-constrained measurement that needs no free prose, and it does so with an
exact null. It is **descriptive, classified by CI position** — like every other
tracking label — and therefore **adds no confirmatory test**; FAMILY_SIZE stays
17 (§5.2).

**What it costs and saves.** The S3c pilot (§2.8) put the batch count needed for
the cross-level delta at **28**, against **40** for the single-cell
`tracks_exemplar` it replaces — the pooling doubles the field count and the
pairing removes the chance-rate baseline. Adopting it **lowers `B_tracking` from
40 to 28**, saving 12 × 12 × 20 = **2,880 generations**.

### KNOWN LIMITATION — the level columns cannot falsify (R5-7, S3B-09)

Stated plainly rather than left to be discovered:

**On `free-prose` and `schema pre-repair`, every one of the three level labels
`{collapsed, reduced, diverse}` is predicted by some rival.** Those two columns
can therefore never produce a mismatch against the whole rival set, and an
observation there is never evidence that the set is incomplete. Per column, the
labels matching **no** rival are:

| Column | Labels matching no rival |
|---|---|
| free-prose | **none** |
| schema pre-repair | **none** |
| post-repair | `diverse` |
| bf16 | `partial`, `worsens` |
| high temp | `worsens` |
| anchor tracking | any grid failing all three predicates |

So `best == 0` — the "no rival matched" outcome §2.6 registers — fires **almost
exclusively through the change and tracking columns**, and is unreachable while
both level columns are scoreable. Verified: S3b fixture C6 shows the most hostile
available observation still scores 3 for `repair artifact`; C6b reaches zero only
with both level columns indeterminate.

**The consequence, and the paper must say it in these terms:** the five-rival set
is a falsifier set **on three of its six columns**. On free-prose and
schema-pre-repair it discriminates *between* rivals but cannot reject them all.
This is a property of a five-rival set that spans the label space, not a fixable
defect — a sixth rival predicting the missing labels would close it, and none is
motivated by the literature.

**Why the format-tax row is present at all.** "The Format Tax" (§6, row 8) argues
the structure-**requesting prompt**, not decoder-side repair, causes most
degradation: *"The dominant cost enters at the prompt: format-requesting
instructions alone cause most of the accuracy loss, before any decoder constraint
is applied."* The original manuscript attributed collapse to `sanitize_config`, a
repair step. If E1 cannot separate a prompt-side from a repair-side cause, the
attribution is unfalsifiable.

**What we conclude if the format-tax row wins**, in the words that will be used:

> The original manuscript's attribution was wrong. Template collapse is caused by
> the prompt asking for a fixed JSON schema, upstream of any repair step;
> `sanitize_config` is a downstream amplifier, not the cause. The instrumentation
> thesis survives — the apparatus is still responsible — but the specific
> component the original paper named is exonerated, and the paper states that its
> own prior attribution was incorrect.

That last clause is not optional.


## 2.6 Classification thresholds and signature scoring

### D_rand — the reference *(redefined at revision 4; see §10, D-09/D-10/D-13)*

Revision 3 anchored the thresholds on "the repository's own **uniform** random
sampler" with an analytic anchor of ≈0.74. S3a measured both and neither held.

**Two references are now defined and they are not the same quantity:**

**`D_rand` — the registered anchor.** Mean pairwise structural diversity of draws
from a **corrected uniform sampler** over the *declared* search space: every one
of the six per-block fields drawn uniformly over **all** its declared values
(including `pooling: "none"` at 25%), `global_pool` and `fc_layers` uniform, at
**fixed block count**, computed with the same *d*, in the E1 batch structure
(16 × 20), seed `20260817`, and averaged over K ∈ {3,4,5,6}.

**Measured: `D_rand` = 0.719205**, mean across-batch std 0.006689.
Analytic value `(53K/12 + 1)/(6K + 2)` averaged over K = **0.718872**; agreement
to 0.000333.

| K | analytic | measured | batch std |
|---:|---:|---:|---:|
| 3 | 0.712500 | 0.713273 | 0.006646 |
| 4 | 0.717949 | 0.720268 | 0.005292 |
| 5 | 0.721354 | 0.720374 | 0.006788 |
| 6 | 0.723684 | 0.722905 | 0.008032 |
| **mean** | **0.718872** | **0.719205** | 0.006689 |

**`D_repo_sampler` — reported, not the anchor.** The repository's own sampler,
same structure and seed: **0.771931** (batch-mean), std 0.007967, pooled 0.769334.
It is reported so the original paper's random arm stays comparable, and it is
**never** used to set a threshold.

**Why the repository sampler is not the anchor**, recorded so this is not
relitigated:

1. **It is not uniform.** `pooling` is decided by a two-stage draw
   (`num_pools = rng.randint(1, min(K,4))`, then `rng.sample` of positions);
   blocks off the list are forced to `"none"` and blocks on it draw from **three**
   values only. Measured over 320 draws: `none` **48.21%**, `strided_conv` 17.68%,
   `avgpool` 17.47%, `maxpool` 16.64% — against 25% under uniformity.
2. **Block count varies**, so pairs pick up the `6·|K_x − K_y|` term. Measured
   inflation from letting K vary, holding the sampler corrected: **+7.96%**
   (0.719205 → 0.776465). The repository sampler's fixed-K subsets run
   **0.6984–0.7162** against **0.771931** pooled — the same confound.

**The anchor is block-count-matched. Decision and reason.** `sanitize_config`
never changes a block count; it rewrites and fills fields *within* blocks. The
collapse E1 measures therefore lives entirely in the six per-block fields, and a
reference inflated by block-count variation would make every threshold too
lenient — a collapsed cell would clear the `collapsed` bar it should fail. The
thresholds anchor to the **fixed-K** value. *(Alternative considered and rejected:
anchoring to the block-count-free value, which is closer to what the LLM arms will
actually produce, but which imports into the reference exactly the variance
component the measured effect cannot touch.)*

**Sanity range, tightened (D-10).** Halt E1 if the measured `D_rand` falls outside
**[0.705, 0.735]**. Revision 3's [0.65, 0.80] admitted every wrong value:

| Value | Inside R3's range | Inside R4's range |
|---|---|---|
| `D_rand`, corrected uniform fixed-K = 0.719205 | yes | **yes** |
| corrected uniform, K free = 0.776465 | yes | **no — halts** |
| repository sampler = 0.771931 | yes | **no — halts** |
| R3's own stated anchor, 0.74 | yes | **no — halts** |

**`D_rand` is written into the E1 results-file header** (§5.5), not only to
`results/E1_reference.json` — fixing D-08, so a results file carries the reference
its labels are fractions of.

### The label vocabulary — levels

| Label | Definition | Value at `D_rand` = 0.719205 |
|---|---|---|
| **collapsed** | D < 0.15·D_rand | D < **0.107881** |
| **reduced** / **partial** (level) | 0.15·D_rand ≤ D < 0.60·D_rand | 0.107881 ≤ D < 0.431523 |
| **diverse** | D ≥ 0.60·D_rand | D ≥ **0.431523** |

`reduced` and `partial` denote the same numeric band at level; the two words
appear in the table because two rivals mean different things by it, and the
distinction is carried by the other columns.

### The label vocabulary — changes (D-01 and D-03, resolved)

Revision 3 defined only `no chg` and `recovers`, leaving the 0.10–0.25 band and
the entire negative direction unnamed — while the `quantisation` row predicted
`partial` in a change column, a label with no ΔD rule. Both are now closed by one
definition:

| Label | Definition | Value at `D_rand` = 0.719205 |
|---|---|---|
| **no chg** | \|ΔD\| < 0.10·D_rand | \|ΔD\| < **0.071921** |
| **partial** (change) | +0.10·D_rand ≤ ΔD < +0.25·D_rand | 0.071921 ≤ ΔD < 0.179801 |
| **recovers** | ΔD ≥ +0.25·D_rand **and** the destination cell is not `collapsed` | ΔD ≥ **0.179801** |
| **worsens** | ΔD ≤ −0.10·D_rand | ΔD ≤ −0.071921 |

`partial` at level and `partial` at change are different rules on different
quantities; the results file records which by the column's `kind` field.

**The demotion, restated (R5-10, fixes S3B-06).** Revision 4 said a change meeting
the `recovers` bound whose destination is still `collapsed` "is demoted to
`partial`" — assigning `partial` to a ΔD **outside** `partial`'s own numeric band.
The band is therefore widened rather than contradicted:

> **`partial` (change)** = `+0.10·D_rand ≤ ΔD < +0.25·D_rand`, **OR**
> `ΔD ≥ +0.25·D_rand` with a `collapsed` destination.

The two clauses are disjoint and together with `no chg`, `recovers` and `worsens`
they partition the ΔD line. *Alternative rejected: naming the demoted case
separately (e.g. `recovers_into_collapse`), which would add a sixth change label
that no rival predicts and would therefore only ever produce mismatches.*

**`worsens` is predicted by no rival.** An observation of `worsens` therefore
**scores as a mismatch against all five, not as indeterminate.** The distinction
is principled and is registered: `indeterminate` is for measurements that are
**unreliable**; `worsens` is a reliable measurement that **contradicts** every
rival. If every rival is contradicted in a column, that is evidence the
five-rival set is incomplete, and §2.6's "no rival matches" outcome exists for it.

### The label vocabulary — anchor tracking (R5-1, fixes S3B-10, S3B-11, S3B-16)

**The registered rule is ONE-SIDED, against the per-field chance rate.** The
substantive null is chance: a genuine prior produces a tracking rate **at** chance,
not below it.

| Label | Definition |
|---|---|
| **tracks** | the BCa 95% interval excludes the chance rate **from above** — its lower bound > chance |
| **no tracking** | the interval **contains** the chance rate, or lies entirely below it |
| **indeterminate** | **insufficient data only** — a cell whose usable batch count falls below the §2.7 threshold for reasons *other than* absence of collapse. Never assigned on interval width alone, and never assigned merely because nothing collapsed (§2.4.7). |

**Chance rates.** For a field *f*, chance = **1/|V_f|**. In aggregate, the
**vocabulary-weighted** rate: the mean of 1/|V_f| over every (batch, field)
collapsed instance entering the statistic.

| Field | \|V_f\| | chance |
|---|---:|---:|
| conv_type | 4 | 0.250000 |
| channels | 4 | 0.250000 |
| activation | 4 | 0.250000 |
| normalization | 4 | 0.250000 |
| skip_connection | 3 | 0.333333 |
| pooling | 4 | 0.250000 |
| **all six, unweighted mean** | | **0.263889** |
| **the three exemplar fields** | | **0.250000** |

The rate actually applied is recomputed from the realised collapsed-field mix and
**emitted per cell** (§5.5, R5-9) so the labelling is auditable.

**Two alternatives were implemented, measured and REJECTED.** S3b swept a
synthetic proportion at *n* = 16 batches under all three rules; **10 of 11 sampled
rates gave different verdicts**:

| true rate | 95% CI | flat 0.50 *(rev 4)* | per-field symmetric | **one-sided (registered)** |
|---:|---|---|---|---|
| 0.10 | [0.000, 0.313] | no tracking | *indeterminate* | **no tracking** |
| 0.25 | [0.063, 0.438] | no tracking | *indeterminate* | **no tracking** |
| 0.40 | [0.125, 0.563] | *indeterminate* | *indeterminate* | **no tracking** |
| 0.50 | [0.188, 0.688] | *indeterminate* | *indeterminate* | **no tracking** |
| **0.60** | [0.313, 0.750] | ***indeterminate*** | tracks | **tracks** |
| **0.75** | [0.438, 0.875] | ***indeterminate*** | tracks | **tracks** |
| 0.90 | [0.563, 0.938] | tracks | tracks | **tracks** |

- **The flat 0.50 bar (revision 4) is rejected.** It returns `indeterminate` at
  true rates of **0.60 and 0.75 — 2.3× and 2.8× chance**, which is unambiguous
  tracking, and it is eager to declare absence. Both errors point one way:
  `tracks` is predicted only by `repair artifact` and `format tax`; `no tracking`
  by the other three. **The bar was systematically biased against the two
  instrument rivals and toward `genuine prior`** — against the paper's own thesis,
  and against the column doing the job it was added for.
- **The symmetric per-field rule is rejected.** Requiring `no tracking` to mean
  "interval entirely below chance" means it **never fires at any plausible rate**,
  because nothing predicts a rate *below* chance. Under it `quantisation`,
  `decoding` and `genuine prior` could never match the tracking column at all.
- **The one-sided rule is the only one under which both verdicts are reachable**
  across the range.

**Revision 4's own prose already described this rule** — it glossed `tracks` as
"with the interval **excluding chance**" while the rule beside it used 0.50 and
the note below conceded chance is 0.25 (S3B-16). The prose is now the rule.

**Boundary (R5-10, fixes S3B-04).** An interval endpoint sitting **exactly on**
the chance rate does not exclude it, so `lo == chance` yields `no tracking`. The
comparison is strict `>` and is deterministic at the bit level.

### The label vocabulary — the cross-level exemplar delta

Defined in §2.5a: `responds` if the BCa lower bound exceeds **0**, `no response`
if the interval contains 0 or lies below, `indeterminate` for insufficient data
only. The null is exact, so unlike the other tracking labels this one needs no
chance-rate estimate.

### Signature scoring (generalised to k indeterminate columns)

Each rival scores the number of its **scoreable** columns that match. A column is
**not scoreable** if it is `indeterminate` under any of the routes: the free-prose
parse-rate rule, the §2.4.5 boundary-straddle rule, or the anchor-tracking
insufficient-data rule (§2.6, R5-1).

Let *n_s* be the number of scoreable columns, out of six.

| Rule | Registered value |
|---|---|
| Minimum for any verdict | **n_s ≥ 4**. Below that: **"no verdict — too few scoreable columns"**. |
| Winning threshold | the winner must match **≥ ceil(0.75 · n_s)** |
| Tie at the top | **"no clean winner — mixed attribution"** |
| Winner below threshold | **"no clean winner — mixed attribution"** |

Worked values: n_s = 6 → ≥ 5; n_s = 5 → ≥ 4; n_s = 4 → ≥ 3.

### Indeterminacy CAN create a winner — flagged, not prevented (R5-6, S3B-07)

Revision 4 claimed the straddle rule "can only reduce the number of matched cells;
it can never create a match". **That is true of cells and false of verdicts**, and
S3b demonstrated it: a `format tax` observation failing **both** change columns
scores 4 of 6 against a threshold of 5 → no winner; make one column it already
failed `indeterminate` and it is 4 of 5 against a threshold of 4 → it wins. The
score never rose; the bar fell.

**This is not prevented.** A threshold that scales with *n_s* must behave this way,
and pinning the bar at 5 regardless of *n_s* would make the registered n_s = 4 and
n_s = 5 cases unwinnable — i.e. it would delete the generalisation §2.6 exists to
provide. Instead the verdict carries its own caveat:

> **When the winner's matched count is below `ceil(0.75 · 6) = 5`, the verdict is
> emitted as `contingent_on_indeterminacy`**, carrying:
> - `n_indeterminate` — how many columns were unscoreable,
> - `would_win_at_n_s_6` — whether the same rival would have won had every column
>   been scoreable,
> - the list of indeterminate columns and the route that made each one so.

A `contingent_on_indeterminacy` verdict is reported in the manuscript **with that
flag attached**, and C2 is not asserted on one alone.

### Free-prose reliability rule

The free-prose parse rate is reported adjacent to every free-prose diversity
number. **If it is below 50%, that column is scored `indeterminate` for every
rival.** With six columns this leaves n_s = 5 and the threshold at ≥ 4 — and,
critically, leaves the format-tax/genuine-prior discrimination intact on the
anchor-tracking column.

`S` (§2.4.6) is reported alongside and characterises how much of the observed
concentration could be a selection artifact. **It does not change the rule**, and
a column ruled `indeterminate` stays so whatever S shows.

A permissive prose-to-fields extractor was considered and rejected: it is a second
instrument with its own artifact.

## 2.7 Ties and degenerate outputs

- A generation that fails to parse contributes to the parse-failure rate and is
  excluded from **both** stages' diversity. **It is included in S**, which is the
  point of S.
- A batch with fewer than 2 parseable generations yields `D = null` — recorded,
  **never imputed**. A cell with **≥10 null batches of 16** is `insufficient` and
  contributes no signature match. *(The 0.6 proportion is unchanged across all
  four revisions: ≥3 of 5, ≥6 of 10, ≥10 of 16.)*
- **Null batches raise the paired test's discreteness floor**, which is handled by
  §5.2's run-time arm: a contrast whose realised `B_batch` gives
  `min_attainable_p ≥ ALPHA` is emitted `undecidable_by_discreteness` with
  `significant: null`, and the manuscript reports it as undecidable rather than as
  a null result.
- An all-identical batch yields D = 0.000 exactly — a **legal measurement**, and
  the single most likely observation in the post-repair schema cells.
- Duplicate generations are retained, not deduplicated: duplication *is* the
  collapse being measured.
- **S degenerate cases.** A generation of fewer than 3 tokens after normalisation
  has an empty 3-gram set. Two empty sets → `d_S = 0`; one empty → `d_S = 1`. A
  batch in which **more than half** the generations have empty sets yields
  `S = null`.
- **`anchor_tracking` degenerate cases.** A batch with **zero collapsed fields**
  contributes `no_collapse` → `no tracking` (§2.4.7), counted in
  `n_no_collapse_batches` and excluded from the interval. A batch with collapsed
  fields but **none among the three the exemplar names** yields
  `tracks_exemplar = null` while `tracks_first` stays defined — the two
  denominators are independent (§2.4.7). A cell whose usable batch count for a
  quantity falls below **0.4 · B_tracking**, counting `no_collapse` batches as
  usable, is `insufficient` for that quantity and the column scores
  `indeterminate` — **the only route to `indeterminate` on that column.**

## 2.8 The anchor-tracking sub-design

**Purpose.** To separate `format tax` from `genuine prior` on a column that does
not require free prose to parse. If the collapse is the model's own prior, its
modal choice cannot depend on how the harness enumerates the vocabulary. If it is
the apparatus, the modal choice **tracks the harness** — the first value
enumerated, or the value shown in the in-context exemplar.

**This is the manipulation that makes C2 decidable without free prose**, and S3b's
fixture C15 confirmed it does so.

### Design — ALL THREE MODELS (R5-2)

Two crossed factors, run at the schema-constrained configuration of **each** of
the three models (Qwen3-1.7B at NF4 / T=0.7 is the anchor; Qwen3-8B at NF4 /
T=0.7; the frontier model at `provider_default` / T=0.7):

| Factor | Levels |
|---|---|
| **enumeration order** | `canonical` — the vocabulary order the repository declares, `standard_3x3` first \| `reversed` — the exact reverse, for **every** field simultaneously |
| **in-context exemplar** | `modal` — one worked example using `standard_3x3` / `relu` / `batchnorm` \| `non-modal` — one worked example using `depthwise_separable` / `gelu` / `groupnorm` |

**3 models × 2 orders × 2 exemplars = 12 cells**, each of `B_tracking` batches ×
20 generations.

Revision 4 ran this at the anchor only, which left the sixth column unavailable at
two of three models and `n_s` at 5 automatically there (S3B-17). It now runs
wherever the main grid runs.

All prompts are frozen in `prompts/E1/anchor/` before any run and hashed into the
results file. **The only difference between the two order levels is the order of
the value lists**; wording, schema structure, exemplar and instruction token count
are otherwise identical, and a diff proving that is stored alongside the hashes.
The **exemplar value map is emitted** as a header field (§5.5, R5-9) rather than
living only in this prose.

### B_tracking — CONFIRMED BY PILOT (R6-1, R6-3)

> **`B_tracking = 28`.** Floor 16; pilot-confirmed value 28; `max(16, 28) = 28`.

**The registered criterion was miscalibrated and is corrected (R6-3).** Revision 5
asked for "the smallest batch count whose 95% interval half-width at a true rate
of 0.40 is below 0.15". That yields an interval of **[0.25, 0.55]**, which
**contains** the field-weighted chance rate **0.263889** — so under the registered
one-sided rule (§2.6) it reads `no tracking`. **The criterion would have certified
a width that cannot detect the effect the column exists to detect.** The corrected
criterion is the direct condition:

> **`B_tracking` = the smallest B ≥ 16 at which the BCa lower bound EXCEEDS the
> field-weighted chance rate, at a simulated true tracking rate of 0.40, in ≥ 80%
> of simulated cells.**

**Pilot result** (`scripts/pilot_tracking.py`, seed 20260818, 400 cells per B,
2,000 bootstrap resamples, per-field collapse probability 0.80; output at
`results/pilots/pilot_tracking.json`):

| B | `tracks_first` coverage | `tracks_exemplar` (single-cell) | **cross-level Δ** |
|---:|---:|---:|---:|
| 16 | 0.672 | 0.440 | 0.593 |
| 20 | **0.830** ✓ | 0.570 | 0.710 |
| 24 | 0.858 | 0.525 | 0.770 |
| **28** | 0.917 | 0.695 | **0.800** ✓ |
| 32 | 0.940 | 0.765 | 0.828 |
| 40 | 0.973 | **0.825** ✓ | 0.932 |
| 64 | 1.000 | 0.968 | 0.990 |

- `tracks_first` needs **20** — it runs over up to six fields.
- Single-cell `tracks_exemplar` needs **40** — three fields, granularity
  {0, ⅓, ⅔, 1} against a chance rate of 0.25.
- The **cross-level delta needs 28**, and it is the binding quantity, because
  **the revision-6 predicates read `tracks_first` and the cross-level delta and
  do not read single-cell `tracks_exemplar`** (§2.5).

**`B_tracking = 28`.** Had the single-cell reading stayed in the predicates it
would have bound at 40; adopting §2.5a saves **2,880 generations** and buys a
better discriminator.

Raising `B_tracking` further remains **compliance, not a deviation** (§8.2); it is
fixed at 28 before the first anchor run and recorded as `B_tracking`,
`B_tracking_floor` and `B_tracking_source`.

### What each rival predicts, and why

The predicates are registered in §2.5. Their motivation:

| Rival | Grid prediction | Reasoning |
|---|---|---|
| **repair artifact** | post tracks first-enumerated **only** | `sanitize_config` coerces and fills to `valid_vals[0]` — literally the first-enumerated value — so reversing the enumeration reverses the repair target. The repair stage never sees the exemplar, which is a prompt object, so it must **not** track it. The model's own pre-repair output is untouched. |
| **format tax** | all four track | The prompt drives the model's own choice, so the effect is present **before** repair; and the prompt carries both the order and the exemplar, so both are expected. Repair cannot undo it. |
| **quantisation / decoding / genuine prior** | none track | Precision, temperature and the weights are all invariant to how the harness lists the options. |

`repair artifact` and `format tax` differ on **all four** grid entries, which is
what makes the column a clean discriminator rather than a single-cell one.

### Confirmatory contrast X5

**X5 — enumeration order at the anchor model, on `tracks_first` (post-repair).**

- Paired sign-flip permutation, paired on **(batch index, exemplar level)**:
  `B_tracking` batches × 2 exemplars = **56 paired differences** (2 × 28).
- **Mode: `monte_carlo`, N = 100,000**, per §3.4's universal tractability rule
  (2³² = 4,294,967,296 ≫ 10⁷). Registered floor
  **1/(1 + 100,000) = 9.99990 × 10⁻⁶ = 0.340% of ALPHA.**
- **X5 remains ONE contrast, at the anchor model only, and FAMILY_SIZE stays 17**
  (R5-2). Column classification at the other two models is **descriptive, by CI
  position** against the chance rate (§2.6) — not a hypothesis test — so it needs
  no contrast of its own. Tripling X5 would take ALPHA to 0.05/19 and tighten the
  threshold for all sixteen other tests to buy nothing the scored columns do not
  already give.
- **Exchangeability:** under the null of no order effect, the sign of each
  (batch, exemplar) difference is exchangeable; pairing is on coordinates matched
  across the order factor.

### Budget

| Component | Generations |
|---|---|
| E1 main grid — 30 cells × 16 × 20 | 9,600 |
| E1 anchor tracking — 12 cells × 28 × 20 | **6,720** |
| **E1 total** | **16,320** |


# 3. Experiment E2 — feedback curation on a tabular benchmark

E2 tests the variable CoLLM-NAS identified, in the regime it did not test:
**small, quantised, single model.** Every prior ablation in the corpus uses
frontier-scale or fine-tuned research-scale models (GPT-4o, 62B PaLM,
purpose-fine-tuned GPT).

## 3.1 Substrate

**NAS-Bench-201 / NATS-Bench topology search space (TSS).** 15,625 architectures;
validation and test accuracy are **table lookups**, so no training occurs and *n*
is limited by generation cost alone.

**All three tasks retained.**

- **Primary: CIFAR-100.** The conservative middle. CoLLM-NAS reports its effect
  largest on ImageNet16-120; choosing that as primary would be choosing the task
  most likely to produce the effect we expect.
- **Secondary: CIFAR-10, ImageNet16-120.** Reported, **not** in the confirmatory
  family, analysed as exploratory (§5.1 A12, §5.4). If the effect appears only on
  ImageNet16-120 it is reported as a secondary finding consistent with
  CoLLM-NAS's difficulty-scaling, **not** as a confirmatory result.

**Why all three.** The substrate is a table lookup: a task adds **no training and
no evaluation cost**, only generation on a locally-served model. Under that cost
structure multi-task coverage is the cheapest external validity in the design, and
a single-task result invites the generalisation objection Yang et al. and Li &
Talwalkar press. Dropping them is **not** a scope reduction this plan recognises
(§8).

This substrate also closes the objection the manuscript concedes
([main.tex:757](paper/main.tex#L757)): the original search space was custom, not
tabular.

## 3.2 Arms

| Arm | Definition |
|---|---|
| **zero-shot** | Each of the *k* proposals generated in a fresh context from the task description alone. No outcome is ever shown. |
| **uncurated in-context accumulation** | Proposal *i*+1 generated in a context containing every prior proposal and its measured validation accuracy, verbatim, appended. Context grows monotonically. The CoLLM-NAS Generator-memory-retained condition, and the structure the original manuscript instantiated. |
| **curated summary** | After each proposal the history is distilled into a bounded strategy statement. **Context is reset each round** and re-seeded with the task description plus the current statement. Raw history never accumulates. |
| **external archive** | Top-*m* proposals and scores held **outside** the model, injected into a fresh context each round. No natural-language history, no growth. |

The curation prompt and *m* are frozen in `prompts/E2/` and hashed into the
results file.

**Generator configuration (primary):** Qwen3-1.7B, NF4, schema-constrained,
post-repair, T = 0.7 — the original paper's stated configuration, so E2's primary
result is measured in the regime E1 characterises. `enable_thinking` **True**,
transcripts stored untruncated (fixing OA-15).

## 3.3 Conditional replicate

After E1 reports, E2's **primary contrast set is re-run once** at the
configuration E1 identifies as least artifactual — defined in advance as the cell,
among those available to a locally-served model, with the highest post-repair
`D_mean`. If that is the primary configuration itself, the replicate is not run
and that is reported. Arms, R, outcome and tests identical; only the generator
configuration differs. This is the sole test of **C5**, evaluated descriptively
(§5.3), so it does not enter the family.

## 3.4 Unit of analysis, estimand, inference

**Unit of analysis: THE RUN, not the architecture.**

One **run** = one search of *k* = 20 proposals, under one arm, at one seed, on one
task. Selection within a run uses **validation** accuracy only. The run's outcome
is the **test** accuracy of the architecture the run selected — test accuracy
never enters selection, fixing OA-11.

**D-20, resolved — validation tie-break.** NAS-Bench-201 contains architectures
with identical validation accuracy, so ties are the expected case, not an edge
case. **Registered rule: among proposals tied on validation accuracy, select the
one with the lowest architecture index in the benchmark's canonical ordering.**
Deterministic, pre-registered, and recorded per run as `selection_tie_count`.
*(Alternatives rejected: first-proposed — makes the outcome depend on generation
order, which differs systematically across arms and would confound the arms with
the tie-break; random — introduces a variance component with no compensating
benefit.)*

### Definition of R

> **`R_final = 24`.** Floor 20; pilot-confirmed value 24; `max(20, 24) = 24`.

**Pilot result (R6-1)** — `scripts/power_e2.py`, seed 20260818, 2,000 simulated
experiments per R × 2,000 permutations, at the registered difference-of-means
statistic and Cliff's-δ tie convention, calibrated to δ = 0.616:

| R | 20 | 22 | **24** | 26 | 28 | 30 | 34 | 40+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| power | 0.702 | 0.752 | **0.822** | 0.873 | 0.890 | 0.922 | 0.963 | ≥0.98 |

**Power at the floor of 20 is 0.702 — below the 0.80 target.** Raising R to 24 is
therefore **COMPLIANCE with this plan, not a deviation** (§3.4 registers the
procedure, not the number). Output at `results/pilots/power_e2.json`.

**Substrate caveat, recorded not hidden.** §3.5 says the pilot variance is drawn
"from the benchmark's own best-of-20 distribution by pure table sampling". **The
NAS-Bench-201 tables are not in this repository and fetching them is outside a
no-compute session.** The pool is SIMULATED — Beta(8,2) scaled to [0.10, 0.74],
bounded and left-skewed like a tabular NAS benchmark — with the run outcome the
max of k = 20 draws, exactly as a run is defined. The registered effect size is
Cliff's δ, a rank statistic, and power at a fixed δ is driven by distributional
overlap, which the simulation controls by construction; but the calibration is
synthetic and is recorded as **S3C-01**.

- The floor of 20 is binding and pre-registered. R may never go below it.
- `scripts/power_e2.py` runs at S3, before any E2 run executes, against a pilot
  variance estimate drawn from the benchmark's own best-of-20 distribution by pure
  table sampling — no generation, no training. It returns the smallest R giving
  power ≥ 0.80 for |δ| ≥ 0.62 at ALPHA.
- **The pilot returned 24, so R_final = 24.** `R_final`, `R_floor` and `R_source`
  are recorded in `results/E2.json`.
- A decrease below the floor is forbidden outright by §8.2 on any grounds.
- R_final is fixed once, before the first run. An increase discovered *after*
  collection begins is a deviation, not compliance.

**Note: ALPHA changed at revision 4**, so the S3 simulation must be run against
**0.0029411764705882353**, not 0.003125. The MDE anchor below is restated
accordingly.

### Estimand

**Primary: mean ± standard deviation of the run outcome across R_final runs.**
Verbatim, Lindauer & Hutter: *"we recommend that, if possible in terms of compute
budgets, all methods should be repeated several times with different seeds and the
authors should report mean and standard deviation (or median and quartiles if the
noise is not symmetric) across the repetitions."* Verbatim, Yang et al.: *"Report
mean and standard deviation of the top-1 test accuracy… for both the randomly
sampled and the searched architectures."*

**Best-of-k curves are reported descriptively as a secondary view only.**

> **We do NOT claim expected-best-of-*k* as a community reporting standard.** The
> S1 corpus critic (C2) checked and found no source supporting it. The claim
> previously recorded in this project — that the NAS 1000-papers survey
> establishes it as the correct estimand — is **NOT IN CORPUS**. The sentence that
> survey contains (*"random search with a budget of k evaluations will, in
> expectation, find architectures in the top 100/k% of the search space"*) is a
> justification for why random search is a strong baseline, not a reporting
> standard. No downstream artifact may cite it as one.

Mean-and-std across R repeated runs **is** an empirical estimate of E[best-of-*k*]
obtained by averaging R independent realisations. The estimand is not abandoned;
the claim about community requirements is.

### Inference (D-16, D-17, D-18, D-19 — all resolved)

**Test statistic — D-17, resolved.** The permutation test statistic is the
**difference of the two arms' sample means of the run outcome**,
`T = mean(arm_a) − mean(arm_b)`, two-sided on |T|. Registered explicitly because a
permutation test on the difference of means, of medians, and on the rank sum give
different p-values on identical data, and revision 3 named none of them.
*(Alternative considered: a rank-sum statistic, which would sit more naturally
beside a rank-based effect size. Rejected because the estimand §3.4 registers is a
mean, and the test should test the estimand being reported.)*

**Tractability — D-16, resolved, and the rule is UNIVERSAL.** Any permutation
distribution in this plan — paired or unpaired, E1 or E2 — is enumerated
**exactly iff its reference set has ≤ 10⁷ members**; otherwise **100,000 random
permutations** with a seed recorded in the results file. The reference set is
2^`B_batch` for a paired sign-flip test and C(n₁+n₂, n₁) for a two-sample test.
Applied: E1's X1–X4 at `B_batch` = 16 give 65,536 → **exact**; X5 at
`B_batch` = 32 gives 4,294,967,296 → **Monte Carlo** (§2.8); E2 at R = 20 gives
C(40,20) = 137,846,528,820 → **Monte Carlo**. **At R = 20, C(40,20) = 137,846,528,820 > 10⁷,
so E2 runs by Monte Carlo**, and its registered floor is
**1/(1 + 100,000) = 9.99990 × 10⁻⁶**, not the exact-test floor of 1.45 × 10⁻¹¹
that revision 3 quoted. Both clear ALPHA; the plan now quotes the one that will
actually be emitted.

Runs are the exchangeable unit. This is the response to OA-12 — the original
applied Welch, Mann–Whitney and a bootstrap to *n* = 20 proposals generated with
serial dependence inside one growing context. Runs are independent by
construction; proposals within a run are not, and are never the unit.

> Serial-dependence-within-one-context inference is **NOT IN CORPUS** (S1 corpus
> critic, C3). All four candidate sources address between-run independence. No
> downstream artifact may attribute a serial-dependence standard to any of them.
> Making the run the unit sidesteps the problem rather than solving it, and the
> paper says so.

**Effect size — Cliff's δ**, with a bootstrap 95% CI. **Not** pooled-SD Cohen's
*d* — OA-13 records that the original paired Welch's *t* (unequal variances) with a
pooled-SD *d* (equal variances) on the same comparison against a 1000:1 variance
ratio.

**D-18, resolved — tie convention.** `δ = (#{a>b} − #{a<b}) / (n₁n₂)`. **Ties
contribute 0 to the numerator and 0.5 each to the Mann–Whitney *U* that §5.5
persists**, which makes `δ = 2U/(n₁n₂) − 1` hold exactly. Registered because
NAS-Bench-201 is a table lookup and identical outcomes are the expected case, and
because OA-9 requires `u_stat` to be persisted "so δ is recoverable" — which is
only true under a stated convention.

**D-19, resolved — BCa jackknife.** The acceleration estimate uses a
**leave-one-run-out jackknife over the pooled set of both arms**: delete one run
from whichever arm it belongs to, recompute δ on the reduced samples, giving
n₁ + n₂ replicates. *(Alternatives rejected: jackknifing one arm only, which
ignores half the influence; and a percentile bootstrap, which is simpler but
loses the bias correction that matters for a bounded statistic like δ.)*

## 3.5 Power / MDE, stopping rule, budget

**Confirmatory contrasts in E2: 4.**

| ID | Contrast |
|---|---|
| Y1 | uncurated vs zero-shot |
| Y2 | curated vs zero-shot |
| Y3 | external archive vs zero-shot |
| Y4 | uncurated vs curated |

**MDE anchor at the floor R = 20**, ALPHA = 0.0029411764705882353, two-sided:
power ≥ 0.80 for |δ| ≥ 0.62, a shift of ≈1.05 pooled SDs. **Provisional** — the
registered quantity is the §3.4 procedure; `scripts/power_e2.py` sets R_final, now
at the revision-4 alpha.

E2's Monte-Carlo floor (9.99990 × 10⁻⁶) is 0.34% of ALPHA, so E2 carries none of
the discreteness constraint that sets E1's batch count. §5.2's gate checks it
anyway.

The MDE is in standardised units only. Translation into accuracy points needs the
benchmark's best-of-20 variance, which is not verified in the corpus; that
translation is produced at S3 by the same script and is not asserted here.

**Stopping rule.** R_final per arm per task, fixed before the first run. **No
interim analyses. No extension on a near-miss. No adaptive stopping.** A run that
crashes is re-executed once at the same seed; twice, and it is recorded as a
failure with `R_effective < R_final` reported in the results file and in the
manuscript's table footnote.

**Generation budget.**

| Component | Generations |
|---|---|
| E1 main grid — 30 × 16 × 20 | 9,600 |
| E1 anchor tracking — 12 × 28 × 20 | 6,720 |
| E2 primary — 4 arms × 24 × 20 × 3 tasks | 5,760 |
| E2 conditional replicate — 4 × 24 × 20 × 1 task | 1,920 |
| E3 | 0 |
| **Total** | **24,000 generations, zero training runs** |

**Both quantities are now pilot-confirmed, so the budget is a number rather than a
formula.** Of the 24,000, roughly **4,160 are frontier API calls** — 1,920 from
the main grid's six frontier cells and 2,240 from the four frontier anchor cells —
which is the only line with a per-call cost.

*(rev 1: 9,400 · rev 2: 12,400 · rev 3: 16,000 · rev 4: 17,280 · rev 5: 19,840 at
the floors · **rev 6: 24,000 confirmed**.)* Every revision has raised it, each
time because that is what made a test decidable or an attribution separable.

---

# 4. Experiment E3 — the proxy size-confound replication (Case B)

*(Unchanged from revisions 1–3 in its entirety.)*

**Bounded scope: a validation-practice finding, not a takedown of RZ-NAS.** Zero
training. Table computation on public data.

## 4.1 Substrate

**NAS-Bench-Suite-Zero** (Krishnakumar, White, Zela, Tu, Safari, Hutter; NeurIPS
2022 D&B). 13 zero-cost proxies × 28 tasks, **1,526,216 pre-computed evaluations**
over **44,798 architectures**, spanning NAS-Bench-101, NAS-Bench-201,
NAS-Bench-301 (DARTS surrogate) and TransNAS-Bench-101 Micro/Macro.

RZ-NAS's menu is GraSP, Gradnorm, Synflow, Zen-Score, ZiCo (plus MAE-DET for COCO
detection). **Four of the five are among the suite's 13.** ZiCo is not and cannot
be — ZiCo is ICLR 2023, the suite is 2022.

## 4.2 What E3 computes

For each proxy ∈ {grasp, grad_norm, synflow, zen-score}, plus baselines {params,
flops}, for **every** (benchmark, task) pair the release covers:

| Statistic | Definition |
|---|---|
| `rho_size` | Spearman ρ, proxy vs **parameter count** — **primary** |
| `tau_size` | Kendall τ-b, same pair |
| `pearson_size` | Pearson *r*, for comparability with the suite's own Table 3 |
| `rho_cellsize` | Spearman ρ, proxy vs **cell size** (non-`none` operation count) |
| `rho_acc` | Spearman ρ, proxy vs validation accuracy |
| `rho_acc_partial` | Spearman **partial** correlation, proxy vs accuracy controlling for parameter count |

Each with a BCa 95% CI (10,000 resamples). `rho_acc_partial` is the quantity that
answers C6: a proxy with high `rho_acc` and near-zero `rho_acc_partial` is
measuring size.

**The comparison that matters** is between where RZ-NAS validated (NAS-Bench-201
only, across three *tasks inside one search space*) and where its headline claims
live and it never validated (DARTS/NAS-Bench-301, TransNAS-Bench-101 Micro and
Macro, NAS-Bench-101). The suite's own RQ1 answer, verbatim: *"Several methods,
such as snip and grasp, perform well on the NAS-Bench-201 tasks, but on average
are outperformed by params and flops on the other benchmarks… on the widely used
NAS-Bench-201 benchmarks, almost all of them perform well."*

## 4.3 ZiCo — transcription only

ZiCo postdates the suite and is **not recomputed**. Numbers are **transcribed**
from its own Table 1 (NATS-Bench-TSS) and Table 3 (NATS-Bench-SSS, the
32,768-architecture space varying **only** channel width — the cleanest available
isolation of size). Every transcribed number carries its source table number,
source note ID and `transcribed: true`. **No transcribed number is presented as a
recomputation**, and no ZiCo statistic enters any inferential test.

## 4.4 MANDATORY CAVEATS — carried verbatim into every downstream artifact

Copied verbatim into the manuscript, any slide deck, and any rebuttal raising E3.
Not paraphrased, not compressed.

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
> published table verbatim, matching to two decimals across every cell, so "two
> independent sources agree" is also false. The finding is struck. It does not
> appear as evidence, as an aside, or in an appendix.

E3 runs **no inferential tests** and is **not** in the confirmatory family. C6's
threshold (`rho_size ≥ rho_acc` for ≥2 proxies off NAS-Bench-201) is evaluated by
comparing point estimates and their CIs, and reported as met or not met with the
CIs shown.

---

# 5. Analysis protocol and deviation rules

## 5.1 Every statistic to be computed, named in advance

| ID | Exp | Statistic | Kind |
|---|---|---|---|
| A1 | E1 | D per batch | descriptive |
| A2 | E1 | D per cell: mean ± std across 16 batches | descriptive |
| A3 | E1 | parse-failure rate per cell | descriptive |
| A4 | E1 | normalised per-field entropy, per field × stage × cell | descriptive |
| A5 | E1 | repair-channel counts per field × cell | descriptive |
| A6 | E1 | `D_rand` (corrected uniform, fixed-K) and `D_repo_sampler` | descriptive |
| A7 | E1 | rival signature score, 5 rivals × 3 models, 6 columns | classification |
| **X1** | E1 | free-prose vs schema, post-repair, NF4, T=0.7 — paired permutation | **confirmatory** |
| **X2** | E1 | schema pre-repair vs post-repair — paired permutation | **confirmatory** |
| **X3** | E1 | NF4 vs bf16, schema post-repair, T=0.7 — paired permutation | **confirmatory** |
| **X4** | E1 | T=0.3 vs T=1.0, schema post-repair, NF4 — paired permutation | **confirmatory** |
| **X5** | E1 | canonical vs reversed enumeration order, **anchor model**, on `tracks_first` post-repair — paired permutation on (batch, exemplar), Monte Carlo | **confirmatory** |
| A8 | E2 | run outcome: mean ± std per arm × task | descriptive |
| A9 | E2 | best-of-*k* curve per arm × task | descriptive, secondary view |
| A10 | E2 | Mann–Whitney *U* per contrast (persisted, fixing OA-9) | descriptive |
| A11 | E2 | Cliff's δ + BCa 95% CI per contrast | effect size |
| **Y1** | E2 | uncurated vs zero-shot, primary task | **confirmatory** |
| **Y2** | E2 | curated vs zero-shot, primary task | **confirmatory** |
| **Y3** | E2 | external archive vs zero-shot, primary task | **confirmatory** |
| **Y4** | E2 | uncurated vs curated, primary task | **confirmatory** |
| A12 | E2 | all four contrasts on the two secondary tasks | exploratory, no p-values |
| A13 | E2 rep | arm ordering + pairwise CIs at the E1-identified configuration | descriptive |
| A14 | E3 | the six correlation statistics with BCa CIs, per proxy × benchmark × task | descriptive |
| A15 | E3 | C6 threshold evaluation | classification |
| A16 | E1 | `D_cell_pooled` + BCa interval, per cell × stage | descriptive |
| A17 | E1 | **paired batch-level** BCa interval on ΔD for the `bf16` and `high temp` contrasts | descriptive |
| A18 | E1 | `S` per batch, `S_mean ± S_std` per cell, `S_cell_pooled` with BCa | descriptive |
| A19 | E1 | boundary-straddle flags: cells scored `indeterminate` | classification |
| A20 | all | `min_attainable_p` planned and realised, plus §5.2 gate verdicts | gate / audit |
| A21 | E1 | `tracks_first` and `tracks_exemplar` proportions with BCa intervals, per cell × stage (all four aggregates); modal-tie counts. **`tracks_exemplar` is reported but read by no predicate** (§2.5). | descriptive |
| **A27** | E1 | **the cross-level exemplar delta Δ per (order, stage), its BCa interval and its label** *(new, R6-2)* | **descriptive** |
| **A22** | E1 | **per-field chance rates and the vocabulary-weighted aggregate actually applied, per cell** *(new, R5-9)* | **descriptive** |
| **A23** | E1 | **per-field `modal_value`, per (field, stage, batch)** *(new, R5-9)* | **descriptive** |
| **A24** | E1 | **the 2×2 tracking label grid per cell, and the predicate outcome per rival** *(new, R5-5/R5-9)* | **classification** |
| **A25** | E1 | **ΔD per change contrast, with its paired batch-level BCa interval** *(new, R5-9)* | **descriptive** |
| A26 | E1 | `contingent_on_indeterminacy` flag, `n_indeterminate`, `would_win_at_n_s_6` | classification |
| **A28** | all | **the two pilot records, marked `pilot`/`confirmatory: false`/`quarantined_from_analysis`** *(new, R6-1)* | **design parameter, NOT analysis** |

**Confirmatory tests: X1–X4 across 3 models = 12, plus X5 = 1, plus Y1–Y4 = 4.
Total 17 — unchanged from revisions 4 and 5.** A1–A28 carry no p-value.

**The cross-level delta (A27) adds no test.** Like every other tracking label it
is classified by CI position, not by a hypothesis test, so it consumes A27 and
produces no p-value. **The pilots (A28) are not analysis at all**: they set
`R_final` and `B_tracking` and are quarantined from the corpus.

**Why extending the tracking sub-design to three models added no test (R5-2).**
A7's signature match is a **classification**, not a hypothesis test: each column's
label comes from a CI position (§2.6), and the winner from a count against
`ceil(0.75·n_s)`. Scoring the tracking column at Qwen3-8B and the frontier model
therefore consumes A21–A24 and produces no p-value. X5 exists to give the
**anchor** an inferential check on the order effect; replicating it per model
would take FAMILY_SIZE to 19 and ALPHA to 0.05/19 = 0.0026315789473684210,
tightening every other test's threshold by 10.5% for no gain the descriptive
columns do not already deliver.

## 5.2 Multiplicity correction and the pre-flight gates

- **Family:** the 17 confirmatory tests named in §5.1.
- **Procedure:** Bonferroni.
- **FAMILY_SIZE = 17.**
- **ALPHA = 0.05 / 17 = 0.0029411764705882353.**

*(Revisions 1–3 registered FAMILY_SIZE = 16, ALPHA = 0.003125. R4-1 adds exactly
one confirmatory test, X5, and the alpha follows. No other amendment adds,
removes or reclassifies a test — the per-amendment check is in §9.)*

Holm–Bonferroni was considered and rejected across all four revisions. It is
uniformly more powerful at the same FWER but yields a step-down sequence rather
than a single number, and the defect this plan exists to prevent (OA-5: the
manuscript declared 0.05/7 while the code applied 0.05/15) is a *number-matching*
defect. A single stated constant a script can assert against is worth more here
than the power.

### Gate 1 — family and alpha

The emitter:
1. reads `FAMILY_SIZE = 17` and `ALPHA = 0.0029411764705882353` from a single
   module-level constant, the same one this document states;
2. writes `alpha_applied` onto **every** emitted statistic;
3. asserts the count of `confirmatory: true` statistics is exactly 17 — **aborts**
   otherwise;
4. asserts every `alpha_applied` equals the top-level `alpha` — **aborts**
   otherwise.

X3 is undefined for the frontier model (no precision factor).
Its slot is retained and emitted as
`{"id": "X3.frontier", "status": "not_applicable", "permutation_mode": "not_applicable", "p": null, "significant": null, "confirmatory": true, "alpha_applied": ALPHA}`
so the count stays exactly 17 **and the slot carries `alpha_applied`**, which
revision 3's specimen omitted — causing the plan's own literal example to trip its
own G-alpha gate. Shrinking the family after registration is the failure mode
being guarded against.

### Gate 2 — the permutation floor is FATAL

**Defect class closed.** Revision 1 registered E1 at `B_batch` = 5, whose paired
floor is 2/2⁵ = **0.0625**, twenty times its alpha. X1–X4 were **structurally
incapable of rejecting, whatever the data showed** — registered and hashed without
the defect being visible. This gate closes the class so no future revision,
deviation or run-time degradation reintroduces an undecidable confirmatory test
silently.

**Plan-load arm — hard abort, before any data is read.** At emitter start-up,
before any results file, generation log or benchmark table is opened:

5. compute `min_attainable_p` for **every** confirmatory test from the declared
   design alone:
   - **paired exact:** `2 / 2^B_batch`
   - **unpaired exact:** `2 / C(n₁+n₂, n₁)`
   - **Monte-Carlo:** `1 / (1 + n_permutations)`
   - **`not_applicable`:** exempt, and recorded as exempt;
6. **ABORT if any confirmatory test has `min_attainable_p ≥ ALPHA`**, naming the
   test, its `B_batch` or *n*, its floor and ALPHA;
7. record every floor and the verdict in `discreteness_gate` (§5.5).

**The permitted values of `permutation_mode` are exactly
`paired_exact`, `unpaired_exact`, `monte_carlo`, `not_applicable`. are exactly `paired_exact`,
`unpaired_exact`, `monte_carlo`, `not_applicable`; revision 3's schema example
wrote `"exact"`, which is not one of them, and the schema has used the enum since
revision 4.

**R6-1 — the full table re-run at ALPHA = 0.0029411764705882353, all 17 tests,
at the pilot-confirmed `R_final = 24` and `B_tracking = 28`.**

Neither pilot moved a floor. X5's reference set grows from 2³² to **2⁵⁶** (2 × 28
paired differences), and E2's from C(40,20) to **C(48,24) ≈ 3.2 × 10¹³** — both
already past the 10⁷ tractability cut, so both still run by Monte Carlo and their
floors depend on **N**, not on the count.

| # | Test | Model | Mode | Design | `min_attainable_p` | % of ALPHA | Verdict |
|---:|---|---|---|---|---:|---:|---|
| 1 | X1 free-prose vs schema | Qwen3-1.7B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 2 | X1 | Qwen3-8B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 3 | X1 | frontier | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 4 | X2 pre- vs post-repair | Qwen3-1.7B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 5 | X2 | Qwen3-8B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 6 | X2 | frontier | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 7 | X3 NF4 vs bf16 | Qwen3-1.7B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 8 | X3 | Qwen3-8B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 9 | X3 | frontier | `not_applicable` | — | exempt | — | **PASS** |
| 10 | X4 T=0.3 vs T=1.0 | Qwen3-1.7B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 11 | X4 | Qwen3-8B | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 12 | X4 | frontier | `paired_exact` | B_batch = 16 | 3.051758e-05 | 1.038% | **PASS** |
| 13 | **X5 enumeration order** | anchor | `monte_carlo` | 56 pairs, N = 100,000 | 9.999900e-06 | 0.340% | **PASS** |
| 14 | Y1 uncurated vs zero-shot | — | `monte_carlo` | R = 24, N = 100,000 | 9.999900e-06 | 0.340% | **PASS** |
| 15 | Y2 curated vs zero-shot | — | `monte_carlo` | R = 24, N = 100,000 | 9.999900e-06 | 0.340% | **PASS** |
| 16 | Y3 archive vs zero-shot | — | `monte_carlo` | R = 24, N = 100,000 | 9.999900e-06 | 0.340% | **PASS** |
| 17 | Y4 uncurated vs curated | — | `monte_carlo` | R = 24, N = 100,000 | 9.999900e-06 | 0.340% | **PASS** |

**The binding floor is X1–X4's paired-exact 3.051758e-05, at 1.038% of ALPHA —
almost two orders of margin.**

Fallbacks and reference values, **none of them operative**:

| Case | Reference set | Cut | Runs as | Floor |
|---|---:|---|---|---:|
| Frontier cell with seeds unhonoured | C(32,16) = 601,080,390 | > 10⁷ | `monte_carlo` | 9.999900e-06 |
| X5 if enumerated exactly | 2⁵⁶ ≈ 7.2 × 10¹⁶ | > 10⁷ | `monte_carlo` | *(not used)* |
| Y1–Y4 if enumerated exactly | C(48,24) ≈ 3.2 × 10¹³ | > 10⁷ | `monte_carlo` | *(not used)* |

**No floor moved and none fails. No STOP condition triggered.** Both pilot
parameters only enlarge already-intractable reference sets, so both tests stay on
Monte Carlo at N = 100,000 and their floors are unchanged.

**No floor fails. No STOP condition triggered.**

**Run-time arm — no silent degradation.** Null batches (§2.7) and failed runs
(§3.5) reduce the realised count after the plan-load gate has passed, raising the
floor. So the emitter also:

8. recomputes `min_attainable_p` from the **realised** usable count, emitting it
   as `min_attainable_p_realised` beside the planned value;
9. where the realised floor ≥ ALPHA, emits that contrast with
   `status: "undecidable_by_discreteness"` and `significant: null` — **never
   `significant: false`** — and the manuscript reports it as undecidable rather
   than as evidence of no effect.

The run-time arm does not abort: one degraded cell should not destroy an otherwise
valid analysis. It refuses to let a degraded cell be *read as a null*, which is the
actual hazard. The plan-load arm aborts because a floor violation there is a
design error with nothing to salvage.

**D-23, resolved — one canonical name.** The quantity is `min_attainable_p`. It
appears as `min_attainable_p_planned` and `min_attainable_p_realised` on a
statistic, and as `min_attainable_p` inside `discreteness_gate.per_test[]` where
only the planned value exists. No other spelling is used anywhere.

## 5.3 Confirmatory vs exploratory

E2's conditional replicate (§3.3) tests C5 through **A13**, which is descriptive
(arm ordering plus pairwise CIs), not a null-hypothesis test. C5 is evaluated by
CI overlap and ordering, not by a p-value, and does not enter the 17-test family.

The same applies to A16–A28: intervals, flags, grids and gate records, never
p-values.
Adding a p-value to any of them would be a deviation requiring a `DEVIATIONS.md`
entry **and** — because it would change FAMILY_SIZE — a further revision if before
G2, and nothing at all if after, because after G2 the family is closed.

## 5.4 No-unplanned-analyses rule

**Any analysis not named in §5.1 is exploratory.** It:
- must be labelled "exploratory" at every point of use;
- **may not** carry a p-value or significance marker;
- **may not** appear in the abstract, contributions list, or conclusions;
- must be logged in `DEVIATIONS.md` before it is run.

This includes subgroup breakdowns, alternative metrics, alternative thresholds,
re-analysis at a different alpha, and any comparison suggested by looking at the
data.

## 5.5 Results-file schema

Every number destined for the manuscript is emitted by a script into a versioned
results file. **No number is transcribed by hand.** `results/E1.json`,
`results/E2.json`, `results/E3.json`, `results/E1_reference.json`.

**`schema_version` is `1.5.0`** (rev 1–5: 1.0.0 … 1.4.0). All changes are
additive — every earlier key keeps its meaning.

**D-25, resolved — the results layer is tracked.** `results/` is **removed from
`.gitignore`** at this revision. Revision 3 directed every results file into a
gitignored path, so the layer G5 depends on ("re-running the analysis reproduces
every table and figure") could never have been checked by anyone cloning the
repository.

**Size management, registered:**
- `generations[].raw_text` is stored **inline** for E1's 10,880 generations
  (bounded: `max_new_tokens` × 34 cells; expected well under 100 MB uncompressed).
- E2's generations store `raw_text_sha256` and the **parsed spec only**; the raw
  text is written to `results/raw/E2/<generation_id>.txt` and those files are
  **gzip-compressed as `results/raw/E2.tar.gz`**, tracked, with a manifest of
  per-file SHA-256 in the results file.
- If `results/` exceeds **200 MB**, E1 raw text moves to the same
  hash-plus-archive scheme and the change is logged in `DEVIATIONS.md`.

**D-21, resolved — `generations[]`.** Every pooled, bootstrapped or entropy
quantity must be recomputable from these records alone.

```json
{
  "schema_version": "1.5.0",
  "experiment": "E1",
  "plan_revision": 6,
  "plan_sha256": "<SHA-256 of EXPERIMENT_PLAN_R4.md at freeze>",
  "plan_supersedes_sha256": "e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201",
  "plan_chain_sha256": [
    "aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d",
    "a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1",
    "be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03",
    "738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d",
    "e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201"
  ],
  "code_commit": "<git rev-parse HEAD>",
  "generated_at": "<ISO-8601 UTC>",
  "environment": {"python": "", "torch": "", "transformers": "",
                  "bitsandbytes": "", "cuda": "", "gpu": "", "driver": ""},
  "model": {"requested": "", "served": "", "revision": "", "quantisation": "",
            "enable_thinking": true, "max_new_tokens": 0, "truncation_chars": null},
  "prompts": {"<name>": "<sha256 of frozen prompt file>"},
  "seeds": [7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008,
            7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016],
  "n_batches_per_cell": 16,
  "b_tracking": {"value": 28, "floor": 16,
                 "source": "results/pilots/pilot_tracking.json",
                 "binding_quantity": "cross_level_exemplar"},
  "r_final": {"value": 24, "floor": 20,
              "source": "results/pilots/power_e2.json",
              "power_at_floor": 0.702},
  "field_collapse_entropy_threshold": 0.15,
  "exemplar_values": {
    "modal": {"conv_type": "standard_3x3", "activation": "relu",
              "normalization": "batchnorm"},
    "non_modal": {"conv_type": "depthwise_separable", "activation": "gelu",
                  "normalization": "groupnorm"},
    "note": "names 3 of the 6 per-block fields; tracks_exemplar's denominator is those 3"
  },
  "chance_rates": {"conv_type": 0.25, "channels": 0.25, "activation": 0.25,
                   "normalization": 0.25, "skip_connection": 0.3333333333333333,
                   "pooling": 0.25,
                   "aggregate_all_six": 0.2638888888888889,
                   "aggregate_exemplar_fields": 0.25},
  "tracking_label_rule": "one_sided_at_chance",

  "d_rand": {
    "value": 0.719205,
    "definition": "corrected uniform sampler, block count FIXED, mean over K in {3,4,5,6}",
    "seed": 20260817,
    "structure": {"n_batches": 16, "n_per_batch": 20},
    "analytic": 0.718872,
    "sanity_range": [0.705, 0.735],
    "sanity_pass": true,
    "d_repo_sampler": 0.771931,
    "sampler_file_sha256": "c656cedf8ff8f543805c6351e6989555036a43519cb4ec81475b0f11499c4914",
    "sampler_extract_sha256": "d8e551f56766c74314caf3ca7a85e4fdb36b5c08282575865f983977270fef4e",
    "extraction_method": "ast source extraction; search_space.py imports torch at module level"
  },

  "bootstrap": {"resamples": 10000, "method": "BCa", "seed": 90210,
                "resampling_unit_pooled": "generation",
                "resampling_unit_delta": "batch_index_pair",
                "resampling_unit_tracking": "batch",
                "resampling_unit_cliffs_delta": "run"},
  "confirmatory_family_size": 17,
  "alpha": 0.0029411764705882353,

  "discreteness_gate": {
    "checked_at": "plan_load", "verdict": "pass",
    "alpha": 0.0029411764705882353,
    "per_test": [{"id": "X5.anchor", "mode": "monte_carlo", "n_planned": 100000,
                  "min_attainable_p": 9.99990000099999e-06, "pass": true,
                  "exempt": false}]
  },

  "generations": [
    {
      "generation_id": "E1.CELL_ID.b03.g07",
      "cell_id": "", "batch": 3, "index_in_batch": 7, "seed": 7004,
      "enumeration_order": "canonical", "exemplar": "modal",
      "raw_text": "<verbatim response, untruncated>",
      "raw_text_sha256": "",
      "finish_reason": "",
      "parse_outcome": "parsed | parse_failed",
      "parse_error": null,
      "spec_pre_repair": {"blocks": [], "global_pool": "", "fc_layers": 1},
      "spec_post_repair": {"blocks": [], "global_pool": "", "fc_layers": 1},
      "repair_channels": {"<field>": ["passthrough", "coerced", "filled"]},
      "metrics_computed_at": {"D": ["pre_repair", "post_repair"],
                              "S": ["raw"],
                              "field_entropy": ["pre_repair", "post_repair"],
                              "anchor_tracking": ["pre_repair", "post_repair"]}
    }
  ],

  "cells": [
    {
      "cell_id": "",
      "factors": {"model": "", "format": "", "precision": "", "temperature": 0.0,
                  "enumeration_order": null, "exemplar": null},
      "seed_honoured": true,
      "batches": [
        {"batch": 0, "seed": 7001, "n": 20, "parse_failures": 0,
         "generation_ids": [],
         "D_pre": null, "D_post": null,
         "S": null, "empty_trigram_count": 0,
         "field_entropy_pre": {}, "field_entropy_post": {},
         "repair_channels": {"<field>": {"passthrough": 0, "coerced": 0, "filled": 0}},
         "collapsed_fields_pre": [], "collapsed_fields_post": [],
         "modal_value_pre": {"<field>": null}, "modal_value_post": {"<field>": null},
         "tracks_first_pre": null, "tracks_first_post": null,
         "tracks_exemplar_pre": null, "tracks_exemplar_post": null,
         "n_first_pre": 0, "n_first_post": 0,
         "n_exemplar_pre": 0, "n_exemplar_post": 0,
         "modal_tie_count": 0}
      ],
      "D_pre_mean": null, "D_pre_std": null,
      "D_post_mean": null, "D_post_std": null,
      "D_pre_pooled": null, "D_pre_pooled_ci95": [null, null],
      "D_post_pooled": null, "D_post_pooled_ci95": [null, null],
      "S_mean": null, "S_std": null, "S_pooled": null, "S_pooled_ci95": [null, null],
      "tracks_first_pre_mean": null,      "tracks_first_pre_ci95": [null, null],
      "tracks_first_post_mean": null,     "tracks_first_post_ci95": [null, null],
      "tracks_exemplar_pre_mean": null,   "tracks_exemplar_pre_ci95": [null, null],
      "tracks_exemplar_post_mean": null,  "tracks_exemplar_post_ci95": [null, null],
      "chance_rate_applied_first": null, "chance_rate_applied_exemplar": null,
      "cross_level_exemplar": {"point": null, "ci95": [null, null],
                               "n_batches_used": 0, "n_null_batches": 0,
                               "chance_rate": 0.0, "label_registered": "",
                               "reason": ""},
      "null_batches": 0, "null_S_batches": 0,
      "null_tracking_batches_first": 0, "null_tracking_batches_exemplar": 0,
      "label_pre": "", "label_post": "",
      "label_tracking_grid": {"pre_first": "", "post_first": "",
                              "cross_level": ""},
      "label_tracking_unread": {"pre_exemplar": "", "post_exemplar": ""},
      "tracking_predicate_outcome": {"repair_artifact": "", "format_tax": "",
                                     "quantisation": "", "decoding": "",
                                     "genuine_prior": ""},
      "boundary_straddle": false, "status": "ok"
    }
  ],

  "statistics": [
    {
      "id": "X5.anchor",
      "kind": "paired_permutation",
      "contrast_operands": {"left": {"cell_id": "", "stage": "post_repair",
                                     "quantity": "tracks_first"},
                            "right": {"cell_id": "", "stage": "post_repair",
                                      "quantity": "tracks_first"}},
      "contrast": "canonical vs reversed enumeration order",
      "paired": true, "pairing_key": ["batch", "exemplar"],
      "permutation_mode": "monte_carlo",
      "test_statistic": "difference_of_means",
      "n_pairs_planned": 32, "n_pairs_realised": 32, "n_permutations": 100000,
      "permutation_seed": 90210,
      "min_attainable_p_planned": 9.99990000099999e-06,
      "min_attainable_p_realised": 9.99990000099999e-06,
      "estimate": null, "ci95": [null, null], "delta_ci95_boot": [null, null],
      "p": null, "alpha_applied": 0.0029411764705882353,
      "confirmatory": true, "significant": null,
      "effect": {"metric": "cliffs_delta", "value": null, "ci95": [null, null],
                 "u_stat": null, "tie_convention": "ties 0 to delta, 0.5 to U"},
      "status": "ok"
    }
  ],

  "deltas": [
    {"id": "bf16.qwen3-1.7b", "column": "bf16",
     "from_cell": "", "to_cell": "", "stage": "post_repair",
     "delta_d_mean": null, "ci95": [null, null],
     "destination_label": "", "label": ""}
  ],
  "signature_match": {
    "<model>": {"repair_artifact": 0, "format_tax": 0, "quantisation": 0,
                "decoding": 0, "genuine_prior": 0,
                "n_scoreable": 6, "winning_threshold": 5,
                "indeterminate_columns": [],
                "indeterminacy_routes": {"<column>": ""},
                "winner": "", "verdict": "",
                "contingent_on_indeterminacy": false,
                "n_indeterminate": 0, "would_win_at_n_s_6": null}
  },
  "na_counts": {}, "failures": []
}
```

New in `1.4.0` — all additive, and all of it closing a Block D coverage gap S3b
found (R5-3, R5-9):

| Field | Closes |
|---|---|
| `tracks_first_pre_mean` / `_ci95`, `tracks_exemplar_pre_mean` / `_ci95` | **S3B-12 — the blocking one.** Revision 4 stored the post-repair aggregates only, so `repair artifact` and `format tax` — which both hinge on the pre-repair value — could not both be scored from the results file. |
| `label_tracking_grid` (replaces `label_tracking`) | S3B-13 — one string could not carry a 2×2 grid |
| `tracking_predicate_outcome` | makes each rival's predicate result auditable |
| `modal_value_pre` / `_post` per field | S3B-14 — the indicator was checkable only by recomputing from raw specs |
| `exemplar_values` (header) | S3B-14 — the map lived only in §2.8's prose |
| `chance_rates` (header), `chance_rate_applied_*` (cell) | S3B-11 / R5-1 — the one-sided rule is auditable only if the rate it used is recorded |
| `tracking_label_rule` | records which of the three candidate rules was applied |
| `field_collapse_entropy_threshold` | S3B-01 — the denominator's definition |
| `n_first_*`, `n_exemplar_*` | S3B-02 — the two denominators differ and are now both stated |
| `deltas[]` | S3B-15 — ΔD had no field and was derived at analysis time |
| `b_tracking` | R5-8 |
| `null_tracking_batches_first` / `_exemplar` | the two quantities can be insufficient independently |
| `contingent_on_indeterminacy`, `n_indeterminate`, `would_win_at_n_s_6`, `indeterminacy_routes` | R5-6 / S3B-07 |
| `bootstrap.resampling_unit_tracking` / `_cliffs_delta` | S3B-03 |

New in `1.5.0` (R6-1, R6-2): `r_final` (header), `b_tracking.binding_quantity`,
`cells[].cross_level_exemplar`, `label_tracking_grid` reshaped to the three
entries the predicates read, and `label_tracking_unread` carrying the single-cell
`tracks_exemplar` labels that are emitted but scored by nothing.

Carried forward from `1.3.0`: `generations[]`, `d_rand`, `contrast_operands`,
`pairing_key`, `test_statistic`, `enumeration_order`, `exemplar`,
`collapsed_fields_*`, `tracks_*` per batch, `modal_tie_count`, `n_scoreable`,
`winning_threshold`, `effect.tie_convention`, `generation_ids`.

**D-21's structural fix.** `contrast_operands` replaces the free-text `contrast`
as the machine-readable operand record: revision 3's schema identified a
contrast's operands **only** by a prose string, and did not identify which
**stage** was compared at all. Both are now explicit fields, so replay does not
require parsing prose.

`results/E2.json` additionally carries `R_floor`, `R_final`, `R_source`,
`R_effective` per arm, and `selection_tie_count` per run; its `runs[]` entries
carry run id, arm, task, seed, the 20 proposal specs with their looked-up
validation and test accuracies, the selected index, and the outcome.
`results/E3.json` carries `correlations[]` with `transcribed`, `source_table`,
`source_note_id`.

**Manuscript binding rule.** No numeric literal is typed into the `.tex`. Every
number resolves to a `results/<exp>.json` key through a lookup macro, and a
checker script verifies at build time that every numeric token in the manuscript
body has a resolvable key. This is the G5 criterion, and it is now checkable by a
third party because the results layer is tracked.

## 5.6 DEVIATIONS.md protocol

`DEVIATIONS.md` carries no deviation entries as of revision 4's hash.

1. **Any departure is logged in `DEVIATIONS.md` BEFORE the analysis it affects is
   run.** Not after. Not at write-up.
2. Each entry carries: date, plan section, what changed, why, and **whether data
   had already been collected for the affected analysis**.
3. An entry added *after* the affected analysis has run is a protocol violation
   and is labelled `LATE — PROTOCOL VIOLATION` in its own heading. Not deleted,
   not backdated.
4. **This plan is not edited after its hash is taken.** Changes go in
   `DEVIATIONS.md`. If superseded wholesale, a numbered revision is written as a
   new file, hashed separately, and cites the prior hash; every superseded plan
   file stays byte-identical. **This revision route closes at the END OF S3**,
   when the analysis code exists and G2 is signed against a plan that has been
   executed rather than only read. The ordering has now caught defects twice —
   25 at S3a against revision 3, 18 at S3b against revision 4 — so it is
   registered, not optional.
5. Every deviation entry is committed before the run it governs, so git history
   independently timestamps the ordering.

---

# 6. Citations the paper is obliged to carry

*(Unchanged.)* Sourced from `audit/references_verified.bib`, never from memory.
**Ten of the fifteen are absent from that file** — they post-date the S0
bibliography audit, which verified the manuscript's existing 47 entries and added
none. Metadata below is from vault notes — fetched source records, not recall —
with note IDs so each is traceable. **They must be added and verified against an
academic API before S6 writing** (OA-38).

| # | Work | Status | Key / source |
|---|---|---|---|
| 1 | **EvoPrompting** — Chen, Dohan, So | in bib | `chen2023evoprompting` |
| 2 | **GENIUS** — Zheng et al. | in bib | `zheng2023genius` |
| 3 | **LLMatic** — Nasir et al. | in bib | `nasir2024llmatic` |
| 4 | **Li & Talwalkar**, UAI 2019 | in bib | `li2020random` |
| 5 | **Yang et al.**, ICLR 2020 | in bib | `yang2020evaluating` |
| 6 | **CoLLM-NAS** — Oral, CVPR 2026 NAS Workshop | **ABSENT** | arXiv:2509.26037v2 — `250926037v2-collm-nas-collaborative-large-language-models-for-efficient-knowledg` |
| 7 | **RZ-NAS** — Ji et al., ICML 2025, PMLR v267 | **ABSENT** | `proceedings.mlr.press/v267/ji25a.html` — `icml-poster-rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflectiv` |
| 8 | **The Format Tax** | **ABSENT** | arXiv:2604.03616 — `260403616-the-format-tax` |
| 9 | **Let Me Speak Freely?** — Tam et al. | **ABSENT** | arXiv:2408.02442 — `240802442-let-me-speak-freely-a-study-on-the-impact-of-format-restrictions-on-pe` |
| 10 | **Grammar-Aligned Decoding** | **ABSENT** | arXiv:2405.21047 — `240521047-grammar-aligned-decoding` |
| 11 | **The Parser Already Knows** | **ABSENT** | arXiv:2608.10137 — `260810137-the-parser-already-knows-lightweight-bias-correction-in-constrained-de` |
| 12 | **NAS-Bench-Suite-Zero** — NeurIPS 2022 D&B | **ABSENT** | arXiv:2210.03230 — `221003230-nas-bench-suite-zero-accelerating-research-on-zero-cost-proxies` |
| 13 | **ZiCo** — ICLR 2023 Spotlight | **ABSENT** | arXiv:2301.11300 — `zico-zero-shot-nas-via-inverse-coefficient-of-variation-on-gradients-full-text` |
| 14 | **ZiCo-BC** — ICCV Workshop 2023 | **ABSENT** | arXiv:2309.14666 — `zico-bc-a-bias-corrected-zero-shot-nas-for-vision-tasks-full-text` |
| 15 | **Lindauer & Hutter** | **ABSENT** | arXiv:1909.02453v3 — `190902453v3-best-practices-for-scientific-research-on-neural-architecture-search` |

Rows 8–11 establish the mechanism this paper applies, and therefore establish what
it may *not* claim (§1.2); rows 12–14 are E3's entire evidence base; row 15 is the
only citable source in the corpus for E2's estimand.

**Also obliged:** **NAS-Bench-201** (`dong2020nasbench201`, in bib) as E2's
substrate, **NAS-Bench-101** (`ying2019nasbench101`, in bib), and the **NAS
1000-papers survey** (`white2023nas`, in bib) — the last cited **only** for its
random-search-baseline point, never as an estimand recommendation (§3.4).

**New at revision 4.** §2.8's manipulation touches the in-context-ordering and
exemplar literature. Whatever is cited there must be cited as **prior art for the
mechanism**, consistent with §1.2's defect rule — not as something this paper
discovers. The specific sources are an S6 task and are recorded as an open action.

---

# 7. What this plan does not do

- **It does not recover the original data.** OA-1 is closed. Every ORPHAN finding
  in `audit/CLAIM_TRACE.md` is permanent. Nothing in E1–E3 re-establishes any
  number in the current manuscript.
- **It does not train anything.** E1 is generation and structural measurement; E2
  is generation plus table lookup; E3 is table computation. Total training runs:
  zero.
- **It does not settle whether CoLLM-NAS's noise-accumulation ablation has been
  independently replicated.** Five candidate citing papers are unverified leads
  (OA-37). None may be cited as corroboration until fetched and read.
- **It does not resolve the generating model of the original run.** OA-3 stands
  and is unresolvable.
- **It does not test MAE-DET**, the DARTS-space parameter-range question L5 left
  open, or the GENIUS Appendix A.3 tables L1 sampled only partially (seam S3).
- **It does not claim order or exemplar effects as novel** (§1.2, §6).
- **It does not attribute tracking to a particular field.** Enumeration order is
  reversed for **every** field simultaneously (§2.8), so a positive tracking
  result shows the harness drives *something*, not *which field*. Per-field
  reversal was considered and declined: it would need six further cells per model
  and the `passthrough` / `coerced` / `filled` decomposition (§2.4.4) already
  supplies per-field evidence on the repair side. **The limit is registered, not
  discovered later.**
- **It does not falsify the rival set on the two free-prose-side level columns.**
  See §2.5's KNOWN LIMITATION: every level label is predicted by some rival there,
  so those columns discriminate between rivals but cannot reject them all.

---

# 8. Scope protection

## 8.1 The calendar consideration: CONSIDERED AND REJECTED

**This project plans on merit and scope. It does not plan around submission dates.
The venue follows the artifact, not the reverse.**

1. **The chosen venue is non-archival** (`VENUE.md`). Missing a cycle costs
   **nothing** — no priority, no publication window, no claim to the result.
2. **Workshop cycles recur.** A design weakened to fit a date is permanent; a date
   missed is not.
3. **The failure this project exists to correct was produced by exactly this
   pressure.** The original manuscript's defects — an unrecoverable dataset, a
   declared correction that did not match the applied one, "pre-specified"
   comparisons computed exhaustively, a replication subsection with no evidentiary
   basis — are the signature of work shaped by a deadline rather than by a design.
4. **Every revision has raised the budget, not lowered it** — 9,400 → 12,400 →
   16,000 → **17,280** at the floor — each time because that is what made a
   confirmatory test decidable or an attribution separable. **When rigour and the
   calendar conflict, rigour wins, and the budget moves.**

## 8.2 What this forecloses

Not available as scope reductions, and not to be proposed at S4 or later on
schedule or budget grounds:

- dropping E1 cells, batches, or generations per batch — **including any reduction
  of `B_batch` below 16**, which must argue against the ceiling table in §2.3 and
  the fatal gate in §5.2, not against cost;
- **dropping §2.5a's cross-level exemplar predicate**, which is the only device
  separating `format tax` from `genuine prior` with an exact null;
- **dropping the §2.8 anchor-tracking sub-design**, which is the only column that
  separates `format tax` from `genuine prior` without depending on free-prose
  parsing, and therefore the only reason C2 is decidable;
- **narrowing that sub-design back to a single model** (R5-2). At one model the
  column is unavailable for the other two and `n_s` falls to 5 there
  automatically, which is the state revision 4 shipped and S3b flagged;
- **reducing `B_tracking` below 28** or **R below 24**, both now pilot-confirmed
  (R6-1). The floors of 16 and 20 bind independently beneath them;
- dropping E2's secondary tasks (§3.1);
- dropping E2's conditional replicate (§3.3), the sole test of C5;
- **reducing R below `R_final = max(20, the S3-confirmed value)`.** The floor of 20
  binds independently: a simulation returning a value *below* 20 does not license
  going below 20. A value *above* 20 raises R_final, and complying is compliance,
  not a deviation (§3.4);
- narrowing the confirmatory family, which would change ALPHA (§5.2).

A scope change on **methodological** grounds remains available — this section
constrains the *reason*, not the possibility. Before G2 it is a further revision;
after G2 a `DEVIATIONS.md` entry, and the revision route is closed.

## 8.3 What is legitimately schedule-sensitive

Nothing in the experimental design. Two things outside it, handled at their own
stages: fetching and byte-verifying `neurips_2026.sty` from two mirrors (S6), and
closing OA-37 and OA-38 before S6 writing. Neither touches E1, E2 or E3.

---

# 9. Defect disposition — the 18 from S3b — NEW

Source: `audit/S3B_SCORER_DEFECTS.md`, found by implementing the two scorers that
decide C2 and running them against 22 synthetic fixture assertions. Every defect
is dispositioned; none is deferred.

| ID | Sev | Disposition at revision 5 | Alternative rejected | § |
|---|---|---|---|---|
| **S3B-01** | BLK | **Field collapse registered:** normalised per-field entropy < **0.15**, mirroring `D < 0.15·D_rand` — both scales put uniform at 1.0. | "entropy exactly 0" (constant): the limiting case, not the phenomenon; a field constant in 19 of 20 generations would have been excluded. | 2.4.4 |
| **S3B-02** | BLK | **Both denominators registered and stated separately:** `tracks_first` over all collapsed fields, `tracks_exemplar` over the three the exemplar names, with `n_first` and `n_exemplar` emitted. | extending the exemplar to all six fields — that changes the manipulation rather than documenting it. | 2.4.7 |
| **S3B-03** | MAT | **Resampling unit registered per statistic**: generation for pooled D, batch-index pair for ΔD, **batch** for the tracking proportions, run for Cliff's δ. | a single global unit, which is what made this wrong. | 2.4.5 |
| **S3B-04** | MIN | **Boundary closed:** an interval endpoint exactly on the chance rate does not exclude it, so `lo == chance` → `no tracking`. Strict `>`, deterministic. | leaving it to the implementer. | 2.6 |
| **S3B-05** | BLK | **Five explicit predicates over the 2×2 grid**, every rival predicting on **both** sub-quantities at **both** stages; `and/or` removed. A predicate is indeterminate only if an entry it reads is. | keeping prose rows and letting the implementer encode them — which is exactly how two implementers would diverge. | 2.5 |
| **S3B-06** | MAT | **`partial` (change) widened** to "the band **OR** a `recovers`-magnitude change into a collapsed destination", so the demotion no longer assigns a label outside its own band. The four change labels partition the line. | a sixth change label (`recovers_into_collapse`) that no rival predicts and could only ever mismatch. | 2.6 |
| **S3B-07** | MAT | **Not prevented — flagged.** A threshold scaling with *n_s* must let indeterminacy create winners; pinning the bar at 5 would make the n_s = 4 and n_s = 5 cases unwinnable. Verdicts below `ceil(0.75·6) = 5` are emitted **`contingent_on_indeterminacy`** with `n_indeterminate` and `would_win_at_n_s_6`. | pinning the threshold, which deletes the generalisation §2.6 exists to provide. | 2.6 |
| **S3B-08** | — | **No defect.** Level boundaries are strict `<`, so a value exactly on one falls in the upper band; verified at the bit level (fixture C13). Recorded because the rule was asked for. | — | 2.6 |
| **S3B-09** | MAT | **Recorded as a KNOWN LIMITATION**, not fixed. Every level label is predicted by some rival on free-prose and schema-pre, so those columns cannot mismatch the whole set and "no rival matched" fires almost only through the change and tracking columns. Stated plainly in §2.5. | inventing a sixth rival to cover the missing labels — none is motivated by the literature, and a rival added to make a falsifier look stronger is not a rival. | 2.5 |
| **S3B-10** | MAT | **The flat 0.50 bar is REJECTED**, with S3b's sweep as the evidence: it returns `indeterminate` at 2.3× and 2.8× chance and is eager to declare absence, biasing systematically toward `genuine prior`. | keeping it "because it is conservative for the claim" — it is conservative in a way that disables the column. | 2.6 |
| **S3B-11** | BLK | **The ONE-SIDED per-field rule is registered.** Chance = 1/\|V_f\|, vocabulary-weighted in aggregate; `tracks` = interval excludes chance from above; `no tracking` = contains it or below; `indeterminate` = insufficient data only. | the **symmetric** per-field rule as originally briefed — it never fires `no tracking` at any plausible rate, making `quantisation`, `decoding` and `genuine prior` unmatchable on this column. | 2.6 |
| **S3B-12** | BLK | **`tracks_{first,exemplar}_pre_mean` and `_ci95` registered at cell level**, alongside the post-repair pair. Without them the column could not be scored from the results file at all. | computing the pre aggregate at analysis time from the per-batch values — which leaves the number the label came from outside the provenance record. | 5.5 |
| **S3B-13** | MAT | **`label_tracking_grid`** replaces the single `label_tracking` string, plus `tracking_predicate_outcome` per rival. | four separate scalar fields — the grid is one object and reads as one. | 5.5 |
| **S3B-14** | MAT | **`modal_value_pre` / `_post` per field emitted**, and **`exemplar_values` registered as a header field** rather than living in prose. | leaving both derivable from `generations[]` — derivable is not checkable. | 5.5 |
| **S3B-15** | MIN | **`deltas[]` registered**, carrying `from_cell`, `to_cell`, `stage`, `delta_d_mean`, its CI, the destination label and the resulting label. | continuing to derive ΔD at analysis time. | 5.5 |
| **S3B-16** | MIN | **Resolved by R5-1**: revision 4's prose already said "excluding chance" while its rule used 0.50. The prose is now the rule. | — | 2.6 |
| **S3B-17** | MAT | **The sub-design runs at all three models** (12 cells). **X5 stays one contrast and FAMILY_SIZE stays 17**, because column classification is descriptive by CI position, not a hypothesis test. | X5 × 3 → FAMILY_SIZE 19, ALPHA 0.05/19: tightens every other test's threshold by 10.5% to buy nothing the scored columns do not already give. | 2.2, 2.8, 5.1 |
| **S3B-18** | MAT | **`B_tracking = max(16, S3 pilot value)`**, floor 16, raising it is compliance. The pilot is pure resampling on synthetic proportions — no model. | relying on R5-2's extra models: that multiplies **cells**, not *n* per cell, and does not narrow the interval. | 2.8, 3.5 |

**Summary:** 5 blocking, 9 material, 3 minor, 1 no-defect. **All 18 dispositioned.**

### Revision 6's scope is closed — and what that means for what it did NOT fix

Revision 6 carries **three things only**: the two pilot-confirmed design
parameters, the cross-level exemplar predicate, and the corrected pilot criterion.
Every other ambiguity S3c found is recorded in `audit/S3C_DEFECTS.md` and, **after
G2, is handled as a `DEVIATIONS.md` implementation decision rather than a plan
change.**

This is deliberate. Five revisions in two days each added machinery, and each
addition generated further defects — 25, then 18, then three found in revision 5's
own drafting. **The growth is the problem being stopped here.** A plan that keeps
acquiring apparatus to close the last round's gaps is not converging on rigour; it
is converging on complexity, and complexity is where the next defect lives.

### Found while drafting revision 5, by re-running the fixtures

Three further defects surfaced during this revision's own implementation pass and
are closed in the text above rather than deferred. Recorded so the recurrence is
visible: **each of the last three revisions has found at least one defect in
itself before freezing.**

| ID | Problem | Resolution | § |
|---|---|---|---|
| **R5-a** | Under `canonical` order the first-enumerated values of the three exemplar fields **are** the `modal` exemplar's values, so `tracks_first` and `tracks_exemplar` are numerically identical in the (canonical, modal) cell and cannot be dissociated. `repair artifact`, which predicts `post_exemplar = no tracking`, was **unsatisfiable there even when true**. | The **degenerate-cell rule**: `tracks_exemplar` is scored only in cells where at least one exemplar field has first-enumerated ≠ exemplar value; the degenerate cell emits `dissociable: false` and its value is taken from a dissociable cell of the same model. | 2.5 |
| **R5-b** | `repair artifact` predicts pre-repair does **not** track — but in that world pre-repair is *diverse*, so no field is collapsed, there is no modal value, and a rule mapping zero collapsed fields to `null` made the column `indeterminate` **exactly when the rival it tests is correct**. | **No collapse means no tracking**: a batch with zero collapsed fields contributes `no tracking`, counted in `n_no_collapse_batches` and excluded from the interval. `indeterminate` is reserved for other unusability. | 2.4.7, 2.7 |
| **R5-c** | Operator decision 4, read as a **conjunction**, made `format tax` **logically unsatisfiable**: in a dissociable cell one modal value cannot equal both the first-enumerated and the exemplar value. | F-T states a value for every grid entry as a **disjunction on the pre pair plus post=pre equality**. R-A's conjunction is satisfiable and is kept. The three predicates stay mutually exclusive. | 2.5 |

**A known sensitivity, recorded not fixed.** `tracks_exemplar` has at most **three**
fields, so its per-batch proportion takes only the values {0, ⅓, ⅔, 1} while its
chance rate is **0.25**. A *single* coincidental match among three therefore reads
as above chance. The 2×2 exemplar factor is the mitigation — a genuine prior
tracks the exemplar under **neither** exemplar level, a format tax under the one
shown — but the per-cell statistic alone is coarse, and any `tracks` verdict on
`tracks_exemplar` must be read together with the other exemplar level rather than
on its own. **This is a limit of a three-field statistic, not a threshold that can
be tuned away.**

**Family check:** none of the 18 dispositions adds a confirmatory test.
**FAMILY_SIZE = 17, ALPHA = 0.05/17 = 0.0029411764705882353 — unchanged.**

---

# 10. Defect disposition — the 25 from S3a *(carried from revision 4)*

Source: `audit/S3A_IMPLEMENTATION_DEFECTS.md`. Every defect is dispositioned; none
is deferred.

| ID | Sev | Disposition at revision 4 | §  |
|---|---|---|---|
| **D-01** | BLOCKING | **`partial` given a ΔD definition:** +0.10·D_rand ≤ ΔD < +0.25·D_rand. *Alternative rejected: replacing the cell, which would have removed the quantisation row's only temperature prediction.* | 2.6 |
| **D-02** | BLOCKING | **Anchor-tracking column added** (§2.8) plus contrast X5. `format tax` and `genuine prior` now differ in two columns, one of which does not require free prose to parse. FAMILY_SIZE 16→17, ALPHA→0.05/17. | 2.5, 2.8 |
| **D-03** | BLOCKING | **Middle band named `partial`; negative direction named `worsens`** (ΔD ≤ −0.10·D_rand). An unnamed-by-any-rival observation **scores as a mismatch, not indeterminate** — `indeterminate` is reserved for unreliable measurement, `worsens` is a reliable measurement that contradicts every rival. | 2.6 |
| **D-04** | BLOCKING | **Frontier substitution registered:** `provider_default` substitutes for the NF4 coordinate in every column definition; the bf16 column is `not_applicable` on that model. No other substitution permitted. | 2.2 |
| **D-05** | MATERIAL | **Resolved by observing the two stages share a subset:** a parse failure is excluded from both stages, so the selection effect is identical at pre- and post-repair. The column stays as literally defined (post-repair) and the caveat now correctly governs it. | 2.1, 2.6 |
| **D-06** | BLOCKING | **Generalised to k indeterminate columns:** winner must match ≥ ceil(0.75·n_s); n_s < 4 → "no verdict". Reproduces "≥4 of 5" exactly at n_s = 5. *Alternative rejected: ceil(0.8·n_s), which at n_s = 4 demands a perfect 4-of-4.* | 2.6 |
| **D-07** | MATERIAL | **One estimand for point and interval:** classification and ΔD use the batch-mean form; the ΔD interval is a paired bootstrap over batch indices. Pooled D and its generation-level bootstrap remain reported but anchor nothing. | 2.4.5 |
| **D-08** | MATERIAL | **`d_rand` block added to the E1 header**, with value, definition, seed, structure, analytic value, sanity range and verdict, plus `d_repo_sampler` and both sampler hashes. | 5.5 |
| **D-09** | MATERIAL | **"Uniform" dropped for the repository sampler; a corrected uniform sampler defined and measured.** The 48.21%-vs-25% `pooling` skew and the block-count variation are both recorded as the cause. | 2.6 |
| **D-10** | MATERIAL | **Sanity range tightened to [0.705, 0.735]**, which rejects the repository sampler (0.7719), the block-free corrected sampler (0.7765) and revision 3's own 0.74 anchor — all three of which [0.65, 0.80] admitted. | 2.6 |
| **D-11** | BLOCKING (worked around) | **`ast` source extraction registered as the method**, with both hashes recorded in the plan and in every results file. *Alternative rejected: reimplementing the sampler, which would silently substitute a different distribution for the one being characterised.* | 2.6, 5.5 |
| **D-12** | MINOR | **`D_RAND_SEED = 20260817` registered** and written into the results file. | 2.6 |
| **D-13** | MINOR | **Reference draw uses the E1 batch structure (16 × 20)**, so the reference and the quantity it anchors have the same shape. The 200-draw pooled form is dropped. | 2.6 |
| **D-14** | MATERIAL | **`permutation_mode` enum fixed** to `paired_exact` / `unpaired_exact` / `monte_carlo` / `not_applicable`; the §5.5 example uses it. | 5.2, 5.5 |
| **D-15** | MATERIAL | **The `not_applicable` specimen now carries `alpha_applied`**, so the plan's own example passes its own G-alpha gate. | 5.2 |
| **D-16** | MATERIAL | **"Tractable" defined numerically and UNIVERSALLY**: any permutation reference set ≤ 10⁷ is enumerated exactly, else Monte Carlo at N = 100,000. E1's X1–X4 (65,536) run exact; **X5 (2³² = 4.29e9) and E2 (C(40,20) = 1.38e11) run Monte Carlo**, and the plan quotes the floors that will actually be emitted. *Caught a second time while drafting revision 4, when X5 was first written as `paired_exact` at 2³² — an unenumerable reference set. Recorded so the recurrence is visible.* | 2.8, 3.4, 5.2 |
| **D-17** | BLOCKING | **Test statistic named: difference of sample means**, two-sided on \|T\|. *Alternative rejected: rank sum, because the registered estimand is a mean and the test should test the estimand.* | 3.4 |
| **D-18** | MATERIAL | **Tie convention registered:** ties contribute 0 to δ's numerator and 0.5 each to *U*, making δ = 2U/(n₁n₂) − 1 exact — which is what makes OA-9's "persist *U* so δ is recoverable" true. | 3.4 |
| **D-19** | MATERIAL | **BCa jackknife registered:** leave-one-run-out over the pooled set of both arms, n₁+n₂ replicates. *Alternatives rejected: one-arm jackknife (ignores half the influence); percentile bootstrap (loses bias correction on a bounded statistic).* | 3.4 |
| **D-20** | MATERIAL | **Validation tie-break registered:** lowest architecture index in the benchmark's canonical ordering, with `selection_tie_count` recorded per run. *Alternatives rejected: first-proposed (confounds tie-break with generation order, which differs by arm); random (adds variance for nothing).* | 3.4 |
| **D-21** | MATERIAL | **`generations[]` added**, plus `contrast_operands`, `pairing_key`, `test_statistic` and per-batch `generation_ids`. Every pooled, bootstrapped and entropy quantity is now recomputable from stored records; operands and stage are machine-readable rather than prose. | 5.5 |
| **D-22** | MINOR | **`B_batch` for batches, `K` for blocks**, applied throughout. | 2.3, 2.4 |
| **D-23** | MINOR | **One canonical name `min_attainable_p`**, with `_planned` / `_realised` suffixes on a statistic and the bare name inside the gate record. No other spelling. | 5.2 |
| **D-24** | MINOR | **`n_blocks`'s exclusion from *G* stated explicitly**, with the double-counting reason. | 2.4.1 |
| **D-25** | MATERIAL | **`results/` removed from `.gitignore`**; size management registered (E1 raw text inline; E2 raw text hashed and archived; a 200 MB trigger to move E1 to the same scheme, logged as a deviation). | 5.5 |

**Per-amendment family check.** R4-1 adds exactly one confirmatory test (X5):
16 → 17. R4-2 (schema), R4-3 (reference), R4-4 (definitions) and R4-5 (arithmetic)
add none. **FAMILY_SIZE = 17, ALPHA = 0.05/17, and every floor in §5.2's table
clears it.**
