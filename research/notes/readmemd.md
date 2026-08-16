---
title: README.md
id: readmemd
tags:
- llm-nas-feedback-positioning-7125b1
- rz-nas
- evolutionary-search
- zero-cost-proxy
created: '2026-08-16T15:52:51.552259Z'
updated: '2026-08-16T15:53:13.805566Z'
source: https://raw.githubusercontent.com/PasaLab/RZ-NAS/main/README.md
source_domain: raw.githubusercontent.com
fetched_at: '2026-08-16T15:52:51.551767Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Official GitHub README (PasaLab/RZ-NAS) for the RZ-NAS ICML 2025 paper.
  Confirms the method: Reflective Zero-cost NAS uses structured prompts (role + instructions
  + in-context example + reflective module) so an LLM understands NAS tasks/architectures
  at text and code levels, replacing full training with zero-cost proxy metrics for
  efficiency, and using LLM-generated reflective feedback as linguistic guidance during
  architecture optimization via evolutionary search (evolution_search.py, configurable
  zero_shot_score proxy and search_space). This is the code-level confirmation that
  RZ-NAS''s ''feedback'' loop is embedded inside an evolutionary mutation-selection
  process scored by cheap zero-cost proxies, not full retraining accuracy or a single
  sequential self-refinement chain -- an important methodological contrast to the
  target paper''s claimed iterative-feedback degradation, since RZ-NAS''s search process
  can discard a bad LLM-suggested mutation via selection rather than being forced
  to accept it as the new baseline.'
---

*Suggested by [[rz-nas-icml-2025-reflective-zero-cost-nas-at-duckduckgo]] — official code repository README for RZ-NAS*

# RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy

## About
This is the repository for the paper RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy. 

LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose Reflective Zero-cost NAS (RZ-NAS) that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs' roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search task and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks. 

## Search

One example of the whole prompt is saved in `template.txt`. More zero-cost proxies and search spaces are saved under the folder `descriptions`. 

For different zero-cost proxies, you can change the parameter `zero_shot_score`.

```
python evolution_search.py --gpu 0 --zero_shot_score
--search_space
```

more customized parameters setting can be found in ./scripts.