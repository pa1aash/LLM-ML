# PRE-REGISTRATION

## Governing artifact

**File:** `EXPERIMENT_PLAN_R2.md` — **revision 2, the governing plan**
**SHA-256:** `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1`
**Length:** 1,323 lines
**Hashed at:** 2026-08-17T09:25:13Z (2026-08-17 14:55 IST)

**Supersedes:** `EXPERIMENT_PLAN.md` — revision 1
**Superseded SHA-256:** `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d`
**Revision 1 hashed at:** 2026-08-17T05:10:13Z

Verify both with:

```bash
shasum -a 256 EXPERIMENT_PLAN.md EXPERIMENT_PLAN_R2.md
```

---

## Supersession relation

Revision 1 remains in the repository **byte-identical to the version that was
hashed**. It was not edited, amended in place, or deleted. Its hash was
re-verified at the moment revision 2 was hashed and matches
`aeb174ff…bad3d` exactly.

This is the procedure revision 1 itself specified, and revision 2 was written
under it rather than under any alternative:

> **§5.6 rule 4** — *"This plan is not edited after its hash is taken. Changes go
> in `DEVIATIONS.md`. If the plan is superseded wholesale, a numbered revision is
> written as a new file, hashed separately, and cites the prior hash it
> supersedes; the original file remains in the repository unmodified."*

Revision 2 is a **wholesale successor**: self-contained, carrying the full plan
with the amendments folded in, so no downstream reader has to reconcile two
documents to know what is registered. It cites the superseded hash in its own
masthead and in its results-file schema (`plan_supersedes_sha256`). Section
numbering is preserved from revision 1, so every existing cross-reference in
`GATES.md`, `STATE.md`, `VENUE.md` and `audit/OPEN_ACTIONS.md` resolves to the
same content; §8 is new and appends.

Rule 4 is carried forward unchanged as revision 2 §5.6 rule 4 and governs any
revision 3.

### What changed, revision 1 → revision 2

| ID | Amendment |
|---|---|
| **A1** | E1 batches per cell 5 → **10** (n = 200 per cell; **6,000** E1 generations; total budget 9,400 → **12,400**). Shared seed vector extended to `[7001…7010]`. |
| **A2** | Within-cell **BCa bootstrap interval on D**, and on ΔD for the two change columns. Secondary resolution check; the paired batch-index contrast remains primary. |
| **A3** | Parse-free **surface diversity S** on raw generated text (token 3-gram Jaccard). Secondary only; never substituted into D, never confirmatory; bounds the free-prose parse-selection effect. |
| **A4** | E2 **retains all three tasks**, with the retention reasoning recorded. |
| **A5** | The calendar consideration recorded as **CONSIDERED AND REJECTED** (new §8). |
| **A6** | Confirmatory family **unchanged at 16, ALPHA unchanged at 0.003125**. |

---

## Statement of data status at the time of the revision-2 hash

**No data has been collected as of this hash.** Re-verified at
2026-08-17T09:18:00Z, immediately before hashing, not carried forward from
revision 1:

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
| Working tree at hash time | clean at `2fa51cd`, except the new and modified S2a files |

No experiment in either revision — E1, E2 or E3 — has been run in any part. No
model has been served, no generation produced, no benchmark table queried, no
analysis script written. No hardware provisioned and no ML dependency installed
in this session or the previous one.

**One near-match, checked and cleared.** A filesystem sweep for `*spec*.json` and
`*transcript*` returns three paths, none of which is experimental data:
`paper/figures/tab_transcript.tex` is a 432-byte **rendered LaTeX table** present
since the initial import (`fa692af`), reporting the zero-causal-attribution
*summary* — the underlying transcripts remain absent, consistent with the
0-TRANSCRIPT census; the other two are hyperresearch claims JSONs matching
`*spec*` through the word "respect" in a paper title. Recorded so the sweep is
reproducible and the exception is not mistaken for a finding.

The pre-existing absence of the *original* experiment's data is a separate fact,
established in S0 and closed as unrecoverable by operator decision (OA-1). It is
recorded here because it is the reason this plan is a rebuild rather than a
re-analysis: no prior dataset exists in the repository that any part of either
revision could have been tuned against.

---

## What the revision-2 hash binds

`EXPERIMENT_PLAN_R2.md` is not edited after this hash. Specifically, all of the
following are fixed as of `a9954ba3…`:

- the thesis and the novelty constraint (§1.1–1.2);
- the abandoned-claims list (§1.3);
- the six proposed claims and their refutation conditions (§1.4);
- E1's factor grid, cell count, **10 batches × 20 generations = 200 per cell**,
  the ten-entry seed vector, the diversity metric, the bootstrap parameters
  (10,000 BCa resamples, `bootstrap_seed = 90210`, resampling unit = generation),
  the surface-diversity measure S and its interpretation and hard constraints,
  the five-rival prediction table, and the numeric classification thresholds
  (§2.1–2.7);
- E2's arms, R = 20, all three tasks with CIFAR-100 primary, the primary
  estimand, permutation inference, effect-size choice, MDE and stopping rule
  (§3.1–3.5);
- E3's proxy set, statistics, the four mandatory caveats and the one prohibition
  (§4.1–4.5);
- the analysis protocol: every named statistic including A16–A19,
  **FAMILY_SIZE = 16**, **ALPHA = 0.003125**, the `min_attainable_p` reporting
  rule, the results-file schema at `schema_version 1.1.0`, and the
  no-unplanned-analyses rule (§5.1–5.5);
- the scope-protection rules and the rejected calendar consideration (§8).

Any departure from any of the above is logged in `DEVIATIONS.md` **before the
affected analysis is run**, per §5.6 rules 1–5. `DEVIATIONS.md` contains no
deviation entries as of this hash.

If revision 2 is superseded wholesale, revision 3 is a new file with its own hash
recorded in the table below, citing `a9954ba3…` as the version it supersedes.
Both earlier files remain byte-identical.

---

## Revision history

| Revision | File | SHA-256 | Hashed at | Supersedes |
|---|---|---|---|---|
| 1 | `EXPERIMENT_PLAN.md` | `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d` | 2026-08-17T05:10:13Z | — |
| **2** | `EXPERIMENT_PLAN_R2.md` | `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1` | 2026-08-17T09:25:13Z | revision 1 (`aeb174ff…bad3d`) |

**Governing revision: 2.**
