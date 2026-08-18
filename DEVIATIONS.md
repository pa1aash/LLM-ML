# DEVIATIONS

Departures from the **governing plan** — currently `EXPERIMENT_PLAN_R6.md`
(revision 6). The plan is frozen at the SHA-256 recorded in `PREREGISTRATION.md`
and is **never edited**. Every change to what is actually done is logged here
instead.

---

## Rules

1. **Log before, not after.** Any departure is written here **before the analysis
   it affects is run**. Not after the run. Not at write-up.

2. **Every entry carries five fields**, in this order:
   - **Date** — ISO-8601.
   - **Plan section** — the §number in the governing plan being departed from.
   - **What changed** — the old text and the new behaviour, concretely.
   - **Why** — the reason. "It seemed better" is not a reason; state what was
     learned that the plan did not anticipate.
   - **Data already collected for this analysis?** — `yes` or `no`, explicitly.
     If `yes`, the entry is a late entry; see rule 4.

3. **Commit before the run.** Each entry is committed before the run or analysis
   it governs, so git history independently timestamps the ordering. A deviation
   whose commit post-dates the results it governs is a late entry regardless of
   what its Date field says.

4. **Late entries are labelled, not hidden.** An entry added after the affected
   analysis has already run is a protocol violation. Its heading is prefixed
   `LATE — PROTOCOL VIOLATION`. It is not deleted, not backdated, not quietly
   reworded. The manuscript discloses the count of late entries.

5. **The plan is not edited.** If it must be superseded wholesale, a numbered
   revision is written as a **new file**, hashed separately, and cites the prior
   hash it supersedes. Every superseded plan file stays in the repository
   byte-identical to the version that was hashed.

6. **Unplanned analyses are deviations.** Any analysis not named in
   the governing plan's §5.1 is exploratory and is logged here before it runs.
   It may not carry a p-value, and may not appear in the abstract, the
   contributions list, or the conclusions (§5.4).

---

## Entry template

```
### D-nnn — <one-line title>

- **Date:** YYYY-MM-DD
- **Plan section:** §x.y
- **What changed:**
- **Why:**
- **Data already collected for this analysis?** yes | no
```

---

## Supersession records — NOT deviations

A wholesale change to the plan before any data collection is a **numbered
revision written as a new file** under **rule 5 above** (the governing plan's own
§5.6 rule 4, renumbered in this list), not a deviation entry. **Five have
occurred**, all before any data collection. All five are recorded here so the
ledger is a complete history, even though none is a departure from a plan under
which work had begun.

**2026-08-17 — revision 1 superseded by revision 2.** Six amendments (A1–A6):
E1 batches 5 → 10; a within-cell bootstrap interval on D and ΔD; a parse-free
surface diversity measure S; retention of all three E2 tasks with reasoning
recorded; a new §8 recording the calendar as considered and rejected; and
confirmation that the confirmatory family was unchanged. `EXPERIMENT_PLAN_R2.md`,
SHA-256 `a9954ba3…1df1`, citing revision 1's `aeb174ff…bad3d`.

**2026-08-17 — revision 2 superseded by revision 3.** Four amendments (R3-1…4):
E1 batches 10 → 16, chosen on the paired permutation test's discreteness ceiling
and justified by a table for *B* = 10/12/14/16; the permutation floor made
**fatal**, checked at plan-load before any data is read, with a run-time arm that
marks degraded contrasts `undecidable_by_discreteness` rather than letting them
read as nulls; **R redefined** as `max(20, the S3-confirmed value)` so that an
increase demanded by the power simulation is compliance rather than a deviation;
and confirmation that the family was unchanged. `EXPERIMENT_PLAN_R3.md`, SHA-256
`be61bda9…df03`, citing revision 2's `a9954ba3…1df1`.

*(Across the first two supersessions the confirmatory family was checked
amendment-by-amendment and stayed at 16 tests, ALPHA = 0.003125.)*

