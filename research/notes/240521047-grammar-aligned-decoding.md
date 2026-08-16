---
title: '[2405.21047] Grammar-Aligned Decoding'
id: 240521047-grammar-aligned-decoding
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T19:11:41.376903Z'
source: https://arxiv.org/abs/2405.21047
source_domain: arxiv.org
fetched_at: '2026-08-16T19:11:41.376544Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2405.21047] Grammar-Aligned Decoding
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2405.21047
(cs)
[Submitted on 31 May 2024 (
v1
), last revised 12 Dec 2025 (this version, v3)]
Title:
Grammar-Aligned Decoding
Authors:
Kanghee Park
,
Jiayu Wang
,
Taylor Berg-Kirkpatrick
,
Nadia Polikarpova
,
Loris D'Antoni
View a PDF of the paper titled Grammar-Aligned Decoding, by Kanghee Park and 4 other authors
View PDF
HTML (experimental)
Abstract:
Large Language Models (LLMs) struggle with reliably generating highly structured outputs, such as program code, mathematical formulas, or well-formed markup. Constrained decoding approaches mitigate this problem by greedily restricting what tokens an LLM can output at each step to guarantee that the output matches a given constraint. Specifically, in grammar-constrained decoding (GCD), the LLM's output must follow a given grammar. In this paper, we demonstrate that GCD techniques (and in general constrained decoding techniques) can distort the LLM's distribution, leading to outputs that are grammatical but appear with likelihoods that are not proportional to the ones given by the LLM, and so ultimately are low-quality. We call the problem of aligning sampling with a grammar constraint, grammar-aligned decoding (GAD), and propose adaptive sampling with approximate expected futures (ASAp), a decoding algorithm that guarantees the output to be grammatical while provably producing outputs that match the conditional probability of the LLM's distribution conditioned on the given grammar constraint. Our algorithm uses prior sample outputs to soundly overapproximate the future grammaticality of different output prefixes. Our evaluation on code generation and structured NLP tasks shows how ASAp often produces outputs with higher likelihood (according to the LLM's distribution) than existing GCD techniques, while still enforcing the desired grammatical constraints.
Comments:
Accepted to NeurIPS 2024
Subjects:
Artificial Intelligence (cs.AI)
; Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2405.21047
[cs.AI]
(or
arXiv:2405.21047v3
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2405.21047
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Jiayu Wang [
view email
]
[v1]
Fri, 31 May 2024 17:39:15 UTC (2,651 KB)
[v2]
Mon, 4 Nov 2024 22:04:00 UTC (2,655 KB)
[v3]
Fri, 12 Dec 2025 00:09:04 UTC (2,619 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Grammar-Aligned Decoding, by Kanghee Park and 4 other authors
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
2024-05
Change to browse by:
cs
cs.CL
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