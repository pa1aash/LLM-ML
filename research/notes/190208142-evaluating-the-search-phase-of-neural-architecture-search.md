---
title: '[1902.08142] Evaluating the Search Phase of Neural Architecture Search'
id: 190208142-evaluating-the-search-phase-of-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
- nas-methodology
- random-search-baseline
created: '2026-08-16T15:54:01.537576Z'
updated: '2026-08-16T15:56:38.559773Z'
source: https://arxiv.org/abs/1902.08142
source_domain: arxiv.org
fetched_at: '2026-08-16T15:54:01.536911Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Yu, Sciuto, Jaggi, Musat & Salzmann (ICLR 2020; arXiv:1902.08142). Proposes
  an evaluation framework isolating the NAS SEARCH PHASE from the downstream-task
  result, comparing NAS search-policy solution quality against random architecture
  selection under matched conditions. Two central, precisely-stated findings directly
  load-bearing for the methodology-standards question: (i) ''On average, the state-of-the-art
  NAS algorithms perform similarly to the random policy'' -- i.e., random search is
  not just a weak baseline but a genuinely competitive one across state-of-the-art
  NAS methods when evaluated fairly; (ii) ''the widely-used weight sharing strategy
  degrades the ranking of the NAS candidates to the point of not reflecting their
  true performance, thus reducing the effectiveness of the search process'' -- identifying
  weight-sharing (used by DARTS/ENAS-style one-shot methods) as a specific methodological
  confound that can make searches LOOK effective while actually destroying the correlation
  between predicted and true architecture quality. Paper''s own summary comment: ''We
  find that random policy in NAS works amazingly well and propose an evaluation framework
  to have a fair comparison.'' This is one of the two canonical ''random-search baseline''
  papers the research query names (the other being Li & Talwalkar 2019, already in
  this vault) and directly establishes the standard the target paper''s random-search
  comparison must be held to.'
---

*Suggested by [[neural-architecture-search-insights-from-1000-papers]] — shows simple baselines competitive with SOTA NAS algorithms, cited by the 1000-papers survey*

*Suggested by [[automated-machine-learning-past-present-and-future-artificial-intelligence-revie]] — cited as showing ENAS/DARTS/NAO have similar average performance to random search under matched search space*

[1902.08142] Evaluating the Search Phase of Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1902.08142
(cs)
[Submitted on 21 Feb 2019 (
v1
), last revised 22 Nov 2019 (this version, v3)]
Title:
Evaluating the Search Phase of Neural Architecture Search
Authors:
Kaicheng Yu
,
Christian Sciuto
,
Martin Jaggi
,
Claudiu Musat
,
Mathieu Salzmann
View a PDF of the paper titled Evaluating the Search Phase of Neural Architecture Search, by Kaicheng Yu and 4 other authors
View PDF
HTML (experimental)
Abstract:
Neural Architecture Search (NAS) aims to facilitate the design of deep networks for new tasks. Existing techniques rely on two stages: searching over the architecture space and validating the best architecture. NAS algorithms are currently compared solely based on their results on the downstream task. While intuitive, this fails to explicitly evaluate the effectiveness of their search strategies. In this paper, we propose to evaluate the NAS search phase. To this end, we compare the quality of the solutions obtained by NAS search policies with that of random architecture selection. We find that: (i) On average, the state-of-the-art NAS algorithms perform similarly to the random policy; (ii) the widely-used weight sharing strategy degrades the ranking of the NAS candidates to the point of not reflecting their true performance, thus reducing the effectiveness of the search process. We believe that our evaluation framework will be key to designing NAS strategies that consistently discover architectures superior to random ones.
Comments:
We find that random policy in NAS works amazingly well and propose an evaluation framework to have a fair comparison. Adding additional results on standard CNN search space used for weight sharing and NASBench-101. 8 pages
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1902.08142
[cs.LG]
(or
arXiv:1902.08142v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1902.08142
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Kaicheng Yu [
view email
]
[v1]
Thu, 21 Feb 2019 17:11:56 UTC (938 KB)
[v2]
Fri, 24 May 2019 11:42:39 UTC (766 KB)
[v3]
Fri, 22 Nov 2019 17:07:59 UTC (783 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Evaluating the Search Phase of Neural Architecture Search, by Kaicheng Yu and 4 other authors
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
2019-02
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
Christian Sciuto
Kaicheng Yu
Martin Jaggi
Claudiu Musat
Mathieu Salzmann
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