# EXPERIMENT PLAN — pre-registered

**Written:** 2026-08-17
**Status at time of writing:** no data collected. The repository contains zero
experimental artifacts (0 RAW / 0 SPEC / 0 TRANSCRIPT across all 24 original
condition × dataset × seed cells, `audit/REPO_INVENTORY.json`). Nothing in this
plan has been run.

This document is frozen at the SHA-256 recorded in `PREREGISTRATION.md`.
It is not edited after that hash is taken. Departures are logged in
`DEVIATIONS.md` (see §5.6).

---

# 1. Thesis and claim set

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
sources establish it (§6, rows 6–9), one of them from the month before this plan
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

## 2.3 Generations per cell, batching, seeding

- **20 generations per batch, 5 batches per cell, 100 generations per cell.**
- **30 cells × 100 = 3,000 generations.** No architecture is trained.
- Batch size 20 matches the original paper's per-condition *n*, so E1's within-
  batch diversity statistic is directly comparable in scale to the original's.
- Diversity is computed **within batch**; a cell reports **mean ± std across its
  5 batches**. This is the same estimand discipline as E2 (§3.4): repeat the
  procedure, report mean and standard deviation across repetitions.

**Seeding scheme.** A single frozen seed vector `S = [7001, 7002, 7003, 7004,
7005]` is shared by **every** cell. Batch *b* of every cell uses `S[b]` for the
sampler. Cross-cell contrasts are therefore **paired at the batch index**, which
removes seed variance from every between-cell comparison. The seed vector is
written into the results file.

For the frontier API, if the provider does not honour a seed parameter, the cell
records `seed_honoured: false` and its five batches are treated as unpaired
replicates. Contrasts involving that cell use the unpaired form of the test, and
the results file flags which form was used per contrast.

## 2.4 Outcomes

### 2.4.1 The design-choice vector

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

### 2.4.2 Primary outcome — mean pairwise structural diversity

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

And, separately, the three repair channels counted per field — this is finer than
the brief specified and is the sharpest instrument in E1, because
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

## 2.5 Pre-registered prediction table — the falsifier set

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

**Free-prose selection effect — pre-registered handling.** Free-prose pre-repair
diversity is conditioned on the generation having parsed at all, which is a
non-random subset. There is no clean fix; a permissive prose-to-fields extractor
was considered and rejected, because it is a second instrument with its own
artifact and would defeat the purpose of the experiment. Instead: the free-prose
parse rate is reported adjacent to every free-prose diversity number, and **if
the free-prose parse rate is below 50%, that cell's diversity estimate is
declared unreliable and the free-prose column is scored `indeterminate` for every
rival** — neither matched nor unmatched — with the maximum achievable signature
score dropping to 4 and the ≥4-of-5 rule reading ≥3-of-4 accordingly.

## 2.7 Ties and degenerate outputs

- A generation that fails to parse contributes to the parse-failure rate and is
  excluded from **both** stages' diversity (it never reaches repair). The pre/post
  contrast therefore always runs over an identical generation set.
- A batch with fewer than 2 parseable generations yields `D = null`. It is
  recorded as null, **never imputed**. The cell's mean is taken over the defined
  batches and the null count is reported beside it. A cell with ≥3 null batches
  is reported as `insufficient` and contributes no signature match.
- An all-identical batch yields D = 0.000 exactly. **This is a legal measurement,
  not a missing value**, and is the single most likely observation in the
  post-repair schema cells.
- Duplicate generations within a batch are retained, not deduplicated —
  duplication *is* the collapse being measured.

---

# 3. Experiment E2 — feedback curation on a tabular benchmark

E2 positions the paper against CoLLM-NAS by testing the variable CoLLM-NAS
identified, in the regime CoLLM-NAS did not test: **small, quantised, single
model.** Every prior ablation in the corpus uses frontier-scale or fine-tuned
research-scale models (GPT-4o, 62B PaLM, purpose-fine-tuned GPT).

## 3.1 Substrate

