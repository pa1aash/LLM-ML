---
title: '[2108.13264] Deep Reinforcement Learning at the Edge of the Statistical Precipice'
id: 210813264-deep-reinforcement-learning-at-the-edge-of-the-statistical-precipice
tags:
- llm-nas-feedback-positioning-7125b1
- statistical-methodology
- benchmark-evaluation
- rliable
created: '2026-08-16T15:44:36.778288Z'
updated: '2026-08-16T15:46:00.476438Z'
source: https://arxiv.org/abs/2108.13264
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:36.777901Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Agarwal, Schwarzer, Castro, Courville & Bellemare (NeurIPS 2021 Outstanding
  Paper; arXiv:2108.13264) argue that comparing point estimates (mean/median) of aggregate
  performance across a small number of runs is statistically unreliable and has produced
  discrepant conclusions on benchmarks like Atari 100k, Procgen, and DeepMind Control
  Suite. They advocate reporting interval estimates, performance profiles (distributions
  over all runs/tasks), and robust aggregate metrics such as the interquartile mean
  (IQM) to bound uncertainty when only a handful of runs are affordable, releasing
  the open-source ''rliable'' library to operationalize this. This is a load-bearing
  methodology citation for the paper''s Q3 statistical-standards analysis: it is the
  standard NAS/RL reviewers now invoke to demand seeds, confidence intervals, and
  robust aggregation instead of single-run or small-N mean comparisons — directly
  bears on whether ''beats random search'' claims from a handful of LLM proposals
  meet the current evidentiary bar, and on the mean-of-population vs. expected-best-of-k
  estimand question since population-level point estimates and best-of-k order statistics
  require different reporting under uncertainty.'
---

[2108.13264] Deep Reinforcement Learning at the Edge of the Statistical Precipice
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2108.13264
(cs)
[Submitted on 30 Aug 2021 (
v1
), last revised 5 Jan 2022 (this version, v4)]
Title:
Deep Reinforcement Learning at the Edge of the Statistical Precipice
Authors:
Rishabh Agarwal
,
Max Schwarzer
,
Pablo Samuel Castro
,
Aaron Courville
,
Marc G. Bellemare
View a PDF of the paper titled Deep Reinforcement Learning at the Edge of the Statistical Precipice, by Rishabh Agarwal and 4 other authors
View PDF
HTML (experimental)
Abstract:
Deep reinforcement learning (RL) algorithms are predominantly evaluated by comparing their relative performance on a large suite of tasks. Most published results on deep RL benchmarks compare point estimates of aggregate performance such as mean and median scores across tasks, ignoring the statistical uncertainty implied by the use of a finite number of training runs. Beginning with the Arcade Learning Environment (ALE), the shift towards computationally-demanding benchmarks has led to the practice of evaluating only a small number of runs per task, exacerbating the statistical uncertainty in point estimates. In this paper, we argue that reliable evaluation in the few run deep RL regime cannot ignore the uncertainty in results without running the risk of slowing down progress in the field. We illustrate this point using a case study on the Atari 100k benchmark, where we find substantial discrepancies between conclusions drawn from point estimates alone versus a more thorough statistical analysis. With the aim of increasing the field's confidence in reported results with a handful of runs, we advocate for reporting interval estimates of aggregate performance and propose performance profiles to account for the variability in results, as well as present more robust and efficient aggregate metrics, such as interquartile mean scores, to achieve small uncertainty in results. Using such statistical tools, we scrutinize performance evaluations of existing algorithms on other widely used RL benchmarks including the ALE, Procgen, and the DeepMind Control Suite, again revealing discrepancies in prior comparisons. Our findings call for a change in how we evaluate performance in deep RL, for which we present a more rigorous evaluation methodology, accompanied with an open-source library rliable, to prevent unreliable results from stagnating the field.
Comments:
Outstanding Paper Award at NeurIPS 2021. Website:
this https URL
. 28 Pages, 33 Figures
Subjects:
Machine Learning (cs.LG)
; Artificial Intelligence (cs.AI); Methodology (stat.ME); Machine Learning (stat.ML)
Cite as:
arXiv:2108.13264
[cs.LG]
(or
arXiv:2108.13264v4
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2108.13264
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Rishabh Agarwal [
view email
]
[v1]
Mon, 30 Aug 2021 14:23:48 UTC (20,260 KB)
[v2]
Tue, 5 Oct 2021 21:05:00 UTC (21,004 KB)
[v3]
Wed, 13 Oct 2021 04:23:11 UTC (21,373 KB)
[v4]
Wed, 5 Jan 2022 18:45:18 UTC (22,380 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Deep Reinforcement Learning at the Edge of the Statistical Precipice, by Rishabh Agarwal and 4 other authors
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
2021-08
Change to browse by:
cs
cs.AI
stat
stat.ME
stat.ML
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
1 blog link
(
what is this?
)
DBLP
- CS Bibliography
listing
|
bibtex
Rishabh Agarwal
Max Schwarzer
Pablo Samuel Castro
Aaron C. Courville
Marc G. Bellemare
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