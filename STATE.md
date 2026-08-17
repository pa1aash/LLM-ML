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

## Current stage: **S2 complete, amended (S2a) — awaiting G2 signature**

S0 audit complete (G0 unsigned). S1 positioning complete (G1 recorded PASSED on
operator authorisation, unsigned). S2 produced the pre-registered experiment plan
and froze it. **S2a amended the plan before any data collection, as revision 2.**

**Governing plan: `EXPERIMENT_PLAN_R2.md`** (revision 2), SHA-256
`a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1`, hashed
2026-08-17T09:25:13Z. It supersedes `EXPERIMENT_PLAN.md` (revision 1,
`aeb174ff…bad3d`), which remains in the repository **byte-identical** and
re-verified. The successor route is what revision 1 §5.6 rule 4 requires; the
plan is never edited in place.

---

## The thesis

> In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.

**Novelty is the APPLICATION, not the mechanism.** The general mechanism —
structured decoding and output repair distorting what is measured about a model
— is published 2024–2026 literature. Its instantiation in LLM-guided NAS is not.
Any downstream sentence claiming the mechanism is a defect
(`EXPERIMENT_PLAN_R2.md` §1.2).

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

### S2a — plan amendment *(this session)*

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

**No compute was used in S2 or S2a. No model trained or called, no hardware
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

**Recorded as CONSIDERED AND REJECTED at S2a** (`EXPERIMENT_PLAN_R2.md` §8).
The nearest workshop deadline is 2026-08-29 AoE and the plan specifies ≈12,400
generations with zero training runs. **The venue follows the artifact, not the
reverse.** The chosen venue is non-archival, so missing a cycle costs nothing —
no priority, no publication window, no claim to the result — and workshop cycles
recur, whereas a design weakened to fit a date is permanent.

The precedent is already set: S2a *raised* the budget by 3,000 generations on
rigour grounds, because that is what made E1's confirmatory tests decidable.
§8.2 lists what may not be proposed as a scope cut on schedule grounds. Scope
changes on **methodological** grounds remain available at any time.

## Open

- **G0, G1, G2 all await operator signature.** G1 and G2 have complete evidence;
  G0's recommendation is in `audit/SESSION_1_REPORT.md` §8. Never self-sign.
- **38 open actions**, `audit/OPEN_ACTIONS.md`. Blocking before S6: **OA-37**
  (CoLLM-NAS replication status, five unverified leads) and **OA-38** (8 of 15
  obliged citations absent from `references_verified.bib`).
- **S3 must run before any data collection**: measure `D_rand`; run
  `scripts/power_e2.py` and confirm or raise R **before** any run; select and pin
  the frontier API model; freeze and hash the E1/E2 prompts; fix and test OA-10
  through OA-17; complete the GENIUS Appendix A.3 pass left open by seam S3.
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
