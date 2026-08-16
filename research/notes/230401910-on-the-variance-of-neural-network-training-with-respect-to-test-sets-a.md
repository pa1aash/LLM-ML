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

---

## Full text (recovered via direct extraction)

Published as a conference paper at ICLR 2024
ON THE VARIANCE OF NEURAL NETWORK TRAINING
WITH RESPECT TO TEST SETS AND DISTRIBUTIONS
Keller Jordan∗
kjordan4077@gmail.com
ABSTRACT
Typical neural network trainings have substantial variance in test-set performance
between repeated runs, impeding hyperparameter comparison and training repro-
ducibility. In this work we present the following results towards understanding
this variation. (1) Despite having significant variance on their test-sets, we demon-
strate that standard CIFAR-10 and ImageNet trainings have little variance in per-
formance on the underlying test-distributions from which their test-sets are sam-
pled. (2) We show that these trainings make approximately independent errors
on their test-sets. That is, the event that a trained network makes an error on one
particular example does not affect its chances of making errors on other examples,
relative to their average rates over repeated runs of training with the same hyper-
parameters. (3) We prove that the variance of neural network trainings on their
test-sets is a downstream consequence of the class-calibration property discov-
ered by Jiang et al. (2021). Our analysis yields a simple formula which accurately
predicts variance for the binary classification case. (4) We conduct preliminary
studies of data augmentation, learning rate, finetuning instability and distribution-
shift through the lens of variance between runs.
1
INTRODUCTION
Modern neural networks (Krizhevsky et al., 2012; He et al., 2016; Vaswani et al., 2017) are trained
using stochastic gradient-based algorithms, involving randomized weight initialization, data order-
ing, and data augmentations. Because of this stochasticity, each independent run of training produces
a different network with better or worse performance than average.
This variance between such independent runs is often substantial. Picard (2021) shows that for stan-
dard CIFAR-10 (Krizhevsky et al., 2009) training configurations, there exist random seeds which
differ by 1.3% in terms of test-set accuracy. In comparison, the gap between the top two methods
competing for state-of-the-art on CIFAR-10 has been less than 1% throughout the majority of the
benchmark’s lifetime1. Prior works therefore view this variance as an obstacle which impedes com-
parisons between training configurations (Bouthillier et al., 2021; Picard, 2021) and reproducibil-
ity (Bhojanapalli et al., 2021; Zhuang et al., 2022). To mitigate stochasticity, Zhuang et al. (2022)
study deterministic tooling, Bhojanapalli et al. (2021) develop regularization methods, and many
recent works (Wightman et al., 2021; Liu et al., 2022) report the average of validation metrics across
multiple runs when comparing training configurations.
In this work we contribute new results towards understanding the variance between runs of neural
network trainings. We use an empirical approach involving hundreds of thousands of trained models
in order to answer the following questions.
1. Repeatedly running a standard training yields a series of models with often substantial vari-
ance in test-set accuracy. Do such models have genuine differences in underlying quality?
Or is this variance just a form of finite-sample noise due to the limited size of the test-set?
2. Does the empirical distribution of test-set accuracy across repeated runs of training possess
any definable structure?
3. Is there any way to estimate the variance of a given training configuration a priori, i.e.,
without the need to empirically measure it across many repeated runs?
∗Experiments performed while at Hive AI
1https://paperswithcode.com/sota/image-classification-on-cifar-10
1
arXiv:2304.01910v4  [cs.LG]  10 Jun 2024

Published as a conference paper at ICLR 2024
Both the first and last of these questions have immediate practical consequences. For the first ques-
tion, if the answer is that every run of training yields a model with the same underlying performance
on held-out batches of test data, then practitioners can confidently execute just a single run per
configuration. Otherwise, a superior strategy would be to take the best model from multiple trials.
For the third question, if a method for estimating variance a priori does exist, then this provides a
useful tool by which practitioners can confidently estimate the statistical significance of hyperpa-
rameter comparisons, without the need for many runs of training. To answer all three questions, we
contribute the following results.
• Random seeds which are “lucky” with respect to one set of test data perform no better than
average with respect to a second set. (Section 3.1)
• Over repeated runs of training, the distribution of errors made by trained networks can be
approximately explained via the framework of independent errors. (Section 3.2)
• Although standard trainings have substantial variance on their test-sets, they have little
variance in performance on their underlying test-distributions. (Section 3.3)
• Variable test-set performance is a downstream effect of the class-calibration property (Jiang
et al., 2021) of neural network trainings. For the binary classification case, this property
implies a simple formula which accurately predicts variance a priori. (Section 3.4)
Our experiments show that these results hold true for standard training configurations across both
CIFAR-10 and ImageNet (Deng et al., 2009). As a limitation, we show that they do not hold true for
two exceptional scenarios: trainings with pathological instability (Section 4.1), and trainings where
there is a shift between the training and test distributions (Section 4.4, Section C). Both of these
cases have a large distribution-wise variance, differing from our results in the standard cases.
To complete our study of variance, we additionally conduct preliminary investigations regarding the
effect of learning rate (Section 4.3) and data augmentation (Section 4.2). We find that when increas-
ing the learning rate, accuracy begins to decline at the same point at which significant distribution-
wise variance appears. And we find that data augmentation reduces variance, although the mecha-
nism by which this happens is not yet clear.
1.1
RELATED WORK
A number of prior works investigate which sources of stochasticity are most responsible for the
variation between runs of training. Fort et al. (2019) observe that when using a below-optimal
learning rate, randomized data ordering has a smaller impact than model initialization on the churn
of predictions between runs. Bhojanapalli et al. (2021) similarly find that fixing the data ordering has
no effect, while fixing the model initialization reduces churn. On the other hand, Bouthillier et al.
(2021) report that data ordering has a larger impact than model initialization. And finally, Summers
& Dinneen (2021) find instead that most variation can be attributed to the high sensitivity of the
training process to initial conditions, by showing that a single bit difference in starting parameters
leads to the full quantity of prediction churn between runs. We replicate the results of Summers &
Dinneen (2021) in Section D, although we find that the result depends upon the training duration.
Dodge et al. (2020) study variation between runs of BERTLARGE finetuning, and achieve substantial
gains in validation performance via the strategy of re-running finetuning many times and taking the
best-performing result. We demonstrate (Section 4.1) that for the case of BERTBASE, the low amount
of genuine distribution-wise variance between runs indicates that any performance gains yielded by
this strategy would only amount to overfitting the validation set. On the other hand, for BERTLARGE
we demonstrate that there is genuinely significant distribution-wise variance, supporting the use of
multiple runs of training as suggested. Mosbach et al. (2020) also study the finetuning instability
of BERTLARGE, and suggest that it can be mitigated by warming up the learning rate, training for
longer with a smaller learning rate, and using bias correction for Adam (Kingma & Ba, 2014).
Earlier works on neural network ensembles have found that they are more well-calibrated than in-
dividual networks (Lakshminarayanan et al., 2017; Nixon et al., 2020). And Mukhoti et al. (2021)
observed that the usefulness of an ensemble’s uncertainty scores depends upon variance between the
individual networks. Our theoretical results in Section 3.4 draw upon the related class-wise calibra-
tion property of neural network trainings. This property was discovered by Jiang et al. (2021), who
used it to obtain a theoretical proof of the empirical phenomenon that the disagreement rate between
2

