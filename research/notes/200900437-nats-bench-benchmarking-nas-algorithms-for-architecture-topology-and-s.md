---
title: '[2009.00437] NATS-Bench: Benchmarking NAS Algorithms for Architecture Topology
  and Size'
id: 200900437-nats-bench-benchmarking-nas-algorithms-for-architecture-topology-and-s
tags:
- llm-nas-feedback-positioning-7125b1
- tabular-nas-benchmarks
- nas-methodology
created: '2026-08-16T15:54:05.051671Z'
updated: '2026-08-16T15:57:10.649961Z'
source: https://arxiv.org/abs/2009.00437
source_domain: arxiv.org
fetched_at: '2026-08-16T15:54:05.048320Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Dong, Liu, Musial & Gabrys (IEEE TPAMI 2021; arXiv:2009.00437, extended version
  of NAS-Bench-201/ICLR 2020). Introduces NATS-Bench, a unified tabular NAS benchmark
  covering BOTH architecture topology (15,625 candidates) and architecture size (32,768
  candidates) across three datasets, explicitly designed to make NAS algorithm comparisons
  FAIR and reproducible by providing 'all logs and diagnostic information trained
  using the same setup for each candidate.' Benchmarks 13 recent state-of-the-art
  NAS algorithms on this shared space to make performance gains attributable to the
  search algorithm itself rather than to differing search spaces/training setups --
  the exact confound the paper's introduction identifies as the core problem in NAS
  comparability ('the overall performance of the algorithms to some extent incomparable
  and the improvement from a sub-module of the searching model unclear'). This is
  the specific tabular benchmark that EvoPrompting (already in this vault) uses in
  its own Appendix A.7 comparison, though EvoPrompting's authors note their comparison
  there 'handicaps' EvoPrompting by removing its code-pretraining advantage. Directly
  relevant to the methodology-standards question as one of the four named tabular
  benchmarks (NAS-Bench-101/201, NATS-Bench, NAS-Bench-Suite-Zero) reviewers expect
  LLM-NAS papers to report against.
---

*Suggested by [[evoprompting-language-models-for-code-level-neural-architecture-search]] — NATS-Bench is the tabular benchmark EvoPrompting uses for its NAS-technique comparison in Appendix A.7*

[2009.00437] NATS-Bench: Benchmarking NAS Algorithms for Architecture Topology and Size
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2009.00437
(cs)
[Submitted on 28 Aug 2020 (
v1
), last revised 26 Jan 2021 (this version, v6)]
Title:
NATS-Bench: Benchmarking NAS Algorithms for Architecture Topology and Size
Authors:
Xuanyi Dong
,
Lu Liu
,
Katarzyna Musial
,
Bogdan Gabrys
View a PDF of the paper titled NATS-Bench: Benchmarking NAS Algorithms for Architecture Topology and Size, by Xuanyi Dong and 3 other authors
View PDF
HTML (experimental)
Abstract:
Neural architecture search (NAS) has attracted a lot of attention and has been illustrated to bring tangible benefits in a large number of applications in the past few years. Architecture topology and architecture size have been regarded as two of the most important aspects for the performance of deep learning models and the community has spawned lots of searching algorithms for both aspects of the neural architectures. However, the performance gain from these searching algorithms is achieved under different search spaces and training setups. This makes the overall performance of the algorithms to some extent incomparable and the improvement from a sub-module of the searching model unclear. In this paper, we propose NATS-Bench, a unified benchmark on searching for both topology and size, for (almost) any up-to-date NAS algorithm. NATS-Bench includes the search space of 15,625 neural cell candidates for architecture topology and 32,768 for architecture size on three datasets. We analyze the validity of our benchmark in terms of various criteria and performance comparison of all candidates in the search space. We also show the versatility of NATS-Bench by benchmarking 13 recent state-of-the-art NAS algorithms on it. All logs and diagnostic information trained using the same setup for each candidate are provided. This facilitates a much larger community of researchers to focus on developing better NAS algorithms in a more comparable and computationally cost friendly environment. All codes are publicly available at:
this https URL
.
Comments:
Accepted to IEEE TPAMI 2021, an extended version of NAS-Bench-201 (ICLR 2020) [
arXiv:2001.00326
]
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:2009.00437
[cs.LG]
(or
arXiv:2009.00437v6
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2009.00437
Focus to learn more
arXiv-issued DOI via DataCite
Related DOI
:
https://doi.org/10.1109/TPAMI.2021.3054824
Focus to learn more
DOI(s) linking to related resources
Submission history
From: Xuanyi Dong [
view email
]
[v1]
Fri, 28 Aug 2020 21:34:56 UTC (10,554 KB)
[v2]
Wed, 2 Sep 2020 01:50:27 UTC (10,553 KB)
[v3]
Fri, 9 Oct 2020 05:39:42 UTC (11,909 KB)
[v4]
Wed, 2 Dec 2020 15:19:25 UTC (12,415 KB)
[v5]
Mon, 25 Jan 2021 02:42:25 UTC (12,540 KB)
[v6]
Tue, 26 Jan 2021 02:33:39 UTC (12,540 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled NATS-Bench: Benchmarking NAS Algorithms for Architecture Topology and Size, by Xuanyi Dong and 3 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.LG
< prev
|
next >
new
|
recent
|
2020-09
Change to browse by:
cs
stat
stat.ML
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
DBLP
- CS Bibliography
listing
|
bibtex
Xuanyi Dong
Lu Liu
Katarzyna Musial
Bogdan Gabrys
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
IArxiv recommender toggle
IArxiv Recommender
(
What is IArxiv?
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