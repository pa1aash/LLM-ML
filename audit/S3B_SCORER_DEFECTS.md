# S3B — SCORER DEFECT REPORT

**Session:** S3b, 2026-08-18. **Governing plan:** `EXPERIMENT_PLAN_R4.md`,
SHA-256 `738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d`.
**The plan was NOT amended this session.** G2 remains unsigned. Revision 5 folds
these in together with the four operator decisions recorded at the end.

Found by implementing the two scorers that decide **C2** — the anchor-tracking
scorer (§2.4.7, §2.8) and the generalised signature scorer (§2.5, §2.6) — and
running them against 22 synthetic fixture assertions. All data was constructed by
hand; no model was called.

Severity: **BLOCKING** — an implementer must invent a rule and two implementers
would invent different ones. **MATERIAL** — executable, but the result would be
wrong or not defensible. **MINOR** — inconsistency with an obvious repair.

---

## S3B-01 — BLOCKING — nothing defines when a FIELD is "collapsed"

**§2.4.7 / §2.4.4 / §2.6.** §2.4.7 opens *"For each field f whose distribution in
a cell is classified **collapsed**…"*. But §2.6's `collapsed` label is defined for
**D**, a batch-level diversity, against `0.15·D_rand`. §2.4.4 supplies a
**normalised per-field entropy** and **no threshold at all**. There is no rule
anywhere in the plan that classifies a *field* as collapsed.

This is the denominator of both tracking quantities. Without it, `tracks_first`
and `tracks_exemplar` are undefined.

*Decided to proceed:* a field is collapsed when its normalised entropy < **0.15**,
mirroring `D < 0.15·D_rand`. The mirror is exact in one respect — both quantities
are normalised so that **1.0 is the uniform reference** — so the same fraction
means the same thing on both scales.
*Revision 5 must:* register the threshold, or define field collapse some other way
and say so.

---

## S3B-02 — BLOCKING — the exemplar has no value for half the fields

**§2.8.** The exemplar is specified as *"modal — one worked example using
`standard_3x3` / `relu` / `batchnorm`"* versus *"non-modal —
`depthwise_separable` / `gelu` / `groupnorm`"*. That is **three** of the six
per-block fields. `channels`, `skip_connection` and `pooling` have no exemplar
value, so `tracks_exemplar(f)` is undefined for them — yet §2.4.7 defines the
quantity over "the fields collapsed in that batch", which can include all six.

*Decided to proceed:* `tracks_exemplar` is computed over the three fields the
exemplar names, with **its own denominator**, reported separately from
`tracks_first` (which uses all collapsed fields). Both are emitted; they are never
merged.
*Revision 5 must:* either give the exemplar a value for all six fields, or state
that `tracks_exemplar` is a three-field statistic and register its denominator.

---

## S3B-03 — MATERIAL — the bootstrap unit for a proportion-over-fields is unregistered

**§2.4.7 vs §2.4.5.** §2.4.7 says the proportions are reported "with BCa 95%
intervals **under §2.4.5's parameters**". §2.4.5's registered resampling unit is
the **generation**. But `tracks_first` is a proportion over **fields** within a
batch, aggregated over batches; generations are not its sampling unit at all.

*Decided to proceed:* resample **batches** — the 16 batch-level proportions —
which is the unit the statistic is actually replicated over.
*Revision 5 must:* register the unit explicitly for this statistic.

---

## S3B-04 — MINOR — the `tracks` / `no tracking` boundary is open

**§2.6.** `tracks` is "lower bound **exceeds** 0.50", `no tracking` is "upper
bound **below** 0.50", `indeterminate` is "the interval **spans** 0.50". An
interval whose endpoint sits **exactly on** 0.50 satisfies none of the three as
written.

*Decided:* an endpoint exactly on the bar does not exclude it, so the case falls
to `indeterminate`.

---

## S3B-05 — BLOCKING — the tracking column's predictions are prose patterns, not labels

**§2.5 vs §2.6.** §2.6 defines a label for **one proportion**. §2.5's tracking
cells are **patterns across two stages and two quantities**:

- repair artifact — *"post-repair modal tracks first-enumerated; pre-repair does not"*
- format tax — *"pre-repair modal tracks first-enumerated **and/or** exemplar"*
- the other three — *"no tracking"* / *"no tracking under any permutation"*

