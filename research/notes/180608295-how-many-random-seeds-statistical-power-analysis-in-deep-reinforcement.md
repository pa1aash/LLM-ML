---
title: '[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement
  Learning Experiments'
id: 180608295-how-many-random-seeds-statistical-power-analysis-in-deep-reinforcement
tags:
- llm-nas-feedback-positioning-7125b1
- nas-methodology
- random-search-baseline
created: '2026-08-16T15:45:02.114154Z'
updated: '2026-08-16T15:51:01.459675Z'
source: https://arxiv.org/abs/1806.08295
source_domain: arxiv.org
fetched_at: '2026-08-16T15:45:02.113639Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Colas, Sigaud & Oudeyer (2018) tutorial establishing how many random seeds
  are statistically required to compare two algorithms'' performance with adequate
  power, using t-tests and bootstrap confidence intervals, plus guidance on the consequences
  of violating test assumptions (non-normality, unequal variance). Written for deep
  RL reproducibility but is the standard methodological citation across empirical
  deep-learning subfields, including NAS, for ''how many seeds/runs justify a significance
  claim.'' Directly bears on the paper''s methodology defensibility: a claim that
  a handful of LLM-proposed architectures (or a small number of random-search runs)
  differ from each other requires a seed count and statistical test calibrated by
  exactly this kind of power analysis — reviewers following this standard would flag
  single-run or few-run comparisons between LLM proposals and random search as statistically
  underpowered regardless of which mean looks larger.'
---

