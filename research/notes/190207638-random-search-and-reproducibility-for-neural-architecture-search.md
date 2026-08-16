---
title: '[1902.07638] Random Search and Reproducibility for Neural Architecture Search'
id: 190207638-random-search-and-reproducibility-for-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
- random-search-baseline
- nas-reproducibility
- load-bearing
created: '2026-08-16T15:48:50.982453Z'
updated: '2026-08-16T15:49:13.069240Z'
source: https://arxiv.org/abs/1902.07638
source_domain: arxiv.org
fetched_at: '2026-08-16T15:48:50.981343Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Li & Talwalkar (UAI 2019; this is the correct ''Li and Talwalkar'' paper
  named explicitly in the research query''s THIRD question, distinct from NAS-Bench-101
  which shares a similar-looking arXiv ID). Central thesis: NAS is a specialized hyperparameter-optimization
  problem, and since random search is already a known competitive baseline for hyperparameter
  optimization, it should be a mandatory NAS baseline too. Proposes and tests two
  random-search variants -- random search with early-stopping and a novel random search
  with weight-sharing (RS-WS) -- on two standard benchmarks (Penn Treebank/PTB and
  CIFAR-10). Findings: random search with early-stopping performs at least as well
  as ENAS, a then-leading NAS method, on both benchmarks; random search with weight-sharing
  beats random search with early-stopping and achieves a then-state-of-the-art result
  on PTB and a highly competitive result on CIFAR-10. Also documents a NAS reproducibility
  crisis: published NAS results commonly lack the source material (code, exact seeds,
  documentation) needed to exactly reproduce them, and the paper explicitly discusses
  the robustness of published NAS gains against the variability inherent in NAS experimental
  setups. The authors'' own remedy is to publish full code, random seeds, and documentation,
  and to report their RS-WS results across multiple runs (6 sets of random seeds per
  the v2 changelog) rather than a single run. This is the canonical citation establishing
  that any NAS method claiming to beat random search must (a) use a strong, well-tuned
  random-search baseline, not a naive one, and (b) report results over multiple seeds/runs,
  both of which the target paper''s evaluation protocol must be checked against.'
---

*Suggested by [[neural-architecture-search-insights-from-1000-papers]] — canonical NAS random-search/reproducibility critique cited by the 1000-papers survey, directly named in the research query*

*Suggested by [[190209635v2-nas-bench-101-towards-reproducible-neural-architecture-search]] — correct paper for Li and Talwalkar random-search baseline standard named explicitly in query THREE; original assigned URL 1902.09635 turned out to be NAS-Bench-101, not this paper*

