---
title: '[2311.08516] LLMs cannot find reasoning errors, but can correct them given
  the error location'
id: 231108516-llms-cannot-find-reasoning-errors-but-can-correct-them-given-the-error
tags:
- llm-nas-feedback-positioning-7125b1
- self-correction
- intrinsic-vs-external-verification
- mistake-finding
created: '2026-08-16T15:44:35.940838Z'
updated: '2026-08-16T15:45:54.467222Z'
source: https://arxiv.org/abs/2311.08516
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:35.940439Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Tyen et al. (ACL 2024 Findings; arXiv:2311.08516) directly establish the
  mechanism behind self-correction failure: LLMs'' poor self-correction on logical/reasoning
  errors (citing Huang et al. 2023''s finding that self-correction ''causes correct
  answers to become incorrect, resulting in worse performance overall'') stems specifically
  from an inability to FIND mistakes, not an inability to fix them once found. When
  ground-truth error locations are supplied externally (a backtracking setup), correction
  ability is robust and boosts performance across 5 reasoning tasks; without that
  external signal, self-correction degrades results. They release BIG-Bench Mistake
  and show a small out-of-domain-trained classifier outperforms a large LLM at mistake-finding.
  This is the single strongest mechanism-literature anchor for ''intrinsic self-correction
  fails without external verification'' — it demonstrates the failure mode (self-generated
  feedback is uninformative/noisy, not that revision itself is broken) that a small-model
  LLM-NAS feedback-degrades-search paper would need to either replicate mechanistically
  or distinguish from.'
---

[2311.08516] LLMs cannot find reasoning errors, but can correct them given the error location
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2311.08516
(cs)
[Submitted on 14 Nov 2023 (
v1
), last revised 4 Jun 2024 (this version, v3)]
Title:
LLMs cannot find reasoning errors, but can correct them given the error location
Authors:
Gladys Tyen
,
Hassan Mansoor
,
Victor Cărbune
,
Peter Chen
,
Tony Mak
View a PDF of the paper titled LLMs cannot find reasoning errors, but can correct them given the error location, by Gladys Tyen and 4 other authors
View PDF
HTML (experimental)
Abstract:
While self-correction has shown promise in improving LLM outputs in terms of style and quality (e.g. Chen et al., 2023b; Madaan et al., 2023), recent attempts to self-correct logical or reasoning errors often cause correct answers to become incorrect, resulting in worse performances overall (Huang et al., 2023). In this paper, we show that poor self-correction performance stems from LLMs' inability to find logical mistakes, rather than their ability to correct a known mistake. Firstly, we benchmark several state-of-the-art LLMs on their mistake-finding ability and demonstrate that they generally struggle with the task, even in highly objective, unambiguous cases. Secondly, we test the correction abilities of LLMs -- separately from mistake finding -- using a backtracking setup that feeds ground truth mistake location information to the model. We show that this boosts downstream task performance across our 5 reasoning tasks, indicating that LLMs' correction abilities are robust. Finally, we show that it is possible to obtain mistake location information without ground truth labels or in-domain training data. We train a small classifier with out-of-domain data, which exhibits stronger mistake-finding performance than prompting a large model. We release our dataset of LLM-generated logical mistakes, BIG-Bench Mistake, to enable further research into locating LLM reasoning mistakes.
Comments:
ACL 2024 Findings
Subjects:
Artificial Intelligence (cs.AI)
; Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2311.08516
[cs.AI]
(or
arXiv:2311.08516v3
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2311.08516
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Gladys Tyen [
view email
]
[v1]
Tue, 14 Nov 2023 20:12:38 UTC (7,191 KB)
[v2]
Tue, 9 Jan 2024 03:32:32 UTC (7,191 KB)
[v3]
Tue, 4 Jun 2024 10:25:13 UTC (7,319 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled LLMs cannot find reasoning errors, but can correct them given the error location, by Gladys Tyen and 4 other authors
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
2023-11
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