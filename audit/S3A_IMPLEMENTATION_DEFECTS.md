# S3a — IMPLEMENTATION DEFECT REPORT

**Session:** S3a, 2026-08-17. **Governing plan:** `EXPERIMENT_PLAN_R3.md`,
SHA-256 `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03`.
**G2 is deliberately unsigned.** Revision is still available; this document is the
input to revision 4.

Every item below was found by writing the measurement instrument against the plan
and running it — not by re-reading the plan. Nothing here amends the plan.
**Record only.**

Severity key:
- **BLOCKING** — the plan cannot be executed as written; an implementer must
  invent a rule, and two implementers would invent different ones.
- **MATERIAL** — executable, but the result would be wrong, unfalsifiable, or
  not defensible to a reviewer.
- **MINOR** — internal inconsistency with an obvious repair.

---

## D-01 — BLOCKING — `partial` is predicted in a CHANGE column but defined only for LEVELS

**§2.5, §2.6.** The `quantisation` row predicts `partial` in the **high temp**
column. That column is a **change** (ΔD). §2.6 defines exactly two change labels,
`no chg` and `recovers`; `partial` is a level label with no ΔD rule anywhere in
the plan.

One of five rivals therefore has an **unscoreable cell**. It can never match, so
`quantisation` is silently capped at 4 of 5 while every other rival can reach 5 —
which biases the "strictly highest score wins" rule against it.

*Decided to proceed:* scored as UNSCOREABLE and recorded.
*Revision 4 must:* either define a ΔD band for `partial`, or replace that cell.

---

## D-02 — BLOCKING — three rival pairs are separated by a single column, and one of them is the column most likely to be indeterminate

**§2.5 vs §2.6.** §2.5 asserts "all five signatures are pairwise distinct". That
holds in the raw label vocabulary. But **§2.6 states that `reduced` and `partial`
are the same numeric band.** Once folded — as the classifier must fold them,
because they are one band — the signatures become:

| Rival | free-prose | schema pre | post | bf16 | high temp |
|---|---|---|---|---|---|
| repair artifact | diverse | **diverse** | collapsed | no chg | no chg |
| format tax | **diverse** | **collapsed** | collapsed | no chg | no chg |
| quantisation | reduced | reduced | reduced | **recovers** | *(unscoreable)* |
| decoding | reduced | reduced | reduced | **no chg** | recovers |
| genuine prior | **collapsed** | collapsed | collapsed | no chg | no chg |

Three pairs now differ in exactly one column:

| Pair | Sole discriminator |
|---|---|
| repair artifact vs format tax | **schema pre-repair** |
| format tax vs genuine prior | **free-prose** |
| quantisation vs decoding | **bf16** (their high-temp cells cannot both be scored, per D-01) |

**The `format tax` / `genuine prior` case is the serious one.** Those are the two
rivals that decide **C2**, the claim that carries half the thesis (§1.4: the
thesis is asserted only if C2 ∧ C5). Their sole discriminator is the free-prose
column — **the one column §2.6 itself singles out as most likely to be declared
`indeterminate`**, because free-prose is the condition most likely to fail
parsing. If the free-prose parse rate lands below 50%, the plan's own rule
suppresses the only cell that separates "the apparatus did it" from "the model
did it", and C2 becomes undecidable.

*Decided to proceed:* recorded; no code workaround exists.
*Revision 4 must:* add a discriminating cell for these pairs that does not depend
on free-prose parsing, or accept in advance and in writing that C2 is conditional
on the free-prose parse rate clearing 50%.

---

## D-03 — BLOCKING — the 0.10–0.25·D_rand band has no label, and negative change has no label

**§2.6.** A ΔD of, say, 0.15·D_rand is neither `no chg` (|ΔD| < 0.10) nor
`recovers` (ΔD ≥ 0.25). The plan names no label for the gap, and gives no rule for
how an unnamed observation scores against a rival that predicted a named one.
Likewise a large **negative** ΔD — further collapse — has no label: `recovers` is
defined only for positive change.

*Decided to proceed:* the classifier returns `other`, which matches no rival and
scores 0 for that column against all five.
*Revision 4 must:* name the middle band and the negative direction, and state
whether an `other` observation scores as a mismatch or as indeterminate. The two
choices give different winners.

---

## D-04 — BLOCKING — the frontier model's columns are defined at a precision it does not have

