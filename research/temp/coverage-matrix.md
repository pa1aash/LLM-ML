# Coverage Matrix — query phrase → atomic item mapping

Walked phrase by phrase through
`research/query-llm-nas-feedback-positioning-7125b1.md`.

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| "deep, adversarial positioning analysis" | scope_conditions: register analyze, inference_depth deep, adversarial searches for every adopted position | OK | No |
| "a small quantised LLM's zero-shot architecture proposals beat random search" | scope_conditions: subject paper claim (i) | OK — retained as the paper's claim, not adopted as true | No |
| "in a CNN search space" | scope_conditions: custom CNN space, not tabular | OK — matters for Q3 benchmark expectations | No |
| "collapsing to a single template" | Sub-Q13–16 (four rival explanations); entity: mode collapse | OK — treated as an explanandum with rivals, not a finding | No |
| "iterative performance feedback degrades rather than improves" | Sub-Q1; scope_conditions: subject paper claim (ii) | OK | No |
| "Register: analyze" | scope_conditions | OK | No |
| "inference_depth: deep" | scope_conditions; pipeline_tier full | OK | No |
| "Answer six questions and commit to a position on each" | required_formats: commit to explicit position ×6; required_section_headings ×6 | OK — one H2 per question, prompt order | No |
| "FIRST, novelty" | heading 1; Sub-Q1, Sub-Q2 | OK | No |
| "already been published or partially scooped" | Sub-Q1 (published) AND Sub-Q2 (partially scooped) | OK — both readings covered separately | No |
| "between 2023 and 2026" | time_horizons: 2023-2026 novelty window | OK | No |
| "EvoPrompting" | entity, prior-work | OK | No |
| "GENIUS/'Can GPT-4 perform neural architecture search'" | entity, prior-work (both names) | OK — alias captured | No |
| "LLMatic" | entity, prior-work | OK | No |
| "GPT-NAS" | entity, prior-work | OK | No |
| "RZ-NAS (ICML 2025, reflective zero-cost strategy)" | entity + time_periods: ICML 2025 | OK — venue is a checkable claim, pinned as a period | No |
| "agentic and multi-agent NAS work from 2025-2026" | entity (category); time_horizons 2025-2026 | OK — both "agentic" and "multi-agent" retained | No |
| "any LLM-NAS ablation reporting a null or negative effect of feedback" | Sub-Q9; entity (category) | OK — the sharpest priority threat; kept as its own item | No |
| "SECOND, mechanism literature" | heading 2 | OK | No |
| "when LLM self-correction helps versus hurts" | Sub-Q10 | OK — both directions | No |
| "whether the effect is model-scale dependent" | Sub-Q11 | OK | No |
| "'intrinsic self-correction fails without external verification' is now settled" | Sub-Q12 | OK | No |
| "reads as confirmatory rather than novel" | Sub-Q12 (second clause) | OK — this is the positioning consequence, retained | No |
| "mode collapse" | Sub-Q13; entity | OK | No |
| "output-diversity loss under RLHF and quantisation" | Sub-Q14 (RLHF) + Sub-Q15 (quantisation) | OK — split; the phrase bundles two distinct mechanisms | No |
| "decoding-temperature effects on generation diversity" | Sub-Q16; entity | OK | No |
| "rival explanations for a model producing twenty identical designs" | framing of Sub-Q13–16 | OK | No |
| "THIRD, methodology standards" | heading 3 | OK | No |
| "what do NAS reviewers in 2025-2026 demand" | Sub-Q17–21; time_horizons 2025-2026 | OK | No |
| "tabular benchmarks (NAS-Bench-101/201, NATS-Bench, NAS-Bench-Suite-Zero)" | entities ×4 (101 and 201 split) | OK — "101/201" expanded to two benchmarks | No |
| "sample sizes and seeds" | Sub-Q18 | OK — both | No |
| "mean-of-population and expected-best-of-k under a fixed budget as the correct estimand" | Sub-Q19 | OK — this is the estimand question; load-bearing for the subject paper | No |
| "statistical independence when proposals are generated sequentially in one context" | Sub-Q20 | OK | No |
| "random-search baselines after Li and Talwalkar and Yang et al." | Sub-Q21; entities ×2 | OK — both authors as separate critique entities | No |
| "strongest published methodological critiques of NAS evaluation" | Sub-Q22 | OK — broader than the two named; kept general | No |
| "state which of them this paper would fail" | Sub-Q23 | OK — demands a verdict, not a survey | No |
| "FOURTH, counter-evidence" | heading 4 | OK | No |
| "strongest existing results AGAINST the paper's thesis" | Sub-Q24 | OK | No |
| "iterative LLM feedback measurably improved architecture or program search" | Sub-Q24 | OK — "or program search" retained; NOT narrowed to NAS alone | No |
| "defeat the claim, bound it, or merely differ in scale" | Sub-Q25 | OK — three-way verdict preserved | No |
| "FIFTH, venue" | heading 5 | OK | No |
| "map the NeurIPS 2026 workshop landscape as it actually stands now" | Sub-Q26; time_periods NeurIPS 2026 | OK — "as it actually stands now" forces live CFP fetches, not recall | No |
| "controlled negative/null result about LLM self-refinement in automated design" | Sub-Q27 | OK — "automated design" kept broader than NAS | No |
| "scope statement, page limit, format requirements, anonymity policy, archival status, submission mechanics" | entity required_fields ×6 | OK — all six as separate fields | No |
| "any stated position on negative results, replication, or evaluation critiques" | entity required_field | OK — all three sub-topics | No |
| "with the call-for-papers URL for each" | entity required_field | OK | No |
| "then rank them for this specific paper and defend the ranking" | Sub-Q28, Sub-Q29 | OK — ranking AND defence | No |
| "SIXTH, framing" | heading 6 | OK | No |
| "strongest defensible thesis this evidence base can support" | Sub-Q30 | OK | No |
| "what claim would have to be abandoned" | Sub-Q31 | OK | No |
| "what single additional experiment would most raise acceptance probability" | Sub-Q32 | OK — "single" preserved; demands one, not a list | No |
| "Prioritise arXiv, OpenReview, ICML/NeurIPS/ICLR proceedings and workshop pages over secondary commentary" | scope_conditions | OK | No |
| "run explicit adversarial searches for criticism and failed replications of every position you adopt" | scope_conditions; required_formats | OK — applies to every position, not just the thesis | No |

## Result

**58 phrases mapped. Zero `Gap? = YES` rows.**

Two phrases were deliberately **split** rather than mapped one-to-one, because
the natural scope of each covers two distinct things:

1. *"output-diversity loss under RLHF and quantisation"* → two sub-questions.
   RLHF-induced diversity collapse and quantisation-induced diversity collapse
   are separate literatures with separate evidence, and the subject model is
   both instruction-tuned and 4-bit quantised, so both rivals apply
   independently.
2. *"NAS-Bench-101/201"* → two benchmark entities.

Two phrases were deliberately **kept broad** against a tempting narrowing:

1. *"architecture or program search"* (Q4) is NOT narrowed to NAS. FunSearch,
   AlphaEvolve-class program search, and code-repair self-refinement all
   qualify as counter-evidence and are among the strongest cases against the
   thesis.
2. *"automated design"* (Q5) is NOT narrowed to NAS, since the best-fitting
   workshops are likely AI-for-science / agentic / AutoML venues rather than a
   NAS-specific one.