**NAS-Bench-201 / NATS-Bench topology search space (TSS).** 15,625
architectures; validation and test accuracy are **table lookups**, so no training
occurs and *n* is limited by generation cost alone. Tasks: CIFAR-10, CIFAR-100,
ImageNet16-120.

- **Primary task: CIFAR-100.** Chosen as the conservative middle. CoLLM-NAS
  reports its noise-accumulation effect scaling with task difficulty and largest
  on ImageNet16-120; selecting ImageNet16-120 as primary would be selecting the
  task most likely to produce the effect we expect. It is not the primary.
- **Secondary tasks: CIFAR-10 and ImageNet16-120.** Reported, **not** in the
  confirmatory family. If the effect appears only on ImageNet16-120, it is
  reported as a secondary finding consistent with CoLLM-NAS's difficulty-scaling
  and is **not** stated as a confirmatory result.

This substrate also closes the objection the manuscript itself concedes
([main.tex:757](paper/main.tex#L757)) and that reviewers drawing on Li &
Talwalkar and Yang et al. would press: the original search space was custom, not
tabular.

## 3.2 Arms

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

## 3.3 Conditional replicate — pre-registered now so it is not an unplanned analysis

After E1 reports, E2's **primary contrast set is re-run once** at the
configuration E1 identifies as least artifactual — defined in advance as the
cell, among those available to a locally-served model, with the highest
post-repair D. If that cell is the primary configuration itself, the replicate is
not run and that fact is reported. The replicate's arms, R, outcome, and tests
are identical to the primary; only the generator configuration differs. This
replicate is the sole test of **C5** and its result is confirmatory, inside the
declared family (§5.3).

## 3.4 Unit of analysis, estimand, inference

**Unit of analysis: THE RUN, not the architecture.**

One **run** = one search of *k* = 20 proposals, under one arm, at one seed, on
one task. Selection within a run uses **validation** accuracy only. The run's
outcome is the **test** accuracy of the architecture the run selected — test
accuracy never enters selection, which fixes OA-11.

**R = 20 independent runs per arm per task.**

**Primary estimand: mean ± standard deviation of the run outcome across the R
runs.** This is the standard the corpus actually supports. Verbatim, Lindauer &
Hutter: *"we recommend that, if possible in terms of compute budgets, all methods
should be repeated several times with different seeds and the authors should
report mean and standard deviation (or median and quartiles if the noise is not
symmetric) across the repetitions."* Verbatim, Yang et al.: *"Report mean and
standard deviation of the top-1 test accuracy… for both the randomly sampled and
the searched architectures."*

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

**Inference: permutation tests over runs.** Two-sided, exact where C(2R,R) is
tractable, otherwise 100,000 random permutations with a fixed seed recorded in
the results file. Runs are the exchangeable unit. This is the correct response to
OA-12 — the original applied Welch, Mann–Whitney and a bootstrap to *n*=20
proposals generated with serial dependence inside one growing context. Runs are
independent by construction; proposals within a run are not, and are never
treated as the unit.

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

## 3.5 Power / MDE and stopping rule

**Confirmatory contrasts in E2 (per §5.3): 4.**

| ID | Contrast |
|---|---|
| Y1 | uncurated vs zero-shot |
| Y2 | curated vs zero-shot |
| Y3 | external archive vs zero-shot |
| Y4 | uncurated vs curated |

**MDE at R=20 per arm, α = 0.003125, two-sided permutation test:** power ≥ 0.80
for |δ| ≥ 0.62, equivalently a location shift of ≈1.05 pooled SDs.

**This number is provisional and must be confirmed before data collection.**
`scripts/power_e2.py` runs the simulation at S3 against a pilot variance estimate
drawn from the benchmark's own best-of-20 distribution (obtainable by pure
table sampling, with no generation and no training). If the simulation shows R=20
insufficient for |δ| = 0.62 at 80% power, **R is raised before any run executes**
and the change is logged in `DEVIATIONS.md`. R is never raised after data
collection begins.

The MDE is stated in standardised units only. Translating it into accuracy points
requires the benchmark's best-of-20 variance, which is not verified in the corpus
as of this writing; that translation is produced at S3 by the same script and is
not asserted here.

**Stopping rule.** Fixed R = 20 per arm per task, decided now. **No interim
analyses. No extension on a near-miss. No adaptive stopping.** A run that crashes
is re-executed once at the same seed; if it crashes twice it is recorded as a
failure, the arm reports R_effective < 20, and the failure count appears in the
results file and in the manuscript's table footnote.

**Generation budget.** 4 arms × 20 runs × 20 proposals × 3 tasks = **4,800
generations**, plus the conditional replicate's 4 arms × 20 runs × 20 proposals ×
1 task = **1,600**, for **6,400**. Plus E1's 3,000. Total ≈ **9,400 generations,
zero training runs.**

---

# 4. Experiment E3 — the proxy size-confound replication (Case B)

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

`rho_acc_partial` is an addition beyond the brief and is the quantity that
actually answers the question C6 asks — how much of a proxy's apparent validity
survives removing size. A proxy whose `rho_acc` is high and whose
`rho_acc_partial` is near zero is measuring size.

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
| A2 | E1 | D per cell: mean ± std across 5 batches | descriptive |
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

**Confirmatory tests: X1–X4 across 3 models = 12, plus Y1–Y4 = 4.**

## 5.2 Multiplicity correction

- **Family:** the 16 confirmatory tests named in §5.1 — X1, X2, X3, X4 (each
  evaluated once per model: Qwen3-1.7B, Qwen3-8B, frontier) and Y1, Y2, Y3, Y4
  (each evaluated once, on the primary task only).
- **Procedure:** Bonferroni.
- **FAMILY_SIZE = 16.**
- **ALPHA = 0.05 / 16 = 0.003125.**

Holm–Bonferroni was considered and rejected. It is uniformly more powerful at the
same FWER, but it yields a step-down sequence rather than a single number, and
the defect this plan exists to prevent (OA-5: the manuscript declared 0.05/7
while the code applied 0.05/15) is a *number-matching* defect. A single stated
constant that a script can assert against is worth more here than the power.

**Enforcement, so OA-5 cannot recur.** The analysis emitter:
1. reads `FAMILY_SIZE = 16` and `ALPHA = 0.003125` from a single module-level
   constant, which is the same constant this document states;
2. writes `alpha_applied` onto **every** emitted statistic;
3. asserts that the count of emitted statistics with `confirmatory: true` is
   exactly 16 — and **aborts** otherwise;
4. asserts that every `alpha_applied` equals the top-level `alpha` — and
   **aborts** otherwise.

A3–A15 are descriptive or exploratory and carry no p-value.

X3 is undefined for the frontier model (no precision factor). Its slot in the
family is retained and emitted as `{"status": "not_applicable", "confirmatory":
true, "p": null}` so the count stays exactly 16 and the family size stated here
matches the family size the code enforces. This is deliberate: shrinking the
family after the fact is the failure mode being guarded against.

## 5.3 Confirmatory vs exploratory

E2's conditional replicate (§3.3) tests C5 through **A13**, which is descriptive
(arm ordering plus pairwise CIs), not a null-hypothesis test. C5 is therefore
evaluated by CI overlap and ordering, not by a p-value, and does not enter the
16-test family. This is stated now so that adding a test for it later would be a
visible deviation.

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

```json
{
  "schema_version": "1.0.0",
  "experiment": "E1",
  "plan_sha256": "<SHA-256 of EXPERIMENT_PLAN.md at freeze>",
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
  "seeds": [7001, 7002, 7003, 7004, 7005],
  "confirmatory_family_size": 16,
  "alpha": 0.003125,
  "cells": [
    {
      "cell_id": "",
      "factors": {"model": "", "format": "", "precision": "", "temperature": 0.0},
      "batches": [
        {"batch": 0, "seed": 7001, "n": 20,
         "parse_failures": 0,
         "D_pre": null, "D_post": null,
         "field_entropy_pre": {}, "field_entropy_post": {},
         "repair_channels": {"<field>": {"passthrough": 0, "coerced": 0, "filled": 0}}}
      ],
      "D_pre_mean": null, "D_pre_std": null,
      "D_post_mean": null, "D_post_std": null,
      "null_batches": 0,
      "label_pre": "", "label_post": "",
      "status": "ok"
    }
  ],
  "statistics": [
    {
      "id": "X2.qwen3-1.7b",
      "kind": "paired_permutation",
      "contrast": "schema_pre_repair vs schema_post_repair",
      "paired": true, "n_pairs": 5, "n_permutations": 0,
      "estimate": null, "ci95": [null, null],
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
                "winner": "", "verdict": ""}
  },
  "na_counts": {},
  "failures": []
}
```

`results/E2.json` and `results/E3.json` share `schema_version`, the header block,
`statistics[]`, `na_counts` and `failures`, and replace `cells[]` with `runs[]`
and `correlations[]` respectively. E3's entries additionally carry
`transcribed: true|false`, `source_table`, and `source_note_id`.

**Manuscript binding rule.** No numeric literal is typed into the `.tex`. Every
number resolves to a `results/<exp>.json` key through a lookup macro, and a
checker script verifies at build time that every numeric token in the manuscript
body has a resolvable key. This is the G5 criterion and it is stated here so the
results-file layer is designed before the data exists rather than after.

## 5.6 DEVIATIONS.md protocol

`DEVIATIONS.md` is created at the same commit as this plan, empty of entries.

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
   supersedes; the original file remains in the repository unmodified.
5. Every deviation entry is committed before the run it governs, so git history
   independently timestamps the ordering.

---

# 6. Citations the paper is obliged to carry

Sourced from `audit/references_verified.bib`, never from memory.

**Eight of the thirteen are not in that file.** They post-date the S0
bibliography audit, which verified the *manuscript's existing* 47 entries and did
not add new ones. Their metadata below is taken from vault notes — fetched source
records, not recall — with the note ID given so each is traceable. **They must be
added to `audit/references_verified.bib`, verified against an academic API, before
S6 writing.** That is logged as OA-37.

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

Rows 6–15 are ten works, not the brief's eight, because "the four
structured-decoding papers" resolve to four separate entries and ZiCo / ZiCo-BC
are two. Every one is load-bearing: rows 8–11 establish the mechanism this paper
applies (and therefore establish what it may *not* claim, §1.2); rows 12–14 are
E3's entire evidence base; row 15 is the only citable source in the corpus for
E2's estimand.

**Also obliged, though not on the brief's list**, because the plan leans on them
directly: **NAS-Bench-201** (Dong & Yang, `dong2020nasbench201`, in bib) as E2's
substrate, **NAS-Bench-101** (`ying2019nasbench101`, in bib) and the **NAS
1000-papers survey** (`white2023nas`, in bib) — the latter cited *only* for its
random-search-baseline point, never as an estimand recommendation (§3.4).

---

# 7. What this plan does not do

Recorded so the boundary is explicit and cannot be quietly crossed.

- **It does not recover the original data.** OA-1 is closed. Every ORPHAN finding
  in `audit/CLAIM_TRACE.md` is permanent. Nothing in E1–E3 re-establishes any
  number in the current manuscript.
- **It does not train anything.** E1 is generation and structural measurement.
  E2 is generation plus table lookup. E3 is table computation. Total training
  runs: zero.
- **It does not settle whether CoLLM-NAS's noise-accumulation ablation has been
  independently replicated.** Five candidate citing papers are unverified leads
  (OA-37/C6 thread in `audit/OPEN_ACTIONS.md`). None may be cited as
  corroboration until fetched and read.
- **It does not resolve the generating model of the original run.** OA-3 stands
  and is unresolvable; the manuscript will say the original generating model is
  unknowable and that E1–E3 use models recorded in metadata at generation time.
- **It does not test MAE-DET**, the DARTS-space parameter-range question L5 left
  open, or the GENIUS Appendix A.3 tables L1 sampled only partially (seam S3 —
  a full pass could still surface a trajectory where the final iteration nets
  worse than zero-shot, which would restore GENIUS as an independent second
  scoop; that pass is an S3 task).
