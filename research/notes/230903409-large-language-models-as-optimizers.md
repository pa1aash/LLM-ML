---
title: '[2309.03409] Large Language Models as Optimizers'
id: 230903409-large-language-models-as-optimizers
tags:
- llm-nas-feedback-positioning-7125b1
- opro
- iterative-feedback
- counter-evidence
created: '2026-08-16T15:45:19.890153Z'
updated: '2026-08-16T15:46:33.159835Z'
source: https://arxiv.org/abs/2309.03409
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:19.889780Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Yang, Wang, Lu, Liu, Le, Zhou, Chen (Google DeepMind, ICLR 2024). Proposes
  Optimization by PROmpting (OPRO): an iterative loop where at each step the LLM is
  given a prompt containing all previously generated solutions with their evaluated
  objective values, and generates new candidate solutions conditioned on that trajectory,
  which are then evaluated and appended back into the prompt for the next round. Demonstrated
  first on toy derivative-free optimization (linear regression, traveling salesman),
  then as the main application on prompt optimization, where OPRO-discovered instructions
  beat human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard
  tasks, tested across ''a variety of LLMs'' as both optimizer and scorer. KEY COUNTER-EVIDENCE
  for question FOUR: this is a published, large-scale (frontier LLMs such as PaLM
  2 and GPT-family models, not small quantized models), peer-reviewed (ICLR 2024)
  demonstration that iterative feedback loops with prior-trajectory conditioning DO
  measurably improve LLM-generated solutions versus non-iterative baselines — directly
  bearing on whether the target paper''s negative feedback finding is scale-bound
  rather than general. Full PDF text could not be extracted (JUNK_CONTENT on arxiv.org/pdf/2309.03409);
  only abstract-level detail captured here — a source-analyst pass on the full paper
  is recommended to extract iteration-count-vs-performance curves and exact model
  sizes used.'
---

[2309.03409] Large Language Models as Optimizers
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2309.03409
(cs)
[Submitted on 7 Sep 2023 (
v1
), last revised 15 Apr 2024 (this version, v3)]
Title:
Large Language Models as Optimizers
Authors:
Chengrun Yang
,
Xuezhi Wang
,
Yifeng Lu
,
Hanxiao Liu
,
Quoc V. Le
,
Denny Zhou
,
Xinyun Chen
View a PDF of the paper titled Large Language Models as Optimizers, by Chengrun Yang and 6 other authors
View PDF
HTML (experimental)
Abstract:
Optimization is ubiquitous. While derivative-based algorithms have been powerful tools for various problems, the absence of gradient imposes challenges on many real-world applications. In this work, we propose Optimization by PROmpting (OPRO), a simple and effective approach to leverage large language models (LLMs) as optimizers, where the optimization task is described in natural language. In each optimization step, the LLM generates new solutions from the prompt that contains previously generated solutions with their values, then the new solutions are evaluated and added to the prompt for the next optimization step. We first showcase OPRO on linear regression and traveling salesman problems, then move on to our main application in prompt optimization, where the goal is to find instructions that maximize the task accuracy. With a variety of LLMs, we demonstrate that the best prompts optimized by OPRO outperform human-designed prompts by up to 8% on GSM8K, and by up to 50% on Big-Bench Hard tasks. Code at
this https URL
.
Comments:
ICLR 2024; 42 pages, 26 figures, 15 tables. Code at
this https URL
Subjects:
Machine Learning (cs.LG)
; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2309.03409
[cs.LG]
(or
arXiv:2309.03409v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2309.03409
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Chengrun Yang [
view email
]
[v1]
Thu, 7 Sep 2023 00:07:15 UTC (4,422 KB)
[v2]
Thu, 7 Dec 2023 05:25:15 UTC (765 KB)
[v3]
Mon, 15 Apr 2024 07:50:32 UTC (765 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Large Language Models as Optimizers, by Chengrun Yang and 6 other authors
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
2023-09
Change to browse by:
cs
cs.AI
cs.CL
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
3 blog links
(
what is this?
)
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