The observation is a **2×2 grid** (pre/post × first/exemplar); the label
vocabulary describes a scalar. Nothing in the plan says how a grid matches a prose
row, nor which grid entries each row reads.

*Decided to proceed:* each rival's row is encoded as an explicit **predicate over
the grid**, and a predicate is `indeterminate` only if a quantity **it reads** is
indeterminate — quantities it does not read cannot make it so. `and/or` is read as
inclusive-or, so `format tax` matches if either pre-repair quantity tracks.
*Revision 5 must:* write the predicates into the plan. This is the single largest
piece of interpretation the implementer had to supply.

---

## S3B-06 — MATERIAL — the `recovers` demotion assigns a label outside its own band

**§2.6.** `partial` (change) is defined as `+0.10·D_rand ≤ ΔD < +0.25·D_rand`.
`recovers` is `ΔD ≥ +0.25·D_rand` **and** the destination is not `collapsed`. The
next sentence says a change meeting the `recovers` bound whose destination **is**
collapsed "is **demoted to `partial`**" — assigning `partial` to a ΔD that is by
construction **outside** `partial`'s numeric band.

*Decided to proceed:* the demotion wins over the band. Verified in fixture C11b:
ΔD = 0.215761 ≥ 0.179801 with a collapsed destination returns `partial`.
*Revision 5 must:* either widen `partial`'s definition to "the band, **or** a
`recovers`-magnitude change into a collapsed destination", or name the demoted
case something else.

---

## S3B-07 — MATERIAL — indeterminacy cannot add a matched cell, but it CAN create a winner

**§2.6.** The plan states the boundary-straddle rule "can only reduce the number
of matched cells; it can never create a match". That is true of **cells** and
false of **verdicts**, because the winning threshold is `ceil(0.75·n_s)` and
removing a column lowers `n_s`.

**Demonstrated (fixture C14b).** A `format tax` observation failing **both** change
columns scores **4 of 6** against a threshold of **5** → no winner. Make one of
the columns it already failed indeterminate: **4 of 5** against a threshold of
**4** → `format tax` wins. The score did not rise; the bar fell.

*Decided:* implemented as the plan specifies, and the fixture is retained as
permanent evidence.
*Revision 5 must:* state this explicitly, and decide whether it is acceptable. A
verdict that appears **because a measurement became unreliable** is a hazard the
plan does not currently acknowledge.

---

## S3B-08 — RESOLVED BY IMPLEMENTATION — the threshold boundary is deterministic

**§2.6.** All level bands use strict `<`, so a value exactly on a boundary falls
in the **upper** band with no tie-break needed. Verified at the bit level
(fixture C13): `D = 0.15·D_rand = 0.10788075` classifies `reduced`; one ULP below
classifies `collapsed`. No defect. Recorded because the brief asked for the rule
to be stated and proved deterministic.

---

## S3B-09 — MATERIAL — "no rival matched" is unreachable in the ordinary case

**§2.6** registers "no rival matches" as a permitted, reportable outcome. It is
**not reachable** while the two columns that decide it are scoreable.

Across the three level columns the labels `{collapsed, reduced, diverse}` partition
the space, and per column:

| Column | Labels matching **no** rival |
|---|---|
| free_prose | **none** — all three are predicted by some rival |
| schema_pre_repair | **none** — all three are predicted |
| post_repair | `diverse` |
| bf16 | `partial`, `worsens` |
| high_temp | `worsens` |

So `free_prose` and `schema_pre_repair` **always** match at least one rival, and
`best == 0` is impossible unless both are `indeterminate`. Verified (fixture C6):
the most hostile observation available still scores **3** for `repair artifact`.
Fixture C6b constructs the only corner where the branch fires — both level columns
indeterminate, `post_repair = diverse`, both changes `worsens`, and a tracking grid
failing all five — giving `n_s = 4` and every score 0.

*Revision 5 should:* note that the outcome exists for a narrow corner, or add a
"no rival exceeds chance" criterion that can fire in the ordinary case.

---

## S3B-10 — MATERIAL — the flat 0.50 bar is biased toward the non-instrument rivals

**§2.6.** The bar is registered at 0.50 with the note that it is "a coin-flip
reference, not a chance-rate reference". Chance is **0.2639** (the
vocabulary-weighted mean of 1/|V_f| over the six fields; 0.25 over the three
exemplar fields). Measured across a sweep at *n* = 16 batches:

