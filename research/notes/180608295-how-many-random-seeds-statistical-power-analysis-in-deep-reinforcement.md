---
title: '[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement
  Learning Experiments'
id: 180608295-how-many-random-seeds-statistical-power-analysis-in-deep-reinforcement
tags:
- llm-nas-feedback-positioning-7125b1
- nas-methodology
- random-search-baseline
created: '2026-08-16T15:45:02.114154Z'
updated: '2026-08-16T15:51:01.459675Z'
source: https://arxiv.org/abs/1806.08295
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:02.113639Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Colas, Sigaud & Oudeyer (2018) tutorial establishing how many random seeds
  are statistically required to compare two algorithms'' performance with adequate
  power, using t-tests and bootstrap confidence intervals, plus guidance on the consequences
  of violating test assumptions (non-normality, unequal variance). Written for deep
  RL reproducibility but is the standard methodological citation across empirical
  deep-learning subfields, including NAS, for ''how many seeds/runs justify a significance
  claim.'' Directly bears on the paper''s methodology defensibility: a claim that
  a handful of LLM-proposed architectures (or a small number of random-search runs)
  differ from each other requires a seed count and statistical test calibrated by
  exactly this kind of power analysis — reviewers following this standard would flag
  single-run or few-run comparisons between LLM proposals and random search as statistically
  underpowered regardless of which mean looks larger.'
---

[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1806.08295
(cs)
[Submitted on 21 Jun 2018 (
v1
), last revised 5 Jul 2018 (this version, v2)]
Title:
How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
Authors:
Cédric Colas
,
Olivier Sigaud
,
Pierre-Yves Oudeyer
View a PDF of the paper titled How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments, by C\'edric Colas and Olivier Sigaud and Pierre-Yves Oudeyer
View PDF
HTML (experimental)
Abstract:
Consistently checking the statistical significance of experimental results is one of the mandatory methodological steps to address the so-called "reproducibility crisis" in deep reinforcement learning. In this tutorial paper, we explain how the number of random seeds relates to the probabilities of statistical errors. For both the t-test and the bootstrap confidence interval test, we recall theoretical guidelines to determine the number of random seeds one should use to provide a statistically significant comparison of the performance of two algorithms. Finally, we discuss the influence of deviations from the assumptions usually made by statistical tests. We show that they can lead to inaccurate evaluations of statistical errors and provide guidelines to counter these negative effects. We make our code available to perform the tests.
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1806.08295
[cs.LG]
(or
arXiv:1806.08295v2
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1806.08295
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Olivier Sigaud [
view email
]
[v1]
Thu, 21 Jun 2018 15:39:19 UTC (3,827 KB)
[v2]
Thu, 5 Jul 2018 06:50:33 UTC (3,827 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments, by C\'edric Colas and Olivier Sigaud and Pierre-Yves Oudeyer
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
2018-06
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
Cédric Colas
Olivier Sigaud
Pierre-Yves Oudeyer
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