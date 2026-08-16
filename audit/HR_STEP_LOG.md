# HR_STEP_LOG — hyperresearch run `llm-nas-feedback-positioning-7125b1`

One line per step. `invoked` = step skill run via the Skill tool; `MANUAL` =
procedure executed by hand; `NOT RUN` = did not execute.

## S0 session (prior)

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| bootstrap | MANUAL | `research/query-<tag>.md`, `research/scaffold.md` | TodoWrite unavailable; chain position tracked by disk artifacts |
| 1 decompose | invoked | `prompt-decomposition.json`, `temp/coverage-matrix.md` | tier=full, format=argumentative, 32 sub-Qs, 58 phrases mapped, 0 gaps |
| 2 width-sweep | invoked | 78 notes, 65 `claims-*.json`, `temp/search-plan.md` | 8 fetchers, 44 seed URLs → 78 notes; 68 planned searches, 17 adversarial |
| 3–16 | NOT RUN | — | session ended after step 2 |

## S1 session — Block A (fetch-defect repair)

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| A.1 diagnose | MANUAL | — | **Root cause identified.** See below. |
| A.2 corpus audit | MANUAL | — | 66 active notes; **37 ABSTRACT-ONLY** (<6000 chars body) |
| A.3 repair | MANUAL | `temp/fulltext-repair-log.md` | curl + pymupdf direct route; 27/27 succeeded, 0 failures |
| A.4 mandatory re-fetch | MANUAL | 27 notes rewritten | all Block A.4 sources now full text |
| A.5 verify | MANUAL | — | **ABSTRACT-ONLY 37 → 10** |

### A.1 — Root cause of the arXiv extraction failure

**It is not pymupdf, not a redirect, not a bot wall.** It is hyperresearch's own
junk-content heuristic rejecting valid PDFs before the parser runs.

Evidence:

```
curl -sSL https://arxiv.org/pdf/2304.10970
  → http=200  content_type=application/pdf  size=625754
  → magic bytes: %PDF-1.5                       (valid PDF)

pymupdf on that identical file
  → pages: 17   page-1 chars: 3305             (parses perfectly)

hyperresearch fetch on the same URL
  → {"ok": false,
     "error": "Skipped junk content from https://arxiv.org/pdf/2304.10970:
               Binary PDF garbage in content",
     "error_code": "JUNK_CONTENT"}
```

The CLI downloads the bytes, applies a text-heuristic that sees binary, and
discards the payload **before** invoking pymupdf. Every arXiv PDF in the corpus
was silently reduced to its abstract landing page by this path.

**Disposition:** routed around, not fixed — modifying the installed package is
out of scope. `research/temp/fulltext-repair-log.md` records the route used per
source. This defect will recur on any future run until the package is patched or
upgraded.

### A.3/A.4 — Routes used

| Route | Sources | Result |
|---|---|---|
| `arxiv-pdf` (curl + pymupdf) | 26 | success |
| `pmlr-raw` (PMLR asset mirror) | 1 (RZ-NAS) | success — no arXiv preprint exists |
| `ar5iv-html` fallback | 0 | not needed |

**RZ-NAS full text recovered: 74,969 characters** from PMLR v267 (ICML 2025).
It landed in `icml-poster-rz-nas-…md` (80,383 bytes total), which is the note the
matcher resolved first; the sibling stub `rz-nas-enhancing-…md` remains short but
is now redundant.

Mandatory Block A.4 list, post-repair status:

| Source | Status |
|---|---|
| RZ-NAS | ✅ full text (PMLR) |
| EvoPrompting | ✅ already full text (17,965 w, S0 batch 1) |
| GENIUS | ✅ already full text (9,839 w, S0 batch 6) |
| LLMatic | ✅ repaired |
| GPT-NAS | ✅ repaired |
| CoLLM-NAS (2025 agentic) | ✅ repaired |
| Agent-Oriented Planning (multi-agent) | ✅ repaired |
| Li & Talwalkar | ✅ repaired (+ full-text copy already existed) |
| Yang et al. | ✅ already full text (7,909 w, S0 batch 7) |
| NAS-Bench-201 | ✅ repaired |
| Huang | ✅ already full text (9,478 w) |
| Kamoi | ✅ already full text (14,988 w) |
| Stechly | ✅ already full text (9,657 w) |
| Tyen | ✅ repaired |
| Olausson | ✅ repaired |

