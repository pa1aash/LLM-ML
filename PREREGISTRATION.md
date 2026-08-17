# PRE-REGISTRATION

## Frozen artifact

**File:** `EXPERIMENT_PLAN.md`
**SHA-256:** `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d`
**Length:** 948 lines

**Hashed at:** 2026-08-17T05:10:13Z (2026-08-17 10:40 IST)

Verify with:

```bash
shasum -a 256 EXPERIMENT_PLAN.md
```

---

## Statement of data status at the time of this hash

**No data has been collected as of this hash.**

This is not an assertion of intent. It is a checked state of the repository at
the moment the hash was taken:

| Check | Result |
|---|---|
| `results/` directory | **absent** |
| `results_v2/` directory | **absent** |
| `results*.json` anywhere in the tree | **none** |
| `metadata.json` anywhere in the tree | **none** |
| Architecture specs (SPEC) across all 24 original condition × dataset × seed cells | **0**, per `audit/REPO_INVENTORY.json` |
| Raw generation records (RAW) across the same cells | **0** |
| Transcripts (TRANSCRIPT) across the same cells | **0** |
| Working tree at hash time | clean except the two new untracked files, `EXPERIMENT_PLAN.md` and `DEVIATIONS.md` |

No experiment in `EXPERIMENT_PLAN.md` — E1, E2 or E3 — has been run in any part.
No model has been served, no generation has been produced, no benchmark table has
been queried, and no analysis script exists yet. No hardware has been provisioned
and no ML dependency has been installed in this session.

The pre-existing absence of the *original* experiment's data is a separate fact,
established in S0 and closed as unrecoverable by operator decision (OA-1). It is
recorded here because it is the reason this plan is a rebuild rather than a
re-analysis: there is no prior dataset that any part of this plan could have been
tuned against, because no prior dataset exists in the repository at all.

---

## What the hash binds

`EXPERIMENT_PLAN.md` is not edited after this hash. Specifically, all of the
following are fixed as of `aeb174ff…`:

- the thesis and the novelty constraint (§1.1–1.2);
- the abandoned-claims list (§1.3);
- the six proposed claims and their refutation conditions (§1.4);
- E1's factor grid, cell count, per-cell *n*, seed vector, diversity metric,
  five-rival prediction table, and the numeric classification thresholds
  (§2.1–2.7);
- E2's arms, R = 20, primary task, primary estimand, permutation inference,
  effect-size choice, MDE and stopping rule (§3.1–3.5);
- E3's proxy set, statistics, and the four mandatory caveats plus the one
  prohibition (§4.1–4.5);
- the analysis protocol: every named statistic, **FAMILY_SIZE = 16**,
  **ALPHA = 0.003125**, the results-file schema, and the no-unplanned-analyses
  rule (§5.1–5.5).

Any departure from any of the above is logged in `DEVIATIONS.md` **before the
affected analysis is run**, per `DEVIATIONS.md` rules 1–6. `DEVIATIONS.md`
contains no entries as of this hash.

If the plan is superseded wholesale rather than amended, the successor is a new
file with its own hash recorded in this document, citing
`aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` as the version
it supersedes. `EXPERIMENT_PLAN.md` remains in the repository byte-identical.

---

## Revision history

| Revision | SHA-256 | Hashed at | Supersedes |
|---|---|---|---|
| 1 | `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` | 2026-08-17T05:10:13Z | — |
