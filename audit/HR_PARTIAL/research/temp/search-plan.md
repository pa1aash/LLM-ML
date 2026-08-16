# Search plan — llm-nas-feedback-positioning-7125b1

Three lenses per atomic item: **A breadth**, **B depth/canonical**, **C
adversarial**. Lens D (period-pinned primary sources) applies to the two
`time_periods` entries — ICML 2025 (RZ-NAS) and NeurIPS 2026 (workshop CFPs) —
where the primary source is the proceedings entry or the live CFP page, not
commentary about it.

| Atomic item | Search query | Type | Lens | Target |
|---|---|---|---|---|
| **Q1 novelty — core** | LLM neural architecture search feedback degrades | academic | breadth | factual |
| Q1 | large language model guided NAS negative result ablation | academic | breadth | factual |
| Q1 | LLM architecture search iterative refinement no improvement | academic | adversarial | contrarian |
| Q1 | when does LLM feedback hurt search | web | adversarial | contrarian |
| Entity: EvoPrompting | EvoPrompting language models code-level neural architecture search | academic | depth | canonical |
| Entity: EvoPrompting | EvoPrompting limitations criticism | web | adversarial | contrarian |
| Entity: GENIUS | Can GPT-4 Perform Neural Architecture Search | academic | depth | canonical |
| Entity: GENIUS | GENIUS GPT-4 NAS reproducibility criticism | web | adversarial | contrarian |
| Entity: LLMatic | LLMatic neural architecture search large language models quality diversity | academic | depth | canonical |
| Entity: GPT-NAS | GPT-NAS generative pre-trained model neural architecture search | academic | depth | canonical |
| Entity: RZ-NAS | RZ-NAS reflective zero-cost neural architecture search ICML 2025 | academic | depth | canonical |
| Entity: RZ-NAS | RZ-NAS ICML 2025 proceedings entry | web | **D period-pinned** | primary |
| Entity: agentic NAS | agentic neural architecture search LLM agent 2025 | academic | breadth | factual |
| Entity: multi-agent NAS | multi-agent LLM neural architecture search 2026 | academic | breadth | factual |
| Q1 scoop risk | LLM NAS ablation removing feedback performance | academic | adversarial | contrarian |
| **Q2 mechanism — core** | LLM self-correction when it helps when it hurts | academic | breadth | factual |
| Q2 | intrinsic self-correction fails without external feedback | academic | depth | canonical |
| Q2 | Large Language Models Cannot Self-Correct Reasoning Yet | academic | depth | canonical |
| Q2 | When Can LLMs Actually Correct Their Own Mistakes critical survey | academic | depth | canonical |
| Q2 | self-refinement degrades performance LLM | academic | adversarial | contrarian |
| Q2 scale | self-correction model scale dependent emergent ability | academic | breadth | factual |
| Q2 scale | small language model self-correction failure | academic | adversarial | contrarian |
| Entity: mode collapse | LLM mode collapse output diversity | academic | breadth | factual |
| Entity: RLHF diversity | RLHF reduces output diversity language model | academic | depth | canonical |
| Entity: RLHF diversity | alignment diversity tradeoff criticism | web | adversarial | contrarian |
| Entity: quantisation | quantization effect on LLM output diversity generation | academic | breadth | factual |
| Entity: quantisation | 4-bit quantization degrades generation quality NF4 | academic | adversarial | contrarian |
| Entity: temperature | decoding temperature diversity quality tradeoff sampling | academic | depth | canonical |
| Entity: temperature | temperature sampling diversity collapse structured output JSON | web | breadth | factual |
| **Q3 methodology — core** | NAS evaluation standards reproducibility 2025 | academic | breadth | factual |
| Entity: Li & Talwalkar | Random Search and Reproducibility for Neural Architecture Search | academic | depth | canonical |
| Entity: Yang et al. | NAS Evaluation is Frustratingly Hard | academic | depth | canonical |
| Q3 critiques | neural architecture search evaluation critique methodological flaws | academic | adversarial | contrarian |
| Q3 critiques | NAS random search baseline as strong as | academic | adversarial | contrarian |
| Entity: NAS-Bench-101 | NAS-Bench-101 reproducible neural architecture search benchmark | academic | depth | canonical |
| Entity: NAS-Bench-201 | NAS-Bench-201 extending scope reproducible NAS | academic | depth | canonical |
| Entity: NATS-Bench | NATS-Bench benchmarking architecture topology size | academic | depth | canonical |
| Entity: NAS-Bench-Suite-Zero | NAS-Bench-Suite-Zero zero-cost proxies benchmark | academic | depth | canonical |
| Q3 estimand | expected best of k fixed budget search evaluation estimand | academic | breadth | factual |
| Q3 estimand | best-of-n sampling evaluation metric search method | academic | breadth | factual |
| Q3 estimand | mean versus max performance comparing search algorithms | academic | adversarial | contrarian |
| Q3 seeds | random seed variance deep learning evaluation number of seeds | academic | breadth | factual |
| Q3 seeds | statistical significance testing deep learning comparisons | academic | depth | canonical |
| Q3 independence | sequential dependence violates independence statistical test | academic | breadth | factual |
| Q3 independence | in-context sequential generation autocorrelation LLM samples | academic | adversarial | contrarian |
| **Q4 counter-evidence** | LLM feedback improves neural architecture search results | academic | breadth | factual |
| Q4 | FunSearch mathematical discoveries program search LLM | academic | depth | canonical |
| Q4 | AlphaEvolve evolutionary coding agent | academic | breadth | factual |
| Q4 | Self-Refine iterative refinement with self-feedback | academic | depth | canonical |
| Q4 | Reflexion verbal reinforcement learning | academic | depth | canonical |
| Q4 | LLM evolutionary optimization improvement over random | academic | breadth | factual |
| Q4 | self-repair code generation silver bullet | academic | adversarial | contrarian |
| Q4 | evolution through large models ELM | academic | depth | canonical |
| Q4 bound | execution feedback versus intrinsic feedback LLM improvement | academic | adversarial | contrarian |
| **Q5 venue** | NeurIPS 2026 workshops list call for papers | web | **D period-pinned** | primary |
| Q5 | NeurIPS 2026 workshop AutoML automated machine learning | web | breadth | factual |
| Q5 | NeurIPS 2026 workshop AI for science agentic | web | breadth | factual |
| Q5 | NeurIPS workshop negative results replication call for papers | web | breadth | factual |
| Q5 | I Can't Believe It's Not Better workshop NeurIPS | web | depth | canonical |
| Q5 | NeurIPS workshop archival non-archival policy anonymity | web | breadth | factual |
| Q5 | AutoML conference 2026 call for papers | web | breadth | factual |
| Q5 | workshop on efficient systems foundation models NeurIPS 2026 | web | breadth | factual |
| Q5 adversarial | criticism of workshop paper value non-archival | web | adversarial | contrarian |
| **Q6 framing** | positioning negative results machine learning publication bias | academic | breadth | factual |
| Q6 | how to publish a null result machine learning | web | breadth | factual |
| Q6 | criticism of underpowered negative results ML | academic | adversarial | contrarian |

## Search gap check against `research/temp/coverage-matrix.md`

Every coverage-matrix row maps to ≥1 planned search. Checked specifically for
the failure modes the skill names:

- **"architecture *or program* search"** — NOT narrowed to NAS. FunSearch,
  AlphaEvolve, ELM, Self-Refine and self-repair searches are planned under Q4.
- **"automated design"** for venue fit — NOT narrowed to NAS workshops. AutoML,
  AI-for-science, agentic, and negative-results workshops are all planned.
- **RLHF vs quantisation** — separate search rows, not one bundled query.
- **NAS-Bench-101 vs 201** — separate rows.
- **Li & Talwalkar vs Yang et al.** — separate rows.
- **"as it actually stands now"** (NeurIPS 2026) — flagged Lens D so it is
  fetched live rather than answered from recall.

**Adversarial searches planned: 17** (minimum required: 5).

Total planned searches: **68**.
