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

## Current stage: **S2 complete at revision 3 — awaiting G2 signature**

S0 audit complete (G0 unsigned). S1 positioning complete (G1 recorded PASSED on
operator authorisation, unsigned). S2 produced the pre-registered experiment plan
and froze it; **S2a** amended it as revision 2 and **S2b** as revision 3, both
before any data collection.

**Governing plan: `EXPERIMENT_PLAN_R3.md`** (revision 3), SHA-256
`be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03`, hashed
2026-08-17T09:45:06Z.

```
  rev 1  aeb174ff…bad3d  EXPERIMENT_PLAN.md      05:10:13Z
    │ §5.6 rule 4
  rev 2  a9954ba3…1df1   EXPERIMENT_PLAN_R2.md   09:25:13Z
    │ §5.6 rule 4
  rev 3  be61bda9…df03   EXPERIMENT_PLAN_R3.md   09:45:06Z   ← GOVERNING
```

Revisions 1 and 2 remain in the repository **byte-identical**; both hashes were
re-verified before revision 3 was written and again after it was committed. The
successor route is what §5.6 rule 4 requires — the plan is never edited in place.

**Revision 3 is the last pre-data revision.** Once G2 is signed the revision
route closes and every change is a `DEVIATIONS.md` entry logged before the
affected analysis runs.

---

## The thesis

> In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.

**Novelty is the APPLICATION, not the mechanism.** The general mechanism —
structured decoding and output repair distorting what is measured about a model
— is published 2024–2026 literature. Its instantiation in LLM-guided NAS is not.
Any downstream sentence claiming the mechanism is a defect
(`EXPERIMENT_PLAN_R3.md` §1.2).

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

### S2b — plan amendment (revision 3) *(this session)*

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

**No compute was used in S2, S2a or S2b. No model trained or called, no hardware
provisioned, no ML dependency installed.**

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
(`EXPERIMENT_PLAN_R3.md` §8). The nearest workshop deadline is 2026-08-29 AoE and
the plan now specifies **9,600 + 320·R** generations — 16,000 at the R floor of
20 — with zero training runs. **The venue follows the artifact, not the reverse.**
The chosen venue is non-archival, so missing a cycle costs nothing — no priority,
no publication window, no claim to the result — and workshop cycles recur,
whereas a design weakened to fit a date is permanent.

**Every revision has raised the budget, not lowered it** — 9,400 → 12,400 →
16,000 at the floor — each time because that is what made a confirmatory test
decidable. That is the precedent §8 fixes. §8.2 lists what may not be proposed as
a scope cut on schedule or budget grounds, now including any reduction of *B*
below 16, which must argue against the ceiling table rather than against cost.
Scope changes on **methodological** grounds remain available; before G2 they are
a further revision, after G2 a `DEVIATIONS.md` entry.

## Open

- **G0, G1, G2 all await operator signature.** G1 and G2 have complete evidence;
  G0's recommendation is in `audit/SESSION_1_REPORT.md` §8. Never self-sign.
- **38 open actions**, `audit/OPEN_ACTIONS.md`. Blocking before S6: **OA-37**
  (CoLLM-NAS replication status, five unverified leads) and **OA-38** (8 of 15
  obliged citations absent from `references_verified.bib`).
- **S3 must run before any data collection**: measure `D_rand`; run
  `scripts/power_e2.py` and **set `R_final = max(20, its output)`** — raising R to
  meet it is compliance, not a deviation (§3.4); select and pin the frontier API
  model; freeze and hash the E1/E2 prompts; **implement gate 2 and confirm it
  passes at plan-load** (§5.2); fix and test OA-10 through OA-17; complete the
  GENIUS Appendix A.3 pass left open by seam S3.
- **The generation budget is not yet a fixed number.** It is `9,600 + 320·R`,
  and R is set by the S3 simulation with a floor of 20 — 16,000 at the floor,
  more if the simulation demands it. The plan does not cap it (§3.5, §8.2).
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
