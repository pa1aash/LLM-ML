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
| Thesis selected | **Met.** Instrumentation-artifact thesis, framed as the **application** of an established 2024–26 mechanism to LLM-guided NAS, not as discovery of the mechanism. The general mechanism is published (4 sources); the NAS-scoped instantiation is NOT IN CORPUS across a vault sweep and a targeted arXiv wave. | `research/temp/corpus-critic-findings.md` C1; `EXPERIMENT_PLAN_R6.md` §1.1–1.2 |
| Target venue selected with CFP requirements recorded | **Met.** AI for Meta-Science (NeurIPS 2026), position track, 8pp, NeurIPS 2026 template with modified footnote. Fallback: AI for Science — Verification in the Age of AI Scientists, Track B (Position), 4–8pp. | `VENUE.md`, `research/temp/venue-candidates.md` |

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery → pre-registration

*Evidence below reflects the **amended** plan (revision 6, S3c). Revisions 1–5
remain byte-identical; **revision 6 governs and is the last before this gate**.*

**Criterion** *(current, set 2026-08-17; restated in five testable parts at S3c)*

> A pre-registered experiment plan exists, is hashed, and is committed before any
> data collection; every claim is falsifiable and every rival has a
> distinguishing prediction.

Met when all five of the following hold:

1. every claim falsifiable with its refuting observation stated;
2. every rival distinguishable by the **implemented** scorer from **registered
   fields**;
3. every confirmatory test clears its discreteness floor;
4. hashed with no data collected;
5. **the registered pilots have run and set their parameters.**

**Superseded criterion** *(original, written before S0)*

> ~~Every ORPHAN claim is either re-grounded in recovered data or removed from the
> manuscript; every internal inconsistency in `CLAIM_TRACE.md` §5 is resolved;
> and the surviving thesis is stated in one sentence that the evidence base
> actually supports.~~

**Why it was replaced, and the cost.** The original assumed ORPHAN claims *could*
be re-grounded. OA-1 closed by operator decision: the data is unrecoverable and
will be regenerated, so the first clause is unsatisfiable and every ORPHAN claim
is removed instead. **Replacing a gate criterion after the work it governs has
begun violates this file's own opening rule.** Recorded, not hidden: the original
stands above, struck. Its surviving parts are discharged in
`EXPERIMENT_PLAN_R6.md` §1.3 and §1.1.

---

### 1. Every claim falsifiable with its refuting observation — **MET**

| Claim | Refuting observation |
|---|---|
| **C1** repair concentrates the design distribution | `D_post ≥ D_pre − 0.10·D_rand` |
| **C2** an apparatus factor dominates the model's prior | `genuine prior` wins the signature match, **or** the winner fails the §2.6 threshold |
| **C3** the effect is not an artifact of model scale | free-prose→schema is `no chg` at 8B or frontier while `collapsed` at 1.7B |
| **C4** uncurated accumulation does not beat curation | uncurated > curated at p < ALPHA with δ > 0 |
| **C5** measurement configuration changes the arm ordering | identical ordering with overlapping 95% CIs on every pairwise difference |
| **C6** RZ-NAS's proxy menu is size-tracking off NAS-Bench-201 | fewer than two proxies meet the condition |

Every threshold resolves to a number at `D_rand` = 0.719205. The **thesis** is
conditional on **C2 ∧ C5** and is withdrawn if C2 fails — the plan states its own
defeat condition. **Limits recorded, not glossed:** §2.5's KNOWN LIMITATION — on
`free-prose` and `schema pre-repair` every level label is predicted by some rival,
so those columns discriminate between rivals but cannot reject the set (fixture
C6); and §7 — enumeration order is reversed for every field at once, so tracking
shows the harness drives *something*, not *which field*.

### 2. Every rival distinguishable by the implemented scorer from registered fields — **MET**

| Requirement | Evidence |
|---|---|
| Predictions are machine-readable | Three explicit predicates over a three-entry grid (§2.5). No prose. |
| Mutually exclusive **and satisfiable** | Checked by construction and fixture. F-T's conjunction form was **logically impossible** and was replaced by a disjunction at revision 5; revision 6 rebuilt the grid around the cross-level delta. |
| **The exemplar channel actually discriminates** | **New at revision 6.** Single-cell `tracks_exemplar` could not separate `format tax` from `genuine prior` — a format tax tracks *whichever* exemplar is shown. §2.5a's cross-level delta asks whether the modal **moves**, and is **identically 0** for any stable modal: fixture **C19** verifies max \|Δ\| = 0.0 exhaustively over the whole exemplar-field vocabulary; **C19b** gives Δ = 1 when the modal follows. |
| The scorer computes them | `src/emit/signature.py`, `src/emit/anchor.py`. **C1–C5: each rival's own signature returns that rival, 6/6 against threshold 5.** |
| …from **registered** fields | Schema 1.5.0: `cross_level_exemplar` per cell, `label_tracking_grid` reshaped to the three read entries, `label_tracking_unread` for the emitted-but-unscored pair. The revision-5 blocking gap (pre-repair aggregates) stays closed. |
| Free prose is not load-bearing | **C15**: free-prose forced `indeterminate`, both instrument rivals still resolve. |
| The new channel is exercised | **C17** — a format tax driven by the exemplar alone, which revision 5's grid would have scored `genuine prior`, now resolves to `format tax`. **C18** — a genuine prior whose fixed modal coincides with one shown exemplar (single-cell reading ⅓ > 0.25 → `tracks`) gives Δ = 0 and still scores `genuine prior`. |
| Degenerate and boundary cases decided | C6/C6b, C7, C8–C10, C11/C11b, C12, C13 bit-exact, C14 contingency, C16 invariance. **27/27 assertions pass.** |