Published as a conference paper at ICLR 2024
Figure 1: Accuracy distributions. The test-set accuracy distributions across our four training durations,
displayed as unsmoothed histograms for 60,000 repeated runs of training each. The differences between the
“luckiest” and most unlucky run (max minus min accuracy) are 13.2%, 6.6%, 1.7%, and 1.4% for the 0, 4, 16,
and 64-epoch training durations, respectively. The standard deviations are 1.87%, 0.56%, 0.19%, and 0.15%.
two independently trained networks is approximately equal to their error rates (Nakkiran & Bansal,
2020; Jiang et al., 2021).
Several prior works (Baldock et al., 2021; Ilyas et al., 2022; Lin et al., 2022) study the effect of
randomly varying the data used to train a neural network, across a large number of training runs.
Our study differs from these works in that we consider the simpler scenario of running a single
training algorithm many times without varying anything except the random seed.
Broadly, our work is related to research aiming to understand the relationship between pairs of neural
networks produced by repeated runs of training. This topic is of both theoretical and practical inter-
est, and has been studied from a variety of angles, including the similarity of internal representations
(Li et al., 2015; Kornblith et al., 2019), degree of correlation between predictions (Fort et al., 2019;
Jiang et al., 2021), similarity of decision boundaries (Somepalli et al., 2022), path-connectivity in
weight-space (Draxler et al., 2018; Garipov et al., 2018), and linear mode connectivity (Frankle
et al., 2020; Tatro et al., 2020; Entezari et al., 2021).
2
SETUP
Notation. We study supervised classification problems in which test-set examples are sampled in-
dependently from a distribution D over X × Y, where Y = {1, . . . , k} is the set of classes and
X is the input space. We make no assumptions on the training distribution. By a training algo-
rithm or configuration, we mean a training pipeline which includes everything necessary for training
besides the random seed. That is, we assume training algorithms already include the choice of op-
timization algorithm, dataset, network architecture, and hyperparameters, so that only the random
seed remains to determine the outcome of training. Following Jiang et al. (2021), for a stochastic
training algorithm A we write h ∼HA to denote sampling a hypothesis from the distribution in-
duced by the algorithm, i.e., by running the algorithm and collecting the hypothesis h : X →Y
computed by the trained network. We write errx,y(h) = 1{h(x)̸ = y} to denote the event that h
makes an error on the example (x, y), so that Eh∼HA[errx,y(h)] is the proportion of runs of training
which make an error on (x, y). We additionally write err(h) = E(x,y)∼D[errx,y(h)] to denote the
distribution-wise error rate, so that the distribution-wise variance is Varh∼HA(err(h)). For a test-set
S = ((x1, y1), . . . , (xn, yn)) we define the test-set error as usual as errS(h) = 1
n
Pn
i=1 errxi,yi(h).
Finally, we write err(A) = Eh∼HA[err(h)] to denote the mean distribution-wise error of hypotheses
produced by the training algorithm. We often refer interchangeably to the variance of the accuracy
and of the error rate, as the two quantities always have the same variance.
Main experimental setup. For our main experiments (Section 3) we train ResNets on CIFAR-10.
We study four different training durations: 0, 4, 16, and 64 epochs. The 0-epoch case corresponds to
evaluating the network at initialization; on average this has random chance-level accuracy, but some
random initializations reach as high as 14% and as low as 6% accuracy. A complete description of
each training configuration is provided in Section A. We execute each configuration 60,000 times
and collect the resulting test-set predictions, yielding the accuracy distributions shown in Figure 1.
These 240,000 collected sets of test-set predictions form our main object of study.
3

Published as a conference paper at ICLR 2024
Figure 2: Error rates on disjoint splits of test data become decorrelated when training to convergence.
We evaluate a large number of independently trained networks on two splits of the CIFAR-10 test-set. When
under-training there is substantial correlation, so that a “lucky” run which over-performs on the first split is also
likely to achieve higher-than-average accuracy on the second. As we increase the training duration, the two
error rates decorrelate from each other.
3
THE STATISTICAL STRUCTURE OF NEURAL NETWORK ERRORS
3.1
DO LUCKY RANDOM SEEDS GENERALIZE?
In Figure 1 we observed that our standard CIFAR-10 training configuration has significant variation
between runs. Even when training for a long duration, we found pairs of random seeds which
produce trained networks whose test-set accuracy differs by more than 1%. In this section, we argue
that this variance is merely a form of finite-sample noise caused by the limited size of the test-set,
and does not imply almost any genuine fluctuation in the quality of the trained network.
Suppose we view the random seed as a training hyperparameter. Then we have observed that it can
be effectively “tuned” to obtain improved performance on the test-set – on average, our training
configuration attains an accuracy of 94.42%, but we can find random seeds which reach above 95%,
which is more than a 10% reduction in the number of errors. However, this improvement on the
test-set alone is not enough to conclude that the random seed genuinely affects model quality. What
remains to be seen is whether this performance improvement can generalize to unseen data, or if we
are just effectively over-fitting the random seed to the observed test-set.
To find out, we perform the following experiment. First, we split the CIFAR-10 test-set into two
halves of 5,000 examples each. CIFAR-10 is already shuffled, so for convenience we simply use
the odd and even-indexed examples as the two halves. We view the first half as the hyperparameter-
validation split and second as the held-out test split. Next, we execute many independent runs of
training, with identical configurations other than the varying random seed. We measure the perfor-
mance of each trained network on both splits of data. If lucky random seeds do generalize, then runs
which perform well on the first split should also perform better than average on the second split.
To additionally determine the effect of training duration, we repeat this experiment for trainings of
0, 4, 16, and 64 epochs, using 60,000 independently trained networks for each duration. We view
the results in Figure 2. For short trainings, the two splits are indeed highly correlated, such that
runs which perform well on the first split also tend to do well on the second. But when training for
longer, this correlation nearly disappears. For example, when training for 64 epochs, our highest-
performing network on the first split does not even perform better than average on the second split.
And on average, the top 1/4 of runs with respect to the first split perform only 0.02% better than
average on the second split.
This result has the following practical implication. Suppose we want to obtain a good CIFAR-10
model. Noticing significant variation between runs (Figure 1), we might be tempted to re-run train-
ing many times, in order to obtain networks with better test-set performance. However, according
to Figure 2, this would be useless, because improvements on the test-set due to re-training will have
near-zero correlation with improvements on unseen data. These networks would be “better” only in
the sense of attaining higher test-set accuracy, but not in the sense of being more accurate on unseen
data from the same distribution.
4

Published as a conference paper at ICLR 2024
Figure 3: Independent errors explain variance when training to convergence. (Left:) We compare the em-
pirical distribution of test-set accuracy with that generated by simulating an equal number of samples assuming
the hypothesis of independent errors. The hypothesis is wrong for short trainings, but becomes a close fit as
training progresses. (Right:) The hypothesis accurately predicts variance when training to convergence.
3.2
ERRORS ARE APPROXIMATELY INDEPENDENT
In the previous section we showed that when training to convergence, disjoint splits of test data
become nearly decorrelated, in the sense that networks which randomly perform well on one split
do not perform better than average on the other. We now test the hypothesis that this phenomenon
Figure 4:
A pair with independent errors.
(Left) is image 776 of the CIFAR-10 test-set. Out
of 60,000 independent runs of 64-epoch training,
21,736 networks (36.2%) correctly predict this ex-
ample. (Right) is image 796, which is correctly
predicted by 36,392 networks (60.7%). The num-
ber of networks which predict both correctly at
the same time is 13,103 (21.83%), which has a
statistically insignificant difference to the quantity
0.362 · 0.607 = 21.97%, which is the predicted
value if their errors are independent.
also extends to individual examples, such that the
event that the network makes an error on a given test
example becomes independent of its other errors as
we train to convergence. Figure 4 shows an example.
Definition 1. The training algorithm A makes
independent errors on a test-set S if for every pair
of examples (xi, yi) and (xj, yj) in S,
Cov
h∼HA(errxi,yi(h), errxj,yj(h)) = 0
(1)
For classification problems, each example’s error
event errxi,yi(h) = 1{h(xi)̸ = yi} is a Bernoulli
variable over the training stochasticity. If the train-
ing algorithm makes independent errors, then these
error variables form a series of independent biased
coin flips, with the test-set error rate distributed as
their average.
To find out whether this hypothet-
ical distribution matches empirical reality, we first
collect the example-wise mean error rates εi :=
Eh[errxi,yi(h)] for i ∈{1, . . . , n}, and then sam-
ple from the distribution by taking the average of n coin flips which are biased by those rates. The
exact variance of the resulting random variable is given by the formula
1
n2
Pn
i=1 εi(1 −εi).
In Figure 3 we compare this simulation of the hypothesized distribution to the empirical distribution
generated by repeated runs of training. We find that for short trainings of 0-16 epochs, the hypothesis
is wrong, as the empirical distribution has extra variance which the hypothesis does not account for.
But for the full 64-epoch training, the hypothesis becomes a close fit to reality. It predicts a standard
deviation of 0.145% and the empirical value is similar at 0.149%.
As further confirmation of the hypothesis, we find that there exist only five pairs of examples in the
CIFAR-10 test-set which deviate from having independent errors by more than 2%. We show all
five pairs in Figure 13. We additionally show in Figure 14 that the hypothesis distribution compares
favorably to that generated by the binomial assumption. In the next section we explore how the
small difference between the independent errors hypothesis and reality can be used to estimate the
variance in accuracy with respect to the underlying test-distribution.
5

