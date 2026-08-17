# GATES

One section per gate on the S0–S7 ladder. **Each criterion is written before the
work it governs.** Evidence is filled in when the work completes. The operator
signs; the gate is not passed until signed.

> **Rule: never self-sign.** An unsigned gate is an open gate regardless of how
> complete the evidence looks.

---

## G0 — Ground truth

**Criterion** *(written before Blocks 2–5)*

> The paper's evidence base is characterised — every headline number classified
> REPRODUCIBLE / PRESENT / ORPHAN, the five forensic questions answered or
> explicitly marked undeterminable, and the reference list verified against
> fetched records.

**Evidence**

| Requirement | Status | Artifact |
|---|---|---|
| Every headline number classified | **Met.** 47 claims traced: 3 REPRODUCIBLE, 30 PRESENT, 14 ORPHAN. Headline surface (abstract + Tables 1–3): 34 claims, 9 ORPHAN = **26%**. | `audit/CLAIM_TRACE.md` |
| F1 generation config | **Answered.** `enable_thinking=False` on both servers; max_new_tokens 2048; `finish_reason` hardcoded `"stop"`; transcripts truncated to 2000 chars; `sanitize_config` silently rewrites malformed output. | `audit/FORENSICS.md` F1 |
| F2 identical-design check | **Answered as undeterminable, with a bounded reconstruction.** Specs absent, so byte comparison is impossible. Jaccard 0.022 ≠ 0 refutes strict identity; Figure 4 values + param std = 0K imply variation in block *ordering*. | `audit/FORENSICS.md` F2 |
| F3 independence | **Answered.** B uses fresh contexts but no RNG control; C and D are sequentially dependent; Welch, Mann–Whitney and the bootstrap all assume independence. | `audit/FORENSICS.md` F3 |
| F4 selection hygiene | **Answered.** Feedback is validation-only — the v2 claim holds. Test accuracy enters via top-5 retrain selection and the convergence figure. Split is per-architecture, not fixed. | `audit/FORENSICS.md` F4 |
| F5 effect sizes and metrics | **Answered.** Pooled-SD *d* against a 1000:1 variance ratio, paired with Welch. Mann–Whitney already computed and reported; Cliff's δ derivable from *U* in principle but `u_stat` was never persisted. | `audit/FORENSICS.md` F5 |
| Reference list verified against fetched records | **Met.** 46/47 resolved (97.9%). 2 FABRICATED, 3 WRONG-METADATA, 1 UNRESOLVED. Both known-bad entries caught independently. | `audit/BIB_AUDIT.md`, `audit/references_verified.bib` |
| Repository characterised | **Met.** 48 files inventoried with SHA-256; data census returns 0 RAW / 0 SPEC / 0 TRANSCRIPT across all 24 condition×dataset×seed cells. | `audit/REPO_INVENTORY.json`, `audit/CONTEXT_PACK.md` |

**Recommendation:** see `audit/SESSION_1_REPORT.md` §8.

**Operator signature:** ______________________  **Date:** ____________

---

## G1 — Position

**Criterion** *(written before the work)*

> The paper's contribution is located against the 2023–2026 literature with a
> defensible novelty claim: it is established whether "feedback degrades
> LLM-guided NAS" is already published or partially scooped, the strongest
> published counter-evidence is identified and answered, and a target venue is
> selected with its call-for-papers requirements recorded.

**Status: PASSED on operator authorisation, 2026-08-17.** Recorded by the S2
session on the operator's instruction, not self-assessed.

**Evidence**