[1806.08295] How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:1806.08295
(cs)
[Submitted on 21 Jun 2018 (
v1
), last revised 5 Jul 2018 (this version, v2)]
Title:
How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
Authors:
Cédric Colas
,
Olivier Sigaud
,
Pierre-Yves Oudeyer
View a PDF of the paper titled How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments, by C\'edric Colas and Olivier Sigaud and Pierre-Yves Oudeyer
View PDF
HTML (experimental)
Abstract:
Consistently checking the statistical significance of experimental results is one of the mandatory methodological steps to address the so-called "reproducibility crisis" in deep reinforcement learning. In this tutorial paper, we explain how the number of random seeds relates to the probabilities of statistical errors. For both the t-test and the bootstrap confidence interval test, we recall theoretical guidelines to determine the number of random seeds one should use to provide a statistically significant comparison of the performance of two algorithms. Finally, we discuss the influence of deviations from the assumptions usually made by statistical tests. We show that they can lead to inaccurate evaluations of statistical errors and provide guidelines to counter these negative effects. We make our code available to perform the tests.
Subjects:
Machine Learning (cs.LG)
; Machine Learning (stat.ML)
Cite as:
arXiv:1806.08295
[cs.LG]
(or
arXiv:1806.08295v2
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.1806.08295
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Olivier Sigaud [
view email
]
[v1]
Thu, 21 Jun 2018 15:39:19 UTC (3,827 KB)
[v2]
Thu, 5 Jul 2018 06:50:33 UTC (3,827 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments, by C\'edric Colas and Olivier Sigaud and Pierre-Yves Oudeyer
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
2018-06
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
Cédric Colas
Olivier Sigaud
Pierre-Yves Oudeyer
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

How Many Random Seeds? Statistical Power
Analysis in Deep Reinforcement Learning
Experiments
C´edric Colas1, Olivier Sigaud1,2 and Pierre-Yves Oudeyer1
1INRIA, Flowers team, Bordeaux, France
2Sorbonne Universit´e, ISIR, Paris, France
Abstract
Consistently checking the statistical signiﬁcance of experimental results
is one of the mandatory methodological steps to address the so-called
“reproducibility crisis” in deep reinforcement learning. In this tutorial paper,
we explain how the number of random seeds relates to the probabilities of
statistical errors. For both the t-test and the bootstrap conﬁdence interval
test, we recall theoretical guidelines to determine the number of random
seeds one should use to provide a statistically signiﬁcant comparison of
the performance of two algorithms. Finally, we discuss the inﬂuence of
deviations from the assumptions usually made by statistical tests. We
show that they can lead to inaccurate evaluations of statistical errors and
provide guidelines to counter these negative eﬀects. We make our code
available to perform the tests1.
1
Introduction
Reproducibility in Machine Learning and Deep Reinforcement Learning (RL)
in particular has become a serious issue in the recent years. As pointed out
in (Islam et al., 2017) and (Henderson et al., 2017), reproducing the results
of an RL paper can turn out to be much more complicated than expected.
Indeed, codebases are not always released and scientiﬁc papers often omit parts
of the implementation tricks. Recently, Henderson et al. conducted a thorough
investigation of various parameters causing this reproducibility crisis. They
used trendy deep RL algorithms such as DDPG (Lillicrap et al., 2015), ACKTR
(Wu et al., 2017), TRPO (Schulman et al., 2015) and PPO (Schulman et al.,
2017) with OpenAI Gym (Brockman et al., 2016) popular benchmarks such as
Half-Cheetah, Hopper and Swimmer, to study the eﬀects of the codebase, the
size of the networks, the activation function, the reward scaling or the random
seeds. Among other results, they showed that diﬀerent implementations of the
same algorithm with the same set of hyper-parameters led to drastically diﬀerent
results.
1Available on github at https://github.com/flowersteam/rl-difference-testing
1
arXiv:1806.08295v2  [cs.LG]  5 Jul 2018

Perhaps the most surprising thing is this: running the same algorithm 10
times with the same hyper-parameters using 10 diﬀerent random seeds and
averaging performance over two splits of 5 seeds can lead to learning curves
seemingly coming from diﬀerent statistical distributions. Notably, all the deep
RL papers reviewed by Henderson et al.. (theirs included) used 5 seeds or less.
Even worse, some papers actually report the average of the best performing
runs. As demonstrated in (Henderson et al., 2017), these methodologies can lead
to claim that two algorithms performances are diﬀerent when they are not. A
solution to this problem is to use more random seeds, to average more diﬀerent
trials in order to obtain a more robust measure of the algorithm performance.
But how can one determine how many random seeds should be used? Shall we
use 5, 10 or 100, as in (Mania et al., 2018)?
This work assumes one wants to test a diﬀerence in performance between two
algorithms. Section 2 gives deﬁnitions and describes the statistical problem of
diﬀerence testing while Section 3 proposes two statistical tests to answer this
problem. In Section 4, we present standard guidelines to choose the sample size
so as to meet requirements in the two types of statistical errors. Finally, we
challenge the assumptions made in the previous section and propose guidelines
to estimate error rates empirically in Section 5. The code is available on Github
at https://github.com/flowersteam/rl-difference-testing.
Figure 1: Algo1 versus Algo2 are two famous Deep RL algorithms, here tested on the
Half-Cheetah benchmark. The mean and conﬁdence interval for 5 seeds are reported.
We might consider that Algo1 outperforms Algo2 because there is not much overlap
between the 95% conﬁdence intervals. But is it suﬃcient evidence that Algo1 really
performs better? Below, we show that the performances of these algorithms is actually
the same, and explain which methods should be used to have more reliable evidence of
the (non-)diﬀerence among two algorithms.
2

2
Deﬁnition of the statistical problem
2.1
First deﬁnitions
Two runs of the same algorithm often yield diﬀerent measures of performance.
This might be due to various factors such as the seed of the random generators
(called random seed or seed thereafter), the initial state of the agent, the stochas-
ticity of the environment, etc. Formally, the performance of an algorithm can be
modeled as a random variable X and running this algorithm in an environment
results in a realization xi. Repeating the procedure N times, one obtains a
statistical sample x = (x1, .., xN). A random variable is usually characterized
by its expected value or mean µ and its standard deviation, noted σ. While the
mean characterizes the expected value of a realization, the standard deviation
evaluates the square root of the squared deviations to this mean, or in simpler
words, how far from the mean the realization are expected to fall. Of course,
the values of µ and σ are unknown. The only thing one can do is to compute
their unbiased estimations x and s:
x ˆ=
n
X
i=1
xi,
s ˆ=
sPN
i+1(xi −x)2
N −1
,
(1)
where x is called the empirical mean, and s is called the empirical standard
deviation. The larger the sample size N, the more conﬁdence one can be in the
estimations.
Here, two algorithms with respective performances X1 and X2 are compared.
If X1 and X2 follow normal distributions, the random variable describing their
diﬀerence (Xdiﬀ= X1 −X2) also follows a normal distribution with parameters
σdiﬀ= (σ2
1 + σ2
2)1/2 and µdiﬀ= µ1 −µ2. In this case, the estimator of the mean
of Xdiﬀis xdiﬀ= x1 −x2 and the estimator of σdiﬀis sdiﬀ=
p
s2
1 + s2
2. The
eﬀect size ϵ can be deﬁned as the diﬀerence between the mean performances of
both algorithms: ϵ = µ1 −µ2.
Testing for a diﬀerence between the performances of two algorithms (µ1 and
µ2) is mathematically equivalent to testing a diﬀerence between their diﬀerence
µdiﬀand 0. The second point of view is considered from now on. We draw a
sample xdiﬀfrom Xdiﬀby subtracting two samples x1 and x2 obtained from X1
and X2.
3

Example 1. To illustrate diﬀerence testing, we use two algorithms (Algo1
and Algo2) and compare them on the Half-Cheetah environment from
the OpenAI Gym framework (Brockman et al., 2016). The algorithms
implemented are not so important here and will be revealed later. First,
we run a study with N = 5 random seeds for each. Figure 1 shows the
average learning curves with 95% conﬁdence intervals. Each point of a
learning curve is the average cumulated reward over 10 evaluation episodes.
The measure of performance Xi of Algo i is the average performance over
the last 10 points (i.e. last 100 evaluation episodes). From Figure 1, it
seems that Algo1 performs better than Algo2. Moreover, the conﬁdence
intervals do not seem to overlap much. However, we need to run statistical
tests before drawing any conclusion.
2.2
Comparing performances with a diﬀerence test
In a diﬀerence test, statisticians deﬁne the null hypothesis H0 and the alternate
hypothesis Ha. H0 assumes no diﬀerence whereas Ha assumes one:
• H0: µdiﬀ= 0
• Ha: µdiﬀ̸ = 0
These hypotheses refer to the two-tail case. When an a priori on which algorithm
performs best is available, (say Algo1), one can use the one-tail version:
• H0: µdiﬀ≤0
• Ha: µdiﬀ> 0
At ﬁrst, a statistical test always assumes the null hypothesis. Once a sample
xdiﬀis collected from Xdiﬀ, one can estimate the probability p (called p-value) of
observing data as extreme, under the null hypothesis assumption. By extreme,
one means far from the null hypothesis (xdiﬀfar from 0). The p-value answers
the following question: how probable is it to observe this sample or a more
extreme one, given that there is no true diﬀerence in the performances of both
algorithms? Mathematically, we can write it this way for the one-tail case:
p-value = P(Xdiﬀ≥xdiﬀ| H0),
(2)
and this way for the two-tail case:
p-value =
 P(Xdiﬀ≥xdiﬀ| H0)
if xdiﬀ> 0
P(Xdiﬀ≤xdiﬀ| H0)
if xdiﬀ≤0.
(3)
When this probability becomes really low, it means that it is highly improb-
able that two algorithms with no performance diﬀerence produced the collected
4

sample xdiﬀ. A diﬀerence is called signiﬁcant at signiﬁcance level α when the
p-value is lower than α in the one-tail case, and lower than α/2 in the two tail
case (to account for the two-sided test2). Usually α is set to 0.05 or lower. In
this case, the low probability to observe the collected sample under hypothesis
H0 results in its rejection. Note that a signiﬁcance level α = 0.05 still results
in 1 chance out of 20 to claim a false positive, to claim that there is a true
diﬀerence when there is not. It is important to note that, when one is conduct-
ing NE experiments, the false positive rate grows linearly with the number of
experiments. In this case, one should use correction for multiple comparisons
such as the Bonferroni correction αBon = α/NE (Rice, 1989). This controls the
familywise error rate (FWER), the probability of rejecting at least one true null
hypothesis (FWER < α). Its use is discussed in (Cabin and Mitchell, 2000).
Another way to see this, is to consider conﬁdence intervals. Two kinds of
conﬁdence intervals can be computed:
• CI1: The 100 · (1 −α) % conﬁdence interval for the mean of the diﬀerence
µdiﬀgiven a sample xdiﬀcharacterized by xdiﬀand sdiﬀ.
• CI2: The 100 · (1 −α) % conﬁdence interval for any realization of Xdiﬀ
under H0 (assuming µdiﬀ= 0).
Having CI2 that does not include xdiﬀis mathematically equivalent to a p-value
below α. In both cases, it means there is less than 100 · α% chance that µdiﬀ= 0
under H0. When CI1 does not include 0, we are also 100 · (1 −α) % conﬁdent
that µ̸ = 0, without assuming H0. Proving one of these things leads to conclude
that the diﬀerence is signiﬁcant at level α.
2.3
Statistical errors
In hypothesis testing, the statistical test can conclude H0 or Ha while each of
them can be either true or false. There are four cases:
Table 1: Hypothesis testing
predicted/true
H0
Ha
H0
True negative
1 −α
False negative
β
Ha
False positive
α
True positive
1 −β
2See Wikipedia’s article for more details on one-tail versus two-tail tests: https://en.
wikipedia.org/wiki/One-_and_two-tailed_tests
5

This leads to two types of errors:
• The type-I error rejects H0 when it is true, also called false positive.
This corresponds to claiming the superiority of an algorithm over another
when there is no true diﬀerence. Note that we call both the signiﬁcance
level and the probability of type-I error α because they both refer to the
same concept. Choosing a signiﬁcance level of α enforces a probability of
type-I error α, under the assumptions of the statistical test.
• The type-II error fails to reject H0 when it is false, also called false
negative. This corresponds to missing the opportunity to publish an article
when there was actually something to be found.
Message 1:
• In the two-tail case, the null hypothesis H0 is µdiﬀ= 0.
The
alternative hypothesis Ha is µdiﬀ̸ = 0.
• p-value = P(Xdiﬀ≥xdiﬀ| H0).
• A diﬀerence is said statistically signiﬁcant when a statistical test
passed. One can reject the null hypothesis when 1) p-value< α; 2)
CI1 does not contain 0; 3) CI2 does not contain xdiﬀ.
• statistically signiﬁcant does not refer to the absolute truth. Two
types of error can occur. Type-I error rejects H0 when it is true.
Type-II error fails to reject H0 when it is false.
• The rate of false positive is 1 out of 20 for α = 0.05. It grows
linearly with the number of experiment NE. Correction procedures
can be applied to correct for multiple comparisons.
3
Choice of the appropriate statistical test
In statistics, a diﬀerence cannot be proven with 100% conﬁdence. To show
evidence for a diﬀerence, we use statistical tests. All statistical tests make
assumptions that allow them to evaluate either the p-value or one of the conﬁdence
intervals described in the Section 2. The probability of the two error types must
be constrained, so that the statistical test produces reliable conclusions. In this
section we present two statistical tests for diﬀerence testing. As recommended
in Henderson et al. (2017), the two-sample t-test and the bootstrap conﬁdence
interval test can be used for this purpose3.
3Henderson et al. also advised for the Kolmogorov-Smirnov test which tests whether
two samples comes from the same distribution. This test should not be used to compare RL
algorithms because it is unable to prove any order relation.
6