| true rate | 95% CI | flat 0.50 | per-field (symmetric) | one-sided at chance |
|---:|---|---|---|---|
| 0.10 | [0.000, 0.313] | no tracking | indeterminate | no tracking |
| 0.20 | [0.000, 0.375] | no tracking | indeterminate | no tracking |
| 0.25 | [0.063, 0.438] | no tracking | indeterminate | no tracking |
| 0.30 | [0.063, 0.500] | indeterminate | indeterminate | no tracking |
| 0.40 | [0.125, 0.563] | indeterminate | indeterminate | no tracking |
| 0.50 | [0.188, 0.688] | indeterminate | indeterminate | no tracking |
| **0.60** | [0.313, 0.750] | **indeterminate** | **tracks** | **tracks** |
| **0.75** | [0.438, 0.875] | **indeterminate** | **tracks** | **tracks** |
| 0.90 | [0.563, 0.938] | tracks | tracks | tracks |

**10 of 11 sampled rates give different verdicts across the three rules.**

The flat bar declares `indeterminate` at true rates of 0.60 and 0.75 — **2.3× and
2.8× chance**, unambiguous tracking — and it is eager to declare `no tracking`.
Both errors point the same way: `tracks` is predicted only by `repair artifact`
and `format tax`; `no tracking` is predicted by the other three. **The flat bar is
therefore systematically biased against the two instrument rivals and toward
`genuine prior`.** For a paper whose thesis is that the apparatus is responsible,
that bias is conservative — but it means the column may routinely fail to do the
job it was added for.

---

## S3B-11 — BLOCKING — the per-field rule as briefed makes three rivals unmatchable

**Proposed operator decision 3** replaces the flat bar with per-field chance
rates. Implemented **symmetrically** — `tracks` if lo > chance, `no tracking` if
hi < chance — it produces the middle column above: **`no tracking` never fires at
any sampled rate**, because asserting it would require the observed rate to sit
measurably **below** chance, which nothing predicts. Under that rule
`quantisation`, `decoding` and `genuine prior` can essentially **never match** the
tracking column.

*Decided to proceed:* a third rule is implemented and reported alongside —
**one-sided at chance**, where the substantive null *is* chance:

- `tracks` — the interval excludes chance from **above** (lo > chance)
- `no tracking` — the interval **contains** chance, or lies below it
- `indeterminate` — reserved for **insufficient data** (too few collapsed fields,
  too many null batches), decided upstream rather than by interval width

This is the only one of the three rules under which both `tracks` and `no
tracking` are reachable at plausible rates (right-hand column above).

*Revision 5 must:* adopt the **one-sided** form, not the symmetric one. Decision 3
as written would otherwise break the column in the opposite direction from the
flat bar.

---

## S3B-12 — BLOCKING — the PRE-repair tracking aggregate has no registered field

**§5.5 (Block D, forward check).** The cell schema registers
`tracks_first_post_mean`, `tracks_first_post_ci95`, `tracks_exemplar_post_mean`
and `tracks_exemplar_post_ci95` — **post-repair only**. But **both** the
`repair artifact` and `format tax` rows hinge on the **pre-repair** value:

- repair artifact — "post-repair tracks; **pre-repair does not**"
- format tax — "**pre-repair** tracks first-enumerated and/or exemplar"

Only the per-**batch** pre value (`batches[].tracks_first_pre`) exists. The cell
aggregate and its interval — which is what the label is computed from — have no
field. **The two rivals the column exists to separate cannot both be scored from
the registered schema.**

*Revision 5 must:* add `tracks_{first,exemplar}_pre_mean` and `_ci95`.

---

## S3B-13 — MATERIAL — one `label_tracking` field for a 2×2 grid

**§5.5.** The cell carries a single `label_tracking` string. The column's
observation is four labels (pre/post × first/exemplar). One string cannot carry
the pattern the rivals predict, so the scorer's input cannot be reconstructed from
the results file.

*Revision 5 must:* replace it with the grid, or with four labelled fields.

---

## S3B-14 — MATERIAL — modal values and the exemplar value map are not emitted

**§5.5 (reverse check).** The scorer needs `modal(f)` per field per stage and the
exemplar's value per field. Neither is a registered field. `modal(f)` is derivable
from `generations[].spec_{pre,post}_repair`, so it is *recoverable* — but a reader
cannot check a tracking indicator without recomputing it from raw specs, and the
exemplar's value map exists only in §2.8's prose.

*Revision 5 should:* emit `modal_value` per (field, stage, batch) and an
`exemplar_values` map in the header.