[1902.07638] Random Search and Reproducibility for Neural Architecture Search
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1902.07638
(cs)
[Submitted on 20 Feb 2019 (
v1
), last revised 30 Jul 2019 (this version, v3)]
Title:
Random Search and Reproducibility for Neural Architecture Search
Authors:
Liam Li
,
Ameet Talwalkar
View a PDF of the paper titled Random Search and Reproducibility for Neural Architecture Search, by Liam Li and 1 other authors
View PDF
HTML (experimental)
Abstract:
Neural architecture search (NAS) is a promising research direction that has the potential to replace expert-designed networks with learned, task-specific architectures. In this work, in order to help ground the empirical results in this field, we propose new NAS baselines that build off the following observations: (i) NAS is a specialized hyperparameter optimization problem; and (ii) random search is a competitive baseline for hyperparameter optimization. Leveraging these observations, we evaluate both random search with early-stopping and a novel random search with weight-sharing algorithm on two standard NAS benchmarks---PTB and CIFAR-10. Our results show that random search with early-stopping is a competitive NAS baseline, e.g., it performs at least as well as ENAS, a leading NAS method, on both benchmarks. Additionally, random search with weight-sharing outperforms random search with early-stopping, achieving a state-of-the-art NAS result on PTB and a highly competitive result on CIFAR-10. Finally, we explore the existing reproducibility issues of published NAS results. We note the lack of source material needed to exactly reproduce these results, and further discuss the robustness of published results given the various sources of variability in NAS experimental setups. Relatedly, we provide all information (code, random seeds, documentation) needed to exactly reproduce our results, and report our random search with weight-sharing results for each benchmark on multiple runs.
Comments:
V2 Changelog: - Modified footnote 2 for ENAS. - Expanded broad reproducibility study for random search with WS for CNN to 6 sets of random seeds v3 Changelog: - Added journal reference - Updated acknowledgements
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1902.07638
[cs.LG]
(or
arXiv:1902.07638v3
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1902.07638
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
Conference on Uncertainty in Artificial Intelligence (UAI), 2019
Submission history
From: Liam Li [
view email
]
[v1]
Wed, 20 Feb 2019 16:49:07 UTC (139 KB)
[v2]
Mon, 15 Jul 2019 21:06:02 UTC (139 KB)
[v3]
Tue, 30 Jul 2019 20:07:41 UTC (139 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Random Search and Reproducibility for Neural Architecture Search, by Liam Li and 1 other authors
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
2019-02
Change to browse by:
cs
stat
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
Liam Li
Ameet Talwalkar
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

## Full text (recovered via direct extraction)

Random Search and Reproducibility for Neural Architecture Search
LIAM LI, Carnegie Mellon University
AMEET TALWALKAR, Carnegie Mellon University and Determined AI
Neural architecture search (NAS) is a promising research direction that has the potential to replace expert-designed networks
with learned, task-specific architectures. In this work, in order to help ground the empirical results in this field, we propose
new NAS baselines that build off the following observations: (i) NAS is a specialized hyperparameter optimization problem;
and (ii) random search is a competitive baseline for hyperparameter optimization. Leveraging these observations, we evaluate
both random search with early-stopping and a novel random search with weight-sharing algorithm on two standard NAS
benchmarks—PTB and CIFAR-10. Our results show that random search with early-stopping is a competitive NAS baseline,
e.g., it performs at least as well as ENAS [41], a leading NAS method, on both benchmarks. Additionally, random search with
weight-sharing outperforms random search with early-stopping, achieving a state-of-the-art NAS result on PTB and a highly
competitive result on CIFAR-10. Finally, we explore the existing reproducibility issues of published NAS results. We note the
lack of source material needed to exactly reproduce these results, and further discuss the robustness of published results
given the various sources of variability in NAS experimental setups. Relatedly, we provide all information (code, random
seeds, documentation) needed to exactly reproduce our results, and report our random search with weight-sharing results for
each benchmark on multiple runs.
Additional Key Words and Phrases: Neural Architecture Search, Hyperparameter Optimization, Automated Machine Learning
1
INTRODUCTION
Deep learning offers the promise of bypassing the process of manual feature engineering by learning representa-
tions in conjunction with statistical models in an end-to-end fashion. However, neural network architectures
themselves are typically designed by experts in a painstaking, ad-hoc fashion. Neural architecture search (NAS)
presents a promising path for alleviating this pain by automatically identifying architectures that are superior to
hand-designed ones. Since the work by Zoph and Le [51], there has been explosion of research activity on this
problem [1, 5, 7, 11, 23, 31, 32, 34, 39, 41, 43, 47, 50]. Notably, there has been great industry interest in NAS, as
evidenced by the vast computational [43, 51, 52] and marketing resources [17] committed to industry-driven
NAS research. However, despite a steady stream of promising empirical results [7, 34, 35, 43, 51, 52], we see three
fundamental issues with the current state of NAS research:
Inadequate Baselines. Leading NAS methods exploit many of the strategies that were initially explored in the
context of traditional hyperparameter optimization tasks, e.g., evolutionary search [21, 40], Bayesian optimization
[4, 20, 44], and gradient-based approaches [2, 36]. Moreover, the NAS problem is in fact a specialized instance of
the broader hyperparameter optimization problem. However, in spite of the close relationship between these two
problems, existing comparisons between novel NAS methods and standard hyperparameter optimization methods
are inadequate. In particular, to the best of our knowledge, no state-of-the-art hyperparameter optimization
methods have been evaluated on standard NAS benchmarks. Without benchmarking against leading hyperparameter
optimization baselines, it difficult to quantify the performance gains provided by specialized NAS methods.
Complex Methods. We have witnessed a proliferation of novel NAS methods, with research progressing in
many different directions. New approaches introduce a significant amount of algorithmic complexity in the search
process, including complicated training routines [1, 7, 41, 47], architecture transformations [6, 11, 32, 43, 46], and
modeling assumptions [5, 23, 26, 31, 50] (see Figure 1 and Section 1.1 for more details). While many technically
diverse NAS methods demonstrate good empirical performance, they often lack corresponding ablation studies
Authors’ addresses: Liam Li, me@liamcli.com, Carnegie Mellon University; Ameet Talwalkar, talwalkar@cmu.edu, Carnegie Mellon University
and Determined AI.
arXiv:1902.07638v3  [cs.LG]  30 Jul 2019

2
•
Li and Talwalkar
[7, 35, 50], and as a result, it is unclear what NAS component(s) are necessary to achieve a competitive empirical
result.
Lack of Reproducibility. Experimental reproducibility is of paramount importance in the context of NAS
research, given the empirical nature of the field, the complexity of new NAS methods, and the steep computational
costs associated with empirical evaluation. In particular, there are (at least) two important notions of reproducibility
to consider: (1) “exact” reproducibility i.e., whether it is possible to reproduce explicitly reported experimental
results; and “broad” reproducibility, i.e., the degree to which the reported experimental results are themselves
robust and generalizable. Broad reproducibility is difficult to measure due to the computational burden of NAS
methods and the high variance associated with extremal statistics. However, most of the published results in
this field do not even satisfy exact reproducibility. For example, of the 12 papers published since 2018 at NeurIPS,
ICML, and ICLR that introduce novel NAS methods (see Table 1), none are exactly reproducible. Indeed, each fails on
account of some combination of missing model evaluation code, architecture search code, random seeds used for
search and evaluation, and/or undocumented hyperparameter tuning.1
While addressing these challenges will require community-wide efforts, in this work we present results that
aim to make some initial progress on each of these issues. In particular, our contributions are as follows:
(1) We help ground existing NAS results by providing a new perspective on the gap between traditional hy-
perparameter optimization and leading NAS methods. Specifically, we evaluate a general hyperparameter
optimization method combining random search with early-stopping [30] on two standard NAS benchmarks
(CIFAR-10 and PTB). With approximately the same amount of compute as DARTS [34], a state-of-the-art
(SOTA) NAS method, this simple method provides a much more competitive baseline for both benchmarks: (1)
on PTB, random search with early-stopping reaches test perplexity of 56.4 compared to the published result
for ENAS [41], a leading NAS method, of 56.3,2 and (2) for CIFAR-10, random search with early-stopping
achieves a test error of 2.85%, whereas the published result for ENAS is 2.89%. While SOTA NAS methods
like DARTS still outperform this baseline, our results demonstrate that the gap is not nearly as large as that
suggested by published random search baselines on these tasks [34, 41].
(2) We identify a small subset of NAS components that are sufficient for achieving good empirical results. We
construct a simple algorithm from the ground up starting from vanilla random search, and demonstrate that
properly tuned random search with weight-sharing is competitive with much more complicated methods
when using similar computational budgets. In particular, we identify the following meta-hyperparameters that
impact the behavior of our algorithm: batch size, number of epochs, network size, and number of evaluated
architectures. We evaluate our proposed method using the same search space and evaluation scheme as
DARTS [34], a leading NAS method. We explore a few modifications of the meta-hyperparameters to improve
search quality and make full use of available GPU memory and computational resources, and observe SOTA
performance on the PTB benchmark and comparable performance to DARTS on the CIFAR-10 benchmark.
We emphasize that we do not perform additional hyperparameter tuning of the final architectures discovered
at the end of the search process.
(3) We open-source all of the necessary code, random seeds, and documentation necessary to reproduce our
experiments. Our single machine results shown in Table 2 and Table 5 follow a deterministic experimental
1It is important to note that these works vary drastically in terms of what materials they provide, and some authors such as Liu et al. [34],
provide a relatively complete codebase for their methods. However, even in the case of DARTS, the code for the CIFAR-10 benchmark is not
deterministic and Liu et al. [34] do not provide random seeds or documentation regarding the post-processing steps in which they perform
hyperparameter optimization on final architectures returned by DARTS. We were thus not able to reproduce the results in Liu et al. [34], but
we were able to use the DARTS code repository (https://github.com/quark0/darts) as the launching point for our experimental setup.
2We could not reproduce this result using the initial final architecture and code provided by the authors (https://github.com/melodyguan/
enas). They have since released another repository (https://github.com/google-research/google-research/tree/master/enas_lm) that reports
reproduced results but we have not verified these figures.

Random Search and Reproducibility for Neural Architecture Search
•
3
Search  
Space
Search 
Method
Evaluation 
Method
Reinforcement  
Learning
Evolutionary Search
Gradient-Based  
Optimization
Bayesian 
Optimization
Full Training
Partial Training
Hypernetworks
Weight-Sharing
Network Morphism
Cell Block
Meta-Architecture
Unstructured & 
Structured
Continuous & 
 Discrete
Random Search
Fig. 1. Components of hyperparameter optimization. Primarily NAS-specific methods are outlined in purple.
setup, given a fixed random seed, and satisfy exact reproducibility. For these experiments on the two standard
benchmarks, we study the broad reproduciblity of our random search with weight-sharing results by repeating
our experiments with different random seeds. We observe non-trivial differences across independent runs
and identify potential sources for these differences. Our results highlight the need for more careful reporting
of experimental results, increased transparency of intermediate results, and more robust statistics to quantify
the performance of NAS methods.
1.1
Background
We first provide an overview of the components of hyperparameter optimization and, by association, NAS. As
shown in Figure 1, a general hyperparameter optimization problem has three components, each of which can
have NAS-specific approaches. We provide a brief overview of the components below, drawing attention to
NAS-specific methods (see the survey by Elsken et al. [12] for a more thorough coverage of NAS).
Search Space. Hyperparameter optimization involves identifying a good hyperparameter configuration from
a set of possible configurations. The search space defines this set of configurations, and can include continuous
or discrete hyperparameters in a structured or unstructured fashion [3, 14, 40, 44]. NAS-specific search spaces
usually involve discrete hyperparameters with additional structure that can be captured with a directed acyclic
graph (DAG) [34, 41]. Additionally, since a search space for designing an entire architecture would have too many
nodes and edges, search spaces are usually defined over some smaller building block, i.e., cell blocks, that are
repeated in some way via a preset or learned meta-architecture to form a larger architecture [12]. We design our
random search NAS algorithm for such a cell block search space, using the same search spaces for the CIFAR-10
and PTB benchmarks as DARTS for our experiments in Section 4. See Section 3 for a concrete example of one
such search space.
Search Method. Given a search space, there are various search methods to select putative configurations to
evaluate. Random search is the most basic approach, yet it is quite effective in practice [3, 29]. Various general
and NAS-specific adaptive methods have also been introduced, all of which attempt to bias the search in some
way towards configurations that are more likely to perform well. In traditional hyperparameter optimization, the

4
•
Li and Talwalkar
choice of search method can depends on the search space. Bayesian approaches based on Gaussian processes
[24, 27, 44, 45] and gradient-based approaches [2, 36] are generally only applicable to continuous search spaces.
In contrast, tree-based Bayesian [4, 20], evolutionary strategies [40], and random search are more flexible and
can be applied to any search space. NAS-specific search methods can also be categorized into the same broad
categories but are tailored for structured NAS search spaces (see Section 2.2 for a more involved discussion).
Evaluation Method. For each hyperparameter configuration considered by a search method, we must evaluate
its quality. The default approach to perform such an evaluation involves fully training a model with the given
hyperparameters, and subsequently measuring its quality, e.g., its predictive accuracy on a validation set. The
first generation of NAS methods relied on full training evaluation, and thus required thousands of GPU days
to achieve a desired result [42, 43, 51, 52]. In contrast, partial training methods exploit early-stopping to speed
up the evaluation process at the cost of noisy estimates of configuration quality. These methods use Bayesian
optimization [13, 24, 27], performance prediction [10, 15], or multi-armed bandits [22, 29, 30] to adaptively
allocate resources to different configurations. NAS-specific evaluation methods exploit the structure of neural
networks to provide even cheaper, heuristic estimates of quality. Many of these methods center around sharing
and reuse: network morphisms build upon previously trained architectures [6, 11, 23]; hypernetworks and
performance prediction encode information from previously seen architectures [5, 31, 50]; and weight-sharing
methods [1, 7, 34, 41, 47] use a single set of weights for all possible architectures.
2
RELATED WORK
We now provide additional context for the three issues we identified with the current state of NAS research in
Section 1.
2.1
Inadequate Baselines
Existing works in NAS do not provide adequate comparison to random search and other hyperparameter
optimization methods. Some works either compare to random search given a budget of just of few evaluations
[34, 41] or Bayesian optimization methods without efficient architecture evaluation schemes [23]. While Real
et al. [43] and Cai et al. [6] provide a thorough comparison to random search, they use random search with full
training even though partial training methods have been shown to be orders-of-magnitude faster than standard
random search [29, 30].
While certain hyperparameter optimization methods [27, 36, 44] require non-trivial modification in order
to work with NAS search spaces, others are easily applicable to NAS problems [4, 10, 13, 20, 29, 30]. Of these
applicable methods, we choose to use a simple method combining random search with early-stopping called
ASHA [30] to provide a competitive baseline for standard hyperparameter optimization. Li et al. [30] showed
ASHA to be a state-of-the-art, theoretically principled, bandit-based partial training method that outperforms
leading adaptive search strategies for hyperparameter optimization. We compare the empirical performance of
ASHA with that of NAS methods in Section 4.
2.2
Complex Methods
Much of the complexity of NAS methods is introduced in the process of adapting search methods for NAS-specific
search spaces: evolutionary approaches need to define a set of possible mutations to apply to different architectures
[42, 43]; Bayesian optimization approaches [23, 26] rely on specially designed kernels; gradient-based methods
transform the discrete architecture search problem into a continuous optimization problem so that gradients can
be applied [7, 34, 35, 47]; and Zoph and Le [51], Zoph et al. [52], and Pham et al. [41] use reinforcement learning
to train a recurrent neural network controller to generate good architectures. All of these search approaches
add a significant amount of complexity with no clear winner, especially since methods some times use different

Random Search and Reproducibility for Neural Architecture Search
•
5
search spaces and evaluation methods. To simplify the search process and help isolate important components of
NAS, we use random search to sample architectures from the search space.
Additional complexity is also introduced by the NAS-specific evaluation methods mentioned previously.
Network morphisms require architecture transformations that satisfy certain criteria; hypernetworks and perfor-
mance prediction methods encode information from previously seen architectures in an auxiliary network; and
weight-sharing methods [1, 7, 34, 41, 47] use a single set of weights for all possible architectures and hence, can
require careful training routines. Despite their complexity, these more efficient NAS evaluation methods are 1-3
orders-of-magnitude cheaper than full training (see Table 5 and Table 2), at the expense of decreased fidelity to the
true performance. Of these evaluation methods, network morphism still requires on the order of 100 GPU days
[11, 31] and, while hypernetworks and prediction performance based methods can be cheaper, weight-sharing is
less complex since it does not require training an auxiliary network. In addition to the computational efficiency
of weight-sharing methods [7, 34, 41, 47], which only require computation on the order of fully training a single
architecture, this approach has also achieved the best result on the two standard benchmarks [7, 34]. Hence, we
use random search with weight-sharing as our starting point for a simple and efficient NAS method.
Our work is inspired by the result of Bender et al. [1], which showed that random search, combined with a
well-trained set of shared weights can successfully differentiate good architectures from poor performing ones.
However, their work required several modifications to stabilize training (e.g., a tunable path dropout schedule
over edges of the search DAG and a specialized ghost batch normalization scheme [19]). Furthermore, they only
report experimental results on the CIFAR-10 benchmark, on which they fell slightly short of the results for
leading NAS methods. In contrast, our combination of random search with weight-sharing greatly simplifies the
training routine and we identify key variables needed to achieve competitive results on both CIFAR-10 and PTB
benchmarks.
2.3
Lack of Reproducibility
The earliest NAS results lacked exact and broad reproducibility due to the tremendous amount of computation
required to achieve the results [43, 51, 52]. Additionally, some of these methods used specialized hardware (i.e.,
TPUs) that were not easily accessible to researchers at the time [43]. Although the final architectures were
eventually provided [16, 18], the code for the search methods used to produce these results has not been released,
precluding researchers from reproducing these results even if they had sufficient computational resources.
Recently, it has become feasible to evaluate the exact and broad reproducibility of many SOTA methods due
to their reduced computational cost. However, while many authors have released code for their work [e.g.,
5, 6, 34, 41], others have not made their code publicly available [e.g., 47, 50], including the work most closely
related to ours by Bender et al. [1]. We summarize the reproducibility of recent NAS publications at some of the
major machine learning conferences in Table 1 according to the availability of the following:
(1) Architecture search code. The output of this code is the final architecture that should be trained on the
evaluation task.
(2) Model evaluation code. The output of this code is the final performance on the evaluation task.
(3) Hyperparameter tuning documentation. This includes code used to perform hyperparameter tuning
of the final architectures, if any.
(4) Random Seeds. This includes random seeds used for both the search and post-processing (i.e., retraining
of final architecture as well as any additional hyperparameter tuning) phases. Most works provide the final
architectures but random seeds are required to verify that the search process actually results in those final
architectures and the performance of the final architectures matches the published result. Note the random
seeds are only useful if the code for search and post-processing phases are deterministic up to a random
seed; this was not the case for the DARTS code used for the CIFAR-10 benchmark.

6
•
Li and Talwalkar
Table 1. Reproducibility of NAS Publications. Summary of the reproducibility status of recent NAS publications appearing
in top machine learning conferences. For the hyperparameter tuning column, N/A indicates we are not aware that the authors
performed additional hyperparameter optimization.
† Published result is not reproducible for the PTB benchmark when training the reported final architecture with provided
code.
∗Code to reproduce experiments was requested on OpenReview.
Architecture
Model Evaluation
Random
Hyperparameter
Conference
Publication
Search Code
Code
Seeds
Tuning
ICLR 2018
Brock et al. [5]
Yes
Yes
No
N/A
Liu et al. [32]
No
No
ICML 2018
Pham et al. [41]†
Yes
Yes
No
Undocumented
Cai et al. [6]
Yes
Yes
No
N/A
Bender et al. [1]
No
No
NIPS 2018
Kandasamy et al. [26]
Yes
Yes
No
N/A
Luo et al. [35]
Yes
Yes
No
Grid Search
ICLR 2019
Liu et al. [34]
Yes
Yes
No
Undocumented
Cai et al. [7]
No
Yes
No
N/A
Zhang et al. [50]∗
No
No
Xie et al. [47]∗
No
No
Cao et al. [8]
No
No
All 4 criteria are necessary for exact reproducibility. Due to the absence of random seeds for all methods
with released code, none of the methods in Table 1 are exactly reproducible from the search phase to the final
architecture evaluation phase.
While only criteria 1–3 are necessary to estimate broad reproducibility, there is minimal discussion of the
broad reproducibility of existing methods in published work. With the exception of NASBOT [26] and DARTS
[34], the methods in Table 1 only report the performance of the best found architecture, presumably resulting
from a single run of the search process. Although this is understandable in light of the computational costs for
some of these methods [6, 35], the high variance of extremal statistics makes it difficult to isolate the impact
of the novel contributions introduced in each work. DARTS is particularly commendable in acknowledging its
dependence on random initialization, prompting the use multiple runs to select the best architecture. In our
experiments in Section 4, we follow DARTS and report the result of our random weight-sharing method across
multiple trials; in fact, we go one step further and evaluate the broad reproducibility of our results with multiple
sets of random seeds.
3
METHODOLOGY
We now introduce our NAS algorithm that combines random search with weight-sharing. Our algorithm is
designed for an arbitrary search space with a DAG representation, and in our in our experiments in Section 4,
we use the same search spaces as that considered by DARTS [34] for the standard CIFAR-10 and PTB NAS
benchmarks.
For concreteness, consider the search space used by DARTS for designing a recurrent cell for the PTB benchmark:
the DAG considered for the recurrent cell has N = 8 nodes and the operations considered include tanh, relu,
sigmoid, and identity. To sample an architecture from this search space, we apply random search in the following
manner:

Random Search and Reproducibility for Neural Architecture Search
•
7
x_{t}
0
h_{t-1}
1
relu
2
tanh
5
sigmoid
8
identity
3
tanh
4
identity
6
relu
h_{t}
7
identity
Fig. 2. Recurrent Cell on PTB Benchmark. The best architecture found by random search with weight-sharing in Sec-
tion 4.1 is depicted. Each numbered square is a node of the DAG and each edge represents the flow of data from one node to
another after applying the indicated operation along the edge. Nodes with multiple incoming edges (i.e., node 0 and output
node h_{t} concatenate the inputs to form the output of the node.
(1) For each node in the DAG, determine what decisions must be made. In the case of the PTB search space, we
need to choose a node as input and a corresponding operation to apply to generate the output of the node.
(2) For each decision, identify the possible choices for the given node. In the case of the PTB search space, if
we number the nodes from 1 to N, node i can take the outputs of nodes 0 to node i −1 as input (the initial
input to the cell is index 0 and is also a possible input). Additionally, we can choose an operation from
{tanh, relu, sigmoid, and identity} to apply to the output of node i.
(3) Finally, moving from node to node, we sample uniformly from the set of possible choices for each decision
that needs to be made.
Figure 2 shows an example of an architecture from this search space.
In order to combine random search with weight-sharing, we simply use randomly sampled architectures to
train the shared weights. Shared weights are updated by selecting a single architecture for a given minibatch and
updating the shared weights by back-propagating through the network with only the edges and operations as
indicated by the architecture activated. Hence, the number of architectures used to update the shared weights is
equivalent to the total number of minibatch training iterations.
After training the shared weights for a certain number of epochs, we use these trained shared weights to
evaluate the performance of a number of randomly sampled architectures on a separate held out dataset. We
select the best performing one as the final architecture, i.e., as the output of our search algorithm.
3.1
Relevant Meta-Hyperparameters
There are a few key meta-hyperparameters that impact the behavior of our search algorithm. We describe each
of them below, along with a description of how we expect them to impact the search algorithm, both in terms of
search quality and computational costs.
(1) Training epochs. Increasing the number of training epochs while keeping all other parameters the same
increases the total number of minibatch updates and hence, the number of architectures used to update the
shared weights. Intuitively, training with more architectures should help the shared weights generalize
better to what are likely unseen architectures in the evaluation step. Unsurprisingly, more epochs increase
the computational time required for architecture search.
(2) Batch size. Decreasing the batch size while keeping all other parameters the same also increases the
number of minibatch updates but at the cost of noisier gradient update. Hence, we expect reducing the

8
•
Li and Talwalkar
batch size to have a similar effect as increasing the number of training epochs but may necessitate adjusting
other meta-hyperparameters to account for the noisier gradient update. Intuitively, more minibatch updates
increase the computational time required for architecture search.
(3) Network size. Increasing the search network size increases the dimension of the shared weights. Intuitively,
this should boost performance since a larger search network can store more information about different
architectures. Unsurprisingly, larger networks require more GPU memory.
(4) Number of evaluated architectures. Increasing the number of architectures that we evaluate using the
shared weights allows for more exploration in the architecture search space. Intuitively, this should help
assuming that there is a high correlation between the performance of an architecture evaluated using
shared weights and the ground truth performance of that architecture when trained from scratch [1].
Unsurprisingly, evaluating more architectures increases the computational time required for architecture
search.
Other learning meta-hyperparameters will likely need to be adjusted accordingly for different settings of the key
relevant meta-hyperparameters listed above. In our experiments in Section 4, we tune gradient clipping as a fifth
meta-hyperparameter, though there are other possible meta-hyperparameters that may benefit from additional
tuning (e.g., learning rate, momentum).
In Section 4, following these intuitions, we incrementally explore the design space of our search method in
order to improve search quality and make full use of the available GPU memory and computational resources.
3.2
Memory Footprint
Since we train the shared weights using a single architecture at a time, we have the option of only loading the
weights associated with the operations and edges that are activated into GPU memory. Hence, the memory
footprint of our random search with weight-sharing can be reduced to that of a single model. In this sense, our
approach is similar to ProxylessNAS [7] and allows us to perform architecture search with weight-sharing on the
larger “proxyless” models that are usually used in the final architecture evaluation step instead of the smaller
proxy models that are usually used in the search step. We take advantage of this in a subset of our experiments
for the PTB benchmark in Section 4.1; performing random search with weight-sharing on a proxyless network
for the CIFAR-10 benchmark is a direction for future work.
In contrast, Bender et al. [1] trains the shared weights with a path dropout schedule that incrementally prunes
edges within the DAG so that the sub-DAGs used to train the shared weights become sparser as training progresses.
Under this training routine, since most of the edges in the search DAG are activated in the beginning, the memory
footprint cannot be reduced to that of a single model to allow a proxyless network for the shared weights.
4
EXPERIMENTS
In line with prior work [34, 41, 51], we consider the two standard benchmarks for neural architecture search: (1)
language modeling on the Penn Treebank (PTB) dataset [37] and (2) image classification on CIFAR-10 [28]. For
each of these benchmarks, we consider the same search space and use much of the same experimental setups as
DARTS [34], and by association SNAS [47], to facilitate a fair comparison of our results to existing work.
To evaluate the performance of random search with weight-sharing on these two benchmarks, we proceed in
the same three stages as Liu et al. [34]:
• Stage 1: Perform architecture search for a cell block on a cheaper search task.
• Stage 2: Evaluate the best architecture from the first stage by retraining a larger, network formed from
multiple cell blocks of the best found architecture from scratch. This stage is used to select the best
architecture from multiple trials.

Random Search and Reproducibility for Neural Architecture Search
•
9
• Stage 3: Perform the full evaluation of the best found architecture from the second stage by either training
for more epochs (PTB) or training with more seeds (CIFAR-10).
We start with the same meta-hyperparameter settings used by DARTS to train the shared weights. Then, we
incrementally modify the meta-hyperparameters identified in Section 3.1 to improve performance until we either
reach state-of-the-art performance (for PTB) or match the performance of DARTS and SNAS (for CIFAR-10).
For our evaluation of random search with early-stopping (i.e., ASHA) on these two benchmarks, we perform
architecture search using partial training of the stage (2) evaluation network and then select the best architecture
for stage (3) evaluation. For both benchmarks, we run ASHA with a starting resource per architecture of r = 1
epoch, a maximum resource of 300 epochs, and a promotion rate of η = 4, indicating the top 1/4 of architectures
will be promoted in each round and trained for 4× more resource.
4.1
PTB Benchmark
We now present results for the PTB benchmark. We use the DARTS search space for the recurrent cell, which
is described in Section 3. For this benchmark, due to higher memory requirements for their mixture operation,
DARTS used a small recurrent network with embedding and hidden dimension of 300 to perform the architecture
search followed by a larger network with embedding and hidden dimension of 850 to perform the evaluation.
For the PTB benchmark, we refer to the network used in the first stage as the proxy network and the network
in the later stages as the proxyless network. We next present the final search results. We subsequently explore
the impact of various meta-hyperparameters on random search with weight-sharing, and finally evaluate the
reproducibility of various methods on this benchmark.
4.1.1
Final Search Results. We now present our final evaluation results in Table 2. Specifically, we report the
output of stage (3), in which we train the proxyless network configured according to the best architectures found
by different methods for 3600 epochs. This setup matches the evaluation scheme used for the reported results in
Table 2 of Liu et al. [34] (see Appendix A.2 for more details). We discuss various aspects of these results in the
context of the three issues—baselines, complex methods, reproducibility—introduced in Section 1.
First, we evaluate the ASHA baseline using 2 GPU days, which is equivalent to the total cost of DARTS (second
order). In contrast to the one random architecture evaluated by Pham et al. [41] and the 8 evaluated by Liu et al.
[34] for their random search baselines, ASHA evaluated over 300 architectures with the allotted computation time.
The best architecture found by ASHA achieves a test perplexity of 56.4, which is comparable to the published
result for ENAS and significantly better than the random search baseline provided by Liu et al. [34], DARTS
(first order), and the reproduced result for ENAS [34]. Our result demonstrates that the gap between SOTA NAS
methods and standard hyperparameter optimization approaches on the PTB benchmark is significantly smaller
than that suggested by the existing comparisons to random search [34, 41].
Next, we evaluate random search with weight-sharing with tuned meta-hyperparameters (see Section 4.1.2
for details). With slightly lower search cost than DARTS, this method finds an architecture that reaches test
perplexity 55.5, achieving SOTA perplexity compared to previous NAS approaches. We note that manually
designed architectures are competitive with RNN cells designed by NAS methods on this benchmark. In fact, the
work by Yang et al. [49] using LSTM with mixture of experts in the softmax layer (MoS) outperforms automatically
designed cells. Our architecture would likely also improve significantly with MoS, but we train without MoS to
provide a fair comparison to ENAS and DARTS.
Finally, we examine the reproducibility of the NAS methods with available code for both architecture search and
evaluation. For DARTS, exact reproducibility was not feasible since Liu et al. [34] do not provide random seeds for
the search process; however, we were able to reproduce the performance of their reported best architecture. We
also evaluated the broad reproducibility of DARTS through an independent run, which reached a test perplexity
of 55.9, compared to the published value of 55.7. For ENAS, end-to-end exact reproducibility was infeasible due to

10
•
Li and Talwalkar
Table 2. PTB Benchmark: Comparison with state-of-the-art NAS methods and manually designed networks. Lower
test perplexity is better on this benchmark. The results are grouped by those for manually designed networks, published
NAS methods, and the methods that we evaluated. Table entries denoted by "-" indicate that the field does not apply, while
entries denoted by "N/A" indicate unknown entries. The search cost, unless otherwise noted, is measured in GPU days. Note
that the search cost is hardware dependent and the search cost shown for our results are calculated for Tesla P100 GPUs; all
other numbers are those reported by Liu et al. [34].
# Search cost is in CPU-days.
∗We could not reproduce this result using the code released by the authors at https://github.com/melodyguan/enas.
† The stage (1) cost shown is that for 1 trial as opposed to the cost for 4 trials shown for DARTS and Random search WS. It is
unclear whether ENAS requires multiple trials followed by stage (2) evaluation in order to find a good architecture.
Test Perplexity
Params
Search Cost
Comparable
Search
Architecture
Source
Valid
Test
(M)
Stage 1
Stage 2
Total
Search Space?
Method
LSTM + DropConnect
[38]
60.0
57.3
24
-
-
-
-
manual
ASHA + LSTM + DropConnect
[30]
58.1
56.3
24
-
-
13
N
HP-tuned
LSTM + MoS
[49]
56.5
54.4
22
-
-
-
-
manual
NAS#
[51]
N/A
64.0
25
-
-
1e4
N
RL
ENAS∗†
[41]
N/A
56.3
24
0.5
N/A
N/A
Y
RL
ENAS†
[34]
60.8
58.6
24
0.5
N/A
N/A
Y
random
Random search baseline
[34]
61.8
59.4
23
-
-
2
Y
random
DARTS (first order)
[34]
60.2
57.6
23
0.5
1
1.5
Y
gradient-based
DARTS (second order)
[34]
58.1
55.7
23
1
1
2
Y
gradient-based
DARTS (second order)
Ours
58.2
55.9
23
1
1
2
Y
gradient-based
ASHA baseline
Ours
58.6
56.4
23
-
-
2
Y
random
Random search WS
Ours
57.8
55.5
23
0.25
1
1.25
Y
random
non-deterministic code and missing random seeds for both the search and evaluation steps. Additionally, when
we tried to reproduce their result using the provided final architecture, we could not match the reported test
perplexity of 56.3 in our rerun. Consequently, in Table 2 we show the test perplexity for the final architecture
found by ENAS trained using the DARTS code base, which Liu et al. [34] observed to give a better test perplexity
than using the architecture evaluation code provided by ENAS. We next considered the reproducibility of random
search with weight-sharing. We verified the exact reproducibility of our reported results, and then investigated
their broad reproducibility by running another experiment with different random seeds. In this second experiment,
we observed a final text perplexity of 56.5, compared with a final test perplexity of 55.5 in the first experiment.
Our detailed investigation in Section 4.1.3 shows that the discrepancies across both DARTS and random search
with weight-sharing are unsurprising in light of the differing convergence rates among architectures on this
benchmark.
4.1.2
Impact of Meta-Hyperparameters. We now detail the meta-hyperparameter settings that we tried for
random search with weight-sharing in order to achieve SOTA performance on the PTB benchmark. Similar to
DARTS, in these preliminary experiments we performed 4 separate trials of each version of random search with
weight-sharing, where each trial consists of executing stage (1) followed by stage (2). In stage (1), we train the
shared weights and then use them to evaluate 2000 randomly sampled architectures. In stage (2), we select the
best architecture out of 2000, according to the shared weights, to train from scratch using the proxyless network
for 300 epochs.
We incrementally tune random search with weight-sharing by adjusting the following meta-hyperparameters
associated with training the shared weights in stage (1): (1) gradient clipping, (2) batch size, and (3) network size.
The settings we consider proceed as follows:

Random Search and Reproducibility for Neural Architecture Search
•
11
• Random (1): We train the shared weights of the proxy network using the same setup as DARTS with the
same values for number of epochs, batch size, and gradient clipping; all other meta-hyperparameters are
the same.
• Random (2): We decrease the maximum gradient norm to account for discrete architectures, as opposed
to the weighted combination used by DARTS, so that gradient updates are not as large in each direction.
• Random (3): We decrease batch size from 256 to 64 in order to increase the number of architectures used
to train the shared weights.
• Random (4): We train the larger proxyless network architecture with shared weights instead of the proxy
network, thereby significantly increasing the number of parameters in the model.
The stage (2) performance of the final architecture after retraining from scratch for each of these settings is shown
in Table 3. With the extra capacity in the larger network used in Random (4), random search with weight-sharing
achieves average validation perplexity of 64.7 across 4 trials, with the best architecture (shown in Figure 2 in
Section 3) reaching 63.8. In light of these stage (2) results, we focused in stage (3) on the best architecture found
by Random (4) Run 1, and achieved test perplexity of 55.5 after training for 3600 epochs as reported in Table 2.
Table 3. PTB Benchmark: Comparison of Stage (2) Intermediate Search Results for Weight-Sharing Methods. In
stage (1), random search is run with different settings to train the shared weights. The resulting networks are used to evaluate
2000 randomly sampled architectures. In stage (2), the best of these architectures for each trial is then trained from scratch
for 300 epochs. We report the performance of the best architecture after stage (2) across 4 trials for each search method.
Setting
Network
Batch
Gradient
Trial
Method
Config
Epochs
Size
Clipping
1
2
3
4
Best
Average
DARTS [34]
proxy
50
256
0.25
67.3
66.3
63.4
63.4
63.4
65.1
Reproduced DARTS
proxy
50
256
0.25
64.5
67.7
64.0
67.7
64.0
66.0
Random (1)
proxy
50
256
0.25
65.6
66.3
66.0
65.6
65.6
65.9
Random (2)
proxy
50
256
0.1
65.8
67.7
65.3
64.9
64.9
65.9
Random (3)
proxy
50
64
0.1
66.1
65.0
64.9
64.5
64.5
65.1
Random (4) Run 1
proxyless
50
64
0.1
66.3
64.6
64.1
63.8
63.8
64.7
Random (4) Run 2
proxyless
50
64
0.1
63.9
64.8
66.3
66.7
63.9
65.4
4.1.3
Investigating Reproducibility. We next examine the stage (2) intermediate results in Table 3 in the context
of reproducibility. The first two rows of Table 3 show a comparison of the published stage (2) results for DARTS
and our independent runs of DARTS. Both the best and average across 4 trials are worse in our reproduction of
their results. Additionally, as previously mentioned, we perform an additional run of Random (4) with 4 different
random seeds to test the broad reproducibility our result. The minimum stage (2) validation perplexity over these
4 trials is 63.9, compared to a minimum validation perplexity of 63.8 for the first set of seeds.
Table 4. PTB Benchmark: Ranking of Intermediate Validation Perplexity. Architectures are retrained from scratch
using the proxyless network and the validation perplexity is reported after training for the indicated number of epochs. The
final test perplexity after training for 3600 epochs is also shown for reference.
Validation Perplexity by Epoch
Test
300
500
1600
2600
3600
Perplexity
Search Method
Value
Rank
Value
Rank
Value
Rank
Value
Rank
Value
Rank
Value
Rank
DARTS
64.0
4
61.9
2
59.5
2
58.5
2
58.2
2
55.9
2
ASHA
63.9
2
62.0
3
59.8
4
59.0
3
58.6
3
56.4
3
Random (4) Run 1
63.8
1
61.7
1
59.3
1
58.4
1
57.8
1
55.5
1
Random (4) Run 2
63.9
2
62.1
4
59.6
3
59.0
3
58.8
4
56.5
4

12
•
Li and Talwalkar
Next, in Table 4 we compare the validation perplexities of the best architectures from ASHA, Random (4) Run
1, Random (4) Run 2, and our independent run of DARTS after training each from scratch for up to 3600 epochs.
The swap in relative ranking across epochs demonstrates the risk of using noisy signals for the reward. In this
case, we see that even partial training for 300 epochs does not recover the correct ranking; training using shared
weights further obscures the signal. The differing convergence rates explain the difference in final test perplexity
of the best architecture from Random (4) Run 2 and those from DARTS and Random (4) Run 1, despite Random
(4) Run 2 reaching a comparable perplexity after 300 epochs.
Overall, the results of Tables 3 and 4 demonstrate a high variance in the stage (2) intermediate results across
trials, along with issues related to differing convergence rates for different architectures. These two issues help
explain the differences between the independent runs of DARTS and random search with weight-sharing. A third
potential source of variation, which could in particular adversely impact our random search with weight-sharing
results, stems from the fact that we did not perform any additional hyperparameter tuning in stage (3); instead
we used the same training hyperparameters that were tuned by Liu et al. [34] for the final architecture found by
DARTS.
4.2
CIFAR-10 Benchmark
We next present results for the CIFAR-10 benchmark. The DAG considered for the convolutional cell has N = 4
search nodes and the operations considered include 3 × 3 and 5 × 5 separable convolutions, 3 × 3 and 5 × 5 dilated
separable convolutions, 3 × 3 max pooling, and 3 × 3 average pooling, and zero [34]. To sample an architecture
from this search space, we have to choose, for each node, 2 input nodes from previous nodes and associated
operations to perform on each input (there are two initial inputs to the cell that are also possible input); we
sample in this fashion twice, once for the normal convolution cell and one for the reduction cell (e.g., see Figure 3).
Note that in contrast to DARTS, we include the zero operation when choosing the final architecture for each trial
for further evaluation in stages (2) and (3). We hypothesize that our results may improve if we impose a higher
complexity on the final architectures by excluding the zero op.
Due to higher memory requirements for weight-sharing, Liu et al. [34] uses a smaller network with 8 stacked
cells and 16 initial channels to perform the convolutional cell search, followed by a larger network with 20 stacked
cells and 36 initial channels to perform the evaluation. Again, we will refer to the network used in the first stage
as the proxy network and the network in the second stage the proxyless network.
Similar to the PTB results in Section 4.1, we will next present the final search results for the CIFAR-10
benchmark, and then dive deeper into these results to explore the impact of meta-hyperparameters on stage (2)
intermediate results, and finally evaluate associated reproducibility ramifications.
4.2.1
Final Search Results. We now present our results after performing the final evaluation in stage (3). We use
the same evaluation scheme used to produce the results in Table 1 of Liu et al. [34]. In particular, we train the
proxyless network configured according to the best architectures found by different methods with 10 different
seeds and report the average and standard deviation. Again, we discuss our results in the context of the three
issues introduced in Section 1.
First, we evaluate the ASHA baseline using 9 GPU days, which is comparable to the 10 GPU days we allotted to
our independent run of DARTS. In contrast to the one random architecture evaluated by Pham et al. [41] and the
24 evaluated by Liu et al. [34] for their random search baselines, ASHA evaluated over 700 architectures in the
allotted computation time. The best architecture found by ASHA achieves an average error of 3.03 ± 0.13, which
is significantly better than the random search baseline provided by Liu et al. [34] and comparable to DARTS (first
order). Additionally, the best performing seed reached a test error of 2.85, which is lower than the published
result for ENAS. Similar to the PTB benchmark, these results suggest that the gap between SOTA NAS methods
and standard hyperparameter optimization is much smaller than previously reported [34, 41].

Random Search and Reproducibility for Neural Architecture Search
•
13
Table 5. CIFAR-10 Benchmark: Comparison with state-of-the-art NAS methods and manually designed networks.
The results are grouped by those for manually designed networks, published NAS methods, and the methods that we
evaluated. Models for all methods are trained with auxiliary towers and cutout. Test error for our contributions are averaged
over 10 random seeds. Table entries denoted by "-" indicate that the field does not apply, while entries denoted by "N/A"
indicate unknown entries. The search cost is measured in GPU days. Note that the search cost is hardware dependent and
the search cost shown for our results are calculated for Tesla P100 GPUs; all other numbers follow those reported by Liu et al.
[34].
∗We show results for the variants of these networks with comparable number of parameters. Larger versions of these
networks achieve lower errors.
# Reported test error averaged over 5 seeds.
† The stage (1) cost shown is that for 1 trial as opposed to the cost for 4 trials shown for DARTS and Random search WS. It is
unclear whether the method requires multiple trials followed by stage (2) evaluation in order to find a good architecture.
‡ Due to the longer evaluation we employ in stage (2) to account for unstable rankings, the cost for stage (2) is 1 GPU day for
results reported by Liu et al. [34] and 6 GPU days for our results.
Test Error
Params
Search Cost
Comparable
Search
Architecture
Source
Best
Average
(M)
Stage 1
Stage 2
Total
Search Space?
Method
Shake-Shake#
[9]
N/A
2.56
26.2
-
-
-
-
manual
PyramidNet
[48]
2.31
N/A
26
-
-
-
-
manual
NASNet-A#∗
[52]
N/A
2.65
3.3
-
-
2000
N
RL
AmoebaNet-B∗
[43]
N/A
2.55 ± 0.05
2.8
-
-
3150
N
evolution
ProxylessNAS†
[7]
2.08
N/A
5.7
4
N/A
N/A
N
gradient-based
GHN#†
[50]
N/A
2.84 ± 0.07
5.7
0.84
N/A
N/A
N
hypernetwork
SNAS†
[47]
N/A
2.85 ± 0.02
2.8
1.5
N/A
N/A
Y
gradient-based
ENAS†
[41]
2.89
N/A
4.6
0.5
N/A
N/A
Y
RL
ENAS
[34]
2.91
N/A
4.2
4
2
6
Y
RL
Random search baseline
[34]
N/A
3.29 ± 0.15
3.2
-
-
4
Y
random
DARTS (first order)
[34]
N/A
3.00 ± 0.14
3.3
1.5
1
2.5
Y
gradient-based
DARTS (second order)
[34]
N/A
2.76 ± 0.09
3.3
4
1
5
Y
gradient-based
DARTS (second order)‡
Ours
2.62
2.78 ± 0.12
3.3
4
6
10
Y
gradient-based
ASHA baseline
Ours
2.85
3.03 ± 0.13
2.2
-
-
9
Y
random
Random search WS‡
Ours
2.71
2.85 ± 0.08
4.3
2.7
6
9.7
Y
random
Next, we evaluate random search with weight-sharing with tuned meta-hyperparameters (see Section 4.2.2 for
details). This method finds an architecture that achieves an average test error of 2.85 ± 0.08, which is comparable
to the reported results for SNAS and DARTS, the top 2 weight-sharing algorithms that use a comparable search
space, as well as GHN [50]. Note that while the two manually tuned architectures we show in Table 5 outperform
the best architecture discovered by random search with weight-sharing, they have over 7× more parameters.
Additionally, the best-performing efficient NAS method, ProxylessNAS, uses a larger proxyless network and a
significantly different search space than the one we consider. As mentioned in Section 3, random search with
weight-sharing can also directly search over larger proxyless networks since it trains using discrete architectures.
We hypothesize that using a proxyless network and applying random search with weight-sharing to the same
search space as ProxylessNAS would further improve our results; we leave this as a direction for future work.
Finally, we examine the reproducibility of the NAS methods using a comparable search space with available
code for both architecture search and evaluation (i.e., DARTS and ENAS; to our knowledge, code is not currently
available for SNAS). For DARTS, exact reproducibility was not feasible since the code is non-deterministic and Liu
et al. [34] do not provide random seeds for the search process; hence, we focus on broad reproducibility of the
results. In our independent run, DARTS reached an average test error of 2.78 ± 0.12 compared to the published
result of 2.76±0.09. Notably, we observed that the process of selecting the best architecture in stage (2) is unstable
when training stage (2) models for only 100 epochs; see Section 4.2.3 for details. Hence, we use 600 epochs in

14
•
Li and Talwalkar
c_{k-2}
0
sep_conv_5x5
2
max_pool_3x3
c_{k-1}
skip_connect
1
sep_conv_5x5
3
sep_conv_3x3
sep_conv_3x3
sep_conv_3x3
sep_conv_5x5
c_{k}
(a) Normal Cell
c_{k-2}
0
sep_conv_5x5
1
max_pool_3x3
2
dil_conv_5x5
c_{k-1}
dil_conv_3x3
avg_pool_3x3
skip_connect
3
avg_pool_3x3
c_{k}
dil_conv_5x5
(b) Reduction Cell
Fig. 3. Convolutional Cells on CIFAR-10 Benchmark: Best architecture found by random search with weight-sharing.
all of our CIFAR experiments, including our independent DARTS run, which explains the discrepancy in stage
(2) costs between original DARTS and our independent run. For ENAS, the published results do not satisfy
exact reproducibility due to the same issues as those for DARTS. We show in Table 5 the broad reproducibility
experiment conducted by Liu et al. [34] for ENAS; here, ENAS found an architecture that achieved a comparable
test error of 2.91 in 8× the reported stage (1) search cost. As with the PTB benchmark, we then investigated
the reproducibility of random search with weight-sharing. We verified exact reproducibility and then examined
broad reproducibility by evaluating 5 additional independent runs of our method. We observe performance below
2.90 test error in 2 of the 5 runs and an average of 2.92 across all 6 runs. We investigate various sources for these
discrepancies in Section 4.2.3.
Table 6. CIFAR-10 Benchmark: Comparison of Stage (2) Intermediate Search Results for Weight-Sharing Methods.
In stage (1), random search is run with different settings to train the shared weights. The shared weights are then used to
evaluate the indicated number of randomly sampled architectures. In stage (2), the best of these architectures for each trial
is then trained from scratch for 600 epochs. We report the performance of the best architecture after stage (2) for each trial
for each search method.
† This run was performed using the DARTS code before we corrected for non-determinism (see Appendix A.2).
Setting
Gradient
Initial
# Archs
Trial
Method
Epochs
Clipping
Channels
Evaluated
1
2
3
4
Best
Average
Reproduced DARTS†
50
5
16
-
2.92
2.77
3.00
3.05
2.77
2.94
Random (1)
50
5
16
1000
3.25
4.00
2.98
3.58
2.98
3.45
Random (2)
150
5
16
5000
2.93
3.80
3.19
2.96
2.93
3.22
Random (3)
150
1
16
5000
3.50
3.42
2.97
2.95
2.97
3.21
Random (4)
300
1
16
11000
3.04
2.90
3.14
3.09
2.90
3.04
Random (5) Run 1
150
1
24
5000
2.96
3.33
2.83
3.00
2.83
3.03
4.2.2
Impact of Meta-Hyperparameters. We next detail the meta-hyperparameter settings that we tried in order
to reach competitive performance on the CIFAR-10 benchmark via random search with weight-sharing. Similar
to DARTS, and as with the PTB benchmark, in these preliminary experiments we performed 4 separate trials of
each version of random search with weight-sharing, where each trial consists of executing stage (1) followed by
stage (2). In stage (1), we train the shared weights and use them to evaluate a given number of randomly sampled
architectures on the test set. In stage (2), we select the best architecture, according to the shared weights, to train
from scratch using the proxyless network for 600 epochs.

Random Search and Reproducibility for Neural Architecture Search
•
15
We incrementally tune random search with weight-sharing by adjusting the following meta-hyperparameters
that impact both the training of shared weights and the evaluation of architectures using these trained weights:
number of training epochs, gradient clipping, number of architectures evaluated using shared weights, and
network size. The settings we consider for random search proceed as follows:
• Random (1): We start by training the shared weights with the proxy network used by DARTS and default
values for number of epochs, gradient clipping, and number of initial filters; all other meta-hyperparameters
are the same.
• Random (2): We increase the number of training epochs from 50 to 150, which concurrently increases the
number of architectures used to update the shared weights.
• Random (3): We reduce the maximum gradient norm from 5 to 1 to adjust for discrete architectures instead
of the weighted combination used by DARTS.
• Random (4): We further increase the number of epochs for training the proxy network with shared weights
to 300 and increase the number of architectures evaluated using the shared weights to 11k.
• Random (5): We separately increase the proxy network size to be as large as possible given the available
memory on a Nvidia Tesla P100 GPU (i.e. by ≈50% due to increasing the number of initial channels from
16 to 24).
The performance of the final architecture after retraining from scratch for each of these settings is shown in
Table 6. Similar to the PTB benchmark, the best setting for random search was Random (5), which has a larger
network size. The best trial for this setting reached a test error of 2.83 when retraining from scratch; we show the
normal and reduction cells found by this trial in Figure 3. In light of these stage (2) results, we focus in stage (3)
on the best architecture found by Random (5) Run 1, and achieve an average test error of 2.85 ± 0.08 over 10
random seeds as shown in Table 5.
4.2.3
Investigating Reproducibility. Our results in this section show that although DARTS appears broadly
reproducible, this result is surprising given the unstable ranking in architectures observed between 100 and 600
epochs for stage (2) evaluation. To begin, the first row of Table 6 shows our reproduced results for DARTS after
training the best architecture for each trial from scratch for 600 epochs. In our reproduced run, DARTS reaches
an average test error of 2.94 and a minimum of 2.77 across 4 trials (see Table 6). Note that this is not a direct
comparison to the published result for DARTS since there, the stage (2) evaluation was performed after training
for only 100 epochs.
Table 7. CIFAR-10 Benchmark: Ranking of Intermediate Test Error for DARTS. Architectures are retrained from
scratch using the proxyless network and the error on the test set is reported after training for the indicated number of epochs.
Rank is calculated across the 4 trials. We also show the average over 10 seeds for the best architecture from the top trial for
reference.
† These results were run before we fixed the non-determinism in DARTS code (see Appendix A.2).
Epochs
Across
Search
100
600
10 Seeds
Method
Trial Value Rank Value Rank Min
Avg
Reproduced
1
7.63
2
2.92
2
Darts†
2
7.67
3
2.77
1
2.62 2.78 ± 0.12
3
8.38
4
3.00
3
4
7.51
1
3.05
4
Delving into the intermediate results, we compare the performance of the best architectures across trials from
our independent run of DARTS after training each from scratch for 100 epochs and 600 epochs (see Table 7). We
see that the ranking is unstable between 100 epochs and 600 epochs, which motivated our strategy of training

16
•
Li and Talwalkar
Table 8. CIFAR-10 Benchmark: Broad Reproducibility of Random Search WS We report the stage 3 performance of
the final architecture from 6 independent runs of random search with weight-sharing.
† This run was performed using the DARTS code before we corrected for non-determinism (see Appendix A.2).
Test Error Across 10 Seeds
Run 1
Run 2†
Run 3
Run 4
Run 5
Run 6
Average
2.85 ± 0.08
2.86 ± 0.09
2.88 ± 0.10
2.95 ± 0.09
2.98 ± 0.12
3.00 ± 0.19
2.92
the final architectures across trials to 600 epochs in order to select the best architecture for final evaluation
across 10 seeds. This suggests we should be cautious when using noisy signals for the performance of different
architectures, especially since architecture search is conducted for DARTS and Random (5) for only 50 and 150
epochs respectively.
Finally, we investigate the variance of random search with weight-sharing with 5 additional runs as shown in
Table 8. The stage (3) evaluation of the best architecture for these 5 additional runs reveal that 2 out of 5 achieve
similar performance as Run 1, while the 3 remainder underperform but still reach a better test error than ASHA.
These broad reproducibility results show that random search with weight-sharing has high variance between
runs, which is not surprising given the change in intermediate rankings that we observed for DARTS.
4.3
Computational Cost
As mentioned in Section 2, there is a trade off between computational cost and the quality of the signal that
we get per architecture that we evaluate. To get a better sense of the tradeoff, we estimate the per architecture
computational cost of different methods considered in our experiments, noting that these methods differ in per
architecture cost by at least an order-of-magnitude as we move from expensive to cheaper evaluation methods:
(1) Full training: The random search baselines considered by Liu et al. [34] cost 0.5 GPU days per architecture
for the PTB benchmark and 4 GPU hours per architecture for the CIFAR-10 benchmark.
(2) Partial training: The amortized cost of ASHA is 9 minutes per architecture for the PTB benchmark and
19 minutes per architecture for the CIFAR-10 benchmark.
(3) Weight-sharing: It is difficult to quantify the equivalent number of architectures evaluated by DARTS
and random search with weight-sharing. For DARTS, the final architecture is taken to be the highest
weighted operation for each architectural decision, but it is unclear how much information is provided by
the gradient updates to the architecture mixture weights during architecture search. For random search
with weight sharing, although we evaluate a given number of architectures using the shared weights, as
stated in Section 3, this is a tunable meta-hyperparameter and the quality of the performance estimates we
receive can be noisy.3 Nonetheless, to provide a rough estimate of the cost per architecture for random
search with weight-sharing, we calculate the amortized cost by dividing the total search cost by the number
of architectures evaluated using the shared weights. Hence, the amortized cost for random search with
weight-sharing is 0.2 minutes per architecture for the PTB benchmark and 0.8 minutes per architecture for
the CIFAR-10 benchmark.
Despite the apparent computational savings from weight-sharing methods, without more robustness and
transparency, it is difficult to ascertain whether the total cost of applying existing weight-sharing methods to
NAS problems warrants their broad application. In particular, the total costs of ProxylessNAS, ENAS, and SNAS
are likely much higher than that reported in Table 2 and Table 5 since, as we saw with DARTS and random
search with weight-sharing, multiple trials are needed due to sensitivity to initialization. Additionally, while
3In principle, the equivalent number of architectures evaluated can be calculated by applying an oracle CDF of ground truth performance
over randomly sampled architectures to the performance of the architectures found by the shared weights.

Random Search and Reproducibility for Neural Architecture Search
•
17
we lightly tuned the meta-hyperparameter settings, we used DARTS’ settings as our starting point and it is
unclear whether the settings they use required considerable tuning. In contrast, we were able to achieve nearly
competitive performance with the default settings of ASHA using roughly the same total computation as that
needed by DARTS and random search with weight-sharing.
4.4
Available Code
Unless otherwise noted, our results are exactly reproducible from architecture search to final evaluation using
the code available at https://github.com/liamcli/randomNAS_release. The code we use for random search with
weight-sharing on both benchmarks is deterministic conditioned on a fixed random seed. We provide the final
architectures used for each of the trials shown in the tables above, as well as the random seeds used to find those
architectures. In addition, we perform no additional hyperparameter tuning for final architectures and only tune
the meta-hyperparameters according to the discussion in the text itself. We also provide code, final architectures,
and random seeds used for our experiments using ASHA. However, we note that there is one uncontrolled source
of randomness in our ASHA experiments—in the distributed setting, the asynchronous nature of the algorithm
means that the results depend on the order in which different architectures finish (partially) training. Lastly, our
experiments were conducted using Tesla P100 and V100 GPUs on Google Cloud. We convert GPU time on V100
to equivalent time on P100 by applying a multiple of 1.5.
5
CONCLUSION
We conclude by summarizing our results and proposing suggestions to push the field forward and foster broader
adoption of NAS methods.
(1) Better baselines that accurately quantify the performance gains of NAS methods. The perfor-
mance of random search with early-stopping evaluated in Section 4 reveals a surprisingly small performance
gap between leading general-purpose hyperparameter optimization methods and specialized methods
tailored for NAS. In traditional hyperparameter optimization benchmarks, random search has also been
shown to be a difficult baseline to beat. For these benchmarks, an informative measure of the performance
of a novel algorithm is its ‘multiple of random search,’ i.e., how much more compute would random search
need to achieve similar performance [29]. An analogous baseline could be useful for NAS, where the
impact of a novel NAS method can be quantified in terms of a multiplicative speedup relative to a standard
hyperparameter optimization method such as random search with early-stopping.
(2) Ablation studies that isolate the impact of individual NAS components. Our head-to-head experi-
mental evaluation of two variants of random search (with early stopping and with weight-sharing) allows
us to pinpoint the performance gains associated with the cheaper weight-sharing evaluation scheme. In
contrast, the fact that random search with weight-sharing is comparable in performance to leading NAS
methods calls into question the necessity of the auxiliary network used by GHN and the complicated
algorithmic components employed by ENAS, SNAS, and DARTS. Relatedly, while ProxylessNAS achieves
better average test error on CIFAR-10 than random search with weight-sharing, it is unclear to what
degree these performance gains are attributable to the search space, search method, and/or proxyless
shared-weights evaluation method. To promote scientific progress, we believe that ablation studies should
be conducted to answer these questions in isolation.
(3) Reproducible results that engender confidence and foster scientific progress. Reproducibility is a
core tenet of scientific progress and crucial to promoting wider adoption of NAS methods. In traditional
hyperparameter optimization, it is standard for empirical results to be reported over 10 independent
experimental runs [14, 25, 27, 29]. In contrast, as we discuss Section 2, results for NAS methods are often
reported over a single experimental run [7, 41, 47, 50], without exact reproducibility. This is a consequence

18
•
Li and Talwalkar
of the steep time and computational cost required to perform NAS experiments, e.g., generating the
experiments reported in this paper alone required several months of wall-clock time and tens of thousands
of dollars. However, in order to adequately differentiate between various methods, results need to be
reported over several independent experimental runs, especially given the nature of the extremal statistics
that are being reported. Consequently, we conclude that either significantly more computational resources
need to be devoted to evaluating NAS methods and/or more computationally tractable benchmarks need to
be developed to lower the barrier for performing adequate empirical evaluations. Relatedly, we feel it is
imperative to evaluate the merits of NAS methods not only on their accuracy, but also on their robustness
across these independent runs.
ACKNOWLEDGMENTS
We thank Maruan Al-Shedivat, Sebastian Caldas, Greg Ganger, Kevin Jamieson, Angela Jiang, Mikhail Khodak,
Gregory Plumb, Afshin Rostamizadeh, Virginia Smith, and Daniel Wong for helpful comments and valuable
discussion. Thanks also to Julien Siems and Frank Hutter’s group for their efforts to reproduce our work, which
led to insights on reproducibility and motivated additional experiments. This work was supported in part by
DARPA FA875017C0141, the National Science Foundation grants IIS1705121 and IIS1838017, an Okawa Grant, a
Google Faculty Award, an Amazon Web Services Award, and a Carnegie Bosch Institute Research Award. Any
opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and
do not necessarily reflect the views of DARPA, the National Science Foundation, or any other funding agency.
A
APPENDIX
A.1
PTB Benchmark
In this section, we provide additional detail for the experiments in Section 4.1.
Architecture Operations. In stage (1), DARTS trained the shared weights network with the zero operation
included in the list of considered operations but removed the zero operation when selecting the final architecture
to evaluate in stages (2) and (3). For our random search with weight-sharing, we decided to exclude the zero
operation for both search and evaluation.
Stage 3 Procedure. For stage (3) evaluation, we follow the ArXiv version of DARTS [33], which reported two
sets of results, one after training for 1600 epochs and another fine tuned result after training for an additional
1000 epochs. In the ICLR version, Liu et al. [34] simply say they trained the final network to convergence. We
trained for another 1000 epochs for a total of 3600 epochs to approximate training to convergence.
A.2
CIFAR-10 Benchmark
In this section, we provide additional detail for the experiments in Section 4.2.
Architecture Operations. In stage (1), DARTS trained the shared weights network with the zero operation
included in the list of considered operations but removed the zero operation when selecting the final architecture
to evaluate in stages (2) and (3). For our random search with weight-sharing, we decided to include the zero
operation for both search and evaluation.
Stage 1 Procedure. For random search with weight-sharing, after the shared weights are fully trained, we
evaluate randomly sampled architectures using the shared weights and select the best one for stage (2) evaluation.
Due to the higher cost of evaluating on the full validation set, we evaluate each architecture using 10 minibatches
instead. We split the total number of architectures to be evaluated into sets of 1000. For each 1000, we select the
best 10 according the cheap evaluation on part of the validation set and evaluate on the full validation set. Then
we select the top architecture across all sets of 1000 for stage (2) evaluation.

Random Search and Reproducibility for Neural Architecture Search
•
19
Reproducibility. The code released by Liu et al. [34] did not produce deterministic results for the CNN
benchmark due to non-determinism in CuDNN and in data loading. We removed the non-deterministic behavior
in CuDNN by setting
cudnn.benchmark = False
cudnn.deterministic = True
cudnn.enabled=True
Note that this only disables the non-deterministic functions in CuDNN and does not adversely affect training
time as much as turning off CuDNN completely. We fix additional non-determinism from data loading by setting
the seed for the random package in addition to numpy.random and pytorch seed and turning off multiple threads
for data loading.
We ran ASHA and one set of trials for Random Search (5) with weight-sharing using the non-deterministic code
before fixing the seeding to get deterministic results; all other settings for random search with weight-sharing are
deterministic. Hence, the result for ASHA does not satisfy exact reproduciblity due to non-deterministic training
and asynchronous updates.
REFERENCES
[1] G. Bender, P.-J. Kindermans, B. Zoph, V. Vasudevan, and Q. Le. Understanding and simplifying one-shot architecture search. In
International Conference on Machine Learning, 2018.
[2] Y. Bengio. Gradient-based optimization of hyperparameters. In Neural Computation, 2000.
[3] J. Bergstra and Y. Bengio. Random search for hyper-parameter optimization. Journal of Machine Learning Research, 13(Feb):281–305,
2012.
[4] J. Bergstra et al. Algorithms for hyper-parameter optimization. In Advances in Neural Information Processing Systems, 2011.
[5] A. Brock, T. Lim, J. Ritchie, and N. Weston. SMASH: One-shot model architecture search through hypernetworks. In International
Conference on Learning Representations, 2018.
[6] H. Cai, J. Yang, W. Zhang, S. Han, and Y. Yu. Path-level network transformation for efficient architecture search. In International
Conference on Machine Learning, 2018.
[7] H. Cai, L. Zhu, and S. Han. ProxylessNAS: Direct neural architecture search on target task and hardware. In International Conference on
Learning Representations, 2019.
[8] S. Cao, X. Wang, and K. M. Kitani. Learnable embedding space for efficient neural architecture compression. In International Conference
on Learning Representations, 2019.
[9] T. Devries and G. W. Taylor. Improved regularization of convolutional neural networks with cutout. 2017.
[10] T. Domhan, J. T. Springenberg, and F. Hutter. Speeding up automatic hyperparameter optimization of deep neural networks by
extrapolation of learning curves. In International Joint Conferences on Artificial Intelligence, 2015.
[11] T. Elsken, J. H. Metzen, and F. Hutter. Multi-objective Architecture Search for CNNs. 2018.
[12] T. Elsken, J. H. Metzen, and F. Hutter. Neural Architecture Search: A Survey. 2018.
[13] S. Falkner, A. Klein, and F. Hutter. Bohb: Robust and efficient hyperparameter optimization at scale. In International Conference on
Machine Learning, 2018.
[14] M. Feurer, A. Klein, K. Eggensperger, J. Springenberg, M. Blum, and F. Hutter. Efficient and robust automated machine learning. In
Advances in Neural Information Processing Systems, 2015.
[15] D. Golovin, B. Sonik, S. Moitra, G. Kochanski, J. Karro, and D.Sculley. Google vizier: A service for black-box optimization. In SIGKDD
Conference on Knowledge Discovery and Data Mining, 2017.
[16] Google. Google repo for amoebanet. https://github.com/tensorflow/tpu/tree/master/models/official/amoeba_net, 2018.
[17] Google. Google automl. https://cloud.google.com/automl/, 2018.
[18] Google. Google repo for nasnet. https://github.com/tensorflow/models/tree/master/research/slim/nets/nasnet, 2018.
[19] E. Hoffer, I. Hubara, and D. Soudry. Train longer, generalize better: closing the generalization gap in large batch training of neural
networks. In Advances in Neural Information Processing Systems, 2017.
[20] F. Hutter, H. Hoos, and K. Leyton-Brown. Sequential model-based optimization for general algorithm configuration. In Proc. of LION-5,
2011.
[21] M. Jaderberg, V. Dalibard, S. Osindero, W. Czarnecki, J. Donahue, A. Razavi, O. Vinyals, T. Green, I. Dunning, K. Simonyan, et al.
Population based training of neural networks. 2017.

20
•
Li and Talwalkar
[22] K. Jamieson and A. Talwalkar. Non-stochastic best arm identification and hyperparameter optimization. In International Conference on
Artificial Intelligence and Statistics, 2015.
[23] H. Jin, Q. Song, and X. Hu. Auto-Keras: Efficient Neural Architecture Search with Network Morphism. 2018.
[24] K. Kandasamy, G. Dasarathy, J. B. Oliva, J. Schneider, and B. Póczos. Gaussian process bandit optimisation with multi-fidelity evaluations.
In Advances in Neural Information Processing Systems, 2016.
[25] K. Kandasamy, G. Dasarathy, J. Schneider, and B. Póczos. Multi-fidelity bayesian optimisation with continuous approximations. In
International Conference on Machine Learning, 2017.
[26] K. Kandasamy, W. Neiswanger, J. Schneider, B. Poczos, and E. Xing. Neural Architecture Search with Bayesian Optimization and Optimal
Transport. Advances in Neural Information Processing Systems, 2018.
[27] A. Klein, S. Falkner, S. Bartels, P. Hennig, and F. Hutter. Fast bayesian optimization of machine learning hyperparameters on large
datasets. International Conference on Artificial Intelligence and Statistics, 2017.
[28] A. Krizhevsky. Learning multiple layers of features from tiny images. In Technical report, Department of Computer Science, Univsersity of
Toronto, 2009.
[29] L. Li, K. Jamieson, G. DeSalvo, A. Rostamizadeh, and A. Talwalkar. Hyperband: Bandit-based configuration evaluation for hyperparameter
optimization. International Conference on Learning Representation, 17, 2017.
[30] L. Li, K. G. Jamieson, A. Rostamizadeh, E. Gonina, M. Hardt, B. Recht, and A. Talwalkar. Massively parallel hyperparameter tuning. 2019.
[31] C. Liu, B. Zoph, M. Neumann, J. Shlens, W. Hua, L.-J. Li, L. Fei-Fei, A. Yuille, J. Huang, and K. Murphy. Progressive Neural Architecture
Search. European Conference on Computer Vision, 2018.
[32] H. Liu, K. Simonyan, O. Vinyals, C. Fernando, and K. Kavukcuoglu. Hierarchical representations for efficient architecture search. In
International Conference on Learning Representations, 2018.
[33] H. Liu, K. Simonyan, and Y. Yang. DARTS: differentiable architecture search. arXiv:1806.09055, 2018.
[34] H. Liu, K. Simonyan, and Y. Yang. DARTS: Differentiable architecture search. In International Conference on Learning Representations,
2019.
[35] R. Luo, F. Tian, T. Qin, E. Chen, and T.-Y. Liu. Neural Architecture Optimization. Advances In Neural Information Processing Systems,
2018.
[36] D. Maclaurin, D. Duvenaud, and R. Adams. Gradient-based hyperparameter optimization through reversible learning. In International
Conference on Machine Learning, 2015.
[37] M. Marcus, M. Marcinkiewicz, and B. Santorini. Building a large annotated corpus of english: The penn treebank. Computational
Linguistics, 19(2):313–330, 1993.
[38] S. Merity, N. Keskar, and R. Socher. Regularizing and optimizing LSTM language models. In International Conference on Learning
Representations, 2018.
[39] R. Negrinho and G. Gordon. DeepArchitect: Automatically Designing and Training Deep Architectures. 2017.
[40] R. S. Olson and J. H. Moore. Tpot: A tree-based pipeline optimization tool for automating machine learning. In Workshop on Automatic
Machine Learning, 2016.
[41] H. Pham, M. Guan, B. Zoph, Q. Le, and J. Dean. Efficient neural architecture search via parameters sharing. In International Conference
on Machine Learning, 2018.
[42] E. Real, S. Moore, A. Selle, S. Saxena, Y. Leon Suematsu, Q. Le, and A. Kurakin. Large-scale evolution of image classifiers. In ICML, 2017.
[43] E. Real, A. Aggarwal, Y. Huang, and Q. V. Le. Regularized Evolution for Image Classifier Architecture Search. 2018.
[44] J. Snoek, H. Larochelle, and R. P. Adams. Practical bayesian optimization of machine learning algorithms. In Advances in Neural
Information Processing Systems, 2012.
[45] K. Swersky, J. Snoek, and R. Adams. Multi-task bayesian optimization. In Advances in Neural Information Processing Systems, 2013.
[46] T. Wei, C. Wang, Y. Rui, and C. W. Chen. Network morphism. In International Conference on Machine Learning, 2016.
[47] S. Xie, H. Zheng, C. Liu, and L. Lin. SNAS: stochastic neural architecture search. In International Conference on Learning Representations,
2019.
[48] Y. Yamada, M. Iwamura, and K. Kise. Shakedrop regularization. 2018.
[49] Z. Yang, Z. Dai, R. Salakhutdinov, and W. W. Cohen. Breaking the softmax bottleneck: A high-rank RNN language model. In International
Conference on Learning Representations, 2018.
[50] C. Zhang, M. Ren, and R. Urtasun. Graph hypernetworks for neural architecture search. In International Conference on Learning
Representations, 2019.
[51] B. Zoph and Q. V. Le. Neural Architecture Search with Reinforcement Learning. International Conference on Learning Representation,
2017.
[52] B. Zoph, V. Vasudevan, J. Shlens, and Q. V. Le. Learning transferable architectures for scalable image recognition. In Conference on
Computer Vision and Pattern Recognition, 2018.