**2026-08-17 — revision 3 superseded by revision 4.** S3a built the measurement
instrument and ran it against revision 3 **before** G2 was signed, and found **25
implementation defects, seven blocking** (`audit/S3A_IMPLEMENTATION_DEFECTS.md`).
Revision 4 folds all 25 in. The load-bearing change is a new **anchor-tracking
manipulation** (§2.8) with one new confirmatory contrast X5, which separates
`format tax` from `genuine prior` without depending on free-prose parsing;
**FAMILY_SIZE 16 → 17 and ALPHA → 0.05/17 = 0.0029411764705882353**. Also:
`generations[]` added to the schema, `results/` un-ignored, D_rand redefined from
a corrected uniform sampler (0.719205) with the sanity range tightened to
[0.705, 0.735], and E2's permutation statistic, tie convention, jackknife and
tie-break all named. `EXPERIMENT_PLAN_R4.md`, SHA-256 `738601db…cc9d`, citing
revision 3's `be61bda9…df03`.

`EXPERIMENT_PLAN.md`, `EXPERIMENT_PLAN_R2.md` and `EXPERIMENT_PLAN_R3.md` all
remain byte-identical; every hash was re-verified before and after each step.

**2026-08-18 — revision 4 superseded by revision 5.** S3b implemented the two
scorers that decide C2 and found **18 defects, five blocking**
(`audit/S3B_SCORER_DEFECTS.md`). Revision 5 folds in all 18. The load-bearing
changes: the **one-sided per-field chance rule** replaces the flat 0.50 bar
(which returned `indeterminate` at 2.3× and 2.8× chance) and the symmetric
per-field rule (which would have made three of five rivals unmatchable); the
**pre-repair tracking aggregates are registered at cell level**, without which
the column could not be scored at all; the tracking sub-design runs at **all
three models**; and `B_tracking` becomes a floor-plus-procedure like R.
**FAMILY_SIZE stays 17 and ALPHA stays 0.0029411764705882353** — the extra models
add no confirmatory test, because column classification is descriptive by CI
position rather than a hypothesis test. `EXPERIMENT_PLAN_R5.md`, SHA-256
`e3206e71…b201`, citing revision 4's `738601db…cc9d`. Three further defects found
in revision 5's own drafting were closed before freezing (plan §9).

`EXPERIMENT_PLAN.md`, `_R2`, `_R3` and `_R4` all remain byte-identical; every hash
was re-verified before and after each step.

**2026-08-18 — revision 5 superseded by revision 6.** S3c ran the two registered
pilots and specified the cross-level exemplar predicate. **`R_final = 24`** (power
at the floor of 20 is 0.702, below the 0.80 target, so raising R is compliance)
and **`B_tracking = 28`** (binding on the cross-level delta; single-cell
`tracks_exemplar` would have needed 40 but no predicate reads it). The registered
`B_tracking` criterion was **miscalibrated** — a half-width of 0.15 at a true rate
of 0.40 gives [0.25, 0.55], which contains the chance rate 0.263889 and reads `no
tracking` — and is corrected. **FAMILY_SIZE stays 17, ALPHA stays
0.0029411764705882353**; the cross-level delta is classified descriptively by CI
position and adds no test. `EXPERIMENT_PLAN_R6.md`, SHA-256 `d63a7625…d340b`,
citing revision 5's `e3206e71…b201`.

**Revision 6's scope was closed by construction and it is the last before G2.**
Six further items found this session are in `audit/S3C_DEFECTS.md` and are handled
after G2 as entries in this ledger, not as plan changes.

`EXPERIMENT_PLAN.md`, `_R2`, `_R3`, `_R4` and `_R5` all remain byte-identical.

**This ledger governs departures from revision 6 from this point forward.**

**The revision route closes at the END OF S3**, when the analysis code exists and
G2 is signed against a plan that has been executed rather than only read.
Revision 3 declared itself the last pre-data revision on the assumption the gate
would be signed next; an implementation pass then found 25 defects in it. That is
why the closing condition is now the code existing, not the calendar. After the
gate is signed, every change — including one that would previously have justified
a new revision — is an entry in the Entries section below, logged before the
affected analysis runs.

