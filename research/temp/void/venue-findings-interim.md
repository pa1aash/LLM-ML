# Venue findings — NeurIPS 2026 workshops (INTERIM, step 2 evidence)

**Status:** interim extraction from the fetched primary source. Not yet the
final Q5 answer — per-workshop page limits, anonymity policies, archival status
and CFP URLs still need fetching from each workshop's own site (the announcement
explicitly says "we typically let each workshop advertise its own call for
papers"). Recorded now because it carries a near-term deadline.

**Primary source:** [[announcing-the-neurips-2026-workshops-neurips-blog]] —
https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/
(published Aug 10, 2026)

---

## ⏰ The deadline is 13 days away

> "Several workshops have begun soliciting submissions, many using our
> **suggested submission date of Aug 29, 2026**."

Today is **2026-08-16**. That is **13 days**. Workshop dates: Sydney Fri 11 –
Sat 12 Dec 2026; Paris and Atlanta Sat 12 – Sun 13 Dec 2026.

This changes the S2 calculus materially. The audit found five blocking actions
(`audit/OPEN_ACTIONS.md`), of which OA-1 — does the raw experimental data still
exist — governs everything. **A 13-day runway is not enough to rebuild the
experiment, but it may be enough for claim surgery** *if* the data is
recoverable. If it is not recoverable, submitting a paper whose headline numbers
are 26% ORPHAN would be indefensible.

## Scale and selectivity

102 workshops accepted from 477 submissions (454 valid) — 48 Sydney, 28 Paris,
26 Atlanta. Proposal acceptance rates 21.5% / 25.4% / 23.6%. Note these are
*workshop proposal* acceptance rates, not paper acceptance rates.

The announcement also warns: *"we would like to warn everyone against any
informal workshop lists circulating on the internet — these lists are not
affiliated with NeurIPS and do not contain reliable information."* The list
below is transcribed from the official announcement only.

---

## Candidate workshops for this paper, by fit

### Tier 1 — direct topical fit

| Workshop | Location | Why it fits |
|---|---|---|
| **Self-Evolving Diversity-Driven Search for Robust AI Systems** | Sydney | The single closest match found. The paper *is* a study of self-evolving search and of diversity collapse under refinement. Both of the paper's claims sit inside this scope. |
| **Workshop for Autonomous Machine Learning Research** | Sydney | LLM-driven autonomous ML research — LLM-guided architecture design is squarely in scope. |
| **SLM-Agents: 1st Workshop on SLMs for Agentic Systems** | Paris | Explicitly about **small** language models in agentic loops. The paper's subject is a 1.7B 4-bit model in an iterative loop; a negative result about small-model self-refinement is directly on-topic, and model scale is the paper's own stated limitation (i). |

### Tier 2 — methodology / evaluation angle

| Workshop | Location | Why it fits |
|---|---|---|
| **Trustworthy AI Evaluation (TAI-Eval)** | Sydney | If the paper is reframed around the estimand problem (mean vs expected-best-of-*k*) and independence violations, it becomes an evaluation-methodology contribution. |
| **Who Verifies the Agents? Toward Reliable Agent Development** | Sydney | Maps onto the "intrinsic self-correction fails without external verification" thesis. |
| **Can We Trust the Judge? Building Reliable Evaluation for Language Models** | Atlanta | Evaluation reliability; adjacent but LLM-judge-focused rather than search-focused. |
| **Interpretability as a Science: Toward Rigorous Foundations for Understanding LLMs** | Sydney | Rigour-of-method framing. Weaker fit — interpretability, not search. |

### Tier 3 — adjacent

| Workshop | Location | Note |
|---|---|---|
| **Foundations of Agentic Systems Theory** | Paris | Theory-leaning; an empirical null may not fit. |
| **AI for Meta-Science: Scaling and Organizing Science in the Age of AI Scientists** | Paris | About AI doing science; the paper is a case study of AI failing to do design. |
| **AI for Science: Verification in the Age of AI Scientists** | Sydney | Verification framing, science-application-oriented. |
| **AI & Science: Evolution or Extinction?** | Atlanta | Broad/positional. |

### Explicitly NOT a fit — correcting an obvious assumption

**I Can't Believe It's Not Better (ICBINB)** runs at NeurIPS 2026 (Sydney), and
ICBINB is the canonical negative-results venue — but this year it is scoped as
**"ICBINB: Failure Modes of AI in Biology."** A CNN-architecture-search null
result is out of scope. This is exactly the kind of assumption that would have
been wrong if answered from recall rather than fetched.

---

## What still must be fetched before Q5 can be answered

The announcement does not carry per-workshop details. For each Tier 1–2
candidate, still needed:

1. scope statement (from the workshop's own site)
2. page limit
3. format requirements (NeurIPS style?)
4. anonymity policy (double-blind assumed but must be confirmed per workshop)
5. archival status (NeurIPS workshops are typically non-archival — confirm)
6. submission mechanics (OpenReview link)
7. any stated position on negative results, replication, or evaluation critiques
8. the CFP URL itself

**None of these may be inferred.** Wave 2 must fetch each workshop's page.

---

## Standing NeurIPS 2026 facts confirmed from the primary source

- Main conference: Sydney, Dec 6–12, 2026. Satellites: Atlanta and Paris, Dec 9–13.
- Workshop mandatory accept/reject notification date: **Sep 29, 2026**.
- Paper author notifications (main track): Sep 24, 2026.
- Workshop chairs: Piotr Koniusz (senior), Theodore Papamarkou, Khoa D. Doan,
  Shao-Hua Sun, Elisa Ricci, Ghada Zamzmi.

---

# UPDATE — per-workshop CFPs fetched (supersedes the tiering above)

115 NeurIPS 2026 workshop groups are live on OpenReview
(`api2.openreview.net/groups?parent=NeurIPS.cc/2026/Workshop`). Seven candidate
CFPs were fetched directly. **Two corrections to the interim tiering, both
material.**

## ❌ Correction 1 — AutoMLR is NOT a fit

"Workshop for Autonomous Machine Learning Research" requires that **the paper
itself be substantially produced by an autonomous agent, end-to-end.** It is not
a venue for human-written papers *about* using an LLM as a design tool. The
interim note ranked it Tier 1 on the title alone. **Removed.**

## ⚠️ Correction 2 — EvoRobust has no live CFP

"Self-Evolving Diversity-Driven Search for Robust AI Systems" — the interim
note's "single closest match" — has **no dedicated website yet**; its OpenReview
`website` field still points at the generic conference page. Confirmed metadata:
Sydney, deadline **Aug 30 2026, 12:29 UTC**, contact
`evorobust-workshop@googlegroups.com`. Still plausibly the best *topical* fit,
but nothing can be confirmed about page limit, format, or archival status.
**Watch, or email the organisers.**

## Ranked candidates, on fetched evidence

| # | Workshop | Loc | Page limit | Anon | Archival | Deadline | Verdict |
|---|---|---|---|---|---|---|---|
| **1** | **Who Verifies the Agents? Toward Reliable Agent Development** | Sydney | 4–9 pp | double-blind | non-archival | — | **Best confirmed match.** Topic list names *"Self-evolving agents: stable improvement without collapse"* and *"Evaluation of agent-generated designs vs. human-engineered systems"* — both are literally this paper. Dual-submission friendly. |
| **2** | **SLM-Agents: 1st Workshop on SLMs for Agentic Systems** | Paris | 4 or 6 pp | double-blind | non-archival | **Aug 29 2026** | **Quantisation and compression explicitly in scope.** The subject model is 1.7B 4-bit — the venue's core population. Scale-dependence becomes a feature, not limitation (i). |
| **3** | EvoRobust (Self-Evolving Diversity-Driven Search) | Sydney | unknown | unknown | unknown | **Aug 30 2026** | Best topical fit on title; **no CFP published**. Contact organisers before relying on it. |
| **4** | Trustworthy AI Evaluation (TAE) | Sydney | not stated | not stated | not stated | — | Scope names *"stability under seeds, data splits"* verbatim — directly the paper's weakest axis. Details missing from the page. |
| **5** | JUDGe: Can We Trust the Judge? | Atlanta | — | — | — | — | **The only venue with an explicit, repeated stated welcome for negative results** — but scoped to LLM-judge/reward-model reliability, not search loops. Strong policy fit, weak topical fit. |
| 6 | AI for Science: Verification in the Age of AI Scientists | Sydney | 4–8 pp | — | non-archival | — | Thematic only; no domain science here. |
| 7 | Interpretability as a Science | Sydney | not stated | not stated | not stated | — | Thin page (280 words). Weakest. |

## Recommendation

**Primary: "Who Verifies the Agents?"** — its call names this paper's exact
subject matter, it is non-archival (so an extended version stays submittable),
double-blind, and dual-submission friendly.

**Secondary: SLM-Agents** — turns the paper's biggest stated weakness (a small
quantised model) into the venue's central interest, and its **Aug 29** deadline
is the binding constraint.

Both are 4–9 pages against a current 10-page PDF (`OA-26`). Non-archival status
means neither forecloses a later archival submission.

**Standing caveat:** every candidate is double-blind and none has a
reproducibility-artifact requirement — unlike AutoML 2026, which is both closed
and artifact-gated. But `OA-1` still governs: submitting headline numbers that
are 26% ORPHAN is a decision to make deliberately, not by default.