3.1
T-test and Welch’s t-test
We want to test the hypothesis that two populations have equal means (null
hypothesis H0). A 2-sample t-test can be used when the variances of both
populations (both algorithms) are assumed equal. However, this assumption
rarely holds when comparing two diﬀerent algorithms (e.g. DDPG vs TRPO).
In this case, an adaptation of the 2-sample t-test for unequal variances called
Welch’s t-test should be used (Welch, 1947). Both tests are strictly equivalent
when the standard deviations are equal. T-tests make a few assumptions:
• The scale of data measurements must be continuous and ordinal (can be
ranked). This is the case in RL.
• Data is obtained by collecting a representative sample from the population.
This seem reasonable in RL.
• Measurements are independent from one another. This seems reasonable
in RL.
• Data is normally-distributed, or at least bell-shaped. The normal law
being a mathematical concept involving inﬁnity, nothing is ever perfectly
normally distributed. Moreover, measurements of algorithm performances
might follow multi-modal distributions. In Section, 5, we investigate the
eﬀects of deviations from normality.
Under these assumptions, one can compute the t-statistic t and the degree
of freedom ν for the Welch’s t-test as estimated by the Welch–Satterthwaite
equation, such as:
t =
xdiﬀ
q
s2
1
N1 + s2
2
N2
,
ν ≈

