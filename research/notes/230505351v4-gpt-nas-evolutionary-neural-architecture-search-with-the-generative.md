---
title: '[2305.05351v4] GPT-NAS: Evolutionary Neural Architecture Search with the Generative
  Pre-Trained Model'
id: 230505351v4-gpt-nas-evolutionary-neural-architecture-search-with-the-generative
tags:
- llm-nas-feedback-positioning-7125b1
- llm-nas
- evolutionary-search
- prior-art
created: '2026-08-16T15:44:45.029534Z'
updated: '2026-08-16T15:50:36.270653Z'
source: https://arxiv.org/abs/2305.05351v4
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:45.028981Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'GPT-NAS (Yu, Liu, Wang, Liu, Feng, Xiong, Tang, Lv — confirmed true author
  list, all eight affiliated w/ the GPT-NAS project, Sichuan University group) optimizes
  neural architectures by using a GPT-style generative model to propose reasonable
  architecture components given a basic one, then runs an evolutionary algorithm (EA)
  as the outer search strategy to select among GPT-proposed candidates across generations.
  Reports outperforming 7 manually-designed and 13 competing NAS-derived architectures,
  and improving finely-tuned architecture performance by up to ~12% vs. an EA-only
  ablation without the GPT component. Critically, GPT-NAS is NOT a zero-shot single-proposal
  method: the GPT model is embedded inside an iterative EA loop across many generations,
  so any priority claim about ''small-model zero-shot LLM-NAS'' must distinguish itself
  from GPT-NAS''s use of LLM-proposed variation operators inside continued evolutionary
  iteration. First submitted May 2023 (v1), last revised Feb 2025 (v4); companion
  DOI links to Big Data Mining and Analytics journal, not a top-tier ML conference,
  suggesting the peer-reviewed venue was a specialty journal rather than NeurIPS/ICML/ICLR.'
---

[2305.05351v4] GPT-NAS: Evolutionary Neural Architecture Search with the Generative Pre-Trained Model
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computer Vision and Pattern Recognition
arXiv:2305.05351v4
(cs)
[Submitted on 9 May 2023 (
v1
), last revised 15 Feb 2025 (this version, v4)]
Title:
GPT-NAS: Evolutionary Neural Architecture Search with the Generative Pre-Trained Model
Authors:
Caiyang Yu
,
Xianggen Liu
,
Yifan Wang
,
Yun Liu
,
Wentao Feng
,
Deng Xiong
,
Chenwei Tang
,
Jiancheng Lv
View a PDF of the paper titled GPT-NAS: Evolutionary Neural Architecture Search with the Generative Pre-Trained Model, by Caiyang Yu and 7 other authors
View PDF
HTML (experimental)
Abstract:
Neural Architecture Search (NAS) has emerged as one of the effective methods to design the optimal neural network architecture automatically. Although neural architectures have achieved human-level performances in several tasks, few of them are obtained from the NAS method. The main reason is the huge search space of neural architectures, making NAS algorithms inefficient. This work presents a novel architecture search algorithm, called GPT-NAS, that optimizes neural architectures by Generative Pre-Trained (GPT) model with an evolutionary algorithm (EA) as the search strategy. In GPT-NAS, we assume that a generative model pre-trained on a large-scale corpus could learn the fundamental law of building neural architectures. Therefore, GPT-NAS leverages the GPT model to propose reasonable architecture components given the basic one and then utilizes EAs to search for the optimal solution. Such an approach can largely reduce the search space by introducing prior knowledge in the search process. Extensive experimental results show that our GPT-NAS method significantly outperforms seven manually designed neural architectures and thirteen architectures provided by competing NAS methods. In addition, our experiments also indicate that the proposed algorithm improves the performance of finely tuned neural architectures by up to about 12% compared to those without GPT, further demonstrating its effectiveness in searching neural architectures.
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2305.05351
[cs.CV]
(or
arXiv:2305.05351v4
[cs.CV]
for this version)
https://doi.org/10.48550/arXiv.2305.05351
Focus to learn more
arXiv-issued DOI via DataCite
Related DOI
:
https://doi.org/10.26599/BDMA.2024.9020036
Focus to learn more
DOI(s) linking to related resources
Submission history
From: Caiyang Yu [
view email
]
[v1]
Tue, 9 May 2023 11:29:42 UTC (8,678 KB)
[v2]
Sun, 28 May 2023 07:56:46 UTC (8,679 KB)
[v3]
Tue, 29 Oct 2024 02:03:06 UTC (8,679 KB)
[v4]
Sat, 15 Feb 2025 04:09:35 UTC (8,679 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled GPT-NAS: Evolutionary Neural Architecture Search with the Generative Pre-Trained Model, by Caiyang Yu and 7 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.CV
< prev
|
next >
new
|
recent
|
2023-05
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