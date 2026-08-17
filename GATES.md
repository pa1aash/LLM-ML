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
| Thesis selected | **Met.** Instrumentation-artifact thesis, framed as the **application** of an established 2024–26 mechanism to LLM-guided NAS, not as discovery of the mechanism. The general mechanism is published (4 sources); the NAS-scoped instantiation is NOT IN CORPUS across a vault sweep and a targeted arXiv wave. | `research/temp/corpus-critic-findings.md` C1; `EXPERIMENT_PLAN_R4.md` §1.1–1.2 |
| Target venue selected with CFP requirements recorded | **Met.** AI for Meta-Science (NeurIPS 2026), position track, 8pp, NeurIPS 2026 template with modified footnote. Fallback: AI for Science — Verification in the Age of AI Scientists, Track B (Position), 4–8pp. | `VENUE.md`, `research/temp/venue-candidates.md` |

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery → pre-registration

*Evidence below reflects the **amended** plan (revision 4, S2c). Revisions 1, 2
and 3 remain in the repository byte-identical; **revision 4 governs**.*

> **This gate is NOT signed yet, deliberately.** It is signed at the **end of
> S3**, after the analysis code exists and has been run against revision 4 the way
> S3a was run against revision 3. Revision 3 declared itself the last pre-data
> revision on the assumption this gate would be signed next; an implementation
> pass then found **25 defects in it, 7 blocking**. A plan is only as sound as its
> last execution, so the gate waits for the code.

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
removal of every ORPHAN claim is discharged in `EXPERIMENT_PLAN_R4.md` §1.3, the
`CLAIM_TRACE.md` §5 inconsistencies are discharged there as abandoned claims, and
the one-sentence thesis is §1.1.

**Evidence**