---

## S3B-15 — MINOR — ΔD has no registered field

**§5.5 (forward check).** The two change columns are differences of `D_mean`
between two cells. No field holds the difference; it is derived at analysis time.
Recoverable, but the number the label is computed from is not itself in the file.

---

## S3B-16 — MINOR — §2.6's tracking prose contradicts its own threshold

**§2.6.** `tracks` is glossed as "…with the interval **excluding chance**" while
the rule stated in the same row uses **0.50**, and the note below concedes chance
is 0.25. The prose describes the rule S3B-11 proposes; the rule implemented is the
flat bar.

---

## S3B-17 — MATERIAL — confirmed: the tracking column exists at one model only

**§2.8.** The sub-design is at the anchor configuration only, but the signature
match is reported **per model** (§5.1 A7, 5 rivals × 3 models). For Qwen3-8B and
the frontier model the tracking column is unavailable, so `n_s = 5` automatically
and `format tax` vs `genuine prior` reverts to depending on free-prose there.
**C2 is decidable at the anchor and no better than revision 3 elsewhere.**

Flagged in the S2c report; **operator decision 1 addresses it** by extending the
sub-design to all three models. Recorded here as confirmed by implementation.

---

## S3B-18 — MATERIAL — the tracking column is power-limited at 16 batches

At *n* = 16 the BCa interval on a proportion is roughly ±0.25 at mid-range (see
the sweep in S3B-10). Under the registered flat bar the column returns
`indeterminate` for true rates from 0.30 to 0.75 — **most of the plausible
range**. An `indeterminate` tracking column drops `n_s` to 5, and if free-prose is
also indeterminate, to 4 — at which point `format tax` and `genuine prior` are
separated **only** by `schema_pre_repair`, which is exactly the single-column
fragility revision 4 was written to remove.

*Revision 5 must:* either adopt the one-sided rule (S3B-11), which is determinate
across the whole sweep, or raise the batch count for the anchor cells, or both.
Note that operator decision 1 (three models) multiplies cells but **does not**
increase *n* per cell, so it does not fix this on its own.

---

## Summary

| Severity | Count | IDs |
|---|---|---|
| **BLOCKING** | 5 | S3B-01, S3B-02, S3B-05, S3B-11, S3B-12 |
| **MATERIAL** | 9 | S3B-03, S3B-06, S3B-07, S3B-09, S3B-10, S3B-13, S3B-14, S3B-17, S3B-18 |
| **MINOR** | 3 | S3B-04, S3B-15, S3B-16 |
| Resolved by implementation | 1 | S3B-08 |

**Both scorers work.** 22 of 22 fixture assertions pass, including C15 — the case
the sixth column exists for: with free-prose forced `indeterminate`,
`repair artifact` and `format tax` still separate, on the tracking column plus
`schema_pre_repair`.

**But the plan as written does not fully specify either scorer.** Five blocking
gaps had to be filled by the implementer, and two of them — the pre-repair
aggregate having no field (S3B-12), and the symmetric per-field rule making three
rivals unmatchable (S3B-11) — sit directly on the path C2 depends on.

---

## Operator decisions recorded for revision 5

Taken by the operator, **not implemented this session**.

1. **Anchor-tracking extends to all three models**, not just the anchor. X5 × 3 by
   symmetry with X1–X4. **FAMILY_SIZE 17 → 19, ALPHA = 0.05/19 =
   0.0026315789473684210.** Cost: 8 more cells, 2,560 generations, ~1,280 frontier
   calls. **Revision 5 must re-run every floor at the new alpha and STOP if any
   fails to clear.** Note S3B-18: this multiplies cells without raising *n* per
   cell, so it does not by itself fix the power problem.
2. **Per-field reversal is DECLINED.** Attribution stays at the aggregate level;
   the `passthrough` / `coerced` / `filled` decomposition supplies the per-field
   evidence on the repair side. **The limit is recorded:** if tracking is found,
   the experiment shows the harness drives *something*, not *which field*.
3. **Per-field chance-rate thresholds replace the flat 0.50 bar.** See S3B-11 —
   the **one-sided** form must be adopted; the symmetric form breaks three rivals.
4. **Every rival gets a prediction on BOTH `tracks_first` and `tracks_exemplar`.**
   This also resolves part of S3B-05, since the predicates then read a fully
   specified grid rather than an `and/or` prose clause.
