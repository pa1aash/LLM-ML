# DEVIATIONS

Departures from the **governing plan** — currently `EXPERIMENT_PLAN_R5.md`
(revision 5). The plan is frozen at the SHA-256 recorded in `PREREGISTRATION.md`
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
§5.6 rule 4, renumbered in this list), not a deviation entry. **Four have
occurred**, all before any data collection. All four are recorded here so the
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

**This ledger governs departures from revision 5 from this point forward.**

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

*None. No data has been collected and no analysis has been run as of the
revision-5 pre-registration hash (`e3206e71…b201`, 2026-08-18T04:00:00Z).*