**All 15 mandatory sources are now full text.**

### A.5 — Remaining ABSTRACT-ONLY (10)

None is a paper abstract. All are web pages that are simply short:

```
readmemd                                    1831   GitHub README
interpretability-as-a-science-workshop      2071   workshop page
automl-2026                                 2125   conference homepage
icbinb-crack-open-the-research-process      3355   series hub page
github-pasalabrz-nas-github                 3365   GitHub repo page
rz-nas-…-at-duckduckgo                      3746   search-results page
tae-neurips-2026-workshop-ai-evaluation     4706   workshop CFP
call-for-workshops-2026                     4771   organiser-facing template
neurips-workshop-2023                       4798   past workshop page
rz-nas-enhancing-…-zero-cost                5537   stub; full text is in the poster note
```

**Zero paper-type sources remain abstract-only.** The Block C labelling
requirement ("a claim resting on an abstract is labelled as resting on an
abstract") therefore applies to no paper citation in the corpus.

## S1 — Blocks B, C, D

| Block | Mode | Status |
|---|---|---|
| B coverage audit + venue gap-fill | NOT RUN | — |
| C steps 3–16 | NOT RUN | — |
| D decision brief | NOT RUN | — |

**Reason: Block C's own stop-condition.** The brief states that steps 12, 13, 14
and 14.5 "are NOT optional… If any of them cannot run, stop and report rather
than shipping an unaudited draft." The remaining session context cannot carry
fourteen further steps plus four adversarial critics, a gap-fetch wave, a
patcher and a cite-check pass. Proceeding would have produced precisely the
unaudited draft that constraint forbids, so the run was stopped here and
reported instead.

The corpus is now in the correct state to resume: 66 active notes, 56 at full
text, all novelty-bearing sources readable in full. Resumption starts at step 3
against this corpus — **not** at step 1, and **not** with a repeated width sweep.

---

## S1a session — scoping decision (recorded, not a skip)

**Steps 10, 11, 15 and 16 are intentionally NOT run.** They draft, synthesise
and polish a long-form report, which is not this project's deliverable. The
adversarial layer (12, 13, 14.5) runs in the next session **against the decision
brief** instead of against a drafted report. This is a deliberate scoping
decision by the operator, recorded here so that the absent artifacts are not
later mistaken for skipped steps or for pipeline failure.

## S1a — Block B (coverage audit and targeted gap-fill)

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| B.1 coverage audit | MANUAL | `research/temp/coverage-audit-s1a.md` | Rebuilt from scratch against the repaired corpus; S0 matrix explicitly distrusted. Q1 YES, Q2 PARTIAL, Q3 PARTIAL, Q4 YES, **Q5 NO**, Q6 PARTIAL |
| B.0 void stale artifacts | MANUAL | `research/temp/void/` + README | `step2-findings-summary.md` and `venue-findings-interim.md` moved and marked VOID — both written when 56% of corpus was abstract-only |
| B.2 gap-fill: Q2 quantisation | invoked (fetcher) | 5 notes + claims | **Gap CLOSED.** Direct hit: 4-bit bitsandbytes on Qwen2.5 0.5B–32B reduces lexical/syntactic diversity, worse at small scale |
| B.2 gap-fill: Q3 benchmark | invoked (fetcher) | 1 note + claims | **Gap CLOSED.** NAS-Bench-Suite-Zero: only a few of 13 zero-cost proxies generalise; synflow correlates 0.57 with model size |
| B.2 gap-fill: Q5 venue | invoked (fetcher) | `research/temp/venue-candidates.md` | dispatched; sweeping all 102 workshops for candidates + 7 fields per CFP |

Corpus: **78 → 94 notes.**

### Notable findings from Block B

1. **The quantisation rival is real but insufficient.** 4-bit measurably
   compresses lexical and syntactic diversity in exactly the model family and
   bit-width the subject paper used — but a mechanistic study finds 4-bit causes
   only mild "Signal Degradation", with catastrophic collapse reserved for 2-bit.
   Quantisation therefore cannot plausibly explain twenty *byte-identical*
   designs. This **relatively strengthens the sanitiser explanation**, which
   produces exact identity by construction. The rivals predict different
   magnitudes and are not interchangeable.

2. **The quantisation literature is contested, not settled.** QeRL finds
   quantisation noise *increases* sampling entropy during RL training. Any claim
   here must be stated as contested.

3. **Zero-cost proxy reliability bears on RZ-NAS priority.** RZ-NAS uses
   zero-cost proxies as its reflection signal; NAS-Bench-Suite-Zero shows single
   proxies generalise poorly and synflow partly measures model size. RZ-NAS's
   positive result is therefore contingent on proxy validity — narrowing, though
   not dissolving, its tension with the subject paper's negative result.

## S1b session

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| A venue sweep | invoked (fetcher, IN FLIGHT) | `research/temp/venue-candidates.md` (pending) | Agent from S1a still running at S1b entry; refined spec delivered mid-flight rather than restarting — hardened enumeration source, 5 additional required workshops, 11 fields, two-framing scope test |
| B steps 3–9 | NOT RUN | — | Stopped at the Block A boundary; see below |

### Block A — spec hardening delivered mid-flight

Rather than duplicate a running agent, the S1b requirements were sent to it:

1. **Enumeration source hardened.** Official NeurIPS blog list only
   (`announcing-the-neurips-2026-workshops-neurips-blog`). Aggregators may locate
   a workshop's site but are never evidence about its rules — NeurIPS has warned
   its own community that circulating lists are unaffiliated and unreliable.
2. **Scope test widened to two framings.** (a) does iterative feedback improve
   LLM-guided architecture search; (b) **how experimental instrumentation in
   LLM-driven research manufactures its own findings.** Framing (b) is what puts
   AI for Meta-Science, AI-Native Academia and XAI4Science in scope — none of
   which the earlier title-inspection shortlist would have surfaced.
3. **Fields expanded 7 → 11**, adding: what the page limit excludes, required
   footnote/template modification, checklist requirement, dual-submission policy,
   tracks offered, and author reviewing obligations. `NOT STATED` is mandatory
   where a page is silent — no inference, no carry-over from another workshop,
   no filling from general NeurIPS policy.

### Block B — not started, deliberately

Stopped at the Block A boundary under the session's own instruction: *"If context
runs short, stop at the last completed boundary and report — do not compress
remaining steps to fit."*

Steps 3–9 are seven steps, and step 5 alone spawns one depth-investigator per
locus (L1–L5 are operator-specified, so at least five). Beginning that chain with
the remaining budget would have produced a truncated depth investigation — the
step whose entire purpose is to read full sources carefully — and a contradiction
graph and loci set built to be consumed by steps that would never run.

**Entry state for the next session is unchanged and complete:** corpus 94 notes,
Q1/Q4 YES, Q2/Q3 closed by gap-fill, Q5 pending only the in-flight sweep. The
five operator-specified loci (L1 priority vs RZ-NAS; L2 rival magnitudes; L3
estimand; L4 independence; L5 RZ-NAS proxy validation) are recorded in the S1b
brief and carry forward verbatim.

### Block A — venue sweep FAILED (agent stalled), partial progress salvaged

**The sweep agent died**: `Agent stalled: no progress for 600s (stream watchdog
did not recover)`, while trying to resolve the exact CFP href for AI for
Meta-Science. **`research/temp/venue-candidates.md` was never written.**

**Q5 REMAINS OPEN.** No venue table exists. Nothing below should be read as a
venue answer.

Salvageable: 10 workshop CFP notes were fetched into the vault before the stall
and are usable by a future sweep, which should *not* re-fetch them:

| Note | Chars |
|---|---|
| `ai-for-meta-science-neurips-2026-workshop` | 8,359 |
| `managing-agents-that-manage-agents-…meta-agents…` | 13,592 |
| `axiom-2026-neurips-workshop` | 11,223 |
| `foundations-of-agentic-systems-theory` | 11,190 |
| `tae-neurips-2026-workshop-ai-evaluation-2` | 7,260 |
| `evaluation-of-interactive-agents-neurips-2026` | 7,050 |
| `opt-2026-optimization-for-machine-learning` | 6,282 |
| `call-for-papers-interpretability-as-a-science` | 5,871 |
| `verification-in-the-age-of-ai-scientists-ai-for-science-2` | 4,934 |
| `icbinb-bio-neurips-2026` | 4,191 |

Note the sweep surfaced candidates the earlier title-inspection shortlist missed
— **Meta-Agents**, **AXIOM**, **Foundations of Agentic Systems Theory**,
**Evaluation of Interactive Agents**, **OPT** — which is evidence the widened
two-framing scope test was doing real work before the agent died.

**Still unfetched from the required S1b shortlist:** AI-Native Academia,
XAI4Science, and confirmation of AutoMLR and EvoRobust status. **No note carries
the eleven required fields**, because the extraction pass never ran — the agent
died during fetching, before any structured recording.

**Disposition:** re-dispatch the sweep next session against the 10 salvaged notes
plus the missing shortlist. The failure is an agent-runtime stall, not a data or
access problem — every page it reached fetched cleanly.

## S1c session

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| A extraction pass | MANUAL (local read, no fetching) | `research/temp/venue-candidates.md` | 10 salvaged CFP notes → 11-field table; `NOT STATED` used throughout, nothing inferred |

### Block A findings

Two deadlines deviate from the Aug 29 default and would be missed by assuming
the common date: **Interpretability as a Science closes Aug 28** (one day
earlier) and **OPT closes Sep 4**.

Three eligibility constraints that bear on venue choice:

- **Interpretability as a Science requires at least one reciprocal reviewer per
  submission** — failure is grounds for rejection without review. That is a
  labour commitment, not just a deadline.
- **AI for Science requires released code/artifacts** for its Verifier Systems
  track (tracks A and B do not).
- **Meta-Agents treats a missing checklist statement as explicit grounds for
  desk rejection.**

Every workshop that states an archival policy states **non-archival**, and every
one that states an anonymity policy states **double-blind**. Four workshops state
neither: AI for Meta-Science, OPT, ICBINB-Bio, and (for anonymity)
Interpretability as a Science.

**Coverage is incomplete and the file says so.** Four required workshops were
never fetched — AI-Native Academia, XAI4Science, AutoMLR confirmation, EvoRobust
confirmation — plus three fetched in earlier sessions but not re-extracted to
these eleven fields (Who Verifies the Agents?, SLM-Agents, JUDGe). The table is
a partial substrate, not the shortlist.

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| 3 contradiction graph | MANUAL | `research/temp/contradiction-graph.json` | 5 ranked fight clusters, 4 consensus claims; built from claims files + prior findings, not by re-reading bodies (S1d context discipline) |
| 4 loci analysis | MANUAL | `research/loci.json` | 5 operator-specified loci, scored, budgets assigned |
| 5 depth investigation | invoked (2 subagents) | 2 interim notes (pending) | L1 and L5 dispatched in parallel |

### S1d scoping decision — three loci deferred to step 8

**L2, L3 and L4 are DEFERRED TO STEP 8** and handled by the corpus critic as
citation checks rather than by depth investigators. Recorded as a scoping
decision, not a skip.

Rationale: each is a *verification* problem against evidence already assembled,
not an open investigation.
- **L2** — the magnitude comparison is already quantified from the S1a gap-fill
  (4-bit = mild Signal Degradation; catastrophic Computation Collapse is 2-bit;
  RLHF collapse is graded; decoding effects partial by construction; only
  sanitiser coercion predicts exact identity). An investigator would re-derive a
  settled comparison.
- **L3** — the 1000-papers survey states the estimand explicitly. What needs
  checking is quotation accuracy and whether reviewer-expectation is over-read
  from one survey.
- **L4** — the serial dependence is established from the subject repo's own code
  (`audit/FORENSICS.md` F3), not from the literature; the literature only
  supplies the standard for valid inference.

**L1 and L5 went to investigators** because both require reading long full texts
and reaching a position that is genuinely not yet determined.

### Step 4 loci summary

| Locus | Type | Budget | Disposition |
|---|---|---|---|
| L1 priority vs RZ-NAS / agentic NAS | dialectical | 12 | step 5 investigator |
| L2 rival magnitudes for diversity collapse | mechanistic | 8 | deferred → step 8 |
| L3 estimand: mean vs expected-best-of-k | methodological | 6 | deferred → step 8 |
| L4 valid inference under serial dependence | methodological | 6 | deferred → step 8 |
| L5 RZ-NAS proxy validation | evidential | 6 | step 5 investigator |

Step 4 was run MANUAL rather than by spawning loci analysts: all five loci were
operator-specified verbatim, so analyst output was fully determined in advance
and spawning them would have re-derived a fixed answer at cost.

**Breadth caveat for the digest front matter:** source count is CLI-default, NOT
the contracted 100-130 — hyperresearch v0.8.5 has no `profile`/`gear` subcommand.

### Step 5 — L1 returned: `interim-report-l1-feedback-degradation-priority`

9 full-text vault notes read, zero new fetches, well inside the 12 budget.

**VERDICT: PARTIALLY SCOOPED — and by a different paper than assumed.**

**Correction to the prior characterisation.** Earlier sessions (and the S1d
locus brief) treated GENIUS's Section 6 "later iterations under-perform earlier
iterations" sentence as the leading scoop candidate. Read against its own
Appendix A.3 per-trial tables, that is wrong: **GENIUS's numbers show feedback
beating zero-shot in every reported trajectory.** The Section 6 remark describes
local mid-run non-monotonicity, not a net feedback-vs-zero-shot deficit. GENIUS
does not support "feedback hurts" — it is the *weakest* scoop candidate, not the
strongest.

**The real prior work is CoLLM-NAS** (arXiv 2509.26037v2, Sept 2025). Its
Generator-memory ablation isolates the identical structural variable the subject
paper instantiates — uncurated iteration history accumulating in a single
growing context vs. curated/reset state — and finds "progressive noise
accumulation, leading to performance degradation." Controlled and quantified,
not anecdotal.

**Evidence weight as reported:** 2 controlled ablations show feedback *helping*
under curated signals (RZ-NAS, EvoPrompting); 1 controlled ablation shows
uncurated context accumulation *hurting* (CoLLM-NAS); GENIUS is anecdotal and
does not net-contradict the "helps" camp; LLMatic motivates without ablating;
GPT-NAS has no textual feedback loop; the EC survey (May 2024) pre-dates the
question.

**Surviving formulation:** *"When an LLM's own uncurated iteration history
accumulates inside a single growing context — rather than being filtered into a
synthesized strategy or an external archive — iterative feedback degrades output
quality, especially as task complexity rises."* Already ablation-verified by
CoLLM-NAS, so the subject paper must cite and distinguish from it.

**Where novelty survives:** the small/quantised single-model regime, and the
template-collapse observation. **No source in this locus tests a sub-7B or
quantised model** — every ablation uses frontier-scale or fine-tuned
research-scale models (GPT-4o, 62B PaLM, purpose-fine-tuned GPT). Investigator
calls this "the cleanest gap the subject paper could claim."

**Honest caveats recorded by the investigator:** CoLLM-NAS is a single
un-peer-reviewed arXiv v2 preprint with no corroborating source in the corpus;
only one of several GENIUS appendix tables was sampled, and a full pass could
strengthen GENIUS as an independent scoop; RZ-NAS's proxy validity is handed to
L5.

### Step 5 — L5 returned: `interim-report-l5-rz-nas-zero-cost-proxy-validation`

4 vault must-reads + 3 fetched full texts (ZiCo, ZiCo-BC, Zen-NAS), both
permitted extra fetches used, settled within budget.

**VERDICT: the wedge HOLDS, and is broader than the query's citation anticipated.**

**(a) Which proxy.** RZ-NAS refines against a **single, experimenter-chosen
zero-cost proxy per run** — menu of five: GraSP, Gradnorm, Synflow, Zen-Score,
ZiCo (plus MAE-DET for COCO). **Not an ensemble.** It cites NAS-Bench-Suite-Zero's
ensemble-motivated warning *verbatim* and never acts on it.

**(b) Validation.** Rank-correlation validation is confined to **NAS-Bench-201 —
the one benchmark NAS-Bench-Suite-Zero itself flags as the easy case** where
nearly all proxies look fine. No cross-benchmark generalisation validation.

**(c) Does the size-confound apply.** Directly, to 2 of the 5:
- **Synflow** — 0.57–0.62 correlation with parameter count.
- **Zen-Score** — 0.68–0.99, the worst in NAS-Bench-Suite-Zero's entire table.
- **ZiCo**, which carries RZ-NAS's single flagship ImageNet claim: its margin
  over a naive `#Params` baseline **nearly vanishes** on the size-isolated
  NATS-Bench-SSS benchmark, and ZiCo-BC independently quantifies a depth/width
  bias worth 0.2–1.1 accuracy points.
- **GraSP** is the one proxy in the menu that is *not* size-confounded — though
  it is simply a weak proxy.

**Consequence for L1.** This narrows but does not eliminate RZ-NAS's priority:
the two papers may not be measuring the same underlying phenomenon. RZ-NAS's
ablation still shows "reflection beats no reflection"; what is now in question is
whether the *signal being reflected on* tracks architecture quality or largely
tracks model size.

**Flagged for step 8 (corpus critic), not chased:**
- No size-matched ablation exists for RZ-NAS itself. That single experiment
  would settle the causal question most directly.
- MAE-DET (the COCO proxy) is untested by any source in hand.
- **Self-report vs independent-reproduction discrepancy in Zen-Score's Kendall
  tau** — Zen-NAS's own paper reports 0.91/0.88; RZ-NAS's and ZiCo's independent
  numbers are 0.28–0.29. The critic must check apples-to-apples comparability
  before this is cited as evidence of systematic self-report inflation.

## S1e session

| Step | Mode | Artifacts | Notes |
|---|---|---|---|
| A push | MANUAL | — | **25 commits pushed**, head `9e53df5`; history audit clean (1 author, 1 committer, 0 attribution matches) |
| 6 cross-locus reconcile | MANUAL | `research/temp/comparisons.md` | 2-body reconciliation (L2/L3/L4 deferred); 6 seams recorded unsmoothed |

### Step 6 — the distinction that had to be held

**L5 does not defeat L1.** RZ-NAS's ablation compares reflection against no
reflection **holding the proxy fixed** — a confound in the shared signal is
common to both arms and cannot manufacture a difference between them. The
ablation's internal validity stands regardless of proxy validity, so L1's
refutation of the unqualified thesis survives. EvoPrompting's ablation (external
fitness selection, not a proxy) is untouched by L5 entirely.

