---
title: '[2402.08115] On the Self-Verification Limitations of Large Language Models
  on Reasoning and Planning Tasks'
id: 240208115-on-the-self-verification-limitations-of-large-language-models-on-reaso
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:44:10.713457Z'
updated: '2026-08-16T15:45:29.153744Z'
source: https://arxiv.org/abs/2402.08115
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:10.713077Z'
fetch_provider: builtin
status: deprecated
type: note
tier: institutional
content_type: paper
deprecated: false
---

[2402.08115] On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2402.08115
(cs)
[Submitted on 12 Feb 2024 (
v1
), last revised 3 Aug 2024 (this version, v2)]
Title:
On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks
Authors:
Kaya Stechly
,
Karthik Valmeekam
,
Subbarao Kambhampati
View a PDF of the paper titled On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks, by Kaya Stechly and 2 other authors
View PDF
HTML (experimental)
Abstract:
There has been considerable divergence of opinion on the reasoning abilities of Large Language Models (LLMs). While the initial optimism that reasoning might emerge automatically with scale has been tempered thanks to a slew of counterexamples--ranging from multiplication to simple planning--there persists a wide spread belief that LLMs can self-critique and improve their own solutions in an iterative fashion. This belief seemingly rests on the assumption that verification of correctness should be easier than generation--a rather classical argument from computational complexity--which should be irrelevant to LLMs to the extent that what they are doing is approximate retrieval. In this paper, we set out to systematically investigate the effectiveness of iterative prompting in the context of reasoning and planning. We present a principled empirical study of the performance of GPT-4 in three domains: Game of 24, Graph Coloring, and STRIPS planning. We experiment both with the model critiquing its own answers and with an external correct reasoner verifying proposed solutions. In each case, we analyze whether the content of criticisms actually affects bottom line performance, and whether we can ablate elements of the augmented system without losing performance. We observe significant performance collapse with self-critique and significant performance gains with sound external verification. We also note that merely re-prompting with a sound verifier maintains most of the benefits of more involved setups.
Comments:
arXiv admin note: text overlap with
arXiv:2310.12397
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2402.08115
[cs.AI]
(or
arXiv:2402.08115v2
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2402.08115
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Kaya Stechly [
view email
]
[v1]
Mon, 12 Feb 2024 23:11:01 UTC (673 KB)
[v2]
Sat, 3 Aug 2024 21:25:31 UTC (671 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks, by Kaya Stechly and 2 other authors
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