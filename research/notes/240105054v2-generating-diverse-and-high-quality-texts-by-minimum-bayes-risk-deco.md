---
title: '[2401.05054v2] Generating Diverse and High-Quality Texts by Minimum Bayes
  Risk Decoding'
id: 240105054v2-generating-diverse-and-high-quality-texts-by-minimum-bayes-risk-deco
tags:
- llm-nas-feedback-positioning-7125b1
- decoding-diversity
- mode-collapse
- llm-generation
created: '2026-08-16T15:44:30.176494Z'
updated: '2026-08-16T15:45:44.974581Z'
source: https://arxiv.org/abs/2401.05054v2
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:30.173496Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Jinnai et al. (arXiv:2401.05054, 2024) show that standard decoding methods
  for LLM text generation face a hard quality-diversity trade-off: beam search and
  low-temperature sampling maximize per-output quality at the cost of collapsing diversity
  across a generated set, while high-temperature/random sampling restores diversity
  at the cost of quality. They propose Diverse MBR (DMBR) and k-medoids MBR (KMBR),
  which explicitly add a diversity objective on top of Minimum Bayes-Risk decoding,
  and show these Pareto-dominate diverse beam search and plain sampling baselines
  on directed generation tasks with both encoder-decoder models and a prompted LLM.
  Relevant as a rival mechanistic explanation: greedy/low-temperature decoding (typical
  for deterministic ''best'' proposals) is a well-documented, decoding-level cause
  of collapsed output diversity, independent of any claim about feedback loops degrading
  search.'
---

[2401.05054v2] Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2401.05054v2
(cs)
[Submitted on 10 Jan 2024 (
v1
), last revised 12 Jun 2024 (this version, v2)]
Title:
Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding
Authors:
Yuu Jinnai
,
Ukyo Honda
,
Tetsuro Morimura
,
Peinan Zhang
View a PDF of the paper titled Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding, by Yuu Jinnai and 3 other authors
View PDF
HTML (experimental)
Abstract:
One of the most important challenges in text generation systems is to produce outputs that are not only correct but also diverse. Recently, Minimum Bayes-Risk (MBR) decoding has gained prominence for generating sentences of the highest quality among the decoding algorithms. However, existing algorithms proposed for generating diverse outputs are predominantly based on beam search or random sampling, thus their output quality is capped by these underlying methods. In this paper, we investigate an alternative approach -- we develop diversity-promoting decoding algorithms by enforcing diversity objectives to MBR decoding. We propose two variants of MBR, Diverse MBR (DMBR) and $k$-medoids MBR (KMBR), methods to generate a set of sentences with high quality and diversity. We evaluate DMBR and KMBR on a variety of directed text generation tasks using encoder-decoder models and a large language model with prompting. The experimental results show that the proposed method achieves a better trade-off than the diverse beam search and sampling algorithms.
Subjects:
Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2401.05054
[cs.CL]
(or
arXiv:2401.05054v2
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2401.05054
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Yuu Jinnai [
view email
]
[v1]
Wed, 10 Jan 2024 10:23:41 UTC (808 KB)
[v2]
Wed, 12 Jun 2024 01:27:32 UTC (372 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Generating Diverse and High-Quality Texts by Minimum Bayes Risk Decoding, by Yuu Jinnai and 3 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.CL
< prev
|
next >
new
|
recent
|
2024-01
Change to browse by:
cs
cs.AI
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