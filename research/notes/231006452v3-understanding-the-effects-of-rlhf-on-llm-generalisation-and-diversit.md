---
title: '[2310.06452v3] Understanding the Effects of RLHF on LLM Generalisation and
  Diversity'
id: 231006452v3-understanding-the-effects-of-rlhf-on-llm-generalisation-and-diversit
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:44:03.827840Z'
updated: '2026-08-16T15:45:28.481483Z'
source: https://arxiv.org/abs/2310.06452v3
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:03.827445Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2310.06452v3] Understanding the Effects of RLHF on LLM Generalisation and Diversity
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2310.06452v3
(cs)
[Submitted on 10 Oct 2023 (
v1
), last revised 19 Feb 2024 (this version, v3)]
Title:
Understanding the Effects of RLHF on LLM Generalisation and Diversity
Authors:
Robert Kirk
,
Ishita Mediratta
,
Christoforos Nalmpantis
,
Jelena Luketina
,
Eric Hambro
,
Edward Grefenstette
,
Roberta Raileanu
View a PDF of the paper titled Understanding the Effects of RLHF on LLM Generalisation and Diversity, by Robert Kirk and 6 other authors
View PDF
HTML (experimental)
Abstract:
Large language models (LLMs) fine-tuned with reinforcement learning from human feedback (RLHF) have been used in some of the most widely deployed AI models to date, such as OpenAI's ChatGPT or Anthropic's Claude. While there has been significant work developing these methods, our understanding of the benefits and downsides of each stage in RLHF is still limited. To fill this gap, we present an extensive analysis of how each stage of the process (i.e. supervised fine-tuning (SFT), reward modelling, and RLHF) affects two key properties: out-of-distribution (OOD) generalisation and output diversity. OOD generalisation is crucial given the wide range of real-world scenarios in which these models are being used, while output diversity refers to the model's ability to generate varied outputs and is important for a variety of use cases. We perform our analysis across two base models on both summarisation and instruction following tasks, the latter being highly relevant for current LLM use cases. We find that RLHF generalises better than SFT to new inputs, particularly as the distribution shift between train and test becomes larger. However, RLHF significantly reduces output diversity compared to SFT across a variety of measures, implying a tradeoff in current LLM fine-tuning methods between generalisation and diversity. Our results provide guidance on which fine-tuning method should be used depending on the application, and show that more research is needed to improve the tradeoff between generalisation and diversity.
Comments:
Code available here:
this https URL
Subjects:
Machine Learning (cs.LG)
; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2310.06452
[cs.LG]
(or
arXiv:2310.06452v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2310.06452
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Robert Kirk [
view email
]
[v1]
Tue, 10 Oct 2023 09:25:44 UTC (1,796 KB)
[v2]
Wed, 3 Jan 2024 11:58:42 UTC (1,818 KB)
[v3]
Mon, 19 Feb 2024 14:39:07 UTC (1,818 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Understanding the Effects of RLHF on LLM Generalisation and Diversity, by Robert Kirk and 6 other authors
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
2023-10
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