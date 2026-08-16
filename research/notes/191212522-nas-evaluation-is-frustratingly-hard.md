---
title: '[1912.12522] NAS evaluation is frustratingly hard'
id: 191212522-nas-evaluation-is-frustratingly-hard
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:45:43.056762Z'
updated: '2026-08-16T15:49:37.041757Z'
source: https://arxiv.org/abs/1912.12522
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:43.056364Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
---

*Suggested by [[neural-architecture-search-insights-from-1000-papers]] — canonical NAS evaluation critique 'NAS evaluation is frustratingly hard' cited by the 1000-papers survey, directly named in the research query*

[1912.12522] NAS evaluation is frustratingly hard
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1912.12522
(cs)
[Submitted on 28 Dec 2019 (
v1
), last revised 13 Feb 2020 (this version, v3)]
Title:
NAS evaluation is frustratingly hard
Authors:
Antoine Yang
,
Pedro M. Esperança
,
Fabio M. Carlucci
View a PDF of the paper titled NAS evaluation is frustratingly hard, by Antoine Yang and 2 other authors
View PDF
HTML (experimental)
Abstract:
Neural Architecture Search (NAS) is an exciting new field which promises to be as much as a game-changer as Convolutional Neural Networks were in 2012. Despite many great works leading to substantial improvements on a variety of tasks, comparison between different methods is still very much an open issue. While most algorithms are tested on the same datasets, there is no shared experimental protocol followed by all. As such, and due to the under-use of ablation studies, there is a lack of clarity regarding why certain methods are more effective than others. Our first contribution is a benchmark of $8$ NAS methods on $5$ datasets. To overcome the hurdle of comparing methods with different search spaces, we propose using a method's relative improvement over the randomly sampled average architecture, which effectively removes advantages arising from expertly engineered search spaces or training protocols. Surprisingly, we find that many NAS techniques struggle to significantly beat the average architecture baseline. We perform further experiments with the commonly used DARTS search space in order to understand the contribution of each component in the NAS pipeline. These experiments highlight that: (i) the use of tricks in the evaluation protocol has a predominant impact on the reported performance of architectures; (ii) the cell-based search space has a very narrow accuracy range, such that the seed has a considerable impact on architecture rankings; (iii) the hand-designed macro-structure (cells) is more important than the searched micro-structure (operations); and (iv) the depth-gap is a real phenomenon, evidenced by the change in rankings between $8$ and $20$ cell architectures. To conclude, we suggest best practices, that we hope will prove useful for the community and help mitigate current NAS pitfalls. The code used is available at
this https URL
.
Comments:
Published as a conference paper at ICLR2020; 13 pages; 10 figures
Subjects:
Machine Learning (cs.LG)
; Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
Cite as:
arXiv:1912.12522
[cs.LG]
(or
arXiv:1912.12522v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1912.12522
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Antoine Yang [
view email
]
[v1]
Sat, 28 Dec 2019 21:24:12 UTC (1,333 KB)
[v2]
Fri, 3 Jan 2020 11:42:17 UTC (1,331 KB)
[v3]
Thu, 13 Feb 2020 22:10:12 UTC (1,333 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled NAS evaluation is frustratingly hard, by Antoine Yang and 2 other authors
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
2019-12
Change to browse by:
cs
cs.CV
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
Pedro M. Esperança
Fabio Maria Carlucci
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