**One thing that is explicitly not a deviation:** raising R to the value
`scripts/power_e2.py` confirms at S3, where that value exceeds 20 — and, at
revision 5, raising `B_tracking` above 16 to meet the tracking-CI-width pilot.
Revision 5 §3.4 and §2.8 registers the procedure rather than the number, so complying with its output
is compliance. Note that the simulation must now run against
**ALPHA = 0.0029411764705882353**, not the 0.003125 of revisions 1–3. Lowering R below 20 is forbidden outright (§8.2) and is not
available even as a logged deviation.

---

## Entries

**Numbering.** Deviation entries are numbered `D-001`, `D-002`, … with three
digits, deliberately distinct from the two-digit `D-01`…`D-25` *defect* IDs the
governing plan uses in its §10 disposition tables. A `D-0nn` here is a departure;
a `D-nn` there is a defect the plan already closed.

**Status at the head of S3-1.** No data has been collected and no analysis has
been run as of the revision-6 pre-registration hash (`d63a7625…d340b`,
2026-08-18T04:35:00Z). Every entry below is therefore a `no` on field five, and
every one is committed before the artifact it governs.

---

### D-001 — the exemplar value map is defined for all six per-block fields

- **Date:** 2026-08-18
- **Plan section:** §2.8, §2.4.7, §5.5 (`exemplar_values`)
- **What changed:** §2.8 names exemplar values for **three** of the six per-block
  fields — `conv_type`, `activation`, `normalization` — and §5.5's
  `exemplar_values` header carries only those three. A worked example of a block
  is not writable without values for `channels`, `skip_connection` and `pooling`;
  the plan left them unspecified. They are fixed here, **identical across both
  exemplar levels**, at values that are **not first-enumerated under either
  enumeration order**:

  | field | `modal` | `non_modal` | position in vocabulary | first under canonical / reversed |
  |---|---|---|---|---|
  | `conv_type` | `standard_3x3` | `depthwise_separable` | 1 / 2 | registered in §2.8 |
  | `channels` | `64` | `64` | 2 of 4 | `32` / `256` — neither |
  | `activation` | `relu` | `gelu` | 1 / 2 | registered in §2.8 |
  | `normalization` | `batchnorm` | `groupnorm` | 1 / 3 | registered in §2.8 |
  | `skip_connection` | `projection` | `projection` | 2 of 3 | `identity` / `none` — neither |
  | `pooling` | `avgpool` | `avgpool` | 2 of 4 | `maxpool` / `none` — neither |

  The emitted `exemplar_values` header gains a `held_constant` sub-map recording
  the three filled fields and the reason. **`tracks_exemplar`'s denominator is
  unchanged** and remains the three fields §2.4.7 registers: the three filled
  fields do not vary across exemplar levels, so they carry no exemplar
  manipulation and are not part of the statistic.
- **Why:** the three unnamed fields must take *some* value in the prompt text.
  Leaving the choice to the moment of writing would let it be made silently, and
  the choice is not neutral: a filled value that happens to be first-enumerated
  would manufacture apparent `tracks_first` signal in the cells where it is
  first. Holding them constant across exemplar levels confines the exemplar
  manipulation to the three registered fields; choosing mid-vocabulary values
  makes their contribution to `tracks_first` **conservative** — if the model
  copies them, the modal value is first-enumerated under neither order and
  contributes 0, biasing `tracks_first` down rather than up.
- **Data already collected for this analysis?** no

---

### D-002 — prompt file layout, composition rule, and the empty exemplar

