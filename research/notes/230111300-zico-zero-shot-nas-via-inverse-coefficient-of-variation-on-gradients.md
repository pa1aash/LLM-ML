---
title: '[2301.11300] ZiCo: Zero-shot NAS via Inverse Coefficient of Variation on Gradients'
id: 230111300-zico-zero-shot-nas-via-inverse-coefficient-of-variation-on-gradients
tags:
- llm-nas-feedback-positioning-7125b1
- locus-l5
created: '2026-08-16T18:32:07.033887Z'
updated: '2026-08-16T18:33:59.621382Z'
source: https://arxiv.org/abs/2301.11300
source_domain: arxiv.org
fetched_at: '2026-08-16T18:32:07.033424Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Abstract-only arXiv listing page (fetch could not extract full PDF text due
  to JUNK_CONTENT bug); superseded by full-text note zico-zero-shot-nas-via-inverse-coefficient-of-variation-on-gradients-full-text
  which contains the extracted PDF body with Tables 1/3/4 correlation coefficients.
---

[2301.11300] ZiCo: Zero-shot NAS via Inverse Coefficient of Variation on Gradients
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2301.11300
(cs)
[Submitted on 26 Jan 2023 (
v1
), last revised 12 Apr 2023 (this version, v3)]
Title:
ZiCo: Zero-shot NAS via Inverse Coefficient of Variation on Gradients
Authors:
Guihong Li
,
Yuedong Yang
,
Kartikeya Bhardwaj
,
Radu Marculescu
View a PDF of the paper titled ZiCo: Zero-shot NAS via Inverse Coefficient of Variation on Gradients, by Guihong Li and 3 other authors
View PDF
HTML (experimental)
Abstract:
Neural Architecture Search (NAS) is widely used to automatically obtain the neural network with the best performance among a large number of candidate architectures. To reduce the search time, zero-shot NAS aims at designing training-free proxies that can predict the test performance of a given architecture. However, as shown recently, none of the zero-shot proxies proposed to date can actually work consistently better than a naive proxy, namely, the number of network parameters (#Params). To improve this state of affairs, as the main theoretical contribution, we first reveal how some specific gradient properties across different samples impact the convergence rate and generalization capacity of neural networks. Based on this theoretical analysis, we propose a new zero-shot proxy, ZiCo, the first proxy that works consistently better than #Params. We demonstrate that ZiCo works better than State-Of-The-Art (SOTA) proxies on several popular NAS-Benchmarks (NASBench101, NATSBench-SSS/TSS, TransNASBench-101) for multiple applications (e.g., image classification/reconstruction and pixel-level prediction). Finally, we demonstrate that the optimal architectures found via ZiCo are as competitive as the ones found by one-shot and multi-shot NAS methods, but with much less search time. For example, ZiCo-based NAS can find optimal architectures with 78.1%, 79.4%, and 80.4% test accuracy under inference budgets of 450M, 600M, and 1000M FLOPs, respectively, on ImageNet within 0.4 GPU days. Our code is available at
this https URL
.
Comments:
ICLR 2023 Spotlight
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2301.11300
[cs.LG]
(or
arXiv:2301.11300v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2301.11300
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Guihong Li [
view email
]
[v1]
Thu, 26 Jan 2023 18:38:56 UTC (1,225 KB)
[v2]
Wed, 1 Mar 2023 16:13:33 UTC (1,221 KB)
[v3]
Wed, 12 Apr 2023 22:45:09 UTC (1,222 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled ZiCo: Zero-shot NAS via Inverse Coefficient of Variation on Gradients, by Guihong Li and 3 other authors
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
2023-01
Change to browse by:
cs
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