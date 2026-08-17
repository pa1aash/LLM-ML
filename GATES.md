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
| Thesis selected | **Met.** Instrumentation-artifact thesis, framed as the **application** of an established 2024–26 mechanism to LLM-guided NAS, not as discovery of the mechanism. The general mechanism is published (4 sources); the NAS-scoped instantiation is NOT IN CORPUS across a vault sweep and a targeted arXiv wave. | `research/temp/corpus-critic-findings.md` C1; `EXPERIMENT_PLAN_R2.md` §1.1–1.2 |
| Target venue selected with CFP requirements recorded | **Met.** AI for Meta-Science (NeurIPS 2026), position track, 8pp, NeurIPS 2026 template with modified footnote. Fallback: AI for Science — Verification in the Age of AI Scientists, Track B (Position), 4–8pp. | `VENUE.md`, `research/temp/venue-candidates.md` |

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery → pre-registration

*Evidence below reflects the **amended** plan (revision 2, S2a). Revision 1
remains in the repository byte-identical; revision 2 governs.*

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
removal of every ORPHAN claim is discharged in `EXPERIMENT_PLAN_R2.md` §1.3, the
`CLAIM_TRACE.md` §5 inconsistencies are discharged there as abandoned claims, and
the one-sentence thesis is §1.1.

**Evidence**

| Requirement | Status | Artifact |
|---|---|---|
| A pre-registered experiment plan exists | **Met.** 1,323 lines: thesis + novelty constraint, 8 abandoned claims each tied to the S0/S1 finding that killed it, 6 proposed claims, 3 fully specified experiments, analysis protocol, deviation rules, citation obligations, explicit non-scope, and scope-protection rules. | `EXPERIMENT_PLAN_R2.md` (**revision 2, governing**) |
| …is hashed | **Met.** SHA-256 `a9954ba3c1dc61fce8e9ddb0b057eb4f14ab99c4b528c0b0446a7171e43b1df1`, taken 2026-08-17T09:25:13Z. Supersedes revision 1, `aeb174ffb008252368cc7fbcb121bd0fa0642f2fa4f3ec70228256920bfbad3d`, taken 2026-08-17T05:10:13Z. Revision 1 remains byte-identical; its hash was re-verified at the moment revision 2 was hashed. | `PREREGISTRATION.md` |
| …and is committed before any data collection | **Met.** Re-verified at 2026-08-17T09:18:00Z, not carried forward: `results/` absent, `results_v2/` absent, 0 `results*.json`, 0 `metadata.json`, 0 RAW / 0 SPEC / 0 TRANSCRIPT, `prompts/` absent, `scripts/power_e2.py` absent. No model served, no generation produced, no benchmark queried, no analysis script written. | `PREREGISTRATION.md`, `audit/REPO_INVENTORY.json` |
| Every claim is falsifiable | **Met.** C1–C6 each state the observation that refutes them, against numeric thresholds fixed in §2.6 and §5.2. The thesis itself is conditional on C2 ∧ C5 and is withdrawn if C2 fails. | `EXPERIMENT_PLAN_R2.md` §1.4 |
| Every rival has a distinguishing prediction | **Met.** Five rivals × five cells; all five signatures are pairwise distinct. Distinguishing cells: repair-artifact vs format-tax → schema pre-repair; format-tax vs genuine-prior → free-prose; genuine-prior vs decoding → temperature; quantisation → bf16. Ties and ≤3-of-5 winners are pre-registered as "no clean winner"; "no rival matches" is a permitted reportable outcome. | `EXPERIMENT_PLAN_R2.md` §2.5–2.6 |
| …**and each distinguishing prediction is decidable** | **Met at revision 2, and was not met at revision 1.** The discriminating load sits on the two change columns, and revision 1's 5 batches gave a paired sign-flip permutation test a smallest attainable two-sided p of 2/2⁵ = 0.0625 — twenty times ALPHA, so X1–X4 could never have rejected. Revision 2's 10 batches give 2/2¹⁰ = 0.001953, which clears ALPHA. Every paired result now also emits `min_attainable_p`, so an undecidable test is reported as undecidable rather than as a null. | `EXPERIMENT_PLAN_R2.md` §2.3, §5.2 |
| Multiplicity fixed numerically in advance | **Met, unchanged across the revision.** FAMILY_SIZE = 16, ALPHA = 0.05/16 = 0.003125, with an emitter-level assertion that aborts if the confirmatory count ≠ 16 or any `alpha_applied` ≠ `alpha`. Each of the six amendments was checked individually against the family definition; none adds a confirmatory test, and promoting E2's secondary tasks (which would force 24 and an alpha change) was explicitly considered and not done. Directly guards against OA-5 recurring. | `EXPERIMENT_PLAN_R2.md` masthead + §5.2 |
| Deviation protocol in force | **Met.** `DEVIATIONS.md` carries zero deviation entries, the log-before-run rule, and `LATE — PROTOCOL VIOLATION` labelling. The revision-1 → revision-2 supersession is recorded there as a supersession, not as a deviation, per §5.6 rule 4. | `DEVIATIONS.md` |
| Scope is protected against non-methodological pressure | **Met (new at revision 2).** The calendar consideration is recorded as CONSIDERED AND REJECTED, with the list of reductions that may not be proposed on schedule grounds. The venue's non-archival status means missing a cycle costs nothing. Revision 2 raised the generation budget 9,400 → 12,400 on rigour grounds, which is the precedent the section fixes. | `EXPERIMENT_PLAN_R2.md` §8 |

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
confirmatory) is already discharged by `EXPERIMENT_PLAN_R2.md` §3.4, §3.5 and §5.
G3 is **not** thereby satisfied. What remains is the code-defect half — OA-10
through OA-17 fixed and tested — plus the S3 tasks the plan defers to it: measure
`D_rand`; run `scripts/power_e2.py` and confirm or raise R **before** any run;
select and pin the frontier API model; freeze and hash the E1/E2 prompts; and
complete the GENIUS Appendix A.3 pass that seam S3 leaves open.

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
