---
title: 'ICML Poster RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective
  Zero-Cost Strategy'
id: icml-poster-rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflectiv
tags:
- llm-nas-feedback-positioning-7125b1
- rz-nas
- counter-evidence
- llm-guided-nas
created: '2026-08-16T15:49:25.950417Z'
updated: '2026-08-16T15:51:02.685765Z'
source: https://icml.cc/virtual/2025/poster/46224
source_domain: icml.cc
fetched_at: '2026-08-16T15:49:25.949321Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'ICML 2025 poster/lay-summary page for RZ-NAS, adding mechanism detail beyond
  the PMLR abstract. Key sentence: ''The reflective module guides the LLM to reflect
  on mutation performance and generates targeted suggestions for further iteration
  improvements'' -- i.e., RZ-NAS embeds LLM feedback INSIDE an iterative evolutionary
  mutation loop (not a single zero-shot proposal), where the LLM is shown how a prior
  mutation performed (via zero-cost proxy score, not full training) and asked to suggest
  the next mutation. Structured prompts combine a role, instructions, an in-context
  example, and the reflective module itself, operating at both text and code levels.
  This is architecturally the closest published analogue to the target paper''s iterative-feedback
  condition, but differs in three load-bearing ways worth flagging for the counter-evidence
  question: (1) feedback signal is a zero-cost proxy metric, not full trained accuracy,
  so the informativeness of the feedback differs; (2) mutations are evaluated via
  evolutionary selection (the pipeline can discard a bad LLM-suggested mutation),
  unlike a pure sequential-refinement setup where each output must be treated as the
  new baseline; (3) the base LLM''s scale/quantization is not disclosed on this page.
  Confirms official venue: ICML 2025 Poster, OpenReview link present but forum page
  is bot-gated.'
---

*Suggested by [[rz-nas-icml-2025-reflective-zero-cost-nas-at-duckduckgo]] — ICML 2025 official poster page for RZ-NAS*

*Suggested by [[rz-nas-enhancing-llm-guided-neural-architecture-search-via-reflective-zero-cost]] — ICML 2025 poster page, confirms official venue listing*

ICML Poster RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
ICML 2025
Poster
RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy
Zipeng Ji ⋅ Guanghui Zhu ⋅ Chunfeng Yuan ⋅ Yihua Huang
2025 Poster
[
OpenReview
]
Abstract
LLM-to-NAS is a promising field at the intersection of Large Language Models (LLMs) and Neural Architecture Search (NAS), as recent research has explored the potential of architecture generation leveraging LLMs on multiple search spaces. However, the existing LLM-to-NAS methods face the challenges of limited search spaces, time-cost search efficiency, and uncompetitive performance across standard NAS benchmarks and multiple downstream tasks. In this work, we propose the Reflective Zero-cost NAS (RZ-NAS) method that can search NAS architectures with humanoid reflections and training-free metrics to elicit the power of LLMs. We rethink LLMs’ roles in NAS in current work and design a structured, prompt-based to comprehensively understand the search tasks and architectures from both text and code levels. By integrating LLM reflection modules, we use LLM-generated feedback to provide linguistic guidance within architecture optimization. RZ-NAS enables effective search within both micro and macro search spaces without extensive time cost, achieving SOTA performance across multiple downstream tasks.
Show more
Lay Summary
We introduce a novel framework that combines the text- and code-level comprehension capabilities of LLMs with a Reflective Zero-Cost evaluation strategy for neural architecture search (NAS). To integrate the text- and code-level understanding abilities of LLMs, we develop structured prompts to precisely define NAS tasks. These prompts include: a high-level role, detailed instructions, an in-context example, and the key reflective module. Moreover, we utilize Zero-Cost proxies instead of training architectures to reduce computational resources and time cost while maintaining competitive performance. The reflective module guides the LLM to reflect on mutation performance and generates targeted suggestions for further iteration improvements.
Show more
Video
Chat is not available.
Successful Page Load
ICML uses cookies for essential functions only. We do not sell your personal
                        information.
Our Privacy Policy »
Accept