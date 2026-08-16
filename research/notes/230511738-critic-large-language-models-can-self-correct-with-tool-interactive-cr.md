---
title: '[2305.11738] CRITIC: Large Language Models Can Self-Correct with Tool-Interactive
  Critiquing'
id: 230511738-critic-large-language-models-can-self-correct-with-tool-interactive-cr
tags:
- llm-nas-feedback-positioning-7125b1
- self-correction
- nas-priority-anchor
created: '2026-08-16T15:53:39.802700Z'
updated: '2026-08-16T15:54:58.614891Z'
source: https://arxiv.org/abs/2305.11738
source_domain: arxiv.org
fetched_at: '2026-08-16T15:53:39.797544Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Gou, Shao, Gong, Shen, Yang, Duan & Chen (ICLR 2024; arXiv:2305.11738, first
  posted May 2023). Introduces CRITIC, a framework letting LLMs validate and revise
  their own outputs by interacting with EXTERNAL TOOLS (search engines, code interpreters,
  etc.) rather than relying on purely intrinsic self-critique. Evaluated on free-form
  QA, mathematical program synthesis, and toxicity reduction, finding CRITIC ''consistently
  enhances the performance of LLMs.'' Load-bearing for the mechanism-literature question:
  the abstract explicitly frames the result as evidence for ''the crucial importance
  of external feedback in promoting the ongoing self-improvement of LLMs'' -- i.e.,
  this paper''s own positive result depends on tool-mediated external verification,
  not pure self-critique, which is consistent with (not contradictory to) the ''intrinsic
  self-correction fails without external verification'' thesis. Per the self-verification-limitations
  paper (Stechly/Valmeekam/Kambhampati, already in this vault), CRITIC''s authors
  were ''the first to notice that, in some cases, LLM self-critique can lead to decreases
  in performance when compared to sound verification'' -- makes this the earliest
  documented instance in the priority chain for self-refinement degrading performance
  without external grounding, predating the 2024 self-verification-limitations study.'
---

*Suggested by [[on-the-self-verification-limitations-of-large-language-models-on-reasoning-and-p]] — cited as first work to notice self-critique can decrease LLM performance vs sound verification*

[2305.11738] CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2305.11738
(cs)
[Submitted on 19 May 2023 (
v1
), last revised 21 Feb 2024 (this version, v4)]
Title:
CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing
Authors:
Zhibin Gou
,
Zhihong Shao
,
Yeyun Gong
,
Yelong Shen
,
Yujiu Yang
,
Nan Duan
,
Weizhu Chen
View a PDF of the paper titled CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing, by Zhibin Gou and 6 other authors
View PDF
HTML (experimental)
Abstract:
Recent developments in large language models (LLMs) have been impressive. However, these models sometimes show inconsistencies and problematic behavior, such as hallucinating facts, generating flawed code, or creating offensive and toxic content. Unlike these models, humans typically utilize external tools to cross-check and refine their initial content, like using a search engine for fact-checking, or a code interpreter for debugging. Inspired by this observation, we introduce a framework called CRITIC that allows LLMs, which are essentially "black boxes" to validate and progressively amend their own outputs in a manner similar to human interaction with tools. More specifically, starting with an initial output, CRITIC interacts with appropriate tools to evaluate certain aspects of the text, and then revises the output based on the feedback obtained during this validation process. Comprehensive evaluations involving free-form question answering, mathematical program synthesis, and toxicity reduction demonstrate that CRITIC consistently enhances the performance of LLMs. Meanwhile, our research highlights the crucial importance of external feedback in promoting the ongoing self-improvement of LLMs.
Comments:
ICLR 2024
Subjects:
Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI)
Cite as:
arXiv:2305.11738
[cs.CL]
(or
arXiv:2305.11738v4
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2305.11738
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Zhibin Gou [
view email
]
[v1]
Fri, 19 May 2023 15:19:44 UTC (465 KB)
[v2]
Sat, 30 Sep 2023 08:35:29 UTC (646 KB)
[v3]
Fri, 16 Feb 2024 08:17:39 UTC (653 KB)
[v4]
Wed, 21 Feb 2024 12:59:21 UTC (653 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing, by Zhibin Gou and 6 other authors
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