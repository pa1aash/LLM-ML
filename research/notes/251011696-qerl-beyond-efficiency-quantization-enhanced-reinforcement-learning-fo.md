---
title: '[2510.11696] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement
  Learning for LLMs'
id: 251011696-qerl-beyond-efficiency-quantization-enhanced-reinforcement-learning-fo
tags:
- llm-nas-feedback-positioning-7125b1
- quantization-diversity
- adversarial-evidence
- nf4-quantization
created: '2026-08-16T16:51:00.455827Z'
updated: '2026-08-16T16:54:11.535191Z'
source: https://arxiv.org/abs/2510.11696
source_domain: arxiv.org
fetched_at: '2026-08-16T16:51:00.455479Z'
fetch_provider: builtin
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'NVIDIA/MIT paper proposing QeRL, an RL fine-tuning framework that combines
  NVFP4/MXFP4/NF4 4-bit quantization with LoRA to accelerate rollouts. Central adversarial-direction
  finding for the quantization-diversity gap: quantization noise increases the model''s
  SAMPLING/POLICY ENTROPY during RL training and deployment (measured as H(pi(.|q))
  over the vocabulary), which the authors interpret as an implicit exploration mechanism
  analogous to explicit parameter-noise injection -- 4-bit quantized Qwen2.5-7B-Instruct
  shows relatively higher entropy than its 16-bit counterpart and converges faster
  in GRPO/DAPO training. IMPORTANT SCOPE CAVEAT: this entropy effect is characterized
  during RL exploration/training dynamics on math reasoning tasks (GSM8K, MATH500),
  not as a study of zero-shot text-generation diversity (lexical/semantic diversity
  of final outputs); the paper explicitly contrasts its finding with prior SFT literature
  (Dettmers et al. 2023 QLoRA; Guo et al. 2023) showing quantization DEGRADES training
  effectiveness in supervised fine-tuning, i.e., the entropy-boost is RL-specific.
  Also notes NF4 specifically underperforms NVFP4/MXFP4 in reward growth speed, and
  that NF4-based QLoRA slows rollout speed by 1.5-2x due to lookup-table dequantization
  overhead.'
---