**§2.5 column definitions vs §2.2.** Every one of the five columns is defined at
a specific coordinate that includes **NF4**. §2.2 states the frontier model has no
precision factor and records `precision: "provider_default (unknown)"`. §2.2 also
says the frontier "contributes to the format, repair and temperature columns" —
but the plan never states the substitution rule that lets a `provider_default`
cell stand in for the NF4 coordinate a column names.

C3 is evaluated on the frontier model, so this is not a corner case.

*Decided to proceed:* would have to assume `provider_default` substitutes for NF4.
*Revision 4 must:* state the substitution explicitly, or redefine the columns
model-relatively.

---

## D-05 — MATERIAL — the scored free-prose column and the caveated free-prose quantity are different stages

**§2.5 vs §2.6.** The prediction table defines the free-prose column as
`D at (free-prose, post-repair, NF4, T=0.7)` — **post**-repair. But §2.6's
reliability rule, and the whole format-tax-vs-genuine-prior argument, are written
about free-prose **pre**-repair diversity, as is §2.4.6's justification for S.

So the parse-rate caveat governs a quantity the scorer never reads.

*Decided to proceed:* scored the column as literally defined (post-repair).
*Revision 4 must:* make the two agree.

---

## D-06 — BLOCKING — the indeterminate rescaling rule covers exactly one indeterminate column

**§2.6.** The rule reads: free-prose parse rate < 50% → that column is
`indeterminate`, "the maximum achievable signature score drop[s] to 4 and the
≥4-of-5 rule read[s] ≥3-of-4."

But **two independent mechanisms** produce `indeterminate` cells — the parse-rate
rule and the bootstrap boundary-straddle rule (§2.6, added at revision 2). Two or
more indeterminate columns are therefore reachable, and the plan gives no rule for
that case. With D-01 in play, `quantisation` starts one cell down before any data
arrives.

*Decided to proceed:* no general rule implemented; the scorer refuses rather than
guesses.
*Revision 4 must:* state the rule as a function of the scoreable-column count.

---

## D-07 — MATERIAL — ΔD is never defined as a difference of which quantity

**§2.5, §2.6, §2.4.5.** The change columns are "the change in D from cell X to
cell Y". Two quantities are called D:

- `D_mean` — the mean of the within-batch D values. §2.6 says thresholds apply to
  this.
- `D_cell_pooled` — the mean over all C(N,2) generation pairs. §2.4.5 says the
  bootstrap on ΔD targets this.

So the **point estimate** being classified and the **interval** that can force it
to `indeterminate` are computed on different estimands. Measured gap on random
draws (`tests/compute_d_rand.py`): 0.002597 absolute, against a no-change band of
0.077193 — small here, but random draws are the maximum-agreement case.

*Decided to proceed:* used the difference of `D_mean` for classification.
*Revision 4 must:* name one quantity for both.

---

## D-08 — MATERIAL — `D_rand` is not in the results file whose labels depend on it

**§2.6 vs §5.5.** Every `label_pre` / `label_post` in `results/E1.json` is a
function of `D_rand`, which lives in a separate `results/E1_reference.json`. The
E1 schema has no field for it. A results file therefore asserts labels without
carrying the reference that produced them, which is exactly the provenance
failure the results-file layer exists to prevent (G5).

*Decided to proceed:* emitted the reference to its own file.
*Revision 4 must:* add `d_rand` and its provenance to the E1 header block.

---

## D-09 — MATERIAL — the plan calls the repository sampler "uniform"; it is not, in two ways

**§2.6.** The text says "the repository's own **uniform** random sampler" and
gives the analytic anchor "≈0.74 (mean over the six fields of 1 − Σp² **under
uniform sampling**)". Reading `src/search_space.py:192-224`, neither holds:

1. **`pooling` is not sampled from its 4-value vocabulary.** Block pooling is
   decided by a two-stage draw (`num_pools = rng.randint(1, min(num_blocks,4))`,
   then `rng.sample` of positions); blocks off the list are forced to `"none"`
   and blocks on it draw uniformly from **three** values only. Measured over 320
   draws: `none` **48.21%**, `strided_conv` 17.68%, `avgpool` 17.47%, `maxpool`
   16.64% — against 25% under uniformity.
2. **`num_blocks` varies over {3,4,5,6}**, so pairs of architectures have
   different block counts and pick up the `6·|Bx−By|` term with a `6·max(Bx,By)`
   denominator. The 0.74 anchor was derived for a **fixed** block count.

