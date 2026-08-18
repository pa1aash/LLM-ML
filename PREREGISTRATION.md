# PRE-REGISTRATION

## Governing artifact

**File:** `EXPERIMENT_PLAN_R6.md` — **revision 6, the governing plan**
**SHA-256:** `d63a7625f06dcbaa08ad35182490036de12c3d0354febee9e141656ec79d340b`
**Length:** 2,276 lines
**Hashed at:** 2026-08-18T04:35:00Z (2026-08-18 10:05 IST)

**Revision 6 is the last revision before G2.** Its scope was closed by
construction: the two pilot-confirmed design parameters, the cross-level exemplar
predicate, and the corrected pilot criterion. Nothing else. Every other ambiguity
S3c found is in `audit/S3C_DEFECTS.md` and is handled after G2 as a
`DEVIATIONS.md` implementation decision.

**FAMILY_SIZE = 17. ALPHA = 0.05 / 17 = 0.0029411764705882353.**
*(Unchanged from revision 4. Revision 5 extends the tracking sub-design to all
three models but adds no confirmatory test — column classification is descriptive
by CI position, not a hypothesis test.)*

**Design parameters, both pilot-confirmed:** `R_final = 24` (power at the floor
of 20 is 0.702, below target) and `B_tracking = 28` (binding on the cross-level
delta). **Total budget: 24,000 generations, zero training runs.**

**The revision route closes at G2.** It has caught defects four times: 25 at S3a,
18 at S3b, three inside revision 5's own drafting, and the miscalibrated
`B_tracking` criterion this session.

Verify the whole chain with:

```bash
shasum -a 256 EXPERIMENT_PLAN.md EXPERIMENT_PLAN_R2.md EXPERIMENT_PLAN_R3.md \
              EXPERIMENT_PLAN_R4.md EXPERIMENT_PLAN_R5.md EXPERIMENT_PLAN_R6.md
```

---

## Supersession chain

```
  revision 1  aeb174ff…bad3d   EXPERIMENT_PLAN.md      2026-08-17T05:10:13Z   16 / 0.003125
        │  §5.6 rule 4
  revision 2  a9954ba3…1df1    EXPERIMENT_PLAN_R2.md   2026-08-17T09:25:13Z   16 / 0.003125
        │  §5.6 rule 4
  revision 3  be61bda9…df03    EXPERIMENT_PLAN_R3.md   2026-08-17T09:45:06Z   16 / 0.003125
        │  §5.6 rule 4   ← S3a: 25 defects, 7 blocking
  revision 4  738601db…cc9d    EXPERIMENT_PLAN_R4.md   2026-08-17T18:25:00Z   17 / 0.00294
        │  §5.6 rule 4   ← S3b: 18 defects, 5 blocking
  revision 5  e3206e71…b201    EXPERIMENT_PLAN_R5.md   2026-08-18T04:00:00Z   17 / 0.00294
        │  §5.6 rule 4   ← S3c: pilots run, cross-level predicate
  revision 6  d63a7625…d340b   EXPERIMENT_PLAN_R6.md   2026-08-18T04:35:00Z   17 / 0.00294  ← GOVERNING
```

Revisions 1–5 remain **byte-identical to the versions that were hashed**. None was
edited, amended in place, or deleted. All four hashes were re-verified immediately
before revision 6 was written and again after it was committed.

Each step was taken under the rule the *preceding* revision carried:

> **§5.6 rule 4** — *"This plan is not edited after its hash is taken. Changes go
> in `DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
> written as a new file, hashed separately, and cites the prior hash it
> supersedes; every superseded plan file stays in the repository byte-identical
> to the version that was hashed."*

Each revision is a **wholesale successor**: self-contained, so no reader
reconciles six documents. Revision 5 cites revision 4's hash in its masthead and
carries the full chain in its results-file schema. Section numbering is preserved
across all five; §9 is new at revision 5 and §10 is revision 4's §9 renumbered.

### What changed, revision 5 → revision 6

| ID | Amendment |
|---|---|
| **R6-1** | **`R_final = 24`, `B_tracking = 28`** — both pilot-confirmed. |
| **R6-2** | **The cross-level exemplar predicate** (new §2.5a). Registered as descriptive; adds no confirmatory test. |
| **R6-3** | **The `B_tracking` pilot criterion corrected** — the registered half-width test would have certified a width that cannot detect the effect. |

### What changed, revision 4 → revision 5

Driven by `audit/S3B_SCORER_DEFECTS.md` — 18 defects found by implementing the two
scorers that decide C2 and running them against 22 synthetic fixture assertions.

| ID | Amendment |
|---|---|
| **R5-1** | **One-sided per-field chance rule** registered for anchor tracking. The flat 0.50 bar and the symmetric per-field rule are both rejected, with the measured disagreement table as evidence. |
| **R5-2** | Tracking sub-design runs at **all three models** (12 cells). **X5 stays one contrast; FAMILY_SIZE stays 17.** |
| **R5-3** | **`tracks_{first,exemplar}_pre_mean` and `_ci95` registered at cell level** — without them the column could not be scored at all. |
| **R5-4** | Field-collapse threshold registered (normalised entropy < 0.15); both tracking denominators stated. |
| **R5-5** | Five tracking predicates written as explicit grid predicates; every rival states a value for every grid entry. |
| **R5-6** | Indeterminacy may create winners; the verdict carries `contingent_on_indeterminacy` rather than the behaviour being prevented. |
| **R5-7** | The level columns' inability to falsify recorded as a KNOWN LIMITATION. |
| **R5-8** | **`B_tracking = max(16, S3 pilot value)`**, floor 16, raising it is compliance. |
| **R5-9** | Block D coverage gaps closed; schema → **1.4.0**. |
| **R5-10** | Bootstrap units per statistic, the `recovers` demotion, the CI boundary, the prose/rule mismatch. |
| **R5-11** | **Full discreteness table re-run for all 17 tests. Every floor clears.** |

Three further defects were found in revision 5's **own** drafting and closed
before freezing (plan §9): the **(canonical, modal) degenerate cell**, the
**no-collapse-means-no-tracking** rule, and the **logically unsatisfiable
conjunction** in the format-tax predicate.

---

## Statement of data status at the time of the revision-5 hash

**No data has been collected as of this hash.** Re-verified independently:

| Check | Result |
|---|---|
| `results_v2/` directory | **absent** |
| experimental `results*.json` | **0 files** |
| `metadata.json` anywhere in the tree | **0 files** |
| RAW / SPEC / TRANSCRIPT across all 24 original cells | **0 / 0 / 0**, per `audit/REPO_INVENTORY.json` |
| `prompts/` (E1/E2 frozen prompts) | **absent — not yet written** |
| `scripts/power_e2.py` (S3 power simulation) | **absent — not yet written** |

`results/` is tracked and holds **model-free** files only, none of them
experimental data: `E1_reference.json` (the D_rand arithmetic), `_fixture_E1.json`
(the S3a replay fixture), and `results/pilots/` — the two S3c pilots, each marked
`pilot: true`, `confirmatory: false`, `quarantined_from_analysis: true`. **The
pilots are simulation over synthetic draws and set design parameters only**; they
may not be analysed for any claim and never enter the confirmatory corpus.

No experiment in any revision — E1, E2 or E3 — has been run in any part. No model
served, no generation produced, no benchmark table queried. No hardware
provisioned and no ML dependency installed in this session or any of the previous
six. `torch` remains absent, which is why the repository's sampler is executed by
verbatim `ast` source extraction.

**Known near-matches**, recorded so the sweep stays reproducible — a sweep for
`*spec*.json` and `*transcript*` returns exactly three paths, none experimental
data: `paper/figures/tab_transcript.tex` (a 432-byte rendered LaTeX table present
since `fa692af`), and two hyperresearch claims JSONs matching `*spec*` through
"re**spec**t" in a paper title.

The pre-existing absence of the *original* experiment's data is a separate fact,
closed as unrecoverable by operator decision (OA-1). No prior dataset exists that
any revision could have been tuned against.

---

## What the revision-5 hash binds

- the thesis, the novelty constraint, the abandoned claims and the six proposed
  claims with their refuting observations (§1);
- E1's **42 cells**, 16 batches × 20 for the main grid, `B_tracking` for the 12
  tracking cells, the seed vector, the ceiling table, D, S, the **field-collapse
  threshold**, and both tracking denominators (§2.1–2.4);
- the **six-column** prediction table with the **three explicit grid predicates**,
  the degenerate-cell rule, the no-collapse rule, and the KNOWN LIMITATION on the
  level columns (§2.5);
- the full label vocabulary and the **one-sided at-chance** tracking rule with its
  per-field chance rates, the widened `partial` band, the generalised scoring
  threshold and `contingent_on_indeterminacy` (§2.6);
- E2's arms, `R_final`, the difference-of-means statistic, the universal
  tractability cut, tie conventions and jackknife (§3);
- E3 unchanged (§4);
- **FAMILY_SIZE = 17**, **ALPHA = 0.0029411764705882353**, gate 1, gate 2's two
  arms, the schema at **`schema_version` 1.4.0**, and the no-unplanned-analyses
  rule (§5);
- the scope-protection rules, now foreclosing narrowing the sub-design back to one
  model and reducing `B_tracking` (§8);
- the defect dispositions for the 18 from S3b (§9) and the 25 from S3a (§10).

Any departure is logged in `DEVIATIONS.md` **before the affected analysis is
run**. `DEVIATIONS.md` contains no deviation entries as of this hash.

---

## Revision history

| Revision | File | SHA-256 | Hashed at | FAMILY_SIZE / ALPHA | Supersedes |
|---|---|---|---|---|---|
| 1 | `EXPERIMENT_PLAN.md` | `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` | 2026-08-17T05:10:13Z | 16 / 0.003125 | — |
| 2 | `EXPERIMENT_PLAN_R2.md` | `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1` | 2026-08-17T09:25:13Z | 16 / 0.003125 | rev 1 |
| 3 | `EXPERIMENT_PLAN_R3.md` | `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03` | 2026-08-17T09:45:06Z | 16 / 0.003125 | rev 2 |
| 4 | `EXPERIMENT_PLAN_R4.md` | `738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d` | 2026-08-17T18:25:00Z | 17 / 0.0029411764705882353 | rev 3 |
| 5 | `EXPERIMENT_PLAN_R5.md` | `e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201` | 2026-08-18T04:00:00Z | 17 / 0.0029411764705882353 | rev 4 |
| **6** | `EXPERIMENT_PLAN_R6.md` | `d63a7625f06dcbaa08ad35182490036de12c3d0354febee9e141656ec79d340b` | 2026-08-18T04:35:00Z | **17 / 0.0029411764705882353** | rev 5 |

**Governing revision: 6. The last revision before G2.**