- **Date:** 2026-08-18
- **Plan section:** §2.1, §2.8, §3.2, §5.5 (`prompts`)
- **What changed:** the plan says prompts are "frozen in `prompts/E1/`",
  "`prompts/E1/anchor/`" and "`prompts/E2/`" and hashed into the results file,
  without stating how a cell's prompt is assembled from them. Registered here:

  1. **Composition is textual and deterministic.** `schema_canonical.txt` and
     `schema_reversed.txt` each carry the token `{{EXEMPLAR_BLOCK}}` alone on one
     line. Composition replaces that line with the exemplar file's contents; runs
     of three or more consecutive newlines in the result are collapsed to two.
  2. **`exemplar_absent.txt` is a zero-byte file**, SHA-256
     `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, so the
     absent level is the *literal* absence of the block rather than a rewording
     of it.
  3. **The main grid's schema cells compose `canonical` + `absent`.** The 30
     main-grid cells therefore carry **no worked example**, and the exemplar is a
     factor of the §2.8 sub-design only, as §2.8 describes it.
  4. **The value enumerations appear exactly once per field**, in one
     `### Allowed values` block, so that "reverse every field's allowed values"
     has a single unambiguous site per field and the canonical-vs-reversed diff
     is checkable line by line.
  5. **Free-prose carries the same search-space description and the same value
     enumerations** as the schema variant, in canonical order, and differs by
     removing the JSON structure template and the return-only-JSON instruction.
  6. Files are written at the paths the plan names, with the filenames S3-1
     specifies: `prompts/E1/{schema_canonical,schema_reversed,freeprose}.txt`,
     `prompts/E1/anchor/exemplar_{modal,nonmodal,absent}.txt`,
     `prompts/E2/e2_{zeroshot,uncurated,curated,archive}.txt`.
- **Why:** §2.8's invariant — "the only difference between the two order levels
  is the order of the value lists" — is only checkable if each field's values
  occur in exactly one place. Point 5 is the narrower of two readings: giving
  free-prose a *different* description would confound the format factor with the
  information the two arms receive, and X1 would no longer isolate format.
  Point 3 keeps the main grid free of an exemplar the plan never registered for
  it.
- **Data already collected for this analysis?** no

---

### D-003 — E2's archive size *m* and the curated statement's bound

- **Date:** 2026-08-18
- **Plan section:** §3.2
- **What changed:** §3.2 defers "the curation prompt and *m*" to the frozen
  `prompts/E2/` artifacts without fixing either. Fixed here: **m = 5** for the
  external-archive arm, and the curated arm's strategy statement is bounded at
  **120 words**, stated in the curation prompt itself. The curation prompt lives
  in `e2_curated.txt` under a `=== CURATION PROMPT ===` delimiter, so the arm's
  two prompts — propose and distil — are one frozen, singly-hashed artifact.
- **Why:** both numbers are prompt content, which §3.2 delegates to this
  artifact, so setting them is compliance. They are logged because the plan
  states neither, and an unstated number chosen at run time is indistinguishable
  from one chosen after seeing results. m = 5 is a quarter of the k = 20
  proposals a run makes, keeping the archive bounded well below the uncurated
  arm's monotonically growing context, which is the contrast the arm exists to
  draw. The 120-word bound plays the same role for the curated arm.
- **Data already collected for this analysis?** no

---

### D-004 — per-generation seeding, and the two record fields it needs

- **Date:** 2026-08-18
- **Plan section:** §2.3 (seeding scheme), §5.5 (`generations[]`)
- **What changed:** §2.3 registers one seed per **batch** — batch *b* uses
  `S[b]` — and §5.5's `generations[]` example stores that batch seed on each
  generation (`"batch": 3` carries `"seed": 7004`). A batch of 20 generations
  seeded once is reproducible only by replaying the whole batch in order. The
  harness seeds **each generation** at
  `generation_seed = S[b] * 1000 + index_in_batch`, and the record carries two
  additional keys:
  `generation_seed` (integer) and `seed_derivation`
  (`"batch_seed * 1000 + index_in_batch"`). **`seed` keeps its registered
  meaning and value — `S[b]`, the batch seed — and every cross-cell contrast
  still pairs on the batch index exactly as §2.3 registers.**
- **Why:** a generation that cannot be reproduced on its own cannot be audited
  on its own, and a re-run that must replay 19 earlier generations to reach the
  twentieth is not a check. The derivation is injective over the registered
  ranges (`S[b] ≤ 7016`, `index < 20`), so no two generations in E1 share a
  seed. Recorded rather than silent because schema 1.5.0 is registered and these
  two keys are not in it.
- **Data already collected for this analysis?** no

---

