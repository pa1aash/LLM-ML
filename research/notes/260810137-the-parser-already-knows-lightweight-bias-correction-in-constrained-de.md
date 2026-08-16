---
title: '[2608.10137] The Parser Already Knows: Lightweight Bias Correction in Constrained
  Decoding'
id: 260810137-the-parser-already-knows-lightweight-bias-correction-in-constrained-de
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T19:11:42.958960Z'
source: https://arxiv.org/abs/2608.10137
source_domain: arxiv.org
fetched_at: '2026-08-16T19:11:42.958587Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2608.10137] The Parser Already Knows: Lightweight Bias Correction in Constrained Decoding
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2608.10137
(cs)
[Submitted on 10 Aug 2026]
Title:
The Parser Already Knows: Lightweight Bias Correction in Constrained Decoding
Authors:
Işıl Özgü
,
Yaoxuan Wu
,
Guy Van den Broeck
,
Miryung Kim
View a PDF of the paper titled The Parser Already Knows: Lightweight Bias Correction in Constrained Decoding, by I\c{s}{\i}l \"Ozg\"u and 3 other authors
View PDF
HTML (experimental)
Abstract:
Grammar Constrained Decoding (GCD) forces Language Models (LMs) to produce syntactically valid outputs by masking out non-conforming tokens at each step. However, rigid masking distorts the model's underlying probability distribution, often biasing generation toward valid but suboptimal outputs. While online sampling restores this distribution, it requires computationally expensive iterative resampling. As a result, existing methods force a compromise between output quality and inference latency. Our key insight is that the internal parser and lexer states inherently maintained during incremental parsing already encode future grammatical validity -- exactly the information required to restore the LM's true distribution. We propose a lightweight, offline-trained logit correction conditioned on this syntactic and lexical state together with candidate next tokens. Because these states are already computed as a necessary part of incremental parsing for masking, extracting them adds negligible overhead while leaving the base LM's weights completely untouched. Across several grammars, this correction substantially closes the gap between the masked distribution and the LM's true distribution, consistently outperforming both masking and online sampling. Even its lightest variant, which relies on the candidate next token alone, still matches or exceeds both baselines: the next token itself carries an implicit lookahead, much like how parsers commonly use a lookahead token to resolve ambiguous decisions. By restoring the probability mass that masking removes, it reconciles the LM's probabilistic integrity with grammar conformance.
Comments:
9 pages, 5 figures
Subjects:
Computation and Language (cs.CL)
; Machine Learning (cs.LG)
ACM
classes:
I.2.7; F.4.2
Cite as:
arXiv:2608.10137
[cs.CL]
(or
arXiv:2608.10137v1
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2608.10137
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Işıl Özgü [
view email
]
[v1]
Mon, 10 Aug 2026 18:52:43 UTC (233 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled The Parser Already Knows: Lightweight Bias Correction in Constrained Decoding, by I\c{s}{\i}l \"Ozg\"u and 3 other authors
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
2026-08
Change to browse by:
cs
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