The two errors push in opposite directions and partly cancel, which is why the
sanity range still passes — see D-10.

*Decided to proceed:* used the repository's sampler verbatim (D-11) and reported
the measurement rather than the anchor.
*Revision 4 must:* drop the word "uniform", or re-derive the anchor from the
sampler's actual distribution.

---

## D-10 — MATERIAL — the D_rand sanity range passes for the wrong reason

**§2.6** halts E1 if D_rand falls outside [0.65, 0.80], anchored on ≈0.74.
Measured (seed 20260817):

| Form | Value | In range |
|---|---|---|
| Plan literal, pooled over C(200,2) | **0.773357** | yes |
| E1 batch structure, mean of 16 batch Ds | **0.771931** | yes |
| E1 batch structure, pooled over C(320,2) | 0.769334 | yes |
| Fixed-block-count subsets | 0.6984 – 0.7162 | yes |

Every form passes, but **none is ≈0.74**, and the spread across forms (0.698 to
0.773) is over half the width of the entire acceptance window. The gate is wide
enough that it would not have caught the D-09 non-uniformity. A gate that passes
whatever it is given is not a gate.

*Decided to proceed:* recorded both forms; used the batch-mean form for
thresholds, per §2.6's statement that thresholds apply to `D_mean`.
*Revision 4 must:* tighten the range around the measured value, or state that the
range is a sanity check on gross sampler failure only and not a validation.

---

## D-11 — BLOCKING (worked around) — the sampler §2.6 names cannot be imported without an ML dependency

**§2.6 vs `src/search_space.py:7`.** The module imports `torch` at top level.
S3a forbids installing ML dependencies, and torch is absent. So "compute D_rand
from the repository's own sampler" is not executable as written.

*Decided to proceed:* rather than reimplement the sampler — which would silently
substitute a different distribution for the one the plan names — `src/emit/
sampler.py` extracts the **verbatim source text** of `SEARCH_SPACE` and
`random_architecture_config` via `ast` and executes those two nodes in a namespace
containing only `random`. The extracted bytes are hashed into
`results/E1_reference.json`:

- `search_space.py` whole-file SHA-256 `c656cedf8ff8f543805c6351e6989555036a43519cb4ec81475b0f11499c4914`
- extracted-nodes SHA-256 `d8e551f56766c74314caf3ca7a85e4fdb36b5c08282575865f983977270fef4e`

*Revision 4 should:* record that D_rand is computed by source extraction, or
split the sampler into a torch-free module.

---

## D-12 — MINOR — no seed is registered for the D_rand draw

**§2.6** specifies the count (200) and the sampler, but no seed — so D_rand is not
reproducible from the plan alone.

*Decided:* registered `D_RAND_SEED = 20260817` in `src/emit/constants.py` and
written into `results/E1_reference.json`.

---

## D-13 — MINOR — §2.6 says 200 architectures; the E1 batch structure needs 16 × 20

**§2.6** says "200 architectures". The thresholds are applied to `D_mean`, a
**batch-mean** quantity over 16 batches of 20. A single pooled draw of 200 has no
batch structure and cannot produce the across-batch reference the paired tests
need. Both were computed; they differ by 0.0014.

*Revision 4 should:* specify the batch structure for the reference draw, so the
reference and the thing it anchors are the same shape.

---

## D-14 — MATERIAL — `permutation_mode: "exact"` in §5.5's example is not a value §5.2 recognises

**§5.5 vs §5.2.** The worked `statistics[]` entry in §5.5 carries
`"permutation_mode": "exact"`. §5.2's floor computation enumerates
`paired exact`, `unpaired exact`, `Monte-Carlo`, `not_applicable`. `"exact"` is
ambiguous between the first two, which have different floors.

Found by the emitter aborting on the plan's own example. That is the correct
behaviour — but it means **the plan's own schema example would not pass its own
gate.**

*Decided to proceed:* used `paired_exact`.
*Revision 4 must:* fix the example to the enum.

---

## D-15 — MATERIAL — the plan's literal `not_applicable` slot trips its own G-alpha gate

**§5.2.** The slot is specified as
`{"status": "not_applicable", "confirmatory": true, "p": null}` — with no
`alpha_applied`. But the same section requires the emitter to assert that
**every** `alpha_applied` equals the top-level alpha. Verified: the literal slot
raises `[G-alpha] statistic 'X3.frontier' carries no alpha_applied`.