| Requirement | Status | Artifact |
|---|---|---|
| A pre-registered experiment plan exists | **Met.** 1,653 lines: thesis + novelty constraint, 8 abandoned claims each tied to the finding that killed it, 6 proposed claims, 3 fully specified experiments plus an anchor-tracking sub-design, analysis protocol with two enforced gates, deviation rules, citation obligations, explicit non-scope, scope protection, and a defect disposition for all 25 S3a findings. | `EXPERIMENT_PLAN_R4.md` (**revision 4, governing**) |
| …is hashed | **Met.** SHA-256 `738601db1d55e81010a62ec1e1259f82e6466f7e8db02f0ec3de4ed15d80cc9d`, taken 2026-08-17T18:25:00Z. Chain: rev 1 `aeb174ff…bad3d` → rev 2 `a9954ba3…1df1` → rev 3 `be61bda9…df03` → rev 4. All three predecessors remain byte-identical; every hash re-verified before and after each step. | `PREREGISTRATION.md` |
| …and is committed before any data collection | **Met.** Re-verified independently, not carried forward: `results_v2/` absent, 0 experimental `results*.json`, 0 `metadata.json`, 0 RAW / 0 SPEC / 0 TRANSCRIPT, `prompts/` absent, `scripts/power_e2.py` absent. `results/` is now tracked (D-25) and holds exactly two **model-free** files — the D_rand computation and the replay-test fixture — neither of which is experimental data. Three known `*spec*`/`*transcript*` near-matches enumerated so the sweep stays reproducible. | `PREREGISTRATION.md`, `audit/REPO_INVENTORY.json` |
| Every claim is falsifiable | **Met.** C1–C6 each state the observation that refutes them against numeric thresholds fixed in §2.6 and §5.2. The thesis is conditional on C2 ∧ C5 and is withdrawn if C2 fails. | `EXPERIMENT_PLAN_R4.md` §1.4 |
| Every rival has a distinguishing prediction | **Met at revision 4, and NOT met at revision 3.** S3a proved that folding `partial` into `reduced` — which §2.6 requires, since they are one band — left three rival pairs separated by a **single** column, and that for the pair deciding **C2** (`format tax` vs `genuine prior`) that column was **free-prose**, the one column §2.6 is most likely to rule unreliable. Revision 4 adds a **sixth column**, anchor tracking (§2.8), measured at the schema-constrained anchor configuration and therefore independent of free-prose parsing. The two rivals now differ in two columns and **free-prose is corroborating rather than load-bearing**. | `EXPERIMENT_PLAN_R4.md` §2.5, §2.8 |
| …and every prediction is *scoreable* | **Met at revision 4.** Revision 3's `quantisation` row predicted `partial` in a **change** column while §2.6 defined only `no chg` and `recovers` for changes — one rival had an unscoreable cell and was silently capped at 4 of 5. Revision 4 defines `partial` on a change (+0.10 to +0.25·D_rand) and names `worsens` for the negative direction, and registers that an observation no rival predicts scores as a **mismatch**, not indeterminate. | `EXPERIMENT_PLAN_R4.md` §2.6 |
| …and each distinguishing prediction is decidable | **Met at revision 4. NOT met at revision 1; marginal at revisions 2–3.** A paired sign-flip test over *B* differences admits a smallest two-sided *p* of 2/2^*B*. At *B* = 5 (rev 1) that floor was **0.0625**, twenty times alpha — X1–X4 could not have rejected on any data. At *B* = 10 (rev 2) the ceiling was **1 assignment-pair**: one discordant batch killed the contrast at any effect size. At *B* = 16 (rev 3–4) the ceiling is **96 pairs at the new alpha** and one discordant batch lands at **17.6% of ALPHA**. The full ceiling table for *B* = 10/12/14/16/32 is in the plan so any future reduction must argue against it. | `EXPERIMENT_PLAN_R4.md` §2.3 |
| …and undecidability cannot recur silently | **Met.** Gate 2 computes `min_attainable_p` for every confirmatory test **at plan-load, before any data is read**, and **aborts** naming the test, its `B_batch` or *n*, its floor and ALPHA. A run-time arm recomputes from the *realised* count — which null batches and failed runs reduce — and emits degraded contrasts as `undecidable_by_discreteness` with `significant: null`, **never `false`**. **Verified by execution:** 8 adversarial fixtures, 8/8 behave as required at the new alpha. | `EXPERIMENT_PLAN_R4.md` §5.2; `tests/test_gates.py` |
| Multiplicity fixed numerically in advance | **Met. Changed at revision 4: FAMILY_SIZE 16 → 17, ALPHA 0.003125 → 0.05/17 = 0.0029411764705882353.** R4-1 adds exactly one confirmatory test (X5); R4-2 through R4-5 add none, and the per-amendment check is tabulated in the plan's masthead and §9. Gate 1 aborts if the confirmatory count ≠ 17 or any `alpha_applied` ≠ ALPHA. **Every floor in the re-run discreteness table clears the tighter alpha** — no STOP condition triggered. | `EXPERIMENT_PLAN_R4.md` masthead, §5.2 |
| The results layer is a provenance record | **Met at revision 4. NOT met at revision 3.** S3a's replay test found only **5 of 12** inspected quantities recomputable: the schema stored batch-level aggregates while pooled D, S, the entropies and every bootstrap interval are defined at generation level, and no generation-level record existed. Revision 4 adds **`generations[]`**, plus `contrast_operands`, `pairing_key` and `test_statistic` so a contrast's operands and stage are machine-readable rather than prose. **`results/` is removed from `.gitignore`** — revision 3 directed the entire G5 layer into a gitignored path. | `EXPERIMENT_PLAN_R4.md` §5.5; `tests/test_replay.py` |
| The threshold reference is measured, not assumed | **Met at revision 4.** Revision 3 called the repository sampler "uniform" and anchored on ≈0.74; S3a measured it and neither held — `pooling` is **48.21% `none`** against 25% under uniformity, and block-count variation inflates *d* by **+7.96%**. Revision 4 anchors on a **corrected uniform sampler at fixed block count, `D_rand` = 0.719205** (analytic 0.718872), reports the repository's sampler separately as `D_repo_sampler` = 0.771931, and **tightens the sanity range to [0.705, 0.735]** — which now rejects the repository sampler, the block-free corrected sampler, and revision 3's own 0.74 anchor, all three of which [0.65, 0.80] admitted. | `EXPERIMENT_PLAN_R4.md` §2.6; `results/E1_reference.json` |
| Deviation protocol in force | **Met.** `DEVIATIONS.md` carries zero deviation entries, the log-before-run rule, and `LATE — PROTOCOL VIOLATION` labelling. All three supersessions are recorded there as supersessions rather than deviations, per §5.6 rule 4, and the ledger states it now governs departures from revision 4. | `DEVIATIONS.md` |
| Sample size is a procedure, not a stale number | **Met.** `R_final = max(20, the value scripts/power_e2.py confirms at S3)`. Raising R to meet the simulation is compliance; lowering below 20 is forbidden outright. The simulation must run at the **new** ALPHA. Budget is `10,880 + 320·R`. | `EXPERIMENT_PLAN_R4.md` §3.4, §3.5, §8.2 |
| Scope is protected against non-methodological pressure | **Met.** The calendar is recorded as CONSIDERED AND REJECTED, with an explicit list of reductions unavailable on schedule or budget grounds — now including any reduction of `B_batch` below 16 **and removal of the §2.8 sub-design**, which is the only reason C2 is decidable. **Every revision has raised the budget** — 9,400 → 12,400 → 16,000 → 17,280 at the floor — each time to make a test decidable or an attribution separable. | `EXPERIMENT_PLAN_R4.md` §8 |
| Every S3a defect is dispositioned | **Met.** All 25 resolved, none deferred, each with the choice made and the alternatives rejected recorded. | `EXPERIMENT_PLAN_R4.md` §9; `audit/S3A_IMPLEMENTATION_DEFECTS.md` |

**Outstanding, and why the gate still waits:**

- **The analysis code for the new machinery does not exist yet.** §2.8's
  `anchor_tracking` outcome, the generalised signature scorer, `generations[]`
  emission and the E2 inference primitives are specified but unexecuted. S3a's
  lesson is that specification and execution diverge — **and revision 4 proved it
  again in its own drafting**, when X5 was first written as `paired_exact` at
  2³² = 4.29 × 10⁹ assignments, an unenumerable reference set, and had to be
  re-registered as Monte Carlo. Signing before the code runs would repeat exactly
  the mistake that produced revisions 2, 3 and 4.
- **OA-37** — the C6 thread: whether CoLLM-NAS's noise-accumulation ablation has
  been independently cited, replicated or challenged, with five unverified
  candidate citing papers. Does not block G2; must be resolved before S6.
- **OA-38** — ten of the fifteen obliged citations are still absent from
  `audit/references_verified.bib`. Does not block G2; must be resolved before S6.
- **New at revision 4:** §2.8's manipulation touches the in-context ordering and
  exemplar literature, which must be cited as **prior art for the mechanism** per
  the §1.2 defect rule. Sourcing it is an S6 task and is not yet an open action.

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
confirmatory) is already discharged by `EXPERIMENT_PLAN_R4.md` §3.4, §3.5 and §5.
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