| Requirement | Status | Artifact |
|---|---|---|
| Is "feedback degrades LLM-guided NAS" already published or partially scooped? | **Answered.** The unqualified thesis is **REFUTED** — contradicted by two controlled ablations (RZ-NAS, ICML 2025; EvoPrompting), and unsupported by its own strongest cited ally, GENIUS, whose per-trial Appendix A.3 tables show feedback beating zero-shot in every reported trajectory. The mechanism-specific version is **SCOOPED** by CoLLM-NAS (Oral, CVPR 2026 NAS Workshop), whose Generator-memory ablation reports uncurated in-context history "induces progressive noise accumulation, leading to performance degradation." | `research/notes/interim-report-l1-feedback-degradation-priority.md`, `research/temp/comparisons.md` |
| Strongest published counter-evidence identified and answered | **Met.** RZ-NAS is the strongest counter-case. Answer: its ablation's *internal* validity stands (a confound in a shared signal cannot manufacture a between-arm difference), but its construct validity is narrowed — it refines against a single experimenter-chosen zero-cost proxy, validates rank correlation only on NAS-Bench-201 (the benchmark NAS-Bench-Suite-Zero itself calls the easy case), and never validates on the search spaces its headline claims rest on. | `research/temp/interim-report-L5.md`, `research/temp/comparisons.md` §1 |
| Thesis selected | **Met.** Instrumentation-artifact thesis, framed as the **application** of an established 2024–26 mechanism to LLM-guided NAS, not as discovery of the mechanism. The general mechanism is published (4 sources); the NAS-scoped instantiation is NOT IN CORPUS across a vault sweep and a targeted arXiv wave. | `research/temp/corpus-critic-findings.md` C1; `EXPERIMENT_PLAN_R3.md` §1.1–1.2 |
| Target venue selected with CFP requirements recorded | **Met.** AI for Meta-Science (NeurIPS 2026), position track, 8pp, NeurIPS 2026 template with modified footnote. Fallback: AI for Science — Verification in the Age of AI Scientists, Track B (Position), 4–8pp. | `VENUE.md`, `research/temp/venue-candidates.md` |

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery → pre-registration

*Evidence below reflects the **amended** plan (revision 3, S2b). Revisions 1 and
2 remain in the repository byte-identical; **revision 3 governs** and is the last
pre-data revision — after this gate is signed, every change is a `DEVIATIONS.md`
entry.*

**Criterion** *(current, set 2026-08-17)*

> A pre-registered experiment plan exists, is hashed, and is committed before any
> data collection; every claim is falsifiable and every rival has a
> distinguishing prediction.

**Superseded criterion** *(original, written before S0)*

> ~~Every ORPHAN claim is either re-grounded in recovered data or removed from the
> manuscript; every internal inconsistency in `CLAIM_TRACE.md` §5 is resolved;
> and the surviving thesis is stated in one sentence that the evidence base
> actually supports.~~

**Why it was replaced, and the cost of replacing it.** The original criterion
assumed ORPHAN claims *could* be re-grounded in recovered data. OA-1 closed by
operator decision: the original data is unrecoverable and will be regenerated.
That makes the first clause unsatisfiable as written — no ORPHAN claim can be
re-grounded, so all of them are removed, which the criterion permits but which
turns S2 from claim surgery into a rebuild. **Replacing a gate criterion after
the work it governs has begun violates this file's own opening rule** ("each
criterion is written before the work it governs"). The violation is recorded
rather than hidden: the original text stands above, struck, and the replacement
is dated. The surviving parts of the original criterion are not lost — the
removal of every ORPHAN claim is discharged in `EXPERIMENT_PLAN_R3.md` §1.3, the
`CLAIM_TRACE.md` §5 inconsistencies are discharged there as abandoned claims, and
the one-sentence thesis is §1.1.

**Evidence**