s2
1
N1 + s2
2
N2
2
s4
1
N2
1 (N1−1) +
s4
2
N2
2 (N2−1)
,
(4)
with xdiﬀ= x1 −x2; s1, s2 the empirical standard deviations of the two samples,
and N1, N2 their sizes. Sample sizes are assumed equal (N1 = N2 = N) thereafter.
The t-statistics are assumed to follow a t-distribution, which is bell-shaped and
whose width depends on the degree of freedom. The higher this degree, the
thinner the distribution.
Figure 2 helps making sense of these concepts. It represents the distribution of
the t-statistics corresponding to Xdiﬀ, under H0 (left distribution) and under Ha
(right distribution). H0 assumes µdiﬀ= 0, the distribution is therefore centered
on 0. Ha assumes a (positive) diﬀerence µdiﬀ= ϵ, the distribution is therefore
shifted by the t-value corresponding to ϵ, tϵ. Note that we consider the one-tail
case here, and test for a positive diﬀerence.
7

A t-distribution is deﬁned by its probability density function T ν
distrib(τ) (left
curve in Figure 2), which is parameterized by ν. The cumulative distribution
function CDFH0(t) is the function evaluating the area under T ν
distrib(t) from
τ = −∞to τ = t. This allows to write:
p-value = 1 −CDFH0(t) = 1 −
Z t
−∞
T ν
distrib(τ) · dτ.
(5)
Figure 2: Representation of H0 and Ha under the t-test assumptions. Areas under the
distributions represented in red, dark blue and light blue correspond to the probability
of type-I error α, type-II error β and the statistical power 1 −β respectively.
In Figure 2, tα represents the critical t-value to satisfy the signiﬁcance level
α in the one-tail case. When t = tα, p-value= α. When t > tα, the p-value is
lower than α and the test rejects H0. On the other hand, when t is lower than
tα, the p-value is superior to α and the test fails to reject H0. As can be seen in
the ﬁgure, setting the threshold at tα might also cause an error of type-II. The
rate of this error (β) is represented by the dark blue area: under the hypothesis
of a true diﬀerence ϵ (under Ha, right distribution), we fail to reject H0 when t
is inferior to tα. β can therefore be computed mathematically using the CDF:
β = CDFHa(tα) =
Z tα
−∞
T ν
distrib(τ −tϵ) · dτ.
(6)
Using the translation properties of integrals, we can rewrite β as:
β = CDFH0(tα −tϵ) =
Z tα−tϵ
−∞−tϵ=−∞
T ν
distrib(τ) · dτ.
(7)
The procedure to run a Welch’s t-test given two samples (x1, x2) is:
• Computing the degree of freedom ν and the t-statistic t based on s1, s2,
N and xdiﬀ.
• Looking up the tα value for the degree of freedom ν in a t-table4 or by
4Available at http://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf.
8

