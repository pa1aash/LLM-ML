---
title: '[2402.01817] LLMs Can''t Plan, But Can Help Planning in LLM-Modulo Frameworks'
id: 240201817-llms-cant-plan-but-can-help-planning-in-llm-modulo-frameworks
tags:
- llm-nas-feedback-positioning-7125b1
- self-correction
- mechanism-literature
created: '2026-08-16T15:53:51.308167Z'
updated: '2026-08-16T15:55:03.011885Z'
source: https://arxiv.org/abs/2402.01817
source_domain: arxiv.org
fetched_at: '2026-08-16T15:53:51.296217Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Kambhampati, Valmeekam, Guan, Verma, Stechly, Bhambri, Saldyt & Murthy (ICML
  2024 position paper; arXiv:2402.01817). Argues auto-regressive LLMs ''cannot, by
  themselves, do planning or self-verification'' and rejects both over-optimistic
  claims (LLMs can self-verify with the right prompting) and over-pessimistic claims
  (LLMs are mere syntax translators for symbolic solvers). Proposes the LLM-Modulo
  Framework: LLMs act as ''universal approximate knowledge sources'' generating candidates,
  paired in tight bi-directional interaction with EXTERNAL model-based verifiers that
  provide the actual correctness/soundness signal; the models driving those external
  verifiers can themselves be learned with LLM assistance. Directly relevant to the
  mechanism-literature question''s framing of ''intrinsic self-correction fails without
  external verification'' -- this is the general theoretical/position-paper articulation
  of that principle from the same author group as the self-verification-limitations
  empirical study, explicitly generalizing beyond that paper''s three toy domains
  to planning/reasoning broadly. Same first-author group (Kambhampati) as the self-verification-limitations
  paper already in this vault, which cites this LLM-Modulo paper as the general framework
  its own empirical findings ''fit into.'''
---

*Suggested by [[on-the-self-verification-limitations-of-large-language-models-on-reasoning-and-p]] — cited as the general LLM-Modulo framework this paper fits into, external-verifier architecture*

[2402.01817] LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2402.01817
(cs)
[Submitted on 2 Feb 2024 (
v1
), last revised 12 Jun 2024 (this version, v3)]
Title:
LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks
Authors:
Subbarao Kambhampati
,
Karthik Valmeekam
,
Lin Guan
,
Mudit Verma
,
Kaya Stechly
,
Siddhant Bhambri
,
Lucas Saldyt
,
Anil Murthy
View a PDF of the paper titled LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks, by Subbarao Kambhampati and 7 other authors
View PDF
HTML (experimental)
Abstract:
There is considerable confusion about the role of Large Language Models (LLMs) in planning and reasoning tasks. On one side are over-optimistic claims that LLMs can indeed do these tasks with just the right prompting or self-verification strategies. On the other side are perhaps over-pessimistic claims that all that LLMs are good for in planning/reasoning tasks are as mere translators of the problem specification from one syntactic format to another, and ship the problem off to external symbolic solvers. In this position paper, we take the view that both these extremes are misguided. We argue that auto-regressive LLMs cannot, by themselves, do planning or self-verification (which is after all a form of reasoning), and shed some light on the reasons for misunderstandings in the literature. We will also argue that LLMs should be viewed as universal approximate knowledge sources that have much more meaningful roles to play in planning/reasoning tasks beyond simple front-end/back-end format translators. We present a vision of {\bf LLM-Modulo Frameworks} that combine the strengths of LLMs with external model-based verifiers in a tighter bi-directional interaction regime. We will show how the models driving the external verifiers themselves can be acquired with the help of LLMs. We will also argue that rather than simply pipelining LLMs and symbolic components, this LLM-Modulo Framework provides a better neuro-symbolic approach that offers tighter integration between LLMs and symbolic components, and allows extending the scope of model-based planning/reasoning regimes towards more flexible knowledge, problem and preference specifications.
Subjects:
Artificial Intelligence (cs.AI)
; Machine Learning (cs.LG)
Cite as:
arXiv:2402.01817
[cs.AI]
(or
arXiv:2402.01817v3
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2402.01817
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
Proceedings of the 41 st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024
Submission history
From: Subbarao Kambhampati [
view email
]
[v1]
Fri, 2 Feb 2024 14:43:18 UTC (4,551 KB)
[v2]
Tue, 6 Feb 2024 01:29:37 UTC (4,552 KB)
[v3]
Wed, 12 Jun 2024 01:13:11 UTC (6,405 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks, by Subbarao Kambhampati and 7 other authors
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
2024-02
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