| Requirement | Status | Artifact |
|---|---|---|
| A pre-registered experiment plan exists | **Met.** 1,486 lines: thesis + novelty constraint, 8 abandoned claims each tied to the S0/S1 finding that killed it, 6 proposed claims, 3 fully specified experiments, analysis protocol with two enforced gates, deviation rules, citation obligations, explicit non-scope, and scope-protection rules. | `EXPERIMENT_PLAN_R3.md` (**revision 3, governing**) |
| …is hashed | **Met.** SHA-256 `be61bda9f7b9a33dd9240ea56e010bc87bf0013495e7b0bbafeab0cbeccbdf03`, taken 2026-08-17T09:45:06Z. Chain: revision 1 `aeb174ff…bad3d` (05:10:13Z) → revision 2 `a9954ba3…1df1` (09:25:13Z) → revision 3. Revisions 1 and 2 remain byte-identical; both hashes were re-verified before revision 3 was written and again after it was committed. | `PREREGISTRATION.md` |
| …and is committed before any data collection | **Met.** Re-verified independently at 2026-08-17T09:39:26Z, a fresh sweep not carried forward: `results/` absent, `results_v2/` absent, 0 `results*.json`, 0 `metadata.json`, 0 RAW / 0 SPEC / 0 TRANSCRIPT, `prompts/` absent, `scripts/power_e2.py` absent. No model served, no generation produced, no benchmark queried, no analysis script written. Three known near-matches on the `*spec*`/`*transcript*` sweep are enumerated so the check stays reproducible. | `PREREGISTRATION.md`, `audit/REPO_INVENTORY.json` |
| Every claim is falsifiable | **Met.** C1–C6 each state the observation that refutes them, against numeric thresholds fixed in §2.6 and §5.2. The thesis itself is conditional on C2 ∧ C5 and is withdrawn if C2 fails. | `EXPERIMENT_PLAN_R3.md` §1.4 |
| Every rival has a distinguishing prediction | **Met.** Five rivals × five cells; all five signatures are pairwise distinct. Distinguishing cells: repair-artifact vs format-tax → schema pre-repair; format-tax vs genuine-prior → free-prose; genuine-prior vs decoding → temperature; quantisation → bf16. Ties and ≤3-of-5 winners are pre-registered as "no clean winner"; "no rival matches" is a permitted reportable outcome. | `EXPERIMENT_PLAN_R3.md` §2.5–2.6 |
| …**and each distinguishing prediction is decidable** | **Met at revision 3. NOT met at revision 1, and only marginally met at revision 2.** The discriminating load sits on the two ΔD change columns. A paired sign-flip permutation test over *B* differences admits a smallest two-sided *p* of 2/2^*B*, and rejection at ALPHA needs the as-or-more-extreme count under `2^B/640`. **At *B* = 5 (revision 1) that floor was 0.0625 — twenty times ALPHA, so X1–X4 could not have rejected on any data.** At *B* = 10 (revision 2) the ceiling is **1 assignment-pair**: the observation must be the strictly unique maximum, so a single discordant batch kills the contrast at any effect size. At *B* = 16 (revision 3) the ceiling is **102 pairs** and one discordant batch lands at *p* = 0.000519, 17% of ALPHA. The ceiling table for *B* = 10/12/14/16 is recorded in the plan so the choice is auditable and any future reduction must argue against it. | `EXPERIMENT_PLAN_R3.md` §2.3 |
| …**and undecidability cannot recur silently** | **Met (new at revision 3).** The permutation floor is now **fatal, not merely reported**. Gate 2 computes `min_attainable_p` for every confirmatory test **at plan-load time, before any data is read**, and **aborts** if any test has `min_attainable_p ≥ ALPHA`, naming the test, its *B* or *n*, its floor and ALPHA. A run-time arm recomputes the floor from the *realised* usable count — which null batches and failed runs can reduce — and emits any degraded contrast as `undecidable_by_discreteness` with `significant: null`, **never `significant: false`**. This closes the defect *class*, not just the revision-1 instance: no future deviation or run-time degradation can reintroduce an undecidable confirmatory test unnoticed. Planned floors all pass with orders of margin (paired 3.05e-5; unpaired 3.33e-9; E2 exact 1.45e-11; Monte-Carlo 1.0e-5). | `EXPERIMENT_PLAN_R3.md` §5.2 gate 2 |
| Multiplicity fixed numerically in advance | **Met, unchanged across all three revisions.** FAMILY_SIZE = 16, ALPHA = 0.05/16 = 0.003125, with gate 1 aborting if the confirmatory count ≠ 16 or any `alpha_applied` ≠ `alpha`. Each of the ten amendments across S2a and S2b was checked individually against the family definition; none adds a confirmatory test. Promoting E2's secondary tasks (which would force 24 and an alpha change) was explicitly considered and not done. Directly guards against OA-5 recurring. | `EXPERIMENT_PLAN_R3.md` masthead + §5.2 |
| Sample size is registered as a procedure, not a stale number | **Met (new at revision 3).** `R_final = max(20, the value scripts/power_e2.py confirms at S3)`. Raising R to meet the simulation is **compliance, not a deviation**; lowering it below the floor of 20 is forbidden outright, including by a simulation saying fewer suffice. This removes an asymmetry revision 2 left open, where §8.2 forbade reducing R below the confirmed value while the plan stated 20 as a fixed number. Budget is stated as `9,600 + 320·R` rather than a fixed total. | `EXPERIMENT_PLAN_R3.md` §3.4, §3.5, §8.2 |
| Deviation protocol in force | **Met.** `DEVIATIONS.md` carries zero deviation entries, the log-before-run rule, and `LATE — PROTOCOL VIOLATION` labelling. Both supersessions are recorded there as supersessions rather than deviations, per §5.6 rule 4, and the ledger states that it now governs departures from revision 3. | `DEVIATIONS.md` |
| Scope is protected against non-methodological pressure | **Met.** The calendar consideration is recorded as CONSIDERED AND REJECTED, with an explicit list of reductions that may not be proposed on schedule or budget grounds — now including any reduction of *B* below 16, which must argue against the ceiling table rather than against cost. The venue's non-archival status means missing a cycle costs nothing. **Every revision has raised the budget, not lowered it** — 9,400 → 12,400 → 16,000 at the floor — each time because that is what made a confirmatory test decidable. | `EXPERIMENT_PLAN_R3.md` §8 |
| The revision route is closed at signature | **Recorded.** Revision 3 is the last pre-data revision. Its masthead, §5.6 rule 4 and `DEVIATIONS.md` all state that once G2 is signed every change is a deviation entry logged before the affected analysis runs. | `EXPERIMENT_PLAN_R3.md` masthead, §5.6 |