*Decided to proceed:* `not_applicable_slot()` stamps `alpha_applied`.
*Revision 4 must:* either add the field to the specimen or exempt NA slots from
G-alpha in the text.

---

## D-16 — MATERIAL — E2's "exact where tractable" resolves to Monte Carlo, but §3.5 quotes the exact floor

**§3.4 vs §3.5.** §3.4 says "exact where C(2R,R) is tractable, otherwise 100,000
random permutations". At the floor R = 20, **C(40,20) = 137,846,528,820** — not
enumerable. So E2 runs by Monte Carlo, whose floor is
**1/(1+100,000) = 9.99990 × 10⁻⁶**. §3.5 nonetheless quotes the exact floor,
**1.45 × 10⁻¹¹**, as E2's floor.

Both clear ALPHA, so gate 2 passes either way and no result changes. But the plan
states a number that will not be the one emitted, and "tractable" is never
defined, so two implementers would not agree on which mode runs.

*Revision 4 must:* define "tractable" numerically and quote the floor of the mode
that will actually run.

---

## D-17 — BLOCKING — E2's permutation test statistic is never named

**§3.4.** "Permutation tests over runs. Two-sided… Runs are the exchangeable
unit." The plan never says **what is permuted into what statistic**. A permutation
test on the difference of means, on the difference of medians, and on the rank sum
give different p-values on identical data. The effect size is Cliff's δ, which
hints at a rank-based test, but the plan does not say so.

*Decided to proceed:* implemented the difference of means (`src/emit/stats.py`).
*Revision 4 must:* name the statistic.

---

## D-18 — MATERIAL — Cliff's δ tie convention is unstated, and E2's substrate produces heavy ties

**§3.4.** NAS-Bench-201 is a table lookup over 15,625 architectures; many runs
will select the **same** architecture and report **identical** test accuracy. Ties
are not an edge case here, they are the expected case.

