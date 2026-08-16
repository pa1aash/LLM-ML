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

**Evidence:** *(pending — Block 8 hyperresearch positioning analysis)*

**Operator signature:** ______________________  **Date:** ____________

---

## G2 — Claim surgery

**Criterion** *(written before the work)*

> Every ORPHAN claim is either re-grounded in recovered data or removed from the
> manuscript; every internal inconsistency in `CLAIM_TRACE.md` §5 is resolved;
> and the surviving thesis is stated in one sentence that the evidence base
> actually supports.

**Evidence:** *(pending)*

**Operator signature:** ______________________  **Date:** ____________

---

## G3 — Preflight

**Criterion** *(written before the work)*

> The experimental plan for any re-run is fixed in advance and written down:
> estimand (mean vs expected-best-of-*k*), unit of analysis, number of seeds,
> correction family and threshold, and the pre-registration of which comparisons
> are confirmatory. The known code defects (OA-10 through OA-17) are fixed and
> the fixes are tested.

**Evidence:** *(pending)*

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
