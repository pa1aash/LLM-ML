---
title: '[2210.03230] NAS-Bench-Suite-Zero: Accelerating Research on Zero Cost Proxies'
id: 221003230-nas-bench-suite-zero-accelerating-research-on-zero-cost-proxies
tags:
- llm-nas-feedback-positioning-7125b1
- nas-bench-suite-zero
- zero-cost-proxies
- tabular-nas-benchmark
- nas-methodology
created: '2026-08-16T16:50:56.175783Z'
updated: '2026-08-16T16:53:58.500292Z'
source: https://arxiv.org/abs/2210.03230
source_domain: arxiv.org
fetched_at: '2026-08-16T16:50:56.175496Z'
fetch_provider: builtin
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'NeurIPS 2022 Datasets & Benchmarks track paper (Krishnakumar, White, Zela,
  Tu, Safari, Hutter) that unifies and pre-computes 13 zero-cost (ZC) proxies -- including
  nwot, synflow, snip, grasp, fisher, jacov, grad-norm, epe-nas, zen-score, and baselines
  params/flops/l2-norm/plain -- across 28 tasks spanning NAS-Bench-101 (CIFAR-10),
  NAS-Bench-201 (CIFAR-10/100/ImageNet16-120), NAS-Bench-301, and TransNAS-Bench-101
  Micro/Macro, yielding 1.5M total ZC proxy evaluations released as a public dataset
  (via NASLib). Directly relevant to the RZ-NAS/zero-cost-feedback question in question
  THREE: the paper''s own bias and generalizability analysis finds that ''only a few
  ZC proxies generalize well across most benchmarks and tasks'' -- e.g., snip and
  grasp perform well on NAS-Bench-201 but are outperformed by the naive params/flops
  baselines on other benchmarks -- and that most ZC proxies carry systematic biases
  (e.g., synflow correlates 0.57 with architecture size, meaning it mechanically favors
  larger networks regardless of true quality). The paper''s fix is to ensemble all
  13 proxies into NAS surrogate models, which improves surrogate rank correlation
  by up to 42% and improves BANANAS/NPENAS search performance -- implying that any
  single zero-cost proxy (the kind of feedback signal RZ-NAS uses) is an unreliable,
  biased estimator on its own and reviewers should ask whether a paper''s zero-cost-proxy-based
  feedback signal was validated for generalization to its specific search space or
  benchmark.'
---