[2510.11696] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Machine Learning
arXiv:2510.11696
(cs)
[Submitted on 13 Oct 2025]
Title:
QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
Authors:
Wei Huang
,
Yi Ge
,
Shuai Yang
,
Yicheng Xiao
,
Huizi Mao
,
Yujun Lin
,
Hanrong Ye
,
Sifei Liu
,
Ka Chun Cheung
,
Hongxu Yin
,
Yao Lu
,
Xiaojuan Qi
,
Song Han
,
Yukang Chen
View a PDF of the paper titled QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs, by Wei Huang and 13 other authors
View PDF
HTML (experimental)
Abstract:
We propose QeRL, a Quantization-enhanced Reinforcement Learning framework for large language models (LLMs). While RL is essential for LLMs' reasoning capabilities, it is resource-intensive, requiring substantial GPU memory and long rollout durations. QeRL addresses these issues by combining NVFP4 quantization with Low-Rank Adaptation (LoRA), accelerating rollout phase of RL while reducing memory overhead. Beyond efficiency, our findings show that quantization noise increases policy entropy, enhancing exploration, and enabling the discovery of better strategies during RL. To further optimize exploration, QeRL introduces an Adaptive Quantization Noise (AQN) mechanism, which dynamically adjusts noise during training. Experiments demonstrate that QeRL delivers over 1.5 times speedup in the rollout phase. Moreover, this is the first framework to enable RL training of a 32B LLM on a single H100 80GB GPU, while delivering overall speedups for RL training. It also achieves faster reward growth and higher final accuracy than 16-bit LoRA and QLoRA, while matching the performance of full-parameter fine-tuning on mathematical benchmarks such as GSM8K (90.8%) and MATH 500 (77.4%) in the 7B model. These results establish QeRL as an efficient and effective framework for RL training in LLMs.
Comments:
Code is available at
this https URL
Subjects:
Machine Learning (cs.LG)
; Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2510.11696
[cs.LG]
(or
arXiv:2510.11696v1
[cs.LG]
for this version)
https://doi.org/10.48550/arXiv.2510.11696
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Wei Huang [
view email
]
[v1]
Mon, 13 Oct 2025 17:55:09 UTC (1,536 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs, by Wei Huang and 13 other authors
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
2025-10
Change to browse by:
cs
cs.CL
cs.CV
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

QERL:
BEYOND EFFICIENCY – QUANTIZATION-
ENHANCED REINFORCEMENT LEARNING FOR LLMS
Wei Huang1,3
Yi Ge2,4
Shuai Yang1
Yicheng Xiao4
Huizi Mao1
Yujun Lin1
Hanrong Ye1
Sifei Liu1
Ka Chun Cheung1
Hongxu Yin1
Yao Lu1
Xiaojuan Qi3
Song Han1,2
Yukang Chen1
1NVIDIA
2MIT
3HKU
4THU
https://github.com/NVlabs/QeRL
ABSTRACT
We propose QeRL, a Quantization-enhanced Reinforcement Learning framework
for large language models (LLMs). While RL is essential for LLMs’ reasoning
capabilities, it is resource-intensive, requiring substantial GPU memory and long
rollout durations. QeRL addresses these issues by combining NVFP4 quantiza-
tion with Low-Rank Adaptation (LoRA), accelerating rollout phase of RL while
reducing memory overhead. Beyond efficiency, our findings show that quanti-
zation noise increases policy entropy, enhancing exploration, and enabling the
discovery of better strategies during RL. To further optimize exploration, QeRL
introduces an Adaptive Quantization Noise (AQN) mechanism, which dynami-
cally adjusts noise during training. Experiments demonstrate that QeRL delivers
over 1.5× speedup in the rollout phase. Moreover, this is the first framework to
enable RL training of a 32B LLM on a single H100 80GB GPU, while delivering
overall speedups for RL training. It also achieves faster reward growth and higher
final accuracy than 16-bit LoRA and QLoRA, while matching the performance of
full-parameter fine-tuning on mathematical benchmarks such as GSM8K (90.8%)
and MATH 500 (77.4%) in the 7B model. These results establish QeRL as an
efficient and effective framework for RL training in LLMs.
Figure 1: Rollout speedup and accuracy of QeRL on Qwen2.5-7B-Instruct. QeRL achieves faster
RL rollout and end-to-end training speeds (batch=8), while delivering performance superior to
vanilla LoRA and QLoRA, also comparable to full-parameter RL on mathematical benchmarks.
1
INTRODUCTION
The ability to perform multi-step reasoning is critical for large language models (LLMs) to handle
complex tasks, from theoretical problem solving to practical decision making (Sui et al., 2025;
Xu et al., 2025; Chu et al., 2025; Yang et al., 2021). Supervised fine-tuning (SFT) is a common
method to improve reasoning by training models to replicate explicit reasoning steps (Huang et al.,
2024d; Min et al., 2024). However, this approach risks promoting imitation rather than encouraging
genuine reasoning. In contrast, reinforcement learning (RL) uses verifiable reward signals to support
adaptive learning, allowing models to explore diverse reasoning traces and identify more robust
solutions (Lambert et al., 2024; DeepSeek-AI, 2025; Chen et al., 2025a).
1
arXiv:2510.11696v1  [cs.LG]  13 Oct 2025
a
Steps
Reward
𝝈𝟏
…
Channel
4-bit
𝐒𝐄𝟑𝐌𝟒
𝐒𝐅𝐏𝟏𝟔
𝝈𝟏
𝝈𝟐
𝝈𝟑
…
…
…
…
Quantization Noise
𝝈𝟑
𝝈𝟐
𝝈𝟏
𝐙𝐧𝐨𝐢𝐬𝐞- Adaptive Quantization Noise
Training Steps
LLM
4-bit
LoRA
🔥
Rollouts
Logits
16-bit
Gradients
16-bit
Rewards
LLM
4-bit
🔥
LoRA
LLM
4-bit
LoRA
🔥
Rollouts
Gradients
16-bit
Rewards
LLM
4-bit
LoRA
🔥
Logits
16-bit
(b) RL via QLoRA
𝐙𝐧𝐨𝐢𝐬𝐞
(c) QeRL
LLM
16-bit
LoRA
🔥
Rollouts
Logits
16-bit
Gradients
16-bit
Rewards
LLM
16-bit
🔥
LoRA
(a) RL via LoRA
Noise Std (𝜎)
𝝈𝟐
𝝈𝟑
𝝈𝟒
𝝈𝟎
Noise Scheduler
Figure 2: The illustration of QeRL. (a) RL via LoRA: reducing trainable parameters, but does
not alleviate the rollout bottleneck. (b) RL via QLoRA: NF4 quantization with LoRA, but NF4
is slower than LoRA. (c) QeRL: NVFP4 quantization with LoRA, reducing memory and enabling
faster RL while matching full-parameter finetuning performance with adaptive quantization noise.
AQN dynamically adjusts quantization noise with an exponential scheduler, enhancing exploration.
RL is effective for LLMs’ reasoning but highly resource-intensive. RL requires substantial GPU
memory, as multiple models, such as policy and reference models in GRPO (Shao et al., 2024),
must run concurrently. The large size of reasoning-focused LLMs (DeepSeek-AI, 2025) further ex-
acerbates memory demands. Training is also slowed by multistage processes, including rollouts,
reward computation, logit evaluation, and gradient updates. Rollouts are particularly costly, in-
volving repeated sampling and processing of long sequences for complex tasks (Yu et al., 2025).
Additionally, RL’s inherent sample inefficiency (Hassani et al., 2024) further increases costs.
Improving RL efficiency in LLMs presents significant challenges. One approach, exemplified by
Tina (Wang et al., 2025), leverages parameter-efficient fine-tuning methods like Low-Rank Adap-
tation (LoRA) (Hu et al., 2022) to reduce trainable parameters.
However, similar to LoRA in
SFT (Chen et al., 2024b), these methods fail to address the core issue of slow rollout speeds. An-
other strategy, demonstrated by FlashRL (Liu et al., 2025a), uses quantized rollout models to reduce
computational costs. However, precision mismatches between the rollout model and logits model
(e.g., 8-bit vs. 16-bit) require importance sampling to correct discrepancies, necessitating both 8-bit
and 16-bit models to run simultaneously, which increases memory usage. To overcome these limita-
tions, we focus on lower-bit quantization while avoiding duplicate models in memory. Additionally,
using QLoRA (Dettmers et al., 2023a) in RL slows rollouts by 1.5–2×, further reducing efficiency.
This slowdown occurs because QLoRA relies on NormalFloat 4-bit (NF4) precision, which requires
unpacking and mapping to floating-point values via a lookup table before matrix multiplication.
To address the limitations of NF4 in QLoRA, a natural solution is to adopt higher-performance quan-
tization. However, standard quantization methods introduce static and deterministic noise, which is
non-beneficial to the later-stage RL training. To avoid this drawback, our analysis surprisingly
reveals that quantization noise, with precise control, can benefit RL by increasing policy entropy
(Fig.3). This added entropy enhances exploration by introducing uncertainty, similar to the effect
of parameter noise in RL (Plappert et al., 2017; Pang & Jiang, 2021), and helps models discover
better strategies (Cui et al., 2025). Our experiments show that a well-designed noise strategy al-
lows quantized LLMs to exploit this effect, reducing memory overhead while gaining better reward
curves. This finding contrasts with results from SFT of LLMs (Dettmers et al., 2023a; Guo et al.,
2023), demonstrating that controllable quantization noise in RL enhances exploration and enables
quantized frameworks to surpass 16-bit LoRA in both efficiency and performance.
We propose QeRL, a quantization-based RL framework designed to train LLMs on reasoning tasks.
As shown in Fig.2, QeRL uses NVFP4 quantization for LLM weights and integrates a Marlin-
based (Frantar et al., 2024) approach in both rollout and prefilling stages. This design accelerates
rollout and prefilling without sacrificing accuracy, with gradient backpropagation enabled through
LoRA layers. To address static quantization noise, we introduce adaptive quantization noise (AQN),
2
𝐎𝐭
w Quantization 
Vocabulary Size
Prob Distribution 
𝐎𝐭
w/o Quantization 
Vocabulary Size
Prob Distribution 
High Entropy
Low Entropy
Quantization
+ LoRA
16bit + LoRA
Accuracy Reward
Training Steps
Training Steps
16bit + LoRA
Quantization
+ LoRA
Loss
Better
Better
Reinforcement Learning
Supervised Finetuning
More Exploration
Figure 3: Advancement of Quantization in RL Exploration. Quantization noise brings higher ini-
tialized entropy, which encourages exploration in RL training, accelerating the increase of reward.
which injects channel-wise random noise during training and adjusts exploration noise dynamically
using an exponential schedule. Additionally, we implement a noise-sharing strategy that merges the
noise vector into the layer normalization layer, enabling zero-parameter overhead for noise injection.
Compared to vanilla LoRA, QeRL achieves faster rollout and better reward growth. For example, as
shown in Fig.1, QeRL outperforms QLoRA and vanilla LoRA in rollout and prefilling speeds on the
Qwen2.5-7B-Instruct model, achieving a GSM8K score of 90.8—surpassing both 16-bit LoRA and
QLoRA while matching full fine-tuning accuracy on MATH 500. QeRL outperforms vanilla LoRA
and QLoRA in both training speed and reward performance. Notably, it achieves approximately a
1.8× speedup in end-to-end training, compared to QLoRA. Additionally, QeRL demonstrates the
capability to train a 32B model with GRPO on a single H100 80GB GPU.
2
PRELIMINARY
Model Quantization
Integer quantization requires mapping float-point weights distributed within
the interval [Wmin, Wmax] to an integer range of 2N, where N is the target bit-width. Given a
tensor W ∈Rd×k, this process is defined as:
˜
W = Round(W
sw
), sw = Wmax −Wmin
qmax
(1)
where ˜
W represents the quantized weight matrix, sW is the scaling factor, and qmax defines the
compressed range. For integer quantization, qmax = 2N −1. In contrast, for the floating-point
quantization, such as FP4 format, qmax = 6, achieved using a 1-bit mantissa and a 2-bit exponent
(E2M1). 4-bit NormalFloat (NF4) is a new data type (Dettmers et al., 2023a), designed for normally
distributed weights. Recently, the latest Blackwell GPU architecture (NVIDIA, 2024) introduces
hardware support for the advanced FP4 format, MXFP4 (Project, 2023) and NVFP4 (NVIDIA,
2024). MXFP4 adopts a shared FP8 (E8M0) scaling factor across parameter blocks of 32 elements,
while NVFP4 employs an FP8 (E4M3) scaling factor with smaller parameter blocks of 16 elements,
enabling finer-grained scaling adjustments compared to MXFP4. Both formats are seamlessly inte-
grated into NVIDIA’s Hopper (NVIDIA, 2023) and Blackwell (NVIDIA, 2024) GPUs.
Low-rank Adaptation
LoRA (Hu et al., 2022) is motivated by the observation that weight updates
in large pre-trained models often lie in a low-dimensional subspace. Instead of directly fine-tuning
all parameters, LoRA introduces a low-rank decomposition to model these updates efficiently:
W + ∆W = W + BA
(2)
where B ∈Rd×r and A ∈Rr×k, with the rank r ≪min(d, k). In this setup, the original weight
matrix W is kept frozen, and only the low-rank matrices A and B are optimized during training.
This formulation drastically reduces the number of trainable parameters and lowers both memory
and computational cost, while retaining the expressivity required for domain adaptation. Within self-
attention modules, LoRA is generally applied to the attention and feed-forward projection matrices
(Wq, Wk, Wv, Wo, Wgate, Wup, Wdown), as these layers are the most critical in LLMs. Other
related works are discussed in Appendix D.
3
METHOD
Our experiments reveal that quantized LLMs can significantly enhance exploration in RL. Applying
parameter-efficient fine-tuning (PEFT) to quantized models not only reduces training resource con-
sumption but also outperforms vanilla LoRA in reward growth and evaluation scores (Fig.2). This
3
challenges the conventional view in SFT that quantization degrades training effectiveness(Dettmers
et al., 2023a; Guo et al., 2023). Notably, we observe that quantization error functions similarly to
random noise in networks (Plappert et al., 2017; Eberhard et al., 2023; Osband et al., 2016), promot-
ing broader exploration of potential actions or tokens in RL by increasing entropy (Fig.3).
3.1
TRAINING FRAMEWORK OF QERL
QeRL is based on the mainstream policy optimization algorithms of LLMs, such as GRPO (Shao
et al., 2024) and DAPO (Yu et al., 2025).
Group Relative Policy Optimization (Shao et al., 2024) is designed based on the Generalized
Advantage Estimation (GAE) (Schulman et al., 2015), eliminating the need for a separately trained
reward model, as required in Proximal Policy Optimization (PPO) (Engstrom et al., 2019; Schulman
et al., 2017). Instead, for a given input query q, multiple samples are generated, resulting in a set
of candidate outputs {o1, o2, ..., oG}. These candidates are evaluated using a rule-based reward, and
the average reward is used for updates. The optimization objective is defined as follows:
J (θ) = Eq,{oi}[ 1
G
G
X
i=1
1
|oi|
|oi|
X
t=1
(min( πθ(oi,t|q)
πθold(oi,t|q)Ai,t, clip( πθ(oi,t|q)
πθold(oi,t|q), 1 −α, 1 + α)Ai,t)
−βDKL(πθ||πref))] (3)
where πθ and πref denote the policy model and reference model, respectively, and the clipping range
(1 −α, 1 + α) stabilized the gradient steps of the policy model. KL penalty is used in GRPO to
avoid the unexpected large change in updating (Schulman et al., 2017). Ai,i is the antagonist of ith
completion, shared across all tokens in ot, defined as:
Ai = ri −mean({r1, r2, ..., rG})
std({r1, r2, ..., rG})
(4)
Dynamic Sampling Policy Optimization (Yu et al., 2025) suggests higher clipping upper-bond can
help avoid entropy collapse. Another improvement in DAPO is to utilize the loss of token-level
policy gradients. In DAPO, the KL penalty from Eq.3 is removed to eliminate the upper limit on
exploration in RL, thereby encouraging more optional tokens in the rollout process.
3.2
QUANTIZATION ENCOURAGES EXPLORATION
To understand how quantization enhances RL, we analyze its effect on the model’s sampling behav-
ior. Our central finding is that the noise introduced by quantization serves as an implicit exploration
mechanism, similar to explicit noise injection techniques in the parameter and action space (Plappert
et al., 2017; Eberhard et al., 2023; Fortunato et al., 2018; Liu et al., 2025b).
Quantization
Improves
Sampling
Entropy
We
study
3
different
quantization
for-
mats
of
FP4
(NVPF4,
MXFP4,
and
NF4)
on
GSM8K
(Cobbe
et
al.,
2021).
0.1
0.15
0.2
0.25
0.3
0
50
100
150
200
NVFP4-LoRA(r32)
NF4-LoRA(r32)
MXFP4-LoRA(r32)
Float16-LoRA(r32)
Entropy
Training Steps
Relatively High 
Entropy
Figure 5: Comparison of RL entropy.
Our empirical study on Qwen2.5-7B-Instruct (Team,
2024) reveals an intriguing finding: when applying PEFT-
based RL, models quantized to 4-bit precision consis-
tently outperform their 16-bit counterparts. This advan-
tage is evident across two key metrics: significantly faster
reward convergence during training and higher adjusted
evaluation scores. As shown in Fig.4, the reward curves
of the models exhibit a steeper upward trend compared to
16-bit models, with convergence patterns closely resem-
bling those of full-parameter fine-tuning in both DAPO
and GRPO. Also, NVFP4 and MXFP4 both show better
reward growth than NF4.
This unexpected performance improvement prompted us to investigate the underlying mecha-
nism.
We discover that quantization inherently increases the sampling entropy, H(π(|q)) =
−P
ot∈V π(ot|q) log π(ot|q), where V is the vocabulary) of the policy during deployment (shown
in Fig.5). During the forward pass, a quantized model introduces small but systematic errors, which
4
0
50
100
150
200
NVFP4-LoRA(r32)
MXFP4-LoRA(r32)
NF4-LoRA(r32)
0
50
100
150
200
MXFP4-LoRA(r32)
Float16-LoRA(r32)
Float16-Full
Training Steps
0.15
0.35
0.55
0.75
0.95
0
50
100
150
200
NVFP4-LoRA(r32)
Float16-LoRA(r32)
Float16-Full
Accuracy Reward
Training Steps
Training Steps
DAPO
NVFP4
MXFP4
NF4
0.15
0.35
0.55
0.75
0.95
0
50
100
150
200
NVFP4-LoRA(r32)
Float16-LoRA(r32)
Float16-Full
Accuracy Reward
0
50
100
150
200
MXFP4-LoRA(r32)
Float16-LoRA(r32)
Float16-Full
0
50
100
150
200
NVFP4-LoRA(r32)
MXFP4-LoRA(r32)
NF4-LoRA(r32)
Training Steps
Training Steps
Training Steps
GRPO
NVFP4
MXFP4
NF4
Figure 4: Training reward performance. The upper figures illustrate the training rewards under
DAPO, while the lower one is GRPO. Although MXFP4 achieves higher scores in the early stages
of training, NVFP4 ultimately converges to better final rewards. LoRA rank is set to 32.
can be modeled as static network noise (Fan et al., 2020). This noise propagates across the network
layers, perturbing the final logits before the softmax function is applied. Consequently, the output
probability distribution over the vocabulary, denoted as πθ(|q), becomes ”flatter,” with less pro-
nounced peaks. This increase in sampling entropy plays a crucial role in reinforcement learning by
encouraging exploration (Cheng et al., 2025; Eysenbach & Levine, 2021). It mitigates the model’s
overconfidence in a single ”optimal” token and instead assigns more meaningful probabilities to a
wider range of plausible next actions (Fig.3). The entropy of other model is provided in Appendix H.
Quantization Noise Functionally, this effect resembles exploration in parameters (Eberhard et al.,
2023; Plappert et al., 2017), which deliberately injects noise into parameters to drive exploration:
(˜θ + θlora) −(θ + θlora) = Q(θ) −θ = ∆ϵ
(5)
where Q(θ) denotes the de-quantized weight, and ∆ϵ is the quantization noise. Such exploratory
noise emerges naturally as a computationally “free” byproduct of compressing model representa-
tions. This contrasts starkly with SFT, where noise is often detrimental because the objective is to
faithfully imitate the true data distribution rather than to discover novel high-reward outputs.
A key limitation of quantization errors is their deterministic nature, which fails to align with the
dynamic exploration-exploitation trade-off required in RL. Unlike stochastic noise in traditional
RL (Plappert et al., 2017; Osband et al., 2016), which is randomly sampled and independently
applied at different training stages, quantization noise remains static throughout the process, lacking
the adaptability needed to enhance exploration at critical phases.
3.3
ADAPTIVE QUANTIZATION NOISE IN PARAMETER SPACE
To transform static quantization noise into a dynamic exploration mechanism, we introduce an Adap-
tive Quantization Noise (AQN) technique. The core idea is to introduce a small set of structured
modulation vectors that slightly perturb the otherwise static quantization noise. In our approach, we
utilize an advanced quantization format, NVFP4.
NVFP4 Quantization NVFP4 represents weights using a dual-scaling mechanism: a coarse, per-
tensor global scaling factor in FP32, SFP32, and a fine-grained tensor of block-wise FP8 (E4M3)
scalers, SE4M3. The dequantization of a 4-bit ˜
W to the high-precision ˆ
W follows:
ˆ
W = Dequant( ˜
W) = SFP32 · (SE4M3 ⊙˜
W)
(6)
5
where ⊙denotes block-wise scalar multiplication, broadcasting each scaler in SE4M3 to its corre-
sponding block of 4-bit weights in ˜
W. The quantization noise of each weight matrix, ∆ϵ = ˆ
W−W,
is the difference between this reconstructed tensor and the original full-precision tensor W.
Adaptive Quantization Noise We introduce a noise vector to the static quantized weight. Specifi-
cally, for each quantized linear layer, we sample a stochastic noise vector, Znoisy ∈R1×d, where d
is the input dimension of the layer. This vector is not fixed but is resampled for each forward pass.
We define it as: Znoisy = ϵ, ϵ ∼N(0, σ2I), where σ is a hyperparameter in different training stage
governing the noise scale, and ϵ is a random vector whose elements are drawn independently from
a standard Gaussian distribution (Plappert et al., 2017). Then the additive noise is defined as:
∆ϵ′ = Znoisy + ∆ϵ = Znoisy +

