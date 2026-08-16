---
title: '[2304.01910] On the Variance of Neural Network Training with respect to Test
  Sets and Distributions'
id: 230401910-on-the-variance-of-neural-network-training-with-respect-to-test-sets-a
tags:
- llm-nas-feedback-positioning-7125b1
- variance-methodology
- statistical-independence
- nas-evaluation-methodology
created: '2026-08-16T15:45:20.838546Z'
updated: '2026-08-16T15:46:38.197623Z'
source: https://arxiv.org/abs/2304.01910
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:20.838082Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Keller Jordan (2023, v4 June 2024). Studies why repeated neural-network
  training runs show substantial test-set performance variance despite identical hyperparameters.
  Key findings: (1) CIFAR-10/ImageNet trainings have little variance on the underlying
  test *distribution* despite high variance on the finite sampled test *set*; (2)
  trained networks make approximately statistically independent errors across repeated
  training runs relative to their per-example average error rate — i.e., errors are
  not systematically correlated run-to-run; (3) this test-set variance is proven to
  be a downstream consequence of the class-calibration property (Jiang et al. 2021),
  yielding a closed-form variance-prediction formula for binary classification; (4)
  preliminary studies of how data augmentation, learning rate, fine-tuning instability,
  and distribution shift modulate this variance. Directly relevant to question THREE''s
  statistical-independence and sample-size/seed requirements: provides the quantitative
  baseline for how much apparent performance difference between two architectures/methods
  on a fixed test set is attributable to training-run noise alone, which is exactly
  the confound a NAS paper comparing an LLM''s proposals to random search must rule
  out with adequate seeds.'
---

[2304.01910] On the Variance of Neural Network Training with respect to Test Sets and Distributions
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2304.01910
(cs)
[Submitted on 4 Apr 2023 (
v1
), last revised 10 Jun 2024 (this version, v4)]
Title:
On the Variance of Neural Network Training with respect to Test Sets and Distributions
Authors:
Keller Jordan
View a PDF of the paper titled On the Variance of Neural Network Training with respect to Test Sets and Distributions, by Keller Jordan
View PDF
HTML (experimental)
Abstract:
Typical neural network trainings have substantial variance in test-set performance between repeated runs, impeding hyperparameter comparison and training reproducibility. In this work we present the following results towards understanding this variation. (1) Despite having significant variance on their test-sets, we demonstrate that standard CIFAR-10 and ImageNet trainings have little variance in performance on the underlying test-distributions from which their test-sets are sampled. (2) We show that these trainings make approximately independent errors on their test-sets. That is, the event that a trained network makes an error on one particular example does not affect its chances of making errors on other examples, relative to their average rates over repeated runs of training with the same hyperparameters. (3) We prove that the variance of neural network trainings on their test-sets is a downstream consequence of the class-calibration property discovered by Jiang et al. (2021). Our analysis yields a simple formula which accurately predicts variance for the binary classification case. (4) We conduct preliminary studies of data augmentation, learning rate, finetuning instability and distribution-shift through the lens of variance between runs.
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2304.01910
[cs.LG]
(or
arXiv:2304.01910v4
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2304.01910
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Keller Jordan [
view email
]
[v1]
Tue, 4 Apr 2023 16:09:55 UTC (5,855 KB)
[v2]
Wed, 8 May 2024 20:02:56 UTC (6,127 KB)
[v3]
Fri, 10 May 2024 08:47:38 UTC (6,127 KB)
[v4]
Mon, 10 Jun 2024 02:25:33 UTC (6,128 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled On the Variance of Neural Network Training with respect to Test Sets and Distributions, by Keller Jordan
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
2023-04
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