[2210.03230] NAS-Bench-Suite-Zero: Accelerating Research on Zero Cost Proxies
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2210.03230
(cs)
[Submitted on 6 Oct 2022]
Title:
NAS-Bench-Suite-Zero: Accelerating Research on Zero Cost Proxies
Authors:
Arjun Krishnakumar
,
Colin White
,
Arber Zela
,
Renbo Tu
,
Mahmoud Safari
,
Frank Hutter
View a PDF of the paper titled NAS-Bench-Suite-Zero: Accelerating Research on Zero Cost Proxies, by Arjun Krishnakumar and 5 other authors
View PDF
HTML (experimental)
Abstract:
Zero-cost proxies (ZC proxies) are a recent architecture performance prediction technique aiming to significantly speed up algorithms for neural architecture search (NAS). Recent work has shown that these techniques show great promise, but certain aspects, such as evaluating and exploiting their complementary strengths, are under-studied. In this work, we create NAS-Bench-Suite: we evaluate 13 ZC proxies across 28 tasks, creating by far the largest dataset (and unified codebase) for ZC proxies, enabling orders-of-magnitude faster experiments on ZC proxies, while avoiding confounding factors stemming from different implementations. To demonstrate the usefulness of NAS-Bench-Suite, we run a large-scale analysis of ZC proxies, including a bias analysis, and the first information-theoretic analysis which concludes that ZC proxies capture substantial complementary information. Motivated by these findings, we present a procedure to improve the performance of ZC proxies by reducing biases such as cell size, and we also show that incorporating all 13 ZC proxies into the surrogate models used by NAS algorithms can improve their predictive performance by up to 42%. Our code and datasets are available at
this https URL
.
Comments:
NeurIPS Datasets and Benchmarks Track 2022
Subjects:
Machine Learning (cs.LG)
; Artificial Intelligence (cs.AI); Machine Learning (stat.ML)
Cite as:
arXiv:2210.03230
[cs.LG]
(or
arXiv:2210.03230v1
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2210.03230
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Colin White [
view email
]
[v1]
Thu, 6 Oct 2022 21:56:26 UTC (1,903 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled NAS-Bench-Suite-Zero: Accelerating Research on Zero Cost Proxies, by Arjun Krishnakumar and 5 other authors
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
2022-10
Change to browse by:
cs
cs.AI
stat
stat.ML
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

---

## Full text (extracted from PDF via pymupdf)

NAS-Bench-Suite-Zero:
Accelerating Research on Zero Cost Proxies
Arjun Krishnakumar∗1, Colin White∗2, Arber Zela∗1, Renbo Tu∗3,
Mahmoud Safari1, Frank Hutter1,4
1University of Freiburg, 2Abacus.AI, 3University of Toronto,
4Bosch Center for Artiﬁcial Intelligence
Abstract
Zero-cost proxies (ZC proxies) are a recent architecture performance prediction
technique aiming to signiﬁcantly speed up algorithms for neural architecture search
(NAS). Recent work has shown that these techniques show great promise, but cer-
tain aspects, such as evaluating and exploiting their complementary strengths, are
under-studied. In this work, we create NAS-Bench-Suite-Zero: we evaluate 13
ZC proxies across 28 tasks, creating by far the largest dataset (and uniﬁed codebase)
for ZC proxies, enabling orders-of-magnitude faster experiments on ZC proxies,
while avoiding confounding factors stemming from different implementations.
To demonstrate the usefulness of NAS-Bench-Suite-Zero, we run a large-scale
analysis of ZC proxies, including a bias analysis, and the ﬁrst information-theoretic
analysis which concludes that ZC proxies capture substantial complementary infor-
mation. Motivated by these ﬁndings, we present a procedure to improve the perfor-
mance of ZC proxies by reducing biases such as cell size, and we also show that
incorporating all 13 ZC proxies into the surrogate models used by NAS algorithms
can improve their predictive performance by up to 42%. Our code and datasets are
available at https://github.com/automl/naslib/tree/zerocost.
1
Introduction
Algorithms for neural architecture search (NAS) seek to automate the design of high-performing
neural architectures for a given dataset. NAS has successfully been used to discover architectures
with better accuracy/latency tradeoffs than the best human-designed architectures [5, 9, 27, 37]. Since
early NAS algorithms were prohibitively expensive to run [57], a long line of recent work has focused
on improving the runtime and efﬁciency of NAS methods (see [9, 48] for recent surveys).
A recent thread of research within NAS focuses on zero-cost proxies (ZC proxies) [1, 22]. These
novel techniques aim to give an estimate of the (relative) performance of neural architectures from
just a single minibatch of data. Often taking just ﬁve seconds to run, these techniques are essentially
“zero cost” compared to training an architecture or to any other method of predicting the performance
of neural architectures [47]. Since the initial ZC proxy was introduced [22], there have been many
follow-up methods [1, 16]. However, several recent works have shown that simple baselines such
as “number of parameters” and “FLOPS” are competitive with all existing ZC proxies across most
settings, and that most ZC proxies do not generalize well across different benchmarks, thus requiring
broader large-scale evaluations in order to assess their strengths [2, 24]. A recent landscape overview
concluded that ZC proxies show great promise, but certain aspects are under-studied and their true
∗Equal contribution. Work done while RT was part-time at Abacus.AI. Email to:
{krishnan, zelaa, fh}@cs.uni-freiburg.de,
colin@abacus.ai,
renbo.tu@mail.utoronto.ca,
safarim@informatik.uni-freiburg.de.
36th Conference on Neural Information Processing Systems (NeurIPS 2022) Track on Datasets and Benchmarks.
arXiv:2210.03230v1  [cs.LG]  6 Oct 2022
NKTEAO
AJ?DI=NGO

AJAN=HEV=PEKJ
QPQ=HJBK
N?DE=OAO
JPACN=PEKJ
T=ILHAO

=?K>KR

AJ?KNA
T=ILHAO
AJ?D¼»¼
N=JOAJ?D¼»¼
AJ?D¾Á»
¼ÀPKP=HAR=HQ=PEKJO
Figure 1: Overview of NAS-Bench-Suite-Zero. We implement and pre-compute 13 ZC prox-
ies on 28 tasks in a uniﬁed framework, and then use this dataset to analyze the generalizability,
complementary information, biases, and NAS integration of ZC proxies.
potential has not been realized thus far [44]. In particular, it is still largely unknown whether ZC
proxies can be effectively combined, and how best to integrate ZC proxies into NAS algorithms.
In this work, we introduce NAS-Bench-Suite-Zero: a uniﬁed and extensible collection of 13
ZC proxies, accessible through a uniﬁed interface, which can be evaluated on a suite of 28 tasks
through NASLib [29] (see Figure 1). In addition to the codebase itself, we release precomputed
ZC proxy scores across all 13 ZC proxies and 28 tasks, which can be used to speed up ZC proxy
experiments. Speciﬁcally, we show that the runtime of ZC proxy experiments such as NAS analyses
and bias analyses are shortened by a factor of at least 103 when using the precomputed ZC proxies in
NAS-Bench-Suite-Zero. By providing a uniﬁed framework with ready-to-use scripts to run large-
scale experiments, NAS-Bench-Suite-Zero eliminates the overhead for researchers to compare
against many other methods and across all popular NAS benchmark search spaces, helping the
community to rapidly increase the speed of research in this promising direction. Our benchmark
suite was very recently used successfully in the Zero Cost NAS Competition at AutoML-Conf 2022.
See Appendix E for more details. In Appendix A, we give detailed documentation, including a
datasheet [10], license, author responsibility, code of conduct, and maintenance plan. We welcome
contributions from the community and hope to grow the repository and benchmark suite as more ZC
proxies and NAS benchmarks are released.
To demonstrate the usefulness of NAS-Bench-Suite-Zero, we run a large-scale analysis of ZC prox-
ies: we give a thorough study of generalizability and biases, and we give the ﬁrst information-theoretic
analysis. Interestingly, based on the bias study, we present a concrete method for improving the
performance of a ZC proxy by reducing biases (such as the tendency to favor larger architectures
or architectures with more conv operations). This may have important consequences for the future
design of ZC proxies. Furthermore, based on the information-theoretic analysis, we ﬁnd that there
is high information gain of the validation accuracy when conditioned on multiple ZC proxies, sug-
gesting that ZC proxies do indeed compute substantial complementary information. Motivated by
these ﬁndings, we incorporate all 13 proxies into the surrogate models used by NAS algorithms
[43, 46], showing that the Spearman rank correlation of the surrogate predictions can increase by up
to 42%. We show that this results in improved performance for two predictor-based NAS algorithms:
BANANAS [46] and NPENAS [43].
Our contributions. We summarize our main contributions below.
• We release NAS-Bench-Suite-Zero, a collection of benchmarks and ZC proxies that uniﬁes
and accelerates research on ZC proxies – a promising new sub-ﬁeld of NAS – by enabling
orders-of-magnitude faster evaluations on a large suite of diverse benchmarks.
• We run a large-scale analysis of 13 ZC proxies across 28 different combinations of search spaces
and tasks by studying the generalizability, bias, and mutual information among ZC proxies.
• Motivated by our analysis, we present a procedure to improve the performance of ZC proxies by
reducing biases, and we show that the complementary information of ZC proxies can signiﬁcantly
improve the predictive power of surrogate models commonly used for NAS.
2
Table 1: List of ZC proxies in NAS-Bench-Suite-Zero. Note that “neuron-wise” denotes whether
the total score is a sum of individual weights.
Name
Data-dependent
Neuron-wise
Type
In NAS-Bench-Suite-Zero
epe-nas [20]


Jacobian

fisher [41]


Pruning-at-init

flops [24]


Baseline

grad-norm [1]


Pruning-at-init

grasp [42]


Pruning-at-init

l2-norm [1]


Baseline

jacov [22]


Jacobian

nwot [22]


Jacobian

params [24]


Baseline

plain [1]


Baseline

snip [14]


Pruning-at-init

synflow [38]


Pruning-at-init

zen-score [16]


Piece. Lin.

2
Background and Related Work
Given a dataset and a search space – a large set of neural architectures – NAS seeks to ﬁnd the
architecture with the highest validation accuracy (or the best application-speciﬁc trade-off among
accuracy, latency, size, and so on) on the dataset. NAS has been studied since the late 1980s [23, 39]
and has seen a resurgence in the last few years [17, 57], with over 1000 papers on NAS in the last
two years alone. For a survey of the different techniques used for NAS, see [9, 48].
Many NAS methods make use of performance prediction. A performance prediction method is
any function which predicts the (relative) performance of architectures, without fully training the
architectures [47]. BRP-NAS [8], BONAS [33], and BANANAS [46] are all examples of NAS
methods that make use of performance prediction. While performance prediction speeds up NAS
algorithms by avoiding fully training neural networks, many still require non-trivial computation time.
On the other hand, a recently-proposed line of techniques, zero-cost proxies (ZC proxies) require just
a single forward pass through the network, often taking just ﬁve seconds [22].
Zero-cost proxies.
The original ZC proxy estimated the separability of the minibatch of data into
different linear regions of the output space [22]. Many other ZC proxies have been proposed since
then, including data-independent ZC proxies [1, 15, 16, 38], ZC proxies inspired by pruning-at-
initialization techniques [1, 14, 38, 42], and ZC proxies inspired by neural tangent kernels [4, 34].
See Table 1 for a full list of the ZC proxies we use in this paper. We describe theoretical ZC proxy
results in Appendix B.1.
Search spaces and tasks.
In our experiments, we make use of several different NAS benchmark
search spaces and tasks. NAS-Bench-101 [53] is a popular cell-based search space for NAS research.
It consists of 423 624 architectures trained on CIFAR-10. The cell-based search space is designed
to model ResNet-like and Inception-like cells [12, 36]. NAS-Bench-201 [6] is a cell-based search
space consisting of 15 625 architectures (6 466 non-isomorphic) trained on CIFAR-10, CIFAR-100,
and ImageNet16-120. NAS-Bench-301 [55] is a surrogate NAS benchmark for the DARTS search
space [18]. The search space consists of normal cell and reduction cells, with 1018 total architectures.
TransNAS-Bench-101 [7] is a NAS benchmark consisting of two different search spaces: a “micro”
(cell-based) search space of size 4 096, and a macro search space of size 3 256. The architectures are
trained on seven different tasks from the Taskonomy dataset [54]. NAS-Bench-Suite [21] collects
these search spaces and tasks within the uniﬁed framework of NASLib [29]. In this work, we extend
this collection by adding two datasets from NAS-Bench-360 [40], SVHN, and four datasets from
Taskonomy. NAS-Bench-360 is a collection of diverse tasks that are ready-to-use for NAS research.
Large-scale studies of ZC proxies.
A few recent works [2, 24, 44, 47] investigated the perfor-
mance of ZC proxies in ranking architectures over different NAS benchmarks, showing that the
relative performance highly depends on the search space, but none study more than 12 total tasks, and
none make the ZC proxy values publicly available. Two predictor-based NAS methods have recently
been introduced: OMNI [47] and ProxyBO [32]. However, OMNI only uses a single ZC proxy, and
3
Table 2: Overview of ZC proxy evaluations in NAS-Bench-Suite-Zero. ∗Note that EPE-NAS is
only deﬁned for classiﬁcation tasks [20].
Search space
Tasks
Num. ZC proxies
Num. architectures
Total ZC proxy evaluations
NAS-Bench-101
1
13
10 000
130 000
NAS-Bench-201
3
13
15 625
609 375
NAS-Bench-301
1
13
11 221
145 873
TransNAS-Bench-101-Micro
7
12∗
3 256
273 504
TransNAS-Bench-101-Macro
7
12∗
4 096
344 064
Add’l. 201, 301, TNB-Micro
9
13
600
23400
Total
28
13
44 798
1 526 216
while ProxyBO uses three, the algorithm dynamically chooses one in each iteration (so individual
predictions are made using a single ZC proxy at a time). Recently, NAS-Bench-Zero was introduced
[2], a new benchmark based on popular computer vision models ResNet [12] and MobileNetV2
[30], which includes 10 ZC proxies. However, the NAS-Bench-Zero dataset is currently not publicly
available. For more related work details, see Appendix B.
Only two prior works combine the information of multiple ZC proxies together in architecture
predictions [1, 2] and both only use the voting strategy to combine at most four ZC proxies. Our
work is the ﬁrst to publicly release ZC proxy values, combine ZC proxies in a nontrivial way, and
exploit the complementary information of 13 ZC proxies simultaneously.
3
Overview of NAS-Bench-Suite-Zero
In this section, we give an overview of the NAS-Bench-Suite-Zero codebase and dataset, which
allows researchers to quickly develop ZC proxies, compare against existing ZC proxies across diverse
datasets, and integrate them into NAS algorithms, as shown in Sections 4 and 5.
We implement all ZC proxies from Table 1 in the same codebase (NASLib [29]). For all ZC proxies,
we use the default implementation from the original work. While this list covers 13 ZC proxies,
the majority of ZC proxies released to date, we did not yet include a few other ZC proxies, for
example, due to requiring a trained supernetwork to make evaluations [4, 34] (therefore needing to
implement a supernetwork on 28 benchmarks), implementation in TensorFlow rather than PyTorch
[25], or unreleased code. Our modular framework easily allows additional ZC proxies to be added to
NAS-Bench-Suite-Zero in the future.
To build NAS-Bench-Suite-Zero, we extend the collection of NASLib’s publicly available bench-
marks, known as NAS-Bench-Suite [21]. This allows us to evaluate and fairly compare all ZC
proxies in the same framework without confounding factors stemming from different implemen-
tations, software versions or training pipelines. Speciﬁcally, for the search spaces and tasks, we
use NAS-Bench-101 (CIFAR-10), NAS-Bench-201 (CIFAR-10, CIFAR-100, and ImageNet16-120),
NAS-Bench-301 (CIFAR-10), and TransNAS-Bench-101 Micro and Macro (Jigsaw, Object Classiﬁ-
cation, Scene Classiﬁcation, Autoencoder) from NAS-Bench-Suite. We add the remaining tasks from
TransNAS-Bench-101 (Room Layout, Surface Normal, Semantic Segmentation), and three tasks each
for NAS-Bench-201, NAS-Bench-301, and TransNAS-Bench-101-Micro: Spherical-CIFAR-100,
NinaPro, and SVHN. This yields a total of 28 benchmarks in our analysis. For all NAS-Bench-201
and TransNAS-Bench-101 tasks, we evaluate all ZC proxy values and the respective runtimes, for
all architectures. For NAS-Bench-301, we evaluate on all 11 221 randomly sampled architectures
from the NAS-Bench-301 dataset, due to the computational infeasibility of exhaustively evaluating
the full set of 1018 architectures. Similarly, we evaluate 10 000 architectures from NAS-Bench-101.
Finally, for Spherical-CIFAR-100, NinaPro, and SVHN, we evaluate 200 architectures per search
space, since only 200 architectures are fully trained for each of these tasks. See Table 2.
We run all ZC proxies from Table 1 on Intel Xeon Gold 6242 CPUs and save their evaluations in
order to create a queryable table with these pre-computed values. We use a batch size of 64 for all ZC
proxy evaluations, except for the case of TransNAS-Bench-101: due to the extreme memory usage of
the Taskonomy tasks (> 30GB memory), we used a batch size of 32. The total computation time for
all 1.5M evaluations was 1100 CPU hours.
4
TNB101_MICRO-AUTOENC
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MACRO-JIGSAW
NB101-CF10
TNB101_MACRO-AUTOENC
TNB101_MACRO-SCENE
NB301-CF10
TNB101_MACRO-SEGMENT
TNB101_MICRO-ROOM
TNB101_MACRO-NORMAL
TNB101_MICRO-JIGSAW
TNB101_MICRO-NORMAL
TNB101_MICRO-OBJECT
TNB101_MICRO-SEGMENT
NB201-IMGNT
TNB101_MICRO-SCENE
NB201-CF10
NB201-CF100
plain
grasp
fisher
epe_nas
grad_norm
snip
synflow
l2_norm
params
zen
jacov
flops
nwot
0.07
-0.19
-0.18
-0.30
-0.32
-0.10
-0.19
-0.32
0.00
0.36
-0.04
0.35
0.03
0.34
-0.02
-0.22
0.24
-0.26
-0.21
-0.12
-0.64
-0.10
-0.26
0.27
-0.02
-0.43
0.34
-0.02
-0.29
-0.05
-0.12
0.01
-0.22
0.00
0.55
-0.27
0.51
0.54
-0.58
-0.30
-0.21
-0.26
-0.28
-0.19
-0.13
-0.28
0.03
0.30
0.15
0.30
0.16
0.44
0.12
0.48
0.66
0.50
0.54
0.00
-0.02
-0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.40
0.00
0.16
0.00
0.39
0.00
0.33
0.51
0.70
0.60
-0.32
-0.56
-0.26
-0.27
-0.25
0.31
-0.33
-0.04
0.21
0.25
0.35
0.36
0.36
0.39
0.60
0.57
0.65
0.58
0.63
-0.27
-0.38
-0.19
-0.19
-0.19
0.20
-0.14
-0.05
0.27
0.32
0.45
0.41
0.49
0.45
0.68
0.57
0.70
0.58
0.63
0.00
0.12
-0.01
0.34
0.31
0.00
0.27
0.18
0.00
0.30
0.00
0.47
0.00
0.48
0.00
0.75
0.72
0.73
0.76
0.04
0.08
-0.03
0.15
0.50
-0.20
0.28
0.45
0.18
0.18
0.30
0.35
0.50
0.32
0.48
0.69
0.53
0.68
0.72
-0.01
0.16
-0.00
0.15
0.37
-0.18
0.32
0.46
0.06
0.30
0.30
0.44
0.62
0.45
0.68
0.69
0.64
0.72
0.73
0.14
0.10
-0.04
0.24
0.59
-0.01
0.27
0.43
0.27
0.38
0.38
0.51
0.71
0.54
0.67
0.39
0.72
0.35
0.35
0.18
0.07
0.08
0.19
-0.29
0.45
0.19
-0.04
0.57
0.40
0.50
0.56
0.75
0.51
0.80
0.71
0.75
0.75
0.71
-0.02
0.79
0.48
0.64
0.36
0.76
0.85
0.42
0.60
0.30
0.76
0.45
0.64
0.46
0.69
0.67
0.65
0.69
0.71
0.03
0.83
0.63
0.76
0.31
0.67
0.89
0.47
0.80
0.25
0.78
0.42
0.57
0.39
0.53
0.77
0.60
0.77
0.80
Spearman rank correlations between ZC proxy values and validation accuracies
Figure 2: Spearman rank correlation coefﬁcient between ZC proxy values and validation accuracies,
for each ZC proxy and benchmark. The rows and columns are ordered based on the mean scores
across columns and rows, respectively.
Speedups and recommended usage.
The average time to compute a ZC proxy across all tasks is
2.6 seconds, and the maximum time (computing grasp on TNB-Macro Autoencoder) is 205 seconds,
compared to 10−5 seconds when instead querying the NAS-Bench-Suite-ZeroAPI.
When researchers evaluate ZC proxy-based NAS algorithms using queryable NAS benchmarks, the
bottleneck is often (ironically) the ZC proxy evaluations. For example, for OMNI [47] or ProxyBO
[32] running for 100 iterations and 100 candidates per iteration, the total evaluation time is roughly 9
hours, yet they can be run on NAS-Bench-Suite-Zero in under one minute. Across all experiments
done in this paper (mutual information study, bias study, NAS study, etc.), we calculate that using
NAS-Bench-Suite-Zero decreases the computation time by at least three orders of magnitude. See
Appendix C.4 for more details.
Since NAS-Bench-Suite-Zero reduces the runtime of experiments by at least three orders
of magnitude (on queryable NAS benchmarks), we recommend researchers take advantage of
NAS-Bench-Suite-Zero to (i) run hundreds of trials of ZC proxy-based NAS algorithms, to reach
statistically signiﬁcant conclusions, (ii) run extensive ablation studies, including the type and usage
of ZC proxies, and (iii) increase the total number of ZC proxies evaluated in the NAS algorithm.
Finally, when using NAS-Bench-Suite-Zero, researchers should report the real-world time NAS
algorithms would take, by adding the time to run each ZC proxy evaluation (which can be queried in
NAS-Bench-Suite-Zero) to the total runtime of the NAS algorithm.
4
Generalizability, Mutual Information, and Bias of ZC Proxies
In this section, we use NAS-Bench-Suite-Zero to study concrete research questions relating to the
generalizability, complementary information, and bias of ZC proxies.
4.1
RQ 1: How well do ZC proxies generalize across different benchmarks?
In Figure 2, for each ZC proxy and each benchmark, we compute the Spearman rank correlation
between the ZC proxy values and the validation accuracies over a set of 1000 randomly drawn
architectures (see Appendix C for the full results on all benchmarks). Out of all the ZC proxies, nwot
and flops have the highest rank correlations across all benchmarks. On some of the benchmarks,
such as TransNAS-Bench-101-Micro Autoencoder and Room Layout, all of the ZC proxies exhibit
poor performance on average, while on the widely used NAS-Bench-201 benchmarks, almost all of
them perform well. Several methods, such as snip and grasp, perform well on the NAS-Bench-201
tasks, but on average are outperformed by params and flops on the other benchmarks.
Although no ZC proxy performs consistently across all benchmarks, we may ask a related question:
is the performance of all ZC proxies across benchmarks correlated enough to capture similarities
among benchmarks? In other words, can we use ZC proxies as a tool to assess the similarities among
tasks. This is particularly important in meta-learning or transfer learning, where a meta-algorithm
aims to learn and transfer knowledge across a set of similar tasks. To answer this question, we
5
compute the Pearson correlation of the ZC proxy scores on each pair of benchmarks. See Figure 3.
As expected, benchmarks that are based on the same or similar search spaces are highly correlated
with respect to the ZC proxy scores. For example, we see clusters of high correlation for the
Trans-NAS-Bench-101-Macro benchmarks, and the NAS-Bench-201 benchmarks.
Answer to RQ 1: Only a few ZC proxies generalize well across most benchmarks and tasks. However,
ZC proxies can be used to assess similarities across benchmarks. This suggests the potential future
direction of incorporating them as task features in a meta-learning setting [19].
4.2
RQ 2: Are ZC proxies complementary with respect to explaining validation accuracy?
NB101-CF10
NB201-CF10
NB201-CF100
NB201-IMGNT
NB301-CF10
TNB101_MICRO-JIGSAW
TNB101_MICRO-SCENE
TNB101_MICRO-OBJECT
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
TNB101_MICRO-NORMAL
TNB101_MICRO-SEGMENT
TNB101_MACRO-JIGSAW
TNB101_MACRO-SCENE
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MACRO-AUTOENC
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
NB101-CF10
NB201-CF10
NB201-CF100
NB201-IMGNT
NB301-CF10
TNB101_MICRO-JIGSAW
TNB101_MICRO-SCENE
TNB101_MICRO-OBJECT
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
TNB101_MICRO-NORMAL
TNB101_MICRO-SEGMENT
TNB101_MACRO-JIGSAW
TNB101_MACRO-SCENE
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MACRO-AUTOENC
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
1.00
0.32
0.33
0.41
0.93
0.03 -0.03 -0.08 -0.24 0.45
0.29
0.16
0.61
0.57
0.50
0.45 -0.03 0.20
0.12
0.32
1.00
0.99
0.92
0.49
0.11
0.38
0.14 -0.05 -0.02 0.34
0.38
0.51
0.44
0.35
0.42
0.35
0.42
0.37
0.33
0.99
1.00
0.96
0.51
0.13
0.37
0.12 -0.10 -0.09 0.35
0.40
0.51
0.44
0.34
0.41
0.36
0.46
0.38
0.41
0.92
0.96
1.00
0.58
0.21
0.36
0.10 -0.17 -0.03 0.46
0.48
0.55
0.47
0.35
0.43
0.38
0.52
0.45
0.93
0.49
0.51
0.58
1.00
0.04 -0.03 -0.13 -0.31 0.45
0.47
0.38
0.68
0.62
0.55
0.59
0.20
0.42
0.35
0.03
0.11
0.13
0.21
0.04
1.00
0.87
0.90
0.79
0.30
0.66
0.64
0.49
0.55
0.52
0.26
0.32
0.56
0.50
-0.03 0.38
0.37
0.36 -0.03 0.87
1.00
0.95
0.82 -0.00 0.55
0.57
0.40
0.46
0.42
0.17
0.26
0.51
0.39
-0.08 0.14
0.12
0.10 -0.13 0.90
0.95
1.00
0.94
0.12
0.48
0.47
0.37
0.46
0.45
0.15
0.19
0.42
0.32
-0.24 -0.05 -0.10 -0.17 -0.31 0.79
0.82
0.94
1.00
0.18
0.32
0.30
0.23
0.33
0.37
0.07
0.12
0.26
0.22
0.45 -0.02 -0.09 -0.03 0.45
0.30 -0.00 0.12
0.18
1.00
0.33
0.19
0.52
0.46
0.50
0.44
0.18
0.15
0.30
0.29
0.34
0.35
0.46
0.47
0.66
0.55
0.48
0.32
0.33
1.00
0.96
0.51
0.57
0.49
0.43
0.46
0.84
0.73
0.16
0.38
0.40
0.48
0.38
0.64
0.57
0.47
0.30
0.19
0.96
1.00
0.39
0.43
0.35
0.31
0.50
0.83
0.69
0.61
0.51
0.51
0.55
0.68
0.49
0.40
0.37
0.23
0.52
0.51
0.39
1.00
0.97
0.95
0.92
0.61
0.68
0.72
0.57
0.44
0.44
0.47
0.62
0.55
0.46
0.46
0.33
0.46
0.57
0.43
0.97
1.00
0.99
0.90
0.56
0.72
0.72
0.50
0.35
0.34
0.35
0.55
0.52
0.42
0.45
0.37
0.50
0.49
0.35
0.95
0.99
1.00
0.92
0.56
0.67
0.69
0.45
0.42
0.41
0.43
0.59
0.26
0.17
0.15
0.07
0.44
0.43
0.31
0.92
0.90
0.92
1.00
0.73
0.71
0.79
-0.03 0.35
0.36
0.38
0.20
0.32
0.26
0.19
0.12
0.18
0.46
0.50
0.61
0.56
0.56
0.73
1.00
0.80
0.89
0.20
0.42
0.46
0.52
0.42
0.56
0.51
0.42
0.26
0.15
0.84
0.83
0.68
0.72
0.67
0.71
0.80
1.00
0.93
0.12
0.37
0.38
0.45
0.35
0.50
0.39
0.32
0.22
0.30
0.73
0.69
0.72
0.72
0.69
0.79
0.89
0.93
1.00
Correlation between benchmarks based on ZC proxy values
Figure 3: Pearson correlation coefﬁcient between ZC proxy scores on
pairs of benchmarks. The entries in the plot are ordered based on the
mean score across each row and column.
While Figure 2 shows the
performance of each indi-
vidual ZC proxy, now we
consider the combined per-
formance of multiple ZC
proxies. If ZC proxies mea-
sure different characteris-
tics of architectures, then a
NAS algorithm can exploit
their complementary infor-
mation in order to yield
improved results.
While
prior work [24, 44] com-
putes the correlation among
pairs of ZC proxies, our
true goal is to assess the
complementary information
of ZC proxies with respect
to explaining the ground-
truth validation accuracy
(But for completeness, we
re-run that experiment and
include the results in Ap-
pendix C). Furthermore, we
wish to measure the com-
plementary information of
more than just two ZC prox-
ies at a time.
For this,
we turn to information the-
oretic measures: by treating
the validation accuracy and ZC proxy values as random variables, we can measure the entropy of the
validation accuracy conditioned on one or more ZC proxies, which intuitively tells us the information
that one or more ZC proxies reveal about the validation accuracy.
Formally, given a search space S, let Y denote the uniform distribution of validation accuracies over
the search space, and let y denote a random sample from Y. Similarly, for a ZC proxy i from 1 to 13,
let Zi denote the uniform distribution of the ZC proxy values, and let zi denote a random sample
from Zi. Let H(·) denote the entropy function. For all pairs zi, zj of ZC proxies, we compute the
conditional entropy H(y | zi, zj), as well as the information gain H(y | zi) −H(y | zi, zj). See
Figure 4. The entropy computations are based on 1000 randomly sampled architectures, using 24-bin
histograms for density smoothing (see Appendix C for more details). We see that synflow and
plain together give the most information about the ground truth validation accuracies, due to their
substantial complementary information.
Now we can ask the same question for k tuples of ZC proxies. Given an ordered list of k ZC proxies
zi1, zi2, . . . zik, we deﬁne the information gain of zik conditioned on y as follows:
IG(zik) := H(y | zi1, . . . , zik−1) −H(y | zi1, . . . , zik).
(1)
Intuitively, IG computes the marginal information we learn about y when zik is revealed, assuming
we already knew the values of zi1, . . . , zik−1. We compare the conditional entropy vs. number of
6
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
3.42
1.98
2.10
1.90
1.84
1.85
1.87
1.86
2.21
2.21
2.52
2.55
2.83
1.98
3.40
2.17
2.05
2.10
2.08
2.08
2.09
2.36
2.38
2.55
2.58
2.87
2.10
2.17
3.37
2.14
2.12
2.11
2.14
2.15
2.33
2.32
2.64
2.65
2.92
1.90
2.05
2.14
3.24
2.51
2.55
2.67
2.63
2.16
2.17
2.40
2.48
2.74
1.84
2.10
2.12
2.51
3.25
2.92
2.82
2.88
2.16
2.17
2.39
2.46
2.73
1.85
2.08
2.11
2.55
2.92
3.26
2.82
2.85
2.15
2.16
2.39
2.48
2.74
1.87
2.08
2.14
2.67
2.82
2.82
3.25
2.94
2.17
2.18
2.40
2.48
2.74
1.86
2.09
2.15
2.63
2.88
2.85
2.94
3.24
2.16
2.16
2.40
2.47
2.74
2.21
2.36
2.33
2.16
2.16
2.15
2.17
2.16
3.46
3.03
2.85
2.73
2.97
2.21
2.38
2.32
2.17
2.17
2.16
2.18
2.16
3.03
3.46
2.86
2.73
2.97
2.52
2.55
2.64
2.40
2.39
2.39
2.40
2.40
2.85
2.86
3.44
2.93
3.07
2.55
2.58
2.65
2.48
2.46
2.48
2.48
2.47
2.73
2.73
2.93
3.43
3.10
2.83
2.87
2.92
2.74
2.73
2.74
2.74
2.74
2.97
2.97
3.07
3.10
3.57
Pairwise conditional entropy on NB301-CF10
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
-0.00
1.44
1.31
1.52
1.57
1.56
1.54
1.55
1.20
1.20
0.90
0.87
0.59
1.42
-0.00
1.23
1.35
1.30
1.31
1.31
1.31
1.04
1.02
0.84
0.82
0.53
1.26
1.20
-0.00
1.23
1.25
1.25
1.23
1.22
1.04
1.04
0.72
0.71
0.45
1.34
1.19
1.10
0.00
0.73
0.69
0.57
0.61
1.08
1.07
0.83
0.76
0.50
1.40
1.15
1.13
0.74
-0.00
0.33
0.43
0.37
1.08
1.08
0.85
0.79
0.52
1.41
1.18
1.14
0.71
0.34
-0.00
0.44
0.41
1.11
1.10
0.87
0.78
0.52
1.38
1.17
1.11
0.59
0.43
0.43
-0.00
0.31
1.09
1.07
0.85
0.77
0.51
1.38
1.15
1.10
0.61
0.36
0.40
0.30
-0.00
1.09
1.08
0.84
0.78
0.50
1.25
1.10
1.13
1.30
1.29
1.31
1.29
1.30
-0.00
0.43
0.60
0.73
0.48
1.24
1.08
1.13
1.29
1.29
1.30
1.27
1.29
0.43
-0.00
0.60
0.72
0.48
0.93
0.89
0.80
1.04
1.05
1.05
1.04
1.04
0.59
0.59
0.00
0.51
0.37
0.88
0.85
0.78
0.96
0.97
0.96
0.95
0.97
0.70
0.70
0.50
-0.00
0.33
0.75
0.70
0.66
0.84
0.85
0.83
0.83
0.83
0.60
0.60
0.50
0.47
0.00
Information gain on NB301-CF10
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Conditional entropy
NB301-CF10
random ordering
greedy ordering
minimum k-tuple
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
NB201-CF100
random ordering
greedy ordering
minimum k-tuple
1
2
3
4
5
6
7
8
9
10
11
12
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Conditional entropy
TNB101_MACRO-autoencoder
random ordering
greedy ordering
minimum k-tuple
Figure 4: Given a ZC proxy pair (i, j), we compute the conditional entropy H(y | zi, zj) (top left),
and information gain H(y | zi) −H(y | zi, zj) (top right). Conditional entropy H(y | zi1, . . . , zik)
vs. k, where the ordering zi1, . . . , zik is selected using three different strategies. The minimum
k-tuple and greedy ordering signiﬁcantly overlap in the ﬁrst two ﬁgures (bottom).
ZC proxies for three different orderings of the ZC proxies. The ﬁrst is a random ordering (averaged
over 100 random trials), which tells us the average information gain when iteratively adding more
ZC proxies. The second is a greedy ordering, computed by iteratively selecting the ZC proxy that
maximizes IG(zik), for k from 1 to 13. The ﬁnal plot exhaustively searches through
 13
k

sets to ﬁnd
the k proxies which minimize H(y | zi1, . . . zik), for k from 1 to 13 (note that this may not deﬁne a
valid ordering). See Figure 4, and Appendix C for the complete results. We see that there is very
substantial information gain when iteratively adding ZC proxies, even if the ZC proxies are randomly
chosen. Optimizing the order of adding ZC proxies yields much higher IG in certain benchmarks
(e.g., NB201-CF100), and a greedy approach is shown to be not far from the optimum.
Answer to RQ 2: In some benchmarks, we see substantial complementary information among ZC
proxies. However, the degree of complementary information depends heavily on the NAS benchmark
at hand. This suggests that we cannot always expect ZC proxies to yield complementary information,
but a machine learning model might be able to identify useful combinations of ZC proxies.
4.3
RQ 3: Do ZC proxies contain biases, such as a bias toward certain operations or sizes,
and can we mitigate these biases?
Identifying biases in ZC proxies can help explain weaknesses and facilitate the development of
higher-performing ZC proxies. We deﬁne bias metrics and study ZC proxy scores for thousands
of architectures for their correlation with biases. This systematic approach yields generalizable
conclusions and avoids the noise from assessing singular architectures. We consider the following
biases: conv:pool (the numerical advantage of convolution to pooling operations in the cell), cell
size (the number of non-zero operations in the cell), num. skip connections, and num. parameters.
For each search space, ZC proxy, and bias, we compute the Pearson correlation coefﬁcient between
the ZC proxy values and the bias values. We consider all 44K architectures referenced in Table 2.
See Table 3 and Appendix C for the full results. We ﬁnd that many ZC proxies exhibit biases to
7
Table 3: Pearson correlation coefﬁcients between predictors and bias metrics (in bold) on different
datasets. For example, for Cell size on NB201-CF100, snip has a correlation of -0.04 (indicating
very little bias), while synflow has a correlation of 0.57 (meaning it favors larger architectures).
Name
Conv:pool
Cell size
Num. skip connections
Num. parameters
NB201-CF10
NB301-CF10
NB201-CF100
NB201-IM
NB301-CF10
NB201-CF100
NB101-CF10
NB301-CF10
epe-nas
0.05
-0.02
0.35
0.35
0.01
0.09
-0.02
-0.01
fisher
0.05
0.01
-0.03
-0.05
-0.15
-0.03
0.11
0.17
flops
0.59
0.70
0.30
0.30
-0.35
-0.30
1.00
0.99
grad-norm
0.35
0.27
-0.04
-0.05
-0.26
-0.26
0.30
0.51
grasp
0.01
0.28
-0.01
0.01
0.03
0.00
-0.03
0.24
l2-norm
0.87
0.76
0.41
0.41
-0.33
-0.41
0.62
0.99
jacov
0.05
-0.11
0.35
0.35
0.08
0.09
-0.18
-0.10
nwot
0.06
0.78
0.28
0.28
-0.21
0.06
0.74
0.95
params
0.61
0.78
0.29
0.29
-0.32
-0.29
1.00
1.00
plain
-0.33
-0.45
0.14
0.14
0.02
0.02
0.03
-0.45
snip
0.37
0.27
-0.04
-0.04
-0.28
-0.28
0.44
0.50
synflow
0.53
0.41
0.57
0.58
-0.20
-0.14
0.57
0.62
zen-score
0.05
0.75
0.35
0.35
-0.33
0.09
0.68
0.99
val-acc
0.36
0.45
0.35
0.43
0.13
-0.06
0.09
0.47
various degrees. Interestingly, some biases are consistent across search spaces, while others are not.
For example, l2-norm has a conv:pool bias on both NB201-C10 and NB301-C10, while nwot has a
strong conv:pool bias on NB301-C10 and almost no bias on NB201-C10. While validation accuracy
does not correlate with number of skip connections, most ZC proxies in the benchmark exhibit a
negative bias towards this metric.
Next, we present a procedure for removing these biases. For this study, we use ZC proxies that had
large biases in Table 3, and we attempt to answer the following questions: (1) can we remove these
biases, and (2) if we can remove the biases, does the performance of ZC proxies improve?
Given a search space of architectures A, let f : A →R denote a ZC proxy (a function that takes as
input an architecture, and outputs a real number). Furthermore, let b : A →R denote a bias measure
such as “cell size”. Recall that Table 3 showed that the correlation between a ZC proxy f and a bias
measure b may be high. For example, the correlation between synflow and “cell size” is high, which
means using synflow would favor larger architectures. To reduce bias, we use a simple heuristic:
f ′(a) = f(a) ·
1
b(a) + C .
(2)
In this expression, C is a constant that we can tune. In deciding on a strategy to tune C, we make two
observations. First, for most bias measures, the bias of val_acc is not zero, which means completely
de-biasing ZC proxies could hurt performance. Second, depending on the application, we may want
to fully remove the bias of a ZC proxy, or else remove bias only insofar as it improves performance.
Therefore, we test three different strategies to tune C by brute force: (1) “minimize”, to minimize
bias, (2) “equalize”, to match the bias with the bias of val_acc, and (3) “performance”, to optimize
the performance (Pearson correlation). See Table 4 for the results.
We ﬁnd that using the “performance” strategy, we are able to increase the performance of ZC proxies
by reducing their bias. Furthermore, the “equalize” strategy sometimes provide good results on par
with the “performance” strategy. This suggests a good bias mitigation strategy when we do not know
the ground truth but have information on how the ground truth correlations with bias. This may have
important consequences for the future design of ZC proxies.
Answer to RQ 3: Many ZC proxies do exhibit different types of biases to various degrees, but the
biases can be mitigated, thereby improving performance.
5
Integration into NAS
The ﬁndings in Section 4.2 showed that ZC proxies contain substantial complementary information,
conditioned on the ground-truth validation accuracies. However, no prior work has combined more
than four ZC proxies, or used a combination strategy other than a simple vote. In this section, we
combine and integrate all 13 ZC proxies into predictor-based NAS algorithms by adding the ZC
proxies directly as features into the surrogate (predictor) models.
8
Table 4: Bias mitigation strategies tested on the ZC proxies with the most biases. We test three
different strategies by tuning C from Equation 2 for different objectives: minimize (tune C to mini-
mize bias), equalize (tune C to match ground truth’s correlation with bias metric), and performance
(tune C to maximize correlation with ground truth). Bias and performance are Pearson correlation
coefﬁcients of the proxy score with the bias metric and with the ground truth accuracy, respectively.
C is searched between -10 and 1000.
ZC proxy
dataset
bias
metric
original
bias
original
perf.
new
bias
new
perf.
strategy
l2-norm
NB201-CF10
conv:pool
0.87
0.42
0.00
0.10
minimize
0.37
0.11
equalize
0.70
0.44
performance
nwot
NB301-CF10
conv:pool
0.78
0.49
0.00
0.03
minimize
0.29
0.14
equalize
0.78
0.49
performance
synﬂow
NB201-CF100
cell size
0.57
0.68
0.01
0.64
minimize
0.35
0.71
equalize
0.35
0.71
performance
synﬂow
NB201-IM
cell size
0.58
0.76
0.01
0.62
minimize
0.43
0.76
equalize
0.46
0.76
performance
ﬂops
NB301-CF10
num. skip
-0.35
0.43
-0.01
0.06
minimize
0.12
-0.05
equalize
-0.35
0.43
performance
We run experiments on two common predictor-based NAS algorithms: BANANAS, based on Bayesian
optimization [46], and NPENAS, based on evolution [43]. Both algorithms use a model-based
performance predictor: a model that takes in an architecture encoding as features (e.g., the adjacency
matrix encoding [45]), and outputs a prediction of that architecture’s validation accuracy. The model
is retrained throughout the search algorithm, as more and more architectures are fully trained. Recent
work has shown that boosted trees such as XGBoost achieve strong performance in NAS [47, 55].
Experimental setup.
For both algorithms, we use the NASLib implementation [29] and default
parameters reported in prior work [47]. First, we assess the standalone performance of XGBoost
when ZC proxies are added as features in addition to the architecture encoding, by randomly
sampling 100 training architectures and 1000 disjoint test architectures, and computing the Spearman
rank correlation coefﬁcient between the set of predicted validation accuracies and the ground-truth
accuracies. On NAS-Bench-201 CIFAR-100, averaged over 100 trials, the Spearman rank correlation
(± std. dev.) improves from 0.640 ± 0.0420 to 0.908 ± 0.012 with the addition of ZC proxies,
representing an improvement of 41.7%. Even more surprisingly, using the ZC proxies alone as
features without the architecture, results in a Spearman rank correlation of 0.907 ± 0.013, implying
that the ZC proxies subsume nearly all information contained in the architecture encoding itself.
We present the full results in Appendix D. These results show that an ensemble of ZC proxies can
substantially increase the performance of model-based predictors.
Similar to the previous experiment, we run both NAS algorithms three different ways: using only the
encoding, only the ZC proxies, and both, as features of the predictor. Each algorithm is given 200
architecture evaluations, and we plot performance over time, averaged over 400 trials. See Figure 5
for the results of BANANAS, and Appendix D for the full results. We ﬁnd that the ZC proxies give
the NAS algorithms a boost in performance, especially in the early stages of the search.
6
Conclusions, Limitations, and Broader Impact
In this work, we created NAS-Bench-Suite-Zero: an extensible collection of 13 ZC proxies
(covering the majority that currently exist), accessible through a uniﬁed interface, which can be
evaluated on a suite of 28 NAS benchmark tasks. In addition to the codebase, we release precomputed
ZC proxy scores across all 13 ZC proxies and 28 tasks, giving 1.5 million total ZC proxy evaluations.
This dataset can be used to speed up ZC proxy-based NAS experiments, e.g., from 9 hours to 4
9
105
Time (s)
70.0
70.5
71.0
71.5
72.0
72.5
73.0
Accuracy (%)
NB201 CF100
Encoding
ZCPs
Encoding + ZCPs
106
Time (s)
44.0
44.5
45.0
45.5
46.0
46.5
47.0
Accuracy (%)
NB201 IMGNT
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
93.9
94.0
94.1
94.2
94.3
94.4
Accuracy (%)
NB301 CF10
Encoding
ZCPs
Encoding + ZCPs
Figure 5: Performance of BANANAS with and without ZC proxies as additional features in the
surrogate model. Each curve shows the mean and standard error across 400 trials.
minutes (see Section 3). Overall, NAS-Bench-Suite-Zero eliminates the overhead in ZC proxy
research, with respect to comparing against different methods and across a diverse set of tasks.
To motivate the usefulness of NAS-Bench-Suite-Zero, we conducted a large-scale analysis of
the generalizability, bias, and the ﬁrst information-theoretic analysis of ZC proxies. Our empirical
analysis showed substantial complementary information of ZC proxies conditioned on validation
accuracy, motivating us to ensemble all 13 into predictor-based NAS algorithms. We show that using
several ZC proxies together signiﬁcantly improves the performance of the surrogate models used in
NAS, as well as improving the NAS algorithms themselves.
Limitations and future work.
Although our work makes substantial progress towards motivating
and increasing the speed of ZC proxy research, there are still some limitations of our analysis. First,
our work is limited to empirical analysis. However, we discuss existing theoretical results in Appendix
B.1. Furthermore, there are some benchmarks on which we did not give a comprehensive evaluation.
For example, on NAS-Bench-301, we only computed ZC proxies on 11 000 architectures, since the
full space of 1018 architectures is computationally infeasible. In the future, a surrogate model [52, 55]
could be trained to predict the performance of ZC proxies on the remaining architectures. Finally,
there is very recent work on applying ZC proxies to one-shot NAS methods [51], which tested one
ZC proxy at a time with one-shot models. Since our work motivates the ensembling of ZC proxies,
an exciting problem for future work is to incorporate 13 ZC proxies into the one-shot framework.
Broader impact.
The goal of our work is to make it faster and easier for researchers to run
reproducible, generalizable ZC proxy experiments and to motivate further study on exploiting the
complementary strengths of ZC proxies. By pre-computing ZC proxies across many benchmarks,
researchers can run many trials of NAS experiments cheaply on a CPU, reducing the carbon footprint
of the experiments [11, 26]. Due to the notoriously high GPU consumption of prior research in NAS
[27, 57], this reduction in CO2 emissions is especially worthwhile. Furthermore, our hope is that
our work will have a positive impact in the NAS and automated machine learning communities by
showing which ZC proxies are useful in which settings, and showing how to most effectively combine
ZC proxies to achieve the best predictive performance. By open-sourcing all of our code and datasets,
AutoML researchers can use our library to further test and develop ZC proxies for NAS.
Acknowledgments and Disclosure of Funding
This research was supported by the following sources: Robert Bosch GmbH is acknowledged for
ﬁnancial support; the German Federal Ministry of Education and Research (BMBF, grant Renormal-
izedFlows 01IS19077C); TAILOR, a project funded by EU Horizon 2020 research and innovation
programme under GA No 952215; the Deutsche Forschungsgemeinschaft (DFG, German Research
Foundation) under grant number 417962828; the European Research Council (ERC) Consolidator
Grant “Deep Learning 2.0” (grant no. 101045765). Funded by the European Union. Views and
opinions expressed are however those of the author(s) only and do not necessarily reﬂect those of the
European Union or the ERC. Neither the European Union nor the ERC can be held responsible for
them.
10
References
[1] Mohamed S Abdelfattah, Abhinav Mehrotra, Łukasz Dudziak, and Nicholas Donald Lane.
Zero-cost proxies for lightweight nas. In Proceedings of the International Conference on
Learning Representations (ICLR), 2021.
[2] Hanlin Chen, Ming Lin, Xiuyu Sun, and Hao Li.
Nas-bench-zero:
A large scale
dataset for understanding zero-shot neural architecture search.
Openreview preprint
https://openreview.net/forum?id=hP-SILoczR, 2021.
[3] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. In Proceedings of
the 22nd acm sigkdd international conference on knowledge discovery and data mining, pages
785–794, 2016.
[4] Wuyang Chen, Xinyu Gong, and Zhangyang Wang. Neural architecture search on imagenet
in four gpu hours: A theoretically inspired perspective. In Proceedings of the International
Conference on Learning Representations (ICLR), 2021.
[5] Xiaoliang Dai, Alvin Wan, Peizhao Zhang, Bichen Wu, Zijian He, Zhen Wei, Kan Chen,
Yuandong Tian, Matthew Yu, Peter Vajda, et al. Fbnetv3: Joint architecture-recipe search using
predictor pretraining. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 16276–16285, 2021.
[6] Xuanyi Dong and Yi Yang. Nas-bench-201: Extending the scope of reproducible neural
architecture search. In Proceedings of the International Conference on Learning Representations
(ICLR), 2020.
[7] Yawen Duan, Xin Chen, Hang Xu, Zewei Chen, Xiaodan Liang, Tong Zhang, and Zhenguo
Li. Transnas-bench-101: Improving transferability and generalizability of cross-task neural
architecture search. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 5251–5260, 2021.
[8] Lukasz Dudziak, Thomas Chau, Mohamed Abdelfattah, Royson Lee, Hyeji Kim, and Nicholas
Lane. Brp-nas: Prediction-based nas using gcns. In H. Larochelle, M. Ranzato, R. Hadsell, M. F.
Balcan, and H. Lin, editors, Advances in Neural Information Processing Systems, volume 33,
pages 10480–10490. Curran Associates, Inc., 2020.
[9] Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. Neural architecture search: A survey.
In JMLR, 2019.
[10] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna
Wallach, Hal Daumé Iii, and Kate Crawford. Datasheets for datasets. Communications of the
ACM, 64(12):86–92, 2021.
[11] Karen Hao. Training a single ai model can emit as much carbon as ﬁve cars in their lifetimes.
MIT Technology Review, 2019.
[12] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition,
pages 770–778, 2016.
[13] Mojan Javaheripi, Shital Shah, Subhabrata Mukherjee, Tomasz L Religa, Caio CT Mendes,
Gustavo H de Rosa, Sebastien Bubeck, Farinaz Koushanfar, and Debadeepta Dey. Litetransform-
ersearch: Training-free on-device search for efﬁcient autoregressive language models. arXiv
preprint arXiv:2203.02094, 2022.
[14] Namhoon Lee, Thalaiyasingam Ajanthan, and Philip Torr. SNIP: Single-shot network pruning
based on connection sensitivity. In Proceedings of the International Conference on Learning
Representations (ICLR), 2019.
[15] Yuhong Li, Cong Hao, Pan Li, Jinjun Xiong, and Deming Chen. Generic neural architecture
search via regression. Proceedings of the Annual Conference on Neural Information Processing
Systems (NeurIPS), 34, 2021.
11
[16] Ming Lin, Pichao Wang, Zhenhong Sun, Hesen Chen, Xiuyu Sun, Qi Qian, Hao Li, and Rong
Jin. Zen-nas: A zero-shot nas for high-performance image recognition. In Proceedings of the
IEEE/CVF International Conference on Computer Vision, pages 347–356, 2021.
[17] Chenxi Liu, Barret Zoph, Maxim Neumann, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei,
Alan Yuille, Jonathan Huang, and Kevin Murphy. Progressive neural architecture search. In
Proceedings of the European Conference on Computer Vision (ECCV), pages 19–34, 2018.
[18] Hanxiao Liu, Karen Simonyan, and Yiming Yang. Darts: Differentiable architecture search. In
Proceedings of the International Conference on Learning Representations (ICLR), 2019.
[19] Zhengying Liu, Adrien Pavao, Zhen Xu, Sergio Escalera, Fabio Ferreira, Isabelle Guyon,
Sirui Hong, Frank Hutter, Rongrong Ji, Julio C. S. Jacques Junior, Ge Li, Marius Lindauer,
Zhipeng Luo, Meysam Madadi, Thomas Nierhoff, Kangning Niu, Chunguang Pan, Danny Stoll,
Sebastien Treguer, Jin Wang, Peng Wang, Chenglin Wu, Youcheng Xiong, Arbër Zela, and
Yang Zhang. Winning solutions and post-challenge analyses of the chalearn autodl challenge
2019. IEEE Transactions on Pattern Analysis and Machine Intelligence, 43(9):3108–3125,
2021.
[20] Vasco Lopes, Saeid Alirezazadeh, and Luís A Alexandre. Epe-nas: Efﬁcient performance
estimation without training for neural architecture search. In International Conference on
Artiﬁcial Neural Networks, pages 552–563. Springer, 2021.
[21] Yash Mehta, Colin White, Arber Zela, Arjun Krishnakumar, Guri Zabergja, Shakiba Moradian,
Mahmoud Safari, Kaicheng Yu, and Frank Hutter. Nas-bench-suite: Nas evaluation is (now)
surprisingly easy. In International Conference on Learning Representations, 2022.
[22] Joe Mellor, Jack Turner, Amos Storkey, and Elliot J Crowley. Neural architecture search without
training. In Proceedings of the International Conference on Machine Learning (ICML), 2021.
[23] Geoffrey F Miller, Peter M Todd, and Shailesh U Hegde. Designing neural networks using
genetic algorithms. In ICGA, volume 89, pages 379–384, 1989.
[24] Xuefei Ning, Changcheng Tang, Wenshuo Li, Zixuan Zhou, Shuang Liang, Huazhong Yang,
and Yu Wang. Evaluating efﬁcient performance estimators of neural architectures. Advances in
Neural Information Processing Systems, 34, 2021.
[25] Daniel S Park, Jaehoon Lee, Daiyi Peng, Yuan Cao, and Jascha Sohl-Dickstein. Towards
nngp-guided neural architecture search. arXiv preprint arXiv:2011.06006, 2020.
[26] David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel
Rothchild, David So, Maud Texier, and Jeff Dean. Carbon emissions and large neural network
training. arXiv preprint arXiv:2104.10350, 2021.
[27] Esteban Real, Alok Aggarwal, Yanping Huang, and Quoc V Le. Regularized evolution for image
classiﬁer architecture search. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence
(AAAI), 2019.
[28] Robin Ru, Clare Lyle, Lisa Schut, Miroslav Fil, Mark van der Wilk, and Yarin Gal. Speedy
performance estimation for neural architecture search. Proceedings of the Annual Conference
on Neural Information Processing Systems (NeurIPS), 34, 2021.
[29] Michael Ruchte, Arber Zela, Julien Siems, Josif Grabocka, and Frank Hutter. Naslib: A modular
and ﬂexible neural architecture search library. https://github.com/automl/NASLib, 2020.
[30] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-Chieh Chen.
Mobilenetv2: Inverted residuals and linear bottlenecks. In Proceedings of the IEEE conference
on computer vision and pattern recognition, pages 4510–4520, 2018.
[31] David W Scott. Sturges’ rule. Wiley Interdisciplinary Reviews: Computational Statistics,
1(3):303–306, 2009.
[32] Yu Shen, Yang Li, Jian Zheng, Wentao Zhang, Peng Yao, Jixiang Li, Sen Yang, Ji Liu, and Cui
Bin. Proxybo: Accelerating neural architecture search via bayesian optimization with zero-cost
proxies. arXiv preprint arXiv:2110.10423, 2021.
12
[33] Han Shi, Renjie Pi, Hang Xu, Zhenguo Li, James Kwok, and Tong Zhang. Bridging the gap
between sample-based and one-shot neural architecture search with bonas. Advances in Neural
Information Processing Systems, 33, 2020.
[34] Yao Shu, Shaofeng Cai, Zhongxiang Dai, Beng Chin Ooi, and Bryan Kian Hsiang Low. Nasi:
Label-and data-agnostic neural architecture search at initialization. In Proceedings of the
International Conference on Learning Representations (ICLR), 2022.
[35] Yao Shu, Zhongxiang Dai, Zhaoxuan Wu, and Kian Hsiang Low. Unifying and boosting
gradient-based training-free neural architecture search. ArXiv, abs/2201.09785, 2022.
[36] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Re-
thinking the inception architecture for computer vision. In Proceedings of the IEEE conference
on computer vision and pattern recognition, pages 2818–2826, 2016.
[37] Mingxing Tan and Quoc Le. Efﬁcientnet: Rethinking model scaling for convolutional neural
networks. In Proceedings of the International Conference on Machine Learning (ICML), 2019.
[38] Hidenori Tanaka, Daniel Kunin, Daniel L Yamins, and Surya Ganguli. Pruning neural networks
without any data by iteratively conserving synaptic ﬂow. Proceedings of the Annual Conference
on Neural Information Processing Systems (NeurIPS), 33:6377–6389, 2020.
[39] Manoel Tenorio and Wei-Tsih Lee. Self organizing neural networks for the identiﬁcation
problem. Advances in Neural Information Processing Systems, 1, 1988.
[40] Renbo Tu, Mikhail Khodak, Nicholas Carl Roberts, Nina Balcan, and Ameet Talwalkar. Nas-
bench-360: Benchmarking diverse tasks for neural architecture search. Openreview submission,
2021.
[41] Jack Turner, Elliot J Crowley, Michael O’Boyle, Amos Storkey, and Gavin Gray. Blockswap:
Fisher-guided block substitution for network compression on a budget. In Proceedings of the
International Conference on Learning Representations (ICLR), 2020.
[42] Chaoqi Wang, Guodong Zhang, and Roger Grosse. Picking winning tickets before training by
preserving gradient ﬂow. In International Conference on Learning Representations, 2020.
[43] Chen Wei, Chuang Niu, Yiping Tang, Yue Wang, Haihong Hu, and Jimin Liang. Npenas:
Neural predictor guided evolution for neural architecture search. IEEE Transactions on Neural
Networks and Learning Systems, 2022.
[44] Colin White, Mikhail Khodak, Renbo Tu, Shital Shah, Sébastien Bubeck, and Debadeepta
Dey. A deeper look at zero-cost proxies for lightweight nas. In ICLR Blog Track, 2022.
https://iclr-blog-track.github.io/2022/03/25/zero-cost-proxies/.
[45] Colin White, Willie Neiswanger, Sam Nolen, and Yash Savani. A study on encodings for neural
architecture search. In Proceedings of the Annual Conference on Neural Information Processing
Systems (NeurIPS), 2020.
[46] Colin White, Willie Neiswanger, and Yash Savani. Bananas: Bayesian optimization with neural
architectures for neural architecture search. In Proceedings of the AAAI Conference on Artiﬁcial
Intelligence (AAAI), 2021.
[47] Colin White, Arber Zela, Robin Ru, Yang Liu, and Frank Hutter. How powerful are performance
predictors in neural architecture search? In Proceedings of the Annual Conference on Neural
Information Processing Systems (NeurIPS), volume 34, 2021.
[48] Martin Wistuba, Ambrish Rawat, and Tejaswini Pedapati. A survey on neural architecture
search. arXiv preprint arXiv:1905.01392, 2019.
[49] Bichen Wu, Xiaoliang Dai, Peizhao Zhang, Yanghan Wang, Fei Sun, Yiming Wu, Yuandong
Tian, Peter Vajda, Yangqing Jia, and Kurt Keutzer. Fbnet: Hardware-aware efﬁcient convnet
design via differentiable neural architecture search. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 10734–10742, 2019.
13
[50] Bichen Wu, Alvin Wan, Xiangyu Yue, Peter Jin, Sicheng Zhao, Noah Golmant, Amir Gho-
laminejad, Joseph Gonzalez, and Kurt Keutzer. Shift: A zero ﬂop, zero parameter alternative to
spatial convolutions. In Proceedings of the IEEE conference on computer vision and pattern
recognition, pages 9127–9135, 2018.
[51] Lichuan Xiang, Łukasz Dudziak, Mohamed S Abdelfattah, Thomas Chau, Nicholas D Lane,
and Hongkai Wen. Zero-cost proxies meet differentiable architecture search. arXiv preprint
arXiv:2106.06799, 2021.
[52] Shen Yan, Colin White, Yash Savani, and Frank Hutter. Nas-bench-x11 and the power of
learning curves. In Proceedings of the Annual Conference on Neural Information Processing
Systems (NeurIPS), 2021.
[53] Chris Ying, Aaron Klein, Esteban Real, Eric Christiansen, Kevin Murphy, and Frank Hutter. Nas-
bench-101: Towards reproducible neural architecture search. In Proceedings of the International
Conference on Machine Learning (ICML), 2019.
[54] Amir R Zamir, Alexander Sax, William Shen, Leonidas J Guibas, Jitendra Malik, and Silvio
Savarese. Taskonomy: Disentangling task transfer learning. In Proceedings of the IEEE
conference on computer vision and pattern recognition, pages 3712–3722, 2018.
[55] Arber Zela, Julien Niklas Siems, Lucas Zimmer, Jovita Lukasik, Margret Keuper, and Frank
Hutter. Surrogate nas benchmarks: Going beyond the limited search spaces of tabular nas
benchmarks. In Proceedings of the International Conference on Learning Representations
(ICLR), 2022.
[56] Qinqin Zhou, Kekai Sheng, Xiawu Zheng, Ke Li, Xing Sun, Yonghong Tian, Jie Chen, and
Rongrong Ji. Training-free transformer architecture search. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pages 10894–10903, 2022.
[57] Barret Zoph and Quoc V. Le. Neural architecture search with reinforcement learning. In
Proceedings of the International Conference on Learning Representations (ICLR), 2017.
14
Table 5: Licenses for the datasets that we use.
Dataset
License
URL
NAS-Bench-101
Apache 2.0
https://github.com/google-research/nasbench
NAS-Bench-201
MIT
https://github.com/D-X-Y/NAS-Bench-201
NAS-Bench-301
Apache 2.0
https://github.com/automl/nasbench301
TransNAS-Bench-101
MIT
https://github.com/yawen-d/TransNASBench
NAS-Bench-360
MIT
https://github.com/rtu715/NAS-Bench-360
A
Dataset Documentation
Here, we give an overview of our dataset documentation. For the full details, including links to the
dataset, usage, and tutorials, see https://github.com/automl/NASLib/tree/zerocost.
A.1
Author responsibility and license
We, the authors, bear all responsibility in case of violation of rights. The license of our dataset and
repository is the Apache License 2.0. For more information, see https://github.com/automl/
NASLib/blob/Develop/LICENSE.
In addition, we include the licenses of the datasets we used in Table 5.
A.2
Maintenance plan
The data is available on GitHub at https://github.com/automl/NASLib/tree/zerocost. We
plan to actively maintain the repository, and we also welcome contributions from the community. For
more information, see https://github.com/automl/NASLib/tree/zerocost.
A.3
Code of conduct
Our Code of Conduct is from the Contributor Covenant, version 2.0. See
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.
A.4
Datasheet
We include a datasheet [10] for NAS-Bench-Suite-Zero. Please see
https://github.com/automl/NASLib/blob/zerocost/docs/DATASHEET.md.
B
Related Work Continued
In this section, we give additional details on related work, continued from Section 2.
Multiple recent works have investigated the performance of ZC proxies in ranking architectures
over different NAS benchmarks. [24] provides rank correlations and pairwise correlations of 10 ZC
proxies across 7 tasks, and concludes that the relative performance of different ZC proxies highly
depends on the search space. They further analyze how ZC proxies have improper biases. [47]
compares 6 ZC proxies across four tasks, and further shows how jacov can be used to accelerate
the search in predictor-based NAS. In particular, OMNI [47] combines jacov with sum of training
losses [28] in the surrogate models of BANANAS and predictor-guided evolution. However, the
predictor-based NAS experiments are restricted to NAS-Bench-201 and a single ZC proxy. Similar
to [47], ProxyBO [32] introduces a NAS framework based on BO which uses ZC proxies to speed
up NAS. It dynamically chooses whether to use a Gaussian process, snip, jacov, or synflow
as the surrogate model in BO. Experiments were done on ﬁve tasks. Note that although the NAS
method makes use of three different ZC proxies, each are used separately to make predictions on the
performance of architectures.
Recently, NAS-Bench-Zero was introduced [2], a new benchmark based on popular computer vision
models ResNet [12] and MobileNetV2 [30], and examined different characteristics of 10 ZC proxies
15
across these search space as well as three existing search spaces. The study shows in particular that
individual ZC proxies do not transfer across NAS benchmarks. They also show that voting among
synflow, zen, snip and synflow is the optimal voting ZC proxy strategy. A recent overview of ZC
proxies [44] computes rank correlation, pairwise correlation, and performance plots for 8 ZC proxies
across 12 tasks.
Only two prior works combine the information of multiple ZC proxies together in architecture
predictions [1, 2] and both only use the voting strategy to combine three or four ZC proxies. Our
work is the ﬁrst to combine ZC proxies in a nontrivial way, and the ﬁrst to combine 13 ZC proxies.
We also conduct analysis on the largest set of ZC proxies and benchmarks to date.
B.1
Theoretical results for ZC proxies
While ZC proxies are starting to be used more widely today [1, 13, 44, 56], still relatively little is
known about them from a theoretical standpoint. However, there have been a few works that do give
theoretical results. In this section, we survey the existing theoretical results for ZC proxies.
Ning et al. gave a theoretical preference analysis for synflow, proving that it favors larger archi-
tectures (Section B.3 in [24]). Speciﬁcally, they prove that given an architecture, introducing a new
fully-connected layer into an MLP architecture causes the synflow value to increase. The core of
their argument is to prove the following statement: “when introducing a new fully-connected layer,
the expected loss gradients with respect to the existing parameters increases.” The authors also claim
that the intuition for this argument should extend to convolutional neural networks. Finally, we note
that our empirical results from Table 3 conﬁrm their theoretical ﬁnding.
Shu et al. [35] attempted to give a uniﬁed, general theory for multiple ZC proxies. First, the authors
prove that ZC proxy values are asymptotically similar. Speciﬁcally, they show that assuming the
loss function of the neural network is β-Lipschitz continuous, and γ-Lipschitz smooth, then with
high-priority, then the values of grad_norm, snip, and grasp are all asymptotically similar up to
constants (i.e., the same under big-Oh notation) to the trace norm of the NTK matrix at initialization.
This result implies that the values of these ZC proxies are highly correlated.
Next, Shu et al. establish generalization bounds for DNNs in terms of the ZC proxies. Speciﬁcally,
they show that the generalization error of a DNN is at most the sum of the training error of the DNN
and O (κ/M), where M can be set to grad_norm, snip, or grasp, and κ is the condition number
of the NTK matrix at initialization, i.e., given the NTK matrix Θ0, κ = λmax(Θ0)/λmin(Θ0).
As a corollary, they also bound the generalization error in terms of the ZC proxy value and other
ﬁxed constants of the neural network, without the training error term.
Other than these results, a few works have derived new ZC proxies via a theoretical analysis or
inspired by existing theories of deep learning. Shu et al. [34] introduce NASI by giving a theoretical
analysis that shows the trace norm of the NTK has a similar form to gradient ﬂow. Other theory-
inspired ZC proxies include TE-NAS [4], which uses the spectrum of the NTK and the number of
linear regions in the input space, and NNGP-NAS [25], which approximates the Neural Network
Gaussian Process using Monte-Carlo methods.
As ZC proxies gain in popularity, a further theoretical analysis is an important step in understanding
their robustness on different datasets, and in designing higher-performing ZC proxies.
C
Details from Section 4
In this section, we give additional details from Section 4.
C.1
Details from Section 4.1: generalization
We give the full extensions of the experiments from Section 4.1. In Figure 6, for each ZC proxy and
each benchmark, we compute the Spearman rank correlation (see Section 4). This is the full version
of Figure 2.
In Figure 7, we compute the Pearson correlation coefﬁcient between ZC proxy scores on pairs of
benchmarks. This is the full version of Figure 3.
16
Table 6: Spearman rank correlation for 100 architectures randomly drawn from the FBNet search
space on various ZC proxies.
ZC Proxy
fisher
flops
grad_norm
grasp
jacov
params
snip
synflow
Spearman
0.2574
0.6484
0.4278
-0.262
-0.0895
0.3762
0.5102
0.4954
Next, we recompute Figure 2 using different metrics: Precision@K and BestRanking@K [2, 24].
Let M denote the number of architectures, and for each architecture ai from i ∈[1, M], denote the
rankings of the ground truth and ZC proxy-estimated scores are ri and ni, respectively. Given K,
deﬁne AK = {ai | ni < KM}. The deﬁnitions are as follows:
Precision@K = #{i | ri < K ∧ni < K}
K
BestRanking@K = argminαi∈AKri/M
In Figure 8, we recompute Figure 2 using Precision@K, for K = 5, 25, 100. In Figure 9, we
recompute Figure 2 using BestRanking@K, for K = 5, 25, 100. Overall, we see similar trends to
Figure 2, but we note that Precision@K and BestRanking@K may be more useful than Spearman in
terms of NAS, since the goal of NAS is to ﬁnd the very best architectures.
C.1.1
Initial results with FBNet
While NAS-Bench-Suite-Zero contains 28 tasks, the majority of search spaces used were designed
for research. Now, in contrast, we give initial results for FBNet [49] as a search space that has been
used to achieve state-of-the-art results.
The FBNet search space consists of 22 searchable layers, with 9 operation choices each (3 ﬁlters and
3 kernel sizes), for a total of 922 = 1021 architectures in the search space. The block structure is
inspired by MobileNetV2 [30] and ShiftNet [50].
See Table 6 for the Spearman rank correlation values of the validation accuracy of 100 randomly drawn
architectures compared to ZC proxies. Even though the FBNet search space is size 1021, some of the
ZC proxies perform surprisingly well, such as snip, synflow, and flops. The highest-performing
ZC proxy is flops.
C.2
Details from Section 4.2: information theory
In this section, we give details from Section 4.2. We start with more details on the conditionial
entropy, including why we chose this metric, how it is computed, and how to interpret the results.
• Why do we choose conditional entropy as the metric?
The conditional entropy of a random variable Y given another random variable X is
H(Y |X) = E[−log(p(y|x))] = −
X
x∈X,y∈Y
p(x, y) log p(x, y)
p(x) ,
(3)
for two support sets X, Y. If we assume entropy to be a measure of information, in other words
uncertainty within a random variable, conditional entropy essentially captures what is left of the
uncertainty after conditioning. H(Y |X) also has certain desirable properties: (1). H(Y |X) = 0
if and only if X completely determines the value of Y ; (2). H(Y |X) = H(Y ) if and only if X
and Y are completely independent; and (3). H(Y |X1, X2) = H(Y, X1, X2) −H(X1, X2). We
can then easily calculate conditional entropy when conditioning on multiple random variables,
and use it as a metric for uncertain information.
• Discretization of ZC proxy scores and ground-truth accuracies.
Calculating conditional entropy as prescribed above requires that all random variables be discrete,
which is not the case for raw validation accuracies and ZC proxy scores. Implementation wise,
we discretize all the ﬂoat values and use Sturge’s rule [31] as a heuristic to choose the number of
bins for discretization:
nbins = round(1 + 3.322 ∗log(N))), where N is the sample size.
(4)
17
Therefore, information about Y does not reveal the exact validation accuracy but rather the interval
in which the value falls.
• Interpreting the information gain heatmap.
The information gain heatmap shows how much the conditional entropy of y|zi1 decreases
to y|zi1, zi2 as the scores of ZC proxy on each column (zi2) is revealed, given that we al-
ready know the scores of ZC proxy on each row (zi1).
For instance, on Figure 4 (top
right), the value 1.42 on the second row, ﬁrst column shows that H(y|scores(synﬂow) −
H(y|scores(synﬂow), scores(epe_nas)) = 1.42. Note that (1). all values on the diagonal
are 0.0 because no information is gained when we add a copy of the existing ZC proxy scores; (2).
The heatmap is not symmetric like pairwise conditional entropy. The order in which conditioning
is applied affects the amount of information gain, i.e. IG(y|zi1, zi2)̸ = IG(y|zi2, zi1); (3). IG
measures how much one ZC proxy’s information complements that of another for determining
the ground-truth accuracy. It does not serve as a direct indicator of the quality of individual ZC
proxy themselves.
• Interpreting the entropy vs. number of ZC proxies plot.
Conditional entropy monotonically decreases as we condition the validation accuracy, y, on an
increasing amount of ZC proxy scores, zi1, . . . zik, which always brings in additional information.
In most cases, marginal IG drastically decreases as the amount of ZC proxies k reaches 4, but
this is only true if the proxies are chosen strategically, using either a greedy or a brute-force
minimization approach. For the majority of benchmarks, the less computationally intensive greedy
strategy matches up to the brute-force strategy. On the other hand, randomly choosing the ZC
proxies does not have stable performance and could be suboptimal, such as on NAS-Bench-201 +
CIFAR-100 in Figure 4 (bottom middle).
For completion, in Figure 10, we plot the average pairwise correlation for all pairs of ZC proxies.
In Figures 11, 12, 13, 14, 15, we show all the conditional entropy and information gain heatmaps,
in addition to the entropy vs. number of ZC proxies plots for all benchmark, dataset pairs. Note
that for TransNAS-Bench-101, there are no results for epe_nas because it is not deﬁned on non-
classiﬁcation tasks. Similarly, synflow returns 0.0 for certain non-classiﬁcation tasks such as the
ones in TransNAS-Bench-101, so we also removed synflow from the TransNAS-Bench-101 plots.
While the conditional entropy and information gain plots from Figure 4 was computed using Equation
4 to compute the number of bins, we also run the same experiment using a different discretization
strategy: the bin dividers are computed based on percentages of the data. See Figure 16 (top). While
the scales differ, we see largely the same trends. For example, there is still a cluster among nwot,
flops, l2_norm, zen, and params. This suggests that this analysis is robust to the two different
discretization strategies. Next, we also re-run the experiment on conditional entropy vs. k from
Figure 4 using the top 1000 architectures only, which may be important in the context of NAS, since
NAS is concerned with ﬁnding the best architectures. See Figure 16 (bottom). We ﬁnd that the
random ordering performs comparatively better, predictably implying that it is harder to distinguish
architectures that are in the top 1000 vs. randomly drawn architectures.
C.3
Details from Section 4.3: biases
In this section, we give details from Section 4.3. In Table 7, for each bias metric we assess, we show
the ZC proxies with the highest and lowest absolute correlation for each search space and dataset,
if applicable. For the number of parameters bias, we do not consider the ZC proxies of params
and flops since they trivially have 1.00 correlation. Note that operation biases are not available in
TransNASBench101-Macro because the search space is architecture-level. This is an extension of
Table 3.
C.4
NAS-Bench-Suite-Zero Speedup Details
Here we show statistics on how our benchmark speeds up NAS experiments previously done with
NAS-Bench-Suite by orders of magnitude. See Table 8.
D
Details from Section 5
In this section, we give the full details from Section 5.
18
Table 7: Pearson correlation coefﬁcients between predictors and bias metrics (in bold) on different
datasets, for the most and least biased ZC proxies on each search space and task. For example, for the
Conv:pool bias on NB201-CF10, synflow is most biased, with a correlation of 0.76, while grasp
is least biased (in terms of absolute value), with a correlation of -0.01.
Name
Conv:pool
Cell size
Num. skip connections
Num. parameters
Most biased
Least biased
Most biased
Least biased
Most biased
Least Biased
Most biased
Least biased
NB101-CF10
synﬂow
grasp
n/a
n/a
n/a
n/a
nwot
epe_nas
0.76
-0.01
0.74
-0.02
NB201-CF10
l2_norm
grasp
synﬂow
grasp
l2_norm
grasp
l2_norm
grasp
0.87
0.01
0.57
-0.02
-0.41
-0.01
0.70
0.00
NB201-CF100
l2_norm
grasp
synﬂow
grasp
l2_norm
grasp
l2_norm
ﬁsher
0.87
0.01
0.57
-0.01
-0.41
-0.01
0.70
0.01
NB201-IM
l2_norm
grasp
synﬂow
grasp
l2_norm
grasp
l2_norm
grasp
0.87
0.01
0.58
0.01
-0.41
-0.01
0.70
0.01
NB301-CF10
params
ﬁsher
n/a
n/a
ﬂops
epe_nas
zen
epe_nas
0.78
0.01
-0.35
0.01
0.99
-0.01
TNB101_MICRO-JIGSAW
n/a
n/a
l2_norm
grasp
plain
grasp
l2_norm
grasp
0.70
-0.02
0.50
-0.01
0.64
0.02
TNB101_MICRO-SCENE
n/a
n/a
l2_norm
ﬁsher
plain
grasp
snip
grasp
0.70
0.07
0.49
-0.10
0.64
-0.04
TNB101_MICRO-OBJECT
n/a
n/a
l2_norm
ﬁsher
plain
grasp
l2_norm
grasp
0.70
-0.08
0.49
-0.06
0.64
-0.02
TNB101_MICRO-AUTOENC
n/a
n/a
l2_norm
grasp
grad_norm
grasp
l2_norm
grasp
0.70
-0.02
-0.46
-0.03
0.64
0.02
TNB101_MICRO-NORMAL
n/a
n/a
l2_norm
plain
snip
grasp
l2_norm
plain
0.70
0.01
-0.45
-0.01
0.64
0.00
TNB101_MICRO-ROOM
n/a
n/a
l2_norm
ﬁsher
plain
jacov
l2_norm
grasp
0.70
0.10
0.45
0.14
0.64
-0.01
TNB101_MICRO-SEGMENT
n/a
n/a
l2_norm
grasp
grad_norm
grasp
l2_norm
grasp
0.70
0.00
-0.43
0.01
0.64
-0.01
TNB101_MACRO-JIGSAW
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
plain
0.89
0.04
TNB101_MACRO-SCENE
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
plain
0.90
0.05
TNB101_MACRO-OBJECT
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
plain
0.89
0.05
TNB101_MACRO-AUTOENC
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
plain
0.89
0.01
TNB101_MACRO-NORMAL
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
grasp
0.89
-0.02
TNB101_MACRO-ROOM
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
grasp
0.89
0.00
TNB10_MACRO-SEGMENT
n/a
n/a
n/a
n/a
n/a
n/a
l2_norm
plain
0.89
0.00
We start by presenting the complete standalone predictor experiments. In Section 5, we mentioned that
on NAS-Bench-201 CIFAR-100, the Spearman rank correlation of XGBoost predictions trained on
100 randomly sampled architectures and averaged over 100 trials, improves from 0.640 to 0.908 when
13 ZC proxies are added. Now, we present the results of this same experiment for all benchmarks.
See Table 9. We see that the large improvement is consistent across the board. We also run the same
experiment when XGBoost is trained on 1000 randomly sampled architectures. See Table 10. Even
though the predictions with the original XGBoost already have high rank correlation, we show that
ZC proxies improve the performance even more.
D.1
Feature importances of ZC proxies
In this section, we train an XGBoost surrogate model on 100 and 1000 randomly drawn architectures
using the ZC proxies as features, and then we plot feature importances for each feature. The feature
importance is calculated by the the number of times a feature is used to split the data across all trees
19
Table 8: Runtimes (on an Intel Xeon Gold 6242 CPU) for all types of experiments done in this
paper, with and without NAS-Bench-Suite-Zero. The runtimes of the experiments with NBSuite
are computed by using the average training times for randomly drawn architectures from each search
space in NBSuite.
Experiment
With NBSuite (approx.)
With NBSuite + NBSuite-Zero
Speedup
Mutual information study
158.2 hours
124.1 seconds
4592×
Architecture bias study
6956 hours
14.8 seconds
1776003×
Standalone XGBoost+ZC, 100 trials
1033 hours
100 seconds
37180×
BANANAS+ZC, 100 trials
4694 hours
4260 seconds
3967×
NPENAS+ZC, 100 trials
1033 hours
3470 seconds
1071×
Table 9: Average Spearman rank correlations between XGBoost predictions and validation accuracies,
for each benchmark, across three different experiments: Encoding uses only the encoding of the
model, ZC uses only the ZC features, and Both concatenates ZC features to the encoding of the model.
100 models were used to train XGBoost.
Features
Encoding
ZC
Both
% Improvement (ZC)
% Improvement (Both)
Benchmark
NB101-CF10
0.546
0.708
0.718
29.67
31.50
NB201-CF10
0.622
0.905
0.906
45.50
45.66
NB201-CF100
0.640
0.907
0.908
41.71
41.87
NB201-IMGNT
0.683
0.879
0.883
28.70
29.28
NB301-CF10
0.314
0.405
0.465
28.98
48.09
TNB101_MACRO-AUTOENC
0.673
0.831
0.837
23.48
24.37
TNB101_MACRO-JIGSAW
0.809
0.706
0.809
-12.73
0.00
TNB101_MACRO-NORMAL
0.617
0.710
0.716
15.07
16.05
TNB101_MACRO-OBJECT
0.736
0.840
0.843
14.13
14.54
TNB101_MACRO-ROOM
0.683
0.589
0.707
-13.76
3.51
TNB101_MACRO-SCENE
0.832
0.891
0.899
7.09
8.05
TNB101_MACRO-SEGMENT
0.900
0.807
0.876
-10.33
-2.67
TNB101_MICRO-AUTOENC
0.714
0.754
0.803
5.60
12.46
TNB101_MICRO-JIGSAW
0.585
0.730
0.743
24.79
27.01
TNB101_MICRO-NORMAL
0.657
0.801
0.809
21.92
23.14
TNB101_MICRO-OBJECT
0.637
0.733
0.752
15.07
18.05
TNB101_MICRO-ROOM
0.582
0.843
0.844
44.85
45.02
TNB101_MICRO-SCENE
0.710
0.849
0.866
19.58
21.97
TNB101_MICRO-SEGMENT
0.767
0.886
0.897
15.51
16.95
(the default feature importance method in the XGBoost library [3]). See Figures 20 and 21 for the
results with a training set size of 100 and 1000, respectively.
D.2
Ablation study on the number of ZC proxies
Next, we give an ablation study on the number of ZC proxies as features, for an XGBoost surrogate
model trained on 1000 randomly drawn architectures. The ordering of ZC proxies is computed via
the greedy method from Section 4.3. See Figure 17. We ﬁnd that on all tasks, the best performance
is achieved with all 13 ZC proxies (in some cases, there are ties). However, after 6-8 ZC proxies,
there is only a small improvement up to the full 13 ZC proxies. This is consistent with our mutual
information study from Section 4.3.
D.3
Additional NAS results
Finally, we present more NAS results, extending the NAS results from Section 5. In Figure 18, we
run BANANAS in the same setting as Section 5, on 11 benchmarks. We see that ZC proxies improve
performance across the board. In Figure 19, we run the same experiment with NPENAS instead of
BANANAS. Note that since NPENAS requires a mutation step, we are only able to run it on complete
benchmarks: NAS-Bench-201 and TransNAS-Bench-101 (in particular, not NAS-Bench-101 or
NAS-Bench-301).
20
Table 10: Average Spearman rank correlations between XGBoost predictions and validation accura-
cies, for each benchmark, across three different experiments: Encoding uses only the encoding of
the model, ZC uses only the ZC features, and Both concatenates ZC features to the encoding of the
model. 1000 models were used to train XGBoost.
Features
Encoding
ZC
Both
% Improvement (ZC)
% Improvement (Both)
Benchmark
NB101-CF10
0.748
0.811
0.851
8.42
13.77
NB201-CF10
0.890
0.954
0.961
7.19
7.98
NB201-CF100
0.906
0.953
0.959
5.19
5.85
NB201-IMGNT
0.922
0.948
0.957
2.82
3.80
NB301-CF10
0.678
0.496
0.705
-26.84
3.98
TNB101_MACRO-AUTOENC
0.890
0.903
0.917
1.46
3.03
TNB101_MACRO-JIGSAW
0.812
0.801
0.856
-1.35
5.42
TNB101_MACRO-NORMAL
0.692
0.759
0.764
9.68
10.40
TNB101_MACRO-OBJECT
0.846
0.880
0.888
4.02
4.96
TNB101_MACRO-ROOM
0.741
0.731
0.793
-1.35
7.02
TNB101_MACRO-SCENE
0.936
0.936
0.953
0.00
1.82
TNB101_MACRO-SEGMENT
0.951
0.920
0.952
-3.26
0.11
TNB101_MICRO-AUTOENC
0.838
0.815
0.861
-2.74
2.74
TNB101_MICRO-JIGSAW
0.768
0.827
0.833
7.68
8.46
TNB101_MICRO-NORMAL
0.816
0.850
0.864
4.17
5.88
TNB101_MICRO-OBJECT
0.806
0.841
0.858
4.34
6.45
TNB101_MICRO-ROOM
0.874
0.943
0.947
7.89
8.35
TNB101_MICRO-SCENE
0.862
0.929
0.943
7.77
9.40
TNB101_MICRO-SEGMENT
0.921
0.934
0.948
1.41
2.93
E
ZC Proxy Competition
NAS-Bench-Suite-Zero was used successfully in the Zero Cost NAS Competition at AutoML-
Conf 2022. During the competition, participants developed new, better versions of ZC proxies in the
NAS-Bench-Suite-Zero codebase. The challenge was as follows: given N models, the participant’s
ZC proxy will be used to rank the models for a speciﬁed task. The Kendall-Tau rank correlation is
used to score the metric, averaged across three benchmarks in the test phase of the competition. The
tasks in the development phase of the competition were NB201 with Ninapro and SVHN, NB301 with
Ninapro and SVHN, and TNB101-Micro with Ninapro, SVHN, and Spherical-CIFAR100. The tasks
in the ﬁnal test phase of the competition were NB101 with CIFAR10, NB201 with ImageNet16x120,
NB301 with CIFAR10, TNB101-Macro with Object Classiﬁcation, and TNB101-Micro with Object
Classiﬁcation. The winning teams used a normalized version of synflow, a normalized version
of fisher, and a product of grad_norm and params. For more information, see the competition
homepage at https://sites.google.com/view/zero-cost-nas-competition/home.
21
TNB101_MICRO-AUTOENC
NB201-NINAPRO
NB301-NINAPRO
NB201-SCIFAR100
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
NB301-SCIFAR100
TNB101_MACRO-JIGSAW
NB101-CF10
TNB101_MACRO-AUTOENC
TNB101_MACRO-SCENE
NB301-CF10
TNB101_MACRO-SEGMENT
TNB101_MICRO-ROOM
TNB101_MACRO-NORMAL
TNB101_MICRO-NINAPRO
NB301-SVHN
TNB101_MICRO-JIGSAW
TNB101_MICRO-NORMAL
TNB101_MICRO-OBJECT
TNB101_MICRO-SEGMENT
NB201-IMGNT
TNB101_MICRO-SCENE
TNB101_MICRO-SCIFAR100
NB201-CF10
NB201-CF100
NB201-SVHN
TNB101_MICRO-SVHN
plain
grasp
fisher
epe_nas
grad_norm
snip
synflow
l2_norm
params
zen
jacov
flops
nwot
0.07 -0.20 0.06 0.10 -0.19 -0.18 0.13 -0.30 -0.32 -0.10 -0.19 -0.32 0.00 0.36 -0.04 0.22 -0.13 0.35 0.03 0.34 -0.02 -0.22 0.24 -0.09 -0.26 -0.21 -0.34 -0.16
-0.12 -0.01 0.04 -0.01 -0.64 -0.10 0.13 -0.26 0.27 -0.02 -0.43 0.34 -0.02 -0.29 -0.05 -0.20 0.18 -0.12 0.01 -0.22 0.00 0.55 -0.27 -0.03 0.51 0.54 0.62 -0.24
-0.58 -0.38 -0.11 0.07 -0.30 -0.21 0.00 -0.26 -0.28 -0.19 -0.13 -0.28 0.03 0.30 0.15 0.42 0.05 0.30 0.16 0.44 0.12 0.48 0.66 0.72 0.50 0.54 0.71 0.81
0.00 0.01 -0.11 -0.27 -0.02 -0.00 0.00 0.00 0.00 0.00 0.01 0.00 0.00 0.40 0.00 0.19 -0.08 0.16 0.00 0.39 0.00 0.33 0.51 0.29 0.70 0.60 0.58 0.40
-0.32 -0.23 -0.20 -0.08 -0.56 -0.26 -0.00 -0.27 -0.25 0.31 -0.33 -0.04 0.21 0.25 0.35 0.40 0.42 0.36 0.36 0.39 0.60 0.57 0.65 0.72 0.58 0.63 0.77 0.78
-0.27 -0.28 -0.10 -0.09 -0.38 -0.19 -0.01 -0.19 -0.19 0.20 -0.14 -0.05 0.27 0.32 0.45 0.42 0.38 0.41 0.49 0.45 0.68 0.57 0.70 0.76 0.58 0.63 0.76 0.83
0.00 0.02 -0.07 0.13 0.12 -0.01 0.05 0.34 0.31 0.00 0.27 0.18 0.00 0.30 0.00 0.45 0.50 0.47 0.00 0.48 0.00 0.75 0.72 0.79 0.73 0.76 0.71 0.92
0.04 0.02 -0.07 -0.00 0.08 -0.03 0.12 0.15 0.50 -0.20 0.28 0.45 0.18 0.18 0.30 0.36 0.70 0.35 0.50 0.32 0.48 0.69 0.53 0.53 0.68 0.72 0.67 0.52
-0.01 -0.11 -0.07 -0.14 0.16 -0.00 0.07 0.15 0.37 -0.18 0.32 0.46 0.06 0.30 0.30 0.36 0.70 0.44 0.62 0.45 0.68 0.69 0.64 0.79 0.72 0.73 0.72 0.76
0.14 0.15 -0.09 0.23 0.10 -0.04 0.07 0.24 0.59 -0.01 0.27 0.43 0.27 0.38 0.38 0.42 0.68 0.51 0.71 0.54 0.67 0.39 0.72 0.67 0.35 0.35 0.18 0.74
0.18 0.29 0.13 -0.41 0.07 0.08 0.08 0.19 -0.29 0.45 0.19 -0.04 0.57 0.40 0.50 0.40 -0.36 0.56 0.75 0.51 0.80 0.71 0.75 0.71 0.75 0.71 0.67 0.77
-0.02 -0.13 -0.09 -0.12 0.79 0.48 0.09 0.64 0.36 0.76 0.85 0.42 0.60 0.30 0.76 0.38 0.68 0.45 0.64 0.46 0.69 0.67 0.65 0.79 0.69 0.71 0.71 0.77
0.03 0.06 0.02 -0.02 0.83 0.63 0.05 0.76 0.31 0.67 0.89 0.47 0.80 0.25 0.78 0.38 0.64 0.42 0.57 0.39 0.53 0.77 0.60 0.64 0.77 0.80 0.76 0.63
Spearman rank correlations between ZC proxy values and validation accuracies
Figure 6: Spearman rank correlation coefﬁcient between ZC proxy values and validation accuracies,
for each ZC proxy and benchmark. The rows and columns are ordered based on the mean scores
across columns and rows, respectively. This is the full version of Figure 2.
22
NB101-CF10
NB201-CF10
NB201-CF100
NB201-IMGNT
NB301-CF10
TNB101_MICRO-JIGSAW
TNB101_MICRO-SCENE
TNB101_MICRO-OBJECT
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
TNB101_MICRO-NORMAL
TNB101_MICRO-SEGMENT
TNB101_MACRO-JIGSAW
TNB101_MACRO-SCENE
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MACRO-AUTOENC
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
NB201-SCIFAR100
NB201-SVHN
NB201-NINAPRO
NB301-SCIFAR100
NB301-SVHN
NB301-NINAPRO
TNB101_MICRO-SCIFAR100
TNB101_MICRO-SVHN
TNB101_MICRO-NINAPRO
NB101-CF10
NB201-CF10
NB201-CF100
NB201-IMGNT
NB301-CF10
TNB101_MICRO-JIGSAW
TNB101_MICRO-SCENE
TNB101_MICRO-OBJECT
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
TNB101_MICRO-NORMAL
TNB101_MICRO-SEGMENT
TNB101_MACRO-JIGSAW
TNB101_MACRO-SCENE
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MACRO-AUTOENC
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
NB201-SCIFAR100
NB201-SVHN
NB201-NINAPRO
NB301-SCIFAR100
NB301-SVHN
NB301-NINAPRO
TNB101_MICRO-SCIFAR100
TNB101_MICRO-SVHN
TNB101_MICRO-NINAPRO
1.00 0.32 0.33 0.41 0.93 0.03 -0.03 -0.08 -0.24 0.45 0.29 0.16 0.61 0.57 0.50 0.45 -0.03 0.20 0.12 0.35 0.13 0.43 0.41 0.78 -0.11 0.15 0.08 -0.04
0.32 1.00 0.99 0.92 0.49 0.11 0.38 0.14 -0.05 -0.02 0.34 0.38 0.51 0.44 0.35 0.42 0.35 0.42 0.37 -0.49 0.92 0.30 -0.32 0.32 -0.22 0.64 0.60 0.23
0.33 0.99 1.00 0.96 0.51 0.13 0.37 0.12 -0.10 -0.09 0.35 0.40 0.51 0.44 0.34 0.41 0.36 0.46 0.38 -0.41 0.95 0.23 -0.31 0.39 -0.25 0.67 0.62 0.26
0.41 0.92 0.96 1.00 0.58 0.21 0.36 0.10 -0.17 -0.03 0.46 0.48 0.55 0.47 0.35 0.43 0.38 0.52 0.45 -0.29 0.90 0.29 -0.15 0.47 -0.14 0.70 0.62 0.28
0.93 0.49 0.51 0.58 1.00 0.04 -0.03 -0.13 -0.31 0.45 0.47 0.38 0.68 0.62 0.55 0.59 0.20 0.42 0.35 0.10 0.31 0.47 0.39 0.78 -0.03 0.23 0.12 -0.06
0.03 0.11 0.13 0.21 0.04 1.00 0.87 0.90 0.79 0.30 0.66 0.64 0.49 0.55 0.52 0.26 0.32 0.56 0.50 -0.01 -0.00 0.19 -0.15 0.24 -0.02 0.71 0.73 0.90
-0.03 0.38 0.37 0.36 -0.03 0.87 1.00 0.95 0.82 -0.00 0.55 0.57 0.40 0.46 0.42 0.17 0.26 0.51 0.39 -0.13 0.30 0.03 -0.55 0.24 -0.37 0.87 0.93 0.97
-0.08 0.14 0.12 0.10 -0.13 0.90 0.95 1.00 0.94 0.12 0.48 0.47 0.37 0.46 0.45 0.15 0.19 0.42 0.32 -0.06 0.02 0.03 -0.45 0.14 -0.26 0.71 0.79 0.93
-0.24 -0.05 -0.10 -0.17 -0.31 0.79 0.82 0.94 1.00 0.18 0.32 0.30 0.23 0.33 0.37 0.07 0.12 0.26 0.22 -0.14 -0.19 0.02 -0.42 -0.10 -0.16 0.46 0.57 0.79
0.45 -0.02 -0.09 -0.03 0.45 0.30 -0.00 0.12 0.18 1.00 0.33 0.19 0.52 0.46 0.50 0.44 0.18 0.15 0.30 -0.14 -0.36 0.82 0.60 0.06 0.55 -0.17 -0.17 -0.05
0.29 0.34 0.35 0.46 0.47 0.66 0.55 0.48 0.32 0.33 1.00 0.96 0.51 0.57 0.49 0.43 0.46 0.84 0.73 -0.25 0.24 0.34 0.07 0.41 0.06 0.61 0.53 0.52
0.16 0.38 0.40 0.48 0.38 0.64 0.57 0.47 0.30 0.19 0.96 1.00 0.39 0.43 0.35 0.31 0.50 0.83 0.69 -0.33 0.34 0.21 -0.08 0.39 -0.07 0.66 0.58 0.53
0.61 0.51 0.51 0.55 0.68 0.49 0.40 0.37 0.23 0.52 0.51 0.39 1.00 0.97 0.95 0.92 0.61 0.68 0.72 -0.06 0.28 0.51 0.17 0.51 0.13 0.46 0.41 0.37
0.57 0.44 0.44 0.47 0.62 0.55 0.46 0.46 0.33 0.46 0.57 0.43 0.97 1.00 0.99 0.90 0.56 0.72 0.72 -0.05 0.22 0.37 0.16 0.53 0.10 0.48 0.43 0.45
0.50 0.35 0.34 0.35 0.55 0.52 0.42 0.45 0.37 0.50 0.49 0.35 0.95 0.99 1.00 0.92 0.56 0.67 0.69 -0.07 0.12 0.37 0.18 0.43 0.16 0.38 0.34 0.40
0.45 0.42 0.41 0.43 0.59 0.26 0.17 0.15 0.07 0.44 0.43 0.31 0.92 0.90 0.92 1.00 0.73 0.71 0.79 -0.18 0.24 0.40 0.22 0.35 0.27 0.23 0.17 0.13
-0.03 0.35 0.36 0.38 0.20 0.32 0.26 0.19 0.12 0.18 0.46 0.50 0.61 0.56 0.56 0.73 1.00 0.80 0.89 -0.38 0.31 0.21 -0.07 0.11 0.13 0.33 0.28 0.21
0.20 0.42 0.46 0.52 0.42 0.56 0.51 0.42 0.26 0.15 0.84 0.83 0.68 0.72 0.67 0.71 0.80 1.00 0.93 -0.25 0.38 0.16 -0.08 0.43 -0.01 0.61 0.53 0.50
0.12 0.37 0.38 0.45 0.35 0.50 0.39 0.32 0.22 0.30 0.73 0.69 0.72 0.72 0.69 0.79 0.89 0.93 1.00 -0.30 0.28 0.36 0.03 0.22 0.25 0.43 0.36 0.37
0.35 -0.49 -0.41 -0.29 0.10 -0.01 -0.13 -0.06 -0.14 -0.14 -0.25 -0.33 -0.06 -0.05 -0.07 -0.18 -0.38 -0.25 -0.30 1.00 -0.43 -0.24 0.16 0.43 -0.22 -0.13 -0.12 0.05
0.13 0.92 0.95 0.90 0.31 -0.00 0.30 0.02 -0.19 -0.36 0.24 0.34 0.28 0.22 0.12 0.24 0.31 0.38 0.28 -0.43 1.00 -0.02 -0.44 0.29 -0.34 0.64 0.58 0.20
0.43 0.30 0.23 0.29 0.47 0.19 0.03 0.03 0.02 0.82 0.34 0.21 0.51 0.37 0.37 0.40 0.21 0.16 0.36 -0.24 -0.02 1.00 0.41 -0.05 0.53 -0.02 -0.01 -0.07
0.41 -0.32 -0.31 -0.15 0.39 -0.15 -0.55 -0.45 -0.42 0.60 0.07 -0.08 0.17 0.16 0.18 0.22 -0.07 -0.08 0.03 0.16 -0.44 0.41 1.00 0.05 0.65 -0.50 -0.59 -0.46
0.78 0.32 0.39 0.47 0.78 0.24 0.24 0.14 -0.10 0.06 0.41 0.39 0.51 0.53 0.43 0.35 0.11 0.43 0.22 0.43 0.29 -0.05 0.05 1.00 -0.48 0.46 0.37 0.30
-0.11 -0.22 -0.25 -0.14 -0.03 -0.02 -0.37 -0.26 -0.16 0.55 0.06 -0.07 0.13 0.10 0.16 0.27 0.13 -0.01 0.25 -0.22 -0.34 0.53 0.65 -0.48 1.00 -0.44 -0.48 -0.35
0.15 0.64 0.67 0.70 0.23 0.71 0.87 0.71 0.46 -0.17 0.61 0.66 0.46 0.48 0.38 0.23 0.33 0.61 0.43 -0.13 0.64 -0.02 -0.50 0.46 -0.44 1.00 0.98 0.83
0.08 0.60 0.62 0.62 0.12 0.73 0.93 0.79 0.57 -0.17 0.53 0.58 0.41 0.43 0.34 0.17 0.28 0.53 0.36 -0.12 0.58 -0.01 -0.59 0.37 -0.48 0.98 1.00 0.87
-0.04 0.23 0.26 0.28 -0.06 0.90 0.97 0.93 0.79 -0.05 0.52 0.53 0.37 0.45 0.40 0.13 0.21 0.50 0.37 0.05 0.20 -0.07 -0.46 0.30 -0.35 0.83 0.87 1.00
Correlation between benchmarks based on ZC proxy values
Figure 7: Pearson correlation coefﬁcient between ZC proxy scores on pairs of benchmarks. The
entries in the plot are ordered based on the mean score across each row and column. This is the full
version of Figure 3.
23
NB101-CF10
NB201-CF10
NB201-IMGNT
TNB101_MICRO-JIGSAW
TNB101_MICRO-OBJECT
TNB101_MICRO-AUTOENC
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MICRO-ROOM
TNB101_MACRO-SCENE
TNB101_MACRO-AUTOENC
NB201-CF100
NB301-CF10
TNB101_MICRO-SCENE
TNB101_MICRO-NORMAL
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
TNB101_MACRO-JIGSAW
TNB101_MICRO-SEGMENT
fisher
grasp
plain
snip
grad_norm
l2_norm
params
jacov
zen
flops
nwot
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.000
0.040
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.040
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.080
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.000
0.040
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.080
0.000
0.000
0.040
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.080
0.000
0.000
0.000
0.040
0.040
0.000
0.000
0.000
0.040
0.000
0.120
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.040
0.080
0.080
0.000
0.040
0.000
0.120
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.040
0.000
0.120
0.040
0.000
0.040
0.160
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.040
0.000
0.000
0.040
0.080
0.080
0.080
0.200
0.040
0.160
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.080
0.000
0.040
0.000
0.080
0.080
0.080
0.120
0.240
0.120
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.040
0.000
0.040
0.000
0.000
0.080
0.200
0.120
0.280
0.080
Precision @ k=5
TNB101_MICRO-AUTOENC
TNB101_MICRO-OBJECT
TNB101_MICRO-JIGSAW
TNB101_MACRO-ROOM
NB101-CF10
TNB101_MICRO-SCENE
TNB101_MICRO-ROOM
NB201-CF10
NB301-CF10
TNB101_MACRO-OBJECT
TNB101_MACRO-SCENE
NB201-CF100
NB201-IMGNT
TNB101_MICRO-NORMAL
TNB101_MACRO-JIGSAW
TNB101_MACRO-SEGMENT
TNB101_MACRO-NORMAL
TNB101_MICRO-SEGMENT
TNB101_MACRO-AUTOENC
fisher
grasp
plain
grad_norm
snip
jacov
l2_norm
params
zen
nwot
flops
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.008
0.032
0.000
0.000
0.008
0.024
0.000
0.000
0.032
0.016
0.000
0.040
0.000
0.016
0.000
0.000
0.000
0.032
0.000
0.024
0.064
0.000
0.000
0.048
0.056
0.016
0.000
0.024
0.032
0.048
0.056
0.032
0.072
0.008
0.008
0.000
0.000
0.320
0.000
0.000
0.024
0.040
0.008
0.008
0.024
0.000
0.024
0.024
0.008
0.056
0.000
0.000
0.000
0.000
0.000
0.008
0.000
0.016
0.024
0.000
0.000
0.032
0.064
0.040
0.000
0.096
0.120
0.128
0.144
0.000
0.000
0.024
0.000
0.000
0.008
0.000
0.016
0.024
0.000
0.000
0.032
0.072
0.040
0.000
0.152
0.128
0.168
0.176
0.016
0.000
0.000
0.056
0.016
0.048
0.024
0.120
0.000
0.088
0.048
0.064
0.032
0.080
0.088
0.048
0.120
0.104
0.168
0.000
0.040
0.072
0.056
0.104
0.120
0.008
0.056
0.096
0.064
0.136
0.152
0.176
0.208
0.064
0.160
0.080
0.216
0.080
0.000
0.040
0.064
0.048
0.040
0.040
0.040
0.096
0.088
0.088
0.168
0.232
0.184
0.176
0.080
0.144
0.088
0.200
0.072
0.000
0.056
0.072
0.088
0.144
0.096
0.016
0.008
0.096
0.096
0.216
0.008
0.008
0.264
0.248
0.216
0.216
0.296
0.152
0.000
0.016
0.032
0.056
0.048
0.024
0.016
0.048
0.112
0.160
0.104
0.144
0.200
0.112
0.416
0.248
0.360
0.208
0.592
0.000
0.040
0.064
0.040
0.040
0.040
0.032
0.088
0.096
0.216
0.256
0.256
0.168
0.192
0.416
0.176
0.368
0.192
0.464
Precision @ k=25
TNB101_MICRO-AUTOENC
TNB101_MICRO-ROOM
NB101-CF10
TNB101_MICRO-OBJECT
TNB101_MACRO-ROOM
TNB101_MICRO-JIGSAW
NB301-CF10
TNB101_MACRO-JIGSAW
TNB101_MACRO-OBJECT
TNB101_MACRO-SCENE
TNB101_MICRO-SCENE
TNB101_MACRO-SEGMENT
TNB101_MICRO-NORMAL
TNB101_MACRO-AUTOENC
NB201-CF10
TNB101_MACRO-NORMAL
NB201-IMGNT
NB201-CF100
TNB101_MICRO-SEGMENT
plain
fisher
grasp
grad_norm
snip
jacov
l2_norm
params
zen
flops
nwot
0.144
0.364
0.008
0.236
0.066
0.178
0.010
0.004
0.054
0.066
0.088
0.106
0.102
0.104
0.010
0.074
0.054
0.032
0.074
0.000
0.056
0.000
0.040
0.050
0.036
0.050
0.018
0.022
0.056
0.126
0.140
0.062
0.104
0.246
0.118
0.306
0.272
0.146
0.012
0.006
0.026
0.046
0.058
0.054
0.188
0.026
0.000
0.002
0.106
0.092
0.098
0.118
0.274
0.080
0.306
0.314
0.118
0.000
0.036
0.000
0.040
0.042
0.042
0.092
0.016
0.000
0.000
0.156
0.176
0.178
0.394
0.280
0.264
0.318
0.302
0.376
0.000
0.038
0.000
0.044
0.054
0.054
0.090
0.020
0.000
0.038
0.170
0.224
0.218
0.310
0.276
0.324
0.328
0.308
0.406
0.080
0.044
0.028
0.088
0.140
0.130
0.048
0.188
0.212
0.160
0.236
0.262
0.246
0.366
0.272
0.304
0.272
0.230
0.226
0.086
0.020
0.292
0.108
0.132
0.140
0.248
0.196
0.150
0.276
0.242
0.236
0.278
0.122
0.330
0.236
0.410
0.398
0.338
0.072
0.050
0.098
0.136
0.122
0.190
0.246
0.182
0.182
0.290
0.296
0.196
0.368
0.124
0.408
0.234
0.294
0.424
0.410
0.078
0.020
0.268
0.154
0.138
0.208
0.218
0.282
0.180
0.302
0.342
0.280
0.420
0.194
0.190
0.374
0.128
0.162
0.456
0.066
0.032
0.096
0.124
0.166
0.188
0.224
0.404
0.516
0.496
0.316
0.302
0.390
0.640
0.406
0.524
0.290
0.422
0.450
0.044
0.024
0.116
0.098
0.178
0.130
0.286
0.462
0.500
0.496
0.252
0.436
0.294
0.534
0.374
0.572
0.500
0.452
0.364
Precision @ k=100
Figure 8: Precision@K between ZC proxy values and validation accuracies, for each ZC proxy and
benchmark. The rows and columns are ordered based on the mean scores across columns and rows,
respectively.
24
TNB101_MACRO-AUTOENC
TNB101_MACRO-SEGMENT
TNB101_MACRO-NORMAL
TNB101_MACRO-JIGSAW
TNB101_MICRO-SEGMENT
TNB101_MACRO-SCENE
NB201-IMGNT
NB201-CF100
TNB101_MICRO-NORMAL
TNB101_MACRO-OBJECT
TNB101_MACRO-ROOM
NB201-CF10
NB301-CF10
TNB101_MICRO-SCENE
TNB101_MICRO-OBJECT
TNB101_MICRO-JIGSAW
NB101-CF10
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
flops
nwot
l2_norm
params
jacov
zen
grasp
plain
snip
grad_norm
fisher
0.025
0.010
0.006
0.003
0.006
0.017
0.083
0.017
0.019
0.025
0.155
0.039
0.067
0.123
0.158
0.124
0.090
0.534
0.444
0.020
0.018
0.004
0.003
0.033
0.051
0.008
0.016
0.046
0.032
0.155
0.036
0.116
0.088
0.284
0.229
0.072
0.404
0.429
0.029
0.011
0.029
0.117
0.019
0.074
0.010
0.025
0.032
0.236
0.056
0.036
0.135
0.082
0.230
0.202
0.050
0.414
0.571
0.153
0.019
0.113
0.118
0.006
0.037
0.048
0.019
0.019
0.125
0.067
0.039
0.130
0.123
0.158
0.124
0.090
0.534
0.444
0.014
0.117
0.100
0.062
0.087
0.047
0.056
0.050
0.016
0.023
0.106
0.100
0.577
0.042
0.195
0.088
0.536
0.323
0.099
0.019
0.006
0.016
0.048
0.005
0.022
0.535
0.563
0.019
0.082
0.044
0.655
0.130
0.042
0.176
0.263
0.050
0.439
0.473
0.216
0.204
0.273
0.156
0.047
0.314
0.194
0.219
0.202
0.386
0.214
0.242
0.212
0.129
0.318
0.372
0.696
0.386
0.530
0.042
0.117
0.245
0.336
0.256
0.248
0.359
0.491
0.234
0.163
0.159
0.447
0.608
0.666
0.179
0.230
0.669
0.009
0.265
0.023
0.021
0.060
0.213
0.072
0.275
0.278
0.244
0.271
0.392
0.389
0.234
0.187
0.532
0.601
0.658
0.697
0.614
0.774
0.024
0.079
0.078
0.177
0.032
0.275
0.247
0.230
0.313
0.391
0.431
0.265
0.296
0.530
0.642
0.646
0.662
0.609
0.757
0.227
0.245
0.155
0.195
0.874
0.292
0.247
0.227
0.968
0.431
0.528
0.242
0.122
0.589
0.644
0.667
0.783
0.611
0.967
Best ranking @ k=5
TNB101_MACRO-AUTOENC
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
TNB101_MACRO-ROOM
TNB101_MICRO-SCENE
NB301-CF10
NB201-IMGNT
NB201-CF100
TNB101_MACRO-JIGSAW
NB201-CF10
TNB101_MACRO-SCENE
TNB101_MICRO-JIGSAW
TNB101_MICRO-SEGMENT
TNB101_MACRO-OBJECT
TNB101_MICRO-NORMAL
TNB101_MICRO-OBJECT
NB101-CF10
TNB101_MICRO-ROOM
TNB101_MICRO-AUTOENC
flops
params
l2_norm
jacov
nwot
zen
plain
grasp
snip
grad_norm
fisher
0.002
0.001
0.005
0.018
0.012
0.005
0.005
0.003
0.001
0.009
0.002
0.016
0.004
0.005
0.004
0.030
0.028
0.120
0.139
0.012
0.004
0.008
0.009
0.012
0.005
0.004
0.003
0.012
0.009
0.002
0.016
0.004
0.010
0.004
0.030
0.028
0.120
0.139
0.012
0.009
0.006
0.009
0.008
0.006
0.007
0.007
0.034
0.018
0.003
0.017
0.002
0.036
0.003
0.049
0.009
0.230
0.049
0.005
0.009
0.014
0.025
0.016
0.135
0.020
0.010
0.031
0.008
0.014
0.044
0.007
0.013
0.016
0.040
0.059
0.096
0.038
0.001
0.001
0.002
0.019
0.030
0.004
0.006
0.006
0.001
0.022
0.005
0.065
0.002
0.006
0.007
0.076
0.022
0.173
0.283
0.010
0.002
0.004
0.004
0.003
0.002
0.359
0.365
0.002
0.473
0.003
0.014
0.002
0.014
0.002
0.053
0.007
0.270
0.135
0.023
0.026
0.037
0.057
0.127
0.307
0.088
0.143
0.144
0.166
0.067
0.074
0.083
0.073
0.035
0.009
0.342
0.004
0.024
0.014
0.049
0.052
0.084
0.033
0.006
0.015
0.020
0.126
0.032
0.223
0.120
0.032
0.282
0.061
0.125
0.274
0.214
0.457
0.007
0.009
0.009
0.071
0.055
0.041
0.011
0.020
0.101
0.033
0.218
0.167
0.003
0.225
0.040
0.257
0.342
0.441
0.455
0.006
0.003
0.014
0.068
0.055
0.049
0.020
0.021
0.103
0.035
0.218
0.200
0.014
0.259
0.040
0.271
0.401
0.326
0.426
0.040
0.050
0.034
0.101
0.133
0.034
0.062
0.070
0.112
0.066
0.191
0.237
0.871
0.247
0.963
0.253
0.415
0.360
0.962
Best ranking @ k=25
TNB101_MICRO-SEGMENT
TNB101_MACRO-NORMAL
TNB101_MACRO-SEGMENT
NB201-IMGNT
TNB101_MACRO-AUTOENC
TNB101_MICRO-SCENE
NB201-CF100
TNB101_MICRO-NORMAL
TNB101_MACRO-ROOM
TNB101_MICRO-JIGSAW
TNB101_MICRO-OBJECT
NB301-CF10
TNB101_MICRO-ROOM
NB201-CF10
TNB101_MACRO-SCENE
TNB101_MACRO-JIGSAW
TNB101_MACRO-OBJECT
NB101-CF10
TNB101_MICRO-AUTOENC
flops
params
l2_norm
zen
nwot
jacov
plain
grasp
fisher
snip
grad_norm
0.001
0.001
0.002
0.001
0.001
0.003
0.001
0.002
0.004
0.004
0.005
0.002
0.007
0.002
0.001
0.001
0.002
0.017
0.010
0.001
0.002
0.004
0.001
0.003
0.003
0.001
0.001
0.003
0.004
0.004
0.002
0.005
0.002
0.001
0.003
0.003
0.017
0.010
0.002
0.002
0.003
0.002
0.008
0.004
0.003
0.003
0.003
0.014
0.009
0.002
0.005
0.005
0.001
0.002
0.008
0.003
0.010
0.001
0.001
0.002
0.002
0.005
0.002
0.001
0.002
0.004
0.005
0.006
0.002
0.035
0.003
0.001
0.001
0.004
0.003
0.013
0.002
0.001
0.002
0.001
0.001
0.002
0.003
0.002
0.004
0.010
0.011
0.001
0.005
0.008
0.001
0.001
0.002
0.018
0.046
0.002
0.003
0.003
0.003
0.003
0.005
0.003
0.002
0.008
0.007
0.027
0.011
0.016
0.002
0.006
0.009
0.005
0.040
0.009
0.008
0.012
0.006
0.027
0.008
0.019
0.043
0.012
0.023
0.003
0.002
0.104
0.003
0.100
0.013
0.114
0.010
0.121
0.008
0.004
0.003
0.011
0.003
0.010
0.003
0.007
0.026
0.019
0.021
0.014
0.005
0.100
0.021
0.129
0.056
0.225
0.042
0.086
0.003
0.007
0.009
0.003
0.009
0.016
0.007
0.023
0.017
0.026
0.013
0.017
0.007
0.024
0.004
0.053
0.047
0.179
0.420
0.002
0.002
0.004
0.002
0.001
0.009
0.006
0.004
0.017
0.017
0.023
0.010
0.005
0.021
0.022
0.043
0.197
0.164
0.357
0.002
0.002
0.002
0.002
0.001
0.008
0.006
0.005
0.024
0.023
0.023
0.008
0.008
0.021
0.155
0.053
0.225
0.164
0.348
Best ranking @ k=100
Figure 9: BestRanking@K between ZC proxy values and validation accuracies, for each ZC proxy
and benchmark. The rows and columns are ordered based on the mean scores across columns and
rows, respectively.
25
plain
grasp
nwot
flops
zen
jacov
epe_nas
synflow
l2_norm
fisher
params
grad_norm
snip
plain
grasp
nwot
flops
zen
jacov
epe_nas
synflow
l2_norm
fisher
params
grad_norm
snip
1.00
-0.44
-0.46
-0.34
0.15
0.12
-0.00
-0.12
-0.25
0.19
-0.15
0.13
0.16
-0.44
1.00
0.06
-0.00
0.02
0.12
0.34
0.29
0.53
0.24
0.36
0.41
0.33
-0.46
0.06
1.00
0.94
0.21
0.43
0.36
0.39
0.46
0.33
0.49
0.34
0.39
-0.34
-0.00
0.94
1.00
0.40
0.49
0.39
0.45
0.53
0.43
0.62
0.48
0.53
0.15
0.02
0.21
0.40
1.00
0.32
0.30
0.52
0.72
0.53
0.77
0.59
0.64
0.12
0.12
0.43
0.49
0.32
1.00
0.68
0.42
0.40
0.67
0.53
0.72
0.76
-0.00
0.34
0.36
0.39
0.30
0.68
1.00
0.80
0.62
0.77
0.66
0.68
0.69
-0.12
0.29
0.39
0.45
0.52
0.42
0.80
1.00
0.75
0.81
0.77
0.67
0.67
-0.25
0.53
0.46
0.53
0.72
0.40
0.62
0.75
1.00
0.66
0.95
0.69
0.72
0.19
0.24
0.33
0.43
0.53
0.67
0.77
0.81
0.66
1.00
0.74
0.89
0.91
-0.15
0.36
0.49
0.62
0.77
0.53
0.66
0.77
0.95
0.74
1.00
0.76
0.80
0.13
0.41
0.34
0.48
0.59
0.72
0.68
0.67
0.69
0.89
0.76
1.00
0.99
0.16
0.33
0.39
0.53
0.64
0.76
0.69
0.67
0.72
0.91
0.80
0.99
1.00
Pairwise correlations of ZC proxies
Figure 10: Pearson correlation coefﬁcient for each pair of ZC proxies, averaged over all benchmarks.
The entries in the plot are ordered based on the mean score across each row and column.
26
zen
l2_norm
nwot
synflow
jacov
epe_nas
params
flops
plain
grad_normsnip
fisher
grasp
zen
l2_norm
nwot
synflow
jacov
epe_nas
params
flops
plain
grad_norm
snip
fisher
grasp
1.09
0.82
0.77
0.74
0.74
0.74
0.90
0.90
0.82
0.77
0.79
0.99
1.02
0.82
1.13
0.93
0.78
0.77
0.79
0.91
0.90
0.87
0.87
0.89
1.05
1.07
0.77
0.93
1.18
0.77
0.77
0.82
0.90
0.91
0.90
0.91
0.94
1.10
1.12
0.74
0.78
0.77
1.23
0.85
0.83
0.95
0.95
0.95
0.90
0.95
1.14
1.16
0.74
0.77
0.77
0.85
1.30
0.94
0.93
0.92
1.01
1.03
1.08
1.22
1.23
0.74
0.79
0.82
0.83
0.94
1.34
0.94
0.94
1.02
1.10
1.13
1.26
1.28
0.90
0.91
0.90
0.95
0.93
0.94
1.23
1.21
0.98
0.94
0.95
1.14
1.16
0.90
0.90
0.91
0.95
0.92
0.94
1.21
1.22
0.98
0.94
0.95
1.14
1.16
0.82
0.87
0.90
0.95
1.01
1.02
0.98
0.98
1.30
1.09
1.12
1.23
1.24
0.77
0.87
0.91
0.90
1.03
1.10
0.94
0.94
1.09
1.30
1.24
1.29
1.27
0.79
0.89
0.94
0.95
1.08
1.13
0.95
0.95
1.12
1.24
1.33
1.30
1.29
0.99
1.05
1.10
1.14
1.22
1.26
1.14
1.14
1.23
1.29
1.30
1.36
1.34
1.02
1.07
1.12
1.16
1.23
1.28
1.16
1.16
1.24
1.27
1.29
1.34
1.37
Pairwise conditional entropy on NB101-CF10
zen
l2_norm
nwot
synflow
jacov
epe_nas
params
flops
plain
grad_normsnip
fisher
grasp
zen
l2_norm
nwot
synflow
jacov
epe_nas
params
flops
plain
grad_norm
snip
fisher
grasp
-0.00
0.27
0.32
0.35
0.35
0.35
0.19
0.19
0.27
0.31
0.29
0.10
0.07
0.31
0.00
0.20
0.35
0.35
0.34
0.22
0.22
0.25
0.26
0.23
0.08
0.06
0.41
0.25
0.00
0.41
0.41
0.36
0.28
0.27
0.28
0.26
0.23
0.08
0.06
0.49
0.45
0.46
0.00
0.38
0.40
0.28
0.28
0.28
0.33
0.28
0.09
0.07
0.56
0.53
0.53
0.45
-0.00
0.36
0.37
0.37
0.29
0.27
0.22
0.08
0.07
0.60
0.55
0.52
0.51
0.40
0.00
0.40
0.39
0.31
0.24
0.21
0.07
0.06
0.32
0.32
0.32
0.27
0.30
0.29
-0.00
0.02
0.25
0.29
0.27
0.09
0.07
0.32
0.32
0.31
0.28
0.30
0.28
0.01
-0.00
0.25
0.29
0.27
0.09
0.07
0.48
0.42
0.39
0.35
0.29
0.27
0.32
0.32
0.00
0.21
0.17
0.07
0.05
0.53
0.43
0.39
0.40
0.27
0.20
0.36
0.36
0.21
-0.00
0.06
0.01
0.03
0.53
0.43
0.38
0.38
0.25
0.20
0.37
0.37
0.21
0.09
-0.00
0.02
0.04
0.37
0.31
0.26
0.23
0.15
0.10
0.23
0.23
0.14
0.07
0.06
0.00
0.03
0.35
0.30
0.25
0.21
0.14
0.09
0.21
0.21
0.13
0.10
0.08
0.03
0.00
Information gain on NB101-CF10
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Conditional entropy
NB101-CF10
random ordering
greedy ordering
minimum k-tuple
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
1.39
1.07
1.06
1.11
0.93
1.27
1.28
1.39
1.39
1.39
1.39
1.36
1.37
1.07
1.63
1.50
1.56
1.17
1.54
1.54
1.50
1.50
1.50
1.55
1.60
1.60
1.06
1.50
1.69
1.41
1.18
1.59
1.60
1.56
1.56
1.56
1.62
1.66
1.67
1.11
1.56
1.41
1.70
1.21
1.60
1.61
1.58
1.58
1.58
1.63
1.68
1.68
0.93
1.17
1.18
1.21
1.91
1.67
1.70
1.85
1.85
1.85
1.88
1.87
1.88
1.27
1.54
1.59
1.60
1.67
2.03
1.99
1.89
1.89
1.89
1.94
2.01
2.01
1.28
1.54
1.60
1.61
1.70
1.99
2.04
1.90
1.90
1.90
1.96
2.02
2.02
1.39
1.50
1.56
1.58
1.85
1.89
1.90
2.04
2.04
2.04
2.04
2.02
2.03
1.39
1.50
1.56
1.58
1.85
1.89
1.90
2.04
2.04
2.04
2.04
2.02
2.03
1.39
1.50
1.56
1.58
1.85
1.89
1.90
2.04
2.04
2.04
2.04
2.02
2.03
1.39
1.55
1.62
1.63
1.88
1.94
1.96
2.04
2.04
2.04
2.11
2.09
2.09
1.36
1.60
1.66
1.68
1.87
2.01
2.02
2.02
2.02
2.02
2.09
2.18
2.16
1.37
1.60
1.67
1.68
1.88
2.01
2.02
2.03
2.03
2.03
2.09
2.16
2.18
Pairwise conditional entropy on NB201-CF10
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
-0.00
0.32
0.34
0.28
0.46
0.12
0.12
-0.00 -0.00 -0.00 -0.00
0.03
0.02
0.56
0.00
0.13
0.06
0.45
0.09
0.08
0.13
0.13
0.13
0.07
0.03
0.02
0.64
0.19
-0.00
0.28
0.51
0.10
0.09
0.13
0.13
0.13
0.08
0.03
0.02
0.59
0.14
0.30
-0.00
0.49
0.10
0.10
0.12
0.12
0.12
0.07
0.03
0.02
0.98
0.74
0.73
0.70
0.00
0.24
0.21
0.06
0.06
0.06
0.03
0.04
0.04
0.76
0.49
0.44
0.43
0.35
0.00
0.03
0.14
0.14
0.14
0.08
0.02
0.02
0.77
0.50
0.44
0.44
0.35
0.05
-0.00
0.15
0.15
0.15
0.09
0.02
0.02
0.65
0.55
0.48
0.46
0.19
0.16
0.15
0.00
0.00
0.00
-0.00
0.02
0.02
0.65
0.55
0.48
0.46
0.19
0.16
0.15
0.00
0.00
0.00
-0.00
0.02
0.02
0.65
0.55
0.48
0.46
0.19
0.16
0.15
0.00
0.00
0.00
-0.00
0.02
0.02
0.72
0.56
0.49
0.47
0.22
0.16
0.15
0.06
0.06
0.06
0.00
0.02
0.02
0.81
0.58
0.51
0.50
0.30
0.16
0.15
0.15
0.15
0.15
0.09
-0.00
0.02
0.81
0.58
0.51
0.50
0.30
0.17
0.15
0.15
0.15
0.15
0.09
0.02
0.00
Information gain on NB201-CF10
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.25
Conditional entropy
NB201-CF10
random ordering
greedy ordering
minimum k-tuple
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
1.89
1.52
1.48
1.54
1.28
1.66
1.67
1.89
1.89
1.89
1.89
1.83
1.84
1.52
2.32
2.14
2.23
1.69
2.12
2.13
2.19
2.19
2.19
2.24
2.26
2.27
1.48
2.14
2.37
2.02
1.71
2.18
2.18
2.24
2.24
2.24
2.29
2.31
2.32
1.54
2.23
2.02
2.38
1.71
2.18
2.18
2.26
2.26
2.26
2.31
2.33
2.33
1.28
1.69
1.71
1.71
2.66
2.28
2.31
2.60
2.60
2.60
2.63
2.60
2.60
1.66
2.12
2.18
2.18
2.28
2.74
2.66
2.59
2.59
2.59
2.65
2.70
2.70
1.67
2.13
2.18
2.18
2.31
2.66
2.75
2.61
2.61
2.61
2.67
2.72
2.72
1.89
2.19
2.24
2.26
2.60
2.59
2.61
2.82
2.82
2.82
2.82
2.78
2.78
1.89
2.19
2.24
2.26
2.60
2.59
2.61
2.82
2.82
2.82
2.82
2.78
2.78
1.89
2.19
2.24
2.26
2.60
2.59
2.61
2.82
2.82
2.82
2.82
2.78
2.78
1.89
2.24
2.29
2.31
2.63
2.65
2.67
2.82
2.82
2.82
2.88
2.85
2.84
1.83
2.26
2.31
2.33
2.60
2.70
2.72
2.78
2.78
2.78
2.85
2.94
2.91
1.84
2.27
2.32
2.33
2.60
2.70
2.72
2.78
2.78
2.78
2.84
2.91
2.94
Pairwise conditional entropy on NB201-CF100
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
nwot
fisher
grasp
0.00
0.37
0.40
0.35
0.60
0.23
0.21
0.00
0.00
0.00
0.00
0.06
0.05
0.80
-0.00
0.18
0.09
0.63
0.19
0.19
0.13
0.13
0.13
0.07
0.06
0.05
0.88
0.23
0.00
0.34
0.65
0.19
0.18
0.13
0.13
0.13
0.07
0.06
0.05
0.85
0.15
0.36
-0.00
0.67
0.20
0.20
0.12
0.12
0.12
0.07
0.05
0.05
1.38
0.97
0.95
0.95
-0.00
0.38
0.35
0.07
0.07
0.07
0.03
0.06
0.06
1.08
0.61
0.56
0.56
0.46
-0.00
0.07
0.14
0.14
0.14
0.08
0.03
0.03
1.08
0.62
0.57
0.57
0.44
0.09
0.00
0.15
0.15
0.15
0.09
0.03
0.03
0.93
0.63
0.58
0.56
0.22
0.22
0.21
0.00
0.00
0.00
0.00
0.03
0.04
0.93
0.63
0.58
0.56
0.22
0.22
0.21
0.00
0.00
0.00
0.00
0.03
0.04
0.93
0.63
0.58
0.56
0.22
0.22
0.21
0.00
0.00
0.00
0.00
0.03
0.04
0.99
0.64
0.59
0.57
0.25
0.23
0.21
0.06
0.06
0.06
0.00
0.03
0.04
1.11
0.68
0.63
0.61
0.34
0.23
0.21
0.15
0.15
0.15
0.09
-0.00
0.03
1.09
0.67
0.62
0.60
0.33
0.23
0.21
0.15
0.15
0.15
0.09
0.03
0.00
Information gain on NB201-CF100
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
NB201-CF100
random ordering
greedy ordering
minimum k-tuple
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
fisher
grasp
nwot
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
fisher
grasp
nwot
2.70
2.09
2.06
2.11
1.84
2.22
2.31
2.70
2.70
2.70
2.59
2.61
2.70
2.09
3.17
2.90
3.05
2.35
2.74
2.80
3.04
3.04
3.04
3.05
3.08
3.09
2.06
2.90
3.22
2.75
2.39
2.82
2.89
3.09
3.09
3.09
3.10
3.14
3.15
2.11
3.05
2.75
3.23
2.37
2.79
2.85
3.10
3.10
3.10
3.11
3.14
3.16
1.84
2.35
2.39
2.37
3.50
2.91
3.01
3.43
3.43
3.43
3.39
3.41
3.46
2.22
2.74
2.82
2.79
2.91
3.53
3.40
3.38
3.38
3.38
3.48
3.48
3.44
2.31
2.80
2.89
2.85
3.01
3.40
3.58
3.43
3.43
3.43
3.53
3.53
3.49
2.70
3.04
3.09
3.10
3.43
3.38
3.43
3.72
3.72
3.72
3.65
3.66
3.72
2.70
3.04
3.09
3.10
3.43
3.38
3.43
3.72
3.72
3.72
3.65
3.66
3.72
2.70
3.04
3.09
3.10
3.43
3.38
3.43
3.72
3.72
3.72
3.65
3.66
3.72
2.59
3.05
3.10
3.11
3.39
3.48
3.53
3.65
3.65
3.65
3.81
3.76
3.72
2.61
3.08
3.14
3.14
3.41
3.48
3.53
3.66
3.66
3.66
3.76
3.81
3.72
2.70
3.09
3.15
3.16
3.46
3.44
3.49
3.72
3.72
3.72
3.72
3.72
3.78
Pairwise conditional entropy on NB201-IMGNT
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
fisher
grasp
nwot
synflow
params
l2_norm
flops
plain
snip
grad_norm
jacov
zen
epe_nas
fisher
grasp
nwot
-0.00
0.62
0.65
0.59
0.87
0.48
0.39
-0.00 -0.00 -0.00
0.12
0.09
-0.00
1.08
-0.00
0.27
0.11
0.82
0.43
0.37
0.13
0.13
0.13
0.12
0.09
0.07
1.16
0.32
-0.00
0.47
0.82
0.40
0.33
0.13
0.13
0.13
0.12
0.08
0.07
1.12
0.17
0.48
-0.00
0.85
0.44
0.38
0.12
0.12
0.12
0.12
0.09
0.07
1.66
1.16
1.11
1.13
-0.00
0.59
0.49
0.07
0.07
0.07
0.11
0.09
0.04
1.30
0.79
0.70
0.74
0.62
0.00
0.12
0.14
0.14
0.14
0.05
0.05
0.08
1.27
0.78
0.69
0.73
0.57
0.17
0.00
0.15
0.15
0.15
0.05
0.04
0.09
1.02
0.68
0.63
0.61
0.29
0.34
0.29
0.00
0.00
0.00
0.06
0.06
-0.00
1.02
0.68
0.63
0.61
0.29
0.34
0.29
0.00
0.00
0.00
0.06
0.06
-0.00
1.02
0.68
0.63
0.61
0.29
0.34
0.29
0.00
0.00
0.00
0.06
0.06
-0.00
1.22
0.76
0.71
0.70
0.41
0.33
0.28
0.15
0.15
0.15
0.00
0.05
0.09
1.20
0.74
0.68
0.68
0.40
0.34
0.28
0.15
0.15
0.15
0.05
-0.00
0.09
1.08
0.69
0.64
0.63
0.32
0.34
0.29
0.06
0.06
0.06
0.06
0.06
0.00
Information gain on NB201-IMGNT
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Conditional entropy
NB201-IMGNT
random ordering
greedy ordering
minimum k-tuple
Figure 11: Conditional entropy and information gain (IG) for each ZC proxy pair across all search
spaces and datasets (Left and Middle). Conditional entropy H(y | zi1, . . . , zik) vs. k, where the
ordering zi1, . . . , zik is selected using three different strategies (Right). (1/5)
27
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
3.42
1.98
2.10
1.90
1.84
1.85
1.87
1.86
2.21
2.21
2.52
2.55
2.83
1.98
3.40
2.17
2.05
2.10
2.08
2.08
2.09
2.36
2.38
2.55
2.58
2.87
2.10
2.17
3.37
2.14
2.12
2.11
2.14
2.15
2.33
2.32
2.64
2.65
2.92
1.90
2.05
2.14
3.24
2.51
2.55
2.67
2.63
2.16
2.17
2.40
2.48
2.74
1.84
2.10
2.12
2.51
3.25
2.92
2.82
2.88
2.16
2.17
2.39
2.46
2.73
1.85
2.08
2.11
2.55
2.92
3.26
2.82
2.85
2.15
2.16
2.39
2.48
2.74
1.87
2.08
2.14
2.67
2.82
2.82
3.25
2.94
2.17
2.18
2.40
2.48
2.74
1.86
2.09
2.15
2.63
2.88
2.85
2.94
3.24
2.16
2.16
2.40
2.47
2.74
2.21
2.36
2.33
2.16
2.16
2.15
2.17
2.16
3.46
3.03
2.85
2.73
2.97
2.21
2.38
2.32
2.17
2.17
2.16
2.18
2.16
3.03
3.46
2.86
2.73
2.97
2.52
2.55
2.64
2.40
2.39
2.39
2.40
2.40
2.85
2.86
3.44
2.93
3.07
2.55
2.58
2.65
2.48
2.46
2.48
2.48
2.47
2.73
2.73
2.93
3.43
3.10
2.83
2.87
2.92
2.74
2.73
2.74
2.74
2.74
2.97
2.97
3.07
3.10
3.57
Pairwise conditional entropy on NB301-CF10
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
epe_nas
synflow
plain
nwot
zen
flops
l2_norm
params
snip
grad_norm
fisher
grasp
jacov
-0.00
1.44
1.31
1.52
1.57
1.56
1.54
1.55
1.20
1.20
0.90
0.87
0.59
1.42
-0.00
1.23
1.35
1.30
1.31
1.31
1.31
1.04
1.02
0.84
0.82
0.53
1.26
1.20
-0.00
1.23
1.25
1.25
1.23
1.22
1.04
1.04
0.72
0.71
0.45
1.34
1.19
1.10
0.00
0.73
0.69
0.57
0.61
1.08
1.07
0.83
0.76
0.50
1.40
1.15
1.13
0.74
-0.00
0.33
0.43
0.37
1.08
1.08
0.85
0.79
0.52
1.41
1.18
1.14
0.71
0.34
-0.00
0.44
0.41
1.11
1.10
0.87
0.78
0.52
1.38
1.17
1.11
0.59
0.43
0.43
-0.00
0.31
1.09
1.07
0.85
0.77
0.51
1.38
1.15
1.10
0.61
0.36
0.40
0.30
-0.00
1.09
1.08
0.84
0.78
0.50
1.25
1.10
1.13
1.30
1.29
1.31
1.29
1.30
-0.00
0.43
0.60
0.73
0.48
1.24
1.08
1.13
1.29
1.29
1.30
1.27
1.29
0.43
-0.00
0.60
0.72
0.48
0.93
0.89
0.80
1.04
1.05
1.05
1.04
1.04
0.59
0.59
0.00
0.51
0.37
0.88
0.85
0.78
0.96
0.97
0.96
0.95
0.97
0.70
0.70
0.50
-0.00
0.33
0.75
0.70
0.66
0.84
0.85
0.83
0.83
0.83
0.60
0.60
0.50
0.47
0.00
Information gain on NB301-CF10
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Conditional entropy
NB301-CF10
random ordering
greedy ordering
minimum k-tuple
nwot
plain
l2_norm
zen
jacov
params
grad_norm
snip
fisher
flops
grasp
nwot
plain
l2_norm
zen
jacov
params
grad_norm
snip
fisher
flops
grasp
3.30
1.69
1.45
1.58
1.96
1.61
1.93
1.90
1.98
2.63
2.61
1.69
3.69
1.72
1.73
1.94
1.89
2.07
2.02
2.32
2.40
2.97
1.45
1.72
3.62
2.15
1.75
2.69
1.92
2.05
2.22
2.20
2.82
1.58
1.73
2.15
3.66
1.81
2.12
1.99
2.15
2.24
2.30
2.86
1.96
1.94
1.75
1.81
3.58
1.92
2.09
2.08
2.26
2.53
2.90
1.61
1.89
2.69
2.12
1.92
3.68
2.05
2.18
2.33
2.29
2.91
1.93
2.07
1.92
1.99
2.09
2.05
3.62
2.63
2.47
2.53
2.96
1.90
2.02
2.05
2.15
2.08
2.18
2.63
3.65
2.52
2.47
2.98
1.98
2.32
2.22
2.24
2.26
2.33
2.47
2.52
3.76
2.50
3.16
2.63
2.40
2.20
2.30
2.53
2.29
2.53
2.47
2.50
3.23
2.86
2.61
2.97
2.82
2.86
2.90
2.91
2.96
2.98
3.16
2.86
3.88
Pairwise conditional entropy on TNB101_MACRO-AUTOENC
nwot
plain
l2_norm
zen
jacov
params
grad_norm
snip
fisher
flops
grasp
nwot
plain
l2_norm
zen
jacov
params
grad_norm
snip
fisher
flops
grasp
0.00
1.62
1.86
1.72
1.35
1.69
1.37
1.40
1.32
0.67
0.69
2.01
0.00
1.98
1.96
1.75
1.81
1.62
1.67
1.37
1.29
0.73
2.18
1.91
-0.00
1.48
1.88
0.93
1.71
1.58
1.41
1.43
0.81
2.08
1.93
1.51
0.00
1.85
1.54
1.67
1.51
1.42
1.36
0.80
1.63
1.64
1.83
1.78
0.00
1.66
1.49
1.50
1.32
1.05
0.69
2.07
1.79
0.99
1.57
1.76
0.00
1.63
1.50
1.35
1.39
0.77
1.70
1.55
1.71
1.64
1.53
1.57
0.00
0.99
1.15
1.10
0.66
1.75
1.63
1.60
1.50
1.57
1.47
1.02
0.00
1.13
1.18
0.68
1.78
1.44
1.54
1.52
1.50
1.43
1.29
1.24
0.00
1.26
0.60
0.60
0.83
1.04
0.93
0.70
0.94
0.71
0.76
0.74
0.00
0.37
1.27
0.92
1.07
1.02
0.99
0.98
0.92
0.91
0.73
1.02
0.00
Information gain on TNB101_MACRO-AUTOENC
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Conditional entropy
TNB101_MACRO-AUTOENC
random ordering
greedy ordering
minimum k-tuple
nwot
zen
l2_norm
plain
grad_norm
params
snip
fisher
grasp
flops
jacov
nwot
zen
l2_norm
plain
grad_norm
params
snip
fisher
grasp
flops
jacov
3.17
1.46
1.43
1.76
1.62
1.62
1.78
1.89
2.29
2.85
2.57
1.46
3.83
2.67
1.99
1.95
2.56
2.25
2.38
2.64
2.80
3.13
1.43
2.67
3.82
1.97
1.98
2.80
2.36
2.45
2.62
2.78
3.12
1.76
1.99
1.97
3.90
2.21
2.18
2.43
2.59
2.86
2.98
3.22
1.62
1.95
1.98
2.21
3.66
2.05
2.87
2.84
3.18
2.80
3.10
1.62
2.56
2.80
2.18
2.05
3.85
2.38
2.53
2.68
2.88
3.19
1.78
2.25
2.36
2.43
2.87
2.38
3.84
3.19
3.12
2.89
3.33
1.89
2.38
2.45
2.59
2.84
2.53
3.19
3.88
3.15
2.95
3.37
2.29
2.64
2.62
2.86
3.18
2.68
3.12
3.15
3.76
3.12
3.44
2.85
2.80
2.78
2.98
2.80
2.88
2.89
2.95
3.12
3.69
3.35
2.57
3.13
3.12
3.22
3.10
3.19
3.33
3.37
3.44
3.35
4.07
Pairwise conditional entropy on TNB101_MACRO-OBJECT
nwot
zen
l2_norm
plain
grad_norm
params
snip
fisher
grasp
flops
jacov
nwot
zen
l2_norm
plain
grad_norm
params
snip
fisher
grasp
flops
jacov
0.00
1.71
1.74
1.40
1.54
1.55
1.39
1.27
0.88
0.32
0.60
2.37
0.00
1.16
1.84
1.88
1.27
1.58
1.44
1.19
1.03
0.70
2.39
1.15
-0.00
1.85
1.84
1.02
1.46
1.37
1.20
1.03
0.70
2.14
1.91
1.93
-0.00
1.69
1.72
1.47
1.31
1.04
0.92
0.68
2.04
1.71
1.69
1.45
-0.00
1.61
0.79
0.83
0.49
0.86
0.56
2.24
1.30
1.05
1.67
1.80
0.00
1.47
1.32
1.18
0.97
0.66
2.07
1.60
1.49
1.42
0.98
1.46
-0.00
0.65
0.73
0.96
0.51
1.99
1.50
1.44
1.30
1.05
1.35
0.69
-0.00
0.74
0.93
0.51
1.48
1.12
1.14
0.90
0.59
1.09
0.65
0.62
0.00
0.65
0.32
0.84
0.89
0.90
0.71
0.88
0.81
0.80
0.73
0.57
-0.00
0.33
1.50
0.94
0.95
0.85
0.97
0.87
0.74
0.69
0.62
0.71
-0.00
Information gain on TNB101_MACRO-OBJECT
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Conditional entropy
TNB101_MACRO-OBJECT
random ordering
greedy ordering
minimum k-tuple
nwot
plain
zen
l2_norm
grad_norm
params
snip
fisher
flops
grasp
jacov
nwot
plain
zen
l2_norm
grad_norm
params
snip
fisher
flops
grasp
jacov
2.83
1.58
1.36
1.35
1.49
1.51
1.61
1.74
2.55
2.17
2.32
1.58
3.82
1.85
1.85
2.05
2.04
2.29
2.40
2.86
2.81
3.21
1.36
1.85
3.73
2.62
1.89
2.51
2.20
2.27
2.77
2.61
3.11
1.35
1.85
2.62
3.71
1.88
2.75
2.31
2.32
2.78
2.54
3.12
1.49
2.05
1.89
1.88
3.65
2.01
2.75
2.81
2.79
3.13
3.15
1.51
2.04
2.51
2.75
2.01
3.76
2.36
2.41
2.86
2.62
3.21
1.61
2.29
2.20
2.31
2.75
2.36
3.79
3.09
2.88
3.02
3.32
1.74
2.40
2.27
2.32
2.81
2.41
3.09
3.81
2.93
3.10
3.37
2.55
2.86
2.77
2.78
2.79
2.86
2.88
2.93
3.56
3.14
3.29
2.17
2.81
2.61
2.54
3.13
2.62
3.02
3.10
3.14
3.84
3.51
2.32
3.21
3.11
3.12
3.15
3.21
3.32
3.37
3.29
3.51
4.05
Pairwise conditional entropy on TNB101_MACRO-SCENE
nwot
plain
zen
l2_norm
grad_norm
params
snip
fisher
flops
grasp
jacov
nwot
plain
zen
l2_norm
grad_norm
params
snip
fisher
flops
grasp
jacov
0.00
1.25
1.48
1.48
1.34
1.32
1.23
1.09
0.29
0.66
0.52
2.24
0.00
1.97
1.97
1.76
1.78
1.53
1.42
0.95
1.01
0.61
2.37
1.88
0.00
1.11
1.83
1.22
1.53
1.45
0.95
1.12
0.61
2.36
1.86
1.09
0.00
1.83
0.96
1.40
1.39
0.93
1.17
0.59
2.17
1.60
1.76
1.77
0.00
1.65
0.90
0.84
0.86
0.52
0.51
2.25
1.72
1.25
1.01
1.75
0.00
1.40
1.35
0.90
1.13
0.55
2.18
1.50
1.59
1.48
1.04
1.43
-0.00
0.70
0.91
0.77
0.47
2.07
1.41
1.54
1.49
0.99
1.40
0.72
-0.00
0.87
0.71
0.44
1.02
0.70
0.79
0.78
0.77
0.71
0.69
0.63
-0.00
0.42
0.27
1.67
1.03
1.23
1.30
0.71
1.21
0.81
0.74
0.70
-0.00
0.32
1.73
0.84
0.93
0.93
0.90
0.83
0.73
0.68
0.75
0.53
0.00
Information gain on TNB101_MACRO-SCENE
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Conditional entropy
TNB101_MACRO-SCENE
random ordering
greedy ordering
minimum k-tuple
Figure 12: Conditional entropy and information gain (IG) for each ZC proxy pair across all search
spaces and datasets (Left and Middle). Conditional entropy H(y | zi1, . . . , zik) vs. k, where the
ordering zi1, . . . , zik is selected using three different strategies (Right). (2/5)
28
nwot
zen
l2_norm
params
grad_norm
plain
snip
fisher
jacov
flops
grasp
nwot
zen
l2_norm
params
grad_norm
plain
snip
fisher
jacov
flops
grasp
2.78
1.43
1.35
1.50
1.66
1.84
1.75
2.15
2.16
2.50
2.36
1.43
3.24
2.05
1.98
1.93
1.99
2.08
2.46
2.52
2.64
2.65
1.35
2.05
3.27
2.45
1.99
1.96
2.23
2.46
2.54
2.57
2.67
1.50
1.98
2.45
3.33
2.02
2.10
2.23
2.48
2.64
2.64
2.72
1.66
1.93
1.99
2.02
3.22
2.45
2.69
2.94
2.63
2.69
2.91
1.84
1.99
1.96
2.10
2.45
3.27
2.48
2.73
2.70
2.79
2.87
1.75
2.08
2.23
2.23
2.69
2.48
3.32
2.81
2.77
2.76
2.95
2.15
2.46
2.46
2.48
2.94
2.73
2.81
3.28
2.89
2.90
2.98
2.16
2.52
2.54
2.64
2.63
2.70
2.77
2.89
3.40
2.92
3.06
2.50
2.64
2.57
2.64
2.69
2.79
2.76
2.90
2.92
3.25
3.02
2.36
2.65
2.67
2.72
2.91
2.87
2.95
2.98
3.06
3.02
3.40
Pairwise conditional entropy on TNB101_MACRO-JIGSAW
nwot
zen
l2_norm
params
grad_norm
plain
snip
fisher
jacov
flops
grasp
nwot
zen
l2_norm
params
grad_norm
plain
snip
fisher
jacov
flops
grasp
-0.00
1.35
1.43
1.28
1.12
0.94
1.03
0.63
0.62
0.28
0.42
1.80
-0.00
1.19
1.26
1.30
1.25
1.16
0.78
0.72
0.60
0.59
1.92
1.23
0.00
0.82
1.29
1.31
1.04
0.82
0.74
0.70
0.60
1.83
1.35
0.87
0.00
1.30
1.23
1.09
0.84
0.69
0.68
0.60
1.56
1.28
1.23
1.19
-0.00
0.77
0.53
0.28
0.59
0.52
0.31
1.43
1.29
1.31
1.18
0.83
0.00
0.79
0.54
0.58
0.48
0.41
1.57
1.24
1.09
1.09
0.63
0.84
-0.00
0.51
0.55
0.56
0.37
1.13
0.82
0.82
0.79
0.34
0.55
0.47
0.00
0.39
0.38
0.30
1.24
0.89
0.87
0.77
0.78
0.70
0.63
0.51
0.00
0.48
0.34
0.75
0.62
0.68
0.61
0.56
0.46
0.50
0.35
0.33
0.00
0.23
1.04
0.75
0.73
0.67
0.49
0.53
0.45
0.42
0.33
0.38
0.00
Information gain on TNB101_MACRO-JIGSAW
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Conditional entropy
TNB101_MACRO-JIGSAW
random ordering
greedy ordering
minimum k-tuple
nwot
plain
zen
l2_norm
jacov
params
snip
grad_norm
flops
fisher
grasp
nwot
plain
zen
l2_norm
jacov
params
snip
grad_norm
flops
fisher
grasp
2.23
1.23
1.23
1.17
1.58
1.29
1.52
1.52
1.92
1.60
1.68
1.23
2.86
1.41
1.41
1.72
1.57
1.69
1.81
1.89
2.09
2.20
1.23
1.41
2.74
1.84
1.63
1.74
1.89
1.78
1.89
1.94
1.96
1.17
1.41
1.84
2.77
1.60
2.20
1.83
1.73
1.88
1.95
1.94
1.58
1.72
1.63
1.60
2.72
1.73
1.86
1.91
2.03
2.06
2.13
1.29
1.57
1.74
2.20
1.73
2.81
1.94
1.83
1.95
2.02
2.07
1.52
1.69
1.89
1.83
1.86
1.94
2.74
2.19
2.03
2.17
2.11
1.52
1.81
1.78
1.73
1.91
1.83
2.19
2.81
2.04
2.29
2.20
1.92
1.89
1.89
1.88
2.03
1.95
2.03
2.04
2.51
2.09
2.15
1.60
2.09
1.94
1.95
2.06
2.02
2.17
2.29
2.09
2.92
2.40
1.68
2.20
1.96
1.94
2.13
2.07
2.11
2.20
2.15
2.40
2.94
Pairwise conditional entropy on TNB101_MACRO-NORMAL
nwot
plain
zen
l2_norm
jacov
params
snip
grad_norm
flops
fisher
grasp
nwot
plain
zen
l2_norm
jacov
params
snip
grad_norm
flops
fisher
grasp
-0.00
1.00
1.00
1.06
0.66
0.95
0.72
0.72
0.31
0.63
0.56
1.62
0.00
1.45
1.44
1.14
1.29
1.16
1.04
0.96
0.76
0.66
1.51
1.33
0.00
0.90
1.11
1.00
0.86
0.96
0.85
0.80
0.79
1.59
1.35
0.93
-0.00
1.17
0.57
0.94
1.03
0.89
0.82
0.83
1.14
1.00
1.09
1.12
-0.00
0.98
0.86
0.80
0.69
0.66
0.59
1.53
1.25
1.07
0.62
1.08
-0.00
0.88
0.98
0.86
0.79
0.74
1.22
1.05
0.85
0.91
0.88
0.80
-0.00
0.55
0.71
0.57
0.63
1.29
0.99
1.02
1.07
0.89
0.97
0.62
0.00
0.76
0.52
0.61
0.59
0.62
0.62
0.63
0.49
0.56
0.48
0.47
0.00
0.42
0.36
1.31
0.82
0.98
0.97
0.86
0.90
0.75
0.63
0.82
0.00
0.52
1.27
0.75
0.99
1.01
0.81
0.87
0.83
0.75
0.79
0.54
-0.00
Information gain on TNB101_MACRO-NORMAL
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
TNB101_MACRO-NORMAL
random ordering
greedy ordering
minimum k-tuple
nwot
zen
grad_norm
l2_norm
params
plain
snip
fisher
grasp
flops
jacov
nwot
zen
grad_norm
l2_norm
params
plain
snip
fisher
grasp
flops
jacov
2.79
1.26
1.38
1.23
1.41
1.70
1.49
1.62
2.15
2.46
2.22
1.26
3.04
1.60
2.20
2.10
1.82
1.85
1.90
2.34
2.40
2.50
1.38
1.60
2.98
1.64
1.70
1.96
2.33
2.40
2.44
2.42
2.48
1.23
2.20
1.64
3.06
2.32
1.82
1.97
1.97
2.35
2.39
2.49
1.41
2.10
1.70
2.32
3.09
1.98
1.99
2.05
2.42
2.46
2.58
1.70
1.82
1.96
1.82
1.98
3.13
2.10
2.21
2.63
2.62
2.65
1.49
1.85
2.33
1.97
1.99
2.10
3.06
2.53
2.50
2.49
2.61
1.62
1.90
2.40
1.97
2.05
2.21
2.53
3.09
2.56
2.55
2.66
2.15
2.34
2.44
2.35
2.42
2.63
2.50
2.56
3.18
2.78
2.87
2.46
2.40
2.42
2.39
2.46
2.62
2.49
2.55
2.78
3.15
2.85
2.22
2.50
2.48
2.49
2.58
2.65
2.61
2.66
2.87
2.85
3.22
Pairwise conditional entropy on TNB101_MACRO-ROOM
nwot
zen
grad_norm
l2_norm
params
plain
snip
fisher
grasp
flops
jacov
nwot
zen
grad_norm
l2_norm
params
plain
snip
fisher
grasp
flops
jacov
0.00
1.53
1.41
1.55
1.37
1.09
1.29
1.16
0.63
0.33
0.56
1.78
0.00
1.44
0.84
0.94
1.22
1.19
1.15
0.70
0.64
0.54
1.61
1.38
0.00
1.35
1.28
1.03
0.65
0.58
0.55
0.56
0.51
1.82
0.85
1.42
0.00
0.73
1.24
1.09
1.08
0.71
0.66
0.56
1.68
0.99
1.39
0.77
-0.00
1.11
1.10
1.04
0.67
0.63
0.51
1.43
1.32
1.18
1.32
1.15
-0.00
1.03
0.92
0.50
0.51
0.49
1.57
1.21
0.73
1.09
1.07
0.96
-0.00
0.52
0.56
0.57
0.45
1.46
1.19
0.68
1.11
1.04
0.88
0.55
-0.00
0.52
0.54
0.43
1.02
0.84
0.74
0.83
0.76
0.54
0.68
0.61
0.00
0.40
0.30
0.69
0.75
0.73
0.75
0.69
0.52
0.66
0.60
0.37
0.00
0.29
1.00
0.72
0.74
0.73
0.64
0.57
0.61
0.56
0.35
0.37
0.00
Information gain on TNB101_MACRO-ROOM
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
TNB101_MACRO-ROOM
random ordering
greedy ordering
minimum k-tuple
nwot
zen
l2_norm
plain
params
jacov
grasp
snip
grad_norm
fisher
flops
nwot
zen
l2_norm
plain
params
jacov
grasp
snip
grad_norm
fisher
flops
3.20
1.58
1.50
1.60
1.60
2.07
1.88
1.98
2.05
2.21
2.63
1.58
3.78
2.42
1.72
2.21
1.98
2.08
2.29
2.28
2.47
2.85
1.50
2.42
3.81
1.71
2.76
1.97
2.05
2.22
2.22
2.46
2.79
1.60
1.72
1.71
3.88
1.90
2.08
3.04
2.35
2.58
2.99
2.83
1.60
2.21
2.76
1.90
3.87
2.15
2.20
2.36
2.38
2.65
2.89
2.07
1.98
1.97
2.08
2.15
3.72
2.38
2.42
2.51
2.73
3.00
1.88
2.08
2.05
3.04
2.20
2.38
3.95
2.60
2.81
3.05
3.01
1.98
2.29
2.22
2.35
2.36
2.42
2.60
3.89
3.11
2.95
3.11
2.05
2.28
2.22
2.58
2.38
2.51
2.81
3.11
3.94
3.09
3.14
2.21
2.47
2.46
2.99
2.65
2.73
3.05
2.95
3.09
4.00
3.22
2.63
2.85
2.79
2.83
2.89
3.00
3.01
3.11
3.14
3.22
3.88
Pairwise conditional entropy on TNB101_MACRO-SEGMENT
nwot
zen
l2_norm
plain
params
jacov
grasp
snip
grad_norm
fisher
flops
nwot
zen
l2_norm
plain
params
jacov
grasp
snip
grad_norm
fisher
flops
-0.00
1.62
1.70
1.60
1.60
1.13
1.32
1.22
1.15
0.99
0.57
2.20
0.00
1.36
2.06
1.57
1.80
1.70
1.49
1.50
1.31
0.93
2.30
1.39
0.00
2.10
1.05
1.84
1.76
1.59
1.59
1.34
1.02
2.28
2.16
2.17
0.00
1.98
1.80
0.84
1.53
1.30
0.89
1.05
2.27
1.67
1.11
1.97
0.00
1.73
1.67
1.51
1.49
1.23
0.99
1.65
1.74
1.75
1.64
1.57
0.00
1.34
1.30
1.21
0.99
0.72
2.07
1.87
1.90
0.90
1.74
1.57
0.00
1.34
1.14
0.89
0.93
1.91
1.61
1.68
1.54
1.53
1.47
1.29
0.00
0.78
0.94
0.78
1.90
1.66
1.73
1.36
1.56
1.43
1.14
0.83
0.00
0.85
0.80
1.79
1.53
1.54
1.01
1.35
1.27
0.95
1.05
0.91
0.00
0.78
1.26
1.04
1.10
1.06
1.00
0.88
0.87
0.77
0.75
0.66
0.00
Information gain on TNB101_MACRO-SEGMENT
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0
1
2
3
4
Conditional entropy
TNB101_MACRO-SEGMENT
random ordering
greedy ordering
minimum k-tuple
Figure 13: Conditional entropy and information gain (IG) for each ZC proxy pair across all search
spaces and datasets (Left and Middle). Conditional entropy H(y | zi1, . . . , zik) vs. k, where the
ordering zi1, . . . , zik is selected using three different strategies (Right). (3/5)
29
l2_norm
plain
snip
params
nwot
grad_norm
flops
fisher
jacov
zen
grasp
l2_norm
plain
snip
params
nwot
grad_norm
flops
fisher
jacov
zen
grasp
2.81
1.62
2.02
1.99
2.24
2.09
2.05
2.65
2.68
2.68
2.74
1.62
3.11
2.12
1.84
2.07
2.15
1.88
2.88
2.91
2.91
3.02
2.02
2.12
2.85
2.13
2.27
2.70
2.18
2.66
2.68
2.68
2.81
1.99
1.84
2.13
2.98
2.13
2.20
2.90
2.76
2.78
2.78
2.91
2.24
2.07
2.27
2.13
2.88
2.31
2.18
2.84
2.88
2.88
2.81
2.09
2.15
2.70
2.20
2.31
2.89
2.23
2.69
2.71
2.71
2.84
2.05
1.88
2.18
2.90
2.18
2.23
3.00
2.77
2.79
2.79
2.92
2.65
2.88
2.66
2.76
2.84
2.69
2.77
3.14
3.14
3.14
3.10
2.68
2.91
2.68
2.78
2.88
2.71
2.79
3.14
3.16
3.16
3.12
2.68
2.91
2.68
2.78
2.88
2.71
2.79
3.14
3.16
3.16
3.12
2.74
3.02
2.81
2.91
2.81
2.84
2.92
3.10
3.12
3.12
3.35
Pairwise conditional entropy on TNB101_MICRO-AUTOENC
l2_norm
plain
snip
params
nwot
grad_norm
flops
fisher
jacov
zen
grasp
l2_norm
plain
snip
params
nwot
grad_norm
flops
fisher
jacov
zen
grasp
0.00
1.20
0.79
0.82
0.57
0.73
0.77
0.16
0.13
0.13
0.08
1.49
-0.00
0.99
1.27
1.04
0.96
1.23
0.23
0.20
0.20
0.09
0.83
0.73
0.00
0.72
0.58
0.16
0.67
0.19
0.17
0.17
0.04
0.99
1.14
0.85
-0.00
0.86
0.78
0.08
0.23
0.20
0.20
0.08
0.63
0.81
0.61
0.75
-0.00
0.57
0.70
0.03
-0.00
-0.00
0.07
0.80
0.74
0.19
0.69
0.58
0.00
0.65
0.20
0.18
0.18
0.04
0.95
1.12
0.82
0.10
0.82
0.76
-0.00
0.23
0.20
0.20
0.08
0.49
0.26
0.48
0.39
0.30
0.46
0.37
-0.00
-0.00
-0.00
0.05
0.48
0.25
0.48
0.38
0.29
0.45
0.37
0.02
0.00
0.00
0.05
0.48
0.25
0.48
0.38
0.29
0.45
0.37
0.02
0.00
0.00
0.05
0.62
0.34
0.54
0.44
0.54
0.51
0.43
0.25
0.23
0.23
-0.00
Information gain on TNB101_MICRO-AUTOENC
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
TNB101_MICRO-AUTOENC
random ordering
greedy ordering
minimum k-tuple
snip
params
flops
l2_norm
grad_norm
nwot
plain
grasp
fisher
jacov
zen
snip
params
flops
l2_norm
grad_norm
nwot
plain
grasp
fisher
jacov
zen
2.48
1.70
1.71
1.73
2.22
1.94
2.09
2.26
2.39
2.40
2.40
1.70
2.55
2.48
1.71
1.69
1.70
2.08
2.26
2.32
2.41
2.41
1.71
2.48
2.55
1.75
1.71
1.74
2.10
2.28
2.33
2.41
2.41
1.73
1.71
1.75
2.63
1.80
2.09
2.14
2.33
2.42
2.53
2.53
2.22
1.69
1.71
1.80
2.54
2.00
2.15
2.34
2.47
2.47
2.47
1.94
1.70
1.74
2.09
2.00
2.63
2.24
2.40
2.45
2.58
2.58
2.09
2.08
2.10
2.14
2.15
2.24
2.98
2.76
2.76
2.87
2.87
2.26
2.26
2.28
2.33
2.34
2.40
2.76
3.09
2.91
2.95
2.95
2.39
2.32
2.33
2.42
2.47
2.45
2.76
2.91
3.07
2.92
2.92
2.40
2.41
2.41
2.53
2.47
2.58
2.87
2.95
2.92
3.11
3.11
2.40
2.41
2.41
2.53
2.47
2.58
2.87
2.95
2.92
3.11
3.11
Pairwise conditional entropy on TNB101_MICRO-OBJECT
snip
params
flops
l2_norm
grad_norm
nwot
plain
grasp
fisher
jacov
zen
snip
params
flops
l2_norm
grad_norm
nwot
plain
grasp
fisher
jacov
zen
-0.00
0.78
0.78
0.75
0.26
0.54
0.39
0.22
0.09
0.08
0.08
0.86
-0.00
0.07
0.84
0.86
0.85
0.47
0.29
0.23
0.15
0.15
0.85
0.07
-0.00
0.81
0.85
0.82
0.46
0.27
0.23
0.14
0.14
0.90
0.92
0.88
0.00
0.83
0.55
0.49
0.31
0.21
0.10
0.10
0.32
0.85
0.84
0.74
0.00
0.54
0.39
0.21
0.07
0.07
0.07
0.69
0.92
0.89
0.54
0.62
0.00
0.39
0.23
0.17
0.05
0.05
0.90
0.90
0.88
0.84
0.83
0.75
-0.00
0.23
0.22
0.11
0.11
0.83
0.83
0.82
0.77
0.76
0.70
0.34
0.00
0.18
0.14
0.14
0.68
0.75
0.74
0.65
0.60
0.62
0.31
0.16
-0.00
0.15
0.15
0.71
0.70
0.70
0.58
0.64
0.53
0.24
0.16
0.19
0.00
0.00
0.71
0.70
0.70
0.58
0.64
0.53
0.24
0.16
0.19
0.00
0.00
Information gain on TNB101_MICRO-OBJECT
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
TNB101_MICRO-OBJECT
random ordering
greedy ordering
minimum k-tuple
snip
grad_norm
params
flops
nwot
l2_norm
plain
grasp
jacov
zen
fisher
snip
grad_norm
params
flops
nwot
l2_norm
plain
grasp
jacov
zen
fisher
1.68
1.46
1.05
1.06
1.20
1.13
1.36
1.50
1.54
1.54
1.59
1.46
1.76
1.08
1.09
1.28
1.22
1.44
1.60
1.64
1.64
1.71
1.05
1.08
1.82
1.76
1.05
1.15
1.47
1.63
1.61
1.61
1.69
1.06
1.09
1.76
1.81
1.07
1.18
1.48
1.64
1.61
1.61
1.69
1.20
1.28
1.05
1.07
1.82
1.45
1.57
1.66
1.78
1.78
1.71
1.13
1.22
1.15
1.18
1.45
1.94
1.59
1.73
1.80
1.80
1.82
1.36
1.44
1.47
1.48
1.57
1.59
2.28
2.11
2.11
2.11
2.13
1.50
1.60
1.63
1.64
1.66
1.73
2.11
2.38
2.16
2.16
2.26
1.54
1.64
1.61
1.61
1.78
1.80
2.11
2.16
2.28
2.28
2.17
1.54
1.64
1.61
1.61
1.78
1.80
2.11
2.16
2.28
2.28
2.17
1.59
1.71
1.69
1.69
1.71
1.82
2.13
2.26
2.17
2.17
2.40
Pairwise conditional entropy on TNB101_MICRO-SCENE
snip
grad_norm
params
flops
nwot
l2_norm
plain
grasp
jacov
zen
fisher
snip
grad_norm
params
flops
nwot
l2_norm
plain
grasp
jacov
zen
fisher
-0.00
0.22
0.63
0.62
0.48
0.55
0.31
0.18
0.14
0.14
0.09
0.30
0.00
0.68
0.67
0.49
0.54
0.32
0.16
0.13
0.13
0.05
0.77
0.74
0.00
0.05
0.77
0.66
0.35
0.18
0.20
0.20
0.12
0.75
0.72
0.05
0.00
0.74
0.64
0.33
0.17
0.20
0.20
0.12
0.62
0.54
0.77
0.75
-0.00
0.37
0.25
0.16
0.04
0.04
0.11
0.81
0.72
0.78
0.76
0.48
-0.00
0.34
0.21
0.14
0.14
0.12
0.92
0.84
0.81
0.80
0.71
0.69
0.00
0.17
0.17
0.17
0.15
0.88
0.78
0.75
0.74
0.72
0.65
0.27
0.00
0.22
0.22
0.12
0.74
0.65
0.67
0.67
0.51
0.48
0.17
0.12
0.00
0.00
0.11
0.74
0.65
0.67
0.67
0.51
0.48
0.17
0.12
0.00
0.00
0.11
0.80
0.69
0.70
0.70
0.68
0.58
0.26
0.13
0.23
0.23
-0.00
Information gain on TNB101_MICRO-SCENE
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
Conditional entropy
TNB101_MICRO-SCENE
random ordering
greedy ordering
minimum k-tuple
snip
params
flops
grad_norm
nwot
l2_norm
plain
fisher
jacov
zen
grasp
snip
params
flops
grad_norm
nwot
l2_norm
plain
fisher
jacov
zen
grasp
1.88
1.15
1.19
1.62
1.29
1.20
1.56
1.71
1.75
1.75
1.78
1.15
1.99
1.94
1.19
1.20
1.28
1.63
1.75
1.79
1.79
1.88
1.19
1.94
2.01
1.23
1.24
1.32
1.66
1.78
1.81
1.81
1.91
1.62
1.19
1.23
2.00
1.43
1.36
1.66
1.87
1.88
1.88
1.90
1.29
1.20
1.24
1.43
2.00
1.58
1.75
1.82
1.96
1.96
1.90
1.20
1.28
1.32
1.36
1.58
2.10
1.76
1.89
1.96
1.96
1.98
1.56
1.63
1.66
1.66
1.75
1.76
2.38
2.21
2.19
2.19
2.29
1.71
1.75
1.78
1.87
1.82
1.89
2.21
2.48
2.26
2.26
2.41
1.75
1.79
1.81
1.88
1.96
1.96
2.19
2.26
2.38
2.38
2.32
1.75
1.79
1.81
1.88
1.96
1.96
2.19
2.26
2.38
2.38
2.32
1.78
1.88
1.91
1.90
1.90
1.98
2.29
2.41
2.32
2.32
2.55
Pairwise conditional entropy on TNB101_MICRO-JIGSAW
snip
params
flops
grad_norm
nwot
l2_norm
plain
fisher
jacov
zen
grasp
snip
params
flops
grad_norm
nwot
l2_norm
plain
fisher
jacov
zen
grasp
0.00
0.73
0.69
0.27
0.59
0.68
0.33
0.17
0.13
0.13
0.11
0.84
-0.00
0.05
0.80
0.79
0.72
0.36
0.24
0.20
0.20
0.11
0.82
0.07
0.00
0.78
0.77
0.69
0.36
0.23
0.20
0.20
0.10
0.38
0.81
0.77
0.00
0.56
0.64
0.33
0.13
0.12
0.12
0.10
0.70
0.79
0.76
0.57
-0.00
0.42
0.25
0.18
0.04
0.04
0.10
0.89
0.82
0.78
0.74
0.51
-0.00
0.34
0.20
0.14
0.14
0.12
0.82
0.75
0.72
0.71
0.63
0.62
0.00
0.17
0.18
0.18
0.09
0.77
0.73
0.70
0.61
0.66
0.59
0.28
-0.00
0.23
0.23
0.07
0.63
0.59
0.57
0.50
0.43
0.42
0.19
0.13
0.00
0.00
0.06
0.63
0.59
0.57
0.50
0.43
0.42
0.19
0.13
0.00
0.00
0.06
0.78
0.67
0.65
0.66
0.65
0.57
0.26
0.14
0.23
0.23
-0.00
Information gain on TNB101_MICRO-JIGSAW
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
Conditional entropy
TNB101_MICRO-JIGSAW
random ordering
greedy ordering
minimum k-tuple
Figure 14: Conditional entropy and information gain (IG) for each ZC proxy pair across all search
spaces and datasets (Left and Middle). Conditional entropy H(y | zi1, . . . , zik) vs. k, where the
ordering zi1, . . . , zik is selected using three different strategies (Right). (4/5)
30
params
flops
l2_norm
nwot
plain
grad_norm
snip
fisher
jacov
zen
grasp
params
flops
l2_norm
nwot
plain
grad_norm
snip
fisher
jacov
zen
grasp
2.19
2.14
1.39
1.43
1.38
1.81
1.85
1.94
1.99
1.99
2.16
2.14
2.20
1.43
1.47
1.41
1.83
1.87
1.95
2.00
2.00
2.17
1.39
1.43
2.28
1.82
1.30
1.85
1.91
2.10
2.14
2.14
2.25
1.43
1.47
1.82
2.28
1.59
2.02
2.04
2.22
2.28
2.28
2.25
1.38
1.41
1.30
1.59
2.67
2.08
2.11
2.42
2.46
2.46
2.64
1.81
1.83
1.85
2.02
2.08
2.62
2.47
2.37
2.43
2.43
2.61
1.85
1.87
1.91
2.04
2.11
2.47
2.62
2.37
2.42
2.42
2.60
1.94
1.95
2.10
2.22
2.42
2.37
2.37
2.63
2.63
2.63
2.61
1.99
2.00
2.14
2.28
2.46
2.43
2.42
2.63
2.68
2.68
2.66
1.99
2.00
2.14
2.28
2.46
2.43
2.42
2.63
2.68
2.68
2.66
2.16
2.17
2.25
2.25
2.64
2.61
2.60
2.61
2.66
2.66
2.90
Pairwise conditional entropy on TNB101_MICRO-NORMAL
params
flops
l2_norm
nwot
plain
grad_norm
snip
fisher
jacov
zen
grasp
params
flops
l2_norm
nwot
plain
grad_norm
snip
fisher
jacov
zen
grasp
0.00
0.05
0.79
0.75
0.80
0.38
0.34
0.25
0.20
0.20
0.03
0.06
0.00
0.76
0.73
0.79
0.37
0.33
0.25
0.20
0.20
0.03
0.88
0.84
-0.00
0.46
0.98
0.43
0.37
0.17
0.14
0.14
0.03
0.85
0.81
0.46
-0.00
0.69
0.26
0.24
0.06
-0.00
-0.00
0.03
1.29
1.27
1.38
1.08
-0.00
0.60
0.56
0.25
0.21
0.21
0.04
0.82
0.80
0.78
0.61
0.55
0.00
0.16
0.25
0.20
0.20
0.02
0.77
0.75
0.72
0.58
0.51
0.16
0.00
0.26
0.20
0.20
0.02
0.69
0.68
0.53
0.41
0.21
0.26
0.27
-0.00
-0.00
-0.00
0.02
0.70
0.69
0.54
0.40
0.23
0.26
0.27
0.05
0.00
0.00
0.02
0.70
0.69
0.54
0.40
0.23
0.26
0.27
0.05
0.00
0.00
0.02
0.74
0.73
0.65
0.64
0.26
0.29
0.30
0.29
0.23
0.23
0.00
Information gain on TNB101_MICRO-NORMAL
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
Conditional entropy
TNB101_MICRO-NORMAL
random ordering
greedy ordering
minimum k-tuple
snip
grad_norm
l2_norm
params
flops
nwot
plain
fisher
grasp
jacov
zen
snip
grad_norm
l2_norm
params
flops
nwot
plain
fisher
grasp
jacov
zen
2.54
2.24
1.69
1.73
1.77
1.90
2.02
2.42
2.29
2.40
2.40
2.24
2.59
1.76
1.73
1.75
1.95
2.10
2.50
2.35
2.46
2.46
1.69
1.76
2.83
1.82
1.87
2.16
2.38
2.52
2.54
2.69
2.69
1.73
1.73
1.82
2.78
2.69
1.81
2.33
2.45
2.50
2.58
2.58
1.77
1.75
1.87
2.69
2.78
1.85
2.34
2.47
2.50
2.58
2.58
1.90
1.95
2.16
1.81
1.85
2.74
2.38
2.50
2.53
2.70
2.70
2.02
2.10
2.38
2.33
2.34
2.38
3.30
2.93
3.04
3.09
3.09
2.42
2.50
2.52
2.45
2.47
2.50
2.93
3.26
3.07
3.04
3.04
2.29
2.35
2.54
2.50
2.50
2.53
3.04
3.07
3.38
3.17
3.17
2.40
2.46
2.69
2.58
2.58
2.70
3.09
3.04
3.17
3.36
3.36
2.40
2.46
2.69
2.58
2.58
2.70
3.09
3.04
3.17
3.36
3.36
Pairwise conditional entropy on TNB101_MICRO-ROOM
snip
grad_norm
l2_norm
params
flops
nwot
plain
fisher
grasp
jacov
zen
snip
grad_norm
l2_norm
params
flops
nwot
plain
fisher
grasp
jacov
zen
-0.00
0.29
0.84
0.80
0.77
0.64
0.51
0.11
0.24
0.14
0.14
0.35
0.00
0.83
0.87
0.84
0.64
0.50
0.09
0.25
0.13
0.13
1.13
1.06
-0.00
1.00
0.96
0.66
0.45
0.30
0.29
0.14
0.14
1.05
1.05
0.96
-0.00
0.09
0.97
0.45
0.33
0.28
0.20
0.20
1.01
1.03
0.91
0.09
-0.00
0.93
0.44
0.31
0.28
0.20
0.20
0.85
0.79
0.58
0.93
0.89
0.00
0.36
0.25
0.21
0.04
0.04
1.27
1.20
0.92
0.96
0.95
0.91
0.00
0.37
0.26
0.21
0.21
0.84
0.76
0.74
0.81
0.79
0.77
0.34
-0.00
0.19
0.22
0.22
1.09
1.03
0.84
0.88
0.88
0.84
0.34
0.31
0.00
0.21
0.21
0.96
0.89
0.67
0.78
0.78
0.65
0.27
0.32
0.18
0.00
0.00
0.96
0.89
0.67
0.78
0.78
0.65
0.27
0.32
0.18
0.00
0.00
Information gain on TNB101_MICRO-ROOM
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Conditional entropy
TNB101_MICRO-ROOM
random ordering
greedy ordering
minimum k-tuple
params
flops
l2_norm
nwot
snip
plain
grad_norm
fisher
jacov
zen
grasp
params
flops
l2_norm
nwot
snip
plain
grad_norm
fisher
jacov
zen
grasp
2.36
2.29
1.59
1.55
1.80
1.58
1.81
2.16
2.16
2.16
2.24
2.29
2.37
1.65
1.59
1.82
1.61
1.83
2.17
2.17
2.17
2.25
1.59
1.65
2.63
2.05
1.95
1.58
1.97
2.50
2.50
2.50
2.46
1.55
1.59
2.05
2.52
2.05
1.84
2.08
2.52
2.52
2.52
2.42
1.80
1.82
1.95
2.05
2.67
2.03
2.52
2.50
2.50
2.50
2.54
1.58
1.61
1.58
1.84
2.03
3.03
2.08
2.82
2.82
2.82
2.94
1.81
1.83
1.97
2.08
2.52
2.08
2.74
2.55
2.55
2.55
2.62
2.16
2.17
2.50
2.52
2.50
2.82
2.55
3.01
3.01
3.01
2.96
2.16
2.17
2.50
2.52
2.50
2.82
2.55
3.01
3.01
3.01
2.96
2.16
2.17
2.50
2.52
2.50
2.82
2.55
3.01
3.01
3.01
2.96
2.24
2.25
2.46
2.42
2.54
2.94
2.62
2.96
2.96
2.96
3.18
Pairwise conditional entropy on TNB101_MICRO-SEGMENT
params
flops
l2_norm
nwot
snip
plain
grad_norm
fisher
jacov
zen
grasp
params
flops
l2_norm
nwot
snip
plain
grad_norm
fisher
jacov
zen
grasp
0.00
0.07
0.76
0.81
0.56
0.78
0.55
0.20
0.20
0.20
0.12
0.08
-0.00
0.72
0.78
0.55
0.75
0.53
0.19
0.19
0.19
0.12
1.04
0.98
-0.00
0.58
0.68
1.05
0.66
0.13
0.13
0.13
0.17
0.97
0.93
0.46
0.00
0.47
0.68
0.44
-0.00
0.00
0.00
0.10
0.88
0.85
0.72
0.62
0.00
0.64
0.15
0.17
0.17
0.17
0.13
1.45
1.41
1.45
1.19
1.00
-0.00
0.94
0.21
0.21
0.21
0.09
0.93
0.91
0.77
0.66
0.22
0.66
-0.00
0.19
0.19
0.19
0.13
0.85
0.83
0.51
0.49
0.51
0.19
0.46
-0.00
-0.00
-0.00
0.04
0.85
0.83
0.51
0.49
0.51
0.19
0.46
0.00
0.00
0.00
0.04
0.85
0.83
0.51
0.49
0.51
0.19
0.46
0.00
0.00
0.00
0.04
0.95
0.93
0.72
0.77
0.65
0.24
0.57
0.22
0.22
0.22
0.00
Information gain on TNB101_MICRO-SEGMENT
1
2
3
4
5
6
7
8
9
10 11 12 13 14
Number of ZC proxies
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Conditional entropy
TNB101_MICRO-SEGMENT
random ordering
greedy ordering
minimum k-tuple
Figure 15: Conditional entropy and information gain (IG) for each ZC proxy pair across all search
spaces and datasets (Left and Middle). Conditional entropy H(y | zi1, . . . , zik) vs. k, where the
ordering zi1, . . . , zik is selected using three different strategies (Right). (5/5)
31
epe_nas
jacov
grasp
plain
fisher
synflow
snip
grad_norm
nwot
flops
l2_norm
zen
params
epe_nas
jacov
grasp
plain
fisher
synflow
snip
grad_norm
nwot
flops
l2_norm
zen
params
4.08
1.18
1.19
1.17
1.20
1.20
1.22
1.20
1.18
1.17
1.17
1.17
1.19
1.18
4.07
1.19
1.22
1.20
1.27
1.23
1.22
1.24
1.26
1.25
1.25
1.24
1.19
1.19
3.99
1.31
1.40
1.22
1.26
1.28
1.23
1.21
1.23
1.21
1.22
1.17
1.22
1.31
4.02
1.25
1.23
1.19
1.19
1.29
1.29
1.30
1.32
1.31
1.20
1.20
1.40
1.25
4.02
1.29
1.78
1.77
1.20
1.17
1.20
1.22
1.21
1.20
1.27
1.22
1.23
1.29
4.05
1.41
1.46
1.38
1.43
1.40
1.47
1.42
1.22
1.23
1.26
1.19
1.78
1.41
4.07
2.57
1.29
1.34
1.31
1.35
1.32
1.20
1.22
1.28
1.19
1.77
1.46
2.57
4.09
1.33
1.34
1.34
1.37
1.34
1.18
1.24
1.23
1.29
1.20
1.38
1.29
1.33
3.92
2.19
2.34
2.13
2.27
1.17
1.26
1.21
1.29
1.17
1.43
1.34
1.34
2.19
3.94
2.71
2.98
2.79
1.17
1.25
1.23
1.30
1.20
1.40
1.31
1.34
2.34
2.71
3.90
2.73
2.98
1.17
1.25
1.21
1.32
1.22
1.47
1.35
1.37
2.13
2.98
2.73
3.93
2.89
1.19
1.24
1.22
1.31
1.21
1.42
1.32
1.34
2.27
2.79
2.98
2.89
3.90
Pairwise conditional entropy on NB301-CF10
epe_nas
jacov
grasp
plain
fisher
synflow
snip
grad_norm
nwot
flops
l2_norm
zen
params
epe_nas
jacov
grasp
plain
fisher
synflow
snip
grad_norm
nwot
flops
l2_norm
zen
params
0.00
2.90
2.89
2.91
2.88
2.88
2.86
2.87
2.89
2.91
2.91
2.90
2.89
2.89
-0.00
2.88
2.84
2.87
2.80
2.84
2.85
2.82
2.81
2.81
2.81
2.83
2.80
2.80
0.00
2.68
2.59
2.77
2.73
2.70
2.76
2.78
2.76
2.78
2.77
2.85
2.79
2.71
0.00
2.77
2.78
2.82
2.82
2.72
2.73
2.71
2.70
2.71
2.82
2.82
2.62
2.77
0.00
2.72
2.24
2.25
2.82
2.84
2.81
2.80
2.81
2.86
2.78
2.83
2.82
2.76
0.00
2.64
2.59
2.67
2.62
2.65
2.58
2.63
2.85
2.85
2.81
2.88
2.30
2.66
0.00
1.51
2.78
2.74
2.77
2.73
2.75
2.88
2.87
2.80
2.89
2.32
2.63
1.52
-0.00
2.76
2.75
2.75
2.72
2.75
2.73
2.67
2.69
2.62
2.72
2.53
2.62
2.58
0.00
1.73
1.58
1.79
1.64
2.77
2.68
2.73
2.65
2.77
2.51
2.61
2.60
1.75
-0.00
1.23
0.96
1.15
2.73
2.65
2.67
2.60
2.70
2.50
2.59
2.56
1.56
1.19
0.00
1.17
0.92
2.75
2.67
2.71
2.61
2.71
2.46
2.58
2.56
1.80
0.94
1.19
0.00
1.04
2.71
2.67
2.68
2.60
2.69
2.48
2.58
2.57
1.63
1.11
0.93
1.01
0.00
Information gain on NB301-CF10
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0
1
2
3
4
Conditional entropy
NB301-CF10
random ordering
greedy ordering
minimum k-tuple
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0
1
2
3
4
Conditional entropy
NB201-CF100
random ordering
greedy ordering
minimum k-tuple
1
2
3
4
5
6
7
8
9
10 11 12 13
Number of ZC proxies
0
1
2
3
4
Conditional entropy
TNB101_MACRO-autoencoder
random ordering
greedy ordering
minimum k-tuple
Figure 16: Given a ZC proxy pair (i, j), we compute the conditional entropy H(y | zi, zj) (top left),
and information gain H(y | zi) −H(y | zi, zj) (top right). Conditional entropy H(y | zi1, . . . , zik)
vs. k, where the ordering zi1, . . . , zik is selected using three different strategies. The minimum
k-tuple and greedy ordering signiﬁcantly overlap in the ﬁrst two ﬁgures (bottom). Similar to Figure
4, but using a different bin discretization strategy.
32
2
4
6
8
10
12
Num. ZC Proxies
0.40
0.45
0.50
0.55
0.60
0.65
0.70
0.75
0.80
Spearman Rank Correlation
NB101 CF10
2
4
6
8
10
12
Num. ZC Proxies
0.80
0.82
0.84
0.86
0.88
0.90
0.92
0.94
0.96
Spearman Rank Correlation
NB201 CF100
2
4
6
8
10
12
Num. ZC Proxies
0.25
0.30
0.35
0.40
0.45
0.50
Spearman Rank Correlation
NB301 CF10
2
4
6
8
10
12
Num. ZC Proxies
0.76
0.78
0.80
0.82
0.84
0.86
0.88
0.90
Spearman Rank Correlation
TNB101-Macro-Autoencoder
Figure 17: Ablation study on the number of ZC proxies as features vs. rank correlation performance,
for an XGBoost surrogate model trained on 1000 randomly drawn architectures. The ordering of ZC
proxies is computed via the greedy method from Section 4.3.
33
105
Time (s)
90.0
90.2
90.4
90.6
90.8
91.0
91.2
91.4
Accuracy (%)
NB201 CF10
Encoding
ZCPs
Encoding + ZCPs
105
Time (s)
70.0
70.5
71.0
71.5
72.0
72.5
73.0
Accuracy (%)
NB201 CF100
Encoding
ZCPs
Encoding + ZCPs
106
Time (s)
44.0
44.5
45.0
45.5
46.0
46.5
47.0
Accuracy (%)
NB201 IMGNT
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
93.9
94.0
94.1
94.2
94.3
94.4
Accuracy (%)
NB301 CF10
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
94.0
94.2
94.4
94.6
94.8
95.0
95.2
Accuracy (%)
TNB101_MICRO JIGSAW
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
43.8
44.0
44.2
44.4
44.6
44.8
45.0
45.2
45.4
Accuracy (%)
TNB101_MICRO OBJECT
Encoding
ZCPs
Encoding + ZCPs
106
Time (s)
0.5600
0.5625
0.5650
0.5675
0.5700
0.5725
0.5750
0.5775
0.5800
SSIM
TNB101_MICRO NORMAL
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
54.0
54.1
54.2
54.3
54.4
54.5
54.6
54.7
54.8
54.9
Accuracy (%)
TNB101_MICRO SCENE
Encoding
ZCPs
Encoding + ZCPs
106
Time (s)
94.46
94.48
94.50
94.52
94.54
94.56
94.58
94.60
mIoU
TNB101_MICRO SEGMENT
Encoding
ZCPs
Encoding + ZCPs
105
106
Time (s)
0.640
0.635
0.630
0.625
0.620
0.615
0.610
0.605
L2 Loss
TNB101_MICRO ROOM
Encoding
ZCPs
Encoding + ZCPs
106
107
Time (s)
0.535
0.540
0.545
0.550
0.555
0.560
0.565
0.570
0.575
SSIM
TNB101_MICRO AUTOENC
Encoding
ZCPs
Encoding + ZCPs
Figure 18: Performance of BANANAS with the vanilla XGBoost surrogate model vs. XGBoost using
the additional ZC proxy scores (concatenated to the architecture encoding) as input.
34
105
106
Time
90.0
90.2
90.4
90.6
90.8
91.0
Accuracy (%)
NB201 CF10
Encoding
ZCPs
Encoding + ZCPs
105
106
Time
71.0
71.2
71.4
71.6
71.8
72.0
72.2
72.4
Accuracy (%)
NB201 CF100
Encoding
ZCPs
Encoding + ZCPs
106
Time
45.00
45.25
45.50
45.75
46.00
46.25
46.50
46.75
47.00
Accuracy (%)
NB201 IMGNT
Encoding
ZCPs
Encoding + ZCPs
106
Time
94.0
94.1
94.2
94.3
94.4
94.5
94.6
94.7
94.8
Accuracy (%)
TNB101_MICRO JIGSAW
Encoding
ZCPs
Encoding + ZCPs
106
Time
44.0
44.2
44.4
44.6
44.8
45.0
Accuracy (%)
TNB101_MICRO OBJECT
Encoding
ZCPs
Encoding + ZCPs
106
107
Time
0.560
0.562
0.564
0.566
0.568
0.570
SSIM
TNB101_MICRO NORMAL
Encoding
ZCPs
Encoding + ZCPs
106
Time
54.0
54.1
54.2
54.3
54.4
54.5
54.6
Accuracy (%)
TNB101_MICRO SCENE
Encoding
ZCPs
Encoding + ZCPs
106
107
Time
94.48
94.49
94.50
94.51
94.52
94.53
94.54
mIoU
TNB101_MICRO SEGMENT
Encoding
ZCPs
Encoding + ZCPs
106
Time
0.6400
0.6375
0.6350
0.6325
0.6300
0.6275
0.6250
0.6225
0.6200
L2 Loss
TNB101_MICRO ROOM
Encoding
ZCPs
Encoding + ZCPs
106
107
Time
0.540
0.542
0.544
0.546
0.548
0.550
0.552
0.554
SSIM
TNB101_MICRO AUTOENC
Encoding
ZCPs
Encoding + ZCPs
Figure 19: Performance of NPENAS with the vanilla XGBoost surrogate model vs. XGBoost using
the additional ZC proxy scores (concatenated to the architecture encoding) as input.
35
params
snip
grad_norm
nwot
zen
synflow
l2_norm
plain
grasp
flops
jacov
fisher
epe_nas
CF10
0
0.166
0.187
0.243
0.28
0.281
0.336
0.361
0.417
0.449
0.454
0.558
1
Feature importances for NB101 (train size: 100)
0.0
0.2
0.4
0.6
0.8
1.0
params
snip
grad_norm
nwot
l2_norm
zen
grasp
flops
plain
synflow
jacov
fisher
epe_nas
CF10
CF100
IMG
0.000173
0.126
0.185
0.202
0.247
0.253
0.276
0.264
0.326
0.328
0.419
0.42
0.818
0
0.114
0.219
0.23
0.275
0.28
0.31
0.306
0.35
0.364
0.463
0.488
0.874
0.000347
0.113
0.22
0.269
0.301
0.309
0.321
0.345
0.39
0.408
0.531
0.58
1
Feature importances for NB201 (train size: 100)
0.0
0.2
0.4
0.6
0.8
1.0
zen
params
l2_norm
snip
nwot
grad_norm
synflow
plain
flops
grasp
jacov
fisher
epe_nas
CF10
0
0.0318
0.0912
0.114
0.187
0.231
0.244
0.302
0.336
0.342
0.348
0.52
1
Feature importances for NB301 (train size: 100)
0.0
0.2
0.4
0.6
0.8
1.0
params
synflow
snip
zen
grad_norm
nwot
l2_norm
plain
grasp
epe_nas
flops
jacov
fisher
JIGSAW
SCENE
OBJECT
AUTOENC
NORMAL
ROOM
SEGMENT
0.0289
0.183
0.107
0.164
0.164
0.257
0.263
0.348
0.384
0.13
0.441
0.424
0.788
0.0235
0.175
0.0566
0.14
0.15
0.19
0.206
0.252
0.27
0.682
0.345
0.378
0.47
0.0261
0.181
0.0806
0.178
0.213
0.227
0.266
0.326
0.344
0.812
0.41
0.364
0.563
0.0265
0
0.175
0.246
0.35
0.324
0.358
0.381
0.436
0
0.476
0.518
1
0.0297
0
0.174
0.246
0.266
0.308
0.298
0.308
0.357
0
0.413
0.553
0.866
0.0239
0.215
0.0758
0.182
0.164
0.249
0.26
0.311
0.285
0.831
0.377
0.34
0.485
0.0363
0
0.204
0.202
0.368
0.235
0.258
0.166
0.314
0
0.409
0.59
0.697
Feature importances for TNB101_MICRO (train size: 100)
0.0
0.2
0.4
0.6
0.8
1.0
synflow
snip
zen
params
l2_norm
grad_norm
plain
grasp
nwot
jacov
epe_nas
flops
fisher
JIGSAW
SCENE
OBJECT
AUTOENC
NORMAL
ROOM
SEGMENT
0.283
0.132
0.19
0.242
0.291
0.15
0.379
0.317
0.457
0.504
0.15
0.591
0.887
0.181
0.102
0.119
0.166
0.188
0.221
0.286
0.239
0.41
0.328
0.812
0.437
0.43
0.175
0.107
0.11
0.158
0.191
0.258
0.324
0.302
0.391
0.352
0.886
0.449
0.491
0
0.157
0.196
0.249
0.33
0.315
0.309
0.401
0.266
0.359
0
0.715
0.825
0
0.221
0.22
0.221
0.313
0.34
0.301
0.398
0.34
0.431
0
0.643
0.917
0.198
0.12
0.155
0.179
0.216
0.256
0.306
0.361
0.354
0.371
1
0.418
0.514
0
0.193
0.233
0.22
0.321
0.356
0.176
0.352
0.505
0.41
0
0.626
0.86
Feature importances for TNB101_MACRO (train size: 100)
0.0
0.2
0.4
0.6
0.8
1.0
Figure 20: Feature importance values for XGBoost trained on a set of 100 architectures using ZC
proxies as features.
36
params
snip
grad_norm
zen
nwot
flops
synflow
l2_norm
plain
grasp
jacov
fisher
epe_nas
CF10
0
0.22
0.268
0.334
0.346
0.358
0.384
0.39
0.442
0.48
0.51
0.57
1
Feature importances for NB101 (train size: 1000)
0.0
0.2
0.4
0.6
0.8
1.0
params
snip
flops
grad_norm
nwot
zen
l2_norm
synflow
grasp
plain
jacov
fisher
epe_nas
CF10
CF100
IMG
0
0.224
0.255
0.305
0.291
0.317
0.33
0.334
0.366
0.394
0.403
0.489
0.755
0.000335
0.243
0.282
0.326
0.329
0.358
0.383
0.387
0.403
0.448
0.47
0.547
0.864
0.00152
0.254
0.335
0.336
0.381
0.397
0.428
0.424
0.426
0.492
0.528
0.613
1
Feature importances for NB201 (train size: 1000)
0.0
0.2
0.4
0.6
0.8
1.0
zen
params
l2_norm
snip
nwot
grad_norm
synflow
plain
flops
grasp
jacov
fisher
epe_nas
CF10
0
0.0179
0.0842
0.133
0.158
0.244
0.272
0.305
0.326
0.356
0.361
0.527
1
Feature importances for NB301 (train size: 1000)
0.0
0.2
0.4
0.6
0.8
1.0
params
synflow
snip
zen
epe_nas
grad_norm
nwot
flops
l2_norm
plain
grasp
jacov
fisher
JIGSAW
SCENE
OBJECT
AUTOENC
NORMAL
ROOM
SEGMENT
0.0333
0.266
0.182
0.224
0.104
0.252
0.294
0.307
0.311
0.386
0.411
0.373
0.63
0.0352
0.23
0.112
0.176
0.511
0.182
0.213
0.212
0.235
0.271
0.283
0.296
0.338
0.0335
0.275
0.157
0.222
0.715
0.269
0.287
0.272
0.317
0.355
0.376
0.36
0.454
0.0415
0
0.299
0.381
0
0.465
0.442
0.449
0.485
0.53
0.574
0.576
1
0.043
0
0.293
0.314
0
0.394
0.379
0.394
0.412
0.421
0.468
0.468
0.807
0.0334
0.294
0.151
0.226
0.721
0.237
0.291
0.265
0.31
0.32
0.327
0.367
0.436
0.0457
0
0.27
0.297
0
0.395
0.311
0.329
0.328
0.286
0.379
0.431
0.698
Feature importances for TNB101_MICRO (train size: 1000)
0.0
0.2
0.4
0.6
0.8
1.0
synflow
params
snip
zen
l2_norm
nwot
grad_norm
epe_nas
plain
grasp
jacov
flops
fisher
JIGSAW
SCENE
OBJECT
AUTOENC
NORMAL
ROOM
SEGMENT
0.405
0.281
0.243
0.322
0.408
0.452
0.307
0.162
0.515
0.447
0.62
0.674
0.957
0.263
0.209
0.209
0.229
0.268
0.338
0.309
0.85
0.4
0.338
0.437
0.446
0.525
0.285
0.215
0.227
0.246
0.28
0.345
0.344
0.97
0.451
0.379
0.477
0.482
0.587
0
0.281
0.309
0.342
0.403
0.37
0.458
0
0.447
0.516
0.48
0.615
0.902
0
0.295
0.358
0.362
0.426
0.396
0.502
0
0.451
0.544
0.539
0.662
1
0.283
0.218
0.223
0.252
0.292
0.355
0.331
0.959
0.393
0.457
0.456
0.498
0.564
0
0.294
0.318
0.348
0.423
0.403
0.474
0
0.329
0.456
0.47
0.625
0.905
Feature importances for TNB101_MACRO (train size: 1000)
0.0
0.2
0.4
0.6
0.8
1.0
Figure 21: Feature importance values for XGBoost trained on a set of 1000 architectures using ZC
proxies as features.
37
