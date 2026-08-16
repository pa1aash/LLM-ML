---
title: '[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning'
id: 230311366v4-reflexion-language-agents-with-verbal-reinforcement-learning
tags:
- llm-nas-feedback-positioning-7125b1
- self-correction
- counter-evidence
- iterative-feedback
created: '2026-08-16T15:44:54.348038Z'
updated: '2026-08-16T15:50:49.450331Z'
source: https://arxiv.org/abs/2303.11366v4
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:54.347310Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Reflexion (Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao; 2023) reinforces
  LLM agents via linguistic self-reflection stored in an episodic memory buffer, without
  weight updates, across sequential-decision-making, coding, and reasoning tasks.
  Headline result: 91% pass@1 on HumanEval, beating contemporaneous GPT-4 zero-shot
  (80%). Critically, Reflexion''s feedback signal in the coding setting is grounded
  in EXTERNAL verification — actual unit-test execution results (pass/fail, error
  traces) — not the model''s own unaided judgment of quality; the paper''s ablations
  vary feedback type (scalar vs. free-form language) and source (external vs. internally
  simulated) and show source matters. This makes Reflexion a bounded counter-example
  to a ''feedback always degrades'' thesis: it demonstrates iterative self-refinement
  helping specifically when an external, ground-truth verifier (test execution) closes
  the loop, which is consistent with rather than contradicting an ''intrinsic self-correction
  fails without external verification'' account — a proposal-then-train-then-report-metric
  NAS loop with a small/quantized model may lack an analogous crisp external verifier
  that the model can act on, or the model may lack capacity to use it.'
---

[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2303.11366v4
(cs)
[Submitted on 20 Mar 2023 (
v1
), last revised 10 Oct 2023 (this version, v4)]
Title:
Reflexion: Language Agents with Verbal Reinforcement Learning
Authors:
Noah Shinn
,
Federico Cassano
,
Edward Berman
,
Ashwin Gopinath
,
Karthik Narasimhan
,
Shunyu Yao
View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors
View PDF
HTML (experimental)
Abstract:
Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.
Comments:
v4 contains a few additional experiments
Subjects:
Artificial Intelligence (cs.AI)
; Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2303.11366
[cs.AI]
(or
arXiv:2303.11366v4
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2303.11366
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Noah Shinn [
view email
]
[v1]
Mon, 20 Mar 2023 18:08:50 UTC (506 KB)
[v2]
Sun, 21 May 2023 06:20:36 UTC (404 KB)
[v3]
Sat, 10 Jun 2023 04:32:30 UTC (396 KB)
[v4]
Tue, 10 Oct 2023 05:21:45 UTC (386 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Reflexion: Language Agents with Verbal Reinforcement Learning, by Noah Shinn and 5 other authors
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
2023-03
Change to browse by:
cs
cs.CL
cs.LG
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