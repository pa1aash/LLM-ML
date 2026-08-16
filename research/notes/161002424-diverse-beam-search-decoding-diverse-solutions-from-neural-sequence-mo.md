---
title: '[1610.02424] Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence
  Models'
id: 161002424-diverse-beam-search-decoding-diverse-solutions-from-neural-sequence-mo
tags:
- llm-nas-feedback-positioning-7125b1
- decoding-diversity
- mode-collapse
- beam-search
created: '2026-08-16T15:50:20.242499Z'
updated: '2026-08-16T15:50:35.151865Z'
source: https://arxiv.org/abs/1610.02424
source_domain: arxiv.org
fetched_at: '2026-08-16T15:50:20.242088Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Vijayakumar et al. (AAAI 2018; arXiv:1610.02424), the foundational Diverse
  Beam Search paper: standard beam search explores the search space in a greedy left-right
  fashion retaining only the top-B candidates, which the authors state directly ''result[s]
  in sequences that differ only slightly from each other'' -- i.e., near-duplicate/collapsed
  outputs are a well-documented, decades-old artifact of standard greedy decoding
  search procedures themselves, not a special or novel finding requiring an LLM-specific
  or feedback-specific explanation. Diverse Beam Search (DBS) fixes this by optimizing
  a diversity-augmented objective during search, and the authors show DBS also finds
  BETTER top-1 solutions than plain beam search by better balancing exploration/exploitation,
  evaluated on image captioning, machine translation, and visual question generation.
  Load-bearing rival-explanation source for the target paper: any observation of an
  LLM proposing near-identical architecture templates could be attributable to standard
  greedy/low-diversity decoding search dynamics documented since 2016, independent
  of whatever role iterative feedback plays -- reviewers will expect this confound
  to be addressed or ruled out via decoding-parameter ablation (temperature/top-p/DBS-style
  diversity penalty) before attributing collapse to feedback per se.'
---

*Suggested by [[240105054v2-generating-diverse-and-high-quality-texts-by-minimum-bayes-risk-deco]] — diverse beam search is the named baseline decoding-diversity method the MBR diversity paper benchmarks against; primary source for decoding-diversity mechanism literature*

[1610.02424] Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:1610.02424
(cs)
[Submitted on 7 Oct 2016 (
v1
), last revised 22 Oct 2018 (this version, v2)]
Title:
Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models
Authors:
Ashwin K Vijayakumar
,
Michael Cogswell
,
Ramprasath R. Selvaraju
,
Qing Sun
,
Stefan Lee
,
David Crandall
,
Dhruv Batra
View a PDF of the paper titled Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models, by Ashwin K Vijayakumar and 6 other authors
View PDF
HTML (experimental)
Abstract:
Neural sequence models are widely used to model time-series data. Equally ubiquitous is the usage of beam search (BS) as an approximate inference algorithm to decode output sequences from these models. BS explores the search space in a greedy left-right fashion retaining only the top-B candidates - resulting in sequences that differ only slightly from each other. Producing lists of nearly identical sequences is not only computationally wasteful but also typically fails to capture the inherent ambiguity of complex AI tasks. To overcome this problem, we propose Diverse Beam Search (DBS), an alternative to BS that decodes a list of diverse outputs by optimizing for a diversity-augmented objective. We observe that our method finds better top-1 solutions by controlling for the exploration and exploitation of the search space - implying that DBS is a better search algorithm. Moreover, these gains are achieved with minimal computational or memory over- head as compared to beam search. To demonstrate the broad applicability of our method, we present results on image captioning, machine translation and visual question generation using both standard quantitative metrics and qualitative human studies. Further, we study the role of diversity for image-grounded language generation tasks as the complexity of the image changes. We observe that our method consistently outperforms BS and previously proposed techniques for diverse decoding from neural sequence models.
Comments:
16 pages; accepted at AAAI 2018
Subjects:
Artificial Intelligence (cs.AI)
; Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:1610.02424
[cs.AI]
(or
arXiv:1610.02424v2
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.1610.02424
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Ashwin Kalyan [
view email
]
[v1]
Fri, 7 Oct 2016 20:56:47 UTC (7,887 KB)
[v2]
Mon, 22 Oct 2018 13:48:32 UTC (7,650 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models, by Ashwin K Vijayakumar and 6 other authors
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
2016-10
Change to browse by:
cs
cs.CL
cs.CV
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
DBLP
- CS Bibliography
listing
|
bibtex
Ashwin K. Vijayakumar
Michael Cogswell
Ramprasaath R. Selvaraju
Ramprasath R. Selvaraju
Qing Sun
…
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