### 3. Every confirmatory test clears its discreteness floor — **MET**

**FAMILY_SIZE = 17, ALPHA = 0.05/17 = 0.0029411764705882353** — unchanged; the
cross-level delta is classified by CI position and adds no test. Re-run at the
pilot-confirmed parameters (§5.2, R6-1):

| Tests | Mode | Design | Floor | % of ALPHA |
|---|---|---|---:|---:|
| X1–X4 × 3 models, 11 live slots | `paired_exact` | B_batch = 16 | 3.051758e-05 | **1.038%** |
| X3.frontier | `not_applicable` | — | exempt | — |
| X5 | `monte_carlo` | 56 pairs, N = 100,000 | 9.999900e-06 | 0.340% |
| Y1–Y4 | `monte_carlo` | R = 24, N = 100,000 | 9.999900e-06 | 0.340% |

**No floor moved and none fails.** Both pilot parameters only enlarge
already-intractable reference sets — X5's to 2⁵⁶, E2's to C(48,24) ≈ 3.2 × 10¹³ —
so both stay on Monte Carlo and their floors depend on N. Enforced, not asserted:
gate 2 aborts before any data is read, and its run-time arm marks a degraded
contrast `undecidable_by_discreteness` with `significant: null`. **B1–B8: 8/8**,
including B4 proving the gate tests decidability rather than adequacy.

### 4. Hashed with no data collected — **MET**

SHA-256 `d63a7625f06dcbaa08ad35182490036de12c3d0354febee9e141656ec79d340b`, taken
2026-08-18T04:35:00Z. Chain of six; all five predecessors byte-identical and
re-verified. Data status re-verified at the hash: `results_v2/` absent,
0 experimental `results*.json`, 0 `metadata.json`, 0 RAW / 0 SPEC / 0 TRANSCRIPT,
`prompts/` absent. `results/` holds model-free files only. **No model has been
called in any session, local or hosted.**

### 5. The registered pilots have run and set their parameters — **MET**

| Pilot | Result | Consequence |
|---|---|---|
| `scripts/power_e2.py` | power **0.702 at R = 20**, 0.822 at R = 24 | **`R_final = 24`.** The floor was insufficient; raising R is compliance under §3.4, not a deviation. |
| `scripts/pilot_tracking.py` | cross-level Δ reaches 80% coverage at **B = 28**; `tracks_first` at 20; single-cell `tracks_exemplar` at 40 | **`B_tracking = 28`**, binding on the cross-level delta. |

**The tracking pilot's registered criterion was itself miscalibrated and the pilot
caught it:** a half-width of 0.15 at a true rate of 0.40 gives [0.25, 0.55], which
**contains** the chance rate 0.263889 and therefore reads `no tracking`. The
criterion would have certified a width that cannot detect the effect. Corrected in
§2.8 (R6-3).

Both are **simulation over synthetic draws** — no model, no training, no benchmark
query — marked `pilot: true`, `confirmatory: false`,
`quarantined_from_analysis: true`, and they set design parameters only.
**Budget now a number, not a formula: 24,000 generations, ~4,160 of them frontier
API calls, zero training runs.**

**One caveat carried, not buried (S3C-01):** the NAS-Bench-201 tables are not in
the repository, so the E2 pilot's pool is simulated rather than sampled from the
benchmark. Power at a fixed Cliff's δ is driven by distributional overlap, which
the simulation controls; the mapping from δ to a mean shift is synthetic. Re-run
against the real table before the first E2 run, logged either way.

---

**VERDICT: all five criteria MET.** The operator signs.

**What signing closes.** The revision route (§5.6 rule 4). Afterwards every change
is a `DEVIATIONS.md` entry logged before the affected analysis runs. That route
has caught defects four times — 25 at S3a, 18 at S3b, three in revision 5's own
drafting, and the miscalibrated pilot criterion this session — so closing it is a
real decision. **Revision 6's scope was closed by construction precisely so that
the gate could be reached**; six further items are in `audit/S3C_DEFECTS.md`, none
blocking, each with a defined trigger and response.

**Outstanding, not blocking:** OA-37 (CoLLM-NAS replication status) and OA-38 (ten
of fifteen obliged citations absent from `references_verified.bib`), both due
before S6, plus the in-context ordering and exemplar literature §2.8 must cite as
prior art per §1.2's defect rule.

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
confirmatory) is already discharged by `EXPERIMENT_PLAN_R6.md` §3.4, §3.5 and §5.
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