evaluating the inverse of the CDF function in α.
• Compare the t-statistic to tα. The diﬀerence is said statistically signiﬁcant
(H0 rejected) at level α when t ≥tα.
Note that t < tα does not mean there is no diﬀerence between the performances
of both algorithms. It only means there is not enough evidence to prove its
existence with 100·(1−α)% conﬁdence (it might be a type-II error). Noise might
hinder the ability of the test to detect the diﬀerence. In this case, increasing the
sample size N could help uncover the diﬀerence.
Selecting the signiﬁcance level α of the t-test enforces the probability of type-I
error to α. However, Figure 2 shows that decreasing this probability boils down
to increasing tα, which in turn increases the probability of type-II error β. One
can decrease β while keeping α constant by increasing the sample size N. This
way, the estimation xdiﬀof µdiﬀgets more accurate, which translates in thinner
distributions in the ﬁgure, resulting in a smaller β. The next section gives
standard guidelines to select N so as to meet requirements for both α and β.
3.2
Bootstrapped conﬁdence intervals
Bootstrapped conﬁdence interval is a method that does not make any assumption
on the distribution of Xdiﬀ. It estimates the conﬁdence interval CI1 for µdiﬀ,
given a sample xdiﬀcharacterized by its empirical mean xdiﬀ. It is done by
re-sampling inside xdiﬀand by computing the mean of each newly generated
sample. The test makes its decision based on whether the conﬁdence interval of
xdiﬀcontains 0 or not. It does not compute a p-value as such.
Without any assumption on the data distribution, an analytical conﬁdence
interval cannot be computed. Here, Xdiﬀfollows an unknown distribution F. An
estimation of the conﬁdence interval CI1 can be computed using the bootstrap
principle.
Let us say we have a sample xdiﬀmade of N measures of performance diﬀerence.
The empirical bootstrap sample x∗
diﬀof size N is obtained by sampling with
replacement inside xdiﬀ. The bootstrap principle then says that, for any statistic
u computed on the original sample and u∗computed on the bootstrap sample,
variations in u are well approximated by variations in u∗5. Therefore, variations
of the empirical mean such as its range can be approximated by variations of
the bootstrapped samples. The bootstrap conﬁdence interval test assumes the
sample size is large enough to represent the underlying distribution correctly,
although this might be diﬃcult to achieve in practice. Deviations from this
5More explanations and justiﬁcations can be found in https://ocw.mit.edu/courses/
mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/
readings/MIT18_05S14_Reading24.pdf.
9

assumption are discussed in Section 5. Under this assumption, the bootstrap
test procedure looks like this:
• Generate B bootstrap samples of size N from the original sample x1 of
Algo1 and B samples from from the original sample x2 of Algo2.
• Compute the empirical mean for each sample: µ1
1, µ2
1, ..., µB
1 and µ1
2, µ2
2, ..., µB
2
• Compute the diﬀerences µ1:B
diﬀ= µ1:B
1
−µ1:B
2
• Compute the bootstrapped conﬁdence interval at 100 · (1 −α)%. This is
basically the range between the 100 · α/2 and 100 · (1 −α)/2 percentiles
of the vector µ1:B
diﬀ(e.g. for α = 0.05, the range between the 2.5th and the
97.5th percentiles).
The number of bootstrap samples B should be chosen large (e.g. > 1000). If
the conﬁdence interval does not contain 0, it means that one can be conﬁdent
at 100 · (1 −α)% that the diﬀerence is either positive (both bounds positive) or
negative (both bounds negative), thus, that there is a statistically signiﬁcant
diﬀerence between the performances of both algorithms6.
Example 1 (continued). Here, the type-I error requirement is set
to α = 0.05. Running the Welch’s t-test and the bootstrap conﬁdence
interval test with two samples (x1, x2) of 5 seeds each leads to a p-
value of 0.031 and a bootstrap conﬁdence interval such that P
 µdiﬀ∈
[259, 1564]

= 0.05. Since the p-value is below the signiﬁcance level α and
the CI1 conﬁdence interval does not include 0, both test passed. This
means both tests found a signiﬁcant diﬀerence between the performances
of Algo1 and Algo2 with a 95% conﬁdence. There should have been only
5% chance to conclude a signiﬁcant diﬀerence if it did not exist.
In fact, we did encounter a type-I error. We know this for sure because
Algo 1 and Algo 2 were the exact same algorithm. They are both
the canonical implementation of DDPG (Lillicrap et al., 2015) from the
OpenAI baselines (Dhariwal et al., 2017). The ﬁrst conclusion was wrong,
we committed a type-I error, rejecting H0 when it was true. We knew
this could happen with probability α = 0.05. Section 5 shows that this
probability might have been under-evaluated because of the assumptions
made by the statistical tests.
6An implementation of the bootstrap conﬁdence interval test can be found at https:
//github.com/facebookincubator/bootstrapped.
10

