# PRE-REGISTRATION

## Governing artifact

**File:** `EXPERIMENT_PLAN_R3.md` — **revision 3, the governing plan**
**SHA-256:** `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03`
**Length:** 1,486 lines
**Hashed at:** 2026-08-17T09:45:06Z (2026-08-17 15:15 IST)

**Revision 3 is the last pre-data revision.** Once G2 is signed the revision
route closes and every subsequent change is a `DEVIATIONS.md` entry logged before
the affected analysis runs.

Verify the whole chain with:

```bash
shasum -a 256 EXPERIMENT_PLAN.md EXPERIMENT_PLAN_R2.md EXPERIMENT_PLAN_R3.md
```

---

## Supersession chain

```
  revision 1  aeb174ff…bad3d   EXPERIMENT_PLAN.md      2026-08-17T05:10:13Z
        │
        ▼  §5.6 rule 4
  revision 2  a9954ba3…1df1    EXPERIMENT_PLAN_R2.md   2026-08-17T09:25:13Z
        │
        ▼  §5.6 rule 4
  revision 3  be61bda9…df03    EXPERIMENT_PLAN_R3.md   2026-08-17T09:45:06Z   ← GOVERNING
```

Revisions 1 and 2 remain in the repository **byte-identical to the versions that
were hashed**. Neither was edited, amended in place, or deleted. Both hashes were
re-verified immediately before revision 3 was written and again after it was
committed, and matched on both occasions.

Each step was taken under the rule the *preceding* revision carried:

> **§5.6 rule 4** — *"This plan is not edited after its hash is taken. Changes go
> in `DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
> written as a new file, hashed separately, and cites the prior hash it
> supersedes; every superseded plan file stays in the repository byte-identical
> to the version that was hashed."*

Each revision is a **wholesale successor**: self-contained, carrying the full
plan with the amendments folded in, so no reader has to reconcile three documents
to know what is registered. Revision 3 cites revision 2's hash in its masthead
and carries the full chain in its results-file schema (`plan_supersedes_sha256`,
`plan_chain_sha256`). Section numbering is preserved across all three, so every
cross-reference in `GATES.md`, `STATE.md`, `VENUE.md` and
`audit/OPEN_ACTIONS.md` resolves to the same content.

Revision 3 amends rule 4 in one respect only: it records that **the revision
route closes when G2 is signed**.

### What changed, revision 1 → revision 2

| ID | Amendment |
|---|---|
| A1 | E1 batches per cell 5 → 10 (200 per cell; 6,000 E1 generations). Seed vector to `[7001…7010]`. |
| A2 | Within-cell BCa bootstrap interval on D, and on ΔD for the two change columns. |
| A3 | Parse-free surface diversity **S** (token 3-gram Jaccard). Secondary only. |
| A4 | E2 retains all three tasks, with the retention reasoning recorded. |
| A5 | The calendar consideration recorded as CONSIDERED AND REJECTED (new §8). |
| A6 | Confirmatory family unchanged at 16; ALPHA unchanged at 0.003125. |

### What changed, revision 2 → revision 3

| ID | Amendment |
|---|---|
| **R3-1** | E1 batches per cell 10 → **16** (n = 320 per cell; **9,600** E1 generations). Seed vector to `[7001…7016]`; earlier entries unchanged. Chosen on the paired permutation test's discreteness ceiling, tabulated for *B* = 10, 12, 14, 16 in §2.3 so the choice is auditable. |
| **R3-2** | The permutation floor becomes **FATAL**. The emitter computes `min_attainable_p` for every confirmatory test at **plan-load time, before any data is read**, and **aborts** if any has `min_attainable_p ≥ ALPHA`. A run-time arm marks degraded contrasts `undecidable_by_discreteness` rather than letting them read as nulls. Closes the defect class that made revision 1's X1–X4 undecidable by construction. |
| **R3-3** | **R redefined** as `R_final = max(20, the value scripts/power_e2.py confirms at S3)`. An increase from that simulation is **compliance, not a deviation**; a decrease below the floor of 20 stays forbidden. Budget restated as `9,600 + 320·R`. |
| **R3-4** | Confirmatory family **unchanged at 16, ALPHA unchanged at 0.003125**. |

---

## Statement of data status at the time of the revision-3 hash

**No data has been collected as of this hash.** Re-verified independently at
2026-08-17T09:39:26Z — a fresh sweep, not carried forward from revision 1 or 2:

| Check | Result |
|---|---|
| `results/` directory | **absent** |
| `results_v2/` directory | **absent** |
| `results*.json` anywhere in the tree | **0 files** |
| `metadata.json` anywhere in the tree | **0 files** |
| RAW records across all 24 original condition × dataset × seed cells | **0**, per `audit/REPO_INVENTORY.json` |
| SPEC records across the same cells | **0** |
| TRANSCRIPT records across the same cells | **0** |
| `prompts/` (E1/E2 frozen prompts) | **absent — not yet written** |
| `scripts/power_e2.py` (S3 power simulation) | **absent — not yet written** |
| Working tree at hash time | clean at `e36c745`, except the new and modified S2b files |

No experiment in any revision — E1, E2 or E3 — has been run in any part. No model
served, no generation produced, no benchmark table queried, no analysis script
written. No hardware provisioned and no ML dependency installed in this session
or either of the previous two.

**Known near-matches, recorded so the sweep stays reproducible.** A filesystem
sweep for `*spec*.json` and `*transcript*` returns exactly three paths on every
run, none of which is experimental data. If a future sweep returns anything other
than these three, that is a finding:

1. `paper/figures/tab_transcript.tex` — a 432-byte **rendered LaTeX table**
   present since the initial import (`fa692af`), reporting the
   zero-causal-attribution *summary*. The underlying transcripts remain absent,
   consistent with the 0-TRANSCRIPT census.
2. `research/temp/claims-230401910-on-the-variance-of-neural-network-training-with-respect-to-test-sets-a.json`
   — a hyperresearch claims JSON, matching `*spec*` through the word
   "re**spec**t" in the paper's title.
3. `audit/HR_PARTIAL/research/temp/claims-230401910-…-with-respect-to-test-sets-a.json`
   — the archived copy of the same file, matching for the same reason.

The pre-existing absence of the *original* experiment's data is a separate fact,
established in S0 and closed as unrecoverable by operator decision (OA-1). It is
recorded here because it is the reason this plan is a rebuild rather than a
re-analysis: no prior dataset exists in the repository that any revision could
have been tuned against.

---

## What the revision-3 hash binds

`EXPERIMENT_PLAN_R3.md` is not edited after this hash. Specifically, all of the
following are fixed as of `be61bda9…`:

- the thesis and the novelty constraint (§1.1–1.2);
- the abandoned-claims list (§1.3);
- the six proposed claims and their refutation conditions (§1.4);
- E1's factor grid, cell count, **16 batches × 20 generations = 320 per cell**,
  the sixteen-entry seed vector, the ceiling table justifying *B* = 16, the
  diversity metric, the bootstrap parameters (10,000 BCa resamples,
  `bootstrap_seed = 90210`, resampling unit = generation), the surface-diversity
  measure S with its interpretation table and hard constraints, the five-rival
  prediction table, and the numeric classification thresholds (§2.1–2.7);
- E2's arms, **`R_final = max(20, the S3-confirmed value)`**, all three tasks with
  CIFAR-100 primary, the primary estimand, permutation inference, effect-size
  choice, MDE anchor, stopping rule, and the budget formula `9,600 + 320·R`
  (§3.1–3.5);
- E3's proxy set, statistics, the four mandatory caveats and the one prohibition
  (§4.1–4.5);
- the analysis protocol: every named statistic including A16–A20,
  **FAMILY_SIZE = 16**, **ALPHA = 0.003125**, **gate 1** (family and alpha) and
  **gate 2** (the fatal permutation floor, plan-load and run-time arms), the
  results-file schema at `schema_version 1.2.0`, and the no-unplanned-analyses
  rule (§5.1–5.5);
- the scope-protection rules, the rejected calendar consideration, and the
  amended R clause (§8).

Any departure is logged in `DEVIATIONS.md` **before the affected analysis is
run**, per §5.6 rules 1–5. `DEVIATIONS.md` contains no deviation entries as of
this hash.

**No revision 4 after G2 is signed.** If revision 3 must be superseded *before*
the gate is signed, revision 4 is a new file with its own hash recorded below,
citing `be61bda9…` as the version it supersedes, and all three earlier files
remain byte-identical.

---

## Revision history

| Revision | File | SHA-256 | Hashed at | Supersedes |
|---|---|---|---|---|
| 1 | `EXPERIMENT_PLAN.md` | `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` | 2026-08-17T05:10:13Z | — |
| 2 | `EXPERIMENT_PLAN_R2.md` | `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1` | 2026-08-17T09:25:13Z | revision 1 (`aeb174ff…bad3d`) |
| **3** | `EXPERIMENT_PLAN_R3.md` | `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03` | 2026-08-17T09:45:06Z | revision 2 (`a9954ba3…1df1`) |

**Governing revision: 3. Last pre-data revision.**
