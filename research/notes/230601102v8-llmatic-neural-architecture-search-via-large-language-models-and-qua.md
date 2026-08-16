---
title: '[2306.01102v8] LLMatic: Neural Architecture Search via Large Language Models
  and Quality Diversity Optimization'
id: 230601102v8-llmatic-neural-architecture-search-via-large-language-models-and-qua
tags:
- llm-nas-feedback-positioning-7125b1
- llm-nas
- quality-diversity
- nas-benchmark
created: '2026-08-16T15:44:27.997088Z'
updated: '2026-08-16T15:45:40.105508Z'
source: https://arxiv.org/abs/2306.01102v8
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:27.996205Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: LLMatic (Nasir et al., GECCO 2024; arXiv:2306.01102) combines LLM code-editing
  with Quality-Diversity (QD/MAP-Elites) optimization for NAS on CIFAR-10 and NAS-Bench-201,
  finding competitive networks within 2,000 evaluated candidates without prior benchmark
  knowledge. Critically, the abstract explicitly states 'LLMs struggle to conduct
  NAS directly through prompts,' which is why the authors wrap the LLM inside a procedural
  QD loop rather than relying on raw zero-shot or iteratively-prompted LLM proposals
  — an implicit acknowledgment, from a load-bearing LLM-NAS paper, that naive prompt-driven
  LLM search (the exact setup the target paper studies) is weak on its own.
---

[2306.01102v8] LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Neural and Evolutionary Computing
arXiv:2306.01102v8
(cs)
[Submitted on 1 Jun 2023 (
v1
), last revised 12 Apr 2024 (this version, v8)]
Title:
LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization
Authors:
Muhammad U. Nasir
,
Sam Earle
,
Christopher Cleghorn
,
Steven James
,
Julian Togelius
View a PDF of the paper titled LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization, by Muhammad U. Nasir and 3 other authors
View PDF
HTML (experimental)
Abstract:
Large Language Models (LLMs) have emerged as powerful tools capable of accomplishing a broad spectrum of tasks. Their abilities span numerous areas, and one area where they have made a significant impact is in the domain of code generation. Here, we propose using the coding abilities of LLMs to introduce meaningful variations to code defining neural networks. Meanwhile, Quality-Diversity (QD) algorithms are known to discover diverse and robust solutions. By merging the code-generating abilities of LLMs with the diversity and robustness of QD solutions, we introduce \texttt{LLMatic}, a Neural Architecture Search (NAS) algorithm. While LLMs struggle to conduct NAS directly through prompts, \texttt{LLMatic} uses a procedural approach, leveraging QD for prompts and network architecture to create diverse and high-performing networks. We test \texttt{LLMatic} on the CIFAR-10 and NAS-bench-201 benchmarks, demonstrating that it can produce competitive networks while evaluating just $2,000$ candidates, even without prior knowledge of the benchmark domain or exposure to any previous top-performing models for the benchmark. The open-sourced code is available in \url{
this https URL
}.
Comments:
Accepted to The Genetic and Evolutionary Computation Conference 2024
Subjects:
Neural and Evolutionary Computing (cs.NE)
; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2306.01102
[cs.NE]
(or
arXiv:2306.01102v8
[cs.NE]
for this version)
https://doi.org/10.48550/arXiv.2306.01102
Focus to learn more
arXiv-issued DOI via DataCite
Related DOI
:
https://doi.org/10.1145/3638529.3654017
Focus to learn more
DOI(s) linking to related resources
Submission history
From: Muhammad Umair Nasir Mr. [
view email
]
[v1]
Thu, 1 Jun 2023 19:33:21 UTC (615 KB)
[v2]
Wed, 16 Aug 2023 15:49:48 UTC (4,542 KB)
[v3]
Sat, 9 Sep 2023 18:58:26 UTC (4,542 KB)
[v4]
Sun, 17 Sep 2023 15:31:15 UTC (4,543 KB)
[v5]
Tue, 3 Oct 2023 07:43:30 UTC (914 KB)
[v6]
Wed, 4 Oct 2023 06:51:09 UTC (1,305 KB)
[v7]
Wed, 10 Apr 2024 13:18:37 UTC (4,356 KB)
[v8]
Fri, 12 Apr 2024 08:17:54 UTC (4,356 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization, by Muhammad U. Nasir and 3 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.NE
< prev
|
next >
new
|
recent
|
2023-06
Change to browse by:
cs
cs.AI
cs.CL
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