Message 2:
• T-tests assume t-distributions of the t-values. Under some assump-
tions, they can compute analytically the p-value and the conﬁdence
interval CI2 at level α.
• The Welch’s t-test does not assume both algorithms have equal
variances but the t-test does.
• The bootstrapped conﬁdence interval test does not make assump-
tions on the performance distribution and estimates empirically the
conﬁdence interval CI1 at level α.
• Selecting a test with a signiﬁcance level α enforces a type-I error α
when the assumptions of the test are veriﬁed.
4
In theory: power analysis for the choice of the
sample size
In the Section 3, we saw that α was enforced by the choice of the signiﬁcance level
in the test implementation. The second type of error β must now be estimated.
β is the probability to fail to reject H0 when Ha is true. When the eﬀect size ϵ
and the probability of type-I error α are kept constant, β is a function of the
sample size N. Choosing N so as to meet requirements on β is called statistical
power analysis. It answers the question: what sample size do I need to have 1−β
chance to detect an eﬀect size ϵ, using a test with signiﬁcance level α? The next
paragraphs present guidelines to choose N in the context of a Welch’s t-test.
As we saw in Section 3.1, β can be analytically computed as:
β = CDFH0(tα −tϵ) =
Z tα−tϵ
−∞−tϵ=−∞
T ν
distrib(τ) · dτ,
(8)
where CDFH0 is the cumulative distribution function of a t-distribution cen-
tered on 0, tα is the critical value for signiﬁcance level α and tϵ is the t-value
corresponding to an eﬀect size ϵ. In the end, β depends on α, ϵ, (s1, s2) the
empirical standard deviations computed on two samples (x1, x2) and the sample
size N.
Example 2. To illustrate, we compare two DDPG variants: one with
action perturbations (Algo1) (Lillicrap et al., 2015), the other with
parameter perturbations (Algo2) (Plappert et al., 2017). Both algorithms
are evaluated in the Half-Cheetah environment from the OpenAI Gym
framework (Brockman et al., 2016).
11

4.1
Step 1 - Running a pilot study
To compute β, we need estimates of the standard deviations of the two algorithms
(s1, s2). In this step, the algorithms are run in the environment to gather two
samples x1 and x2 of size n. From there, we can compute the empirical means
(x1, x2) and standard deviations (s1, s2).
Example 2 (continued). Here we run both algorithms with n = 5.
We ﬁnd empirical means (x1, x2) = (3523, 4905) and empirical standard
deviations (s1, s2) = (1341, 990) for Algo1 (blue) and Algo2 (red) respec-
tively. From Figure 3, it seems there is a slight diﬀerence in the mean
performances xdiﬀ= x2 −x1 > 0.
Running preliminary statistical tests at level α = 0.05 lead to a p-value
of 0.1 for the Welch’s t-test, and a bootstrapped conﬁdence interval of
CI1 = [795, 2692] for the value of xdiﬀ= 1382. The Welch’s t-test does
not reject H0 (p-value> α) but the bootstrap test does (0̸ ∈CI1). One
should compute β to estimate the chance that the Welch’s t-test missed
an underlying performance diﬀerence (type-II error).
Figure 3: DDPG with action perturbation versus DDPG with parameter perturbation
tested in Half-Cheetah. Mean and 95% conﬁdence interval computed over 5 seeds are
reported. The ﬁgure shows a small diﬀerence in the empirical mean performances.
12

4.2
Step 2 - Choosing the sample size
Given a statistical test (Welch’s t-test), a signiﬁcance level α (e.g. α = 0.05) and
empirical estimations of the standard deviations of Algo1 and Algo2 (s1, s2),
one can compute β as a function of the sample size N and the eﬀect size ϵ one
wants to be able to detect.
Example 2 (continued). For N in [2, 50] and ϵ in [0.1, .., 1] × x1, we
compute tα and ν using the formulas given in Section 3.1, as well as tϵ
for each ϵ. Finally, we compute the corresponding probability of type-II
error β using Equation 8. Figure 4 shows the evolution of β as a function
of N for the diﬀerent ϵ.
Considering the semi-dashed black line for
ϵ = xdiﬀ= 1382, we ﬁnd β = 0.51 for N = 5: there is 51% chance of
making a type-II error when trying to detect an eﬀect ϵ = 1382. To meet
the requirement β = 0.2, N should be increased to N = 10 (β = 0.19).
Figure 4: Evolution of the probability of type-II error as a function of the sample size
N for various eﬀect sizes ϵ, when (s1, s2) = (1341, 990) and α = 0.05. The requirement
0.2 is represented by the horizontal dashed black line. The curve for ϵ = xdiﬀis
represented by the semi-dashed black line.
In our example, we ﬁnd that N = 10 was enough to be able to detect an
eﬀect size ϵ = 1382 with a Welch’s t-test, using signiﬁcance level α and using
empirical estimations (s1, s2) = (1341, 990). However, let us keep in mind that
these computations use various approximations (ν, s1, s2) and make assumptions
about the shape of the t-values distribution. Section 5 investigates the inﬂuence
of these assumptions.
13

4.3
Step 3 - Running the statistical tests
Both algorithms should be run so as to obtain a sample xdiﬀof size N. The
statistical tests can be applied.
Example 2 (continued). Here, we take N = 10 and run both the
Welch’s t-test and the bootstrap test. We now ﬁnd empirical means
(x1, x2) = (3690, 5323) and empirical standard deviations (s1, s2) =
(1086, 1454) for Algo1 and Algo2 respectively. Both tests rejected H0,
with a p-value of 0.0037 for the Welch’s t-test and a conﬁdence interval for
the diﬀerence µdiﬀ∈[732, 2612] for the bootstrap test. Both tests passed.
In Figure 5, plots for N = 5 and N = 10 can be compared. With a larger
number of seeds, the diﬀerence that was not found signiﬁcant with N = 5
is now more clearly visible. With a larger number of seeds, the estimate
xdiﬀis more robust, more evidence is available to support the claim that
Algo2 outperforms Algo1, which translates to tighter conﬁdence intervals
represented in the ﬁgures.
Figure 5: Performance of DDPG with action perturbation (Algo1) and parameter
perturbation (Algo2) with N = 5 seeds (left) and N = 10 seeds (right). The 95%
conﬁdence intervals on the right are smaller, because more evidence is available (N
larger). The underlying diﬀerence appears when N grows.
Message 3: Given a sample size N, a minimum eﬀect size to detect ϵ
and a requirement on type-I error α the probability of type-II error β can
be computed. This computation relies on the assumptions of the t-test.
The sample size N should be chosen so as to meet the requirements on β.
14