Published as a conference paper at ICLR 2024
3.3
DISTRIBUTION-WISE VARIANCE IS SMALL
In Section 3.1 we showed that accuracy is decorrelated between disjoint splits of test-data, and
argued that this implies there is little genuine variation in model quality between runs of training. In
this section we formalize our notion of model quality as accuracy on the underlying test-distribution,
and show that the variance of this quantity between runs of training turns out to be very small.
Neural networks are typically evaluated by their performance on a test-set. However, what ultimately
determines the expected performance of a neural network on new batches of unseen data is not the
test-set error rate, but rather the error rate on the underlying distribution from which the test-set was
sampled. We call this the distribution-wise error rate err(h) = E(x,y)∼D[1{h(x)̸ = y}].
Figure 5:
Test-set variance overestimates
distribution-wise variance.
We use Equa-
tion 3 to estimate the distribution-wise variance
Varh∼HA(err(h)). It becomes 20× smaller than
the test-set variance when training to convergence.
Estimating the mean of distribution-wise error
across training stochasticity is relatively easy, be-
cause the mean test-set accuracy is an unbiased es-
timator as ES∼Dn[Eh[errS(h)]] = Eh[err(h)]. Esti-
mating its variance Varh(err(h)) is more challeng-
ing, because the variance in test-set accuracy is po-
tentially an overestimate (proof in Section B.1).
Theorem 1. In expectation, the variance in test-set
accuracy overestimates the variance in true error.
E
S∼Dn

Var
h∼HA(errS(h))

≥Var
h∼HA(err(h))
(2)
We note that this ≥becomes a strict > given very
mild additional assumptions. To obtain an unbiased
estimate of Varh(err(h)), we recall the results of
Section 3.2. When training to convergence, test-set
accuracy follows a distribution which can be approx-
imately recovered by assuming that errors are inde-
pendent (Definition 1, Figure 3). The distribution-wise variance in this case should be essentially
zero, assuming the distribution is not concentrated in a small number of discrete examples. On
the other hand, for shorter trainings we observed substantial test-set variance in excess of that pre-
dicted by Definition 1, i.e., Varh∼HA(errS(h)) >
1
n2
Pn
i=1 Varh(errxi,yi(h)). For example, the
hypothesis predicts that our 4-epoch configuration should have a standard deviation of 0.22%, but
the empirical value was much larger at 0.56%. This suggests that these shorter trainings may have
significant distribution-wise variance between runs.
We provide the following theorem which makes this intuitive connection rigorous (proof in Sec-
tion B.2). It turns out that a slight rescaling of the excess in empirical variance over that predicted
by Definition 1 forms an unbiased estimator for the variance of the distribution-wise error rate.
Theorem 2. The following quantity is an unbiased estimator for Varh∼HA(err(h)).
ˆσ2
S =
n
n −1
 
Var
h∼HA(errS(h)) −1
n2
n
X
i=1
Var
h∼HA(errxi,yi(h))
!
(3)
In Figure 5 we compare this quantity to the test-set variance Varh∼HA(errS(h)) across a range of
training durations. When training for 4 epochs, the standard deviation of distribution-wise error
is estimated at
p
ˆσ2
S = 0.52%, indicating that there are indeed significant differences in quality
between neural networks trained for this duration. In contrast, when training for the full duration of
64 epochs, we estimate that the distribution-wise error rate has a standard deviation between runs
of only 0.033%. In Section C we obtain a similarly small estimate for ImageNet trainings. This is
248× less variance than the 4-epoch configuration has, and 20× less variance than the 64-epoch
configuration naively has on the test-set. This result indicates that when training to convergence,
there is very little variation in model quality (i.e., expected performance with respect to new batches
of data from the test-distribution) between runs of training.
Having confirmed that the distribution-wise variance is small, it still remains to explain why there is
high variance on the finite test-set in the first place. We investigate this question in the next section.
6

Published as a conference paper at ICLR 2024
3.4
VARIATION CAN BE PREDICTED FROM CLASS-WISE CALIBRATION
In this section we prove that variance in test-set accuracy between runs of training is an inevitable
consequence of the fact that ensembles of trained networks approximately satisfy the class-wise
calibration property of Jiang et al. (2021). Our analysis yields a simple formula which accurately
estimates variance for binary classification problems.
Classical machine learning algorithms based on convex loss functions can have neither test-set-wise
nor test-distribution-wise variance, because training eventually converges to the single global opti-
mum which always makes the same set of predictions. For example, in Figure 7 (left) we find that
repeatedly training a regularized linear model on CIFAR-10 leads to a standard deviation of below
0.01%. On the other hand, neural networks can have many optima (Auer et al., 1995; Choromanska
et al., 2015), so that every run of training can potentially lead to a different solution with different
behavior on the test-distribution. Despite this, in the previous section we showed that neural net-
work trainings in fact have little variance in their overall distribution-wise performance. What then
explains the property of neural network trainings that they have high variance on their test-sets?
We argue that the following property of neural network trainings, which Jiang et al. (2021) demon-
strate approximately holds in practice, is connected to their variable performance on test-sets.
Definition 2. The stochastic training algorithm A satisfies class-wise calibration (Jiang et al.,
2021) if for every class c ∈Y and confidence level q ∈[0, 1],
P(x,y)∼D
 y = c | Ph∼HA(h(x) = c) = q

= q.
(4)
As an explanatory example, if we let S′ ⊂S be the subset of test images which are classified by
30-40% of independently trained neural networks as “cat,” then 30-40% of S′ really will be cats.
We prove (Section B.3) the following theorem connecting class-wise calibration to variance.
Theorem 3. Let A be a stochastic training algorithm for binary classification. If it is class-wise
calibrated, then its expected variance on a test-set of size n is equal to
E
S∼Dn

Var
h∼HA(errS(h))

