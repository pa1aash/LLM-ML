---
title: '[2303.17651v2] Self-Refine: Iterative Refinement with Self-Feedback'
id: 230317651v2-self-refine-iterative-refinement-with-self-feedback
tags:
- llm-nas-feedback-positioning-7125b1
- self-refine
- self-correction
- iterative-feedback
created: '2026-08-16T15:44:34.866390Z'
updated: '2026-08-16T15:45:48.913100Z'
source: https://arxiv.org/abs/2303.17651v2
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:34.866014Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Madaan et al. (arXiv:2303.17651, 2023), the foundational ''Self-Refine''
  paper: a single LLM generates an output, then critiques and revises its own output
  iteratively, with no additional training or RL. Across 7 tasks (dialog, math reasoning,
  code, etc.) using GPT-3.5/ChatGPT/GPT-4, self-refine outputs were preferred by humans
  and automatic metrics over one-shot generation, improving ~20% absolute on average.
  This is the canonical positive result for self-feedback that any paper claiming
  feedback DEGRADES LLM-guided search must position against; note Self-Refine''s tasks
  are primarily generative/stylistic/reasoning tasks with soft or model-judged quality
  signals, not hard combinatorial search with an external ground-truth objective (like
  NAS validation accuracy), which is a scope distinction the target paper can use
  to bound rather than contradict this result.'
---

[2303.17651v2] Self-Refine: Iterative Refinement with Self-Feedback
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2303.17651v2
(cs)
[Submitted on 30 Mar 2023 (
v1
), last revised 25 May 2023 (this version, v2)]
Title:
Self-Refine: Iterative Refinement with Self-Feedback
Authors:
Aman Madaan
,
Niket Tandon
,
Prakhar Gupta
,
Skyler Hallinan
,
Luyu Gao
,
Sarah Wiegreffe
,
Uri Alon
,
Nouha Dziri
,
Shrimai Prabhumoye
,
Yiming Yang
,
Shashank Gupta
,
Bodhisattwa Prasad Majumder
,
Katherine Hermann
,
Sean Welleck
,
Amir Yazdanbakhsh
,
Peter Clark
View a PDF of the paper titled Self-Refine: Iterative Refinement with Self-Feedback, by Aman Madaan and 15 other authors
View PDF
HTML (experimental)
Abstract:
Like humans, large language models (LLMs) do not always generate the best output on their first try. Motivated by how humans refine their written text, we introduce Self-Refine, an approach for improving initial outputs from LLMs through iterative feedback and refinement. The main idea is to generate an initial output using an LLMs; then, the same LLMs provides feedback for its output and uses it to refine itself, iteratively. Self-Refine does not require any supervised training data, additional training, or reinforcement learning, and instead uses a single LLM as the generator, refiner, and feedback provider. We evaluate Self-Refine across 7 diverse tasks, ranging from dialog response generation to mathematical reasoning, using state-of-the-art (GPT-3.5, ChatGPT, and GPT-4) LLMs. Across all evaluated tasks, outputs generated with Self-Refine are preferred by humans and automatic metrics over those generated with the same LLM using conventional one-step generation, improving by ~20% absolute on average in task performance. Our work demonstrates that even state-of-the-art LLMs like GPT-4 can be further improved at test time using our simple, standalone approach.
Comments:
Code, data, and demo at
this https URL
Subjects:
Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2303.17651
[cs.CL]
(or
arXiv:2303.17651v2
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2303.17651
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Uri Alon [
view email
]
[v1]
Thu, 30 Mar 2023 18:30:01 UTC (15,993 KB)
[v2]
Thu, 25 May 2023 19:13:47 UTC (1,505 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Self-Refine: Iterative Refinement with Self-Feedback, by Aman Madaan and 15 other authors
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
2023-03
Change to browse by:
cs
cs.AI
cs.LG
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
1 blog link
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