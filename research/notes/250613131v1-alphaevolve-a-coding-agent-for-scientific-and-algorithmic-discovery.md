---
title: '[2506.13131v1] AlphaEvolve: A coding agent for scientific and algorithmic
  discovery'
id: 250613131v1-alphaevolve-a-coding-agent-for-scientific-and-algorithmic-discovery
tags:
- llm-nas-feedback-positioning-7125b1
- counter-evidence
- iterative-feedback
- evolutionary-search
- program-search
- frontier-model
created: '2026-08-16T15:44:21.993885Z'
updated: '2026-08-16T15:47:32.802661Z'
source: https://arxiv.org/abs/2506.13131v1
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:21.993443Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'AlphaEvolve (Novikov et al., DeepMind, Jun 2025) is an evolutionary coding
  agent that orchestrates an autonomous pipeline of frontier LLMs to iteratively rewrite
  algorithm code, ''continuously receiving feedback from one or more evaluators,''
  and ''iteratively improves the algorithm.'' Deployed at Google, it found a more
  efficient data-center scheduling algorithm, a simplification in TPU circuit design,
  sped up training of the LLM underpinning AlphaEvolve itself, and discovered a procedure
  multiplying two 4x4 complex-valued matrices in 48 scalar multiplications — the first
  improvement over Strassen''s algorithm in that exact setting in 56 years — explicitly
  extending prior automated discovery work (Romera-Paredes et al. 2023, i.e. FunSearch).
  This is the single strongest published counter-example to a blanket ''iterative
  feedback degrades LLM-guided search'' thesis for Q4: it is a large-scale, frontier-model,
  multi-evaluator, population-based evolutionary system (not single-context sequential
  self-refinement by one small quantized model), so it bounds the target claim to
  small/single-model/single-context/no-external-evaluator regimes rather than refuting
  a narrower version of it — the paper reports no ablation isolating the causal effect
  of iterative feedback alone versus population diversity maintenance, LLM ensembling,
  or evaluator strength.'
---

[2506.13131v1] AlphaEvolve: A coding agent for scientific and algorithmic discovery
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2506.13131v1
(cs)
[Submitted on 16 Jun 2025]
Title:
AlphaEvolve: A coding agent for scientific and algorithmic discovery
Authors:
Alexander Novikov
,
Ngân Vũ
,
Marvin Eisenberger
,
Emilien Dupont
,
Po-Sen Huang
,
Adam Zsolt Wagner
,
Sergey Shirobokov
,
Borislav Kozlovskii
,
Francisco J. R. Ruiz
,
Abbas Mehrabian
,
M. Pawan Kumar
,
Abigail See
,
Swarat Chaudhuri
,
George Holland
,
Alex Davies
,
Sebastian Nowozin
,
Pushmeet Kohli
,
Matej Balog
View a PDF of the paper titled AlphaEvolve: A coding agent for scientific and algorithmic discovery, by Alexander Novikov and 17 other authors
View PDF
HTML (experimental)
Abstract:
In this white paper, we present AlphaEvolve, an evolutionary coding agent that substantially enhances capabilities of state-of-the-art LLMs on highly challenging tasks such as tackling open scientific problems or optimizing critical pieces of computational infrastructure. AlphaEvolve orchestrates an autonomous pipeline of LLMs, whose task is to improve an algorithm by making direct changes to the code. Using an evolutionary approach, continuously receiving feedback from one or more evaluators, AlphaEvolve iteratively improves the algorithm, potentially leading to new scientific and practical discoveries. We demonstrate the broad applicability of this approach by applying it to a number of important computational problems. When applied to optimizing critical components of large-scale computational stacks at Google, AlphaEvolve developed a more efficient scheduling algorithm for data centers, found a functionally equivalent simplification in the circuit design of hardware accelerators, and accelerated the training of the LLM underpinning AlphaEvolve itself. Furthermore, AlphaEvolve discovered novel, provably correct algorithms that surpass state-of-the-art solutions on a spectrum of problems in mathematics and computer science, significantly expanding the scope of prior automated discovery methods (Romera-Paredes et al., 2023). Notably, AlphaEvolve developed a search algorithm that found a procedure to multiply two $4 \times 4$ complex-valued matrices using $48$ scalar multiplications; offering the first improvement, after 56 years, over Strassen's algorithm in this setting. We believe AlphaEvolve and coding agents like it can have a significant impact in improving solutions of problems across many areas of science and computation.
Subjects:
Artificial Intelligence (cs.AI)
; Machine Learning (cs.LG); Neural and Evolutionary Computing (cs.NE)
Cite as:
arXiv:2506.13131
[cs.AI]
(or
arXiv:2506.13131v1
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2506.13131
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Matej Balog [
view email
]
[v1]
Mon, 16 Jun 2025 06:37:18 UTC (2,574 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled AlphaEvolve: A coding agent for scientific and algorithmic discovery, by Alexander Novikov and 17 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.AI
< prev
|
next >
new
|
recent
|
2025-06
Change to browse by:
cs
cs.LG
cs.NE
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
(
What is the Explorer?
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?
)
Litmaps Toggle
Litmaps
(
What is Litmaps?
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?
)
DagsHub Toggle
DagsHub
(
What is DagsHub?
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?
)
Core recommender toggle
CORE Recommender
(
What is CORE?
)
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community?
Learn more about arXivLabs
.
Which authors of this paper are endorsers?
|
Disable MathJax
(
What is MathJax?
)