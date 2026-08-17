# PRE-REGISTRATION

## Governing artifact

**File:** `EXPERIMENT_PLAN_R4.md` — **revision 4, the governing plan**
**SHA-256:** `738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d`
**Length:** 1,653 lines
**Hashed at:** 2026-08-17T18:25:00Z (2026-08-17 23:55 IST)

**FAMILY_SIZE = 17. ALPHA = 0.05 / 17 = 0.0029411764705882353.**
*(Revisions 1–3 registered 16 and 0.003125. Revision 4 adds exactly one
confirmatory test, X5, and the alpha follows.)*

**The revision route closes at the END OF S3**, when the analysis code exists and
G2 is signed against a plan that has been executed rather than only read. That
ordering is what S3a established: revision 3 declared itself final on the
assumption the gate would be signed next, and an implementation pass then found
25 defects in it. Until the end of S3, this plan remains amendable by a further
numbered revision.

Verify the whole chain with:

```bash
shasum -a 256 EXPERIMENT_PLAN.md EXPERIMENT_PLAN_R2.md \
              EXPERIMENT_PLAN_R3.md EXPERIMENT_PLAN_R4.md
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
  revision 3  be61bda9…df03    EXPERIMENT_PLAN_R3.md   2026-08-17T09:45:06Z
        │
        ▼  §5.6 rule 4      (S3a implementation pass: 25 defects, 7 blocking)
  revision 4  738601db…cc9d    EXPERIMENT_PLAN_R4.md   2026-08-17T18:25:00Z  ← GOVERNING
```

Revisions 1, 2 and 3 remain in the repository **byte-identical to the versions
that were hashed**. None was edited, amended in place, or deleted. All three
hashes were re-verified immediately before revision 4 was written and again after
it was committed, and matched on both occasions.

Each step was taken under the rule the *preceding* revision carried:

