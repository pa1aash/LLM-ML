# STATE

**Project:** an instrumentation-artifact study of LLM-guided neural architecture
search. *(The manuscript's former title — "When Does Feedback Help? A Controlled
Study of LLM-Guided Neural Architecture Design" — no longer describes the paper;
its thesis was refuted at S1 and its claims abandoned at S2.)*
**Target:** AI for Meta-Science (NeurIPS 2026), position track, 8pp — see
`VENUE.md`. Fallback: AI for Science: Verification, Track B.
**Ladder:** S0 ground truth → S1 position → S2 claim surgery → S3 preflight →
S4 build → S5 results-file layer → S6 write → S7 referee

---

## Current stage: **S2d complete at revision 5 — G2 evidence filled, unsigned**

S0 audit complete (G0 unsigned). S1 positioning complete (G1 PASSED on operator
authorisation, unsigned). S2 produced the pre-registered plan; **S2a/S2b/S2c/S2d**
amended it as revisions 2–5. **S3a** implemented the emitter and gates against
revision 3 and found 25 defects; **S3b** implemented the two scorers that decide
C2 against revision 4 and found 18. Revision 5 folds in all 18, plus three more it
found in its own drafting.

**Governing plan: `EXPERIMENT_PLAN_R5.md`** (revision 5), SHA-256
`e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201`, hashed
2026-08-18T04:00:00Z.
**FAMILY_SIZE = 17, ALPHA = 0.05/17 = 0.0029411764705882353 — unchanged.**

```
  rev 1  aeb174ff…bad3d  EXPERIMENT_PLAN.md      17 Aug 05:10Z   16 / 0.003125
  rev 2  a9954ba3…1df1   EXPERIMENT_PLAN_R2.md   17 Aug 09:25Z   16 / 0.003125
  rev 3  be61bda9…df03   EXPERIMENT_PLAN_R3.md   17 Aug 09:45Z   16 / 0.003125   ← S3a: 25 defects
  rev 4  738601db…cc9d   EXPERIMENT_PLAN_R4.md   17 Aug 18:25Z   17 / 0.00294    ← S3b: 18 defects
  rev 5  e3206e71…b201   EXPERIMENT_PLAN_R5.md   18 Aug 04:00Z   17 / 0.00294    ← GOVERNING
```

Revisions 1–4 remain **byte-identical**; every hash re-verified before and after
each step. The plan is never edited in place.

**G2's evidence is now complete and the gate is still unsigned.** All four
criteria are met (`GATES.md`). The operator signs; the revision route closes when
they do.

---

## The thesis

> In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.

**Novelty is the APPLICATION, not the mechanism.** The general mechanism —
structured decoding and output repair distorting what is measured about a model
— is published 2024–2026 literature. Its instantiation in LLM-guided NAS is not.
Any downstream sentence claiming the mechanism is a defect
(`EXPERIMENT_PLAN_R5.md` §1.2).

---

## Done

### S0 — ground truth
- Git bootstrap, local identity `Palaash Gang <palaashgang@gmail.com>`,
  pre-commit hook enforcing repo-scope and no-AI-attribution, `.gitignore`
  extended, secret scan clean, cloud host IP redacted, README genericised.
- Full audit: `audit/REPO_INVENTORY.json`, `CONTEXT_PACK.md`, `CLAIM_TRACE.md`,
  `FORENSICS.md`, `BIB_AUDIT.md`, `references_verified.bib`, `OPEN_ACTIONS.md`.
- Scaffolding: `STATE.md`, `GATES.md`, `VENUE.md`.

### S1 — position
- Corpus repaired (full-text extraction fixed for 27 sources; ABSTRACT-ONLY fell
  37 → 10), coverage audit, Q2/Q3 gap-fill, contradiction graph, loci analysis,
  two depth investigations (L1 priority, L5 proxy validity), cross-locus
  reconciliation, corpus critic.
