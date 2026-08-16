---
title: '[2604.03616] The Format Tax'
id: 260403616-the-format-tax
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T19:11:42.073564Z'
source: https://arxiv.org/abs/2604.03616
source_domain: arxiv.org
fetched_at: '2026-08-16T19:11:42.073197Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2604.03616] The Format Tax
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2604.03616
(cs)
[Submitted on 4 Apr 2026]
Title:
The Format Tax
Authors:
Ivan Yee Lee
,
Loris D'Antoni
,
Taylor Berg-Kirkpatrick
View a PDF of the paper titled The Format Tax, by Ivan Yee Lee and 2 other authors
View PDF
HTML (experimental)
Abstract:
Asking a large language model to respond in JSON should be a formatting choice, not a capability tax. Yet we find that structured output requirements -- JSON, XML, LaTeX, Markdown -- substantially degrade reasoning and writing performance across open-weight models. The research response has focused on constrained decoding, but sampling bias accounts for only a fraction of the degradation. The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied. This diagnosis points to a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy. Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy. Notably, most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close. Code is available at
this https URL
.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2604.03616
[cs.CL]
(or
arXiv:2604.03616v1
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2604.03616
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Ivan Yee Lee [
view email
]
[v1]
Sat, 4 Apr 2026 07:16:28 UTC (1,558 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled The Format Tax, by Ivan Yee Lee and 2 other authors
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
2026-04
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