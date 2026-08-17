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

## Current stage: **S2 complete — awaiting G2 signature**

S0 audit complete (G0 unsigned). S1 positioning complete (G1 recorded PASSED on
operator authorisation, unsigned). S2 produced the pre-registered experiment plan
and froze it.

---

## The thesis

> In LLM-guided neural architecture search, reported effects of feedback are
> substantially attributable to properties of the measurement apparatus rather
> than properties of the model.

**Novelty is the APPLICATION, not the mechanism.** The general mechanism —
structured decoding and output repair distorting what is measured about a model
— is published 2024–2026 literature. Its instantiation in LLM-guided NAS is not.
Any downstream sentence claiming the mechanism is a defect
(`EXPERIMENT_PLAN.md` §1.2).

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

### S2 — claim surgery and pre-registration *(this session)*
- **`EXPERIMENT_PLAN.md`** — 948 lines. Thesis + binding novelty constraint;
  8 abandoned claims each tied to the S0/S1 finding that killed it; 6 proposed
  claims with refutation conditions; E1 (30-cell discrimination factorial, 3,000
  generations, five-rival falsifier set with numeric thresholds), E2 (4 arms ×
  R=20 runs on NAS-Bench-201, permutation inference, Cliff's δ), E3 (proxy
  size-confound replication on NAS-Bench-Suite-Zero's public 1.5M evaluations);
  analysis protocol with FAMILY_SIZE=16 and ALPHA=0.003125 enforced in code;
  results-file schema; citation obligations; explicit non-scope.
- **`PREREGISTRATION.md`** — SHA-256
  `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d`, taken
  2026-08-17T05:10:13Z, with the checked no-data-collected statement.
- **`DEVIATIONS.md`** — created, zero entries, log-before-run protocol in force.
- `GATES.md` — G1 recorded PASSED on operator authorisation; G2 criterion
  replaced (the replacement, and the fact that replacing a criterion mid-ladder
  violates the file's own rule, are both recorded there) and its evidence filled.
- `VENUE.md` — venue selected and its CFP fields recorded; OA-26 closed at
  8 pages.
- `audit/OPEN_ACTIONS.md` — OA-37 (C6 thread) and OA-38 (missing bib entries)
  opened; OA-5 and OA-26 dispositions recorded.

**No compute was used. No model was trained or called, no hardware provisioned,
no ML dependency installed.**

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

## ⏰ Time

**Deadline 2026-08-29 AoE — 12 days.** The plan specifies ≈9,400 generations and
zero training runs. Whether that fits depends on hardware not yet provisioned
(an S3/S4 question, flagged, not resolved).

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
