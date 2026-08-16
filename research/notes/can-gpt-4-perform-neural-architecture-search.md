---
title: Can GPT-4 Perform Neural Architecture Search?
id: can-gpt-4-perform-neural-architecture-search
tags:
- llm-nas-feedback-positioning-7125b1
created: '2026-08-16T15:46:30.237432Z'
source: https://arxiv.org/html/2304.10970
source_domain: arxiv.org
fetched_at: '2026-08-16T15:46:30.236098Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

*Suggested by [[230410970-can-gpt-4-perform-neural-architecture-search]] — full-text HTML version of GENIUS abstract page fetched in batch*

Can GPT-4 Perform Neural Architecture Search?
Title:
Content selection saved. Describe the issue below:
Description:
arXiv is now an independent nonprofit!
Learn more
×
License: CC BY 4.0
arXiv:2304.10970v4 [cs.LG] 02 Aug 2023
Can GPT-4 Perform Neural Architecture Search?
Mingkai Zheng
Affiliation:
The University of Sydney  
SenseTime Research  
CAML Lab, University of Cambridge
mingkaizheng@outlook.com
,
xisu5992@uni.sydney.edu.au,{youshan,wangfei,qianchen}@sensetime.com
,
c.xu@sydney.edu.ausamuel.albanie.academic@gmail.com
Xiu Su
Shan You
Fei Wang
Chen Qian
Chang Xu
Samuel Albanie
Affiliation:
The University of Sydney  
SenseTime Research  
CAML Lab, University of Cambridge
mingkaizheng@outlook.com
,
xisu5992@uni.sydney.edu.au,{youshan,wangfei,qianchen}@sensetime.com
,
c.xu@sydney.edu.ausamuel.albanie.academic@gmail.com
Abstract
We investigate the potential of GPT-4
[
52
]
to perform Neural Architecture Search (NAS)—the task of designing effective neural architectures.
Our proposed approach,
G
PT-4
E
nhanced
N
eural arch
I
tect
U
re
S
earch (GENIUS), leverages the generative capabilities of GPT-4 as a black-box optimiser to quickly navigate the architecture search space, pinpoint promising candidates, and iteratively refine these candidates to improve performance.
We assess GENIUS across several benchmarks, comparing it with existing state-of-the-art NAS techniques to illustrate its effectiveness.
Rather than targeting state-of-the-art performance, our objective is to highlight GPT-4’s potential to assist research on a challenging technical problem through a simple prompting scheme that requires relatively limited domain expertise.
1
1
1
Code available at
https://github.com/mingkai-zheng/GENIUS
.
.
More broadly, we believe our preliminary results point to future research that harnesses general purpose language models for diverse optimisation tasks.
We also highlight important limitations to our study, and note implications for AI safety.
1
Introduction
Recent years have witnessed a string of high-profile scientific breakthroughs by applying deep neural networks to problems spanning domains such as protein folding
[
38
]
, exoplanet detection
[
59
]
and drug discovery
[
61
]
.
To date, however, successful applications of AI have been marked by the effective use of domain expertise to guide the design of the system, training data and development methodology.
The recent release of GPT-4 represents a milestone in the development of “general purpose” systems that exhibit a broad range of capabilities.
While the full extent of these capabilities remains unknown, preliminary studies and simulated human examinations indicate that the model’s knowledge spans many scientific domains
[
52
,
6
]
.
It is therefore of interest to consider the potential for GPT-4 to serve as a general-purpose research tool that substantially reduces the need for domain expertise prevalent in previous breakthroughs.
In this work, we investigate the feasibility of using
GPT-4
without domain-specific fine-tuning to assist with a research task that has received considerable attention in the machine learning community: deep neural network design.
Deep neural networks have proven effective on a diverse array of language and perception tasks, spanning domains such as question answering
[
56
]
, object recognition
[
16
,
40
]
and object detection
[
19
,
46
]
.
In the quest to improve performance, novel neural architecture designs, exemplified by proposals such as ResNets
[
23
]
and Transformers
[
71
]
, have attained substantial gains in performance.
Consequently, there has been significant interest in developing techniques that yield further improvements to neural network architectures.
In particular,
Neural Architecture Search
(
NAS
)
[
84
]
—which seeks to automate the identification of optimal network configurations for specific tasks—has developed into an active area of research.
The starting point for this work was a pilot exploration that sought to assess whether GPT-4 possessed knowledge relevant for our target task, focusing specifically on the design of Convolution Neural Networks (CNNs).
We began by simply prompting GPT-4
2
2
2
ChatGPT Mar 23 Version.
:
“What are the design principles for a high-performance CNN model? Can you provide some examples based on your knowledge?"
GPT-4 responded as follows:
(1) Depth
: Deeper networks can learn complex features and patterns. Increasing depth by adding more convolutional layers can improve performance while controlling overfitting.
(2) Width
: Increasing the number of filters in convolutional layers can help capture more diverse and complex features. Striking a balance between width and computational cost is crucial.
(3) Skip connections
: Skip connections allow gradients to flow through the network more easily, mitigating the vanishing gradient problem and enabling the training of deeper networks.
(4) Efficient computation
: Techniques like depthwise separable convolutions or group convolutions can reduce the number of parameters and computational costs without sacrificing performance.
(5) Normalization
: Normalization methods like batch normalization, layer normalization, or instance normalization can improve convergence and stability.
While the response to our rudimentary prompt lacks fine-grained specificity, it nevertheless suggests that GPT-4 possesses knowledge relevant to the target task.
A natural next question then arises: does GPT-4 simply have “surface level” awareness of information related to this task, or does it have the depth of knowledge required to play a substantially greater role in the design and engineering of neural network architectures?
Our investigation seeks to address this question by examining the degree to which GPT-4 can propose effective neural network architecture designs. We view our work as a tentative exploration of the potential of GPT-4 to assist with scientific discovery, providing suggestions that enable rapid research prototyping on a challenging optimisation task.
Further, we suggest that evidence of GPT-4’s ability to search neural network architecture design spaces with limited input from human domain experts has implications for AI safety.
However, we also emphasise the preliminary nature of our study and highlight some limitations (
Section
6
) to our methodology.
2
Related Work
2.1
Neural Architecture Design and Search
Neural architecture design plays a prominent role in deep learning research, with numerous studies focusing on developing architectural enhancements.
Seminal works such as LeNet-5
[
42
]
, AlexNet
[
41
]
, VGGNet
[
60
]
, GoogleNet
[
66
]
, ResNet
[
24
]
, DenseNet
[
34
]
, SENet
[
30
]
and Transformers
[
71
]
contributed design insights to improve performance.
Numerous subsequent studies
[
29
,
58
,
28
,
83
,
49
,
75
,
34
,
81
]
have further leveraged hand-crafted designs to explore the space of efficient, more capable architectures.
Neural Architecture Search (NAS) builds on many of these ideas but seeks a greater level of automation in the design process.
Early efforts
[
84
,
85
]
employed reinforcement learning to explore the search space of potential architectures, with later approaches leveraging evolutionary strategies
[
57
]
and Bayesian optimisation
[
39
]
.
There has been considerable focus on reducing the computational burden associated with the search, with proposals such as DARTS
[
47
]
leveraging gradient-based search and EfficientNAS
[
54
]
employing sub-network sampling to increase efficiency.
A rich body of work has further explored this direction
[
62
,
13
,
80
,
79
,
36
,
65
,
7
,
67
,
22
,
68
,
64
,
80
]
.
More recent work has employed evolutionary prompt engineering with soft prompt tuning to use language models for evolutionary NAS
[
8
]
.
In contrast to conventional search strategies, we employ a process that simply prompts GPT-4 to propose designs from a given search space with a handful of examples.
2.2
Exploring GPT-4’s research capabilities
Early studies in the technical report accompanying the release of GPT-4
[
52
]
demonstrated that the model can achieve strong results across a broad suite of examinations designed to test human knowledge in widely-studied scientific disciplines such as biology, chemistry, physics, and computer science
[
2
]
etc.
3
3
3
We note that these results should be interpreted cautiously since the tests were designed for humans rather than language models.
Nevertheless, they indicate some degree of familiarity with concepts that form prerequisites for various domains of scientific research.
A complementary set of preliminary qualitative studies conducted on an early variant of GPT-4 further highlight its ability to perform sophisticated reasoning across many topic areas
[
6
]
, a further key building block for research applications.
These studies also note important limitations in the model of relevance for research tasks - these include longstanding problems with “hallucinations”
[
50
]
and bias
[
27
,
4
]
, as well as an inability to construct appropriate plans in arithmetic and reasoning problems.
Exploring applications in the chemistry domain, concurrent work explores how GPT-4 can be coupled to existing tools like web search and code execution to advance chemical research
[
3
,
1
]
.
Focusing on a different domain, we view our work as complementary to these explorations.
Figure 1:
An overview of the GENIUS framework
.
After an initial problem encoding (corresponding to iteration
T
=
0
T=0
), GPT-4 proposes a model configuration.
A Python program is then executed to evaluate the quality of the configuration (assessed through its accuracy), and the results are passed back to GPT-4 via a natural language prompt for further iterations.
3
Approach
Our proposed method,
G
PT-4
E
nhanced
N
eural arch
I
tect
U
re
S
earch (GENIUS), aims to tackle the challenging neural architecture search (NAS) problem by using GPT-4 as a “black box” optimiser. This entails first simply encoding the NAS problem statement into a human-readable text format that GPT-4 can parse. The model then responds with a model configuration proposal that aims to maximise a given performance objective (e.g., accuracy on a particular benchmark). GENIUS operates through an iterative refinement process.
In the first iteration, we provide the problem encoding to the GPT-4 model which responds with an initial model configuration.
Subsequently, we employ training and evaluation code to execute the model and obtain its empirical accuracy.
This performance metric is then passed back to the GPT-4 model, prompting it to generate an improved model based on the insights gained from previous experiments.
The algorithm is depicted in Algorithm
1
.
Input :
GPT-4
: The GPT-4 API.
Problem_Encoding
: The human-readable text that encodes the NAS problem.
Run
: The training and testing codes for executing and obtaining the ground truth results.
for
T=0 to iteration
do
if
T == 0
then
model = GPT-4(Problem_Encoding)
else
prompt = “
By using this model, we achieved an accuracy of
{Accuracy}
%. Please recommend a new model that outperforms prior architectures based on the abovementioned experiments. Also, Please provide a rationale explaining why the suggested model surpasses all previous architectures.
’’
model = GPT-4(prompt)
 end if