**Not met by this session, and outstanding:** the C6 thread — whether
CoLLM-NAS's noise-accumulation ablation has been independently cited, replicated
or challenged — is unsettled, with five unverified candidate citing papers. It
does not block G2 but must be resolved before S6 writing (OA-37). Likewise OA-38:
eight of the fifteen obliged citations are still absent from
`audit/references_verified.bib`.

**Operator signature:** ______________________  **Date:** ____________

---

## G3 — Preflight

**Criterion** *(written before the work)*

> The experimental plan for any re-run is fixed in advance and written down:
> estimand (mean vs expected-best-of-*k*), unit of analysis, number of seeds,
> correction family and threshold, and the pre-registration of which comparisons
> are confirmatory. The known code defects (OA-10 through OA-17) are fixed and
> the fixes are tested.

**Evidence:** *(pending)* — note that the *plan* half of this criterion (estimand,
unit of analysis, seeds, correction family and threshold, which comparisons are
confirmatory) is already discharged by `EXPERIMENT_PLAN_R3.md` §3.4, §3.5 and §5.
G3 is **not** thereby satisfied. What remains is the code-defect half — OA-10
through OA-17 fixed and tested — plus the S3 tasks the plan defers to it: measure
`D_rand`; run `scripts/power_e2.py` and set `R_final = max(20, its output)`
**before** any run, which raises R as compliance rather than as a deviation
(§3.4); select and pin the frontier API model; freeze and hash the E1/E2 prompts;
**implement gate 2 — the fatal permutation floor — and confirm it passes at
plan-load** (§5.2); and complete the GENIUS Appendix A.3 pass that seam S3 leaves
open.

**Operator signature:** ______________________  **Date:** ____________

---

## G4 — Build

**Criterion** *(written before the work)*

> Re-run experiments complete with RAW, SPEC and TRANSCRIPT artifacts stored for
> every condition × dataset × seed cell, under a pinned environment, with the
> generating model recorded in metadata.

**Evidence:** *(pending)*

**Operator signature:** ______________________  **Date:** ____________

---

## G5 — Results-file layer

**Criterion** *(written before the work)*

> Every number destined for the manuscript is emitted by a script from stored
> data, into a versioned results file. No number is transcribed by hand. Re-running
> the analysis reproduces every table and figure byte-for-byte.

**Evidence:** *(pending)*

**Operator signature:** ______________________  **Date:** ____________

---

## G6 — Write

**Criterion** *(written before the work)*

> The manuscript is written against the results-file layer, fits the target
> venue's page limit and format, and every numeric assertion resolves to a key in
> a results file. The bibliography is the verified one.

**Evidence:** *(pending)*

**Operator signature:** ______________________  **Date:** ____________

---

## G7 — Referee

**Criterion** *(written before the work)*

> An adversarial read against the target venue's review criteria produces no
> finding that would sink the paper, and the G-anon rule in `VENUE.md` is
> satisfied and verified.

**Evidence:** *(pending)*

**Operator signature:** ______________________  **Date:** ____________