ˆ
W −W

(7)
where ∆ϵ′ is equivalent to the dynamic noise of each weight matrix. In our setting, we freeze the
main branch weight and update the low-rank matrix during RL. The W and ˆ
W are consistent values.
In the early stages, we leverage the inherent quantization noise to enhance the model’s exploration
capabilities. As training progresses, σ gradually reduces following an exponential decay scheduler:
σ(k) = σstart ·
 σend
σstart
 k−1
K−1
(8)
where σstart and σend represent the initial and final noise levels, k is the current stage, and K is the
total interval, which are evenly divided in the training steps (more scheduler comparison in Sec.4.2).
For instance, our experiments in GSM8K with a total of around 600 training steps, noise is injected at
10 evenly spaced intervals, initialized with quantization noise, then from σstart to σend. This approach
aims to balance exploration and exploitation (Fox et al., 2015).
Q
NVFP4
K
NVFP4
V
NVFP4
RMSNorm
Multi-Head Self-Attention 
𝒁!"#$% + 𝒘
𝐙!"#$%
+
Activation
Merged
Gate
NVFP4
Up
NVFP4
RMSNorm
Feedforward Layer
𝐙!"#$%
𝐙!"#$%
𝐙!"#$%
𝐙!"#$%
+
𝒁!"#$% + 𝒘
Activation
Merged
Down
NVFP4
Figure 6: Deployment scheme of adaptive quanti-
zation noise in LLMs. Znoise is integrated in Lay-
erNorm (e.g., RMSNorm) of each block in LLMs.
Noise Merging While introducing a noise vec-
tor enables dynamic control over quantization
noise, explicitly creating a separate vector for
each quantized layer is not feasible. First, it
imposes a burden on parameter efficiency, in-
creasing memory overhead.
Moreover, high-
precision noise cannot be directly added to
quantized weights, as this would break the com-
patibility of our inference kernel designed for
NVFP4 × BF16 operations. We propose a sim-
ple solution that integrates this noise vector di-
rectly into the layer normalization parameters
of LLM architectures.
X

Znoisy + ˆ
W