### D-005 — `coerced` on `channels` snaps to the nearest legal value

- **Date:** 2026-08-18
- **Plan section:** §2.4.4 (repair channels), §2.4.1
- **What changed:** §2.4.4's table defines `coerced` as "present,
  out-of-vocabulary, **rewritten to `valid_vals[0]`**". That is true of the five
  string fields but **not** of `channels`: the repository's `sanitize_config`
  ([run_v2.py:52-67](src/run_v2.py#L52)) snaps `channels` to the nearest legal
  value, `min(valid_vals, key=lambda x: abs(x - val))`, and §2.4.1 says so
  explicitly — "`channels` … **categorical**, because repair snaps to the
  nearest legal value". The two passages disagree. The harness implements the
  **repository's** behaviour, because the repository's sanitiser is the object
  under test, and records the channel as `coerced` with the destination value
  stored alongside.
- **Why:** reimplementing `channels` as "rewrite to `valid_vals[0]`" would make
  the instrument measure a sanitiser that does not exist. The consequence for
  §2.8 is stated rather than left implicit: on `channels`, a coercion does
  **not** land on the first-enumerated value, so a channels coercion does not
  contribute to `tracks_first` the way a string-field coercion does. `filled`
  is unaffected — an absent `channels` is inserted at `valid_vals[0]` under both
  readings, which is the mechanism the `repair artifact` rival rests on.
- **Data already collected for this analysis?** no

---

### D-006 — the sanitiser's value lists are parameterised by the cell's enumeration order

- **Date:** 2026-08-18
- **Plan section:** §2.8, §2.5 (the `repair artifact` predicate)
- **What changed:** the repository's `sanitize_config` hard-codes its `valid`
  dictionary in canonical order. §2.8's mechanism requires more than that:
  "`sanitize_config` coerces and fills to `valid_vals[0]` — literally the
  first-enumerated value — **so reversing the enumeration reverses the repair
  target**." That is only true if the sanitiser and the prompt share one
  enumeration-order object. The harness therefore takes the order as a
  parameter: `sanitise(spec, enumeration_order)` fills and coerces to
  `order[0]`, and the prompt for that cell enumerates in the same order, from
  the same source.
- **Why:** without this the `repair artifact` row of §2.5 is unfalsifiable — the
  repair target would never move, so `post_first` could never track the reversed
  order, and X5 would be measuring the model alone rather than the apparatus.
  This is the single mechanism the entire anchor-tracking column rests on, and
  known-answer test **D9** exists to check it holds.
- **Data already collected for this analysis?** no

---

### D-007 — generation records carry the fields that make backend honesty auditable

- **Date:** 2026-08-18
- **Plan section:** §5.5 (`generations[]`), §2.1 (`model` header)
- **What changed:** schema 1.5.0's `generations[]` record is extended, additively
  and without changing the meaning of any registered key, with:
  `backend` (`local_bf16` | `local_nf4` | `hosted_api` | `stub`),
  `model_served` and `model_revision_served` **per generation**,
  `quantisation`, `finish_reason_source` (`computed_from_token_ids` |
  `provider` | `stub`), `status` (`ok` | `backend_error`),
  `error`, `prompt_sha256`, `sanitiser_applied`, `enumeration_order_applied`,
  `n_generated_tokens`, and `generation_seed` / `seed_derivation` from D-004.
- **Why:** OA-3 is that no artifact can say which model produced the original
  proposals, because the served model was never recorded. A header field alone
  does not close it: a server swapped mid-run would leave the header intact.
  Recording what answered **on every generation** makes the swap visible.
  `finish_reason_source` closes the corresponding hole for OA-16 — a
  `finish_reason` whose provenance is unrecorded is not distinguishable from a
  hardcoded one, which is exactly the defect.
- **Data already collected for this analysis?** no

---

### D-008 — `PLAN_FILENAME` and the schema's own stale plan reference

- **Date:** 2026-08-18
- **Plan section:** §5.5 (`plan_sha256`)
- **What changed:** `src/emit/constants.py` carried
  `PLAN_FILENAME = "EXPERIMENT_PLAN_R5.md"` alongside `PLAN_REVISION = 6` and
  revision 6's hash; corrected to `EXPERIMENT_PLAN_R6.md`. The plan's own §5.5
  specimen labels the field
  `"plan_sha256": "<SHA-256 of EXPERIMENT_PLAN_R4.md at freeze>"`, a stale
  caption carried forward across revisions. The emitted value is and stays
  revision 6's `d63a7625…d340b`, which is what `plan_revision: 6`,
  `plan_supersedes_sha256` and `plan_chain_sha256` are all consistent with.
- **Why:** a filename constant that names the wrong document is a provenance
  defect even when the hash beside it is right — anyone reconciling the two
  would have to guess which is authoritative. The plan is closed and is not
  edited; the correction is to the code and is recorded here.
- **Data already collected for this analysis?** no

---

### D-009 — the emitter header is completed to schema 1.5.0

- **Date:** 2026-08-18
- **Plan section:** §5.5
- **What changed:** the S3a emitter announced `schema_version: 1.5.0` while
  omitting registered 1.4.0/1.5.0 header keys. Added, all with the values §5.5
  states: `b_tracking` (value / floor / source / binding_quantity), `r_final`
  (value / floor / source / power_at_floor), `field_collapse_entropy_threshold`,
  `exemplar_values`, `chance_rates`, `tracking_label_rule`, `d_rand`,
  `generations[]`, `deltas[]`, and `bootstrap`'s four registered
  `resampling_unit_*` keys in place of the single `resampling_unit` the S3a
  emitter wrote.
- **Why:** the file claimed a schema version it did not satisfy, so a consumer
  validating against §5.5 would have failed on fields the emitter simply never
  wrote. This is code catching up with the registered schema, not a change to
  it; every added key takes the value the plan specifies.
- **Data already collected for this analysis?** no

---

### D-010 — `max_new_tokens = 4096` with reasoning enabled

- **Date:** 2026-08-18
- **Plan section:** §2.1 (`enable_thinking` True), §5.5 (`model.max_new_tokens`)
- **What changed:** §5.5 emits `max_new_tokens` but the plan never fixes it. The
  original harness used 2,048 **with reasoning suppressed**
  ([run_v2.py:34](src/run_v2.py#L34), `enable_thinking=False` at
  [llm_server_small.py:43](src/llm_server_small.py#L43)). Reasoning is enabled
  here (OA-15), so the same budget would spend a large share of itself on the
  thinking trace before the JSON object begins. Fixed at **4,096**.
- **Why:** truncation is recorded honestly as `finish_reason: "length"` (OA-16),
  so a budget that is too small does not corrupt the record — it shows up as a
  measurable truncation rate. But truncation also inflates the parse-failure
  rate, which is a reported outcome (§2.4.3) and a gate on the free-prose column
  (§2.6, the 50% reliability rule), so the budget is not neutral. 4,096 doubles
  the original allowance to pay for the thinking trace. **The S3-2 smoke run
  measures the realised truncation rate; raising the budget on that evidence
  would be a further entry here, logged before the first E1 cell runs.**
- **Data already collected for this analysis?** no

---

### D-011 — the cross-level delta drops a broken batch pair rather than falling back to unpaired

- **Date:** 2026-08-18
- **Plan section:** §2.5a
- **What changed:** §2.5a pools the two exemplar cells "at the same batch index"
  and does not say what to do when one cell has a usable batch at index *b* and
  the other does not. **Registered here: the pair is dropped**, counted in
  `n_null_batches`, and never replaced by an unpaired difference. Already the
  behaviour of `src/emit/anchor.py`; logged now, before the first cross-level
  computation, as `audit/S3C_DEFECTS.md` S3C-04 requires.
- **Why:** §2.5a's null is exact *because* the same batch index is compared
  across the two cells — if the modal value is the same in both, the own and
  other sums are identically equal. An unpaired fallback would forfeit exactly
  that, replacing an exact null with an estimated one, on the column that
  separates `format tax` from every other rival.
- **Data already collected for this analysis?** no