5
In practice: inﬂuence of deviations from as-
sumptions
Under their respective assumptions, the t-test and bootstrap test enforce the
probability of type-I error to the selected signiﬁcance level α. These assumptions
should be carefully checked, if one wants to report the probability of errors
accurately. First, we propose to compute an empirical evaluation of the type-
I error based on experimental data, and show that: 1) the bootstrap test is
sensitive to small sample sizes; 2) the t-test might slightly under-evaluate the
type-I error for non-normal data. Second, we show that inaccuracies in the
estimation of the empirical standard deviations s1 and s2 due to low sample
size might lead to large errors in the computation of β, which in turn leads to
under-estimate the sample size required for the experiment.
5.1
Empirical estimation of the type-I error
Remember, type-I errors occur when the null hypothesis (H0) is rejected in favor
of the alternative hypothesis (Ha), H0 being correct. Given the sample size N,
the probability of type-I error can be estimated as follows:
• Run twice this number of trials (2×N) for a given algorithm. This ensures
that H0 is true because all measurements come from the same distribution.
• Get average performance over two randomly drawn splits of size N. Con-
sider both splits as samples coming from two diﬀerent algorithms.
• Test for the diﬀerence of both ﬁctive algorithms and record the outcome.
• Repeat this procedure T times (e.g. T = 1000)
• Compute the proportion of time H0 was rejected. This is the empirical
evaluation of α.
Example 3 We use Algo1 from Example 2. From 42 available measures
of performance, the above procedure is run for N in [2, 21]. Figure 6
presents the results. For small values of N, empirical estimations of the
false positive rate are much larger than the supposedly enforced value
α = 0.05.
15

Figure 6:
Empirical estimations of the false positive rate on experimental data
(Example 3) when N varies, using the Welch’s t-test (blue) and the bootstrap conﬁdence
interval test (orange).
In our experiment, the bootstrap conﬁdence interval test should not be used
with small sample sizes (< 10). Even in this case, the probability of type-I error
(≈10%) is under-evaluated by the test (5%). The Welch’s t-test controls for
this eﬀect, because the test is much harder to pass when N is small (due to
the increase of tα). However, the true (empirical) false positive rate might still
be slightly under-evaluated. In this case, we might want to set the signiﬁcance
level to α < 0.05 to make sure the true positive rate stays below 0.05. In the
bootstrap test, the error is due to the inability of small samples to correctly
represent the underlying distribution, which impairs the enforcement of the false
positive rate to the signiﬁcance level α. Concerning the Welch’s t-test, this might
be due to the non-normality of our data (whose histogram seems to reveal a
bimodal distribution). In Example 1, we used N = 5 and encountered a type-I
error. We can see on the Figure 6 that the probability of this to happen was
around 10% for the bootstrap test and above 5% for the Welch’s t-test.
5.2
Inﬂuence of the empirical standard deviations
The Welch’s t-test computes t-statistics and the degree of freedom ν based on
the sample size N and the empirical estimations of standard deviations s1 and
s2. When N is low, estimations s1 and s2 under-estimate the true standard
deviation in average. Under-estimating (s1, s2) leads to smaller ν and lower tα,
which in turn leads to lower estimations of β. Finally, ﬁnding lower β leads to
the selection of smaller sample size N to meet β requirements. Let us investigate
how big this eﬀect can be. In Figure 7, one estimates the standard deviation
of a normally distributed variable N(0, 1). The empirical estimation s is quite
variable and underestimates σ = 1 in average.
16

Figure 7: Empirical standard deviation of X ∼N(0, 1). The true standard deviation
σ = 1 is represented in red. Mean +/- std are shown.
We consider estimations of the false negative rate as a function of N when
comparing two normal distributions (σ = 1), one centered on 3, the other on
3 + ϵ. When we select n = 5 for a preliminary study and compute estimations
(s1, s2) from this sample, our average error is mean(sn=5)= −0.059 (see above
Figure 7). One could also make larger errors: mean(sn=5)−std(sn=5)= −0.40
from the same ﬁgure.
Figure 8 shows the eﬀect of an error of 0.40 on the evaluation of β. One can
see that, if we want to detect an eﬀect size ϵ = 0.9 (green curve) and meet a
requirement β = 0.2, one would choose N = 17 when standard deviations are
correctly estimated (left) and N = 7 when they are under-evaluated. When
the number of samples n available in the preliminary study to compute (s1, s2)
grows, the under-estimation reduces in average and in the worst case. This, in
turn, reduces the inaccuracy in the estimation of β and therefore in the required
N. Another solution is to systematically choose the sample size larger than what
is prescribed by the computation of β.
17

