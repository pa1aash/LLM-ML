---
title: 'Zen-NAS: A Zero-Shot NAS for High-Performance Deep Image Recognition (full
  text)'
id: zen-nas-a-zero-shot-nas-for-high-performance-deep-image-recognition-full-text
tags:
- llm-nas-feedback-positioning-7125b1
- locus-l5
- zero-cost-proxy
- nas
created: '2026-08-16T18:36:56.519097Z'
updated: '2026-08-16T18:37:34.864945Z'
source: https://arxiv.org/pdf/2102.01063
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Full-text ICCV 2021 paper (Alibaba) proposing Zen-Score, a zero-shot proxy
  measuring network expressivity via expected Gaussian complexity of the input gradient,
  rescaled by BatchNorm variance statistics to fix a 'scale-sensitive' overflow/underflow
  problem in deep vanilla networks; Zen-Score is one of RZ-NAS's five candidate proxies.
  Reports Kendall's tau of 0.91 (CIFAR-10) and 0.88 (CIFAR-100) between Zen-Score
  and accuracy on ResNet-50-derived structures -- much higher than the 0.28-0.29 correlation
  ZiCo's paper reports for Zen-score on NATS-Bench-TSS, indicating benchmark/search-space-dependent
  correlation strength.
---

Zen-NAS: A Zero-Shot NAS for High-Performance Image
Recognition
Ming Lin *
Alibaba Group
Bellevue, Washington, USA
ming.l@alibaba-inc.com
Pichao Wang
Alibaba Group
Bellevue, Washington, USA
pichao.wang@alibaba-inc.com
Zhenhong Sun
Alibaba Group
Hangzhou, Zhejiang, China
zhenhong.szh@alibaba-inc.com
Hesen Chen
Alibaba Group
Hangzhou, Zhejiang, China
hesen.chs@alibaba-inc.com
Xiuyu Sun
Alibaba Group
Hangzhou, Zhejiang, China
xiuyu.sxy@alibaba-inc.com
Qi Qian
Alibaba Group
Bellevue, Washington, USA
qi.qian@alibaba-inc.com
Hao Li
Alibaba Group
Hangzhou, Zhejiang, China
lihao.lh@alibaba-inc.com
Rong Jin
Alibaba Group
Hangzhou, Zhejiang, China
jinrong.jr@alibaba-inc.com
August 24, 2021
Abstract
Accuracy predictor is a key component in Neural Architecture Search (NAS) for ranking architectures.
Building a high-quality accuracy predictor usually costs enormous computation. To address this issue,
instead of using an accuracy predictor, we propose a novel zero-shot index dubbed Zen-Score to rank the
architectures. The Zen-Score represents the network expressivity and positively correlates with the model
accuracy. The calculation of Zen-Score only takes a few forward inferences through a randomly initialized
network, without training network parameters. Built upon the Zen-Score, we further propose a new NAS
algorithm, termed as Zen-NAS, by maximizing the Zen-Score of the target network under given inference
budgets. Within less than half GPU day, Zen-NAS is able to directly search high performance architectures
in a data-free style. Comparing with previous NAS methods, the proposed Zen-NAS is magnitude times
faster on multiple server-side and mobile-side GPU platforms with state-of-the-art accuracy on ImageNet.
Searching and training code as well as pre-trained models are available from https://github.com/
idstcv/ZenNAS.
*Accepted by ICCV 2021. Author home page https://minglin-home.github.io
1
arXiv:2102.01063v4  [cs.CV]  23 Aug 2021
0
2
4
6
8
Inference Latency (ms)
70
75
80
Top-1 Accuracy (%)
4.9x speed-up
NVIDIA V100 FP16
RegNet
ResNet
EﬃcientNet
OFANet
DenseNet
ResNeSt
MobileNet
MnasNet
DNANet
DFNet
ZenNet
Figure 1: ZenNets top-1 accuracy v.s. inference latency (milliseconds per image) on ImageNet. Bench-
marked on NVIDIA V100 GPU, half precision (FP16), batch size 64, searching cost 0.5 GPU day.
1
Introduction
The design of high-performance deep neural networks is a challenging task. Neural Architecture Search
(NAS) methods facilitate this progress. There are mainly two key components, architecture generator and ac-
curacy predictor, in existing NAS algorithms. The generator proposes potential high-performance networks
and the predictor predicts their accuracies. Popular generators include uniform sampling [13], evolutionary
algorithm [41] and reinforcement learning [30]. The accuracy predictors include brute-force methods [42,
57, 3, 41], predictor-based methods [30, 56, 29] and one-shot methods [26, 61, 69, 62, 57, 59, 6, 66, 54, 5].
A major challenge of building a high-quality accuracy predictor is the enormous computational cost.
Both brute-forced methods and predictor-based methods require to train considerable number of networks.
The one-shot methods reduce the training cost via parameter sharing. Albeit being more efﬁcient than
brute-forced methods, the one-shot methods still need to train a huge supernet which is still computationally
expensive. Recent studies also ﬁnd that nearly all supernet-based methods suffer from model interfering
[5, 63] which degrades the quality of accuracy predictor [46]. In addition, since the supernet must be much
larger than the target network, it is difﬁcult to search large target networks under limited resources. These
issues make the one-shot methods struggling in designing high-performance networks.
To solve these problems, instead of using an expensive accuracy predictor, we propose an almost zero-
2
cost proxy, dubbed Zen-Score, for efﬁcient NAS. The Zen-Score measures the expressivity [39, 31] of a
deep neural network and positively correlates with the model accuracy. The computation of Zen-Score
only takes a few forward inferences on randomly initialized network using random Gaussian inputs, making
it extremely fast, lightweight and data-free. Moreover, Zen-Score deals with the scale-sensitive problem
caused by Batch Normalization (BN)[4, 35], making it widely applicable to real-world problems.
Based on Zen-Score, we design a novel Zen-NAS algorithm. It maximizes the Zen-Score of the target
network within inference budgets. Zen-NAS is a Zero-Shot method since it does not optimize network
parameters during search 1. We apply Zen-NAS to search optimal networks under various inference budgets,
including inference latency, FLOPs (Floating Point Operations) and model size, and achieve the state-of-the-
art (SOTA) performance on CIFAR-10/CIFAR-100/ImageNet, outperforming previous human-designed and
NAS-designed models by a large margin. Zen-NAS is the ﬁrst zero-shot method that achieves SOTA results
on large-scale full-resolution ImageNet-1k dataset [12] by the time of writing this work [32, 1, 7].
Our approach is inspired by recent advances in deep learning studies [34, 11, 23, 39, 9, 28, 31, 44, 47,
14, 60] which show that deep models are superior than shallow ones since deep models are more expressive
under the same number of neurons. According to the bias-variance trade-off in statistical learning theory
[19], increasing the expressivity of a deep network implies smaller bias error. When the size n of training
dataset is large enough, the variance error will diminish as O(1/√n) →0. This means that the general-
ization error is dominated by the bias error which could be reduced by more expressive networks. These
theoretical results are well-aligned with large-scale deep learning practices[36, 52, 37].
We summarize our main contributions as follows:
• We propose a novel zero-shot proxy Zen-Score for NAS. The proposed Zen-Score is computationally
efﬁcient and is proved to be scale-insensitive in the present of BN. A novel NAS algorithm termed
Zen-NAS is proposed to search for networks with maximal Zen-Score in the design space.
• Within half GPU day, the ZenNets designed by Zen-NAS achieve up to 83.6% top-1 accuracy on Im-
ageNet that is as accurate as EfﬁcientNet-B5 with inference speed magnitude times faster on multiple
hardware platforms. To our best knowledge, Zen-NAS is the ﬁrst zero-shot method that outper-
forms training-based methods on ImageNet.
2
Related Work
We brieﬂy review the related works. For comprehensive review of NAS, the monograph [43] is referred to.
In the early days of NAS, brute-force methods are adopted to search architectures by directly training
a network to obtain its accuracy. For example, the AmoebaNet [41] conducts structure search on CIFAR-
10 using Evolutionary Algorithm (EA) [20] and then transfers the structure to ImageNet. It takes about
3150 GPU days of searching and achieves 74.5% top-1 accuracy on ImageNet. Inspired by the success of
AmoebaNet, many EA-based NAS algorithms are proposed to improve the searching efﬁciency, such as
EcoNAS [69], CARS [62], GeNet [57] and PNAS [25]. These methods search on down-sampled images or
reduce the number of queries. Reinforced Learning is another popular generator (sampler) in NAS, including
NASNet [70], Mnasnet [49] and MetaQNN [3].
Both EA and RL based methods require lots of network training. To address this problem, the predictor-
based methods encode architectures into high dimensional vectors. A number of architectures are trained to
obtain their accuracies [30, 29] and then are used as training data for learning accuracy predictor. The one-
shot methods further reduce the training cost by training a big supernet. This framework is widely applied
1Obviously, the ﬁnal searched architecture must be trained on the target dataset before deployment.
3
in many efﬁcient NAS methods, including DARTS [26], SNAS [59], PC-DARTS [61], ProxylessNAS [6],
GDAS [66], FBNetV2 [54], DNANet [21], Single-Path One-Shot NAS [13].
Although the above efforts have greatly reduced the searching cost, their top-1 accuracies on ImageNet
are below 80.0%. The authors of OFANet [5] noted that weight-sharing suffers from model interfering.
They propose a progressive-shrinking strategy to address this issue. The resultant OFANet achieves 80.1%
accuracy after searching for 51.6 GPU days. EfﬁcientNet [50] is another high precision network designed
by NAS. It takes about 3800 GPU days to search EfﬁcientNet-B7 whose accuracy is 84.4%. In comparison,
Zen-NAS achieves 83.6% accuracy while using magnitude times fewer resources.
A few on-going works are actively exploring zero-shot proxies for efﬁcient NAS. However, these efforts
have not delivered the SOTA results. In a recent empirical study, [1] evaluates the performance of six
zero-shot pruning proxies on NAS benchmark datasets. The synﬂow [51] achieves best results in their
experiments. We compare synﬂow with Zen-Score under fair settings and show that Zen-Score achieves
+1.1% better accuracy on CIFAR-10 and +8.2% better accuracy on CIFAR-100. The concurrent work TE-
NAS [7] uses a combination of NTK-score and network expressivity as NAS proxy. Speciﬁcally, the TE-
NAS estimates the expressivity by directly counting the number of active regions RN on randomly sampled
images. In comparison, Zen-Score not only considers the distribution of linear regions but also considers
the Gaussian complexity of linear classiﬁer in each linear region, giving a more accurate estimation of
network expressivity. The computation of Zen-Score is 20 to 28 times faster than TE-NAS score. In terms of
performance, TE-NAS achieves 74.1% top-1 accuracy on ImageNet, lagging behind SOTA baselines. Zen-
NAS achieves +9.5% better accuracy within similar searching cost. Another concurrent work NASWOT
[33] computes the architecture score according to the kernel matrix of binary activation patterns between
mini-batch samples. It achieves similar top-1 accuracies on CIFAR-10/CIFAR-100 as TE-NAS.
It is important to distinguish Zen-NAS from unsupervised NAS (UnNAS) [24]. In UnNAS, the network
is trained to predict the pre-text tasks therefore it still requires parameter training. In Zen-NAS, no parameter
training is required during the search.
In this work, we mostly focus on the vanilla network space described in the next section. Several previous
works design networks in a more general irregular design space, such as DARTS [26] and RandWire [58].
Zen-NAS cannot be applied to these irregular design spaces since Zen-Score is not mathematically well-
deﬁned in irregular design spaces. In practice, the vanilla network space is a large enough space which
covers most SOTA networks, including but not limited to ResNet, MobileNet and EfﬁcientNet. Particularly,
Zen-NAS outperforms DARTS-based methods by a signiﬁcant margin on ImageNet.
3
Expressivity of Vanilla Network
In this section, we discuss how to measure the expressivity of vanilla convolutional neural network (VCNN)
family, an ideal prototype for theoretical studies. We show that the expressivity of a network can be efﬁ-
ciently measured by its expected Gaussian complexity, or Φ-score for short. In the next section, we further
show that for very deep networks, directly computing Φ-score incurs numerical overﬂow. This overﬂow can
be addressed by adding BN layers and then re-scaling the Φ-score by a constant. This new score is named
as Zen-Score in Section 4.
3.1
Notations
An L-layer neural network is formulated as a function f : Rm0 →RmL where m0 is the input dimension
and mL is the output dimension. x0 ∈Rm0 denotes the input image. Correspondingly, the output feature
map of the t-th layer is denoted by xt. The t-th layer has mt−1 input channels and mt output channels. The
4
convolutional kernel is θt ∈Rmt×mt−1×k×k. The image resolution is H × W. The mini-batch size is B.
The Gaussian distribution of mean µ and variance σ2 is denoted by N(µ, σ).
3.2
Vanilla Convolutional Neural Network
The vanilla convolutional neural network (VCNN) is a widely used prototype in theoretical studies [39,
47, 14]. The main body of a vanilla network is stacked by multiple convolutional layers. Each layer consists
of one convolutional operator followed by RELU activation. All other components are removed from the
backbone, including residual link and Batch Normalization. After the main body, global average pool layer
(GAP) reduces the feature map resolution to 1x1, followed by a fully-connected layer. At the end a soft-max
operation converts the network output to label prediction. Given the input x and network parameters θ,
f(x|θ) refers to the output of the main body of the network, that is the feature map before the GAP layer
(pre-GAP layer). We measure the network expressivity with respect to pre-GAP because it contains most of
the information we need.
Modern networks use auxiliary structures such as residual link , Batch Normalization and self-attention
block [16]. These structures will not signiﬁcantly affect the representation power of networks. For example,
BN layer can be merged into convolutional kernel via kernel fusion. Self-attention linearly combines existing
feature maps hence spans the same subspace. Therefore, these structures are temporarily removed when
measuring network expressivity and then added back in training and testing stages. For non-RELU activation
functions, they are replaced by RELU in a similar way. These simple modiﬁcations make our method
applicable to a majority of non-VCNN models widely used in practice. In fact, nearly all single-branch
feed-forward networks can be converted to vanilla network by the aforementioned modiﬁcations.
3.3
Φ-Score as Proxy of Expressivity
Given a VCNN f(x|θ), we propose a novel numerical index Φ-score as a proxy of its expressivity. The
deﬁnition of Φ-score is inspired by recent theoretical studies on deep network expressivity [47, 60]. A key
observation in these studies is that a vanilla network can be decomposed into piece-wise linear functions
conditioned on activation patterns [34]:
Lemma 1 ([34, 31]). Denote the activation pattern of the t-th layer as At(x). Then for any vanilla network
f(·),
f(x|θ) =
X
Si∈S
Ix(Si)W Six
(1)
where Si is a convex polytope depending on {A1(x), A2(x), · · · , AL(x)}; S is a ﬁnite set of convex poly-
topes in Rm0; Ix(Si) = 1 if x ∈Si otherwise zero; W Si is a coefﬁcient matrix of size RmL×m0.
According to Lemma 1, any vanilla network is an ensemble of piece-wise linear functions segmented
by convex polytopes S = {S1, S2, · · · , S|S|} where |S| is the number of linear-regions (see Figure 2 in
[14]. The number of linear regions |S| has been used as expressivity proxy in several theoretical studies
[34, 47, 14, 67, 60]. However, directly using |S| incurs two limitations: a) Counting |S| for large network
is computationally infeasible; b) The representation power of each WSi is not considered in the proxy. The
ﬁrst limitation is due to fact that the number of linear regions grow exponentially for large networks [34, 60].
To understand the second limitation, we recall the Gaussian complexity [18] of linear classiﬁers:
Lemma 2 ([18]). For linear function class {f : f(X) = WX s.t. ∥W∥F ≤G}, its Gaussian complexity is
upper bounded by O(G).
5
0
10
20
30
number of layers
25
50
75
score
nan
w/o BN
(a) Φ-score of Pw/oBN networks
0
10
20
30
number of layers
6
8
10
score
with BN
(b) Φ-score of PBN networks
0
10
20
30
number of layers
25
50
75
score
Zen
(c) Zen-Score of PBN networks
0
20
40
60
bottleneck channels
11
12
score
w/o BN
(d) Φ-score of Qw/oBN networks
0
20
40
60
bottleneck channels
5.0
5.5
6.0
score
with BN
(e) Φ-score of QBN networks
0
20
40
60
bottleneck channels
11
12
score
Zen
(f) Zen-Score of QBN networks
Figure 2: Φ-scores and Zen-Scores of networks, with different depths and bottleneck channels.
In other words, Lemma 2 says that the expressivity of linear function class measured by Gaussian com-
plexity is controlled by the Frobenius norm of its parameter matrix W. Inspired by Lemma 1 and Lemma 2,
we deﬁne the following index for measuring network expressivity :
Deﬁnition 1 (Φ-score for VCNN). The expected Gaussian complexity for a vanilla network f(·) is deﬁned
by
Φ(f) = log Ex,θ
( X
Si∈S
Ix(Si)∥W Si∥F
)
(2)
= log Ex,θ∥∇xf(x|θ)∥F .
(3)
In Deﬁnition 1, we measure the network expressivity by its expected Gaussian complexity, or Φ-score for
short. Since any VCNN is ensemble of linear functions, it is nature to measure its expressivity by averaging
the Gaussian complexity of linear function in each linear region. To this end, we randomly sample x and
θ from some prior distributions and then average ∥WSi∥F . This is equivalent to compute the expected
gradient norm of f with respect to input x. In our implementation, x and θ are sampled from standard
Gaussian distribution which works well in practice. It is important to note that in Φ-score, only the gradient
of x rather than θ is involved. This is different to zero-cost proxies in [1] which compute gradient of θ in
their formulations. These proxies measure the trainability [55, 7] instead of the expressivity of networks.
4
Zen-Score and Zen-NAS
In this section, we show that directly computing Φ-score for very deep networks incurs numerical overﬂow
due to the gradient explosion without BN layers. The gradient explosion could be resolved by adding BN
layers back but the Φ-score will be adaptively re-scaled, making it difﬁcult to compare Φ-score between
different networks. The same phenomenon has been known as ‘scale-sensitive’ problem in deep learning
complexity analysis [4, 35]. To address this open question, we propose to re-scale the Φ-score one more
6
time by the product of BN layers’ variance statistics. This new score is denoted as Zen-Score in order to
distinguish from the original Φ-score. The Zen-Score is proven to be scale-insensitive. Finally, we present
Zen-NAS algorithm built on Zen-Score and demonstrate its effectiveness in the next section.
4.1
Overﬂow and BN-rescaling
When computing Φ-score for very deep vanilla networks, numerical overﬂow incurs almost surely. This is
because BN layers are removed from the network and the magnitude of network output grows exponentially
along depth. To see this, we construct a set of vanilla networks Pw/oBN without BN layers. All networks
have the same widths but different depths. Figure 2(a) plots the Φ-scores for Pw/oBN. After 30 layers, Φ-
score overﬂows. To address the overﬂow, we add BN layers back and compute the Φ-scores in Figure 2(b).
This time the overﬂow dismisses but the Φ-scores are scaled-down by a large factor. This phenomenon is
termed as BN-rescaling.
To demonstrate that BN-rescaling disturbs architecture ranking, we construct another two set of net-
works, Qw/oBN and QBN, with and without BN respectively. All networks have two layers and have the
same number of input and ﬁnal output channels. The number of bottleneck channels, that is the width of
the hidden layer, varies from 2 to 60. The corresponding Φ-score curves are plotted in Figure 2(d) and (e)
respectively. When BN layer is presented, the Φ-score becomes nearly constant for all networks. This will
confuse the architecture generator and drive the search to a wrong direction.
4.2
From Φ-Score to Zen-Score
Algorithm 1 Zen-Score
Require: Network F(·) with pre-GAP feature map f(·); α = 0.01.
Ensure: Zen-Score Zen(F).
1: Remove all residual links in F.
2: Initialize all neurons in F by N(0, 1).
3: Sample x, ϵ ∼N(0, 1).
4: Compute ∆≜Ex,ϵ∥f(x) −f(x + αϵ)∥F
.
5: For the i-th BN layer with m output channels, compute ¯σi =
qP
j σ2
i,j/m where σi,j is the mini-batch
standard deviation statistic of the j-th channel in BN.
6: Zen(F) ≜log(∆) + P
i log(¯σi).
In the above subsection, we showed that BN layer is necessary to prevent numerical overﬂow in com-
puting Φ-score but comes with the side-effect of re-scaling. In this subsection, we design a new Zen-Score
which is able to calibrate re-scaling when BN layer is present. The computation of Zen-Score is described
in Algorithm 1. Figure 3 visualizes the computational graph of Algorithm 1.
In Algorithm 1, all residual links are removed from the network as pre-processing. Then we randomly
sample input vectors and perturb them with Gaussian noise. The perturbation of the pre-GAP feature map
is denoted as ∆in Line 4. This step replaces the gradient of x with ﬁnite differential ∆to avoid backward-
propagation. To get Zen-Score, the scaling factor ¯σ2
i is averaged from the variance of each channel in BN
layer. Finally, the Zen-Score is computed by the log-sum of ∆and ¯σi. The following theorem guarantees
that the Zen-Score of network with BN layers approximates the Φ-score of the same network without BN
layers. The proof is postponed to Supplementary H.
7
Conv
RELU
BatchNorm
pre-GAP feature map
computation steps of  Zen-score
Figure 3: Zen-Score computational graph. x0 is one mini-batch of input images. For each BN layer, we
extract its mini-batch deviation parameter σi. ∆x0{f(x0)} is the differential of pre-GAP feature map f(x0)
with respect to x0.
Theorem 1. Let ¯f(x0) = ¯xL be an L-layer vanilla network without BN layers. f(x0) = xL is its sister
network with BN layers. For some constants 0 < δ < 1, K0 ≤O[
p
log(1/δ)], when BHW ≥O[(LK0)2]
is large enough, with probability at least 1 −δ, we have
(1 −Lϵ)2 ≤(QL
t=1 ¯σ2
t )Eθ{∥xL∥2}
Eθ∥¯xL∥2
≤(1 + Lϵ)2
(4)
where ϵ ≜O(2K0/
√
BHW).
Informally speaking, Theorem 1 says that to compute ∥¯f(·)∥, we only need to compute ∥f(·)∥then re-
scale with QL
t=1 ¯σt. The approximation error is bounded by Lϵ. By taking gradient of x on both ¯f(·) and
f(·), we obtain the desired relationship between Zen-Score and Φ-score.
4.3
Zen-NAS For Maximizing Expressivity
We design Zen-NAS algorithm to maximize the Zen-Score of the target network. The step-by-step
description of Zen-NAS is given in Algorithm 2. The Zen-NAS uses Evolutionary Algorithm (EA) as ar-
chitecture generator. It is possible to choose other generators such as Reinforced Learning or even greedy
selection. The choice of EA is due to its simplicity.
In Algorithm 2, we randomly generate N structures. At each iteration step t, we randomly select a
structure in the population P and mutate it. The mutation algorithm is presented in Algorithm 3. The width
and depth of the selected layer is mutated in a given range. We choose [0.5, 2.0] as the mutation range in this
work, that is, within half or double of the current value. The new structure ˆFt is appended to the population
if its inference cost does not exceed the budget. The maximal depth of networks is controlled by L, which
prevents the algorithm generate over-deep structures. Finally, we maintain the population size by removing
networks with the smallest Zen-Scores. After T iterations, the network with the largest Zen-Score is returned
as the output of Zen-NAS. We name the found architectures as ZenNets.
8
Algorithm 2 Zen-NAS
Require: Search space S, inference budget B, maximal depth L, total number of iterations T, evolutionary
population size N, initial structure F0.
Ensure: NAS-designed ZenNet F ∗.
1: Initialize population P = {F0}.
2: for t = 1, 2, · · · , T do
3:
Randomly select Ft ∈P.
4:
Mutate ˆFt = MUTATE(Ft, S)
5:
if ˆFt exceeds inference budget or has more than L layers then
6:
Do nothing.
7:
else
8:
Get Zen-Score z = Zen( ˆFt).
9:
Append ˆFt to P.
10:
end if
11:
Remove network of the smallest Zen-Score if the size of P exceeds B.
12: end for
13: Return F ∗, the network of the highest Zen-Score in P.
Algorithm 3 MUTATE
Require: Structure Ft, search space S.
Ensure: Randomly mutated structure ˆFt.
1: Uniformly select a block h in Ft.
2: Uniformly alternate the block type, kernel size, width and depth of h within some range.
3: Return the mutated structure ˆFt.
5
Experiments
In this section, experiments on CIFAR-10/CIFAR-100 [20] and ImageNet-1k [12] are conducted to validate
the superiority of Zen-NAS. We ﬁrst compare Zen-Score to several zero-shot proxies on CIFAR-10 and
CIFAR-100, using the same search space, search policy and training settings. Then we compare Zen-NAS
to the state-of-the-art methods on ImageNet. Zen-NAS on CIFAR-10/CIFAR-100 can be found in Supple-
mentary D. Finally, we compare the searching cost of Zen-NAS with SOTA methods in subsection 5.3.
Due to space limitation, the inference speed on NVIDIA T4 and Google Pixel2 is reported in Supplemen-
tary C. The Zen-Scores of ResNets and accuracies under fair training settings are reported in Supplementary
E. We enclose one big performance table of networks on ImageNet in Supplementary I.
To align with previous works, we consider the following two search spaces:
• Search Space I Following [15, 40], this search space consists of residual blocks and bottleneck blocks
deﬁned in ResNet.
• Search Space II Following [45, 38], this search space consists of MobileNet blocks. The depth-wise
expansion ratio is searched in set {1, 2, 4, 6}.
Please see Supplementary A for datasets description and detail experiment settings.
In each trial, the initial structure is a randomly selected small network which is guaranteed to satisfy the
inference budget. The kernel size is searched in set {3, 5, 7}. Following conventional designs, the number
of stages is three for CIFAR-10/CIFAR-100 and ﬁve for ImageNet. The evolutionary population size is 256,
number of evolutionary iterations T = 96, 000. The resolution is 32x32 for CIFAR-10/CIFAR-100 and
9
proxy
CIFAR-10
CIFAR-100
Zen-Score
96.2%
80.1%
FLOPs
93.1%
64.7%
grad
92.8%
65.4%
synﬂow
95.1%
75.9%
TE-Score
96.1%
77.2%
NASWOT
96.0%
77.5%
Random
93.5±0.7%
71.1±3.1%
Table 1: Top-1 accuracies on CIFAR-10/CIFAR-100 for ﬁve zero-shot proxies. Budget: model size N ≤
1 M. ‘Random’: average accuracy ± std for random search.
proxy
model
N
time
speed-up
TE-Score
ResNet-18
16
0.34
1/28x
ResNet-50
16
0.77
1/20x
NASWOT†
ResNet-18
16
0.040
1/3.3x
ResNet-50
16
0.059
1/1.6x
Zen-Score
ResNet-18
16
0.012
1.0
ResNet-50
16
0.037
1.0
Table 2: Time cost (in seconds) of computing Zen/TE-Score for ResNet-18/50 at resolution 224x224. The
statistical error is within 5%. ‘time’: time for computing Zen/TE-score for N images, measured in seconds,
averaged over 100 trials. ‘speed-up’: speed-up rate of TE-Score v.s. Zen-Score.
†: The ofﬁcial implementation outputs Inf score for ResNet-18/50.
224x224 for ImageNet.
5.1
Zen-Score v.s. Other Zero-Shot Proxies
Following [1, 7], we compare Zen-Score to ﬁve zero-shot proxies: FLOPs, gradient-norm (grad) of network
parameters, synﬂow [51], TE-NAS score (TE-Score) [7] and NASWOT [33]. For each proxy, we replace
Zen-Score by that proxy in Algorithm 2 and then run Algorithm 2 for T = 96, 000 iterations to ensure
convergence. Since synﬂow is the smaller the better, we use its negative value in Algorithm 2. Following
convention, we search for best network on CIFAR-10/CIFAR-100 within model size N ≤1 M. The conver-
gence curves are plotted in Supplementary C. In these ﬁgures, all six scores improves monotonically along
iterations.
After the above NAS step, we train the network of the best score for each proxy under the same training
setting. To provide a random baseline, we randomly generate networks. The width of the layer varies in
10
0.5
1.0
1.5
2.0
FLOPs
×109
70.0
72.5
75.0
77.5
80.0
Top-1 Accuracy (%)
44% Reduction
RegNet
EﬃcientNet
OFANet
MobileNet
MnasNet
DNANet
DFNet
ZenNet
Figure 4: ZenNets optimized for FLOPs.
range [4, 512], and the depth of each stage varies in range [1, 10]. If the network size is larger than 1 M, we
shrink its width by factor 0.75 each time until it satisﬁes the budget. 32 random networks are generated and
trained in total.
The top-1 accuracy is reported in Table 1. Zen-Score signiﬁcantly outperforms the other ﬁve proxies on
both CIFAR-10 and CIFAR-100. TE-Score and NASWOT are the runner-up proxies with similar perfor-
mance, followed by synﬂow. It is not surprise to see that naive proxies, such as FLOPs and gradient-norm,
perform poorly, even worse than random search.
To compare the computational efﬁciency of Zen-Score and TE-score, we compute two scores for ResNet-
18 and ResNet-50 at 224x224 resolution. The expected time cost is averaged over 100 trials. We ﬁnd that
averaging Zen/TE-Score over N = 16 random images is sufﬁcient to reduce the statistical error below 5%.
The results are reported in Table 2. The computation of Zen-Score is 20 ∼28 times faster than TE-Score.
We tried our best to benchmark NASWOT for ResNet-18/50 using the ofﬁcial code. However, the ofﬁcial
code always outputs Inf for ResNet-18/50 at resolution 224. Despite of the Inf issue, Zen-Score is 3.3x times
faster than NASWOT on ResNet-18 and 1.6x times faster on ResNet-50.
11
NAS
Method
Top-1 (%)
GPU Day
AmoebaNet-A [41]
EA
74.5
3150†
EcoNAS [69]
EA
74.8
8
CARS-I [62]
EA
75.2
0.4
GeNet [57]
EA
72.1
17
DARTS [26]
GD
73.1
4
SNAS [59]
GD
72.7
1.5
PC-DARTS [61]
GD
75.8
3.8
ProxylessNAS [6]
GD
75.1
8.3
GDAS [66]
GD
74
0.8
FBNetV2-L1 [54]
GD
77.2
25
NASNet-A [70]
RL
74
1800
Mnasnet-A [49]
RL
75.2
-
MetaQNN [3]
RL
77.4
96
PNAS [25]
SMBO
74.2
224
SemiNAS [29]
SSL
76.5
4
TE-NAS [7]
ZS
74.1
0.2
OFANet [5]
PS
80.1
51.6
EfﬁcientNet-B7 [50]
Scaling
84.4
3800‡
Zen-NAS
ZS
83.6
0.5
Table 3: NAS searching cost comparison. ’Top-1’: top-1 accuracy on ImageNet-1k. ’Method’: ’EA’ is short
for Evolutionary Algorithm; ’GD’ is short for Gradient Descent; ’RL’ is short for reinforcement Learning;
’ZS’ is short for Zero-shot; ’SMBO’, ’SSL’, ’PS’ and ’Scaling’ are special searching methods/frameworks.
†: Running on TPU; ‡: The cost is estimated by [54];
5.2
Zen-NAS on ImageNet
We use Zen-NAS to search efﬁcient network (ZenNet) on ImageNet. We consider the following popular net-
works as baselines: (a) manually-designed networks, including ResNet [15], DenseNet [17], ResNeSt [64],
MobileNet-V2 [45] (b) NAS-designed networks for fast inference on GPU, including OFANet-9ms/11ms
[5], DFNet [22], RegNet [40]; (c) NAS-designed networks optimized for FLOPs, including OFANet-389M/482M/595M
[5], DNANet [21], EfﬁcientNet [50], Mnasnet [49].
Among these networks, EfﬁcientNet is a popular baseline in NAS-related works. EfﬁcientNet-B0/B1
are suitable for mobile device for their small FLOPs and model size. EfﬁcientNet-B3∼B7 are large models
that are best to be deployed on a high-end GPU. Although EfﬁcientNet is optimized for FLOPs, its inference
speed on GPU is within top-tier ones. Many previous works compare to EfﬁcientNet by inference speed on
GPU [64, 5, 40].
Searching Low Latency Networks
Following previous works [5, 22, 40], we use Zen-NAS to optimize
network inference speed on NVIDIA V100 GPU. We use Search Space I in this experiment. The inference
speed is tested at batch size 64, half precision (ﬂoat16). We search for networks of inference latency within
0.1/0.2/0.3/0.5/0.8/1.2 milliseconds (ms) per image. For testing inference latency, we set batch-size=64
and do mini-batch inference 30 times. The averaged inference latency is recorded. The top-1 accuracy on
12
ImageNet v.s. inference latency is plotted in Figure 1. Clearly, ZenNets outperform baseline models in both
accuracy and inference speed by a large margin. The largest model ZenNet-1.2ms achieves 83.6% top-1
accuracy which is between EfﬁcientNet-B5 and B6. It is about 4.9x faster than EfﬁcientNet at the same
accuracy level.
Searching Lightweight Networks
Following previous works [5, 50], we use Zen-NAS to search lightweight
networks with small FLOPs. We use Search Space II in this experiment. We search for networks of com-
putational cost within 400/600/900 M FLOPs. Similar to OFANet and EfﬁcientNet, we add SE-blocks after
convolutional layers. The top-1 accuracy v.s. FLOPs is plotted in Figure 4. Again, ZenNets outperform
most models by a large margin. ZenNet-900M-SE achieves 80.8% top-1 accuracy which is comparable to
EfﬁcientNet-B3 with 43% fewer FLOPs. The runner-up is OFANet whose efﬁciency is similar to ZenNet.
5.3
Searching Cost of Zen-NAS v.s. SOTA
The major time cost of Zen-NAS is the computation of Zen-Score. The network latency is predicted by an
in-house latency predictor whose time cost is nearly zero. According to Table 2, the computation of Zen-
Score for ResNet-50 only takes 0.15 second. This means that scoring 96,000 networks similar to ResNet-50
only takes 4 GPU hours, or 0.17 GPU day.
We compare Zen-NAS searching cost to SOTA NAS methods in Table 3. Since every NAS method uses
different settings, it is difﬁcult to make a fair comparison that everyone agrees with. Nevertheless, we only
concern about the best model reported in each paper and the corresponding searching cost. This gives us a
rough impression of the efﬁciency of these methods and their practical ability of designing high-performance
models.
From Table 3, for conventional NAS methods, it takes hundreds to thousands GPU days to ﬁnd a good
structure of accuracy better than 78.0%. Many one-shot methods are very fast. For most one-shot methods,
the best accuracy is below 80%. In comparison, Zen-NAS achieves 83.6% top-1 accuracy within 0.5 GPU
day. Among methods achieving above 80.0% top-1 accuracy in Table 3, the searching speed of Zen-NAS
is nearly 100 times faster than OFANet and 7800 times faster than EfﬁcientNet. TE-NAS uses less GPU
day than Zen-NAS in Table 3. This does not conﬂict with Table 2 because the total number of networks
evaluated by the two methods are different.
6
Conclusion
We proposed Zen-NAS, a zero-shot neural architecture search framework for designing high performance
deep image recognition networks. Without optimizing network parameters, Zen-NAS ranks networks via
network expressivity which can be numerically measured by Zen-Score. The searching speed of Zen-NAS
is dramatically faster than previous SOTA methods. The ZenNets automatically designed by Zen-NAS are
signiﬁcantly more efﬁcient in terms of inference latency, FLOPs and model size, in multiple recognition
tasks. We wish the elegance of Zen-NAS will inspire more theoretical researches towards a deeper under-
standing of efﬁcient network design.
References
[1] Mohamed S. Abdelfattah, Abhinav Mehrotra, Łukasz Dudziak, and Nicholas D. Lane. Zero-Cost Proxies for
Lightweight NAS. In ICLR, 2021. 3, 4, 6, 10
13
[2] Gustavo Aguilar, Yuan Ling, Yu Zhang, Benjamin Yao, Xing Fan, and Chenlei Guo. Knowledge Distillation from
Internal Representations. In AAAI, 2020. 18
[3] Bowen Baker, Otkrist Gupta, Nikhil Naik, and Ramesh Raskar. Designing Neural Network Architectures using
Reinforcement Learning. In ICLR, 2017. 2, 3, 12
[4] Peter L. Bartlett, Dylan J. Foster, and Matus J. Telgarsky. Spectrally-normalized margin bounds for neural net-
works. In NIPS, 2017. 3, 6
[5] Han Cai, Chuang Gan, Tianzhe Wang, Zhekai Zhang, and Song Han. Once-for-All: Train One Network and
Specialize it for Efﬁcient Deployment on Diverse Hardware Platforms. In ICLR, 2020. 2, 4, 12, 13, 18
[6] Han Cai, Ligeng Zhu, and Song Han. ProxylessNAS: Direct Neural Architecture Search on Target Task and
Hardware. In ICLR, 2019. 2, 4, 12, 18
[7] Wuyang Chen, Xinyu Gong, and Zhangyang Wang. Neural architecture search on imagenet in four gpu hours: A
theoretically inspired perspective. In ICLR, 2021. 3, 4, 6, 10, 12, 26
[8] Xin Chen, Lingxi Xie, Jun Wu, and Qi Tian. Progressive DARTS: Bridging the Optimization Gap for NAS in the
Wild. In ICCV, 2019. 18
[9] Nadav Cohen and Amnon Shashua. Inductive Bias of Deep Convolutional Networks through Pooling Geometry.
In ICLR, 2017. 3
[10] Ekin D. Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, and Quoc V. Le.
AutoAugment: Learning
Augmentation Policies from Data. In CVPR, 2019. 18
[11] Amit Daniely, Roy Frostig, and Yoram Singer. Toward Deeper Understanding of Neural Networks: The Power of
Initialization and a Dual View on Expressivity. In NIPS, 2016. 3
[12] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. ImageNet: A large-scale hierarchical image
database. In CVPR, 2009. 3, 9
[13] Zichao Guo, Xiangyu Zhang, Haoyuan Mu, Wen Heng, Zechun Liu, Yichen Wei, and Jian Sun. Single Path
One-Shot Neural Architecture Search with Uniform Sampling. In ECCV, 2020. 2, 4
[14] Boris Hanin and David Rolnick. Complexity of Linear Regions in Deep Networks. In ICML, 2019. 3, 5
[15] K. He, X. Zhang, S. Ren, and J. Sun. Deep Residual Learning for Image Recognition. In CVPR, 2016. 9, 12, 20,
21
[16] Jie Hu, Li Shen, Samuel Albanie, Gang Sun, and Enhua Wu. Squeeze-and-Excitation Networks. In CVPR, 2018.
5
[17] Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kilian Q. Weinberger. Densely Connected Convolutional
Networks. In CVPR, 2017. 12
[18] Sham M. Kakade, Karthik Sridharan, and Ambuj Tewari. On the Complexity of Linear Prediction: Risk Bounds,
Margin Bounds, and Regularization. In NIPS, 2008. 5
[19] Vladimir Koltchinskii. Oracle Inequalities in Empirical Risk Minimization and Sparse Recovery Problems, volume
2033. Springer Science & Business Media, 2011. 3
[20] Alex Krizhevsky. Learning multiple layers of features from tiny images, 2009. 3, 9
[21] Changlin Li, Jiefeng Peng, Liuchun Yuan, Guangrun Wang, Xiaodan Liang, Liang Lin, and Xiaojun Chang. Block-
wisely Supervised Neural Architecture Search with Knowledge Distillation. In CVPR, 2020. 4, 12, 18
[22] Xin Li, Yiming Zhou, Zheng Pan, and Jiashi Feng. Partial Order Pruning: For Best Speed/Accuracy Trade-off in
Neural Architecture Search. In CVPR, 2019. 12
[23] Shiyu Liang and R. Srikant. Why Deep Neural Networks for Function Approximation? In ICLR, 2016. 3
[24] Chenxi Liu, Piotr Doll´ar, Kaiming He, Ross Girshick, Alan Yuille, and Saining Xie. Are Labels Necessary for
Neural Architecture Search? In ECCV, 2020. 4
14
[25] Chenxi Liu, Barret Zoph, Maxim Neumann, Jonathon Shlens, Wei Hua, Li-Jia Li, Li Fei-Fei, Li Fei-Fei, Alan L.
Yuille, Jonathan Huang, and Kevin Murphy. Progressive Neural Architecture Search. In ECCV, 2018. 3, 12, 18
[26] Hanxiao Liu, Karen Simonyan, and Yiming Yang. DARTS: Differentiable Architecture Search. In ICLR, 2019. 2,
4, 12, 18
[27] Ilya Loshchilov and Frank Hutter. SGDR: Stochastic Gradient Descent with Warm Restarts. In ICLR, 2017. 18
[28] Zhou Lu, Hongming Pu, Feicheng Wang, Zhiqiang Hu, and Liwei Wang. The Expressive Power of Neural Net-
works: A View from the Width. In NIPS, 2017. 3
[29] Renqian Luo, Xu Tan, Rui Wang, Tao Qin, Enhong Chen, and Tie-Yan Liu. Semi-Supervised Neural Architecture
Search. In NIPS, 2020. 2, 3, 12
[30] Renqian Luo, Fei Tian, Tao Qin, Enhong Chen, and Tie-Yan Liu. Neural Architecture Optimization. In NIPS,
2018. 2, 3
[31] Maithra Raghu, Ben Poole, Jon Kleinberg, Surya Ganguli, and Jascha Sohl-Dickstein. On the Expressive Power
of Deep Neural Networks. In ICML, 2017. 3, 5
[32] Joseph Mellor, Jack Turner, Amos Storkey, and Elliot J. Crowley. Neural Architecture Search without Training.
arXiv:2006.04647 [cs, stat], 2021. 3
[33] Joseph Mellor, Jack Turner, Amos Storkey, and Elliot J. Crowley. Neural Architecture Search without Training. In
ICML, 2021. 4, 10
[34] Guido Mont´ufar, Razvan Pascanu, Kyunghyun Cho, and Yoshua Bengio. On the Number of Linear Regions of
Deep Neural Networks. In NIPS, 2014. 3, 5
[35] Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, and Nathan Srebro.
The role of over-
parametrization in generalization of neural networks. In ICML, 2018. 3, 6
[36] Thao Nguyen, Maithra Raghu, and Simon Kornblith. Do Wide and Deep Networks Learn the Same Things?
Uncovering How Neural Network Representations Vary with Width and Depth. In ICLR, 2021. 3
[37] Hieu Pham, Zihang Dai, Qizhe Xie, Minh-Thang Luong, and Quoc V. Le. Meta Pseudo Labels. arXiv:2003.10580
[cs, stat], 2021. 3
[38] Hieu Pham, Melody Guan, Barret Zoph, Quoc Le, and Jeff Dean. Efﬁcient Neural Architecture Search via Param-
eters Sharing. In ICML, 2018. 9, 18
[39] Ben Poole, Subhaneil Lahiri, Maithra Raghu, Jascha Sohl-Dickstein, and Surya Ganguli. Exponential expressivity
in deep neural networks through transient chaos. In NIPS, 2016. 3, 5
[40] Ilija Radosavovic, Raj Prateek Kosaraju, Ross Girshick, Kaiming He, and Piotr Doll´ar. Designing Network Design
Spaces. In CVPR, 2020. 9, 12
[41] Esteban Real, Alok Aggarwal, Yanping Huang, and Quoc V. Le. Regularized Evolution for Image Classiﬁer
Architecture Search. In AAAI, 2019. 2, 3, 12, 18
[42] Esteban Real, Sherry Moore, Andrew Selle, Saurabh Saxena, Yutaka Leon Suematsu, Quoc V. Le, and Alex
Kurakin. Large-Scale Evolution of Image Classiﬁers. In ICML, 2017. 2
[43] Pengzhen Ren, Yun Xiao, Xiaojun Chang, Po-Yao Huang, Zhihui Li, Xiaojiang Chen, and Xin Wang. A Compre-
hensive Survey of Neural Architecture Search: Challenges and Solutions, 2020. 3
[44] David Rolnick and Max Tegmark. The power of deeper networks for expressing natural functions. In ICLR, 2018.
3
[45] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-Chieh Chen. MobileNetV2: In-
verted Residuals and Linear Bottlenecks. In CVPR, 2018. 9, 12
[46] Christian Sciuto, Kaicheng Yu, Martin Jaggi, Claudiu Musat, and Mathieu Salzmann. Evaluating the Search Phase
of Neural Architecture Search. arXiv:1902.08142 [cs, stat], 2019. 2
15
[47] Thiago Serra, Christian Tjandraatmadja, and Srikumar Ramalingam. Bounding and Counting Linear Regions of
Deep Neural Networks. In ICML, 2018. 3, 5
[48] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna.
Rethinking the
Inception Architecture for Computer Vision. In CVPR, 2016. 18
[49] Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan, and Quoc V. Le. MnasNet: Platform-Aware Neural
Architecture Search for Mobile. In CVPR, 2019. 3, 12
[50] Mingxing Tan and Quoc Le. EfﬁcientNet: Rethinking Model Scaling for Convolutional Neural Networks. In
ICML, 2019. 4, 12, 13
[51] Hidenori Tanaka, Daniel Kunin, Daniel L. K. Yamins, and Surya Ganguli. Pruning neural networks without any
data by iteratively conserving synaptic ﬂow. In NIPS, 2020. 4, 10
[52] Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, and Herv´e J´egou. Train-
ing data-efﬁcient image transformers & distillation through attention. arXiv:2012.12877 [cs], 2021. 3
[53] Roman Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge
Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2018. 29
[54] Alvin Wan, Xiaoliang Dai, Peizhao Zhang, Zijian He, Yuandong Tian, Saining Xie, Bichen Wu, Matthew Yu, Tao
Xu, Kan Chen, Peter Vajda, and Joseph E. Gonzalez. FBNetV2: Differentiable Neural Architecture Search for
Spatial and Channel Dimensions. In CVPR, 2020. 2, 4, 12
[55] Chaoqi Wang, Guodong Zhang, and Roger Grosse. Picking Winning Tickets Before Training by Preserving Gra-
dient Flow. In ICLR, 2019. 6
[56] Wei Wen, Hanxiao Liu, Hai Li, Yiran Chen, Gabriel Bender, and Pieter-Jan Kindermans. Neural Predictor for
Neural Architecture Search. In ECCV, 2020. 2
[57] Lingxi Xie and Alan Yuille. Genetic CNN. In ICCV, 2017. 2, 3, 12
[58] Saining Xie, Alexander Kirillov, Ross Girshick, and Kaiming He. Exploring Randomly Wired Neural Networks
for Image Recognition. arXiv:1904.01569 [cs], 2019. 4
[59] Sirui Xie, Hehui Zheng, Chunxiao Liu, and Liang Lin. SNAS: Stochastic neural architecture search. In ICLR,
2018. 2, 4, 12, 18
[60] H. Xiong, L. Huang, M. Yu, L. Liu, F. Zhu, and L. Shao. On the Number of Linear Regions of Convolutional
Neural Networks. In ICML, 2020. 3, 5
[61] Yuhui Xu, Lingxi Xie, Xiaopeng Zhang, Xin Chen, Guo-Jun Qi, Qi Tian, and Hongkai Xiong. PC-DARTS: Partial
Channel Connections for Memory-Efﬁcient Architecture Search. In ICLR, 2019. 2, 4, 12
[62] Zhaohui Yang, Yunhe Wang, Xinghao Chen, Boxin Shi, Chao Xu, Chunjing Xu, Qi Tian, and Chang Xu. CARS:
Continuous Evolution for Efﬁcient Neural Architecture Search. In CVPR, 2020. 2, 3, 12
[63] Chris Ying, Aaron Klein, Esteban Real, Eric Christiansen, Kevin Murphy, and Frank Hutter. NAS-Bench-101:
Towards Reproducible Neural Architecture Search. In ICML, 2019. 2
[64] Hang Zhang, Chongruo Wu, Zhongyue Zhang, Yi Zhu, Zhi Zhang, Haibin Lin, Yue Sun, Tong He, Jonas Mueller,
R. Manmatha, Mu Li, and Alexander Smola. ResNeSt: Split-Attention Networks, 2020. 12
[65] Hongyi Zhang, Moustapha Cisse, Yann N. Dauphin, and David Lopez-Paz.
Mixup: Beyond Empirical Risk
Minimization. In ICLR, 2018. 18
[66] Miao Zhang, Huiqi Li, Shirui Pan, Xiaojun Chang, and Steven Su. Overcoming Multi-Model Forgetting in One-
Shot NAS With Diversity Maximization. In CVPR, 2020. 2, 4, 12
[67] Xiao Zhang and Dongrui Wu. Empirical Studies on the Properties of Linear Regions in Deep Neural Networks. In
ICLR, 2019. 5
[68] Zhun Zhong, Liang Zheng, Guoliang Kang, Shaozi Li, and Yi Yang. Random Erasing Data Augmentation. In
AAAI, 2020. 18
16
[69] Dongzhan Zhou, Xinchi Zhou, Wenwei Zhang, Chen Change Loy, Shuai Yi, Xuesen Zhang, and Wanli Ouyang.
EcoNAS: Finding Proxies for Economical Neural Architecture Search. In CVPR, 2020. 2, 3, 12
[70] Barret Zoph, Vijay Vasudevan, Jonathon Shlens, and Quoc V. Le. Learning Transferable Architectures for Scalable
Image Recognition. In CVPR, 2018. 3, 12, 18
17
A
Datasets and Experiment Settings
Dataset CIFAR-10 has 50 thousand training images and 10 thousand testing images in 10 classes with
resolution 32x32. CIFAR-100 has the same number of training/testing images but in 100 classes. ImageNet-
1k has over 1.2 million training images and 50 thousand validation images in 1000 classes. We use the
ofﬁcial training/validation split in our experiments.
Augmentation We use the following augmentations as in [38]: mix-up [65], label-smoothing [48], random
erasing [68], random crop/resize/ﬂip/lighting and AutoAugment [10].
Optimizer For all experiments, we use SGD optimizer with momentum 0.9; weight decay 5e-4 for CIFAR-
10/100, 4e-5 for ImageNet; initial learning rate 0.1 with batch size 256; cosine learning rate decay [27].
We train models up to 1440 epochs in CIFAR-10/100, 480 epochs in ImageNet. Following previous works
[2, 21, 5], we use EfﬁcientNet-B3 as teacher networks when training ZenNets.
B
Implementation
Our code is implemented in PyTorch. The synﬂow implementation is available from https://github.
com/mohsaied/zero-cost-nas/blob/main/foresight/pruners/measures/synflow.
py. The ofﬁcial TE-NAS score implementation is available from https://github.com/VITA-Group/
TENAS/blob/main/lib/procedures. The ofﬁcial NASWOT implementation is available from https:
//github.com/BayesWatch/nas-without-training. Our searching and training code are re-
leased on https://github.com/idstcv/ZenNAS.
C
Additional Figures
We test the performance of ZenNets on devices other than NVIDIA V100 GPU. The two hardware platforms
are considered. NVIDIA T4 is an industrial level GPU optimized for INT8 inference. All networks are
exported to TensorRT engine at precision INT8 to benchmark their inference speed on T4. Google Pixel2 is
a modern cell phone with moderate powerful mobile GPU. In Figure 5 and Figure 6, we report the inference
speed of ZenNets on T4 and Pixel2 as well as several SOTA models. The best ZenNet-1.2ms is 10.9x times
faster than EfﬁcientNet on NVIDIA T4, 1.6x times faster on Pixel2.
The evolutionary processes of optimizing zero-shot proxies are plotted in Figure 7, 8, 9, 10, 11.
D
Zen-NAS on CIFAR
Following previous works, we use Zen-NAS to optimize model size on CIFAR-10 and CIFAR-100 datasets.
We use Search Space I in this experiment. We constrain the number of network parameters within {1.0 M,
2.0 M}. The resultant networks are labeled as ZenNet-1.0M/2.0M. Table 4 summarized our results. We com-
pare several popular NAS-designed models for CIFAR-10/CIFAR-100 in Figure 13, including AmoebaNet
[41], DARTS [26], P-DARTS [8], SNAS [59], NASNet-A [70], ENAS[38], PNAS [25], ProxylessNAS [6].
ZenNets outperform baseline methods by 30% ∼50% parameter reduction while achieving the same accu-
racies.
18
0.0
2.5
5.0
7.5
10.0
12.5
Inference Latency (ms)
70
75
80
Top-1 Accuracy (%)
10.9x speed-up
NVIDIA T4 TensorRT INT8
RegNet
ResNet
EﬃcientNet
OFANet
DenseNet
ResNeSt
MobileNet
MnasNet
DNANet
DFNet
ZenNet
Figure 5: ZenNets top-1 accuracy on ImageNet-1k v.s. inference latency (milliseconds per image) on
NVIDIA T4, TensorRT INT8, batch size 64. ZenNet-0.8ms∼1.2ms and ZenNet-400M-SE∼900M-SE are
plotted as two separated curves.
model
# params
FLOPs
C10
C100
ZenNet-1.0M
1.0 M
162 M
96.5%
80.1%
ZenNet-2.0M
2.0 M
487 M
97.5%
84.4%
Table 4: ZenNet-1.0M/2.0M on CIFAR-10 (C10) and CIFAR-100 (C100).
E
Zen-Scores and Accuracies of ResNets under Fair Training Setting
ResNets are widely used in computer vision. It is interesting to understand the ResNets via Zen-Score
analysis. We report the Zen-Scores of ResNets in Table 5. In Figure 14, we plot the Zen-Score against top-1
accuracy of ResNet and ZenNet on ImageNet. From the ﬁgure, it is clearly that even for the same model, the
training method matters a lot. There is considerable performance gain of ResNets after using our enhanced
training methods. The Zen-Scores positively correlate to the top-1 accuracies for both ResNet and ZenNets.
Next we show that the Zen-Scores is well-aligned with top-1 accuracies across different models. We
19
0
1000
2000
3000
4000
Inference Latency (ms)
70
75
80
Top-1 Accuracy (%)
1.6x speed-up
Google Pixel2
RegNet
ResNet
EﬃcientNet
OFANet
DenseNet
ResNeSt
MobileNet
MnasNet
DNANet
DFNet
ZenNet
Figure 6: ZenNets top-1 accuracy on ImageNet-1k v.s. inference latency (milliseconds per image) on Google
Pixel2, single image. ZenNet-0.8ms∼1.2ms and ZenNet-400M-SE∼900M-SE are plotted as two separated
curves.
Model
FLOPs
# Params
Zen-Score
ResNet-18
1.82G
11.7M
59.53
ResNet-34
3.67G
21.8M
112.32
ResNet-50
4.12G
25.5M
140.3
ResNet-101
7.85G
44.5M
287.87
ResNet-152
11.9G
60.2M
433.57
Table 5: Zen-Scores of ResNets.
consider two baselines in Table 6. The 2nd column reports the top-1 accuracies obtained in the ResNet
original paper [15]. We found that these models are under-trained. We use enhanced training methods to
train ResNets in the same way as we trained ZenNets. The corresponding top-1 accuracies are reported in
the 3rd column.
20
0
20000
40000
60000
80000
EA iteration
40
60
80
100
120
Zen-score
Zen
Figure 7: NAS process for maximizing Zen-Score. x-axis: number of evolutionary iterations. y-axis: Largest
Zen-Score in the current population.
Model
Top-1 [15]
Top-1 (ours)
ResNet-18
70.9%
72.1%
ResNet-34
74.4%
76.3%
ResNet-50
77.4%
79.0%
ResNet-101
78.3%
81.0%
ResNet-152
79.2%
82.3%
Table 6: Top-1 accuracies of ResNets. Reported by [15] and using enhanced training methods we used in
this paper.
F
Effectiveness of Zen-Score
We show that Zen-Score effectively indicates the model accuracy during the evolutionary search. In the
searching process of ZenNet-1.0M, we uniformly sample 16 structures from the evolutionary population.
These structures have different number of channels and layers. Then the sampled structures are trained
on CIFAR-10/CIFAR-100. The top-1 accuracy v.s. Zen-Score are plotted in Figure 15. The Zen-Scores
21
0
20000
40000
60000
80000
EA iteration
1
2
Flops
×108
FLOPs
Figure 8: NAS process for maximizing FLOPs. x-axis: number of evolutionary iterations. y-axis: Largest
FLOPs in the current population.
effectively indicates the network accuracies, especially in high-precision regimes.
G
FLOPs/Params/Latency of ZenNets in Table 1
proxy
params
FLOPs
latency
Zen-Score
1.0M
170M
0.15ms
FLOPs
1.0M
285M
0.07ms
grad
0.2M
41M
0.14ms
synﬂow
1.0M
104M
0.11ms
TE-Score
1.0M
118M
0.08ms
NASWOT
1.0M
304M
0.25ms
Random
1.0M
110 M
0.09ms
Latency is measured on NVIDIA V100 FP16 batch size 64. ‘grad’ cannot ﬁnd a model near params≈1M.
22
0
20000
40000
60000
80000
EA iteration
0
250
500
750
1000
grad-norm
grad-norm
Figure 9: NAS process for maximizing grad-norm. x-axis: number of evolutionary iterations. y-axis:
Largest grad-norm in the current population.
23
0
20000
40000
60000
80000
EA iteration
200
250
300
350
synﬂow
synﬂow
Figure 10: NAS process for maximizing synﬂow. x-axis: number of evolutionary iterations. y-axis: Smallest
synﬂow in the current population.
24
0
20000
40000
60000
80000
EA iteration
100
110
120
NASWOT
NASWOT
Figure 11: NAS process for maximizing NASWOT. x-axis: number of evolutionary iterations. y-axis:
Largest NASWOT score in the current population.
25
0
20000
40000
60000
80000
EA iteration
6392
6394
6396
6398
TE-NAS score
TE-NAS
Figure 12: NAS process for maximizing TE-NAS score. x-axis: number of evolutionary iterations. y-axis:
Largest TE-NAS score in the current population. The NTK score in TE-NAS is the smaller the better.
Therefore we use RN −NTK as TE-score in EA. This is slightly different from [7] where the rank of NTK
is used as score.
26
1
2
3
4
5
# params
×106
96.5
97.0
97.5
Top-1 Accuracy (%)
NASNet-A
AmoebaNet-B
PNAS
ENAS
DARTS
SNAS
ProxylessNAS
P-DARTS
ZenNet
(a) CIFAR-10
1
2
3
4
# params
×106
80.0
81.0
82.0
83.0
84.0
Top-1 Accuracy (%)
DART
P-DARTS
ENAS
ZenNet
(b) CIFAR-100
Figure 13: ZenNet accuracy v.s. model size (# params) on CIFAR-10 and CIFAR-100.
27
100
200
300
400
Zen-score
72
74
76
78
80
82
Top-1 Accuracy (%)
ResNet-18
ResNet-34
ResNet-50
ResNet-101
ResNet-152
ResNet-18
ResNet-34
ResNet-50
ResNet-101
ResNet-152
ZenNet-0.1ms
ZenNet-0.2ms
ZenNet-0.3ms
ResNet (He 2016)
ResNet (ours)
ZenNet
Figure 14: ResNet/ZenNet Zen-Score v.s. top-1 accuracy on ImageNet.
50
100
150
Zen-Score
80
90
Top-1 (%)
τ = 0.91
(a) CIFAR-10
50
100
150
Zen-Score
40
60
80
Top-1 (%)
τ = 0.88
(b) CIFAR-100
Figure 15: Zen-Score v.s. top-1 accuracy, 16 randomly sampled structures generated from ResNet-50, with
Kendall’s τ-score between accuracy and Zen-Score.
28
H
Proof of Theorem 1
We introduce a few more notations for our proof. Suppose the network has L convolutional layers. The t-th
layer has mt−1 input channels and mt output channels. The convolutional kernel is θt ∈Rmt×m−1t×k×k.
The image resolution is H × W. The mini-batch size is B. The output feature map of the t-th layer is xt.
We use x(i,b,h,w)
t
to denote the pixel of xt in the i-th channel, b-th image at cooridinate (h, w). N(µ, σ)
denotes Gaussian distribution with mean µ and variance σ2. For random variables z, a and a constant b, the
notation z = a ± b means |z −a| ≤b. To avoid notation clutter, we use C1/δ
log (·) to denote some logarithmic
polynomial in 1/δ and some other variables. Since the order of these variables in C1/δ
log (·) is logarithmic,
they do not alternate the polynomial order of our bounds.
The input image x0 are sampled from N(0, 1). In a vanilla network without BN layer, the feature map
¯xt is generated by the following forward inference process:
¯x0 =x0
¯xt = [θt ∗¯xt−1]+
where ∗is the convolutional operator, [z]+ = max(z, 0).
In Zen-Score computation, BN layer is inserted after every convolutional operator. The forward inference
now becomes:
gt =θt ∗xt−1
(5)
[σ(i)
t ]2 =
1
BHW
X
b,h,w
[g(i,b,h,w)
t
]2
(6)
¯σ2
t = 1
mt
mt
X
i=1
[σ(i)
t ]2
(7)
x(i)
t
=
"
g(i)
t
σ(i)
t
#
+
=
1
σ(i)
t
[g(i)
t ]+ .
(8)
Please note that in Eq. (8), we use a modiﬁed BN layer instead of the standard BN, where we do not subtract
mean value in the normalization step. This will greatly simply the proof. If the reader is concerned about
this, it is straightforward to replace all BN layers with our modiﬁed BN layers so that the computational
process exactly follows our proof. In practice, we did not observe noticable difference by switching between
two BN layers because the mean value of mini-batch is very close to zero.
To show that the Zen-Score computed on BN-enabled network f(x0) = xL approximates the Φ-score
computed on BN-free network ¯f(x0) = ¯xL, we only need to prove
(
L
Y
t=1
¯σt)2Eθ∥xL∥2 ≈Eθ∥¯xL∥2 .
(9)
In deed, when Eq. (9) holds true, by taking gradient w.r.t. x on both side, the proof is then completed. To
prove Eq. (9), we need the following theorems and lemmas.
H.1
Useful Theorems and Lemmas
The ﬁrst theorem is Bernstein’s inequality. It can be found in many statistical textbooks, such as [53, Theo-
rem 2.8.1].
29
Theorem 2 (Bernstein’s inequality). Let x1, x2, · · · , xN be independent bounded random variables of mean
zero, variance σ. |xi| ≤K for all i ∈{1, 2, · · · , N}. a = [a1, a2, · · · , aN] is a ﬁxed N-dimensional vector.
Then ∀t ≥0,
P(

N
X
i=1
aixi
 ≥t) ≤2 exp

−c min

t2
σ2∥a∥2
2
,
t
K∥a∥∞

.
A direct corollary gives the upper bound of sum of random variables.
Corollary 1. Under the same setting of Theorem 2, with probability at least 1 −δ,

N
X
i=1
aixi
 ≤C1/δ
log (·)σ∥a∥2 .
Proof. Let
δ ≜2 exp

−c min

t2
σ2∥a∥2
2
,
t
K∥a∥∞

= max

2 exp

−c
t2
σ2∥a∥2
2

, 2 exp

−c
t
K∥a∥∞

.
That is,
δ ≥2 exp

−c
t2
σ2∥a∥2
2

⇔t ≤
r
1
c log(2/δ)σ∥a∥2 = C1/δ
log (·)σ∥a∥2 ,
and
δ ≥2 exp

−c
t
K∥a∥∞

⇔t ≤1
c log(2/δ)K∥a∥∞= C1/δ
log (·)K∥a∥∞.
Therefore, with probability at least 1 −δ,

N
X
i=1
aixi
 ≤min{C1/δ
log (·)σ∥a∥2, C1/δ
log (·)K∥a∥∞}
≤C1/δ
log (·) min{σ∥a∥2, K∥a∥∞} .
That is,

N
X
i=1
aixi
 ≤C1/δ
log (·)σ∥a∥2 .
When the random variables are sampled from Gaussian distribution, it is more convenient to use the
following tighter bound.
30
Theorem 3. Let x1, x2, · · · , xN be sampled from N(0, σ), a ∈RN be a ﬁxed a vector. Then ∀t ≥0,
P(

N
X
i=1
aixi
 > t) ≤exp

−
t2
2σ2∥a∥2
2

.
Corollary 2. With probability at least 1 −δ,

N
X
i=1
aixi
 ≤
p
2 log(1/δ)σ∥a∥2 = C1/δ
log (·)σ∥a∥2 .
The proof is simple since the sum of Gaussian random variables is still Gaussian random variables.
The following two lemmas are critical in our lower bound analysis. The proof is straightforward once
using the symmetric property of random variable distribution.
Lemma 3. Suppose x ∈R is a mean zero, variance σ2 random variable with symmetric distribution. Then
E[x]2
+ = 4σ2/4.
Lemma 4. Suppose θi ∼N(0, 1). ∥x∥= ∥y∥are two ﬁxed vectors. Then
Eθ[
X
i
θixi]2
+ = 1
2Eθ[
X
i
θixi]2 = Eθ[
X
i
θiyi]2
+ .
H.2
Proof of Eq. (9)
Since x0 ∼N(0, 1), with probability at least 1 −δ, ∥x0∥∞≤C1/δ
log (·) ≜K0 for some constant K0. Now
suppose at layer t, ∥xt−1∥∞≤Kt−1. The following lemma shows that after convolution, ∥gt∥∞is also
bounded with high probability.
Lemma 5. Let θ(i,b,h,w) ∼N(0, 1), θt ∈Rmt×mt−1×k×k. For ﬁxed xt−1 ∈Rmt−1×B×H×W , gt ≜
θt ∗xt−1. Then with probability at least 1 −δ,
∥gt∥∞≤C1/δ
log (·)2k√mt−1Kt−1 .
Proof. Let us consider g(j,b,α,β)
t
, that is, the j-th channel, b-th image, at pixel (α, β). For any 1 ≤j ≤mt,
1 ≤α ≤H, 1 ≤β ≤W,
g(j,b,α,β)
t
=
m−1t
X
i=1
k−1
2
X
p=−k−1
2
k−1
2
X
q=−k−1
2
θ(j,i,p,q)
t
x(i,b,α+p,β+p)
t−1
Clearly,
Eθg(j,b,α,β)
t
= 0 .
According to Corollary 2,
|g(j,b,α,β)
t
| ≤C1/δ
log (·)C1/δ
log (·)Kt−1
√mt−1k
≤C1/δ
log (·)2k√mt−1Kt−1 .
31
The variance of gt is bounded with high probability too.
Lemma 6. With probability at least 1 −δ,
E[g(j,b,α,β)
t
]2 =σ∗
t ± C1/δ
log (·)k√mt−1Kt−1
σ∗2
t
≜1
4mt−1k2 .
Proof. By deﬁnition,
g(j,b,α,β)
t
=
m−1t
X
i=1
k−1
2
X
p=−k−1
2
k−1
2
X
q=−k−1
2
θ(j,i,p,q)
t
x(i,b,α+p,β+p)
t−1
Clearly, g(j,b,α,β)
t
is Gaussian random variable with zero-mean.
E[g(j,b,α,β)
t
]2 =
mt−1
X
i=1
k−1
2
X
p=−k−1
2
k−1
2
X
q=−k−1
2
[x(i,b,α+p,β+p)
t−1
]2 .
By Lemma 3,
E[x(i,b,α+p,β+p)
t−1
]2 =1
4 .
Therefore,
|E[g(j,b,α,β)
t
]2 −1
4mt−1k2|
≤C1/δ
log (·)k√mt−1Kt−1 .
Deﬁne σ∗2
t
≜1
4mt−1k2, the proof is completed.
Next we show that both σ(i)
t
and ¯σt concentrate around σ∗.
Lemma 7. With probability 1 −δ,
[σ(i)
t ]2 =(1 ± ϵt)[σ∗
t ]2
¯σt =(1 ±
ϵt
√mt
)[σ∗
t ]2
where
ϵt ≜4C1/δ
log (·)5
1
√
BHW
K2
t−1
Proof. Directly apply Corollary 1,
[σ(i)
t ]2 =E[g(j,b,α,β)
t
]2 ± C1/δ
log (·)
1
√
BHW
max{[g(j,b,α,β)
t
]2}
=E[g(j,b,α,β)
t
]2 ± C1/δ
log (·)
1
√
BHW
C1/δ
log (·)4mt−1k2K2
t−1
=[σ∗
t ]2 ±
1
√
BHW
C1/δ
log (·)5mt−1k2K2
t−1 .
32
Similary,
¯σ2
t =[σ∗
t ]2 ±
1
√mtBHW C1/δ
log (·)5mt−1k2K2
t−1 .
Deﬁne
ϵt ≜
1
[σ∗
t ]2
1
√
BHW
C1/δ
log (·)5mt−1k2K2
t−1
=
4
mt−1k2 C1/δ
log (·)5
1
√
BHW
mt−1k2K2
t−1
=4C1/δ
log (·)5
1
√
BHW
K2
t−1
Then we have
[σ(i)
t ]2 =(1 ± ϵt)[σ∗
t ]2
¯σt =(1 ±
ϵt
√mt
)[σ∗
t ]2
Next is our main lemma.
Lemma 8. Under the same setting of Lemma 7, with probability 1 −δ,
(σ∗
t )2∥xt∥2 =
1
1 ± ϵt
∥[gt]+ ∥2 .
Proof. By deﬁnition,
∥xt∥2 =
X
i
"
1
σ(i)
t
#2 h
g(i)
t
i2
+
=
X
i

1
(1 ± ϵt)σ∗
t
2 h
g(i)
t
i2
+
Then
(σ∗
t )2∥xt∥2
P
i
h
g(i)
t
i2
+
=
1
P
i
h
g(i)
t
i2
+
X
i
"
σ∗
t
σ(i)
t
#2 h
g(i)
t
i2
+
By Lemma 7, we have
1
1 + ϵt
≤σ∗
t
σ(i)
t
≤
1
1 −ϵt
33
Finally, we inductively bound |x(i,b,h,w)
t
|.
Lemma 9. With probability at least 1 −δ,
|x(i,b,h,w)
t
| ≤
C1/δ
log (·)2
p
(1 −ϵt)
Kt−1
Kt ≤C1/δ
log (·)2t
tY
j=1
(1 −ϵj)−1/2K0 .
Proof. By deﬁnition,
x(i,b,h,w)
t
=
1
σ(i)
t
[g(i,b,h,w)
t
]+
From Lemma 5,
[g(i,b,h,w)
t
]+ ≤C1/δ
log (·)2Kt−1
√mt−1k
From Lemma 7,
[σ(i)
t ]2 = (1 ± ϵt)[σ∗
t ]2
= 1
4(1 ± ϵt)mt−1k2
Then
|x(i,b,h,w)
t
| ≤
C1/δ
log (·)2Kt−1√mt−1k
q
1
4(1 ± ϵt)mt−1k2
≤
C1/δ
log (·)2Kt−1√mt−1k
q
1
4(1 −ϵt)mt−1k2
≤2
C1/δ
log (·)2Kt−1
p
(1 −ϵt)
→
C1/δ
log (·)2Kt−1
p
(1 −ϵt)
absorb 2 into C1/δ
log (·)
Therefore,
Kt ≜
C1/δ
log (·)2Kt−1
p
(1 −ϵt)
⇒Kt = C1/δ
log (·)2t
tY
j=1
(1 −ϵj)−1/2K0
34
Combining all above together, we are now ready to prove Eq. (9).
Denote z0 = 1. It is trivial to see that z0∥x0∥2 = z0∥¯xt∥2. By induction, suppose at layer t, we already
have zt−1∥xt−1∥2 = ∥¯xt−1∥2. Using Lemma 4,
Eθ∥¯xt∥2 =Eθ∥[θt ∗¯xt−1]+ ∥2
=Eθ∥[θt ∗zt−1xt−1]+ ∥2
=zt−1Eθ∥[θt ∗xt−1]+ ∥2
=zt−1Eθ∥[gt]+ ∥2
On the other hand, from Lemma 8,
¯σ2
t zt−1∥xt∥2 =zt−1
¯σ2
t
(σ∗
t )2 (σ∗
t )2∥xt∥2
=zt−1(1 ±
ϵt
√mt
)(σ∗
t )2∥xt∥2
Lemma [lem:sigma-i-concentration]
=zt−1(1 ±
ϵt
√mt
)
1
1 ± ϵt
∥[gt]+ ∥2 .
Therefore,
Eθ{¯σ2
t zt−1∥xt∥2} = (1 ±
ϵt
√mt
)
1
1 ± ϵt
Eθ∥¯xt∥2
By taking
zt ≜¯σ2
t zt−1/[(1 ±
ϵt
√mt
)
1
1 ± ϵt
] ,
we complete the induction of zt∥xt∥2 = ∥¯xt∥2 for all t.
Chaining t = {1, 2, · · · , L}, we get
Eθ{(
L
Y
t=1
¯σ2
t )∥xL∥2} =
L
Y
t=1

(1 ±
ϵt
√mt
)
1
1 ± ϵt

Eθ∥¯xL∥2 ,
where
ϵt ≜4C1/δ
log (·)5
1
√
BHW
K2
t−1
Kt ≜C1/δ
log (·)2t
tY
j=1
(1 −ϵj)−1/2K0 .
Finally, integrate everything together, we have proved that, with probability at least 1 −δ,
(
L
Y
t=1
¯σ2
t )Eθ{∥xL∥2} =
L
Y
t=1

(1 ±
ϵt
√mt
)
1
1 ± ϵt

Eθ∥¯xL∥2 .
35
That is,
L
Y
t=1

(1 −
ϵt
√mt
)
1
1 + ϵ

≤
(QL
t=1 ¯σ2
t )Eθ{∥xL∥2}
Eθ∥¯xL∥2
≤
L
Y
t=1

(1 +
ϵt
√mt
)
1
1 −ϵt

.
To further simply the above results, we consider the asymptotic case where BHW is large enough. Then
ϵt will be a small number. By ﬁrst order approximation of binomial expansion, (1 + ϵ)L ≈1 + Lϵ + O(ϵ2).
To see that ϵt is bounded by a small constant, we denote γt ≜maxj∈[1,t] ϵj. Then
Kt ≤O[(1 + t −1
2
γt−1)K0]
γt ≤O{
K0
√
BHW
[(1 + (t −1)
2
γt−1]} .
(10)
By the recursive equation Eq. (10), when γt−1 ≤
2
L−1,
γt ≤O{
K0
√
BHW
[(1 + (t −1)
2
γt−1]}
≤O{
2K0
√
BHW
} .
Therefore, by taking
2K0
√
BHW ≤2
L, that is BHW ≥O{L2K2
0}, we have
ϵ = max ϵt ≤O{
2K0
√
BHW
}
to be a small number.
When ϵ is a small number,
(QL
t=1 ¯σ2
t )Eθ{∥xL∥2}
Eθ∥¯xL∥2
≤
L
Y
t=1

(1 +
ϵt
√mt
)
1
1 −ϵt

≤(1 + ϵ)L(1 −ϵt)−L
≈(1 + Lϵ)2 .
Similarly,
(QL
t=1 ¯σ2
t )Eθ{∥xL∥2}
Eθ∥¯xL∥2
≥(1 −Lϵ)2 .
36
I
One Big Table of Networks on ImageNet
model
resolution
# params
FLOPs
Top-1 Acc
latency(ms)
V100
T4
Pixel2
RegNetY-200MF
224
3.2 M
200 M
70.4%
0.22
0.12
118.17
RegNetY-400MF
224
4.3 M
400 M
74.1%
0.44
0.17
181.09
RegNetY-600MF
224
6.1 M
600 M
75.5%
0.25
0.21
173.19
RegNetY-800MF
224
6.3 M
800 M
76.3%
0.31
0.22
202.66
ResNet-18
224
11.7 M
1.8 G
70.9%
0.13
0.06
158.70
ResNet-34
224
21.8 M
3.6 G
74.4%
0.22
0.11
280.44
ResNet-50
224
25.6 M
4.1 G
77.4%
0.40
0.20
502.43
ResNet-101
224
44.5 M
7.8 G
78.3%
0.66
0.32
937.11
ResNet-152
224
60.2 M
11.5 G
79.2%
0.94
0.46
1261.97
EfﬁcientNet-B0
224
5.3 M
390 M
76.3%
0.35
0.62
160.72
EfﬁcientNet-B1
240
7.8 M
700 M
78.8%
0.55
1.02
254.26
EfﬁcientNet-B2
260
9.2 M
1.0 G
79.8%
0.64
1.21
321.45
EfﬁcientNet-B3
300
12.0 M
1.8 G
81.1%
1.12
1.86
569.30
EfﬁcientNet-B4
380
19.0 M
4.2 G
82.6%
2.33
3.66
1252.79
EfﬁcientNet-B5
456
30.0 M
9.9 G
83.3%
4.49
6.99
2580.25
EfﬁcientNet-B6
528
43.0 M
19.0 G
84.0%
7.64
12.36
4287.81
EfﬁcientNet-B7
600
66.0 M
37.0 G
84.4%
13.73
†
8615.92
MobileNetV2-0.25
224
1.5 M
44 M
51.8%
0.08
0.04
16.71
MobileNetV2-0.5
224
2.0 M
108 M
64.4%
0.10
0.05
26.99
MobileNetV2-0.75
224
2.6 M
226 M
69.4%
0.15
0.08
49.78
MobileNetV2-1.0
224
3.5 M
320 M
72.0%
0.17
0.08
65.59
MobileNetV2-1.4
224
6.1 M
610 M
74.7%
0.24
0.12
110.70
MnasNet-1.0
224
4.4 M
330 M
74.2%
0.17
0.11
65.50
DNANet-a
224
4.2 M
348 M
77.1%
0.29
0.60
157.94
DNANet-b
224
4.9 M
406 M
77.5%
0.37
0.77
173.66
DNANet-c
224
5.3 M
466 M
77.8%
0.37
0.81
194.27
DNANet-d
224
6.4 M
611 M
78.4%
0.54
1.10
248.08
DFNet-1
224
8.5 M
746 M
69.8%
0.07
0.04
82.87
37
DFNet-2
224
18.0 M
1.8 G
73.9%
0.12
0.07
168.04
DFNet-2a
224
18.1 M
2.0 G
76.0%
0.19
0.09
223.20
OFANet-9ms
118
5.2 M
313 M
75.3%
0.14
0.13
82.69
OFANet-11ms
192
6.2 M
352 M
76.1%
0.17
0.19
94.17
OFANet-389M(+)
224
8.4 M
389 M
79.1%
0.26
0.49
116.34
OFANet-482M(+)
224
9.1 M
482 M
79.6%
0.33
0.57
142.76
OFANet-595M(+)
236
9.1 M
595 M
80.0%
0.41
0.61
150.83
OFANet-389M*
224
8.4 M
389 M
76.3%
0.26
0.49
116.34
OFANet-482M*
224
9.1 M
482 M
78.8%
0.33
0.57
142.76
OFANet-595M*
236
9.1 M
595 M
79.8%
0.41
0.61
150.83
DenseNet-121
224
8.0 M
2.9 G
74.7%
0.53
0.43
395.51
DenseNet-161
224
28.7 M
7.8 G
77.7%
1.06
0.50
991.61
DenseNet-169
224
14.1 M
3.4 G
76.0%
0.69
0.65
490.24
DenseNet-201
224
20.0 M
4.3 G
77.2%
0.89
1.10
642.98
ResNeSt-50
224
27.5 M
5.4 G
81.1%
0.76
‡
615.77
ResNeSt-101
224
48.3 M
10.2 G
82.3%
1.40
‡
1130.59
ZenNet-0.1ms
224
30.1 M
1.7 G
77.8%
0.10
0.08
181.7
ZenNet-0.2ms
224
49.7 M
3.4 G
80.8%
0.20
0.16
357.4
ZenNet-0.3ms
224
85.4 M
4.9 G
81.5%
0.30
0.26
517.0
ZenNet-0.5ms
224
118 M
8.3 G
82.7%
0.50
0.41
798.7
ZenNet-0.8ms
224
183 M
13.9 G
83.0%
0.80
0.57
1365.0
ZenNet-1.2ms
224
180 M
22.0 G
83.6%
1.20
0.85
2051.1
ZenNet-400M-SE
224
5.7 M
410 M
78.0%
0.248
0.39
87.9
ZenNet-600M-SE
224
7.1 M
611 M
79.1%
0.358
0.52
128.6
ZenNet-900M-SE
224
13.3 M
926 M
80.8%
0.55
0.55
215.68
Table 7: One big table of all networks referred in this work.
+: OFANet trained using supernet parameters as initialization.
∗: OFANet trained from scratch. We adopt this setting for fair compari-
son.
†: fail to run due to out of memory.
‡: ofﬁcial model implementation not supported by TensorRT.
38
J
Detail Structure of ZenNets
We list detail structure in Table 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18.
The ’block’ column is the block type. ’Conv’ is the standard convolution layer followed by BN and
RELU. ’Res’ is the residual block used in ResNet-18. ’Btn’ is the residual bottleneck block used in ResNet-
50. ’MB’ is the MobileBlock used in MobileNet and EfﬁcientNet. To be consistent with ’Btn’ block, each
’MB’ block is stacked by two MobileBlocks. That is, the kxk full convolutional layer in ’Btn’ block is
replaced by depth-wise convolution in ’MB’ block. ’kernel’ is the kernel size of kxk convolution layer
in each block. ’in’, ’out’ and ’bottleneck’ are numbers of input channels, output channels and bottleneck
channels respectively. ’stride’ is the stride of current block. ’# layers’ is the number of duplication of current
block type.
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
24
2
-
1
Res
3
24
32
2
64
1
Res
5
32
64
2
32
1
Res
5
64
168
2
96
1
Btn
5
168
320
1
120
1
Btn
5
320
640
2
304
3
Btn
5
640
512
1
384
1
Conv
1
512
2384
1
-
1
Table 8: ZenNet-0.1ms
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
24
2
-
1
Btn
5
24
32
2
32
1
Btn
7
32
104
2
64
1
Btn
5
104
512
2
160
1
Btn
5
512
344
1
192
1
Btn
5
344
688
2
320
4
Btn
5
688
680
1
304
3
Conv
1
680
2552
1
-
1
Table 9: ZenNet-0.2ms
39
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
24
2
-
1
Btn
5
24
64
2
32
1
Btn
3
64
128
2
128
1
Btn
7
128
432
2
128
1
Btn
5
432
272
1
160
1
Btn
5
272
848
2
384
4
Btn
5
848
848
1
320
3
Btn
5
848
456
1
320
3
Conv
1
456
6704
1
-
1
Table 10: ZenNet-0.3ms
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
8
2
-
1
Btn
7
8
64
2
32
1
Btn
3
64
152
2
128
1
Btn
5
152
640
2
192
4
Btn
5
640
640
1
192
2
Btn
5
640
1536
2
384
4
Btn
5
1536
816
1
384
3
Btn
5
816
816
1
384
3
Conv
1
816
5304
1
-
1
Table 11: ZenNet-0.5ms
40
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
16
2
-
1
Btn
5
16
64
2
64
1
Btn
3
64
240
2
128
2
Btn
7
240
640
2
160
3
Btn
7
640
768
1
192
4
Btn
5
768
1536
2
384
5
Btn
5
1536
1536
1
384
3
Btn
5
1536
2304
1
384
5
Conv
1
2304
4912
1
-
1
Table 12: ZenNet-0.8ms
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
32
2
-
1
Btn
5
32
80
2
32
1
Btn
7
80
432
2
128
5
Btn
7
432
640
2
192
3
Btn
7
640
1008
1
160
5
Btn
7
1008
976
1
160
4
Btn
5
976
2304
2
384
5
Btn
5
2304
2496
1
384
5
Conv
1
2496
3072
1
-
1
Table 13: ZenNet-1.2ms
41
block
kernel
in
out
stride
bottleneck
expansion
# layers
Conv
3
3
16
2
-
-
1
MB
7
16
40
2
40
1
1
MB
7
40
64
2
64
1
1
MB
7
64
96
2
96
4
5
MB
7
96
224
2
224
2
5
Conv
1
224
2048
1
-
-
1
Table 14: ZenNet-400M-SE
block
kernel
in
out
stride
bottleneck
expansion
# layers
Conv
3
3
24
2
-
-
1
MB
7
24
48
2
48
1
1
MB
7
48
72
2
72
2
1
MB
7
72
96
2
88
6
5
MB
7
96
192
2
168
4
5
Conv
1
192
2048
1
-
-
1
Table 15: ZenNet-600M-SE
block
kernel
in
out
stride
bottleneck
expansion
# layers
Conv
3
3
16
2
-
-
1
MB
7
16
48
2
72
1
1
MB
7
48
72
2
64
2
3
MB
7
72
152
2
144
2
3
MB
7
152
360
2
352
2
4
MB
7
360
288
1
264
4
3
Conv
1
288
2048
1
-
-
1
Table 16: ZenNet-900M-SE
42
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
88
1
-
1
Btn
7
88
120
1
16
1
Btn
7
120
192
2
16
3
Btn
5
192
224
1
24
4
Btn
5
224
96
2
24
2
Btn
3
96
168
2
40
3
Btn
3
168
112
1
48
3
Conv
1
112
512
1
-
1
Table 17: ZenNet-1.0M for CIFAR-10/CIFAR-100
block
kernel
in
out
stride
bottleneck
# layers
Conv
3
3
32
1
-
1
Btn
5
32
120
1
40
1
Btn
5
120
176
2
32
3
Btn
7
176
272
1
24
3
Btn
3
272
176
1
56
3
Btn
3
176
176
1
64
4
Btn
5
176
216
2
40
2
Btn
3
216
72
2
56
2
Conv
1
72
512
1
-
1
Table 18: ZenNet-2.0M for CIFAR-10/CIFAR-100
43
