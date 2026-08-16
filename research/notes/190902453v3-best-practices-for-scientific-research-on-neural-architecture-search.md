---
title: '[1909.02453v3] Best Practices for Scientific Research on Neural Architecture
  Search'
id: 190902453v3-best-practices-for-scientific-research-on-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
- nas-methodology
- random-search-baseline
- nas-benchmarks
created: '2026-08-16T15:45:58.564073Z'
updated: '2026-08-16T15:49:44.238782Z'
source: https://arxiv.org/abs/1909.02453v3
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:58.563690Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Lindauer & Hutter (2020, v3), the canonical NAS-evaluation methodology checklist
  (automl.org/nas_checklist.pdf). Proposes 14 best practices grouped under code release,
  fair comparison, and detail reporting. Best Practice 8 explicitly distinguishes
  random SAMPLING (one draw, ~zero runtime) from random SEARCH (anytime procedure
  evaluating multiple samples over the same time budget as the compared method) and
  requires comparison against both, citing Sciuto et al. 2019 and Xie et al. 2019
  (random sampling can be strong in well-designed spaces) and Li & Talwalkar 2019
  (random search is very competitive). Best Practice 9 requires multiple seeded runs
  with mean+stdev reporting, since 'NAS methods are almost always stochastic.' Best
  Practices 4/10 push toward tabular/surrogate benchmarks, tabulating NAS-Bench-101
  (423k archs), NAS-Bench-201 (6k, 3 datasets), NAS-Bench-301 (10^18, surrogate).
  Notes many NAS benchmarks are 'relatively easy' -- random search often lands within
  0.5% of optimal -- meaning small claimed margins over random search require careful
  statistical treatment. This is the primary methodology-standards authority for evaluating
  any NAS paper's use of random-search baselines, seeds, and tabular benchmarks.
---