= X · Znoisy + X · ˆ
W
(9)
By exploiting this equivalency in Eq.9, we subsume the role of Znoisy into the learnable weight
parameter of the LayerNorm operation (e.g. RMSNorm (Zhang & Sennrich, 2019)) that typically
follows the scaling after normalization.
RMSNormnoise(x) = wnoise ⊙
x
q
1
N
PN
i=1 x2
i + δ
, wnoise = Znoise + w
(10)
where w represents the scaling factor of RMSNorm. In this configuration, channel-wise additive
noise Znoisy transfers to row-wise multiplicative noise Znoise
w
+ I of weight (proof provided in Ap-
pendix G). Multiplicative noise has been shown to be effective in RL (Pang & Jiang, 2021; Zhang
et al., 2025a). Due to the higher sensitivity of RL to multiplicative noise, we initialize the noise level
with σstart = 1e-2 to ensure stability.
This approach extends adaptive quantization noise to the layer parameters Wq, Wk, Wv, Wgate,
and Wup within each block, as these layers directly interact with normalized activations. To align
with LLM architectures (Team, 2024; Grattafiori et al., 2024), Wq, Wk, and Wv share the same
RMSNorm, while Wgate and Wup share another (as shown in Fig.6).
6
(a) Performance of Qwen2.5-3B-Instruct.
Model
W#
Training
GSM8K
Qwen2.5-3B
-Instruct
BF16
61.2
NF4
-
57.5−3.7
MXFP4
-
59.8−1.4
NVFP4
-
59.4−1.8
BF16
Full
84.4+23.2
BF16
LoRA
76.1+14.9
NF4
LoRA
76.1+14.9
MXFP4
LoRA
73.4+12.2
NVFP4
LoRA
83.3+22.2
+AQN
83.7+22.6
(b) Performance of Qwen2.5-7B-Instruct.
Model
W#
Training
GSM8K
Qwen2.5-7B
-Instruct
BF16
-
76.3
NF4
-
70.5−5.8
MXFP4
-
71.3−5.0
NVFP4
-
73.4−2.9
BF16
Full
91.2+14.9
BF16
LoRA
88.1+11.8
NF4
LoRA
85.0+8.7
MXFP4
LoRA
86.4+10.1
NVFP4
LoRA
88.5+12.2
+AQN
90.8+13.5
Table 1: Qwen2.5 Performance on GSM8K. GRPO algorithm is used to train 3B and 7B models on
GSM8K dataset, while “Full” denotes the full-parameter training and “W#” represents the bit-width
and data format of weight. + and - are compared with original bfloat-16 (BF16) models.
0
0.2
0.4
0.6
0
50
100 150 200 250
Float16-Full
QeRL
LoRA
Accuracy Reward
Training Steps
Qwen2.5 7B
Qwen2.5 14B
0
0.2
0.4
0.6
0
50
100 150 200 250
Float16-Full
QeRL
LoRA
Training Steps
Figure 7: Training reward of 7/14B models.
0.25
0.45
0.65
0.85
0
20
40
60
80
w AQN
w/o AQN
0.05
0.2
0.35
0.5
0
50
100
150
200
250
w AQN
w/o AQN
Accuracy Reward
𝐙noise
𝟏
𝐙noise
𝟐
𝐙noise
𝟑
𝐙noise
𝟏
Qwen2.5 3B
Qwen2.5 7B
Training Steps
Training Steps
Figure 8: Ablation of AQN on 3/7B model.
4
EXPERIMENT
4.1
EXPERIMENT SETTINGS
RL Training We conducted training experiments using DAPO (Yu et al., 2025) and GRPO (Shao
et al., 2024) on two prominent mathematical reasoning datasets: GSM8K (Cobbe et al., 2021) and
BigMath (Albalak et al., 2025). GSM8K comprises 7,500 samples with a generation number of 8,
while BigMath includes 122,000 samples with a generation number of 16. Both datasets feature
problems of medium to high difficulty, spanning levels 3 to 5. For GSM8K, we trained 3B and 7B
models, whereas for BigMath, we trained 7B, 14B, and 32B models. Specifically, the 7B and 14B
models were trained on problems ranging from levels 3 to 5, while the 32B model was exclusively
trained on the more challenging level 4–5 problems. Training checkpoints were evaluated between
500 and 1000 steps. To account for the sensitivity of Znoise perturbation, we set its range from 5e-2
to 5e-4 for dynamic noise estimation. In the main experiments, the LoRA rank is fixed at 32. The
speedup tests are performed on a single H100 GPU, while the final evaluated model is trained using
8 H100 GPUs to ensure experimental efficiency on such large-scale data. Detailed hyperparameters
and deployment of QeRL are provided in Appendix E and Appendix F.
Backbone Models We conduct experiments on Qwen2.5 (Team, 2024) series, using basic without
any mathematic data fine-tuning. For weight-only quantization, we applied AWQ (Lin et al., 2024)
to MXFP4 and NVFP4 formats. The calibration dataset included 256 sequences, each 2048 tokens
long, sampled from OpenThoughts-114k (Guha et al., 2025). Weight-only formats also support
inference acceleration on NVIDIA-H100 GPUs with the Marlin kernel (Frantar et al., 2024). For
NF4 quantization, we used the default configuration (Dettmers et al., 2023a).
Evaluation Benchmarks and Metrics We focus on several widely used mathematical reasoning
benchmarks, including GSM8K (Cobbe et al., 2021), MATH500 (Lightman et al., 2023), AIME
2024/2025 (Li et al., 2024), and AMC 23 (Li et al., 2024), for evaluation. During inference, we use
a temperature of 0.6, completion length of 4096, and top-p sampling with p = 0.95. Each data set
is evaluated multiple times, and we report primarily the average accuracy of one sample (Pass@1).
7
Model
W#
Training
MATH 500
AIME 24
AIME 25
AMC 23
Average↑
7B
BF16
-
74.8
9.2
6.6
25.0
28.9
NVFP4
-
73.7−1.3
8.3−0.9
3.3−3.3
17.5−7.5
25.7−3.2
BF16
Full
77.4+2.6
16.7+7.5
10.0+3.4
45.0+20.0
37.3+8.4
BF16
LoRA
77.0+2.2
13.3+4.1
10.0+3.4
42.5+17.5
35.7+6.8
NVFP4
LoRA
76.8+2.0
13.7+4.5
10.0+3.4
47.5+22.5
37.0+8.1
+AQN
77.4+2.6
15.5+6.3
10.0+3.4
42.5+17.5
36.4+7.5
14B
BF16
-
78.6
11.3
9.2
45.0
36.0
NVFP4
-
76.4−2.2
11.2−0.1
8.3−0.9
40.0−5.0
34.0−2.0
BF16
Full
83.2+4.6
20.0+8.7
15.1+5.9
55.0+10.0
43.3+7.3
BF16
LoRA
81.0+2.4
14.0+3.7
13.3+4.1
52.5+7.5
40.2+4.2
NVFP4
LoRA
79.4+0.8
16.7+5.4
13.3+4.1
52.5+7.5
40.5+4.5
+AQN
80.2+1.6
17.5+6.2
12.6+3.4
57.5+12.5
42.0+6.0
32B
BF16
-
81.4
14.0
10.8
52.5
39.7
NVFP4
-
80.6−0.8
11.3−2.7
10.0−0.8
45.0−7.5
36.7−3.0
BF16
Full
84.0+2.6
20.0+6.0
23.3+12.5
57.5+5.0
46.2+6.5
BF16
LoRA
83.6+2.2
16.7+3.7
13.3+2.5
55.0+2.5
42.2+2.3
NVFP4
LoRA
81.6+0.2
16.7+3.7
15.0+4.2
52.5+0.0
41.4+1.7
+AQN
83.3+1.9
16.7+3.7
19.2+8.4
63.3+10.8
45.6+5.9
Table 2: Performance across four benchmarks. DAPO algorithm is used to train Qwen2.5-7/14/32B-
Instruction models on BigMath dataset, while “Full” denotes the full-parameter training.
0.25
0.4
0.55
0.7
0.85
0
50
100
150
Linear Decay
Exponential Decay
Cosine Decay
Logarithmic Decay
Accuracy Reward
Training Steps
Figure 9: Comparison of noise schedulers.
0.25
0.45
0.65
0.85
0
50
100
150
rank=16
rank=32
rank=64
rank=128
Training Steps
Accuracy Reward
Figure 10: Ablation of LoRA rank.
4.2
EXPERIMENT RESULTS
Reasoning Performance As shown in Tab.1, we report the GSM8k training results of the 3B and
7B models using GRPO. While quantized models exhibit performance degradation compared to
BF16, applying PEFT with RL to the 3B model demonstrates that NVFP4 combined with AQN
achieves a performance of 83.7 from 59.4, surpassing the 76.1 achieved by 16-bit PEFT training
and falling only 0.7 points below full-parameter training. Similarly, for the 7B model, our method
outperforms 16-bit LoRA by 1.7 points. Furthermore, compared to QLoRA, our approach improves
average accuracy by 7.6 and 5.8 points for the 3B and 7B models, respectively. Tab.2 presents
the results on the BigMath dataset for the 7B, 14B, and 32B models trained with DAPO. Across
all datasets, QeRL consistently matches or exceeds the performance of 16-bit models trained with
LoRA. Notably, QeRL trains only about 1% of the parameters required for full-parameter training
while using just 40%–50% of the GPU memory of vanilla LoRA. For the 7B model, QeRL improves
the average score from 25.7 (quantized) to 36.4, compared to 35.7 with vanilla LoRA. Similar trends
are observed in the 14B and 32B models, where QeRL consistently outperforms vanilla LoRA across
benchmarks, further supporting the conclusion that quantization enhances RL. Remarkably, on the
AMC 23 dataset, the 14B model with QeRL achieves 57.5, exceeding 55.0 of full-parameter training.
Reward Visualization In Sec.3.2, we compare the accuracy rewards of quantized LoRA, vanilla
LoRA, and full-parameter training under GRPO and DAPO. Fig.7 presents the accuracy reward
curves for the 7B and 14B models on the challenging BigMath dataset. Notably, QeRL achieves a
rapid reward increase within 200 steps, while vanilla LoRA requires over 500 steps (Appendix H) to
show improvement. This finding highlights that the inherent noise introduced by quantized LLMs
enhances exploration in RL, enabling faster reward growth and higher reward targets.
8
Model
Method
W#
Model Size
Training Speedup (Batch Size)
2
4
8
Qwen2.5-7B-Instruct
LoRA
BF16
15.2 GB
-
-
-
QLoRA
NF4
5.7 GB
×0.8 ↓
×0.8 ↓
×0.7 ↓
QeRL
NVFP4
5.9 GB
×1.5 ↑
×1.4 ↑
×1.2 ↑
Qwen2.5-14B-Instruct
LoRA
BF16
29.6 GB
-
-
-
QLoRA
NF4
10.2 GB
×0.9 ↓
×0.7 ↓
×0.7 ↓
QeRL
NVFP4
10.6 GB
×1.4 ↑
×1.2 ↑
×1.2 ↑
Table 3: Memory Saving and Speedup of 7B and 14B models. We report the end-to-end speedup
in the GRPO process of each training step. Each input has a length of 256 tokens, and each max
completion length is 2048. More results of other models are shown in Appendix J.
0
40
80
LoRA
QLoRA
QeRL
R=16
R=32
R=64
Qwen2.5-14B-Instruct
65.4
45.1
95.3
63.1
44.2
92.9
61.2
42.8
86.0
2.1×
2.1×
2.0×
Throughput (tokens/s)
20
40
60
LoRA
QLoRA
QeRL
R=16
R=32
R=64
Qwen2.5-32B-Instruct
Throughput (tokens/s)
34.0
25.2
58.0
33.3
25.6
56.0
31.9
51.3
2.3×
2.2×
2.2×
23.0
Figure 11: Rollout throughput of 14/32B model. The setting is aligned with Tab. 7 (batch is 1).
Noise Decay Schedule Fig.9 compares the performance of different noise decay functions for the 3B
model: linear, exponential, cosine, and logarithmic decay. While their performance differences are
negligible in the early training stages, exponential decay achieves more stable improvements later
by reducing noise to lower levels. The corresponding decay curves are provided in Appendix H.
Ablation of AQN Using default quantized noise throughout the training limits the exploration in
RL. To address this, we propose the AQN. As shown in Fig.8, when we start with the default quan-
tized noise and periodically inject additional noise in later stages, the reward curve grows more
steadily. Notably, when the reward approaches convergence, AQN effectively expands the model’s
exploration space, enabling further improvements in reward.
Ablation of LoRA Rank Fig.10 compares the reward curves of the 3B model during QeRL with
different LoRA ranks. Specifically, ranks of 16, 32, 64, and 128 exhibit similar trends and reward
growth rates, with rank 16 converging slightly faster, making it a more economical choice.
4.3
MEMORY SAVING AND SPEEDUP
Tab.3 compares the quantized model sizes and end-to-end RL training speedup of these PEFT meth-
ods, with all experiments conducted on a single NVIDIA H100-80GB GPU (NVIDIA, 2023). For
7B and 14B models, both QLoRA (NF4) and QeRL (NVFP4, supported by the Marlin kernel (Fran-
tar et al., 2024)) significantly reduce memory usage, shrinking the model sizes to 25%–30% of their
16-bit counterparts. Due to the limitations of NF4 generation speed (Egashira et al., 2024), QLoRA
slows to 0.7×–0.8× across different batch sizes. In contrast, QeRL achieves 1.2×–1.5× training
speedups over vanilla LoRA, benefiting from the generation speed of long reasoning sequences.
This efficiency is particularly evident in RL, where the computational demands of long-horizon roll-
outs emphasize QeRL’s advantage. Notably, our speedup measurements are based on the average
speed during the first 30 steps, where the output token length is relatively short. In later stages of
training, as the model generates longer outputs, the speed advantage of QeRL becomes even more
pronounced. Its dual benefits in memory efficiency and training speed make QeRL highly effective
for end-to-end RL workflows, especially in scenarios requiring extensive rollouts. Fig.11 shows
rollout performance across various LoRA ranks, with QeRL achieving over 2× speedups on 14B
and 32B models. More efficiency comparisons for other models and settings are in Appendix J.
9
5
CONCLUSION
This paper presents QeRL, an efficient training framework for RL on LLMs, which integrates
NVFP4 precision quantization with LoRA fine-tuning. The framework is based on the novel obser-
vation that quantization can enhance exploration during RL, contrary to findings in SFT. Quantized
LLMs not only surpass vanilla 16-bit LoRA training but also approach full-parameter fine-tuning
performance. To address the static nature of quantization noise, we introduce an AQN mechanism,
which dynamically adjusts noise during training to enhance RL stability. Extensive experiments
show that QeRL significantly improves accuracy across models of various sizes compared to both
16-bit LoRA and QLoRA. Additionally, with NVFP4 kernel support, QeRL achieves a round a 1.5×
speedup in end-to-end RL training while drastically reducing memory usage.
REFERENCES
Alon Albalak, Duy Phung, Nathan Lile, Rafael Rafailov, Kanishk Gandhi, Louis Castricato, Anikait
Singh, Chase Blagden, Violet Xiang, Dakota Mahan, et al. Big-math: A large-scale, high-quality
math dataset for reinforcement learning in language models. arXiv preprint arXiv:2502.17387,
2025.
Shengnan An, Yifei Li, Zeqi Lin, Qian Liu, Bei Chen, Qiang Fu, Weizhu Chen, Nanning Zheng, and
Jian-Guang Lou. Input-tuning: Adapting unfamiliar inputs to frozen pretrained models. CoRR,
abs/2203.03131, 2022.
Roberto L Castro, Andrei Panferov, Soroush Tabesh, Oliver Sieberling, Jiale Chen, Mahdi Nikdan,
Saleh Ashkboos, and Dan Alistarh. Quartet: Native fp4 training can be optimal for large language
models. arXiv preprint arXiv:2505.14669, 2025.
Mengzhao Chen, Wenqi Shao, Peng Xu, Jiahao Wang, Peng Gao, Kaipeng Zhang, Yu Qiao, and
Ping Luo. Efficientqat: Efficient quantization-aware training for large language models. arXiv
preprint arXiv:2407.11062, 2024a.
Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear
memory cost. arXiv preprint arXiv:1604.06174, 2016.
Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. Longlora:
Efficient fine-tuning of long-context large language models. In ICLR, 2024b.
Yukang Chen, Wei Huang, Baifeng Shi, Qinghao Hu, Hanrong Ye, Ligeng Zhu, Zhijian Liu,
Pavlo Molchanov, Jan Kautz, Xiaojuan Qi, et al.
Scaling rl to long videos.
arXiv preprint
arXiv:2507.07966, 2025a.
Zaiwei Chen, Siva Theja Maguluri, and Martin Zubeldia. Concentration of contractive stochastic
approximation: Additive and multiplicative noise. The Annals of Applied Probability, 35(2):
1298–1352, 2025b.
Daixuan Cheng, Shaohan Huang, Xuekai Zhu, Bo Dai, Wayne Xin Zhao, Zhenliang Zhang, and
Furu Wei. Reasoning with exploration: An entropy perspective. arXiv preprint arXiv:2506.14758,
2025.
Brian Chmiel, Maxim Fishman, Ron Banner, and Daniel Soudry. Fp4 all the way: Fully quantized
training of llms. arXiv preprint arXiv:2505.19115, 2025.
Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V.
Le, Sergey Levine, and Yi Ma. SFT memorizes, RL generalizes: A comparative study of founda-
tion model post-training. CoRR, abs/2501.17161, 2025.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to
solve math word problems. arXiv preprint arXiv:2110.14168, 2021.
Ganqu Cui, Yuchen Zhang, Jiacheng Chen, Lifan Yuan, Zhi Wang, Yuxin Zuo, Haozhan Li, Yuchen
Fan, Huayu Chen, Weize Chen, et al. The entropy mechanism of reinforcement learning for
reasoning language models. arXiv preprint arXiv:2505.22617, 2025.
10
DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.
CoRR, abs/2501.12948, 2025.
Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer. Gpt3. int8 (): 8-bit matrix
multiplication for transformers at scale. NeurIPS, 35:30318–30332, 2022.
Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient finetuning
of quantized llms. In NeurIPS, 2023a.
Tim Dettmers, Ruslan Svirschevski, Vage Egiazarian, Denis Kuznedelev, Elias Frantar, Saleh Ashk-
boos, Alexander Borzunov, Torsten Hoefler, and Dan Alistarh. Spqr: A sparse-quantized repre-
sentation for near-lossless llm weight compression. arXiv preprint arXiv:2306.03078, 2023b.
Onno Eberhard, Jakob Hollenstein, Cristina Pinneri, and Georg Martius.
Pink noise is all you
need: Colored noise exploration in deep reinforcement learning. In The Eleventh International
Conference on Learning Representations, 2023.
Kazuki Egashira, Mark Vero, Robin Staab, Jingxuan He, and Martin Vechev. Exploiting llm quan-
tization. Advances in Neural Information Processing Systems, 37:41709–41732, 2024.
Logan Engstrom, Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry
Rudolph, and Aleksander Madry. Implementation matters in deep rl: A case study on ppo and
trpo. In International conference on learning representations, 2019.
Benjamin Eysenbach and Sergey Levine. Maximum entropy rl (provably) solves some robust rl
problems. arXiv preprint arXiv:2103.06257, 2021.
Angela Fan, Pierre Stock, Benjamin Graham, Edouard Grave, R´emi Gribonval, Herve Jegou, and
Armand Joulin. Training with quantization noise for extreme model compression. arXiv preprint
arXiv:2004.07320, 2020.
Meire Fortunato, Mohammad Gheshlaghi Azar, Bilal Piot, Jacob Menick, Matteo Hessel, Ian Os-
band, Alex Graves, Volodymyr Mnih, Remi Munos, Demis Hassabis, Olivier Pietquin, Charles
Blundell, and Shane Legg.
Noisy networks for exploration.
In International Conference on
Learning Representations, 2018. URL https://openreview.net/forum?id=rywHCPkAW.
Roy Fox, Ari Pakman, and Naftali Tishby. Taming the noise in reinforcement learning via soft
updates. arXiv preprint arXiv:1512.08562, 2015.
Elias Frantar, Saleh Ashkboos, Torsten Hoefler, and Dan Alistarh. Gptq: Accurate post-training
quantization for generative pre-trained transformers. arXiv preprint arXiv:2210.17323, 2022.
Elias Frantar, Roberto L Castro, Jiale Chen, Torsten Hoefler, and Dan Alistarh.
Marlin:
Mixed-precision auto-regressive parallel inference on large language models.
arXiv preprint
arXiv:2408.11743, 2024.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad
Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783, 2024.
Etash Guha, Ryan Marten, Sedrick Keh, Negin Raoof, Georgios Smyrnis, Hritik Bansal, Marianna
Nezhurina, Jean Mercat, Trung Vu, Zayne Sprague, et al. Openthoughts: Data recipes for reason-
ing models. arXiv preprint arXiv:2506.04178, 2025.
Han Guo, Philip Greengard, Eric P Xing, and Yoon Kim. Lq-lora: Low-rank plus quantized matrix
decomposition for efficient language model finetuning. arXiv preprint arXiv:2311.12023, 2023.
Hossein Hassani, Roozbeh Razavi-Far, Mehrdad Saif, and Liang Lin. Towards sample-efficiency
and generalization of transfer and inverse reinforcement learning: A comprehensive literature
review. CoRR, abs/2411.10268, 2024.
Juan Camilo Gamboa Higuera, David Meger, and Gregory Dudek. Synthesizing neural network con-
trollers with probabilistic model-based reinforcement learning. In 2018 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pp. 2538–2544. IEEE, 2018.
11
Pin-Lun Hsu, Yun Dai, Vignesh Kothapalli, Qingquan Song, Shao Tang, Siyu Zhu, Steven Shimizu,
Shivam Sahni, Haowen Ning, Yanning Chen, and Zhipeng Wang. Liger-kernel: Efficient tri-
ton kernels for LLM training. In Championing Open-source DEvelopment in ML Workshop @
ICML25, 2025. URL https://openreview.net/forum?id=36SjAIT42G.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. Lora: Low-rank adaptation of large language models. In ICLR, 2022.
Wei Huang, Yue Liao, Jianhui Liu, Ruifei He, Haoru Tan, Shiming Zhang, Hongsheng Li, Si Liu,
and Xiaojuan Qi. Mixture compressor for mixture-of-experts llms gains more. arXiv preprint
arXiv:2410.06270, 2024a.
Wei Huang, Yangdong Liu, Haotong Qin, Ying Li, Shiming Zhang, Xianglong Liu, Michele Magno,
and Xiaojuan Qi. Billm: Pushing the limit of post-training quantization for llms. arXiv preprint
arXiv:2402.04291, 2024b.
Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, Michele Magno,
and Xiaojuan Qi.
Slim-llm: Salience-driven mixed-precision quantization for large language
models. arXiv preprint arXiv:2405.14917, 2024c.
Zhen Huang, Haoyang Zou, Xuefeng Li, Yixiu Liu, Yuxiang Zheng, Ethan Chern, Shijie Xia, Yiwei
Qin, Weizhe Yuan, and Pengfei Liu. O1 replication journey - part 2: Surpassing o1-preview
through simple distillation, big progress or bitter lesson? CoRR, abs/2411.16489, 2024d.
Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brah-
man, Lester James V. Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, Yuling Gu, Saumya Malik,
Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm,
Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hannaneh Hajishirzi. T¨ulu
3: Pushing frontiers in open language model post-training. CoRR, abs/2411.15124, 2024.
Janghwan Lee, Jiwoong Park, Jinseok Kim, Yongjik Kim, Jungju Oh, Jinwook Oh, and Jungwook
Choi. Amxfp4: Taming activation outliers with asymmetric microscaling floating-point for 4-bit
llm inference. arXiv preprint arXiv:2411.09909, 2024.
Brian Lester, Rami Al-Rfou, and Noah Constant. The power of scale for parameter-efficient prompt
tuning. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (eds.),
EMNLP, pp. 3045–3059, 2021.
Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif
Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in
ai4maths with 860k pairs of competition math problems and solutions. Hugging Face repository,
13(9):9, 2024.
Xiang Lisa Li and Percy Liang. Prefix-tuning: Optimizing continuous prompts for generation. In
Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), ACL, pp. 4582–4597, 2021.
Baohao Liao and Christof Monz. Apiq: Finetuning of 2-bit quantized large language model. arXiv
preprint arXiv:2402.05147, 2024.
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan
Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth
International Conference on Learning Representations, 2023.
Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Wei-Ming Chen, Wei-Chen Wang, Guangxuan
Xiao, Xingyu Dang, Chuang Gan, and Song Han. Awq: Activation-aware weight quantization for
on-device llm compression and acceleration. Proceedings of Machine Learning and Systems, 6:
87–100, 2024.
Haokun Liu, Derek Tam, Mohammed Muqeeth, Jay Mohta, Tenghao Huang, Mohit Bansal, and
Colin Raffel. Few-shot parameter-efficient fine-tuning is better and cheaper than in-context learn-
ing. In NeurIPS, 2022.
Liyuan Liu, Feng Yao, Dinghuai Zhang, Chengyu Dong, Jingbo Shang, and Jianfeng Gao. Flashrl:
8bit rollouts, full power rl, 2025a. URL https://fengyao.notion.site/flash-rl.
12
Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang, Kwang-
Ting Cheng, and Min-Hung Chen. Dora: Weight-decomposed low-rank adaptation. In ICML,
2024.
Xiangyan Liu, Jinjie Ni, Zijian Wu, Chao Du, Longxu Dou, Haonan Wang, Tianyu Pang, and
Michael Qizhe Shieh. Noisyrollout: Reinforcing visual reasoning with data augmentation. arXiv
preprint arXiv:2504.13055, 2025b.
Zechun Liu, Barlas Oguz, Changsheng Zhao, Ernie Chang, Pierre Stock, Yashar Mehdad, Yangyang
Shi, Raghuraman Krishnamoorthi, and Vikas Chandra. Llm-qat: Data-free quantization aware
training for large language models. arXiv preprint arXiv:2305.17888, 2023.
Yingqian Min, Zhipeng Chen, Jinhao Jiang, Jie Chen, Jia Deng, Yiwen Hu, Yiru Tang, Jiapeng
Wang, Xiaoxue Cheng, Huatong Song, Wayne Xin Zhao, Zheng Liu, Zhongyuan Wang, and Ji-
Rong Wen. Imitate, explore, and self-improve: A reproduction report on slow-thinking reasoning
systems. CoRR, abs/2412.09413, 2024.
NVIDIA. Nvidia h100 tensor core GPU architecture overview. https://resources.nvidia.com/en-us-
tensor-core, 2023.
NVIDIA.
Nvidia blackwell architecture technical brief.
https://resources.nvidia.com/
en-us-blackwell-architecture, 2024. Accessed: 2025-05-13.
OpenAI. Introducing GPT-5. https://openai.com/index/introducing-gpt-5/, aug 2025. Accessed:
2025-09-21.
Ian Osband, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. Deep exploration via
bootstrapped dqn. Advances in neural information processing systems, 29, 2016.
Bo Pang and Zhong-Ping Jiang. Robust reinforcement learning for stochastic linear quadratic control
with multiplicative noise. Trends in Nonlinear and Adaptive Control: A Tribute to Laurent Praly
for his 65th Birthday, pp. 249–277, 2021.
Matthias Plappert, Rein Houthooft, Prafulla Dhariwal, Szymon Sidor, Richard Y Chen, Xi Chen,
Tamim Asfour, Pieter Abbeel, and Marcin Andrychowicz. Parameter space noise for exploration.
arXiv preprint arXiv:1706.01905, 2017.
Open Compute Project. Ocp microscaling formats (mx) specification version 1.0. https://www.
opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf, 2023.
Ac-
cessed: 2023-09-13.
John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel.
High-
dimensional continuous control using generalized advantage estimation.
arXiv preprint
arXiv:1506.02438, 2015.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.
Yuzhang Shang, Zhihang Yuan, Qiang Wu, and Zhen Dong. Pb-llm: Partially binarized large lan-
guage models. arXiv preprint arXiv:2310.00034, 2023.
Wenqi Shao, Mengzhao Chen, Zhaoyang Zhang, Peng Xu, Lirui Zhao, Zhiqian Li, Kaipeng Zhang,
Peng Gao, Yu Qiao, and Ping Luo. Omniquant: Omnidirectionally calibrated quantization for
large language models. arXiv preprint arXiv:2308.13137, 2023.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y. K. Li,
Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open
language models. CoRR, abs/2402.03300, 2024.
Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng,
Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient RLHF framework. In EuroSys,
pp. 1279–1297, 2025.
13
Yang Sui, Yu-Neng Chuang, Guanchu Wang, Jiamu Zhang, Tianyi Zhang, Jiayi Yuan, Hongyi Liu,
Andrew Wen, Shaochen Zhong, Hanjie Chen, and Xia Ben Hu. Stop overthinking: A survey on
efficient reasoning for large language models. CoRR, abs/2503.16419, 2025.
Yi-Lin Sung, Varun Nair, and Colin Raffel. Training neural networks with fixed sparse masks. In
NeurIPS, pp. 24193–24205, 2021.
Qwen Team. Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2024.
Albert Tseng, Jerry Chee, Qingyao Sun, Volodymyr Kuleshov, and Christopher De Sa. Quip#:
Even better llm quantization with hadamard incoherence and lattice codebooks. arXiv preprint
arXiv:2402.04396, 2024.
Albert Tseng, Tao Yu, and Youngsuk Park.
Training llms with mxfp4.
arXiv preprint
arXiv:2502.20586, 2025.
Shangshang Wang, Julian Asilis, ¨Omer Faruk Akg¨ul, Enes Burak Bilgin, Ollie Liu, and Willie
Neiswanger. Tina: Tiny reasoning models via lora. CoRR, abs/2504.15777, 2025.
Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, and Song Han. Smoothquant:
Accurate and efficient post-training quantization for large language models.
In International
Conference on Machine Learning, pp. 38087–38099. PMLR, 2023.
Fengli Xu, Qianyue Hao, Zefang Zong, Jingwei Wang, Yunke Zhang, Jingyi Wang, Xiaochong Lan,
Jiahui Gong, Tianjian Ouyang, Fanjin Meng, Chenyang Shao, Yuwei Yan, Qinglong Yang, Yiwen
Song, Sijian Ren, Xinyuan Hu, Yu Li, Jie Feng, Chen Gao, and Yong Li. Towards large reasoning
models: A survey of reinforced reasoning with large language models. CoRR, abs/2501.09686,
2025.
Yi Yang, Yueting Zhuang, and Yunhe Pan. Multiple knowledge representation for big data artificial
intelligence: framework, applications, and case studies. Frontiers of Information Technology &
Electronic Engineering, 22(12):1551–1558, 2021.
Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong
Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi
Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi
Wang, Hongli Yu, Weinan Dai, Yuxuan Song, Xiangpeng Wei, Hao Zhou, Jingjing Liu, Wei-
Ying Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yonghui Wu, and Mingxuan Wang. DAPO: an
open-source LLM reinforcement learning system at scale. CoRR, abs/2503.14476, 2025.
Elad Ben Zaken, Yoav Goldberg, and Shauli Ravfogel. Bitfit: Simple parameter-efficient fine-tuning
for transformer-based masked language-models. In ACL, pp. 1–9, 2022.
Biao Zhang and Rico Sennrich. Root mean square layer normalization. Advances in neural infor-
mation processing systems, 32, 2019.
Hanfang Zhang, Bing-Chang Wang, and Ying Cao. Reinforcement learning solutions to stochas-
tic multi-agent graphical games with multiplicative noise. IEEE Transactions on Circuits and
Systems I: Regular Papers, 2025a.
Jintao Zhang, Jia Wei, Pengle Zhang, Xiaoming Xu, Haofeng Huang, Haoxu Wang, Kai Jiang,
Jun Zhu, and Jianfei Chen.
Sageattention3: Microscaling fp4 attention for inference and an
exploration of 8-bit training. arXiv preprint arXiv:2505.11594, 2025b.
Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang,
Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, and Junyang Lin. Group sequence policy op-
timization. CoRR, abs/2507.18071, 2025.
14
APPENDIX
A
ETHICS STATEMENT
This work exclusively leverages publicly available open-source datasets that have been previously
established and validated in academic research. No new text, video, or audio materials are generated
or incorporated as part of this study. The datasets utilized are strictly intended for research purposes
and are not employed for any commercial applications.
B
REPRODUCIBILITY STATEMENT
To ensure the research community can replicate our findings, this project will be released as open-
source software. The methodology is described in detail in Sec.3, while Sec.4.1 and Appendix E
outline the complete training protocols and implementation details, including all hyperparameter
settings.
C
USE OF LARGE LANGUAGE MODELS
During the preparation of this manuscript, we utilized large language models—GPT-5 (OpenAI,
2025)—exclusively to refine the language, focusing on improving grammar, flow, and tone at the
sentence and paragraph levels. These tools were not employed to generate ideas, design experiments,
or draw conclusions. All technical content, methodologies, and interpretations were independently
written, thoroughly verified, and approved by the authors. To minimize the risk of factual inaccu-
racies or citation errors, every model-edited sentence underwent human review, and all references
were carefully cross-checked with their primary sources. The authors accept full responsibility for
ensuring the accuracy and integrity of this manuscript.
D
RELATED WORK
Reinforcement Learning for LLMs
Recent efforts have focused on enhancing reasoning in
LLMs using RL (Min et al., 2024; Chu et al., 2025).
DeepSeekMath (Shao et al., 2024) im-
proves mathematical reasoning by continuing pre-training on math-intensive data and introducing
Group Relative Policy Optimization (GRPO) (Shao et al., 2024). Building on this, DeepSeek-
R1 (DeepSeek-AI, 2025) demonstrates that RL alone can drive strong reasoning, achieving per-
formance comparable to proprietary models with large-scale training. Complementary system-level
contributions, such as DAPO (Yu et al., 2025), offer an open-source RL framework with a de-
coupled optimization strategy, achieving competitive results through a simplified training pipeline.
GSPO (Zheng et al., 2025) stabilizes RL training and reduces variance through sequence-level op-
timization, proving effective in large-scale mixture-of-experts models. HybridFlow (Sheng et al.,
2025) introduces a flexible RLHF framework with hybrid control flow and a 3D-HybridEngine.
Together, these works demonstrate significant progress in advancing LLM reasoning with RL.
Quantization for LLMs
Quantization is a key technique for compressing LLMs, improving effi-
ciency by reducing parameter precision. The most common approach, Post-Training Quantization
(PTQ) (Dettmers et al., 2022; Frantar et al., 2022; Xiao et al., 2023; Shao et al., 2023; Lin et al.,
2024), transforms pre-trained models cost-effectively without retraining. Recent work has pushed
quantization to ultra-low bit-widths while maintaining performance (Huang et al., 2024c; Dettmers
et al., 2023b; Shang et al., 2023; Huang et al., 2024b; Liao & Monz, 2024; Tseng et al., 2024; Huang
et al., 2024a), including advancements in Quantization Aware Training (QAT) to improve robust-
ness (Liu et al., 2023; Chen et al., 2024a). Additionally, novel precision formats like NF4 (Dettmers
et al., 2023a), FP4 (Tseng et al., 2025; Chmiel et al., 2025), and MXFP4 (Chmiel et al., 2025)
enable accurate weight representation, achieving high compression with minimal or improved ac-
curacy loss. NVFP4 (NVIDIA, 2024) is a groundbreaking 4-bit floating-point format introduced
with NVIDIA’s Blackwell GPU architecture. This format expands on the idea of compact, low-bit
”micro” floating-point representations, offering developers enhanced versatility by adding another
flexible option for their projects (Zhang et al., 2025b; Castro et al., 2025; Lee et al., 2024).
15
Efficient Fine-tuning
Efficient fine-tuning is pivotal for adapting LLMs with minimal computa-
tional cost. LoRA (Hu et al., 2022) pioneered this approach by adding low-rank adapters to frozen
weight matrices. DoRA (Liu et al., 2024) improved upon this by decomposing weight updates
into directional and magnitude components, addressing low-rank constraints and enhancing stabil-
ity. QLoRA (Dettmers et al., 2023a) integrated LoRA with 4-bit quantization to further reduce
resource usage, while LongLoRA (Chen et al., 2024b) introduced fine-tuning methods for long-
context processing. Tina (Wang et al., 2025) demonstrated that compact models could gain rea-
soning ability through RL with LoRA. Beyond the LoRA family (Hu et al., 2022), other efficient
fine-tuning techniques include prompt tuning, prefix tuning, IA3, BitFit, Fisher-masked tuning, and
input-tuning (Lester et al., 2021; Li & Liang, 2021; Liu et al., 2022; Zaken et al., 2022; Sung et al.,
2021; An et al., 2022; Guo et al., 2023). These advancements underscore the importance of efficient
fine-tuning for practical LLM adaptation.
E
EXPERIMENT HYPERPARAMETERS
Training Data and Reward Function
We trained the Qwen2.5-3B-Instruct, Qwen2.5-7B-
Instruct, Qwen2.5-14B-Instruct, and Qwen2.5-32B-Instruct models, which are widely used for
evaluating reasoning capabilities. Unlike other studies that rely on math-specialized models, we
aim to evaluate training performance starting from general-purpose base models. Additionally,
QeRL can be smoothly transferred to other model families, such as the Qwen3 series. For the
GSM8K dataset, we primarily trained the Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct models
using GRPO, while for the BigMath dataset, we focused on training the Qwen2.5-7B-Instruct,
Qwen2.5-14B-Instruct, and Qwen2.5-32B-Instruct models using DAPO. Specifically, for the 7B
and 14B models, we selected data with medium to high difficulty levels (grades 3–5), and for
the 32B model, we used high-difficulty data (grades 4–5). For problem prompts, we append the
suffix
Solve the following math problem step by step.
The reasoning
process and direct answer are enclosed within <think> </think>
and <answer> </answer> tags, respectively, i.e., <think> reasoning
process here </think> <answer> answer here </answer>:
<think> ...
</think> <answer> ...
</answer>.
RL Training Configuration
For both GRPO and DAPO, we use the hyperparameters in Tab.4,
without using entropy or KL losses. For 4-bit training, the learning rate is set to 1e−5. However,
due to the fragile of the BF16 model with LoRA, the learning rate can not be larger than 5e−6, or it
will collapse in the late training stage.
Hyperparameter
Value
Optimizer
AdamW-8bit
Policy learning rate
1e−5 (QeRL, QLoRA) / 5e−6 (LoRA)
Training batch size
128
Samples per prompt
8 (GSM8K) / 16 (BigMath)
Policy updates per rollout
4 (GSM8K, off-policy) / 1 (BigMath, on-policy)
Max response length
4096 (GSM8K) / 8192 (BigMath)
Rollout temperature
1.0
Clip range ϵlow, ϵhigh
0.2, 0.28
Noise range Zstart, Zend
1e-2, 5e-4
Table 4: Hyperparameters of GRPO and DAPO training
F
DEPLOYMENT OF QERL
In Algorithm 1, we provide a detailed explanation of how QeRL is deployed within the GRPO
framework. During the steps in stage 0, the added noise σ is set to 0, where only quantization noise
effects. At stage 1, σ is initialized to σstart, and by the final stage (K-1) σ gradually transitions to
σstart. This progressive adjustment of noise ensures a structured and controlled exploration process
throughout the training stages, balancing stability and exploration effectively.
16
Algorithm 1 Deploy GRPO with QeRL and Adaptive Quantization Noise
Input NVFP4 policy model π˜θ; reward function rϕ; task prompts D; hyperparameters; LoRA rank, LoRA
alpha; number of stages K; σstart, σend;
1: policy model πθ ←π˜θ+θlora
2: for iteration = 1, ..., I do
3:
reference model πref ←πθ
4:
for step = 1, ..., M do
5:
Divide total steps M into K equal stages: steps per stage = ⌊M/K⌋
6:
Determine current stage k: k = ⌊
step−1
steps per stage⌋
7:
Set noise level σ ←