= err(A)
2n
+ (1−1
n) · Var
h∼HA(err(h))
(5)
Figure 6: Predicting variance. Across hundreds
of tasks, Equation 6 accurately predicts the stan-
dard deviation of test-set error. In contrast, the
binomial assumption is inaccurate.
We showed in Section 3.3 that Varh(err(h)) is small
in practice. Therefore, this theorem practically re-
duces to the following simple formula:
ES[Varh(errS(h)] ≈err(A)/2n
(6)
In Figure 6 we use this formula to predict test-
set variance across 511 different binary classifica-
tion tasks generated by assigning each CIFAR-10
class to be either positive or negative. We use each
task’s test-set error rate as a cheap approximation to
err(A). The resulting predictions are a close fit with
empirical reality, with R2 = 0.996 across the col-
lection of tasks. For example, compared to the com-
monly used binomial assumption (Dietterich, 1998;
Raschka, 2018), the variances predicted by Equa-
tion 6 are 70× more accurate in terms of their mean
squared distance to the empirical values.
We additionally prove (Section B.4) a lower bound
for general k-way classification.
Theorem 4. Given a training algorithm A for k-
way classification, if it is class-wise calibrated, then
its expected variance on a test-set of size n is at least
E
S∼Dn

Var
h∼HA(errS(h))

≥err(A)
nk
(7)
Together, these theorems show that the variance of neural network trainings on finite test-sets is a
predictable consequence of their class-wise calibration.
7

Published as a conference paper at ICLR 2024
Figure 7: (Far left:) A regularized linear model has very little variance between runs of training. (Center left:)
Removing either data augmentation or 80% of training data reduces the mean accuracy to a similar level, but
the former produces far more variance than the latter. (Right two:) When finetuning BERTBASE on MRPC,
performance on the validation and test sets are not strongly correlated across repeated runs. On the other hand,
BERTLARGE has significant correlated variance, indicating genuine distribution-wise variance.
4
ADDITIONAL EXPERIMENTS
In this section we conduct preliminary investigations regarding the effect of data augmentation,
learning rate, finetuning instability, and distribution-shift on variance. We additionally include a
replication study of Summers & Dinneen (2021) in Section D, which confirms their findings that
variance is caused by extreme sensitivity to initial conditions rather than any particular stochastic
factor like network initialization or data ordering.
4.1
THE EFFECT OF FINETUNING INSTABILITY
In this section we study BERT (Devlin et al., 2018) finetuning, a setting where previous works have
reported significant variance between runs (Devlin et al., 2018; Dodge et al., 2020; Mosbach et al.,
2020). Our contribution is to use the tools developed in Section 3 to clearly differentiate the behavior
of BERTLARGE from BERTBASE.
For our experiment, we finetune pretrained checkpoints of both models 1,000 times each on the
MRPC (Dolan & Brockett, 2005) task. In Figure 7 (right) we show that for BERTBASE, the valida-
tion and test splits of MRPC are close to decorrelated in terms of the finetuned model performance,
similarly to Section 3.1. The top 15% of seeds in terms of validation-set performance achieve only
0.09% higher performance than average on the test-set, whereas for BERTLARGE the correlation is
higher. The test-set error rate of BERTBASE has a standard deviation of 0.80% between runs of fine-
tuning, and BERTLARGE has a stddev of 2.24%. This is already a significant gap of almost 8× more
test-set variance for BERTLARGE; using Equation 3 increases the gap further. In particular, we esti-
mate the distribution-wise standard deviation at 0.21% for BERTBASE, and 2.08% for BERTLARGE,
amounting to 100× more distribution-wise variance for BERTLARGE.
4.2
THE EFFECT OF DATA AUGMENTATION
In this section we investigate the effect of data augmentation on variance. In Figure 7 (center left) we
compare two modifications of our CIFAR-10 training: first, removing a fixed 80% of training data,
and second, removing data augmentation. While both modifications yield a similar mean accuracy
of 87.5%, removing augmentations results in 3.5× more variance between runs. Furthermore, the
large-ensemble accuracy of the networks trained without augmentation is higher, reaching 91.2%,
compared to the reduced-data ensemble, which reaches only 89.8%. We conclude that data augmen-
tation reduces variance, although the mechanism by which this happens is not yet known.
4.3
THE EFFECT OF LEARNING RATE
In this section we investigate the relationship between learning rate and variance. Our experiment
is to execute 1,000 64-epoch CIFAR-10 trainings for each binary-power learning rate between 2−10
and 22. For each setting, we measure the mean and variance of test-set accuracy. We observe that
the learning rate 0.5 yields both the highest mean and the lowest variance. Raising it to 1.0 causes
the standard deviation of test-set accuracy to increase from 0.148% to 0.168%. This may seem
insignificant, but Equation 3 estimates that it implies a significant 5× increase in distribution-wise
8

Published as a conference paper at ICLR 2024
Figure 8: Accuracy is maximized by the largest learning rate without excess variance. Across learning
rates, we compare the observed stddev of test-set accuracy to that predicted by the independent errors frame-
work. The best learning rate is apparently the largest one which does not induce significant excess variance.
variance. We therefore conjecture that, as a general property of neural network trainings, the optimal
learning rate is the largest one which does not induce significant distribution-wise variance.
4.4
THE EFFECT OF DISTRIBUTION SHIFT
In this section we summarize our results on distribution shift, which are fully described in Section C.
Our experimental setup is to train 1,000 ResNet-18s on ImageNet with identical hyperparameters,
and then use Equation 3 to estimate their distribution-wise variances on various test-sets: namely,
the main ImageNet validation set, ImageNet-V2 (Recht et al., 2019), and three distribution-shifted
sets. We find that the main validation set has a distribution-wise standard deviation of 0.034%,
which is quite similar to the CIFAR-10 case. ImageNet-V2, which is intended to be a sample from
the same underlying distribution as ImageNet, has a standard deviation of 0.071%. Each of the
three distribution-shifted sets, on the other hand, have at least six times more variance than that.
For example, ImageNet-Sketch (Wang et al., 2019) has a distribution-wise standard deviation of
0.257%, meaning that on average every 50 runs will contain a pair of networks whose performance
on the ImageNet-Sketch distribution differs by over 1%, assuming a roughly Gaussian accuracy
distribution. Overall, distribution-wise variance is high for precisely those test-distributions which
are significantly shifted relative to the training distribution. Why this happens is unknown.
5
DISCUSSION
A central focus of this paper is the distinction between a model’s observed error rate on a test-set, and
its true error rate on the underlying test-distribution from which that test-set was sampled. The mean
of the former, over repeated runs of training, provides an unbiased estimate of the mean of the latter.
But the variance of the former does not in general provide an unbiased estimate for the variance
of the latter, meaning that we cannot tell how unstable a training really is just from measuring its
variance on a test-set. To recover an unbiased estimate, we derive a new formula (Equation 3). Using
this formula we discover that for standard trainings, the variance between runs of training in terms of
distribution-wise error rate is typically very small, with a standard deviation of only around 0.03%
for both CIFAR-10 and ImageNet trainings.
Our understanding of variance is further simplified by the independent errors framework. It turns out
that over repeated runs of standard CIFAR-10 training, the event that the trained network makes an
error on one particular example has almost no effect on its chances of making other errors. Overall,
our takeaway is that for standard trainings, even though some random seeds lead to substantially
higher or lower performance on the test-set due to independent errors, all seeds have nearly equal
performance on the underlying test-distribution.
However, we found two exceptions to this takeaway. The first is trainings which have pathologi-
cal instability, such as BERTLARGE finetuning where the test-set accuracy can vary by more than
15% (Section 4.1), and distribution-wise variance is also high. The second more interesting ex-
ception is trainings whose test distributions are shifted relative to their training distributions (Sec-
tion 4.4, Section C). Understanding why variance appears alongside distribution shift is an intriguing
task whose solution we look forward to in future work.
9

Published as a conference paper at ICLR 2024
ACKNOWLEDGEMENTS
We are grateful to Behnam Neyshabur for his guidance on a preliminary version of this work. We
thank Ehsan Amid, Luke Johnston, and Ryan Weber each for their insightful comments on the draft.
REFERENCES
Peter Auer, Mark Herbster, and Manfred K Warmuth. Exponentially many local minima for single
neurons. Advances in neural information processing systems, 8, 1995.
Robert Baldock, Hartmut Maennel, and Behnam Neyshabur. Deep learning through the lens of
example difficulty. Advances in Neural Information Processing Systems, 34:10876–10889, 2021.
Andrei Barbu, David Mayo, Julian Alverio, William Luo, Christopher Wang, Dan Gutfreund, Josh
Tenenbaum, and Boris Katz. Objectnet: A large-scale bias-controlled dataset for pushing the
limits of object recognition models.
Advances in neural information processing systems, 32,
2019.
Srinadh Bhojanapalli, Kimberly Wilber, Andreas Veit, Ankit Singh Rawat, Seungyeon Kim, Aditya
Menon, and Sanjiv Kumar. On the reproducibility of neural network predictions. arXiv preprint
arXiv:2102.03349, 2021.
Xavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan Nichyporuk, Justin
Szeto, Nazanin Mohammadi Sepahvand, Edward Raff, Kanika Madan, Vikram Voleti, et al. Ac-
counting for variance in machine learning benchmarks. Proceedings of Machine Learning and
Systems, 3:747–769, 2021.
Anna Choromanska, Mikael Henaff, Michael Mathieu, G´erard Ben Arous, and Yann LeCun. The
loss surfaces of multilayer networks. In Artificial intelligence and statistics, pp. 192–204. PMLR,
2015.
Benjamin Cohen-Wang, Joshua Vendrow, and Aleksander Madry. Ask your distribution shift if
pre-training is right for you. arXiv preprint arXiv:2403.00194, 2024.
Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hi-
erarchical image database. In 2009 IEEE conference on computer vision and pattern recognition,
pp. 248–255. IEEE, 2009.
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Llm. int8 (): 8-bit matrix
multiplication for transformers at scale. arXiv preprint arXiv:2208.07339, 2022.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.
Terrance DeVries and Graham W Taylor. Improved regularization of convolutional neural networks
with cutout. arXiv preprint arXiv:1708.04552, 2017.
Thomas G Dietterich. Approximate statistical tests for comparing supervised classification learning
algorithms. Neural computation, 10(7):1895–1923, 1998.
Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi, and Noah Smith.
Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.
arXiv preprint arXiv:2002.06305, 2020.
Bill Dolan and Chris Brockett. Automatically constructing a corpus of sentential paraphrases. In
Third International Workshop on Paraphrasing (IWP2005), 2005.
Felix Draxler, Kambis Veschgini, Manfred Salmhofer, and Fred Hamprecht. Essentially no barriers
in neural network energy landscape. In International conference on machine learning, pp. 1309–
1318. PMLR, 2018.
Rahim Entezari, Hanie Sedghi, Olga Saukh, and Behnam Neyshabur.
The role of permutation
invariance in linear mode connectivity of neural networks. arXiv preprint arXiv:2110.06296,
2021.
10

Published as a conference paper at ICLR 2024
Stanislav Fort, Huiyi Hu, and Balaji Lakshminarayanan. Deep ensembles: A loss landscape per-
spective. arXiv preprint arXiv:1912.02757, 2019.
Jonathan Frankle, Gintare Karolina Dziugaite, Daniel Roy, and Michael Carbin. Linear mode con-
nectivity and the lottery ticket hypothesis. In International Conference on Machine Learning, pp.
3259–3269. PMLR, 2020.
Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin, Dmitry P Vetrov, and Andrew G Wilson. Loss
surfaces, mode connectivity, and fast ensembling of dnns. Advances in neural information pro-
cessing systems, 31, 2018.
G. H. Hardy, J. E. Littlewood, and G. P´olya. Inequalities. Cambridge Mathematical Library. Cam-
bridge University Press, Cambridge, 1934.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recog-
nition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp.
770–778, 2016.
Dan Hendrycks, Steven Basart, Norman Mu, Saurav Kadavath, Frank Wang, Evan Dorundo, Rahul
Desai, Tyler Zhu, Samyak Parajuli, Mike Guo, et al. The many faces of robustness: A critical
analysis of out-of-distribution generalization.
In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 8340–8349, 2021.
Andrew Ilyas, Sung Min Park, Logan Engstrom, Guillaume Leclerc, and Aleksander Madry. Data-
models: Predicting predictions from training data. arXiv preprint arXiv:2202.00622, 2022.
Yiding Jiang, Vaishnavh Nagarajan, Christina Baek, and J Zico Kolter. Assessing generalization of
sgd via disagreement. arXiv preprint arXiv:2106.13799, 2021.
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint
arXiv:1412.6980, 2014.
Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. Similarity of neural
network representations revisited. In International Conference on Machine Learning, pp. 3519–
3529. PMLR, 2019.
Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. Cifar-100 and cifar-10 (canadian institute for
advanced research), 2009. URL http://www.cs.toronto.edu/˜kriz/cifar.html.
MIT License.
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convo-
lutional neural networks. Communications of the ACM, 60(6):84–90, 2012.
Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable predictive
uncertainty estimation using deep ensembles. Advances in neural information processing systems,
30, 2017.
Guillaume Leclerc, Andrew Ilyas, Logan Engstrom, Sung Min Park, Hadi Salman, and Aleksander
Madry. ffcv. https://github.com/libffcv/ffcv/, 2022.
Yixuan Li, Jason Yosinski, Jeff Clune, Hod Lipson, and John Hopcroft. Convergent learning: Do
different neural networks learn the same representations? arXiv preprint arXiv:1511.07543, 2015.
Jinkun Lin, Anqi Zhang, Mathias L´ecuyer, Jinyang Li, Aurojit Panda, and Siddhartha Sen. Mea-
suring the effect of training data on deep learning predictions via randomized experiments. In
International Conference on Machine Learning, pp. 13468–13504. PMLR, 2022.
Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feichtenhofer, Trevor Darrell, and Saining Xie.
A convnet for the 2020s. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pp. 11976–11986, 2022.
Marius Mosbach, Maksym Andriushchenko, and Dietrich Klakow. On the stability of fine-tuning
bert: Misconceptions, explanations, and strong baselines. arXiv preprint arXiv:2006.04884, 2020.
11

Published as a conference paper at ICLR 2024
Jishnu Mukhoti, Andreas Kirsch, Joost van Amersfoort, Philip HS Torr, and Yarin Gal. Deep deter-
ministic uncertainty: A simple baseline. arXiv preprint arXiv:2102.11582, 2021.
Preetum Nakkiran and Yamini Bansal. Distributional generalization: A new kind of generalization.
arXiv preprint arXiv:2009.08092, 2020.
Jeremy Nixon, Balaji Lakshminarayanan, and Dustin Tran. Why are bootstrapped deep ensembles
not better? In ”I Can’t Believe It’s Not Better!”NeurIPS 2020 workshop, 2020.
David Page. How to train your resnet 4: Architecture, 2019.
URL https://myrtle.ai/
learn/how-to-train-your-resnet-4-architecture/.
David Picard. Torch. manual seed (3407) is all you need: On the influence of random seeds in deep
learning architectures for computer vision. arXiv preprint arXiv:2109.08203, 2021.
Sebastian Raschka. Model evaluation, model selection, and algorithm selection in machine learning.
arXiv preprint arXiv:1811.12808, 2018.
Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, and Vaishaal Shankar. Do imagenet classifiers
generalize to imagenet? In International conference on machine learning, pp. 5389–5400. PMLR,
2019.
Gowthami Somepalli, Liam Fowl, Arpit Bansal, Ping Yeh-Chiang, Yehuda Dar, Richard Baraniuk,
Micah Goldblum, and Tom Goldstein. Can neural nets learn the same model twice? investigating
reproducibility and double descent from the decision boundary perspective. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 13699–13708, 2022.
Cecilia Summers and Michael J Dinneen. Nondeterminism and instability in neural network opti-
mization. In International Conference on Machine Learning, pp. 9913–9922. PMLR, 2021.
Norman Tatro, Pin-Yu Chen, Payel Das, Igor Melnyk, Prasanna Sattigeri, and Rongjie Lai. Op-
timizing mode connectivity via neuron alignment. Advances in Neural Information Processing
Systems, 33:15300–15311, 2020.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural informa-
tion processing systems, 30, 2017.
Haohan Wang, Songwei Ge, Zachary Lipton, and Eric P Xing. Learning robust global representa-
tions by penalizing local predictive power. Advances in Neural Information Processing Systems,
32, 2019.
Ross Wightman, Hugo Touvron, and Herv´e J´egou.
Resnet strikes back: An improved training
procedure in timm. arXiv preprint arXiv:2110.00476, 2021.
Donglin Zhuang, Xingyao Zhang, Shuaiwen Song, and Sara Hooker. Randomness in neural network
training: Characterizing the impact of tooling. Proceedings of Machine Learning and Systems, 4:
316–336, 2022.
12

Published as a conference paper at ICLR 2024
A
TRAINING DETAILS
A.1
CIFAR-10
For our main experiments (Section 3) we train thousands of ResNet-9s on CIFAR-10. Our network
architecture is the same as was used by Ilyas et al. (2022), namely, a 9-layer ResNet descended from
Page (2019). Our 0-epoch configuration corresponds to a randomly initialized network. Our 4, 16,
and 64-epoch configurations all train using SGD with learning rate 0.5, momentum 0.9, and weight
decay 5e-4, with the learning rate linearly ramped down to zero by the end of training. We train
using random flipping, 2-pixel translation, and 12-pixel Cutout (DeVries & Taylor, 2017) data aug-
mentations. We use batch size 500 and load data using the FFCV (Leclerc et al., 2022) library. Our
training script is made available at https://github.com/KellerJordan/ffcv-cifar/
blob/master/train.py. The 64-epoch configuration attains an average accuracy of 94.42%
without the use of test-time augmentation. For each of the four durations we execute training 60,000
times, generating 240,000 sets of test-set predictions, which form our object of study for Section 3.
A.2
IMAGENET
For our ImageNet experiments (Section 4.4, Section C) we train 1,000 ResNet-18s on ImageNet.
We use standard random flip and random resized crop data augmentations. We train at resolution
192 for 100 epochs with batch size 1024, using SGD-momentum with learning rate 0.5, momentum
0.9, and weight decay 5e-5. We linearly ramp the learning rate up from 5e-5 to 0.5 by epoch 2, and
then down to zero by the end of training. We evaluate at resolution 256 with crop ratio 0.875. We use
the FFCV dataloader here as well, and base our training on https://github.com/libffcv/
ffcv-imagenet.
A.3
BERT FINETUNING
For our BERT finetuning experiments (Section 4.1) we finetune BERTBASE and BERTLARGE on
the MRPC (Dolan & Brockett, 2005) binary classification dataset. MRPC contains 3,668 training
examples, 407 validation examples, and 1,725 test examples. We train for 3 epochs at batch size 16,
using Adam (Kingma & Ba, 2014) with default hyperparameters other than the learning rate, which
is linearly ramped from a maximum of 2e-5 down to zero by the end of training.
13

Published as a conference paper at ICLR 2024
B
PROOFS
Lemma 1. The variance of error is equal to the expected covariance between pairs of examples.
Var
h∼HA(err(h)) =
E
(x1,y1),(x2,y2)∼D2

Cov
h∼HA
 errx1,y1(h), errx2,y2(h)

Proof.
Var
h∼HA(err(h)) =
E
h∼HA

(err(h) −Eh′[err(h′)])2 
= E
h
"
E
x,y[errx,y(h) −E
h′[errx,y(h′)]]
2#
= E
h

E
x1,y1[errx1,y1(h) −E
h′[errx1,y1(h′)]] ·
E
x2,y2[errx2,y2(h) −E
h′[errx2,y2(h′)]]

= E
h
E
x1,y1
E
x2,y2

(errx1,y1(h) −E
h′[errx1,y1(h′)])(errx2,y2(h) −E
h′[errx2,y2(h′)])

=
E
x1,y1
E
x2,y2 E
h

(errx1,y1(h) −E
h′[errx1,y1(h′)])(errx2,y2(h) −E
h′[errx2,y2(h′)])

=
E
(x1,y1),(x2,y2)∼D2

Cov
h∼HA (errx1,y1(h), errx2,y2(h))

.
Lemma 2. For an IID test-set S = ((x1, y1), . . . , (xn, yn)), the expected variance in the test error
rate can be decomposed into a mixture of distribution-wise and example-wise variances.
E
S∼Dn

Var
h∼HA(errS(h))

= (1 −1/n) · Var
h∼HA(err(h)) + (1/n) ·
E
(x,y)∼D

Var
h∼HA(errx,y(h))

Proof.
E
S∼Dn

Var
h∼HA(errS(h))

= E
S
"
Var
h
 
1
n
n
X
i=1
errxi,yi(h)
!#
= E
S

1
n2
n
X
i=1
n
X
j=1
Cov
h (errxi,yi(h), errxj,yj(h))


= 1
n2
n
X
i=1
n
X
j=1
E
S

Cov
h (errxi,yi(h), errxj,yj(h))

= 1
n2
n
X
i=1
E
S

Var
h (errxi,yi(h))

+ 1
n2
n
X
i=1
X
j̸=i
E
S

Cov
h (errxi,yi(h), errxj,yj(h))

= 1
n2
n
X
i=1
E
xi,yi

Var
h (errxi,yi(h))

+ 1
n2
n
X
i=1
X
j̸=i
E
(xi,yi),(xj,yj)

Cov
h (errxi,yi(h), errxj,yj(h))

= n
n2 E
x,y

Var
h (errx,y(h))

+ n(n −1)
n2
E
(x1,y1),(x2,y2)

Cov
h (errx1,y1(h), errx2,y2(h))

= (1/n)
E
(x,y)∼D

Var
h∼HA(errx,y(h))

+ (1 −1/n)
E
(x1,y1),(x2,y2)

Cov
h (errx1,y1(h), errx2,y2(h))

= (1/n) ·
E
(x,y)∼D

Var
h∼HA(errx,y(h))

+ (1 −1/n) · Var
h∼HA(err(h)).
Where the last step uses Lemma 1.
14

Published as a conference paper at ICLR 2024
B.1
THEOREM 1
Theorem 1. In expectation, variance in test-set accuracy overestimates variance in true error.
E
S∼Dn

Var
h∼HA(errS(h))

≥Var
h∼HA(err(h))
Proof. The difference between the two terms is
E
S∼Dn

Var
h∼HA(errS(h))

−Var
h∼HA(err(h))
= 1
n

E
(x,y)∼D

Var
h∼HA(errx,y(h))

−Var
h∼HA(err(h))

= 1
n

E
x,y

Var
h (errx,y(h))

−
E
(x1,y1),(x2,y2)

Cov
h (errx1,y1(h), errx2,y2(h))

= 1
n

0.5 ·
E
x1,y1

Var
h (errx1,y1(h))

+ 0.5 ·
E
x2,y2

Var
h (errx2,y2(h))

−
E
(x1,y1),(x2,y2)

Cov
h (errx1,y1(h), errx2,y2(h))
 
= 1
2n
E
(x1,y1),(x2,y2)

Var
h (errx1,y1(h)) + Var
h (errx2,y2(h)) −2 Cov
h (errx1,y1(h), errx2,y2(h))

≥1
2n
E
(x1,y1),(x2,y2)

Var
h (errx1,y1(h)) + Var
h (errx2,y2(h)) −2
q
Var
h (errx1,y1(h)) Var
h (errx2,y2(h))

= 1
2n
E
(x1,y1),(x2,y2)
 q
Var
h (errx1,y1(h)) −
q
Var
h (errx2,y2(h))
2 
≥0.
Where the first two steps use Lemma 1 and then Lemma 2.
Note that this is almost always a strict greater-than, unless the test distribution is a single dirac delta.
B.2
THEOREM 2
Theorem 2. The following quantity is an unbiased estimator for Varh∼HA(err(h)).
ˆσ2
S =
n
n −1
 
Var
h∼HA(errS(h)) −1
n2
n
X
i=1
Var
h∼HA(errxi,yi(h))
!
Proof.
Var
h∼HA(err(h)) =
n
n −1

E
S∼Dn

Var
h∼HA(errS(h))

−(1/n) ·
E
(x,y)∼D

Var
h∼HA(errx,y(h))

=
n
n −1
 
E
S∼Dn

Var
h∼HA(errS(h))

−(1/n) ·
E
S∼Dn
"
1
n
n
X
i=1
Var
h∼HA(errxi,yi(h))
#!
=
E
S∼Dn
"
n
n −1
 
Var
h∼HA(errS(h)) −1
n2
n
X
i=1
Var
h∼HA(errxi,yi(h))
!#
Where the first equality is a rearrangement of Lemma 2.
15

Published as a conference paper at ICLR 2024
The quantity ˆσ2
S is also equal to
 n
2
−1 Pn
i=1
P
j̸=i Covh∼HA(errxi,yi(h), errxj,yj(h)). Comparing
this formula to Lemma 1 may help provide intuition for why it is an estimator for the distribution-
wise variance. The formulation given in Theorem 2 looks less intuitive, but the benefit is that we
only have to calculate n separate variances, rather than
 n
2

covariances.
We note that the proofs of Theorem 1 and Theorem 2 do not assume anything about the error function
errx,y(h)2, so, e.g., they are also true for regression tasks.
B.3
THEOREM 3
Theorem 3. If A is a training algorithm for binary classification which satisfies class-wise calibra-
tion (Definition 2), then its expected variance on an IID test-set of size n is
E
S∼Dn

Var
h∼HA(errS(h))

= err(A)
2n
+ (1 −1/n) · Var
h∼HA(err(h))
Proof. Define the random variable q(x) = Eh∼HA[1{h(x) = 1}] to be the proportion of training
runs which classify x as positive, with the randomness being over x ∼D. We first obtain a formula
for err(A) in terms of q. By the usual laws of conditional expectation we have:
err(A) =
E
x,y,h[errx,y(h)] = E
q [ E
x,y,h[errx,y(h) | q(x) = q]]
= E
q [ E
x,y,h[1{h(x)̸ = y} | q]]
= E
q [ E
x,y,h[1{y = 0}1{h(x) = 1} + 1{y = 1}1{h(x) = 0} | q]]
= E
q [ E
x,y[E
h[1{y = 0}1{h(x) = 1} + 1{y = 1}1{h(x) = 0} | q] | q]]
= E
q [ E
x,y[1{y = 0} E
h[1{h(x) = 1} | q] + 1{y = 1} E
h[1{h(x) = 0} | q] | q]]
= E
q [ E
x,y[q · 1{y = 0} + (1 −q) · 1{y = 1} | q]]
= E
q [q(1 −E
x,y[1{y = 1} | q]) + (1 −q) E
x,y[1{y = 1} | q]].
Using the assumption of class-wise calibration, this formula simplifies to Eq[2q(1 −q)]. Next we
analyze the example-wise variance. We have:
E
x,y[Var
h (errx,y(h))] = E
q [ E
x,y[Var
h (1{h(x)̸ = y)}) | q(x) = q]]
= E
q [ E
x,y[E
h[1{h(x)̸ = y}](1 −E
h[1{h(x)̸ = y}]) | q]]
= E
q [ E
x,y[E
h[1{h(x) = 1}] E
h[1{h(x) = 0}] | q]]
= E
q [ E
x,y[q(1 −q) | q]]
= E
q [q(1 −q)].
Where the second equality uses the formula for variance of a Bernoulli variable. The third equality
uses the fact that, regardless of whether y = 0 or y = 1, the product Eh[1{h(x)̸ = y}](1 −
Eh[1{h(x)̸ = y}]) is equal to Eh[1{h(x) = 1}] Eh[1{h(x) = 0}]. The fourth equality applies the
assumption of class-wise calibration.
Combining the above two results yields Ex,y[Varh(errx,y(h))] = err(A)/2. Therefore by Lemma 2
we have:
E
S∼Dn

