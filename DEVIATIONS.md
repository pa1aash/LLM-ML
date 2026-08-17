# DEVIATIONS

Departures from `EXPERIMENT_PLAN.md`. The plan is frozen at the SHA-256 recorded
in `PREREGISTRATION.md` and is **never edited**. Every change to what is actually
done is logged here instead.

---

## Rules

1. **Log before, not after.** Any departure is written here **before the analysis
   it affects is run**. Not after the run. Not at write-up.

2. **Every entry carries five fields**, in this order:
   - **Date** — ISO-8601.
   - **Plan section** — the §number in `EXPERIMENT_PLAN.md` being departed from.
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
   hash it supersedes. `EXPERIMENT_PLAN.md` stays in the repository byte-identical
   to the version that was hashed.

6. **Unplanned analyses are deviations.** Any analysis not named in
   `EXPERIMENT_PLAN.md` §5.1 is exploratory and is logged here before it runs.
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

## Entries

*None. No data has been collected and no analysis has been run as of the
pre-registration hash.*