Figure 8: Evolution of the probability of type-II error as a function of the sample
size N and the eﬀect size ϵ, when (s1, s2) = (1 −error, 1 −error) and α = 0.05. Left:
error = 0, this is the ideal case. Right: error = 0.40, a large error that can be made
when evaluating s over n = 5 samples. The compared distributions are normal, one is
centered on 3, the other on 3 + ϵ.
Message 4:
• One should not blindly believe in statistical tests results. These
tests are based on assumptions that are not always reasonable.
• α must be empirically estimated, as the statistical tests might un-
derestimate it, because of wrong assumptions about the underlying
distributions or because of the small sample size.
• The bootstrap test evaluation of type-I error is strongly dependent
on the sample size. A bootstrap test should not be used with less
than 20 samples.
• The inaccuracies in the estimation of the standard deviations of the
algorithms (s1, s2), due to small sample sizes n in the preliminary
study, lead to under-estimate the sample size N required to meet
requirements in type-II errors.
18

6
Conclusion
In this paper, we outlined the statistical problems that arise when comparing
the performance of two RL algorithms. We deﬁned type-I, type-II errors and
proposed appropriate statistical tests to test for performance diﬀerence. Finally
and most importantly, we detailed how to pick the right number of random seeds
(the sample size) so as to reach the requirements in both error types.
The most important part is what came after. We challenged the hypotheses
made by the Welch’s t-test and the bootstrap test and found several problems.
First, we showed signiﬁcant diﬀerence between empirical estimations of the false
positive rate in our experiment and the theoretical values supposedly enforced
by both tests. As a result, the bootstrap test should not be used with less
than N = 20 samples and tighter signiﬁcance level should be used to enforce a
reasonable false positive rate (< 0.05). Second, we show that the estimation of
the sample size N required to meet requirements in type-II error were strongly
dependent on the accuracy of (s1, s2). To compensate the under-estimation
of N, N should be chosen systematically larger than what the power analysis
prescribes.
Final recommendations
• Use the Welch’s t-test over the bootstrap conﬁdence interval test.
• Set the signiﬁcance level of a test to lower values (α < 0.05) so as
to make sure the probability of type-I error (empirical α) keeps
below 0.05.
• Correct for multiple comparisons in order to avoid the linear growth
of false positive with the number of experiments.
• Use at least n = 20 samples in the pilot study to compute robust
estimates of the standard deviations of both algorithms.
• Use larger sample size N than the one prescribed by the power
analysis. This helps compensating for potential inaccuracies in
the estimations of the standard deviations of the algorithms and
reduces the probability of type-II errors.
Acknowledgement
This research is ﬁnancially supported by the French Minist`ere des Arm´ees -
Direction G´en´erale de l’Armement.
19

References
Brockman, G., Cheung, V., Pettersson, L., Schneider, J., Schulman, J., Tang, J.,
Zaremba, W., 2016. Openai gym. arXiv preprint arXiv:1606.01540.
Cabin, R. J., Mitchell, R. J., 2000. To bonferroni or not to bonferroni: when and
how are the questions. Bulletin of the Ecological Society of America 81 (3),
246–248.
Dhariwal, P., Hesse, C., Klimov, O., Nichol, A., Plappert, M., Radford, A.,
Schulman, J., Sidor, S., Wu, Y., 2017. Openai baselines. https://github.
com/openai/baselines.
Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., Meger, D., 2017.
Deep reinforcement learning that matters. arXiv preprint arXiv:1709.06560.
Islam, R., Henderson, P., Gomrokchi, M., Precup, D., 2017. Reproducibility
of benchmarked deep reinforcement learning tasks for continuous control.
In: Proceedings of the ICML 2017 workshop on Reproducibility in Machine
Learning (RML).
Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver,
D., Wierstra, D., 2015. Continuous control with deep reinforcement learning.
arXiv preprint arXiv:1509.02971.
Mania, H., Guy, A., Recht, B., 2018. Simple random search provides a competitive
approach to reinforcement learning. arXiv preprint arXiv:1803.07055.
Plappert, M., Houthooft, R., Dhariwal, P., Sidor, S., Chen, R. Y., Chen, X.,
Asfour, T., Abbeel, P., Andrychowicz, M., 2017. Parameter space noise for
exploration. arXiv preprint arXiv:1706.01905.
Rice, W. R., 1989. Analyzing tables of statistical tests. Evolution 43 (1), 223–225.
Schulman, J., Levine, S., Moritz, P., Jordan, M. I., Abbeel, P., 2015. Trust region
policy optimization. CoRR, abs/1502.05477.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O., 2017. Proximal
policy optimization algorithms. arXiv preprint arXiv:1707.06347.
Welch, B. L., 1947. The generalization ofstudent’s’ problem when several diﬀerent
population variances are involved. Biometrika 34 (1/2), 28–35.
Wu, Y., Mansimov, E., Liao, S., Grosse, R., Ba, J., 2017. Scalable trust-region
method for deep reinforcement learning using kronecker-factored approxima-
tion. arXiv preprint arXiv:1708.05144.
20