What L5 attacks is **construct validity** — not whether the improvement exists,
but *what it is an improvement in*. Consequence: RZ-NAS and the subject paper may
not be measuring the same phenomenon, so RZ-NAS's counter-example status is
**narrowed in scope, not cancelled**.

### Six seams recorded (not smoothed)

- **S1** No source establishes whether a size-confounded proxy is *sufficient*
  for RZ-NAS's ablation to transfer to accuracy-based feedback. Nobody has asked.
- **S2** **Evidence-strength asymmetry:** the "partially scooped" verdict — the
  one with the most consequence for novelty — rests on a single un-peer-reviewed
  arXiv v2 (CoLLM-NAS). L5's verdict rests on a NeurIPS D&B paper plus two proxy
  papers. → step 8 C6.
- **S3** L1's GENIUS finding sampled one appendix table of several; a full pass
  could restore GENIUS as an independent scoop. L1 records this as a falsifier of
  its own position.
- **S4** **The surviving novelty claim — template collapse — was assessed by
  neither investigator.** L1 explicitly excludes it; L5 does not touch it. It
  rests on deferred L2 evidence and the repo audit's sanitiser finding.
- **S5** Zen-Score tau discrepancy is **UNUSABLE** until C5 clears it as
  apples-to-apples.
- **S6** MAE-DET size-confound status is **UNKNOWN**, not clean.