- Venue sweep to `research/temp/venue-candidates.md` — facts and URLs only.

### S2 — claim surgery and pre-registration
- **`EXPERIMENT_PLAN.md`** (revision 1, frozen) — 948 lines. Thesis + binding
  novelty constraint; 8 abandoned claims each tied to the S0/S1 finding that
  killed it; 6 proposed claims with refutation conditions; E1, E2, E3; analysis
  protocol with FAMILY_SIZE=16 and ALPHA=0.003125 enforced in code; results-file
  schema; citation obligations; explicit non-scope.
- **`PREREGISTRATION.md`** — revision-1 hash `aeb174ff…bad3d`, taken
  2026-08-17T05:10:13Z, with the checked no-data-collected statement.
- **`DEVIATIONS.md`** — created, zero entries, log-before-run protocol in force.
- `GATES.md` — G1 recorded PASSED on operator authorisation; G2 criterion
  replaced (the replacement, and the fact that replacing a criterion mid-ladder
  violates the file's own rule, are both recorded there).
- `VENUE.md` — venue selected and its CFP fields recorded; OA-26 closed at
  8 pages.
- `audit/OPEN_ACTIONS.md` — OA-37 (C6 thread) and OA-38 (missing bib entries)
  opened; OA-5, OA-26 and OA-32 dispositions recorded.

### S2a — plan amendment (revision 2)

**`EXPERIMENT_PLAN_R2.md`** — 1,323 lines, wholesale successor, six amendments:

- **A1** — E1 batches per cell 5 → **10** (200 per cell, **6,000** E1
  generations; total budget 9,400 → **12,400**); seed vector extended to
  `[7001…7010]`. Adopted because the five rivals are separated by the two ΔD
  change columns, and — found while implementing it — **revision 1's 5 batches
  made the paired permutation test structurally incapable of reaching ALPHA**
  (smallest attainable two-sided p = 2/2⁵ = 0.0625 vs α = 0.003125). Ten batches
  give 0.001953 and are the minimum at which E1's confirmatory tests are
  decidable at all.
- **A2** — within-cell BCa bootstrap interval on D and on ΔD (10,000 resamples,
  seed 90210, **resampling generations, not pairs**). Secondary resolution check.
- **A3** — parse-free surface diversity **S** (token 3-gram Jaccard on raw text,
  including parse failures). Secondary only, hard-constrained against becoming a
  backdoor confirmatory measure; bounds the free-prose selection effect.
- **A4** — E2 retains all three tasks, with the retention reasoning recorded:
  table-lookup substrate, marginal cost is local generation only, cheapest
  external validity in the design.
- **A5** — new **§8 Scope protection**: the calendar consideration recorded as
  CONSIDERED AND REJECTED, with the list of reductions that may not be proposed
  on schedule grounds.
- **A6** — confirmatory family **unchanged at 16, ALPHA unchanged at 0.003125**;
  checked amendment-by-amendment.

Revision 1 remains byte-identical and its hash was re-verified at the moment
revision 2 was hashed. Data status re-verified independently at
2026-08-17T09:18:00Z, not carried forward.

### S2b — plan amendment (revision 3)

**`EXPERIMENT_PLAN_R3.md`** — 1,486 lines, wholesale successor, four amendments:

- **R3-1** — E1 batches per cell 10 → **16** (320 per cell, **9,600** E1
  generations); seed vector extended to `[7001…7016]`. Chosen on the paired
  permutation test's **discreteness ceiling**, tabulated for *B* = 10/12/14/16 so
  the choice is auditable. At *B* = 10 the ceiling is **1 assignment-pair** — the
  observation must be the strictly unique maximum, so a single discordant batch
  kills the contrast at any effect size. At *B* = 16 the ceiling is **102** and
  one discordant batch lands at *p* = 0.000519, 17% of ALPHA.
- **R3-2** — the permutation floor becomes **FATAL**. The emitter computes
  `min_attainable_p` for every confirmatory test **at plan-load time, before any
  data is read**, and **aborts** if any test has `min_attainable_p ≥ ALPHA`. A
  run-time arm recomputes from the *realised* usable count and marks degraded
  contrasts `undecidable_by_discreteness` with `significant: null` — never
  `significant: false`. This closes the defect **class** that made revision 1's
  X1–X4 undecidable by construction, not just that instance.
- **R3-3** — **R redefined** as `R_final = max(20, the value
  scripts/power_e2.py confirms at S3)`. Raising R to meet the simulation is
  **compliance, not a deviation**; lowering below 20 stays forbidden. Removes an
  asymmetry revision 2 left open. Budget restated as **9,600 + 320·R** (16,000 at
  the floor) rather than a fixed number.
- **R3-4** — confirmatory family **unchanged at 16, ALPHA unchanged at
  0.003125**; checked amendment-by-amendment.

Revisions 1 and 2 both remain byte-identical, re-verified before and after. Data
status re-verified independently at 2026-08-17T09:39:26Z, with the three known
`*spec*`/`*transcript*` near-matches enumerated so the sweep stays reproducible.

### S3a — build the instrument, run its gates against the plan

Built **before** G2 was signed, deliberately, because the last two revisions each
shipped a defect that was invisible until someone tried to execute the plan.

- **`src/emit/`** — the emitter (schema 1.2.0), the only path by which a number
  reaches a results file. Three fatal gates: **G-family** (confirmatory count ≠ 16
  → abort), **G-alpha** (any `alpha_applied` ≠ alpha → abort), **G-discreteness**
  plan-load arm (any confirmatory test with `min_attainable_p ≥ alpha` → abort,
  naming the test, its *B* or *n*, its floor and alpha). Plus the run-time arm,
  which marks a degraded contrast `undecidable_by_discreteness` with
  `significant: null` and does **not** abort.
- **`tests/`** — 8 adversarial gate fixtures (**8/8** behaved as required),
  11 known-answer metric cases (**11/11** matched), the D_rand computation, the
  replay test, and the signature-matching probe. `tests/run_all.py` runs all five
  suites: **5/5 pass**.
- **`D_rand` measured** from the repository's own sampler, no model involved:
  **0.771931** (E1 batch-mean form), across-batch std **0.007967**. Inside the
  §2.6 sanity range, but not at the ≈0.74 anchor the plan cites — see D-09/D-10.
  Tracked copy at `audit/E1_reference_S3a.json` because `results/` is gitignored.
- **`audit/S3A_IMPLEMENTATION_DEFECTS.md`** — 25 defects: **7 blocking**,
  13 material, 5 minor. Six of the seven blocking items are in §2.5/§2.6.

**No compute was used in S2, S2a, S2b or S3a. No model called — local or hosted —
no training, no GPU, no ML dependency installed.** `src/search_space.py` imports
torch, which is absent, so the sampler was executed by verbatim source extraction
(D-11) rather than by installing anything.

### S2c — plan amendment (revision 4) *(this session)*

**`EXPERIMENT_PLAN_R5.md`** — 1,653 lines, wholesale successor. Folds in all 25
S3a defects; §9 carries a defect-by-defect disposition.

- **R4-1** — new **§2.8 anchor-tracking sub-design**: enumeration order
  {canonical, reversed} × in-context exemplar {modal, non-modal} at the anchor
  configuration, **4 cells × 16 × 20 = 1,280 generations**. New outcome
  `anchor_tracking` (`tracks_first`, `tracks_exemplar`), a **sixth prediction
  column**, and one new confirmatory contrast **X5**. This is what fixes the
  blocking defect D-02: `format tax` and `genuine prior` now differ in two
  columns, one of which does **not** require free prose to parse, so **free-prose
  becomes corroborating rather than load-bearing for C2**.
  **FAMILY_SIZE 16 → 17; ALPHA → 0.05/17 = 0.0029411764705882353.**
- **R4-2** — **`generations[]`** added to the schema at generation level, plus
  `contrast_operands`, `pairing_key` and `test_statistic`, so every pooled,
  bootstrapped and entropy quantity is recomputable and every contrast's operands
  and stage are machine-readable. **`results/` removed from `.gitignore`** — the
  layer G5 depends on is now tracked.
- **R4-3** — **`D_rand` redefined** from a corrected uniform sampler at fixed
  block count: **0.719205** (analytic 0.718872, agreement 0.000333). The
  repository's sampler is reported separately as **`D_repo_sampler` = 0.771931**
  and never anchors a threshold — it is not uniform (`pooling` is 48.21% `none`
  against 25%) and its block-count variation inflates *d*. Sanity range tightened
  **[0.65, 0.80] → [0.705, 0.735]**, which now rejects the repository sampler, the
  block-free corrected sampler *and* revision 3's own 0.74 anchor.
- **R4-4** — remaining blocking and material defects resolved: `partial` given a
  ΔD band and `worsens` named; frontier precision substitution stated;
  indeterminate rescaling generalised to *k* columns
  (winner needs ≥ ceil(0.75·n_scoreable), n_s < 4 → no verdict); E2's
  **difference-of-means** permutation statistic, Cliff's δ tie convention,
  leave-one-run-out BCa jackknife and lowest-index validation tie-break all named.
- **R4-5** — **full discreteness table re-run at ALPHA = 0.05/17. Every floor
  clears.** `B_batch` = 16 keeps a ceiling of 96 assignment-pairs (was 102) and
  one discordant batch at 17.6% of ALPHA; the discordance tolerance is unchanged
  at 1, so no change to `B_batch` is required.

**Budget: 10,880 + 320·R generations — 17,280 at the R floor of 20.**
*(rev 1: 9,400 · rev 2: 12,400 · rev 3: 16,000 · rev 4: 17,280.)*

`src/emit/constants.py` updated to the new family and alpha; the **B1–B8 gate
fixtures re-run and 8/8 still behave as required**, with B1/B2 now testing
16/18 against a family of 17 rather than 15/17 against 16 — they are written
against `K.FAMILY_SIZE`, so they test the invariant rather than a literal.
Full suite: **5/5 pass**.

**No compute in S2, S2a, S2b, S3a or S2c. No model called — local or hosted — no
training, no GPU, no ML dependency installed.**

### S3b — implement the two scorers that decide C2 *(this session)*

Built **before** revision 5 and before G2, on the same principle as S3a: the plan
is only as sound as its last execution.

- **`src/emit/anchor.py`** — the anchor-tracking scorer (§2.4.7, §2.8).
  Per-field modal extraction restricted to collapsed fields; `tracks_first` and
  `tracks_exemplar` kept **separate, never merged**; ties broken toward the
  earlier-enumerated value with `modal_tie_count` recorded; zero collapsed fields
  → `null`, never imputed; BCa intervals bootstrapped over **batches**. Emits
  **three** labellings side by side: the plan's flat 0.50 bar, a symmetric
  per-field chance rule, and a **one-sided null-at-chance** rule.
- **`src/emit/signature.py`** — the generalised signature scorer (§2.5, §2.6).
  Five rivals × six columns; the new `partial` / `worsens` change bands;
  indeterminate columns lowering `n_s` with threshold `ceil(0.75·n_s)` and
  `n_s < 4` → no verdict; strict-max winner; tie or sub-threshold → mixed
  attribution; zero-match → reportable outcome.
- **`tests/test_scorers.py`** — C1–C16, **22/22 assertions pass**, including
  **C15**: with free-prose forced `indeterminate`, `repair artifact` and
  `format tax` still separate.
- **`tests/check_coverage.py`** — plan-to-code coverage. **13/15 forward
  mappings and 11/15 reverse mappings resolve; 6 gaps.**
- **`audit/S3B_SCORER_DEFECTS.md`** — 18 defects: **5 blocking**, 9 material,
  3 minor, 1 resolved by implementation.

**The two that sit on C2's path:** the **pre-repair** tracking aggregate has no
registered cell field, though both instrument rivals hinge on it (S3B-12); and the
per-field rule as briefed, implemented symmetrically, makes `quantisation`,
`decoding` and `genuine prior` unmatchable on the tracking column (S3B-11) — the
**one-sided** form is required.

**No compute. No model called — local or hosted — no training, no GPU, no ML
dependency installed. All fixture data constructed by hand.**

### S2d — plan amendment (revision 5) *(this session)*

**`EXPERIMENT_PLAN_R5.md`** — 2,158 lines. Folds in all 18 S3b defects; §9 carries
the disposition, §10 keeps revision 4's disposition of the 25 from S3a.

- **R5-1** — the **one-sided per-field chance rule** is registered for anchor
  tracking. `tracks` = interval excludes chance from above; `no tracking` =
  contains it or below; `indeterminate` = insufficient data only. Chance is
  **1/|V_f|** per field, **0.263889** weighted over all six, **0.25** over the
  three exemplar fields. The revision-4 flat 0.50 bar and the symmetric per-field
  rule are both **rejected** — the flat bar returned `indeterminate` at 2.3× and
  2.8× chance; the symmetric rule never fires `no tracking` and would have made
  three of five rivals unmatchable.
- **R5-2** — tracking runs at **all three models** (12 cells). **X5 stays one
  contrast and FAMILY_SIZE stays 17**: column classification is descriptive by CI
  position, not a hypothesis test, so per-model scoring needs no per-model
  contrast, and tripling X5 would tighten alpha for sixteen other tests to buy
  nothing.
- **R5-3** — **`tracks_{first,exemplar}_pre_mean` and `_ci95` registered** at cell
  level. The blocking one: without them the column could not be scored at all.
- **R5-4/5/6/7/8** — field-collapse threshold (normalised entropy < 0.15); both
  tracking denominators; three explicit grid predicates; `contingent_on_
  indeterminacy` instead of preventing the behaviour; the level columns' inability
  to falsify recorded as a KNOWN LIMITATION; **`B_tracking = max(16, S3 pilot)`**.
- **R5-9/10** — schema → **1.4.0**, closing every Block D coverage gap.
- **R5-11** — **full discreteness table re-run for all 17 tests; every floor
  clears**, the binding one at 1.038% of ALPHA.

**Three defects found in revision 5's own drafting and closed before freezing:**
the (canonical, modal) **degenerate cell** where `tracks_first` and
`tracks_exemplar` cannot be dissociated; **no collapse means no tracking**, without
which `repair artifact` was untestable exactly when true; and the **logically
unsatisfiable conjunction** in the format-tax predicate.

**Budget: 9,600 + 240·B_tracking + 320·R — 19,840 at both floors.**
*(rev 1: 9,400 · rev 2: 12,400 · rev 3: 16,000 · rev 4: 17,280 · rev 5: 19,840.)*

Fixtures re-run against R5's constants: **B1–B8 8/8 unchanged**, **C1–C16 22/22**,
full suite **7/7**.

**No compute in any session. No model called — local or hosted — no training, no
GPU, no ML dependency installed.**

## The findings that shape everything downstream

1. **The repository contains no experimental data.** 0 RAW / 0 SPEC /
   0 TRANSCRIPT across all 24 original cells; 26% of headline claims ORPHAN.
   **OA-1 is CLOSED** — unrecoverable, will be regenerated. Every ORPHAN finding
   in `audit/CLAIM_TRACE.md` is permanent.
2. **`sanitize_config` collapses out-of-vocabulary *and absent* fields to
   `standard_3x3 / relu / batchnorm`** — exactly the reported "narrow prior" —
   and runs on the LLM arms only. E1 exists to separate this from the model.
3. **The unqualified thesis is refuted** (RZ-NAS, EvoPrompting, and GENIUS's own
   per-trial tables) and the mechanism-specific version is **scooped** by
   CoLLM-NAS (Oral, CVPR 2026 NAS Workshop).
4. **The instrumentation mechanism is already published**; only its NAS
   application is open. This is the binding novelty constraint.

## Time — the calendar is not an input to scope

**Recorded as CONSIDERED AND REJECTED at S2a, carried into revision 3**
(`EXPERIMENT_PLAN_R5.md` §8). The nearest workshop deadline is 2026-08-29 AoE and
the plan now specifies **9,600 + 240·B_tracking + 320·R** generations — 19,840 at
both floors — with zero training runs. **The venue follows the artifact, not the reverse.**
The chosen venue is non-archival, so missing a cycle costs nothing — no priority,
no publication window, no claim to the result — and workshop cycles recur,
whereas a design weakened to fit a date is permanent.

**Every revision has raised the budget, not lowered it** — 9,400 → 12,400 →
16,000 → 17,280 → 19,840 at the floors — each time because that is what made a confirmatory test
decidable. That is the precedent §8 fixes. §8.2 lists what may not be proposed as
a scope cut on schedule or budget grounds, now including any reduction of *B*
below 16, which must argue against the ceiling table rather than against cost.
Scope changes on **methodological** grounds remain available; before G2 they are
a further revision, after G2 a `DEVIATIONS.md` entry.

## Open

- **G0, G1, G2 all await operator signature.** G0's recommendation is in
  `audit/SESSION_1_REPORT.md` §8. Never self-sign.
- **G2's evidence is complete and all four criteria are met. The gate awaits the
  operator's signature.** Signing closes the revision route.
- **Remaining before data collection (S3):** freeze and hash the E1/E2 prompts
  including the twelve tracking prompts with their order-only diffs; run
  `scripts/power_e2.py` at the registered ALPHA to set `R_final`; run the
  tracking-CI-width pilot to set `B_tracking`; measure `D_rand` from the
  registered sampler; fix and test OA-10 through OA-17; select and pin the
  frontier model.
- **38 open actions**, `audit/OPEN_ACTIONS.md`. Blocking before S6: **OA-37**
  (CoLLM-NAS replication status, five unverified leads) and **OA-38** (8 of 15
  obliged citations absent from `references_verified.bib`).
- **S3 must run before any data collection**: measure `D_rand`; run
  `scripts/power_e2.py` at the new ALPHA and **set `R_final = max(20, its output)`** — raising R to
  meet it is compliance, not a deviation (§3.4); select and pin the frontier API
  model; freeze and hash the E1/E2 prompts; **implement gate 2 and confirm it
  passes at plan-load** (§5.2); fix and test OA-10 through OA-17; complete the
  GENIUS Appendix A.3 pass left open by seam S3.
- **The generation budget is not yet a fixed number.** It is `10,880 + 320·R`,
  and R is set by the S3 simulation with a floor of 20 — 17,280 at the floor,
  more if the simulation demands it. The plan does not cap it (§3.5, §8.2). The
  simulation must run at the **new** ALPHA, 0.0029411764705882353.
- `neurips_2026.sty` must be fetched and byte-verified from **two** independent
  mirrors at S6 (`media.neurips.cc` has returned 404/403).
- Anonymity and archival status of the selected venue are **NOT STATED** on its
  CFP. Treated as double-blind; verify at S6.

## Blocked

- *(cleared)* The `GH007` push block is resolved; `origin/main` is current.

## Not done, deliberately

- No experiment run, no model trained, no ML dependency installed.
- Nothing under `paper/`, `src/`, `scripts/`, `logs/` or `archive/` modified in
  any session so far. The manuscript is untouched and still states the abandoned
  claims; it is rewritten at S6 against the results-file layer, not before.