Var
h∼HA(errS(h))

= (1 −1/n) · Var
h∼HA(err(h)) + (1/n) ·
E
(x,y)∼D

Var
h∼HA(errx,y(h))

= err(A)
2n
+ (1 −1/n) · Var
h∼HA(err(h)).
2Other than it being non-pathological enough to allow the interchanges of expectation via Fubini’s theorem.
16

Published as a conference paper at ICLR 2024
B.4
THEOREM 4
Theorem 4. If A is a training algorithm for k-way classification which satisfies class-wise calibra-
tion (Definition 2), then its expected variance on an IID test-set of size n is at least
E
S∼Dn

Var
h∼HA(errS(h))

≥err(A)
nk
Proof. For each class c ∈{1, . . . , k}, define the random variable qc(x) = Eh∼HA[1{h(x) = c}]
to be the proportion of runs of training which classify x as c. Let q(x) = (q1(x), . . . , qk(x)) be the
vector of these variables. The laws of conditional expectation yield the following expression for the
expected error.
err(A) =
E
x,y,h[errx,y(h)]
= E
q [ E
x,y,h[errx,y(h) | q(x) = q]]
= E
q [ E
x,y,h[1{h(x)̸ = y} | q]]
= E
q
"
E
x,y,h
" k
X
c=1
1{y = c}1{h(x)̸ = c} | q
##
= E
q
"
E
x,y
"
E
h
" k
X
c=1
1{y = c}1{h(x)̸ = c} | q
#
| q
##
= E
q
" k
X
c=1
(1 −qc) E
x,y [1{y = c} | q]
#
= E
q
" k
X
c=1
qc(1 −qc)
#
.
The last step uses the assumption of class-wise calibration. We next derive a related expression for
the example-wise variance.
E
x,y[Var
h (errx,y(h))] = E
q [ E
x,y[Var
h (1{h(x)̸ = y)}) | q(x) = q]]
= E
q [ E
x,y[E
h[1{h(x)̸ = y} | q](1 −E
h[1{h(x)̸ = y} | q]) | q]]
= E
q [ E
x,y[qy(1 −qy) | q]]
= E
q
"
E
x,y
" k
X
c=1
1{y = c}qc(1 −qc) | q
##
= E
q
" k
X
c=1
E
x,y[1{y = c} | q] · qc(1 −qc)
#
= E
q
" k
X
c=1
q2
c(1 −qc)
#
We now analyze the ratio between Pk
c=1 q2
c(1 −qc) and Pk
c=1 qc(1 −qc).
17

