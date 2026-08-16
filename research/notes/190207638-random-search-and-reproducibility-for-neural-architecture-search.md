---
title: '[1902.07638] Random Search and Reproducibility for Neural Architecture Search'
id: 190207638-random-search-and-reproducibility-for-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
- random-search-baseline
- nas-reproducibility
- load-bearing
created: '2026-08-16T15:48:50.982453Z'
updated: '2026-08-16T15:49:13.069240Z'
source: https://arxiv.org/abs/1902.07638
source_domain: arxiv.org
fetched_at: '2026-08-16T15:48:50.981343Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Li & Talwalkar (UAI 2019; this is the correct ''Li and Talwalkar'' paper
  named explicitly in the research query''s THIRD question, distinct from NAS-Bench-101
  which shares a similar-looking arXiv ID). Central thesis: NAS is a specialized hyperparameter-optimization
  problem, and since random search is already a known competitive baseline for hyperparameter
  optimization, it should be a mandatory NAS baseline too. Proposes and tests two
  random-search variants -- random search with early-stopping and a novel random search
  with weight-sharing (RS-WS) -- on two standard benchmarks (Penn Treebank/PTB and
  CIFAR-10). Findings: random search with early-stopping performs at least as well
  as ENAS, a then-leading NAS method, on both benchmarks; random search with weight-sharing
  beats random search with early-stopping and achieves a then-state-of-the-art result
  on PTB and a highly competitive result on CIFAR-10. Also documents a NAS reproducibility
  crisis: published NAS results commonly lack the source material (code, exact seeds,
  documentation) needed to exactly reproduce them, and the paper explicitly discusses
  the robustness of published NAS gains against the variability inherent in NAS experimental
  setups. The authors'' own remedy is to publish full code, random seeds, and documentation,
  and to report their RS-WS results across multiple runs (6 sets of random seeds per
  the v2 changelog) rather than a single run. This is the canonical citation establishing
  that any NAS method claiming to beat random search must (a) use a strong, well-tuned
  random-search baseline, not a naive one, and (b) report results over multiple seeds/runs,
  both of which the target paper''s evaluation protocol must be checked against.'
---

*Suggested by [[190209635v2-nas-bench-101-towards-reproducible-neural-architecture-search]] — correct paper for Li and Talwalkar random-search baseline standard named explicitly in query THREE; original assigned URL 1902.09635 turned out to be NAS-Bench-101, not this paper*

[1902.07638] Random Search and Reproducibility for Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1902.07638
(cs)
[Submitted on 20 Feb 2019 (
v1
), last revised 30 Jul 2019 (this version, v3)]
Title:
Random Search and Reproducibility for Neural Architecture Search
Authors:
Liam Li
,
Ameet Talwalkar
View a PDF of the paper titled Random Search and Reproducibility for Neural Architecture Search, by Liam Li and 1 other authors
View PDF
HTML (experimental)
Abstract:
Neural architecture search (NAS) is a promising research direction that has the potential to replace expert-designed networks with learned, task-specific architectures. In this work, in order to help ground the empirical results in this field, we propose new NAS baselines that build off the following observations: (i) NAS is a specialized hyperparameter optimization problem; and (ii) random search is a competitive baseline for hyperparameter optimization. Leveraging these observations, we evaluate both random search with early-stopping and a novel random search with weight-sharing algorithm on two standard NAS benchmarks---PTB and CIFAR-10. Our results show that random search with early-stopping is a competitive NAS baseline, e.g., it performs at least as well as ENAS, a leading NAS method, on both benchmarks. Additionally, random search with weight-sharing outperforms random search with early-stopping, achieving a state-of-the-art NAS result on PTB and a highly competitive result on CIFAR-10. Finally, we explore the existing reproducibility issues of published NAS results. We note the lack of source material needed to exactly reproduce these results, and further discuss the robustness of published results given the various sources of variability in NAS experimental setups. Relatedly, we provide all information (code, random seeds, documentation) needed to exactly reproduce our results, and report our random search with weight-sharing results for each benchmark on multiple runs.
Comments:
V2 Changelog: - Modified footnote 2 for ENAS. - Expanded broad reproducibility study for random search with WS for CNN to 6 sets of random seeds v3 Changelog: - Added journal reference - Updated acknowledgements
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1902.07638
[cs.LG]
(or
arXiv:1902.07638v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1902.07638
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
Conference on Uncertainty in Artificial Intelligence (UAI), 2019
Submission history
From: Liam Li [
view email
]
[v1]
Wed, 20 Feb 2019 16:49:07 UTC (139 KB)
[v2]
Mon, 15 Jul 2019 21:06:02 UTC (139 KB)
[v3]
Tue, 30 Jul 2019 20:07:41 UTC (139 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Random Search and Reproducibility for Neural Architecture Search, by Liam Li and 1 other authors
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
1 blog link
(
what is this?
)
DBLP
- CS Bibliography
listing
|
bibtex
Liam Li
Ameet Talwalkar
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