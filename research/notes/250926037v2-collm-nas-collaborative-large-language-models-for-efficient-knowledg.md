---
title: '[2509.26037v2] CoLLM-NAS: Collaborative Large Language Models for Efficient
  Knowledge-Guided Neural Architecture Search'
id: 250926037v2-collm-nas-collaborative-large-language-models-for-efficient-knowledg
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:44:16.522490Z'
source: https://arxiv.org/abs/2509.26037v2
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:16.522088Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2509.26037v2] CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2509.26037v2
(cs)
[Submitted on 30 Sep 2025 (
v1
), last revised 17 May 2026 (this version, v2)]
Title:
CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search
Authors:
Zhe Li
,
Zhiwei Lin
,
Yongtao Wang
View a PDF of the paper titled CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search, by Zhe Li and 2 other authors
View PDF
HTML (experimental)
Abstract:
The integration of Large Language Models (LLMs) with Neural Architecture Search (NAS) has introduced new possibilities for automating the design of neural architectures. However, most existing methods face critical limitations, including architectural invalidity, computational inefficiency, and inferior performance compared to traditional NAS. In this work, we present Collaborative LLM-based NAS (CoLLM-NAS), a two-stage NAS framework with knowledge-guided search driven by two complementary LLMs. Specifically, we propose a stateful Navigator LLM to guide search direction, a stateless Generator LLM to synthesize high-quality candidates, and a Coordinator module to orchestrate inter-LLM communication and manage evaluation processes. CoLLM-NAS efficiently guides the search process by combining LLMs' inherent knowledge of structured neural architectures with progressive knowledge from iterative feedback and historical trajectory. Experimental results on ImageNet and NAS-Bench-201 show that CoLLM-NAS surpasses existing NAS methods and conventional search algorithms, achieving new state-of-the-art results while significantly reducing search costs by 4--10. Furthermore, CoLLM-NAS consistently enhances the performance and efficiency of various two-stage NAS methods (e.g., OFA, SPOS, and AutoFormer) across diverse search spaces (e.g., MobileNet, ShuffleNet, and AutoFormer), demonstrating its excellent generalization.
Comments:
Accepted as Oral at CVPR 2026 Workshop on Neural Architecture Search (NAS)
Subjects:
Artificial Intelligence (cs.AI)
; Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
Cite as:
arXiv:2509.26037
[cs.AI]
(or
arXiv:2509.26037v2
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2509.26037
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Zhe Li [
view email
]
[v1]
Tue, 30 Sep 2025 10:12:49 UTC (1,505 KB)
[v2]
Sun, 17 May 2026 07:21:08 UTC (1,420 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search, by Zhe Li and 2 other authors
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
2025-09
Change to browse by:
cs
cs.CV
cs.LG
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