δ = (#{a>b} − #{a<b})/(n₁n₂) is standard, but whether ties contribute 0.5 each to
the Mann–Whitney *U* that §5.5 persists determines whether δ is recoverable from
*U* at all. The plan requires `u_stat` to be persisted "so δ is recoverable"
(fixing OA-9) but never fixes the convention that makes that true.

*Decided:* ties contribute 0 to δ's numerator and 0.5 each to *U*, which makes
δ = 2U/(n₁n₂) − 1 hold exactly. Verified on a fully-tied fixture: δ = 0.0,
U = 200.0, 2U/400 − 1 = 0.0.
*Revision 4 must:* state the convention.

---

## D-19 — MATERIAL — BCa on Cliff's δ needs a jackknife the plan does not specify

**§3.4, §2.4.5.** BCa requires an acceleration estimate from a jackknife. For a
**two-sample** statistic, the plan does not say whether to jackknife the first
sample, the second, or both pooled. The three give different intervals.

*Revision 4 must:* specify, or drop to a percentile bootstrap.

---

## D-20 — MATERIAL — run-outcome tie-breaking is unspecified, and the substrate guarantees ties

**§3.4.** "Selection within a run uses validation accuracy only. The run's outcome
is the test accuracy of the architecture the run selected." NAS-Bench-201 contains
architectures with identical validation accuracy. When two proposals in a run tie
on validation, which one is selected — first proposed, last, lowest index? The
choice changes the reported test accuracy and is fully deterministic, so it is not
noise that averages out.

*Revision 4 must:* state the tie-break.

---

## D-21 — MATERIAL — seven of twelve inspected quantities cannot be replayed from the results file

**§5.5.** Block D built a fixture using the schema exactly as specified and tried
to recompute every statistic from the record's own stored inputs.

| Quantity | Replayable | Why |
|---|---|---|
| `cells[].D_*_mean` / `_std` | **yes** | from `batches[].D_*`, bit-exact |
| `statistics[].p` / `estimate` | **yes*** | *only because the free-text `contrast` happened to parse as two `cell_id`s |
| `statistics[].effect.cliffs_delta` / `u_stat` | **yes** | bit-exact from the same operands |
| `cells[].batches[].repair_channels` | **yes** | the counts are the primitive |
| `discreteness_gate` | **yes** | floors recompute from `n_planned` |
| which stage a contrast used | **no** | no field identifies `D_pre` vs `D_post` |
| `cells[].D_*_pooled` | **no** | needs per-generation design vectors; none are stored |
| `cells[].D_*_pooled_ci95` | **no** | BCa resamples generations; unreconstructable even given `bootstrap_seed` |
| `cells[].S_*` and `batches[].S` | **no** | S is computed on raw generated text; no text is stored anywhere |
| `batches[].field_entropy_*` | **no** | pools field values across every block of every generation |
| E2 `runs[]` → Y1–Y4 | **no** | §5.5 names `runs[]` but never specifies its fields |

**The structural problem:** the schema records **batch-level aggregates**, while
`D_pooled`, `S`, the entropies and every bootstrap interval are defined at the
**generation level**. No generation-level record exists, so those quantities can
be asserted but never checked. The manuscript binding rule (§5.5) guarantees every
number traces to a results-file key; it does not guarantee the key traces to
anything.

*Revision 4 must:* either add a generation-level record (design vector, raw text
hash, parse status per generation), or state explicitly that the pooled/S/entropy
/bootstrap family is unreplayable and drop the claim that the results file is a
provenance record for them.

---

## D-22 — MINOR — the `B` collision is real and now sits inside adjacent formulas

**§2.3 vs §2.4.1/§2.4.2.** `B` is the paired **batch** count in §2.3's ceiling
arithmetic (`2/2^B`) and the **block** count in §2.4.2's distance formula
(`6·|Bx−By|`, `6·max(Bx,By)`). Revision 3 added a parenthetical noting the
collision. In implementation the two appear within a few lines of each other and
the note is not sufficient: `n_pairs` and `n_blocks` were used throughout the code
instead.

*Revision 4 should:* rename one of them in the text.

---

## D-23 — MINOR — `min_attainable_p` is named three ways

**§2.7 and §5.2 prose** say the emitter "emits `min_attainable_p`". **§5.5's
schema** has `min_attainable_p_planned` and `min_attainable_p_realised`. **§5.2's
gate record** has `per_test[].min_attainable_p`. All three coexist; a checker
script looking for one name will miss the others.

---

## D-24 — MINOR — `n_blocks` is in the design-choice vector but not in *G*

**§2.4.1 vs §2.4.2.** §2.4.1 lists the architecture-level members as
"`n_blocks` = B, `global_pool`, `fc_layers`". §2.4.2's *G* is
`{global_pool, fc_layers}` and `|G|` = 2, with block-count difference handled by
the separate `6·|Bx−By|` term. Consistent once understood, but the vector
definition and the distance formula list different members and an implementer must
notice that `n_blocks` is deliberately excluded from *G* to avoid double-counting.

---

## D-25 — MATERIAL — the plan writes `D_rand` to a path the repository gitignores

**§2.6 vs `.gitignore:13`.** §2.6 directs that D_rand "is computed at S3 *before
any generation runs*, and written to `results/E1_reference.json`". `.gitignore`
line 13 excludes `results/`. So the reference value that **every classification
threshold in E1 is a fraction of** would be written to an untracked path and would
never enter version control — compounding D-08, which already notes it is absent
from the results file whose labels depend on it.

The same applies to `results/E1.json`, `results/E2.json` and `results/E3.json`:
the entire results-file layer the manuscript binding rule (§5.5, G5) depends on is
gitignored.

*Decided to proceed:* wrote a tracked copy to `audit/E1_reference_S3a.json`,
flagged in the file itself. `.gitignore` was **not** modified — that is an
operator decision, and S0 recorded `.gitignore` as append-only.
*Revision 4 must:* resolve whether the results layer is tracked. If it is not,
the G5 criterion ("re-running the analysis reproduces every table and figure")
cannot be checked by anyone who clones the repository.

---

## Summary

| Severity | Count | IDs |
|---|---|---|
| **BLOCKING** | 7 | D-01, D-02, D-03, D-04, D-06, D-11, D-17 |
| **MATERIAL** | 13 | D-05, D-07, D-08, D-09, D-10, D-14, D-15, D-16, D-18, D-19, D-20, D-21, D-25 |
| **MINOR** | 5 | D-12, D-13, D-22, D-23, D-24 |

**D-11 is worked around and does not block.** The remaining six BLOCKING items
are concentrated in one place: **the signature-matching machinery of §2.5/§2.6 —
the mechanism that decides C2, and therefore half the thesis — is not
executable as written.** The gates, the metrics and the emitter all are.