Published as a conference paper at ICLR 2024
Without loss of generality, let q1 ≤q2 ≤· · · ≤qk be in nondecreasing order. Then we have
k
X
c=1
q2
c(1 −qc) = k ·
 
1
k
k
X
c=1
qc · qc(1 −qc)
!
≥k ·
 
1
k
k
X
c=1
qc
! 
1
k
k
X
c=1
qc(1 −qc)
!
= 1
k
k
X
c=1
qc(1 −qc).
The inequality step is due to an application of Chevychev’s sum inequality (Hardy et al., 1934),
which is possible because the series q1(1 −q1), . . . , qk(1 −qk) is nondecreasing, which we prove
as follows.
We first recall that Pk
c=1 qc = 1, and that we assumed without loss of generality that q1 ≤· · · ≤qk.
For the first k −1 terms, the monotonicity of the mapping x 7→x(1 −x) on the interval [0, 1/2],
combined with the fact that qc ≤1/2 for c ∈{1, . . . , k −1}, implies q1(1 −q1) ≤· · · ≤qk−1(1 −
qk−1). It remains to show that qk−1(1 −qk−1) ≤qk(1 −qk). If qk ≤1/2, then this is again due to
the monotonicity of x 7→x(1−x) on [0, 1/2]. Otherwise if qk ≥1/2, then combining qk−1 ≤1−qk
and (1 −qk) ≤1/2 yields qk−1(1 −qk−1) ≤(1 −qk)(1 −(1 −qk)) = qk(1 −qk). Either way, we
have shown that q1(1 −q1) ≤· · · ≤qk(1 −qk) is in nondecreasing order, allowing the application
of Chevychev’s sum inequality above.
Putting Lemma 2 together with the above results, as follows, yields the theorem.
E
S∼Dn

