# Coverage audit — S1a, against the REPAIRED corpus

Rebuilt from scratch after Block A. **Does not trust the S0 coverage matrix**,
which was computed when 56% of the corpus was abstract-only.

Corpus state: **66 active notes, 56 full text, 10 abstract-only.** All 10
abstract-only notes are web pages (workshop CFPs, GitHub pages, a search-results
page). **Zero paper-type sources are abstract-only.**

Verdict scale: **YES** = answerable at full-text depth now. **PARTIAL** = core
covered, a named sub-topic missing. **NO** = cannot be answered.

---

## Q1 — Novelty and priority — **YES**

Every named prior work is present at full text.

| Named in query | Note ID | Chars |
|---|---|---|
| EvoPrompting | `evoprompting-language-models-for-code-level-neural-archite` | 105,336 |
| GENIUS / "Can GPT-4 Perform NAS" | `can-gpt-4-perform-neural-architecture-search` | 61,852 |
| LLMatic | `230601102v8-llmatic-neural-architecture-search-via-large-l` | 53,492 |
| GPT-NAS | `230505351v4-gpt-nas-evolutionary-neural-architecture-searc` | 71,935 |
| **RZ-NAS (ICML 2025)** | `icml-poster-rz-nas-enhancing-llm-guided-neural-architectur` | 77,678 |
| agentic/multi-agent NAS 2025-26 | `250926037v2-collm-nas-…` (75,905); `241002189-agent-oriented-planning-…` (81,445) | — |
| LLM+EA landscape | `240110034v3-evolutionary-computation-in-the-era-of-large-l` | 142,572 |
| NAS field survey | `neural-architecture-search-insights-from-1000-papers` | 201,141 |

Supporting stubs retained: `rz-nas-enhancing-…` (5,537, ABSTRACT-ONLY),
`github-pasalabrz-nas-github` (3,365, ABSTRACT-ONLY),
`rz-nas-…-at-duckduckgo` (3,746, ABSTRACT-ONLY) — **the RZ-NAS full text lives
in the ICML poster note**; cite that one, not the stubs.

## Q2 — Mechanism literature — **PARTIAL**

Self-correction and diversity-collapse literature is comprehensively full text.
**One named sub-topic has zero sources.**

| Sub-topic | Coverage |
|---|---|
| Intrinsic self-correction fails | `large-language-models-cannot-self-correct-reasoning-yet` (57,695); `231001798-…` (11,745); `when-can-llms-actually-correct-their-own-mistakes…` (97,413); `on-the-self-verification-limitations-…` (63,836); `231108516-llms-cannot-find-reasoning-errors…` (56,653); `230511738-critic-…` (227,722); `240201817-llms-cant-plan-…` (64,738) |
| Scale dependence | `241202674-mind-the-gap-…` (114,955) — generation–verification gap vs pretraining FLOPs |
| Self-repair modest/absent | `230609896-is-self-repair-a-silver-bullet…` (136,324) |
| RLHF diversity loss | `understanding-the-effects-of-rlhf-…` (111,558) |
| Mode collapse | `240204477v1-detecting-mode-collapse-…` (8,369) |
| Decoding temperature / diversity | `161002424-diverse-beam-search` (53,377); `240105054v2-generating-diverse-…` (110,774); `260111227v2-language-of-thought-…` (70,258) |
| **Quantisation → diversity** | ❌ **ZERO SOURCES** |

**GAP 1.** The query names "output-diversity loss under RLHF **and
quantisation**". The subject model is 4-bit NF4. Quantisation is an untested
rival explanation for the paper's headline, and the corpus cannot currently
speak to it. → gap-fill dispatched.

## Q3 — Methodology standards — **PARTIAL**