0
if k = 0
σstart ·

σend
σstart
 k−1
K−1
otherwise (exponential decay)
8:
Sample a batch Db from D
9:
Update the old policy model with AQN: πθold ←πθ + N(0, σ2)
10:
Sample G outputs {oi}G
i=1 ∼πθold(· | q) for each question q ∈Db
11:
Compute rewards {ri}G
i=1 for each sampled output oi by running rϕ
12:
Compute ˆAi,t for the t-th token of oi through group relative advantage estimation.
13:
for GRPO iteration = 1, ..., µ do
14:
Update the policy model πθ by maximizing the GRPO objective (Equation 3)
15:
end for
16:
end for
17: end for
Output πθ
G
PROOF OF NOISE SHARING
In this section, we further demonstrate the effectiveness of the noise-sharing operation proposed in
Eq.10, detailing the process by which additive noise is transformed into multiplicative noise. With
AQN, input of each block follows:
RMSNormnoise(X) = (Znoise
w
+ I) ⊙RMSNorm(X),
(11)
where RMSNorm(·) denotes the vanilla RMSNorm operation and w is the original scaling factor
in RMSNorm(·). The element-wise multiplication (⊙) will be auto-broadcast during computing.
Then, the operation of the following linear computation is defined as:
((Znoise
w
+ I) ⊙RMSNorm(X)) · ˆ
W = RMSNorm(X) · ((Znoise
w
+ I)⊤⊙ˆ
W),
(12)
Thus, the additive Gaussian noise, when incorporated into the noise-sharing mechanism of Layer-
Norm, can be equivalently regarded as multiplicative Gaussian noise (denoted as ( Znoise
w
+ I)) and
applied row-wise to the weight matrix ˆ
W. Since RMSNorm is only applied to the inputs of each
attention block and feed-forward network (FFN) block, this mechanism ensures that the Q, K, and
V matrices in the attention block share the same noise, while the down and up layers in the FFN
block also share a single, identical noise set. This noise-injection strategy avoids disrupting the
multiplication kernels of NVFP4 and BF16 in QeRL or introducing additional matrix multiplication
operations.
Both additive and multiplicative noise have been shown to positively contribute to exploration in
RL (Plappert et al., 2017; Higuera et al., 2018; Chen et al., 2025b). However, multiplicative noise
tends to be more sensitive, especially in deep networks like LLMs. To address this, we initialize
the noise standard deviation (σ) to 1e-2, which is smaller than the typical 1e-1 used in traditional
noise-based networks.
H
ADDITIONAL EXPERIMENTS OF TRAINING
Training Rewards of Different Model
Fig.12 and Fig.13 further compare the performance of
QeRL and 16-bit LoRA training on complex reasoning datasets. In Fig.12, we present the training
17
0
0.1
0.2
0.3
0.4
0.5
0.6
0
100
200
300
400
500
QeRL
LoRA
Training Steps
Accuracy Reward
Problem Level: 3~5
Figure 12: Training reward of 7B model.
0.1
0.2
0.3
0.4
0.5
0.6
0
50
100
150
200
250
QeRL
LoRA
Training Steps
Accuracy Reward
Problem Level: 4~5
Figure 13: Training reward of 32B model.
rewards of the Qwen2.5-7B-Instruct model on the BigMath dataset with difficulty levels ranging
from 3 to 5, as an extension of Fig.7. Leveraging the exploration benefits of QeRL in quantized
models, a rapid increase in reward is observed after approximately 200 steps, whereas 16-bit LoRA
requires over 500 steps to achieve a similar rise. Meanwhile, as shown in Fig.13, we trained the
Qwen2.5-32B-Instruct model on the highest difficulty data (levels 4–5). Although the difference
in reward growth between QeRL and LoRA is less pronounced in the 32B model compared to the
smaller 3B, 7B, and 14B models, QeRL still consistently performs better than LoRA.
0.2
0.3
0.4
0.5
0
100
200
300
400
500
600
QeRL
LoRA
Training Steps
Accuracy Reward
Figure 14: Entropy in RL steps.
More Experiments of Entropy
As an extension of
Fig.5, Fig.14 illustrates the entropy curve of the Qwen2.5-
14B-Instruct model at various training steps. Notably, the
entropy of QeRL remains consistently higher than that of
LoRA throughout the RL process, particularly during the
initial steps. This observation highlights the advantage of
QeRL in promoting exploration during RL, as higher en-
tropy indicates a broader search of the solution space. The
increased exploratory capacity facilitated by quantization
appears to enable the model to navigate complex environ-
ments more effectively, ultimately supporting improved
optimization. These results further validate the role of quantization in enhancing the exploration-
exploitation balance in RL tasks.
0
0.02
0.04
0.06
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
Linear Decay
Exponential Decay
Cosine Decay
Logarithmic Decay
Training Steps
Noise Scale (𝝈)
Figure 15: Noise curve of different schedulers.
Noise Scheduler
Fig.15 illustrates the noise
scheduler employed in our experiments, show-
ing four distinct decay strategies: linear, expo-
nential, cosine, and logarithmic. The scheduler
adjusts the noise level in 10 stages to guide the
training process. The linear decay method re-
duces noise uniformly across stages, ensuring a
consistent rate of change. The exponential de-
cay rapidly decreases the noise at the beginning
and uses smaller noise scales in later stages,
which we found effective for achieving stable
and higher rewards in later stages of training.
The cosine decay follows a smooth oscillatory
pattern, gradually reducing noise with a cosine curve, whereas the logarithmic decay decreases noise
sharply in early stages and stabilizes in later ones. Among these, we chose the exponential decay
strategy due to its ability to maintain smaller noise scales during the later stages, resulting in a more
stable and higher reward curve. This flexibility in controlling noise levels plays a critical role in
balancing exploration and convergence during training.
I
ADDITIONAL ABLATION STUDY
Ablation of Learning Rate We examine the impact of learning rate variations on the performance
of quantized models compared to 16-bit models. As illustrated in Fig.16 and Fig.17, with a relatively
small learning rate of 5e-6, QeRL marginally outperforms LoRA, achieving a reward close to 0.95.
18
0.35
0.5
0.65
0.8
0.95
0
50
100
150
200
QeRL(lr=3e-5)
QeRL(lr=5e-6)
Training Steps
Accuracy Reward
× 2.0 Speed Up
Figure 16: Ablation of learning rate in QeRL
(Qwen2.5-7B-Instruct).
0.2
0.4
0.6
0.8
1
0
50
100
150
200
LoRA(lr=3e-5)
LoRA(lr=5e-6)
Training Steps
Accuracy Reward
Figure 17: Ablation of learning rate in LoRA
(Qwen2.5-7B-Instruct).
Method
W#
Model Size
BS#
Throughput (Tokens/s)
E2E RL Speedup
Rollout Phase
Speedup
w/o GC
w/ GC
LoRA
BF16
6.2 GB
2
151.2
-
-
-
QeRL
NVFP4
2.8 GB
2
157.0
×1.0
×1.1
×1.0
LoRA
BF16
6.2 GB
8
2226.3
-
-
-
QeRL
NVFP4
2.8 GB
8
2271.4
×1.0
×1.1
×1.1
Table 5: Memory Saving and Speedup of Qwen2.5-3B-Instruct Model.
The table reports the
throughput (tokens/s) for the rollout phase under two batch size settings (2 and 8). Each input
has a length of 256 tokens, and each max completion length is 2048. “W#” denotes the data for-
mat, “BS#” is the number of batch size, and “E2E” denotes the end-to-end speed of GRPO training.
“GC” denotes gradient checkpointing.
Method
W#
Model Size
BS#
Throughput (Tokens/s)
E2E RL Speedup
Rollout Phase
Speedup
w/o GC
w/ GC
LoRA
BF16
15.2 GB
2
115.4
-
-
-
QeRL
NVFP4
5.9 GB
2
151.6
×1.3 ↑
×1.2 ↑
×1.2 ↑
LoRA
BF16
15.2 GB
8
1641.1
-
-
-
QeRL
NVFP4
5.9 GB
8
2091.8
×1.3 ↑
×1.1 ↑
×1.1 ↑
Table 6: Memory Saving and Speedup of Qwen2.5-7B-Instruct Model.
The table reports the
throughput (tokens/s) for the rollout phase under two batch size settings (2 and 8). Each input
has a length of 256 tokens, and each max completion length is 2048. “W#” denotes the data for-
mat, “BS#” is the number of batch size, and “E2E” denotes the end-to-end speed of GRPO training.
“GC” denotes gradient checkpointing.
When the learning rate is increased to 3e-5, the larger update magnitude in the adapter results in
faster reward growth and quicker model convergence. However, in 16-bit models, the excessive
update magnitude leads to instability, often causing the training process to collapse. In contrast,
QeRL demonstrates remarkable robustness to larger learning rates due to the presence of NVFP4
quantization noise, which helps stabilize updates. This robustness enables QeRL to maintain stable
training even under high learning rates, achieving a reward growth rate nearly twice as fast as the
16-bit model. These results underscore QeRL’s superior adaptability and efficiency, particularly in
challenging training scenarios with high learning rates.
J
MORE EFFICIENCY EXPERIMENTS
Tab.5, Tab.6, Tab.7, and Tab.8 provide additional speed benchmarks for the Qwen2.5-3B-Instruct,
Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, and Qwen2.5-32B-Instruct models, evaluated under
batch sizes of 2 and 8. For the 3B and 7B models, we did not enable memory-efficient techniques
such as gradient checkpointing (Chen et al., 2016) or Liger loss (Hsu et al., 2025) in order to max-
imize training speed. However, due to the substantial size of the 14B and 32B models and the
computational overhead introduced by importance sampling with gradients during RL training, we
19
Method
W#
Model Size
BS#
Throughput (Tokens/s)
E2E RL Speedup
Rollout Phase
Speedup
w/o GC
w/ GC
LoRA
BF16
29.6 GB
2
65.4
-
-
-
QeRL
NVFP4
10.6 GB
2
95.3
×1.3 ↑
×1.4 ↑
×1.4 ↑
LoRA
BF16
29.6 GB
8
737.2
-
OOM
-
QeRL
NVFP4
10.6 GB
8
1091.1
×1.5 ↑
OOM
×1.3 ↑
Table 7: Memory Saving and Speedup of Qwen2.5-14B-Instruct Model. The table reports the
throughput (tokens/s) for the rollout phase under two batch size settings (2 and 8). Each input
has a length of 256 tokens, and each max completion length is 2048. “W#” denotes the data for-
mat, “BS#” is the number of batch size, and “E2E” denotes the end-to-end speed of GRPO training.
“GC” denotes gradient checkpointing.
Method
W#
Model Size
BS#
Throughput (Tokens/s)
E2E RL Speedup
Rollout Phase
Speedup
w/o GC
w/ GC
LoRA
BF16
62.3 GB
2
34.0
-
OOM
OOM
QeRL
NVFP4
20.7 GB
2
60.0
×1.8
OOM
10.6 s/step
LoRA
BF16
62.3 GB
8
344.3
-
OOM
OOM
QeRL
NVFP4
20.7 GB
8
688.2
×2.0
OOM
12.2 s/step
Table 8: Memory Saving and Speedup of Qwen2.5-32B-Instruct Model. The table reports the
throughput (tokens/s) for the rollout phase under two batch size settings (2 and 8). Each input
has a length of 256 tokens, and each max completion length is 2048. “W#” denotes the data for-
mat, “BS#” is the number of batch size, and “E2E” denotes the end-to-end speed of GRPO training.
“GC” denotes gradient checkpointing.
Model
BF16 (Tokens/s)
Rank 16
Rank 32
Rank 64
3B
151.2
148.8
138.6
7B
115.4
113.2
108.3
14B
65.4
63.1
61.2
32B
34.0
33.3
31.9
Model
NVFP4 (Tokens/s)
Rank 16
Rank 32
Rank 64
3B
157.0
153.1
140.0
7B
151.6
149.9
137.7
14B
95.3
92.9
86.0
32B
58.0
56.0
51.3
Table 9: Throughput under different LoRA ranks in the rollout stage. We test the tokens/s for each
model in the vLLM engine, and the setting is aligned with Tab.7. We set the batch size as 1.
employ gradient checkpoint to accelerate computation. For training on GPUs with smaller memory
capacity, enabling gradient checkpointing is recommended to reduce memory usage, although this
may come at the cost of slower overall training speed. During the rollout phase, the precision of
NVFP4, optimized by the Marlin kernel (Frantar et al., 2024), demonstrates a significant accelera-
tion, achieving speeds of 1.0 to 2.0×. In particular, performance gains become more pronounced
as model size increases, with the 32B model achieving up to a 2.0× speedup. This indicates that
NVFP4’s advantages are particularly impactful for large-scale models, where computational de-
mands are higher.
In end-to-end RL efficiency evaluation, we report the per-step latency of GRPO training, defined as
the wall clock time to complete an optimization step including rollout generation, log-probability
computation, and parameter updates. We benchmark with rollout batch sizes of 2 and 8 while fixing
the maximum input length to 256 tokens and the maximum completion length to 2,048 tokens. For
fairness, we match the vLLM memory budget between BF16 and NVFP4 variants by setting the
same gpu memory utilization in the engine: 0.20 for Qwen2.5-3B-Instruct, 0.30 for 7B, 0.45 for
14B, and 0.40 for 32B (the latter to enable single-GPU training). Under these controlled settings,
20
the E2E latency reductions mirror the rollout phase acceleration and become more pronounced as
the model size grows, with the largest gains observed on Qwen2.5-14B-Instruct.
Additionally, Tab.9 provides a comparison of inference speeds between 16-bit and NVFP4 main
models across various LoRA ranks. NVFP4 consistently outperforms 16-bit models in terms of
speed at all adapter ranks, showcasing its ability to maintain efficiency across diverse configura-
tions. However, as the rank increases, both NVFP4 and BF16 experience a gradual decline in rollout
speed within the vLLM engine, likely due to the increased computational overhead associated with
higher ranks. Despite this, NVFP4 continues to demonstrate superior performance, highlighting its
robustness and adaptability for both small-scale and large-scale setups. These findings underscore
NVFP4’s potential to optimize inference efficiency, particularly when combined with advanced ker-
nels and varying adapter configurations.
K
LIMITATION ANALYSIS
We have demonstrated that our method, QeRL, achieves superior performance in RL training for
LLMs compared to 16-bit vanilla LoRA training. Additionally, QeRL matches the accuracy of 16-
bit full-parameter reinforcement fine-tuning while delivering over 2× training speedup relative to
both vanilla LoRA and QLoRA. However, since RL for LLMs inherently demands significantly
greater computational resources than SFT, our experiments, conducted on model sizes ranging from
3B to 32B, do not yet establish whether QeRL can maintain the same level of performance for mod-
els exceeding 70B parameters, leaving that investigation for future work. Another limitation is that
RL training often requires tens or even hundreds of hours, and while we have provided comprehen-
sive evaluations on reasoning benchmarks such as GSM8K, MATH 500, AIME 24, AIME 25, and
AMC 23, we did not extend our evaluations to other benchmarks or data types, such as code, or to
general-purpose language tasks unrelated to reasoning. Nevertheless, our technique can be seam-
lessly adapted to richer and more diverse training datasets. We encourage the community to explore
and apply this method to a broader range of tasks in future research.
21