Var
h∼HA(errS(h))

= (1 −1/n) · Var
h∼HA(err(h)) + (1/n) ·
E
(x,y)∼D

Var
h∼HA(errx,y(h))

≥(1/n) · E
x,y

Var
h (errx,y(h))

= 1
n E
q
" k
X
c=1
q2
c(1 −qc)
#
≥1
nk E
q
" k
X
c=1
qc(1 −qc)
#
= err(A)
nk
.
B.5
REPLICATION OF THE MAIN RESULT FROM JIANG ET AL. (2021)
Because it is theoretically related to our results, we include a simplified proof of the main result
from Jiang et al. (2021), which is Theorem 4.1 of that work.
Theorem 5 (Jiang et al. (2021)). If a stochastic training algorithm A is class-wise calibrated, then
its error rate is equal to its expected disagreement rate between two trained networks.
err(A) =
E
h1,h2∼H2
A,(x,y)∼D
[1{h1(x)̸ = h2(x)}]
18

Published as a conference paper at ICLR 2024
Proof. Let q : X 7→[0, 1]k be defined as in Section B.4. Then the laws of conditional expectation
yield the following expression for the disagreement rate.
E
h1,h2∼H2
A,(x,y)∼D
[1{h1(x)̸ = h2(x)}] = E
q

E
h1,h2,(x,y) [1{h1(x)̸ = h2(x)} | q(x) = q]

= E
q

E
h2,(x,y)

E
h1
[1{h1(x)̸ = h2(x)} | q] | q

= E
q
"
E
h2,(x,y)
" k
X
c=1
qc · 1{h2(x)̸ = c} | q
##
= E
q
"
E
x,y
"
E
h2
" k
X
c=1
qc · 1{h2(x)̸ = c} | q
#
| q
##
= E
q
"
E
x,y
" k
X
c=1
qc(1 −qc) | q
##
= E
q
" k
X
c=1
qc(1 −qc)
#
= err(A).
Each conversion of a conditional expectation over HA to a formula involving q uses the assumption
of class-wise calibration. The final step is via the fact that err(A) = Eq
Pk
c=1 qc(1 −qc) as we
showed in Section B.4.
19

Published as a conference paper at ICLR 2024
Figure 9: Distribution shift produces excess distribution-wise variance between runs. Across 1,000 runs
of ImageNet training, both the ImageNet validation set and ImageNet-V2 have accuracy distributions close to
that predicted by the independent errors hypothesis, and hence, little distribution-wise variance. On the other
hand, the accuracy distributions on distribution-shifted sets have significant excess variance, indicating genuine
differences between trained models.
C
IMAGENET AND DISTRIBUTION SHIFTS
In this section we show that shifted distributions of test data have increased variance in their accuracy
distributions across repeated runs of training. We additionally confirm that the findings of Section 3
generalize to standard ImageNet training.
Our experiment is as follows. We independently train 1,000 ResNet-18s on ImageNet using a stan-
dard configuration (Section A.2). Their average top-1 accuracy is 71.0%. We study the predictions
of these networks on the ImageNet validation set, ImageNet-V2, and three shifted datasets.
We first look at the ImageNet validation set. In Figure 9 (rightmost) we observe that the empirical
accuracy distribution on this set closely matches the one predicted by the independent errors hypoth-
esis. The observed standard deviation is 0.118%, and Equation 3 estimates that the distribution-wise
standard deviation is 0.034%. This value is close to what we found for CIFAR-10, confirming that
both training scenarios adhere to the conclusions of Section 3.
Next we consider ImageNet-V2 (Recht et al., 2019). This dataset is intended to have the same
distribution of examples as ImageNet, and we find that its accuracy distribution has similar statistical
properties as well. In particular, we find that the distribution predicted by independent errors also
closely matches its true distribution. Equation 3 estimates a distribution-wise standard deviation of
0.071%, which is larger than what we found on the ImageNet validation set, but still relatively small.
We note that the test-set accuracy distribution for this dataset is wider, but this can be explained
simply by the fact that it is 5× smaller than the ImageNet validation set.
By contrast, ImageNet-R (Hendrycks et al., 2021), ObjectNet (Barbu et al., 2019) and ImageNet-
Sketch (Wang et al., 2019) all have different statistical behavior compared to the first two datasets.
These datasets are constructed to have shifted distributions relative to ImageNet, and we find that
their accuracy distributions have significant excess variance over that predicted by the independent
errors hypothesis. We estimate using Equation 3 that the distribution-wise standard deviations for
these datasets are 0.181%, 0.179%, and 0.257% respectively. This indicates significant genuine
variability between repeated runs of training in terms of their performance on these distributions.
The above result provides empirical confirmation of a theory advanced by Cohen-Wang et al. (2024).
The authors observed that pretraining provides a greater performance benefit for models evaluated
on out-of-support distribution shifts like ImageNet-Sketch than it does for in-support shifts like
ImageNet-V2. Seeking to understand this phenomenon, they analyzed a simple logistic regression
setting and found that without pretraining, out-of-support shifts can induce more variance in behav-
ior between runs of training than in-support shifts, due to a greater dependence on the initialization.
Our above result, namely that ImageNet-Sketch has a distribution-wise standard deviation of 0.257%
across repeated ResNet-18 trainings whereas ImageNet-V2 has only 0.071% (13× less variance),
provides evidence that the logistic regression-based theory of Cohen-Wang et al. (2024), beyond
being a source of useful intuition, is also directly true for neural networks.
In Figure 10 we additionally investigate correlations between pairs of these five datasets.
The
strongest correlation is between ImageNet-R and ImageNet-Sketch, with R2 = 0.14 (p < 10−8).
20