> **§5.6 rule 4** — *"This plan is not edited after its hash is taken. Changes go
> in `DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
> written as a new file, hashed separately, and cites the prior hash it
> supersedes; every superseded plan file stays in the repository byte-identical
> to the version that was hashed."*

Each revision is a **wholesale successor**: self-contained, carrying the full plan
with the amendments folded in, so no reader reconciles four documents to know what
is registered. Revision 4 cites revision 3's hash in its masthead and carries the
full chain in its results-file schema (`plan_supersedes_sha256`,
`plan_chain_sha256`). Section numbering is preserved across all four; §2.8 and §9
are new at revision 4 and append.

### What changed, revision 3 → revision 4

Driven by `audit/S3A_IMPLEMENTATION_DEFECTS.md` — 25 defects found by building the
measurement instrument and running it against the plan.

| ID | Amendment |
|---|---|
| **R4-1** | **Anchor-tracking manipulation** (new §2.8): enumeration order {canonical, reversed} × in-context exemplar {modal, non-modal} at the anchor configuration, 4 cells × 16 × 20. New outcome `anchor_tracking`, a sixth prediction column, and one new confirmatory contrast **X5**. **FAMILY_SIZE 16 → 17; ALPHA → 0.05/17.** Separates `format tax` from `genuine prior` without depending on free-prose parsing. |
| **R4-2** | **`generations[]`** added to the schema at generation level; `contrast_operands`, `pairing_key` and `test_statistic` added to statistics; **`results/` removed from `.gitignore`**; size management registered. |
| **R4-3** | **D_rand redefined** from a corrected uniform sampler at fixed block count — **0.719205** (analytic 0.718872). The repository's sampler reported separately as **D_repo_sampler = 0.771931**. Sanity range tightened from [0.65, 0.80] to **[0.705, 0.735]**. |
| **R4-4** | Remaining blocking and material defects resolved explicitly: `partial` given a ΔD band; `worsens` named; frontier precision substitution; indeterminate rescaling generalised to *k* columns; E2's permutation statistic, tie convention, jackknife and tie-break all named. |
| **R4-5** | **Full discreteness table re-run at ALPHA = 0.05/17. Every floor clears.** |

A defect-by-defect disposition for all 25 is in **§9** of the plan.

---

## Statement of data status at the time of the revision-4 hash

**No data has been collected as of this hash.** Re-verified independently — a
fresh sweep, not carried forward from any earlier revision:

| Check | Result |
|---|---|
| `results_v2/` directory | **absent** |
| `results*.json` (experimental) | **0 files** |
| `metadata.json` anywhere in the tree | **0 files** |
| RAW records across all 24 original condition × dataset × seed cells | **0**, per `audit/REPO_INVENTORY.json` |
| SPEC records across the same cells | **0** |
| TRANSCRIPT records across the same cells | **0** |
| `prompts/` (E1/E2 frozen prompts) | **absent — not yet written** |
| `scripts/power_e2.py` (S3 power simulation) | **absent — not yet written** |

**`results/` is now a tracked directory** (R4-2, defect D-25) and contains two
files. **Neither is experimental data, and both are model-free:**

1. `results/E1_reference.json` — the D_rand computation. Produced by
   `tests/compute_d_rand_r4.py` from a corrected uniform sampler and from the
   repository's own sampler. **No model is involved at any point**; it is
   arithmetic over pseudo-random draws from a declared vocabulary.
2. `results/_fixture_E1.json` — the S3a replay-test fixture. Synthetic, produced
   by `tests/test_replay.py` to prove which schema fields can be recomputed from
   their own stored inputs. Contains no generated text and no model output.

No experiment in any revision — E1, E2 or E3 — has been run in any part. No model
served, no generation produced, no benchmark table queried. No hardware
provisioned and no ML dependency installed in this session or any of the previous
four. `torch` remains absent, which is why the repository's sampler is executed by
verbatim `ast` source extraction (defect D-11, now the registered method).

**Known near-matches, recorded so the sweep stays reproducible.** A sweep for
`*spec*.json` and `*transcript*` returns exactly three paths, none of them
experimental data. Anything other than these three in a future sweep is a finding:

1. `paper/figures/tab_transcript.tex` — a 432-byte **rendered LaTeX table**
   present since the initial import (`fa692af`), reporting the
   zero-causal-attribution *summary*. The underlying transcripts remain absent.
2. `research/temp/claims-230401910-…-with-respect-to-test-sets-a.json` — a
   hyperresearch claims JSON, matching `*spec*` through "re**spec**t" in a title.
3. `audit/HR_PARTIAL/research/temp/claims-230401910-…json` — the archived copy.

The pre-existing absence of the *original* experiment's data is a separate fact,
established in S0 and closed as unrecoverable by operator decision (OA-1). It is
the reason this plan is a rebuild rather than a re-analysis: no prior dataset
exists that any revision could have been tuned against.

---

## What the revision-4 hash binds

- the thesis and the novelty constraint, including the new statement that order
  and exemplar effects are **prior art, not a claim** (§1.1–1.2);
- the abandoned-claims list (§1.3) and the six proposed claims with their
  refutation conditions (§1.4);
- E1's factor grid, **34 cells**, 16 batches × 20 generations, the sixteen-entry
  seed vector, the ceiling table at the new alpha, the diversity metric, the
  bootstrap parameters, S, and **the §2.8 anchor-tracking sub-design with its
  four cells, its `tracks_first` / `tracks_exemplar` outcomes and its five rival
  predictions** (§2.1–2.8);
- the **six-column** prediction table and the full label vocabulary — `collapsed`,
  `reduced`/`partial` at level, `no chg`, `partial`, `recovers`, `worsens` at
  change, and `tracks` / `no tracking` / `indeterminate` — with every numeric
  threshold at **D_rand = 0.719205** (§2.5–2.6);
- the generalised signature-scoring rule: winner needs ≥ ceil(0.75 · n_scoreable),
  `n_s < 4` → no verdict (§2.6);
- E2's arms, `R_final = max(20, S3-confirmed)`, all three tasks with CIFAR-100
  primary, the **difference-of-means** permutation statistic, the **universal**
  tractability cut of 10⁷, the Cliff's δ tie convention, the leave-one-run-out
  BCa jackknife, and the lowest-index validation tie-break (§3.1–3.5);
- E3's proxy set, statistics, four mandatory caveats and one prohibition
  (§4.1–4.5);
- the analysis protocol: every named statistic including X5 and A21,
  **FAMILY_SIZE = 17**, **ALPHA = 0.0029411764705882353**, gate 1, gate 2's
  plan-load and run-time arms, the `permutation_mode` enum, the schema at
  **`schema_version` 1.3.0** with `generations[]`, and the no-unplanned-analyses
  rule (§5.1–5.5);
- the scope-protection rules, now foreclosing removal of the §2.8 sub-design
  (§8);
- the defect disposition for all 25 S3a findings (§9).

Any departure is logged in `DEVIATIONS.md` **before the affected analysis is
run**, per §5.6 rules 1–5. `DEVIATIONS.md` contains no deviation entries as of
this hash.

If revision 4 must be superseded before the end of S3, revision 5 is a new file
with its own hash recorded below, citing `738601db…cc9d`, and all four earlier
files remain byte-identical.

---

## Revision history

| Revision | File | SHA-256 | Hashed at | FAMILY_SIZE / ALPHA | Supersedes |
|---|---|---|---|---|---|
| 1 | `EXPERIMENT_PLAN.md` | `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` | 2026-08-17T05:10:13Z | 16 / 0.003125 | — |
| 2 | `EXPERIMENT_PLAN_R2.md` | `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1` | 2026-08-17T09:25:13Z | 16 / 0.003125 | rev 1 |
| 3 | `EXPERIMENT_PLAN_R3.md` | `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03` | 2026-08-17T09:45:06Z | 16 / 0.003125 | rev 2 |
| **4** | `EXPERIMENT_PLAN_R4.md` | `738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d` | 2026-08-17T18:25:00Z | **17 / 0.0029411764705882353** | rev 3 |

**Governing revision: 4. The revision route closes at the end of S3.**