| Named in query | Note ID | Chars |
|---|---|---|
| Li & Talwalkar | `190207638-random-search-…` (85,525); `random-search-and-reproducibility-…` (83,399) | — |
| Yang et al. | `nas-evaluation-is-frustratingly-hard` | 47,936 |
| NAS-Bench-101 | `190209635v2-nas-bench-101-…` | 59,575 |
| NAS-Bench-201 | `200100326v2-nas-bench-201-…` | 66,763 |
| NATS-Bench | `200900437v6-nats-bench-…` | 74,957 |
| **NAS-Bench-Suite-Zero** | ❌ **ZERO SOURCES** | — |
| Lindauer & Hutter checklist | `best-practices-for-scientific-researchon-…` (53,690); `190902453v3-…` (10,672) | — |
| Sciuto et al. | `evaluating-the-search-phase-of-neural-architecture-search` | 61,743 |
| Seeds / statistical power | `180608295-how-many-random-seeds-…` (42,933); `210813264-deep-reinforcement-learning-at-the-edge-…` (104,470); `230401910-on-the-variance-…` (74,713) | — |
| Estimand (expected-best-of-k) | `neural-architecture-search-insights-from-1000-papers` | 201,141 |

**GAP 2.** NAS-Bench-Suite-Zero is named explicitly in the query and absent
entirely. It also bears on Q1/Q4: RZ-NAS uses zero-cost proxies as its feedback
signal, so proxy reliability is load-bearing. → gap-fill dispatched.

## Q4 — Counter-evidence — **YES**

Every strong counter-case is present at full text.

| Counter-case | Note ID | Chars |
|---|---|---|
| FunSearch (Nature) | `mathematical-discoveries-from-program-search-…` | 72,786 |
| AlphaEvolve | `250613131v1-alphaevolve-…` | 136,078 |
| Evolution through Large Models | `220608896v1-evolution-through-large-models` | 128,870 |
| Self-Refine | `230317651v2-self-refine-…` | 129,319 |
| Reflexion | `230311366v4-reflexion-…` | 64,221 |
| OPRO | `230903409-large-language-models-as-optimizers` | 155,345 |
| RZ-NAS | `icml-poster-rz-nas-…` | 77,678 |
| CoLLM-NAS | `250926037v2-collm-nas-…` | 75,905 |
| EvoPrompting ablation | `evoprompting-…` | 105,336 |

## Q5 — Venue — **NO**

The single genuine failure. The width sweep was academic-API-first; workshop
calls are web pages.

Present: the official 102-workshop list
(`announcing-the-neurips-2026-workshops-neurips-blog`, 10,585) and six candidate
CFPs — `who-verifies-the-agents-…` (6,202), `slm-agents-…` (6,341),
`workshop-for-autonomous-machine-learning-research-…` (12,135),
`judge-2026-can-we-trust-the-judge` (10,931),
`verification-in-the-age-of-ai-scientists-…` (6,446),
`call-for-papers-automl-2026` (11,283).

Missing or inadequate:

- **EvoRobust** — no note at all, despite being a leading topical candidate.
- **TAE** (4,706) and **Interpretability as a Science** (2,071) — ABSTRACT-ONLY,
  fields not extractable.
- **No systematic sweep** of the 102-workshop list. Six candidates were chosen
  by title inspection, not by scanning the full list.
- The seven required fields (scope, page limit, template, anonymity, archival,
  mechanics, negative-results stance) are not recorded uniformly for any
  candidate.

→ gap-fill dispatched; output to `research/temp/venue-candidates.md` as
facts-and-URLs only.

## Q6 — Framing — **PARTIAL (derivative)**

Directly supported by `240603980-position-embracing-negative-results-in-machine-l`
(58,796), which argues predictive performance alone is an inadequate publication
criterion. Otherwise Q6 is a synthesis of Q1–Q5 and inherits their gaps: it
cannot be settled until Q2's quantisation rival and Q5's venue facts are in.

---

## Summary

| Q | Verdict | Gap |
|---|---|---|
| 1 Novelty | **YES** | — |
| 2 Mechanism | **PARTIAL** | quantisation → diversity: zero sources |
| 3 Methodology | **PARTIAL** | NAS-Bench-Suite-Zero: zero sources |
| 4 Counter-evidence | **YES** | — |
| 5 Venue | **NO** | EvoRobust absent; 2 thin; no systematic sweep; fields not recorded |
| 6 Framing | **PARTIAL** | derivative of Q2 and Q5 |

Two gap-fill waves dispatched, scoped to these gaps only. No other fetching.
