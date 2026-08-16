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