Accuracy
= Run(model)
 end for
Output :
The Best Model Configuration
Algorithm 1
GPT-4 Enhanced Neural Architecture Search (GENIUS)
4
Proof of Concept
In this section, we first apply our GENIUS to two benchmark datasets to validate its effectiveness and empirically investigate its behavior.
Following this, we assess the performance of the optimal architecture identified by GENIUS on a widely-used benchmark in the NAS domain where we compare to the existing state-of-the-art.
4.1
Dataset and Benchmark
1.
NAS-Bench-Macro
4
4
4
https://github.com/xiusu/NAS-Bench-Macro
- This benchmark was first proposed in MCT-NAS
[
62
]
for single-path one-shot NAS methods. It consists of 6561 architectures and their isolated evaluation results on the CIFAR-10 dataset
[
40
]
. The search space of NAS-Bench-Macro is conducted with 8 searching layers, where each layer contains 3 candidate blocks. These blocks are marked as Identity, InvertedResidual Block with kernel size = 3 and expansion ratio = 3, and InvertedResidual Block with kernel size = 5 and expansion ratio = 6. Thus, the total size of the search space is
3
8
=
6561
3^{8}=6561
.
2.
Channel-Bench-Macro
5
5
5
https://github.com/xiusu/Channel-Bench-Macro
- This benchmark was first proposed in BCNet
[
63
]
for channel number search. The search space of this benchmark is conducted with 7 searching layers, where each layer contains 4 uniformly distributed candidate widths. Thus, the overall search space is
4
7
=
16384
4^{7}=16384
. It also provides the test results for all the 16384 architectures on CIFAR10
[
40
]
. Additionally, this benchmark includes two base models, MobileNet
[
58
]
and ResNet
[
24
]
.
4.2
Empirical Study
Random Sampling Baseline.
In the realm of NAS, randomly sampled architectures are typically employed as a baseline. In the context of this study, we will utilize a stochastic function to uniformly sample from the available operations and channel numbers associated with each layer. Concretely, we will perform 10 sampling iterations and subsequently identify the most optimal architectures to serve as our baselines. Nevertheless, we observed considerable variance across individual trials resulting from this sampling approach. To address this, we repeated the 10-iteration process 10,000 times and calculated the average of the best outcomes.
(a)
Accuracy (temp=1)
(b)
Accuracy (temp=0)
(c)
Ranking (temp=1)
(d)
Ranking (temp=0)
Figure 2:
We conducted experiments on
NAS-Bench-Macro
and tested the results at two different temperatures: 0 and 1. Each experiment was repeated 3 times with 10 iterations per experiment. We show both the accuracy and ranking for each iteration. It’s important to note that higher accuracy and lower ranking numbers indicate better architecture.
NAS-Bench-Macro
. To assess the effectiveness of GENIUS, we conduct an experiment using the NAS-Bench-Macro. For this experiment, we set the maximum number of iterations to 10. Since the benchmark provides ground truth accuracy values for each model configuration as a lookup table, we use these to retrieve the relevant accuracy score at each step.
The GPT-4 API includes a
temperature
hyperparameter that controls the randomness of the model’s output, with higher values leading to greater randomness in the output.
We conducted experiments with both temperature=0 and temperature=1 to assess the effectiveness of GENIUS under different levels of randomness.
The experimental results are presented in Figure
2
. We show both the accuracy and the model’s ranking for each iteration. The best model obtained is ranked 8/6561 (Top 0.12%), while the worst model is ranked 61/6561 (Top 0.93%), remaining reasonable.
(
We provide detailed numerical results for this experiment in Appendix A.1
)
We observe that GENIUS exhibits some randomness in its responses, even when the temperature is set to 0.
Nonetheless, despite this randomness, satisfactory results are achieved in the majority of cases.
(a)
ResNet Accuracy
(b)
MobileNet Accuracy
(c)
ResNet Ranking
(d)
MobileNet Ranking
Figure 3:
We performed experiments on the
Channel-Bench-Macro
benchmark, testing the results on both ResNet and MobileNet base models with a fixed Temperature of 0. Each experiment was conducted 3 times with 10 iterations. We show both accuracy and ranking for each iteration. Similar to previous experiments, higher accuracy and lower ranking numbers indicate better architecture.
Channel-Bench-Macro.
We further evaluate the effectiveness of GENIUS on Channel-Bench-Macro. In this experiment, we fix the temperature to 0 and perform only one trial on both ResNet and MobileNet settings. The experimental results are presented in Figure
3
. Similar to the previous experiment, we show the accuracy and rank for 10 iterations. Specifically, GENIUS achieves Rank 33 / 16384 (Top 0.2%) for the ResNet-based model and Rank 16 / 16384 (Top 0.1%) for the MobileNet-based model, further demonstrating its effectiveness. (
We provide detailed numerical results for this experiment in Appendix A.2
)
4.3
NAS-Bench-201
Next, we extend our application of GENIUS to the well-known NAS-Bench-201
[
18
]
benchmark
6
6
6
https://github.com/D-X-Y/NAS-Bench-201
.
This benchmark focuses on designing a cell block for neural architectures.
The cell in the search space is represented as a densely connected directed acyclic graph (DAG) consisting of four nodes and six edges, where nodes represent feature maps, and edges correspond to operations.
With five available operations, the total number of possible search spaces amounts to
5
6
=
15625
5^{6}=15625
.
We conduct evaluations on CIFAR10, CIFAR100, and ImageNet16-120.
Table 1:
Experimental Results on Nas-Bench-201. We set
Temperature = 0
for GPT-4 in this experiment. We report the experimental results based on 5 trials for GENIUS. The performances of DRNAS
[
10
]
,
β
\beta
-DARTS
[
78
]
, and
Λ
\Lambda
-DARTS
[
51
]
are identical, potentially attributable to their near-optimal performance on NAS-Bench-201.
Method
CIFAR10
CIFAR100
ImageNet16-120
Validation
Test
Validation
Test
Validation
Test
DARTS
[
47
]
39.77±0.00
54.30±0.00
38.57±0.00
15.61±0.00
18.87±0.00
16.32±0.00
DSNAS
[
32
]
89.66±0.29
93.08±0.13
30.87±16.40
31.01±16.38
40.61±0.09
41.07±0.09
PC-DARTS
[
77
]
89.96±0.15
93.41±0.30
67.12±0.39
67.48±0.89
40.83±0.08
41.31±0.22
SNAS
[
76
]
90.10±1.04
92.77±0.83
69.69±2.39
69.34±1.98
42.84±1.79
43.16±2.64
iDARTS
[
82
]
89.86±0.60
93.58±0.32
70.57±0.24
70.83±0.48
40.38±0.59
40.89±0.68
GDAS
[
17
]
89.89±0.08
93.61±0.09
71.34±0.04
70.70±0.30
41.59±1.33
41.71±0.98
DRNAS
[
10
]
91.55±0.00
94.36±0.00
73.49±0.00
73.51±0.00
46.37±0.00
46.34±0.00
β
\beta
-DARTS
[
78
]
91.55±0.00
94.36±0.00
73.49±0.00
73.51±0.00
46.37±0.00
46.34±0.00
Λ
\Lambda
-DARTS
[
51
]
91.55±0.00
94.36±0.00
73.49±0.00
73.51±0.00
46.37±0.00
46.34±0.00
GENIUS (Ours)
91.07±0.20
93.79±0.09
70.96±0.33
70.91±0.72
45.29±0.81
44.96±1.02
Consistent with prior experiments, we set the temperature to 0 to minimize randomness and utilize 10 iterations for GENIUS. As this benchmark offers both validation and test accuracy, we employ validation accuracy in the prompt and report the test accuracy corresponding to the highest validation accuracy.
The results are displayed in Table
1
, where we observe that GENIUS achieves competitive performance, though slightly behind leading methods (
[
10
,
78
,
51
]
) attaining accuracies of 93.79±0.09, 70.91±0.72, and 44.96±1.02 on CIFAR10, CIFAR100, and ImageNet16-120, respectively.
(
We also provide additional numerical results for each iteration in Appendix A.3
)
5
Large-Scale Experiments
Our previous experiments demonstrated the potential of using GPT-4 to address the NAS problem.
However, the three benchmarks
[
18
,
62
,
63
]
considered above have two shortcomings.
First, the search space is limited, ranging from 6561 to 16384 architecture candidates in total.
Second, there is no imposition of a FLOPs constraint, which offers a useful proxy for the computational constraints facing architecture designers who target real-world deployment.
To address these shortcomings, we next evaluate the performance of GENIUS on the ImageNet dataset
[
16
]
with the MobileNet V2 search space
[
58
,
28
]
. This setting is widely used for evaluating the performance of NAS algorithms and provides a more realistic and challenging search scenario.
Search Strategy
.
The ImageNet dataset consists of 1.28 million training images and 50K validation images from 1,000 classes.
To avoid overfitting, we split the training data into 99% for training and 1% for validation, retaining the official 50K validation images for testing.
Following the same protocol as in previous experiments, we run our GENIUS method for 10 iterations and validate its performance on the 1% validation set.
Finally, we evaluate the performance of the best architecture selected from the validation set on the 50K testing images.
For each architecture, we train the model for 20 epochs using a standard SGD optimizer with a learning rate of 0.5, weight decay of 1e-4, batch size of 1024, and momentum of 0.9. We use only basic data augmentations such as RandomResizedCrop and RandomFlip during the search stage. We also use 196x196 as the input size to save the search cost.
Search Space
. To ensure a fair comparison with recent works
[
62
,
65
,
79
]
, we conduct architecture search over a search space that includes mobile inverted bottleneck MBConv
[
58
]
and squeeze-excitation modules
[
31
]
. The search space comprises seven basic operators, such as MBConv with kernel sizes of 3, 5, 7 and expansion ratios of 4, 6, as well as a skip connection to enable different depths of architectures. We divide the search space into 5 stages, each containing a maximum of 6 layers. In total, the search space contains approximately
7
30
7^{30}
possible architecture candidates.
Table 2:
Comparison of searched architectures for different NAS methods on ImageNet. Our search cost is measured on V100 GPUs to fair compare with the previous method.
†
\dagger
denotes searched on TPUs.
Method
FLOPs
(M)
Params
(M)
Top-1
(%)
Top-5
(%)
Search Cost
(GPU Days)
MobileNetV2
[
58
]
300
3.4
72.0
91.0
Human Designed
AngleNet
[
33
]
325
-
74.2
-
Unkown
Proxyless-R
[
7
]
320
4.0
74.6
92.2
15
MnasNet-A2
[
67
]
340
4.8
75.6
92.7
288
†
\dagger
BetaNet-A
[
20
]
333
4.1
75.9
92.8
7
SPOS
[
22
]
328
-
76.2
-
12
SCARLET-B
[
12
]
329
6.5
76.3
93.0
22
ST-NAS-A
[
21
]
326
5.2
76.4
93.1
Unkown
GreedyNAS-B
[
79
]
324
5.2
76.8
93.0
7
MCT-NAS-B
[
62
]
327
6.3
76.9
93.4
12
FairNAS-C
[
13
]
325
5.6
76.7
93.3
Unkown
K-shot-NAS-B
[
65
]
332
6.2
77.2
93.3
12
FBNetV2-L1
[
72
]
325
-
77.2
-
25
NSENet
[
14
]
333
7.6
77.3
-
167
GreedyNASv2-S
[
36
]
324
5.7
77.5
93.5
7
Cream-S
[
53
]
287
6.0
77.6
93.3
12
GENIUS - 329 (Ours)
329
7.0
77.8
93.7
5.6
ProxylessNAS
[
7
]
465
7.1
75.1
-
15
SCARLET-A
[
12
]
365
6.7
76.9
93.4
24
GreedyNAS-A
[
79
]
366
6.5
77.1
93.3
7
BossNet-M2
[
44
]
403
-
77.4
93.6
10
DNA-B
[
43
]
403
4.9
77.5
93.3
8.5
EfficientNet-B0 (Timm)
[
68
,
74
]
390
5.3
77.7
93.3
Unkown
ST-NAS-B
[
21
]
503
7.8
77.9
93.8
Unkown
MCT-NAS-A
[
62
]
442
8.4
78.0
93.9
12
GENIUS - 401 (Ours)
401
7.5
78.2
93.8
5.7
FLOPs Constraint
. In order to further limit the FLOPs of the generated architectures, we incorporate a FLOPs look-up table within the problem encoding, allowing the GPT-4 to efficiently access the FLOPs count for each operation in every layer. Despite this, we discovered that the resulting architectures frequently surpass the designated FLOPs constraints. To overcome this challenge, we introduce a supplementary iterative loop within the GENIUS framework, which involves evaluating the actual FLOPs, providing feedback to the GPT-4, and iteratively refining the design until it adheres to the FLOPs constraint.
Retraining Strategy
. Upon selecting the optimal architecture from the validation set, we adhere to the training strategy employed in a majority of prior works.
[
68
,
79
,
53
]
. Specifically, we utilize the standard SGD optimizer with a momentum of 0.9 and a weight decay of 4e-5. We set an initial learning rate of 0.8, incorporating a warmup period of 5 epochs, and apply the cosine learning rate scheduler as described in
[
48
]
. Additionally, we also involve a dropout rate of 0.2, RandAugment
[
15
]
with n=2 and m=9. Furthermore, we employ an exponential moving average (EMA) network, and the performance is reported on the EMA network. The retraining process is conducted using 8 NVIDIA A100 GPUs, with a batch size of 2,048 and 500 epochs.
Results
. We conducted experiments using two popular FLOPs constraints, one at approximately 300M and another at around 400M. The results are presented in Table
2
. Notably, our GENIUS architecture demonstrates strong performance when compared to previous work.
In the 300M setting, GENIUS achieves a 77.8% Top-1 accuracy with 329M FLOPs, which is 0.2% higher than CREAM-S
[
53
]
at 287M FLOPs.
In the 400M setting, GENIUS attains a 78.2% Top-1 accuracy with 401M FLOPs, outperforming MCT-NAS-A’s 442M FLOPs by 0.2%.
These results validate the effectiveness of GENIUS.
We note that the search cost of GENIUS is significantly lower than that of previous methods.
We also note, however, that under scenarios that multiple require architectures at different FLOP constraints, Single Path One Shot approaches allow the user to amortise the cost of the search over different FLOP constraints—this amortisation is not available to GENIUS in the simple formulation we propose.
5.1
Ablation Study
Table 3:
Training epochs for search stage. We fix input size as 224 in this experiment.
Epochs
10
20
30
40
50
Top-1 (%)
76.4
76.7
76.7
76.7
76.6
Search Cost
3.0
6.1
9.2
12.3
15.4
Table 4:
Input size for search stage. We fix epochs as 20 in this experiment.
Input Size
224
196
160
128
96
Top-1 (%)
76.7
76.9
76.7
76.5
76.2
Search Cost
6.1
5.6
5.2
4.8
4.5
In NAS, search cost is a primary concern. Our GENIUS method necessitates providing the actual accuracy of a model as feedback to GPT-4. For large-scale datasets (e.g., ImageNet), executing a standard training strategy for each generated architecture can be exceedingly costly. Instead, we can train the model in a lower-cost setting, as long as the results are adequately informative for GPT-4. Consequently, we conduct two experiments, as shown in Table
4
and
4
, to investigate the trade-off between search cost and final accuracy. We constrain the FLOPs to approximately 300M in this experiment and select the best architecture based on 1% validation accuracy. The retraining strategy remains the same as in previous experiments, but with only 180 epochs.
Table
4
demonstrates the results of training the GENIUS-suggested model for 10, 20, 30, 40, and 50 epochs, respectively, and providing feedback to GPT-4. We observe that 20 epochs of training yields sufficient accuracy to supply informative feedback; additional epochs do not improve the final accuracy but substantially increase the search cost. In Table
4
, we fix the training epochs at 20 and vary the input size: 224, 196, 160, 128, and 96. Optimal results are achieved with an input size of 196, while further reducing the input size considerably diminishes the final accuracy. Therefore, our default setting consists of 20 epochs of training with an input size of 196. We recognize that GPT-4’s response variability might influence the ablation study. However, given the stability of the results in these two experiments, we believe they still provide valuable insights into the trade-off between search cost and final accuracy.
5.2
Transfer Learning
Classification
. We further assess the transferability of our GENIUS model by employing an ImageNet-pretrained model, which we subsequently fine-tune on the CIFAR10 and CIFAR100 datasets. The experimental setup adheres to the procedures outlined in
[
13
,
37
]
. Table
5
presents the results, indicating that GENIUS achieves marginally superior performance compared to FairNAS-A
[
13
]
, thereby demonstrating its transferability.
Table 5:
Transfer learning performance on the classification task.
Backbone
Input Size
FLOPs(M)
Param(M)
CIFAR-10
CIFAR-100
NASNet-A
[
85
]
331
×
\times
331
12030
85
98.0
86.7
EfficientNet-B0
[
68
]
224
×
\times
224
387
5.3
98.1
86.8
MixNet-M
[
69
]
224
×
\times
224
359
5.0
97.9
87.1
FairNas-A
[
13
]
224
×
\times
224
391
5.9
98.2
87.3
FairNas-C
[
13
]
224
×
\times
224
324
5.6
98.0
86.7
GENIUS - 329 (Ours)
224
×
\times
224
329
7.0
98.2
87.3
GENIUS - 401 (Ours)
224
×
\times
224
401
7.5
98.3
87.4
Object Detection
. In this section, we assess the performance of our model by applying it to the object detection task, following the experimental setup detailed in
[
13
]
. Specifically, we directly employ the configuration file
7
7
7
https://github.com/open-mmlab/mmdetection/blob/main/configs/retinanet/retinanet_r50_fpn_1x_coco.py
from MMDetection
[
9
]
and override the model definitions. We train the model on the MS COCO
[
46
]
train2017
set (118k images) and evaluate it on the
val2017
set (5k images). The model is optimized over 12 epochs using a batch size of 16 across 8 GPUs. The initial learning rate is set to 0.01 and is decayed by a factor of 0.1 at epochs 8 and 11. We use the SGD optimizer with a momentum of 0.9 and weight decay of 1e-4. The detection algorithm employed in this study is RetinaNet
[
45
]
. Performance results are presented in Table
6
, demonstrating that our GENIUS model significantly outperforms previous methods in the detection task. For instance, our model achieves a 7.8% improvement over the MobileNetV2 baseline and a 0.9% enhancement compared to prior art (GreedyNASV2). These experiments indicate that the GENIUS-searched architectures possess strong generalization capabilities in localization-sensitive tasks.
Table 6:
Transfer learning performance on object detection with RetinaNet
[
45
]
. The performance is evaluated on COCO
val2017
. The FLOPs are evaluated with 224x224 inputs. Top-1 indicates the ImageNet Results. The results for other methods are directly copied from
[
53
]
.
Backbone
FLOPs(M)
AP(%)
AP
50
AP
75
AP
S
AP
M
AP
L
Top-1
MobileNetV2
[
58
]
300
28.3
46.7
29.3
14.8
30.7
38.1
72.0
MobileNetV3
[
28
]
219
29.9
49.3
30.8
14.9
33.3
41.1
75.2
MnasNet-A2
[
67
]
340
30.5
50.2
32.0
16.6
34.1
41.1
75.6
SPOS
[
22
]
365
30.7
49.8
32.2
15.4
33.9
41.6
75.0
FairNAS-C
[
13
]
325
31.2
50.8
32.7
16.3
34.4
42.3
76.7
MixNet-M
[
69
]
360
31.3
51.7
32.4
17.0
35.0
41.9
77.0
MixPath-A
[
11
]
349
31.5
51.3
33.2
17.4
35.3
41.8
76.9
FairNAS-A
[
13
]
392
32.4
52.4
33.9
17.2
36.3
43.2
77.5
Cream-S
[
53
]
287
33.2
53.6
34.9
18.2
36.6
44.4
77.6
GreedyNASV2
[
36
]
324
34.9
-
-
-
-
-
77.5
GENIUS - 329 (Ours)
329
35.8
55.3
38.1
19.6
38.7
48.1
77.8
5.3
Eliciting design principles from GPT-4
The architectures uncovered by GENIUS exhibit strong performance on various visual tasks, surpassing the state-of-the-art in several cases.
Moreover, our search required little domain expertise—instead, this technical burden was transferred to GPT-4.
It is therefore of interest to examine how GPT-4 describes the principles by which it tackles the search problem.
When prompted, it offers the following maxims when considering the MobileNetV2 search space:
(1) In the initial stages, employ simpler operations to effectively capture low-level information. Subsequently, integrate more complex operations in the later stages to accurately represent higher-level information.
(2) To capture intricate features, the latter stages of the network must exhibit increased depth, while the earlier stages can maintain a shallower architecture.
We have no guarantee that these introspective descriptions truly reflect the principles used during the GENIUS search process
[
70
]
, but they nevertheless suggest an interpretable, intuitive characterisation of how GPT-4 approaches a specific search scenario.
6
Limitations
We identify several important limitations to our study.
Reproducibility.
First, we have little insight into the operations that wrap GPT-4 inference behind the API provided by OpenAI.
For example, we do not know if our problem encoding text is pre-processed or if the model response is post-processed in some way (for example, by content moderation policies that are opaque to API clients).
It is possible that any such operations change over the course of an experiment, and we are unable to control for such changes.
Second, even with the temperature set to 0, we observe some variation in GPT-4 responses, making it challenging to numerically reproduce a particular experimental run.
Benchmark contamination.
We do not know which data was included in the training set for GPT-4, or the final cut-off date for training data provided to the model
8
8
8
In
[
52
]
, the authors note:
GPT-4 generally lacks knowledge of events that have occurred after the vast majority of its pre-training data cuts off in September 2021…. the pre-training and post-training data contain a small amount of more recent data.
.
It is therefore possible that the benchmarks employed in our studies have all been “seen” by GPT-4, and thus it is searching “from memory” rather than leveraging insight about how to improve an architecture design.
We note that previous studies examining the evidence of contamination have often found its effect on final performance to be somewhat limited
[
5
,
55
]
, perhaps due to the challenge of memorizing so much magnitude of the training data.
Nevertheless, the fact that we cannot rule out contamination represents a significant caveat to our findings.
One potential solution to address this in future work could be the construction of private optimisation benchmarks that are hidden from the open internet to ensure that they are excluded from the training data of large language models.
Limited control and inscrutability.
Prompting represents our sole point of control over GPT-4, but we have relatively little understanding of how changes to the prompt influence behaviour as an optimiser.
On the NAS-Bench-201 benchmark (see more details in Appendix A.3.), we find that later iterations under-perform earlier iterations in some cases, and it is unclear why this should be the case given that: (i) our prompt requests improved performance, (ii) our experimental evidence suggests that GPT-4 is capable of providing improved performance.
We believe future work on this problem is particularly valuable.
7
AI safety
As AI systems become more capable, they exhibit greater potential for useful applications.
However, they also represent greater risk—a concern that has been discussed by leading researchers within the field of AI for more than 60 years
[
73
]
.
The use of GPT-4 as a black-box optimiser can potentially represent an offloading of intellectual labour from a human researcher to an inscrutable system.
This contributes to the risk of
enfeeblement
[
26
]
in which know-how erodes by delegating increasingly many important functions to machines.
If general-purpose black-box optimisers ultimately prove superior to interpretable alternatives, competition pressures may incentivise such delegation
[
25
]
.
Architecture search, in particular, represents a potential vector for self-improvement (potentially complementing strategies that improve the inference capabilities of a trained model
[
35
]
).
Such research can yield improved performance on tasks deemed beneficial by society, but may also exacerbate risk.
We believe it is useful to study whether existing, publicly available frontier models like GPT-4 possess such capabilities.
Our tentative results (subject to the important limiting caveats described in Sec.
6
), taken together with concurrent studies of scientific automation in other domains
[
3
,
1
]
, suggest that GPT-4 could potentially represent an artefact that leads to accelerated scientific research and therefore caution is appropriate in its application.
8
Conclusion
In this paper, we present GENIUS, a novel NAS approach that employs the GPT-4 language model as a black-box optimiser to expedite the process of discovering efficient neural architectures.
We compare GENIUS against leading NAS methods, underscoring its effectiveness and highlighting the of GPT-4 as a tool for research and development.
We also note safety implications and discuss several important limitations of our work.
In future work, we plan to further study the capabilities and limitations of GPT-4 (and other frontier language models) to serve as optimisers in applications that have traditionally required extensive domain expertise, and to more extensively investigate the safety implications of such research.
Acknowledgment
We thank H. Bradley for suggesting the method acronym.
This work was supported by an Isaac Newton Trust grant.
S. Albanie would like to thank Z. Novak and N. Novak for enabling his contribution.
References
[1]
Boiko, D.A., MacKnight, R., Gomes, G.: Emergent autonomous scientific research
capabilities of large language models. arXiv preprint arXiv:2304.05332
(2023)
[2]
Bordt, S., von Luxburg, U.: Chatgpt participates in a computer science exam.
arXiv preprint arXiv:2303.09461 (2023)
[3]
Bran, A.M., Cox, S., White, A.D., Schwaller, P.: Chemcrow: Augmenting
large-language models with chemistry tools. arXiv preprint arXiv:2304.05376
(2023)
[4]
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P.,
Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al.: Language models
are few-shot learners. Advances in neural information processing systems
33
, 1877–1901 (2020)
[5]
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P.,
Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al.: Language models
are few-shot learners. Advances in neural information processing systems
33
, 1877–1901 (2020)
[6]
Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E.,
Lee, P., Lee, Y.T., Li, Y., Lundberg, S., et al.: Sparks of artificial
general intelligence: Early experiments with gpt-4. arXiv preprint
arXiv:2303.12712 (2023)
[7]
Cai, H., Zhu, L., Han, S.: Proxylessnas: Direct neural architecture search on
target task and hardware. arXiv preprint arXiv:1812.00332 (2018)
[8]
Chen, A., Dohan, D.M., So, D.R.: Evoprompting: Language models for code-level
neural architecture search. arXiv preprint arXiv:2302.14838 (2023)
[9]
Chen, K., Wang, J., Pang, J., Cao, Y., Xiong, Y., Li, X., Sun, S., Feng, W.,
Liu, Z., Xu, J., Zhang, Z., Cheng, D., Zhu, C., Cheng, T., Zhao, Q., Li, B.,
Lu, X., Zhu, R., Wu, Y., Dai, J., Wang, J., Shi, J., Ouyang, W., Loy, C.C.,
Lin, D.: MMDetection: Open mmlab detection toolbox and benchmark. arXiv
preprint arXiv:1906.07155 (2019)
[10]
Chen, X., Wang, R., Cheng, M., Tang, X., Hsieh, C.J.: Dr{nas}: Dirichlet
neural architecture search. In: International Conference on Learning
Representations (2021),
https://openreview.net/forum?id=9FWas6YbmB3
[11]
Chu, X., Li, X., Lu, S., Zhang, B., Li, J.: Mixpath: A unified approach for
one-shot neural architecture search. arXiv preprint arXiv:2001.05887 (2020)
[12]
Chu, X., Zhang, B., Li, J., Li, Q., Xu, R.: Scarletnas: Bridging the gap
between scalability and fairness in neural architecture search. arXiv
preprint arXiv:1908.06022
4
(6) (2019)
[13]
Chu, X., Zhang, B., Xu, R.: Fairnas: Rethinking evaluation fairness of weight
sharing neural architecture search. In: Proceedings of the IEEE/CVF
International Conference on computer vision. pp. 12239–12248 (2021)
[14]
Ci, Y., Lin, C., Sun, M., Chen, B., Zhang, H., Ouyang, W.: Evolving search
space for neural architecture search. In: Proceedings of the IEEE/CVF
International Conference on Computer Vision. pp. 6659–6669 (2021)
[15]
Cubuk, E.D., Zoph, B., Shlens, J., Le, Q.V.: Randaugment: Practical automated
data augmentation with a reduced search space. In: Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops. pp.
702–703 (2020)
[16]
Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L.: ImageNet: A
Large-Scale Hierarchical Image Database. In: CVPR09 (2009)
[17]
Dong, X., Yang, Y.: Searching for a robust neural architecture in four gpu
hours. In: Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition. pp. 1761–1770 (2019)
[18]
Dong, X., Yang, Y.: Nas-bench-201: Extending the scope of reproducible neural
architecture search. In: International Conference on Learning Representations
(2020),
https://openreview.net/forum?id=HJxyZkBKDr
[19]
Everingham, M., Van Gool, L., Williams, C.K., Winn, J., Zisserman, A.: The
pascal visual object classes (voc) challenge. International journal of
computer vision
88
(2), 303–338 (2010)
[20]
Fang, M., Wang, Q., Zhong, Z.: Betanas: Balanced training and selective drop
for neural architecture search. arXiv preprint arXiv:1912.11191 (2019)
[21]
Guo, R., Lin, C., Li, C., Tian, K., Sun, M., Sheng, L., Yan, J.: Powering
one-shot topological nas with stabilized share-parameter proxy. In: Computer
Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28,
2020, Proceedings, Part XIV. pp. 625–641. Springer (2020)
[22]
Guo, Z., Zhang, X., Mu, H., Heng, W., Liu, Z., Wei, Y., Sun, J.: Single path
one-shot neural architecture search with uniform sampling. In: Computer
Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28,
2020, Proceedings, Part XVI 16. pp. 544–560. Springer (2020)
[23]
He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image
recognition. In: Proceedings of the IEEE conference on computer vision and
pattern recognition. pp. 770–778 (2016)
[24]
He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image
recognition. In: Proceedings of the IEEE conference on computer vision and
pattern recognition. pp. 770–778 (2016)
[25]
Hendrycks, D.: Natural selection favors ais over humans. arXiv preprint
arXiv:2303.16200 (2023)
[26]
Hendrycks, D., Mazeika, M.: X-risk analysis for ai research. arXiv preprint
arXiv:2206.05862 (2022)
[27]
Hovy, D., Spruit, S.L.: The social impact of natural language processing. In:
Proceedings of the 54th Annual Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers). pp. 591–598 (2016)
[28]
Howard, A., Sandler, M., Chu, G., Chen, L.C., Chen, B., Tan, M., Wang, W., Zhu,
Y., Pang, R., Vasudevan, V., et al.: Searching for mobilenetv3. In:
Proceedings of the IEEE/CVF international conference on computer vision. pp.
1314–1324 (2019)
[29]
Howard, A.G., Zhu, M., Chen, B., Kalenichenko, D., Wang, W., Weyand, T.,
Andreetto, M., Adam, H.: Mobilenets: Efficient convolutional neural networks
for mobile vision applications. arXiv preprint arXiv:1704.04861 (2017)
[30]
Hu, J., Shen, L., Albanie, S., Sun, G., Wu, E.: Squeeze-and-excitation
networks. IEEE Transactions on Pattern Analysis and Machine Intelligence
42
, 2011–2023 (2017)
[31]
Hu, J., Shen, L., Albanie, S., Sun, G., Wu, E.: Squeeze-and-excitation
networks. IEEE Transactions on Pattern Analysis and Machine Intelligence
42
, 2011–2023 (2017)
[32]
Hu, S., Xie, S., Zheng, H., Liu, C., Shi, J., Liu, X., Lin, D.: Dsnas: Direct
neural architecture search without parameter retraining. In: Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp.
12084–12092 (2020)
[33]
Hu, Y., Liang, Y., Guo, Z., Wan, R., Zhang, X., Wei, Y., Gu, Q., Sun, J.:
Angle-based search space shrinking for neural architecture search. In:
Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August
23–28, 2020, Proceedings, Part XIX 16. pp. 119–134. Springer (2020)
[34]
Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q.: Densely connected
convolutional networks. In: Proceedings of the IEEE conference on computer
vision and pattern recognition. pp. 4700–4708 (2017)
[35]
Huang, J., Gu, S.S., Hou, L., Wu, Y., Wang, X., Yu, H., Han, J.: Large language
models can self-improve. arXiv preprint arXiv:2210.11610 (2022)
[36]
Huang, T., You, S., Wang, F., Qian, C., Zhang, C., Wang, X., Xu, C.:
Greedynasv2: Greedier search with a greedy path filter. In: Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp.
11902–11911 (2022)
[37]
Huang, Y., Cheng, Y., Bapna, A., Firat, O., Chen, D., Chen, M., Lee, H., Ngiam,
J., Le, Q.V., Wu, Y., et al.: Gpipe: Efficient training of giant neural
networks using pipeline parallelism. Advances in neural information
processing systems
32
(2019)
[38]
Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O.,
Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., et al.:
Highly accurate protein structure prediction with alphafold. Nature
596
(7873), 583–589 (2021)
[39]
Kandasamy, K., Neiswanger, W., Schneider, J., Poczos, B., Xing, E.P.: Neural
architecture search with bayesian optimisation and optimal transport.
Advances in neural information processing systems
31
(2018)
[40]
Krizhevsky, A., Hinton, G., et al.: Learning multiple layers of features from
tiny images (2009)
[41]
Krizhevsky, A., Sutskever, I., Hinton, G.E.: Imagenet classification with deep
convolutional neural networks. In: Pereira, F., Burges, C., Bottou, L.,
Weinberger, K. (eds.) Advances in Neural Information Processing Systems.
vol. 25. Curran Associates, Inc. (2012),
https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
[42]
LeCun, Y., Bottou, L., Bengio, Y., Haffner, P.: Gradient-based learning applied
to document recognition. Proceedings of the IEEE
86
(11),
2278–2324 (1998)
[43]
Li, C., Peng, J., Yuan, L., Wang, G., Liang, X., Lin, L., Chang, X.:
Block-wisely supervised neural architecture search with knowledge
distillation. In: Proceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition. pp. 1989–1998 (2020)
[44]
Li, C., Tang, T., Wang, G., Peng, J., Wang, B., Liang, X., Chang, X.: Bossnas:
Exploring hybrid cnn-transformers with block-wisely self-supervised neural
architecture search. In: Proceedings of the IEEE/CVF International Conference
on Computer Vision. pp. 12281–12291 (2021)
[45]
Lin, T.Y., Goyal, P., Girshick, R., He, K., Dollár, P.: Focal loss for
dense object detection. In: Proceedings of the IEEE international conference
on computer vision. pp. 2980–2988 (2017)
[46]
Lin, T.Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D.,
Dollár, P., Zitnick, C.L.: Microsoft coco: Common objects in context. In:
European conference on computer vision. pp. 740–755. Springer (2014)
[47]
Liu, H., Simonyan, K., Yang, Y.: Darts: Differentiable architecture search.
arXiv preprint arXiv:1806.09055 (2018)
[48]
Loshchilov, I., Hutter, F.: Sgdr: Stochastic gradient descent with warm
restarts. arXiv preprint arXiv:1608.03983 (2016)
[49]
Ma, N., Zhang, X., Zheng, H.T., Sun, J.: Shufflenet v2: Practical guidelines
for efficient cnn architecture design. In: Proceedings of the European
conference on computer vision (ECCV). pp. 116–131 (2018)
[50]
Maynez, J., Narayan, S., Bohnet, B., McDonald, R.: On faithfulness and
factuality in abstractive summarization. arXiv preprint arXiv:2005.00661
(2020)
[51]
Movahedi, S., Adabinejad, M., Imani, A., Keshavarz, A., Dehghani, M., Shakery,
A., Araabi, B.N.: $\lambda$-DARTS: Mitigating performance
collapse by harmonizing operation selection among cells. In: The Eleventh
International Conference on Learning Representations (2023),
https://openreview.net/forum?id=oztkQizr3kk
[52]
OpenAI: Gpt-4 technical report (2023)
[53]
Peng, H., Du, H., Yu, H., Li, Q., Liao, J., Fu, J.: Cream of the crop:
Distilling prioritized paths for one-shot neural architecture search.
Advances in Neural Information Processing Systems
33
(2020)
[54]
Pham, H., Guan, M., Zoph, B., Le, Q., Dean, J.: Efficient neural architecture
search via parameters sharing. In: International conference on machine
learning. pp. 4095–4104. PMLR (2018)
[55]
Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry,
G., Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual
models from natural language supervision. In: International conference on
machine learning. pp. 8748–8763. PMLR (2021)
[56]
Rajpurkar, P., Zhang, J., Lopyrev, K., Liang, P.: Squad: 100,000+ questions for
machine comprehension of text. arXiv preprint arXiv:1606.05250 (2016)
[57]
Real, E., Moore, S., Selle, A., Saxena, S., Suematsu, Y.L., Tan, J., Le, Q.V.,
Kurakin, A.: Large-scale evolution of image classifiers. In: International
Conference on Machine Learning. pp. 2902–2911. PMLR (2017)
[58]
Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., Chen, L.C.: Mobilenetv2:
Inverted residuals and linear bottlenecks. In: Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition (CVPR) (June 2018)
[59]
Shallue, C.J., Vanderburg, A.: Identifying exoplanets with deep learning: A
five-planet resonant chain around kepler-80 and an eighth planet around
kepler-90. The Astronomical Journal
155
(2),  94 (2018)
[60]
Simonyan, K., Zisserman, A.: Very deep convolutional networks for large-scale
image recognition. In: International Conference on Learning Representations
(2015)
[61]
Stokes, J.M., Yang, K., Swanson, K., Jin, W., Cubillos-Ruiz, A., Donghia, N.M.,
MacNair, C.R., French, S., Carfrae, L.A., Bloom-Ackermann, Z., et al.: A deep
learning approach to antibiotic discovery. Cell
180
(4), 688–702
(2020)
[62]
Su, X., Huang, T., Li, Y., You, S., Wang, F., Qian, C., Zhang, C., Xu, C.:
Prioritized architecture sampling with monto-carlo tree search. In:
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. pp. 10968–10977 (2021)
[63]
Su, X., You, S., Xie, J., Wang, F., Qian, C., Zhang, C., Xu, C.: Searching for
network width with bilaterally coupled network. IEEE Transactions on Pattern
Analysis and Machine Intelligence pp. 1–17 (2022).
https://doi.org/10.1109/TPAMI.2022.3226777
[64]
Su, X., You, S., Xie, J., Zheng, M., Wang, F., Qian, C., Zhang, C., Wang, X.,
Xu, C.: Vitas: Vision transformer architecture search. In: Computer
Vision–ECCV 2022: 17th European Conference, Tel Aviv, Israel, October
23–27, 2022, Proceedings, Part XXI. pp. 139–157. Springer (2022)
[65]
Su, X., You, S., Zheng, M., Wang, F., Qian, C., Zhang, C., Xu, C.: K-shot nas:
Learnable weight-sharing for nas with k-shot supernets. In: International
Conference on Machine Learning. pp. 9880–9890. PMLR (2021)
[66]
Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D.,
Vanhoucke, V., Rabinovich, A.: Going deeper with convolutions. In: 2015 IEEE
Conference on Computer Vision and Pattern Recognition (CVPR). pp. 1–9
(2015). https://doi.org/10.1109/CVPR.2015.7298594
[67]
Tan, M., Chen, B., Pang, R., Vasudevan, V., Sandler, M., Howard, A., Le, Q.V.:
Mnasnet: Platform-aware neural architecture search for mobile. In:
Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition. pp. 2820–2828 (2019)
[68]
Tan, M., Le, Q.: Efficientnet: Rethinking model scaling for convolutional
neural networks. In: International conference on machine learning. pp.
6105–6114. PMLR (2019)
[69]
Tan, M., Le, Q.V.: Mixconv: Mixed depthwise convolutional kernels. arXiv
preprint arXiv:1907.09595 (2019)
[70]
Turpin, M., Michael, J., Perez, E., Bowman, S.R.: Language models don’t always
say what they think: Unfaithful explanations in chain-of-thought prompting.
arXiv preprint arXiv:2305.04388 (2023)
[71]
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
Kaiser, Ł., Polosukhin, I.: Attention is all you need. Advances in neural
information processing systems
30
(2017)
[72]
Wan, A., Dai, X., Zhang, P., He, Z., Tian, Y., Xie, S., Wu, B., Yu, M., Xu, T.,
Chen, K., et al.: Fbnetv2: Differentiable neural architecture search for
spatial and channel dimensions. In: Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition. pp. 12965–12974 (2020)
[73]
Wiener, N.: Some moral and technical consequences of automation. Science
131 3410
, 1355–8 (1960)
[74]
Wightman, R.: Pytorch image models.
https://github.com/rwightman/pytorch-image-models
(2019).
https://doi.org/10.5281/zenodo.4414861
[75]
Xie, S., Girshick, R., Dollár, P., Tu, Z., He, K.: Aggregated residual
transformations for deep neural networks. In: Proceedings of the IEEE
conference on computer vision and pattern recognition. pp. 1492–1500 (2017)
[76]
Xie, S., Zheng, H., Liu, C., Lin, L.: Snas: stochastic neural architecture
search. arXiv preprint arXiv:1812.09926 (2018)
[77]
Xu, Y., Xie, L., Zhang, X., Chen, X., Qi, G.J., Tian, Q., Xiong, H.: Pc-darts:
Partial channel connections for memory-efficient architecture search. arXiv
preprint arXiv:1907.05737 (2019)
[78]
Ye, P., Li, B., Li, Y., Chen, T., Fan, J., Ouyang, W.: b-darts: Beta-decay
regularization for differentiable architecture search. In: Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp.
10874–10883 (2022)
[79]
You, S., Huang, T., Yang, M., Wang, F., Qian, C., Zhang, C.: Greedynas: Towards
fast one-shot nas with greedy supernet. In: Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition. pp. 1999–2008 (2020)
[80]
Yu, J., Jin, P., Liu, H., Bender, G., Kindermans, P.J., Tan, M., Huang, T.,
Song, X., Pang, R., Le, Q.: Bignas: Scaling up neural architecture search
with big single-stage models. In: Computer Vision–ECCV 2020: 16th European
Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part VII 16. pp.
702–717. Springer (2020)
[81]
Zhang, H., Wu, C., Zhang, Z., Zhu, Y., Zhang, Z., Lin, H., Sun, Y., He, T.,
Muller, J., Manmatha, R., Li, M., Smola, A.: Resnest: Split-attention
networks. arXiv preprint arXiv:2004.08955 (2020)
[82]
Zhang, M., Su, S.W., Pan, S., Chang, X., Abbasnejad, E.M., Haffari, R.: idarts:
Differentiable architecture search with stochastic implicit gradients. In:
International Conference on Machine Learning. pp. 12557–12566. PMLR (2021)
[83]
Zhang, X., Zhou, X., Lin, M., Sun, J.: Shufflenet: An extremely efficient
convolutional neural network for mobile devices. In: Proceedings of the IEEE
conference on computer vision and pattern recognition. pp. 6848–6856 (2018)
[84]
Zoph, B., Le, Q.: Neural architecture search with reinforcement learning. In:
International Conference on Learning Representations (2017),
https://openreview.net/forum?id=r1Ue8Hcxg
[85]
Zoph, B., Vasudevan, V., Shlens, J., Le, Q.V.: Learning transferable
architectures for scalable image recognition. In: Proceedings of the IEEE
conference on computer vision and pattern recognition. pp. 8697–8710 (2018)
Appendix A
Numerical Results
A.1
Detailed Numerical Results for Figure
2
Table 7:
Experimental Results on NAS-Bench-Macro. We set
Temperature = 1
for GPT-4 in this experiment. T is the iteration.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Optimal
Trial 1
Acc
90.90
92.40
92.30
92.53
92.63
92.66
92.97
92.56
92.50
92.56
93.13
Ranking
3440
590
766
353
203
180
19
311
394
314
1
Trial 2
Acc
90.42
92.49
92.53
92.85
92.54
92.56
92.58
92.73
92.48
92.78
93.13
Ranking
4042
442
384
50
332
331
272
119
446
82
1
Trial 3
Acc
91.35
92.78
92.82
92.74
92.34
92.35
92.45
92.56
92.54
92.66
93.13
Ranking
2609
83
65
117
683
664
483
311
341
180
1
Table 8:
Experimental Results on NAS-Bench-Macro. We set
Temperature = 0
for GPT-4 in this experiment. T is the iteration.. ‘-’ denotes that GPT-4 asserts there is no chance to improve the performance further.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Optimal
Trial 1
Acc
85.70
92.62
92.82
93.05
92.95
92.46
-
-
-
-
93.13
Ranking
6221
212
64
8
21
479
-
-
-
-
1
Trial 2
Acc
92.45
92.66
92.92
92.64
92.33
92.72
-
-
-
-
93.13
Ranking
496
189
27
198
695
128
-
-
-
-
1
Trial 3
Acc
92.41
92.74
92.83
92.74
92.33
92.53
92.69
92.34
92.56
92.72
93.13
Ranking
564
113
61
112
689
352
152
683
314
128
1
A.2
Detailed Numerical Results for Figure
3
Table 9:
Experimental Results on Channel-Bench-Macro with
ResNet
. We set
Temperature = 0
for GPT-4 in this experiment. T is the iteration.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Optimal
Trial 1
Acc
93.06
93.52
93.56
93.61
93.70
93.73
93.62
93.76
93.49
93.66
93.89
Ranking
9862
1205
737
411
103
61
365
33
1515
173
1
Trial 2
Acc
92.89
93.41
93.65
93.64
93.67
93.48
93.82
93.62
93.80
93.64
93.89
Ranking
12457
2813
209
272
142
1708
8
376
13
260
1
Trial 3
Acc
92.60
93.41
93.44
93.64
93.65
93.67
93.75
93.62
93.66
93.73
93.89
Ranking
15178
2813
2349
272
190
142
37
376
181
59
1
Table 10:
Experimental Results on Channel-Bench-Macro with
MobileNet
. We set
Temperature = 0
for GPT-4 in this experiment. T is the iteration. ‘-’ denotes that GPT-4 asserts there is no chance to improve the performance further.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Optimal
Trial 1
Acc
91.02
91.46
91.66
91.76
91.35
91.63
91.53
91.35
91.46
91.51
91.89
Ranking
5383
630
65
16
1383
80
318
1383
630
380
1
Trial 2
Acc
91.03
91.60
91.66
91.76
91.42
91.53
91.67
91.76
-
-
91.89
Ranking
5271
146
65
16
871
318
59
16
-
-
1
Trial 3
Acc
91.07
91.52
91.66
91.59
91.76
91.66
91.42
91.67
91.76
-
91.89
Ranking
4707
359
65
164
16
65
871
59
16
-
1
A.3
Detailed Numerical Results for NAS-Bench-201
Table 11:
Experimental Results on NAS-Bench-201 with
CIFAR10
. We set Temperature = 0 for GPT-4 in this experiment. T is the iteration. We perform GENIUS on the validation set and report the final accuracy and ranking on the test set based on the best architectures verified on the validation set.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Test Acc
Ranking
Trial 1
90.59
90.15
90.42
90.06
89.60
91.28
90.15
90.92
90.88
86.41
93.79
142
Trial 2
90.88
90.44
90.86
88.99
87.45
90.05
89.33
88.65
90.43
85.10
93.83
114
Trial 3
91.28
90.80
90.88
91.10
90.15
86.41
86.45
86.34
86.17
86.33
93.79
142
Trial 4
90.60
90.05
90.43
89.36
89.93
90.05
91.01
90.85
89.36
88.64
93.92
62
Trial 5
90.36
89.48
89.52
89.98
90.80
89.90
89.36
89.28
89.82
89.98
93.64
279
Table 12:
Experimental Results on NAS-Bench-201 with
CIFAR100
. We set Temperature = 0 for GPT-4 in this experiment. T is the iteration. We perform GENIUS on the validation set and report the final accuracy and ranking on the test set based on the best architectures verified on the validation set.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Test Acc
Ranking
Trail 1
69.46
71.29
69.66
69.46
68.79
70.75
69.16
70.24
70.16
69.18
71.51
103
Trial 2
70.05
65.33
69.64
70.81
66.77
65.19
70.70
70.37
66.85
65.84
70.78
292
Trial 3
69.39
69.56
69.43
70.65
70.35
68.04
69.59
67.64
67.97
66.44
70.16
724
Trail 4
70.62
65.53
71.42
70.78
69.56
65.77
70.78
68.88
65.53
66.23
71.96
57
Trail 5
67.00
70.35
69.59
65.05
67.17
65.34
70.65
70.35
69.16
68.31
70.16
724
Table 13:
Experimental Results on NAS-Bench-201 with
ImageNet16-120
. We set Temperature = 0 for GPT-4 in this experiment. T is the iteration. We perform GENIUS on the validation set and report the final accuracy and ranking on the test set based on the best architectures verified on the validation set.
T = 0
T = 1
T = 2
T = 3
T = 4
T = 5
T = 6
T = 7
T = 8
T = 9
Test Acc
Ranking
Trial 1
44.78
45.25
44.17
46.40
46.27
46.32
44.20
42.77
44.67
43.96
46.67
8
Trial 2
43.47
43.85
45.57
45.13
44.83
40.08
45.23
40.24
45.27
43.15
45.51
135
Trial 3
36.92
43.95
38.06
44.23
39.87
40.23
43.87
42.00
38.38
43.53
44.00
813
Trial 4
42.64
40.77
38.73
44.48
44.29
39.96
43.23
44.11
39.96
44.39
43.96
850
Trial 5
45.75
43.95
42.00
40.23
43.27
43.03
39.667
43.95
42.00
43.60
44.65
434
Appendix B
ImageNet
B.1
MobileNetV2 Search Space
Table 14:
The "Num Blocks" represents the maximum number of blocks in a group. The "Stride" indicates the convolutional stride of the first block in each group.
Input Shape
Operators
Channels
Num Blocks
Stride
224
2
×
3
224^{2}\times 3
3
×
3
3\times 3
Conv
16
1
2
112
2
×
16
112^{2}\times 16
3
×
3
3\times 3
Depthwise & Pointwise Conv
16
1
2
56
2
×
16
56^{2}\times 16
Choice Block
24
6
2
28
2
×
24
28^{2}\times 24
Choice Block
40
6
2
14
2
×
40
14^{2}\times 40
Choice Block
80
6
1
14
2
×
80
14^{2}\times 80
Choice Block
96
6
2
7
2
×
96
7^{2}\times 96
Choice Block
192
6
1
7
2
×
192
7^{2}\times 192
1
×
1
1\times 1
Conv
320
1
1
7
2
×
320
7^{2}\times 320
Global Avg. Pooling
320
1
1
320
320
1
×
1
1\times 1
Conv
1,280
1
1
1,280
1,280
Fully Connect
1,000
1
-
B.2
Architecture Details
GENIUS - 329
⬇
1
#
Input
56
x
56
x
16
2
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
3
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
4
5
#
Input
28
x
28
x
24
6
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
7
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
8
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
9
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
10
11
#
Input
14
x
14
x
40
12
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
13
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
14
InvertedResidual
(
kernel_size
=7,
exp_ratio
=4)
15
16
#
Input
14
x
14
x
80
17
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
18
InvertedResidual
(
kernel_size
=7,
exp_ratio
=4)
19
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
20
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
21
22
#
Input
7
x
7
x
96
23
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
24
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
25
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
26
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
GENIUS - 401
⬇
1
#
Input
56
x
56
x
16
2
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
3
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
4
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
5
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
6
7
#
Input
28
x
28
x
24
8
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
9
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
10
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
11
InvertedResidual
(
kernel_size
=3,
exp_ratio
=4)
12
13
#
Input
14
x
14
x
40
14
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
15
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
16
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
17
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
18
19
#
Input
14
x
14
x
80
20
InvertedResidual
(
kernel_size
=3,
exp_ratio
=6)
21
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
22
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
23
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
24
25
#
Input
7
x
7
x
96
26
InvertedResidual
(
kernel_size
=7,
exp_ratio
=6)
27
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)
28
InvertedResidual
(
kernel_size
=7,
exp_ratio
=6)
29
InvertedResidual
(
kernel_size
=5,
exp_ratio
=6)