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
| Thesis selected | **Met.** Instrumentation-artifact thesis, framed as the **application** of an established 2024–26 mechanism to LLM-guided NAS, not as discovery of the mechanism. The general mechanism is published (4 sources); the NAS-scoped instantiation is NOT IN CORPUS across a vault sweep and a targeted arXiv wave. | `research/temp/corpus-critic-findings.md` C1; `EXPERIMENT_PLAN_R5.md` §1.1–1.2 |
| Target venue selected with CFP requirements recorded | **Met.** AI for Meta-Science (NeurIPS 2026), position track, 8pp, NeurIPS 2026 template with modified footnote. Fallback: AI for Science — Verification in the Age of AI Scientists, Track B (Position), 4–8pp. | `VENUE.md`, `research/temp/venue-candidates.md` |

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery → pre-registration

*Evidence below reflects the **amended** plan (revision 5, S2d). Revisions 1–4
remain byte-identical; **revision 5 governs**.*

**Criterion** *(current, set 2026-08-17; restated in four testable parts at S2d)*

> A pre-registered experiment plan exists, is hashed, and is committed before any
> data collection; every claim is falsifiable and every rival has a
> distinguishing prediction.

The criterion is met when all four of the following hold:

1. **every claim is falsifiable with its refuting observation stated;**
2. **every rival has a distinguishing prediction that the implemented scorer can
   compute from registered fields;**
3. **every confirmatory test clears its discreteness floor;**
4. **the plan is hashed with no data collected.**

**Superseded criterion** *(original, written before S0)*

> ~~Every ORPHAN claim is either re-grounded in recovered data or removed from the
> manuscript; every internal inconsistency in `CLAIM_TRACE.md` §5 is resolved;
> and the surviving thesis is stated in one sentence that the evidence base
> actually supports.~~

**Why it was replaced, and the cost of replacing it.** The original assumed ORPHAN
claims *could* be re-grounded. OA-1 closed by operator decision: the data is
unrecoverable and will be regenerated, so the first clause is unsatisfiable as
written and every ORPHAN claim is removed instead. **Replacing a gate criterion
after the work it governs has begun violates this file's own opening rule.** The
violation is recorded rather than hidden: the original stands above, struck. Its
surviving parts are discharged — ORPHAN removal in `EXPERIMENT_PLAN_R5.md` §1.3,
the `CLAIM_TRACE.md` §5 inconsistencies there as abandoned claims, the
one-sentence thesis at §1.1.

---

### 1. Every claim is falsifiable with its refuting observation stated — **MET**

| Claim | Refuting observation | Registered at |
|---|---|---|
| **C1** repair concentrates the design distribution | `D_post ≥ D_pre − 0.10·D_rand` | §1.4, §2.6 |
| **C2** an apparatus factor dominates the model's prior | `genuine prior` wins the signature match, **or** the winner fails the §2.6 threshold | §1.4, §2.5–2.6 |
| **C3** the effect is not an artifact of model scale | the free-prose→schema contrast is `no chg` at 8B or frontier while `collapsed` at 1.7B | §1.4 |
| **C4** uncurated accumulation does not beat curation | uncurated > curated at p < ALPHA with δ > 0 | §1.4, §3.5 |
| **C5** measurement configuration changes the arm ordering | identical ordering with overlapping 95% CIs on every pairwise difference | §1.4, §3.3 |
| **C6** RZ-NAS's proxy menu is size-tracking off NAS-Bench-201 | fewer than two proxies meet the condition | §1.4, §4.2 |

Every threshold resolves to a number at the registered `D_rand` = 0.719205. The
**thesis itself** is conditional on **C2 ∧ C5** and is withdrawn if C2 fails
(§1.4) — the plan states its own defeat condition.

**Recorded limits, so the criterion is not overclaimed:** §2.5's KNOWN LIMITATION
— on `free-prose` and `schema pre-repair` every level label is predicted by some
rival, so those two columns discriminate *between* rivals but cannot reject the
set. "No rival matched" fires almost only through the change and tracking
columns. Verified by fixture C6.

### 2. Every rival has a distinguishing prediction the implemented scorer can compute from registered fields — **MET**