[1909.02453v3] Best Practices for Scientific Research on Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1909.02453v3
(cs)
[Submitted on 5 Sep 2019 (
v1
), last revised 3 Nov 2020 (this version, v3)]
Title:
Best Practices for Scientific Research on Neural Architecture Search
Authors:
Marius Lindauer
,
Frank Hutter
View a PDF of the paper titled Best Practices for Scientific Research on Neural Architecture Search, by Marius Lindauer and 1 other authors
View PDF
HTML (experimental)
Abstract:
Finding a well-performing architecture is often tedious for both DL practitioners and researchers, leading to tremendous interest in the automation of this task by means of neural architecture search (NAS). Although the community has made major strides in developing better NAS methods, the quality of scientific empirical evaluations in the young field of NAS is still lacking behind that of other areas of machine learning. To address this issue, we describe a set of possible issues and ways to avoid them, leading to the NAS best practices checklist available at
this http URL
.
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1909.02453
[cs.LG]
(or
arXiv:1909.02453v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1909.02453
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Marius Lindauer [
view email
]
[v1]
Thu, 5 Sep 2019 14:39:27 UTC (46 KB)
[v2]
Mon, 20 Jan 2020 08:28:00 UTC (65 KB)
[v3]
Tue, 3 Nov 2020 08:52:42 UTC (56 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Best Practices for Scientific Research on Neural Architecture Search, by Marius Lindauer and 1 other authors
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
2019-09
Change to browse by:
cs
stat
stat.ML
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
DBLP
- CS Bibliography
listing
|
bibtex
Marius Lindauer
Frank Hutter
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
---

## Full-text extraction (from PDF, arxiv.org/pdf/1909.02453v3, Lindauer & Hutter, v3 Nov 2020)

Authors: Marius Lindauer (Leibniz University Hannover), Frank Hutter (University of Freiburg & Bosch Center for AI). This is the canonical "NAS best practices checklist" paper (checklist at automl.org/nas_checklist.pdf), directly cited by the research query as a methodology-standards touchstone.

**Framing:** "the quality of scientific empirical evaluations in the young field of NAS is still lacking behind that of other areas of machine learning." Explicitly builds on and cites prior critiques: Sciuto et al. 2019 ("Evaluating the search phase of neural architecture search," arXiv:1902.08142), Li and Talwalkar 2019 ("Random search and reproducibility for neural architecture search," UAI), Xie et al. 2019 ("Exploring randomly wired neural networks for image recognition," arXiv:1904.01569), and Yang et al. 2020 ("NAS evaluation is frustratingly hard," ICLR, OpenReview id=HygrdpVKvr) — "these have led to serious scepticism of outsiders concerning NAS."

**Full list of 14 Best Practices (verbatim titles):**
1. Release Code for the Training Pipeline(s) you use — training pipeline (optimizer, epochs, LR schedule, augmentation, regularization) often matters more than the architecture itself; cites Yang et al. 2020 showing CutOut+ScheduledDropPath+auxiliary towers+AutoAugment+more channels/epochs on DARTS/CIFAR-10 yielded +3% combined vs <1% from choosing the best architecture alone.
2. Release Code for Your NAS Method.
3. Don't Wait Until You've Cleaned up the Code; release a labeled prototype dump immediately.
4. Use the Same NAS Benchmarks, not Just the Same Datasets — defines "NAS Benchmark" (Definition 3) = dataset with fixed train/test split + search space + runnable code with pre-defined hyperparameters. Gives Example 5: NAS-Bench-101 (Ying et al. 2019, ICML) as "the first tabular NAS benchmark" with pre-computed evaluations for all cells. Also references NAS-Bench-1Shot1, NAS-Bench-201 (Dong & Yang 2020, ICLR), NAS-Bench-NLP, and NAS-Bench-301 (Siems et al. 2020) as the first *surrogate* NAS benchmark (search space >10^18 architectures, ~60k evaluated subset + surrogate predictor models).
5. Run Ablation Studies — quantify which component changes drove results; praises Yang et al. 2020 for showing training protocol/search space/macro design "substantially impact overall performance."
6. Use the Same Evaluation Protocol for the Methods Being Compared — flags that NAS runs sometimes return a single final architecture vs. thousands sampled/evaluated to pick the best; these are NOT comparable regimes.
7. Evaluate Performance as a Function of Compute Resources — defines Architecture identification variant (Definition 7, only search cost counts) vs. AutoML variant (Definition 8, search + final training cost counts).
8. Compare Against Random Sampling and Random Search (DIRECTLY RELEVANT TO QUERY). Defines Random sampling (Definition 9: draw ONE random sample, return it; runtime ~0) vs Random search (Definition 10: draw random samples, evaluate each with a defined criterion, track best-so-far incumbent; anytime procedure run for the same time budget as the compared method). States: "many NAS papers avoid a comparison against these baselines. As Sciuto et al. (2019) and Xie et al. (2019) show, random sampling can already yield strong performance in a well-designed search space, and Li and Talwalkar (2019) show that random search can be very competitive." Explicit recommendation: compare against BOTH random sampling and random search "to assess whether good performance is due to a well-designed search space (and training pipeline) or due to the NAS method."
9. Perform Multiple Runs with Different Seeds — "NAS methods are almost always stochastic... re-running the same method on the same dataset does not necessarily lead to the same result (Li and Talwalkar, 2019)." Recommends reporting mean AND standard deviation (or median/quartiles if asymmetric) across repeated runs with controlled/reported seeds, "ideally... random seeds from 1 to 10."
10. Use Tabular or Surrogate Benchmarks If Possible — lists table of benchmarks (Table 1): NAS-Bench-101 (423k architectures, no one-shot support, constrained space), NAS-Bench-1Shot1 (6k-364k, one-shot yes, 3 subspaces of NB-101), NAS-Bench-201 (6k, one-shot yes, 3 datasets + learning curves), NAS-HPO (62,208, no one-shot, 4 datasets + NAS+HPO), NAS-Bench-NLP (15k, one-shot yes, NLP), NAS-Bench-301 (10^18, one-shot yes, surrogate benchmark).
11. Control Confounding Factors (hardware, DL library versions, runtime differences).
12. Report the Use of Hyperparameter Optimization — tuning the NAS method's own hyperparameters is itself "manual architecture engineering... replace[d]... by manual hyperparameter optimization of the NAS method"; this time should count as part of runtime.
13. Report End-to-End Resources Required for the Entire NAS Method — Example 11 formalizes: for k parallel search runs of time T_search each with validation time T_valid and final training T_final, total cost = k·(T_search+T_valid) [architecture-identification variant] or k·(T_search+T_valid)+T_final [AutoML variant].
14. Report All the Details of Your Experimental Setup (hardware, GPU/TPU type, DL library + version).

**Section 5, "Further Ways Forward":** Calls for a standardized library of diverse NAS benchmarks and an open-source library of NAS methods to control confounding factors community-wide. Notes "many of the current NAS benchmarks are relatively easy in the sense that even random search performs very well (often within 0.5% of optimal)" — directly relevant to why random-search baselines are load-bearing in this literature: on several tabular benchmarks the ceiling-to-random gap is small, so beating random search by any claimed margin needs care.

**Direct relevance to the query's methodology-standards question (THREE):** This paper is THE canonical checklist reference. Best Practice 8 (random sampling vs random search baselines, citing Li & Talwalkar 2019 and Sciuto et al. 2019 explicitly) and Best Practice 9 (multiple seeded runs, mean+stdev) are the two most directly load-bearing standards against which a "small quantised LLM beats random search" claim must be checked: (a) was the comparison against random SEARCH (anytime, same time/eval budget) or merely random SAMPLING (a single draw)? (b) how many seeds/repetitions, and was mean-vs-std reported, or only a single run? Best Practice 4/10 (use tabular/surrogate NAS benchmarks: NAS-Bench-101, NAS-Bench-201, NAS-Bench-301) also directly matches the query's named benchmarks (NAS-Bench-101/201, NATS-Bench, NAS-Bench-Suite-Zero) as the expected evaluation surface.