Published as a conference paper at ICLR 2024
Figure 10: Correlations between distribution shifts. We visualize the accuracy values of 1,000 ResNets
which were independently trained on ImageNet. Each network is evaluated on the ImageNet validation set, as
well as four extra datasets (IN-V2, IN-R, IN-Sketch, and ObjectNet). We display the scatterplots of accuracy
on each of the
 5
2

pairs. The following pairs had statistically significant correlations: (ImageNet-R, ImageNet),
(ImageNet-Sketch, ImageNet), (ObjectNet, ImageNet-V2), and (ImageNet-Sketch, ImageNet-R). All but one
pair have weak correlations with R2 < 0.01. The strong correlation is between ImageNet-R and ImageNet-
Sketch with R2 = 0.14. We hypothesize that this is caused by the fact that both sets contain many sketch-like
images, so that this pair has a) similar distributions and b) shifted distributions relative to the training set. We
report two-sided p-values.
Manual inspection shows that both ImageNet-Sketch and ImageNet-R contain many sketch-like
images, suggesting that similar features may induce correlation between distributions. All other
pairs have R2 < 0.01.
For example, ImageNet-Sketch is decorrelated from ObjectNet, with
R2 = 0.001 (p = 0.34).
Overall, our findings suggest that training instability is in some sense a relative notion. ImageNet
training is highly stable when evaluated on the main distribution, with a small standard deviation
of 0.034% on the underlying distribution of the ImageNet validation set. But it is unstable on
shifted distributions, with ImageNet-Sketch having a much larger standard deviation of 0.257%.
This serves as a caveat to the main takeaway: from the perspective of the main training distribution,
all runs perform at nearly the same level, but from the perspective of shifted distributions, there are
sometimes significant differences between runs.
D
REPLICATION STUDY OF SUMMERS & DINNEEN (2021)
D.1
THE THREE SOURCES OF RANDOMNESS
Training neural networks typically involves three sources of stochasticity: model initialization, data
ordering, and data augmentations. In this section we investigate how each of these sources con-
tributes to the final variance between runs that we observe at the end of training.
We develop a CIFAR-10 training framework3 that allows each source to be independently controlled
by one of three different seeds. For example, when the data-augmentation seed is fixed and the data-
order seed is varied, then the set of augmented images seen by the network throughout training will
remain the same, but will be presented in a different order. When all three seeds are fixed, training
is deterministic, so that repeated runs produce the same network every time. Standard training is
equivalent to allowing all three seeds to vary.
Our experiment is to fix two seeds, and vary just the third (e.g., varying only the data order while
keeping the model initialization and data augmentations fixed). Our naive intuition is that each
factor contributes some part to the overall variance, so that this should decrease variance relative to
the baseline of varying all three seeds.
3https://github.com/KellerJordan/CIFAR10-isolated-rng
21

Published as a conference paper at ICLR 2024
Figure 11: One source of stochasticity yields the same variance as three for full training. When training
for only 1 epoch, varying all three sources of randomness induces a standard deviation of 1.33% in test-set
accuracy between runs, while varying any single source alone induces 25-40% less variance. But when training
for 64 epochs, varying any one source induces as much variance as all three together. Each distribution corre-
sponds to 4,000 runs of training.
Figure 12: Neural network training has high sensitivity to initial conditions. (Left:) For short trainings,
pairs of runs which differ only by one network having been “poked” (i.e., had a single weight changed slightly
at initialization) disagree on 7.0-7.5% of predictions. Pairs of runs with fully different random seeds disagree
more, on ∼8.5% of predictions. For long trainings, there is almost no difference. The histograms are over
repeated pairs of runs. (Right:) The earlier a network is poked during the training process, the more its predic-
tions will disagree with the network that trained unperturbed from the same random seed.
We show the results in Figure 11. For short trainings of under 16 epochs, this intuition is correct.
For example, when training for 4 epochs, if we fix the data order and augmentations, while varying
only the model initialization, then variance in test-set accuracy is reduced by 26%, such that the
standard deviation decreases from 0.45% to 0.38%.
However, for longer trainings of 32 epochs or more, varying just one of the three random factors
produces approximately the same variance as the baseline of varying all three. For example, across
4,000 runs of training for 64 epochs, varying just the model initialization (with data ordering and
augmentation fixed) produces a standard deviation of 0.158%, almost the same as the baseline, which
has 0.160%. At n = 4, 000 runs of training this is not a statistically significant difference, so it is
possible that the true values are the same, or that they differ by a small amount. We conclude that
for this training regime, any single random factor suffices to generate the full quantity of variance,
rather than each factor contributing to overall variance.
D.2
SENSITIVITY TO INITIAL CONDITIONS
In the previous section, we showed that when training to convergence, varying just the model ini-
tialization (or just the data ordering, or augmentations) produces approximately the same quantity
of variance between runs as a baseline fully random setup. In this section we find that even varying
a single weight at initialization suffices. Our findings replicate the work of Summers & Dinneen
(2021), who reach similar conclusions.
22

Published as a conference paper at ICLR 2024
Consider multiplying a single random weight in the network by 1.001. We call this “poking” the
network. This is a tiny change; recent work in quantization (e.g., Dettmers et al., 2022) suggests that
trained models can typically have all their weights modified more than this without losing accuracy.
Nevertheless, in Figure 12 we demonstrate that poking the network early in training produces a large
difference in the final result. Our experiment is to run two trainings with the same random seed, but
with one network being “poked” at some point during training. We measure the disagreement rate
between the two networks, i.e., the fraction of their test-set predictions that differ. For short trainings,
poking induces much less disagreement than changing the random seed. But when training for
128 epochs, poking alone produces an average disagreement of 5.14%, barely less than the 5.19%
produced by using entirely different random seeds. We have also observed that varying just the first
batch of data, or the numerical precision of the first step (e.g., fp16 vs. fp32) has a similar effect. We
conclude that almost all variation between runs is not produced by specific sources of randomness
like model initialization, data ordering, etc., but is instead intrinsic to the training process, which
has extreme sensitivity to initial conditions.
E
ADDITIONAL FIGURES
Figure 13: There exist five pairs whose errors deviate by ≥2% from independence. The first column is
the product of the probability (over training stochasticity) that the trained network predicts the first example
correctly and the probability that it predicts the second example correctly. The second column is the probability
that the trained network predicts both of them correctly. Each quantity is measured across 60,000 runs of
our 64-epoch training configuration. The independent errors hypothesis (Definition 1) predicts that these two
quantities should be equal. Out of all
 10,000
2

pairs of examples in the CIFAR-10 test-set, only these five deviate
by more than 2% from that prediction. The remaining 49,994,995 pairs are all within 2% of that prediction.
23

Published as a conference paper at ICLR 2024
Figure 14: The binomial approximation overestimates variance. Compared to the empirical distribution
of test-set accuracy, the binomial approximation predicts a distribution with too much variance. We use p =
0.9441 (the average accuracy) and n = 10, 000 (the size of the test-set) to simulate 60, 000 samples from
Binom(n, p), which we find overestimates variance by a factor of ≈2.5×. In comparison, the framework of
independent errors (Definition 1) provides an accurate estimate.
24