| Requirement | Evidence |
|---|---|
| Predictions are machine-readable | The five rows are three **explicit predicates** over the 2×2 tracking grid plus five level/change labels (§2.5, R5-5). No prose `and/or` remains. |
| The predicates are mutually exclusive | R-A requires both pre entries `no tracking`; F-T requires at least one `tracks`; NONE requires all four `no tracking`. |
| **The predicates are satisfiable** | Checked by construction. F-T's conjunction form was **logically impossible** — one modal value cannot equal both the first-enumerated and a different exemplar value — and was replaced by a disjunction-plus-equality (plan §9, R5-c). |
| The scorer computes them | `src/emit/signature.py`, `src/emit/anchor.py`. **C1–C5: each rival's own signature returns that rival, strict-max, 6/6 against threshold 5.** |
| …**from registered fields** | Plan-to-code coverage re-checked. The blocking gap S3b found — the pre-repair tracking aggregates having no cell field — is closed by **R5-3**; `label_tracking_grid`, `modal_value_*`, `exemplar_values`, `chance_rates` and `deltas[]` close the rest (schema 1.4.0, §5.5). |
| The discriminator does not depend on free prose | **Fixture C15**: free-prose forced `indeterminate`, `repair artifact` and `format tax` still resolve — 4/5 and 5/5. This is the case the sixth column exists for. |
| Invariance is not misread | **Fixture C16**: a genuine prior collapsed onto values matching neither enumeration head nor either exemplar returns `no tracking` under both orders, and `genuine prior` wins 6/6. |
| Degenerate and boundary cases are decided | C6/C6b zero-match, C7 tie, C8–C10 indeterminacy scaling, C11/C11b `partial`, C12 `worsens`, C13 bit-exact boundary, C14 the contingency. **22/22 assertions pass.** |

**Recorded limit:** attribution is at the aggregate level. Enumeration order is
reversed for **every** field at once, so a positive tracking result shows the
harness drives *something*, not *which field* (§7). And `tracks_exemplar` is a
three-field statistic whose smallest non-zero value (⅓) already exceeds its
chance rate (0.25), so a `tracks` verdict on it must be read against the other
exemplar level rather than alone (§9).

### 3. Every confirmatory test clears its discreteness floor — **MET**

**FAMILY_SIZE = 17, ALPHA = 0.05/17 = 0.0029411764705882353.** All 17 floors
recomputed at S2d (§5.2, R5-11):

| Tests | Mode | Floor | % of ALPHA |
|---|---|---:|---:|
| X1–X4 × 3 models, 11 live slots | `paired_exact`, B_batch = 16 | 3.051758e-05 | **1.038%** |
| X3.frontier | `not_applicable` | exempt | — |
| X5 | `monte_carlo`, N = 100,000 | 9.999900e-06 | 0.340% |
| Y1–Y4 | `monte_carlo`, N = 100,000 | 9.999900e-06 | 0.340% |

**The binding floor is at 1.038% of ALPHA — almost two orders of margin. No floor
fails; no STOP condition triggered.** Enforced, not merely asserted: gate 2's
plan-load arm aborts before any data is read if any floor ≥ ALPHA, and its
run-time arm marks a degraded contrast `undecidable_by_discreteness` with
`significant: null` rather than `false`. **Fixtures B1–B8: 8/8 behave as required
at the revision-5 constants**, including B5 (an undecidable B=5 family aborts) and
B4 (a decidable-but-inadequate B=10 family does **not**, proving the gate tests
decidability rather than adequacy).

### 4. The plan is hashed with no data collected — **MET**

SHA-256 `e3206e718161cc139830ff79741c6fe8f78e1d34f1147d3f644b36be2107b201`, taken
2026-08-18T04:00:00Z. Chain rev 1 → rev 5, all four predecessors byte-identical
and re-verified before and after. Data status re-verified independently at the
hash: `results_v2/` absent, 0 experimental `results*.json`, 0 `metadata.json`,
0 RAW / 0 SPEC / 0 TRANSCRIPT, `prompts/` absent, `scripts/power_e2.py` absent.
`results/` holds two **model-free** files — the D_rand arithmetic and the replay
fixture. No model has been called in any session, local or hosted.

---

**VERDICT: all four criteria MET.** The operator signs.

**What signing closes.** The revision route (§5.6 rule 4). After signature every
change is a `DEVIATIONS.md` entry logged before the affected analysis runs. That
route has caught defects three times — 25 at S3a, 18 at S3b, 3 in revision 5's own
drafting — so closing it is a real decision, not a formality.

**Outstanding, and not blocking G2:** OA-37 (CoLLM-NAS replication status, five
unverified leads) and OA-38 (ten of fifteen obliged citations absent from
`references_verified.bib`), both due before S6. §2.8's manipulation also touches
the in-context ordering and exemplar literature, which must be cited as prior art
per §1.2's defect rule — an S6 task.

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
confirmatory) is already discharged by `EXPERIMENT_PLAN_R5.md` §3.4, §3.5 and §5.
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
