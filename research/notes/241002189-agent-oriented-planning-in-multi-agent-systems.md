---
title: '[2410.02189] Agent-Oriented Planning in Multi-Agent Systems'
id: 241002189-agent-oriented-planning-in-multi-agent-systems
tags:
- llm-nas-feedback-positioning-7125b1
- tangential
- counter-evidence-context
created: '2026-08-16T15:45:33.341127Z'
updated: '2026-08-16T15:52:18.803390Z'
source: https://arxiv.org/abs/2410.02189
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:33.340472Z'
fetch_provider: builtin
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Li, Xie, Li, Tsung, Ding, Li, ''Agent-Oriented Planning in Multi-Agent Systems''
  (arXiv:2410.02189, ICLR 2025). NOT a NAS or architecture-search paper — it is a
  general multi-agent LLM task-planning framework (AOP) that decomposes user queries
  into sub-tasks for specialist agents, evaluated for solvability/completeness/non-redundancy,
  with a meta-agent reward model and an integrated feedback loop for adjusting sub-tasks/scheduling.
  Only the arXiv abstract page was fetched (691 words); no methodology or numeric
  results beyond the abstract were captured.\n\nRelevance is tangential rather than
  direct: the abstract claims ''we integrate a feedback loop into AOP to further enhance
  the effectiveness and robustness of such a problem-solving process'' and reports
  that ''extensive experiments demonstrate the advancement of AOP in solving real-world
  problems compared to both single-agent systems and existing planning strategies
  for multi-agent systems'' — i.e. this is a published case where an iterative feedback
  loop is reported to IMPROVE a multi-agent LLM system''s output quality. This is
  potentially useful as Q4 counter-evidence context (a domain where feedback reportedly
  helps), but it differs from the target paper''s claim in kind: AOP''s feedback loop
  operates over task decomposition/scheduling in general problem-solving, not over
  architecture or program search proposals scored against a fixed numeric objective,
  so it bounds rather than directly rebuts a NAS-specific feedback-degradation claim.
  Should not be over-weighted as a rebuttal; flagged as weak/tangential evidence only.'
---

[2410.02189] Agent-Oriented Planning in Multi-Agent Systems
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Artificial Intelligence
arXiv:2410.02189
(cs)
[Submitted on 3 Oct 2024 (
v1
), last revised 11 Mar 2025 (this version, v2)]
Title:
Agent-Oriented Planning in Multi-Agent Systems
Authors:
Ao Li
,
Yuexiang Xie
,
Songze Li
,
Fugee Tsung
,
Bolin Ding
,
Yaliang Li
View a PDF of the paper titled Agent-Oriented Planning in Multi-Agent Systems, by Ao Li and 5 other authors
View PDF
HTML (experimental)
Abstract:
Through the collaboration of multiple LLM-empowered agents possessing diverse expertise and tools, multi-agent systems achieve impressive progress in solving real-world problems. Given the user queries, the meta-agents, serving as the brain within multi-agent systems, are required to decompose the queries into multiple sub-tasks that can be allocated to suitable agents capable of solving them, so-called agent-oriented planning. In this study, we identify three critical design principles of agent-oriented planning, including solvability, completeness, and non-redundancy, to ensure that each sub-task can be effectively resolved, resulting in satisfactory responses to user queries. These principles further inspire us to propose AOP, a novel framework for agent-oriented planning in multi-agent systems, leveraging a fast task decomposition and allocation process followed by an effective and efficient evaluation via a reward model. According to the evaluation results, the meta-agent is also responsible for promptly making necessary adjustments to sub-tasks and scheduling. Besides, we integrate a feedback loop into AOP to further enhance the effectiveness and robustness of such a problem-solving process. Extensive experiments demonstrate the advancement of AOP in solving real-world problems compared to both single-agent systems and existing planning strategies for multi-agent systems. The source code is available at
this https URL
Comments:
Accepted by ICLR'2025
Subjects:
Artificial Intelligence (cs.AI)
; Machine Learning (cs.LG); Multiagent Systems (cs.MA)
Cite as:
arXiv:2410.02189
[cs.AI]
(or
arXiv:2410.02189v2
[cs.AI]
for this version)
https://doi.org/10.48550/arXiv.2410.02189
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Yuexiang Xie [
view email
]
[v1]
Thu, 3 Oct 2024 04:07:51 UTC (386 KB)
[v2]
Tue, 11 Mar 2025 11:22:17 UTC (403 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Agent-Oriented Planning in Multi-Agent Systems, by Ao Li and 5 other authors
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
2024-10
Change to browse by:
cs
cs.LG
cs.MA
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