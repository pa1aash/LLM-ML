---
title: '[1902.09635v2] NAS-Bench-101: Towards Reproducible Neural Architecture Search'
id: 190209635v2-nas-bench-101-towards-reproducible-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
- nas-bench
- tabular-nas-benchmark
created: '2026-08-16T15:45:09.853534Z'
updated: '2026-08-16T15:46:21.328583Z'
source: https://arxiv.org/abs/1902.09635v2
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:09.852861Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Ying, Klein, Real, Christiansen, Murphy, Hutter (ICML 2019). Introduces
  NAS-Bench-101, the first public tabular NAS benchmark: a compact but expressive
  cell-based search space reduced via graph isomorphism to 423k unique convolutional
  architectures, each trained and evaluated multiple times on CIFAR-10, yielding a
  queryable dataset of over 5 million trained models. Purpose is explicitly to solve
  the NAS reproducibility crisis by letting any algorithm''s search quality be evaluated
  in milliseconds via lookup instead of new training runs, and the paper itself benchmarks
  a range of architecture optimization algorithms against this dataset as a validation
  exercise. NOTE: this is NOT Li & Talwalkar''s ''Random Search and Reproducibility
  for NAS'' as the task brief guessed — that is a separate paper (a different arXiv
  ID) which still needs to be located and fetched for question THREE''s random-search-baseline
  standard.'
---

[1902.09635v2] NAS-Bench-101: Towards Reproducible Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1902.09635v2
(cs)
[Submitted on 25 Feb 2019 (
v1
), last revised 14 May 2019 (this version, v2)]
Title:
NAS-Bench-101: Towards Reproducible Neural Architecture Search
Authors:
Chris Ying
,
Aaron Klein
,
Esteban Real
,
Eric Christiansen
,
Kevin Murphy
,
Frank Hutter
View a PDF of the paper titled NAS-Bench-101: Towards Reproducible Neural Architecture Search, by Chris Ying and 5 other authors
View PDF
HTML (experimental)
Abstract:
Recent advances in neural architecture search (NAS) demand tremendous computational resources, which makes it difficult to reproduce experiments and imposes a barrier-to-entry to researchers without access to large-scale computation. We aim to ameliorate these problems by introducing NAS-Bench-101, the first public architecture dataset for NAS research. To build NAS-Bench-101, we carefully constructed a compact, yet expressive, search space, exploiting graph isomorphisms to identify 423k unique convolutional architectures. We trained and evaluated all of these architectures multiple times on CIFAR-10 and compiled the results into a large dataset of over 5 million trained models. This allows researchers to evaluate the quality of a diverse range of models in milliseconds by querying the pre-computed dataset. We demonstrate its utility by analyzing the dataset as a whole and by benchmarking a range of architecture optimization algorithms.
Comments:
Published in the Proceedings of the 36th International Conference on Machine Learning
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1902.09635
[cs.LG]
(or
arXiv:1902.09635v2
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1902.09635
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Chris Ying [
view email
]
[v1]
Mon, 25 Feb 2019 21:56:54 UTC (3,090 KB)
[v2]
Tue, 14 May 2019 05:33:47 UTC (3,993 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled NAS-Bench-101: Towards Reproducible Neural Architecture Search, by Chris Ying and 5 other authors
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
Chris Ying
Aaron Klein
Esteban Real
Eric Christiansen
Kevin Murphy
…
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