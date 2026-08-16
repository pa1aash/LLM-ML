---
title: '[2605.11128] Sampling More, Getting Less: Calibration is the Diversity Bottleneck
  in LLMs'
id: 260511128-sampling-more-getting-less-calibration-is-the-diversity-bottleneck-in
tags:
- llm-nas-feedback-positioning-7125b1
- mode-collapse
- output-diversity
created: '2026-08-16T16:51:02.427678Z'
updated: '2026-08-16T16:54:25.605905Z'
source: https://arxiv.org/abs/2605.11128
source_domain: arxiv.org
fetched_at: '2026-08-16T16:51:02.427411Z'
fetch_provider: builtin
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Proposes a validity-diversity framework attributing LLM diversity collapse
  to miscalibration of the step-by-step token probability distribution during decoding,
  decomposed into ''order calibration'' (valid tokens not reliably ranked above invalid
  ones, forcing a trade-off between recovering valid continuations and admitting invalid
  ones under rank-cutoff sampling) and ''shape calibration'' (probability mass over-concentrated
  on a few valid continuations with a heavy tail of mixed valid/invalid tokens). Across
  14 models and controlled diagnostic tasks with known valid-answer sets, the authors
  show these local per-step miscalibrations compound across decoding steps into large
  sequence-level diversity losses -- i.e., diversity collapse is a general property
  of how LLMs allocate probability mass, not merely an artifact of particular sampling
  heuristics (temperature, top-k, top-p). SCOPE CAVEAT FOR THE QUANTIZATION GAP: this
  paper does NOT test or mention quantization anywhere in the text; it is general
  mechanism literature on why LLMs collapse to narrow output sets (relevant to the
  RLHF/decoding side of the corpus''s diversity-collapse coverage) but provides no
  direct evidence, positive or negative, about quantization''s effect on diversity.
  It is included for the broader self-refinement/mode-collapse mechanism question,
  not as quantization evidence.'
---

[2605.11128] Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2605.11128
(cs)
[Submitted on 11 May 2026]
Title:
Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs
Authors:
Amin Banayeeanzade
,
Qingchuan Yang
,
Dhruv Tarsadiya
,
Fatemeh Bahrani
,
Leonardo Blas
,
Alfy Samuel
,
Robin Jia
,
Meisam Razaviyayn
,
Sai Praneeth Karimireddy
View a PDF of the paper titled Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs, by Amin Banayeeanzade and 8 other authors
View PDF
HTML (experimental)
Abstract:
Diversity is essential for language-model applications ranging from creative generation to scientific discovery, yet modern LLMs often collapse into a narrow subset of plausible outputs. While prior work has developed benchmarks for measuring this lack of diversity, less is known about how the step-by-step probability distributions at inference time cause the problem. We introduce a validity--diversity framework that attributes diversity collapse to how an LLM allocates probability mass across valid and invalid continuations during decoding. This framework decomposes the bottleneck into two complementary forms of miscalibration. First, order calibration: valid tokens are not reliably ranked above invalid tokens, so rank-based cutoff rules must trade off between recovering valid continuations and admitting invalid ones. Second, shape calibration: probability mass is overly concentrated only on few valid continuations while having a heavy-tail of mixed valid and invalid tokens, so maintaining high validity limits diversity. We formalize both mechanisms and show that local failures compound across decoding steps, producing strong sequence-level losses in diversity. Empirically, we develop controlled diagnostics for probing these bottlenecks, including tasks with exactly known valid sets and oracle cutoff baselines. Across 14 language models spanning multiple families and scales, we find that diversity collapse is not merely a limitation of particular sampling heuristics, but a consequence of order and shape miscalibration in the LLM distribution.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2605.11128
[cs.CL]
(or
arXiv:2605.11128v1
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2605.11128
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Qingchuan Yang [
view email
]
[v1]
Mon, 11 May 2026 18:36:30 UTC (1,387 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs, by Amin Banayeeanzade and 8 other authors
View PDF
HTML (experimental)
TeX Source
view license
Current browse context:
cs.CL
< prev
|
next >
new
|
recent
|
2026-05
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

Sampling More, Getting Less: Calibration is the
Diversity Bottleneck in LLMs
Amin Banayeeanzade∗♠
Qingchuan Yang∗♠
Dhruv Tarsadiya♠
Fatemeh Bahrani♠
Leonardo Blas♠
Alfy Samuel♣
Robin Jia♠
Meisam Razaviyayn♠
Sai Praneeth Karimireddy♠
♠University of Southern California
♣Capital One
{banayeea,qcyang,razaviya,karimire}@usc.edu
Demo: https://diversitycalibration.github.io
Abstract
Diversity is essential for language-model applications ranging from creative genera-
tion to scientific discovery, yet modern LLMs often collapse into a narrow subset of
plausible outputs. While prior work has developed benchmarks for measuring this
lack of diversity, less is known about how the step-by-step probability distributions
at inference time cause the problem. We introduce a validity–diversity framework
that attributes diversity collapse to how an LLM allocates probability mass across
valid and invalid continuations during decoding. This framework decomposes the
bottleneck into two complementary forms of miscalibration. First, order calibra-
tion: valid tokens are not reliably ranked above invalid tokens, so rank-based cutoff
rules must trade off between recovering valid continuations and admitting invalid
ones. Second, shape calibration: probability mass is overly concentrated only on
few valid continuations while having a heavy-tail of mixed valid and invalid to-
kens, so maintaining high validity limits diversity. We formalize both mechanisms
and show that local failures compound across decoding steps, producing strong
sequence-level losses in diversity. Empirically, we develop controlled diagnostics
for probing these bottlenecks, including tasks with exactly known valid sets and
oracle cutoff baselines. Across 14 language models spanning multiple families
and scales, we find that diversity collapse is not merely a limitation of particular
sampling heuristics, but a consequence of order and shape miscalibration in the
LLM distribution.
1
Introduction
 
Token Index (sorted by probability)
10
11
10
9
10
7
10
5
10
3
10
1
Token Probability
(logscale)
 cat
 star
 cunning
 hollow
 áng
 
.lazy llama {s
 courteous
Prompt: Write a movie plot.
Answer: There once was a _________
Valid and Frequent
Valid and Rare
Invalid
0
1
2
3
4
5
6
7
8
Temperature
0.0
0.2
0.4
0.6
0.8
1.0
Aggregate Probability
Figure 1: (Left) The token distribution of a generation step from QWEN3.5-35B-A3B. The distribu-
tion is very sharp in the front, followed by a heavy tail with mixed valid and invalid tokens. As a
result, (Right) many valid tokens are unlikely to appear in the output under any temperature sampling.
† tokens are subsampled non-uniformly for enhanced visualization.
∗Equal Contribution.
Preprint.
arXiv:2605.11128v1  [cs.CL]  11 May 2026
Diversity in generation is essential for a wide range of applications, including synthetic data gen-
eration [3], creative writing [49], recommendation systems [6], coding [47], and exploration for
scientific discovery [39]. However, contemporary large language models (LLMs) often exhibit a
notable lack of diversity [18, 30, 36, 44]. For instance, 59% of stories in a GPT-4-generated dataset
begin with “Once upon a time”, and GPT-5.5 repeatedly outputs “Valparaíso, Chile” when asked to
name a random city in the world (see Appendix G).
These examples illustrate a broader failure mode: when generation is overly concentrated on a small
set of high-probability outputs, many valid alternatives may be systematically undersampled. Recent
work has made substantial progress in measuring this lack of diversity [49], but they neither explain
the source of the collapse nor provide diagnostic tools to systematically trace the problem.
Although standard sampling methods intend to resolve the problem, they rather reveal the difficulty;
temperature sampling flattens the distribution, but often shifts probability mass toward invalid or
nonsensical continuations before sufficient diversity is recovered [35]. Top-token filtering methods
such as top-k and min-p [28] truncate the ranked distribution, but they either drop many valid
alternatives or include invalid tokens. This suggests that the bottleneck is not merely the decoding
heuristic, but the properties of the LLM distribution itself. We therefore ask:
What are the distributional properties of LLMs that constrain their ability
to generate outputs that are both valid and diverse?
To formalize this view, we study the inference-time distribution of an LLM through the lens of
validity–diversity trade-off. Rather than only measuring diversity on completed generations, we
analyze the decoding process itself and how the model’s next-token distribution allocates probability
mass across generations. This perspective reveals two distinct failure modes.
First, LLMs fail in order calibration: valid tokens are not reliably ranked above invalid ones. In
Figure 1, we show that many valid alternative tokens (blue) appear farther down the ranked distribution
and are interleaved with invalid ones (red). When this occurs, any top-token filtering rule faces an
unavoidable trade-off: expanding the cutoff recovers more valid continuations but also admits more
invalid ones, while tightening it preserves validity but excludes valid alternatives.
Second, LLMs fail in shape calibration: probability mass is non-uniformly concentrated on a small
number of valid continuations (green), but much smaller probability is assigned to other valid tokens
(blue), while having a heavy tail of many invalid tokens (red). In the right panel of Figure 1, we show
that increasing temperature shifts probability mass away from the head, but much of this mass flows
into the invalid tail rather than recovering rare valid alternatives. We formalize these effects and show
that the resulting validity–diversity loss compounds when generating longer sequences.
Across 14 language models spanning multiple families and scales, we find that these calibration
failures constitute the primary bottleneck to diversity and addressing them unlocks broader diversity
in model outputs. Our findings also have implications for model training and design, suggesting
directions for mitigating these bottlenecks at their source. Finally, our analysis challenges implicit
assumptions underlying common sampling strategies and provides guidance for more principled
benchmarking and evaluation of decoding methods.
Contributions. Building on this framework, our contributions are:
1. We introduce a framework for analyzing the validity–diversity trade-off at both token and
sequence levels.
2. We introduce order calibration and shape calibration as two complementary distributional
bottlenecks. We theoretically and empirically demonstrate that local failures compound over
sequence length.
3. We develop controlled empirical diagnostics for probing these bottlenecks, including settings
with exactly known valid sets and oracle cutoff baselines, and show that no decoding method
that relies on top-token filtering can effectively recover diversity.
2
Related Work
Diversity and mode collapse. Limited output diversity has emerged as a central failure mode of
modern language models [44, 10, 12, 46]. Homogeneity of the generation appears both within a
single model across repeated samples [36] and across different models on the same prompts [18].
Even frontier models remain substantially less diverse than humans [49], especially the models with
2
extensive alignment and post-training [45, 43, 22, 20, 30]. Together, these works motivate studying
diversity as a first-class property of language generation.
Evaluation. Diversity is inherently multi-dimensional, and recent work has moved beyond narrow
lexical metrics toward broader assessments of open-ended generation [49, 18, 21]. Attempts to
improve diversity might lead to text degeneration [15], and temperature should be carefully tuned [38,
50]. Therefore, diversity should not be assessed in isolation from quality [34], and raw diversity is
misleading when many outputs are low-quality [35, 42]. Following this perspective, we treat diversity
as meaningful only insofar as it broadens the space of valid, useful outputs, and we use this lens to
diagnose when existing decoding rules fail to do so.
Improving diversity. A long line of work has sought to improve diversity through prompting [48,
29, 41], training [25, 16, 26, 7], base-aligned model collaboration [42, 32], and inference-time
interventions [40, 37]. Closer to our work, inference-time stochastic methods such as temperature
scaling [1], top-k [8], top-p [15], and min-p [28] sampling modify the support or sharpness of the
next-token distribution. Subsequent methods make truncation more adaptive [13, 27, 28, 33, 51]. Our
work complements this literature: rather than proposing another decoding strategy, we examine why
existing sampling rules often fail to recover meaningful diversity.
3
Preliminaries
We consider an auto-regressive LLM with vocabulary V. Given a prompt x ∈V∗and a generated
prefix y<t = (y1, . . . , yt−1) ∈Vt−1, the model defines a conditional distribution p(· | y<t, x) over
the next token. The probability of a complete output y = (y1, . . . , yd) of length d is p(y | x) =
Qd
t=1 p(yt | y<t, x). When the task is fixed and unambiguous, we omit x from our notations.
We use V ⊆V∗to represent the set of all valid responses to x. With slight misuse of notation, we say
y<t ∈V , if there exists a continuation w ⊆V∗such that the concatenation y<t ◦w ∈V .
Definition 3.1 (Validity and Diversity). For a prompt x, let Y ∼p(· | x) denote the model’s
distribution over complete responses.
1. (Validity) We define validity as the total probability mass that the model assigns to V :
Val(p) := p(Y ∈V | x) =
X
y∈V
p(y | x).
2. (Diversity) We assume that all valid responses are equally preferred, and hence define diversity
as the normalized effective support size of the model distribution restricted to the valid set:
Div(p) := eH(˜p)
|V | ,
where ˜p = p(Y | Y ∈V, x), and H is the Shannon entropy.
Intuitively, validity captures the probability mass that the model assigns to valid responses, and
diversity then quantifies the effective coverage of valid outputs under the distribution restricted to
the valid set [14, 19]. In a related work, Yang et al. [45] defines the exponential of entropy to be a
token-level measure of the effective number of plausible next steps during generation. Both validity
and diversity take values in the interval [0, 1], with higher values indicating better performance.
Moreover, we define:
Definition 3.2 (Valid Continuations and Valid Tokens). Given a context y<t ∈Vt−1, valid continua-
tions are defined as the number of all sequences in V that begin with the prefix y<t,
N(y<t) :=
{z ∈V∗: y<t ◦z ∈V }
,
and the set of valid tokens is accordingly defined as tokens that lead to at least one valid continuation,
G(y<t) := {v ∈V : N(y<t ◦v) > 0}.
A decoding rule achieves high validity if it assigns high probability only on valid tokens at each time
step, and it achieves high diversity if it explores many distinct tokens in G rather than concentrating
on only a few of them. However, LLMs, regardless of the decoding strategy employed, often
exhibit a pronounced validity–diversity trade-off. In this work, we identify two primary sources
of this phenomenon arising from properties of the model distribution: In §4, we first introduce
order calibration and its implications on top-token filtering methods. Next in §5, we identify the
3
shape calibration issue and we show that together, these effects constitute the primary sources of the
observed validity–diversity trade-off.
4
Order Calibration Fails: Valid tokens are not ranked first
Modern decoding strategies implicitly assume that valid tokens are concentrated near the top of the
ranked distribution and that simple statistics of the distribution (e.g., cumulative mass or relative
probability gaps) can reliably identify and retain these tokens. Under this view, diversity is increased
by expanding the retained set, while validity is preserved by truncating low-probability regions.
In this section, we show that the LLM token distributions systematically violate these assumptions.
Valid tokens are not confined to the head but are frequently interspersed with invalid tokens throughout
the tail (see Figure 1), and the relationship between rank and validity is neither monotone nor stable
across contexts. As a result, any decoding rule based solely on rank-based filtering faces an inherent
limitation: it must inevitably trade off between excluding valid tokens and admitting invalid ones.
Even small imperfections in separating valid and invalid tokens at each step compound multiplicatively
over long generations, leading to a sharp degradation in reachable valid outputs.
Cutoff strategies. We abstract all the top-token filtering methods as cutoff strategies. Let S denote
a cutoff strategy. Given a prefix y<t, it first sorts the tokens by their conditional probabilities, and
then selects a cutoff index, retaining all tokens up to that index and discarding the rest. Importantly,
our framing strictly contains any adaptive top-token filtering method, since S is not a predetermined
rule; we allow it to be any arbitrary cutoff strategy, potentially depending on the prefix y<t and the
model distribution p(· | y<t) at each step. Let St(y<t) denote the set of the retained tokens. An ideal
strategy S would include as many valid tokens as possible (high recall) while excluding all invalid
tokens (high precision). Therefore, we define the following to measure the quality of a strategy:
Definition 4.1 (Precision/Recall). Let V ⊆Vd denote the set of valid sequences, G(y<t) the set of
valid next tokens, N(y<t) the number of valid continuations, and St(y<t) the set of retained tokens
for a prefix y<t.
1. (Local Precision) We define local precision as the fraction of retained tokens that are valid,
Prect(S; y<t) := |St(y<t) ∩G(y<t)|
|St(y<t)|
.
2. (Local Recall) We define local recall as the fraction of valid continuations that remain reachable
after truncation.
Rect(S; y<t) :=
P
v∈St(y<t)∩G(y<t) N(y<t ◦v)
N(y<t)
.
Moreover, let QS denote the sequence distribution induced by uniformly sampling from the retained
sets. Then,
3. (Sequence-Level Precision) We define sequence precision as the probability of generating a
valid sequence, i.e.,
Precseq(S) := QS(Y ∈V ).
4. (Sequence-Level Recall) We define sequence recall as the fraction of valid sequences that
remain reachable.
Recseq(S) := |{y ∈V : yt ∈St(y<t) ∀t}|
|V |
Relation to validity and diversity. Sequence precision coincides exactly with validity. Sequence
recall captures a complementary notion of diversity: it measures how much of the valid output space
remains accessible under the decoding rule. While our definition of diversity is entropy-based, recall
provides a notion of coverage. In particular, if recall is small, then the decoder can only explore a
small subset of valid outputs, regardless of how probability is distributed within it.
4.1
A controlled testbed for order calibration
Our goal is to empirically measure the precision–recall trade-off introduced by any cutoff strategy.
A central challenge in practice is that the valid set V is intractable to characterize, as it grows
exponentially with sequence length, especially in open-ended tasks such as storytelling. To address
this, we propose a practical procedure to approximate the precision/recall metrics. Detailed setup,
models, and prompts are found in Appendix B.1.
4
the
soft
try
blue
云
The boy with
Sweep Logits
silver umbrella found a …
Greedy Decode
eyes full of sadness …
the last star, tucked it …
silver umbrella found a …
的hair found a door in …
d=1
d=2
d=3
Cutoff
Invalid / Retained
Valid / Retained
Valid / Dropped
Invalid / Dropped
Judge
0.00
0.25
0.50
0.75
1.00
Local Recall
0.0
0.2
0.4
0.6
0.8
1.0
Local Precision
d=1
d=2
d=3
Figure 2: (Left) We sweep the logits and cutoff thresholds at each conditional distribution to
enumerate retained tokens up to a certain depth, followed by greedy decoding from each leaf. A judge
model then evaluates the validity of the generated sequences, allowing us to attribute a validity label
to each token. We then measure the number of valid/invalid tokens that were retained/dropped by the
cutoff strategy to obtain local precision and recall. (Right) The frontier precision–recall trade-offs at
different depths obtained by sweeping cutoff strategies. The trade-off degrades as depth increases.
Measuring token validity. Given a fixed prefix y<t, we query the LLM to get a sorted list of all next
token candidates {v1, · · · , v|V|}. For each token vj, we construct the extended prefix y<t ◦vj and
then perform greedy decoding to completion. This approximates the model’s most likely continuation
conditioned on having selected vj (see Figure 2, middle panel). We then evaluate the resulting
sequence using an LLM-as-a-judge [11], scoring grammar, semantic, and overall validity. By
thresholding this score, we obtain a binary validity label for the token vj. Repeating this process for
all tokens yields an approximate assessment of token-level validity given the prefix, and allows us to
compute precision–recall trade-off as a function of the cutoff strategy in the next sections.
Appendix A.1 provides additional details, including the evaluation rubric. Appendix A.2 validates
the reliability of the LLM judge against human annotations and examines the impact of judge model
choice. Moreover, Appendix A.3 compares greedy completions vs sampling and shows that the
results are robust to this choice.
1
20k
40k
60k
80k
Cutoff Index
0.00
0.25
0.50
0.75
1.00
Prompt: Write a creative story.
     Response: In _________
Recall
Precision
Figure 3: Local precision–recall
trade-off when sweeping the cut-
off in a single generation step.
Single-step precision–recall trade-off. The extracted labels allow
us to measure the precision–recall trade-off at a single decoding
step to observe how valid tokens are distributed in the conditional.
In Figure 3, we sweep the cutoff from the first index up to the
token at rank 80k on a story generation task with Qwen3.5-35B.
Plotting the precision and recall at each cutoff, we observe that
precision drops sharply at the front, but recall slowly improves,
even at high token indexes. This indicates that there is a strong
precision–recall trade-off and order calibration is severely violated
on this single conditional. We provide qualitative examples in
Appendix B.2.
Multi-step precision–recall trade-off. We extend our single-step
methodology to a more realistic setup that captures the multi-step
effects. Particularly, we extend the procedure to depth d > 1: Instead of immediately decoding
greedily, we recursively expand tokens at each successive step, constructing a tree of continuations
(Figure 2, left). After expanding all nodes up to d tokens at each branch, we complete each leaf via
greedy decoding. By evaluating these resulting sequences with a judge, we obtain a validity label for
each token in this sequence along the tree: a token is valid if at least one sequence containing it is
valid. Since the number of sequences grows exponentially with depth and each depth requires many
LLM calls, we sweep up to depth 3 and subsample tokens at each depth, as detailed in Appendix B.
Given the validity label of every token up to step d, we construct the precision–recall trade-off
curves by sweeping over all possible cutoff strategies, and computing the local trade-off for every
node using Definition 4.1. Note that our framework includes all top-token filtering strategies, as it
allows any node to adjust its own cutoff arbitrarily. Each cutoff strategy gives a single point in the
precision–recall curve; we take the Pareto frontier of all strategies as a representative of the best
achievable trade-off.
Local precision–recall trade-off worsens with depth. We perform the above procedure across 10
seeds, each repeated with a random query from NoveltyBench [49] and a random prefix y<t. For
each seed, we compute the Pareto-optimal precision–recall curve at every node in the generation tree
5
as previously mentioned. Figure 2 (right) summarizes the results. To analyze the effect of horizon
length, we group nodes by their depth in the generation tree and report, for each depth, the maximum,
minimum, and average Pareto frontiers. We observe the following:
• Even the optimal cutoff strategy exhibits a non-negligible local precision–recall trade-off.
• The trade-off worsens as depth increases (from d = 1 to d = 2, and from d = 2 to d = 3).
• This degradation is not only present in the average, but also on the maximum frontier.
Overall, these results show that the precision–recall trade-off induced by cutoffs worsens with
decoding depth. This provides empirical evidence that order calibration is frequently violated: valid
continuations are not reliably ranked above invalid ones, and this misalignment compounds over
longer horizons.
4.2
Local order failures compound into sequence-level collapse
These measurements are at the level of local precision and recall. At the sequence level, the trade-off
is stronger: even small but constant local imperfections lead to a dramatic collapse in global diversity
since the errors incurred at each depth compound multiplicatively, as we show in the following:
Theorem 4.2 (Compounding effect of decoding steps). Suppose that at least m decoding positions
exhibit a constant local precision–recall trade-off: at each such position, high local precision must
discard a constant fraction of valid continuations. Then there exist constants c, C > 0 such that any
cutoff strategy S satisfying
Precseq(S) ≥1 −δ
must satisfy
Recseq(S) ≤(1 −δ)−C e−cm.
0.0
0.5
1.0
Average AUC
0.5B
1B
2B
4B
8B
16B
32B
64B 128B
Model Size
0.0
0.5
1.0
Recall
(at Prec.=0.8)
post-trained
pre-trained only
Figure 4:
Precision–recall trade-offs
across Qwen-3, Llama-3, Olmo-3 on 9
sizes and training stage.
Evaluations
are averaged on 3 random positions and
queries. (Top) Average area under the
precision–recall frontier. (Bottom) Aver-
age recall at precision 0.8.
Table 1: Semantic and Lexical Diversity
of Cutoff Strategies. Higher Embedding
Diversity score corresponds to higher se-
mantic diversity; lower Self-BLEU score
corresponds to higher lexical diversity.
Strategy
Emb. Diversity (↑) Self-BLEU (↓)
oracle
0.40±0.15
0.69±0.21
top-k
0.33±0.14
0.71±0.17
min-p
0.29±0.13
0.80±0.16
top-p
0.25±0.12
0.86±0.13
no filtering
0.25±0.11
0.86±0.12
Interpretation. The theorem formalizes a compound-
ing effect. High sequence-level validity leaves only a
small total budget for local precision errors. Hence, at
most O(log(1/(1 −δ))) decoding steps can tolerate
such trade-offs; the remaining steps must use near-
perfect cutoffs. If valid and invalid tokens are inter-
leaved, such cutoffs necessarily discard a constant frac-
tion of valid continuations. These losses compound
multiplicatively, so the reachable valid set shrinks ex-
ponentially. In this sense, any cutoff rule can maintain
validity only by sacrificing broad validity, thereby prov-
ing a hardness result for any decoding strategy that
relies on top-token filtering. The details of the proof
are in Appendix E.
4.3
Scaling and the diversity gap
Sections 4.1 and 4.2 establish local precision–recall as
a meaningful diagnostic for order calibration. We now
use this diagnostic to quantify the practical importance
of order calibration.
Model Size. Figure 4 summarizes the local precision–
recall trade-offs across model families, scales, and train-
ing stages (see Appendix B.3). The average AUC of the
precision–recall frontier exhibits a mild upward trend
with model size. However, the improvement is modest
and far from eliminating the trade-off. In particular,
when precision is fixed at 0.8, recall remains low and
non-monotonic across model sizes. This shows that
larger models do not reliably recover more valid con-
tinuations under a high-precision constraint. Therefore,
while scale slightly improves order calibration, it does
not by itself resolve the failure in order calibration.
Oracle filtering. To quantify how much diversity is lost specifically due to order miscalibration,
we present an oracle validity filter that samples only from tokens labeled valid by our diagnostic
6
procedure. We apply the oracle filter only during the first two decoding steps and then continue
generation normally. For other strategies, we sweep a grid of temperatures and cutoff parameters and
report the best diversity for validity at least 0.8 (see Appendix B.4).
Table 1 shows that even this limited oracle intervention yields a clear improvement: oracle filtering
achieves the highest embedding diversity and the lowest Self-BLEU. This indicates that valid tokens
excluded by rank-based cutoffs yield meaningfully different generations. Therefore, the order
calibration gap has direct output-level consequences: valid alternatives are present in the model
distribution, but standard rank-based sampling rules fail to reliably expose them.
5
Shape Calibration Fails: Sharp, heavy-tailed distributions limit diversity
In this section, we focus on a second, complementary bottleneck, namely shape calibration. While
the LLM conditional distribution varies across tasks, prior work suggests that next-token distributions
are typically head-heavy and long-tailed, with most probability mass concentrated in a relatively
small nucleus and a large, unreliable tail [13, 15]. In Appendix I, we randomly sample conditional
next-token distributions from a diverse set of tasks and examine their sorted logits. We show that the
logits’ behavior can be consistently described by a linear decay in the head, followed by a heavy-tailed
distribution that decays logarithmically. After applying softmax, this translates to an exponential
(geometric) decay in the head, i.e., p(vk | y<t) ∝exp(−λk/T) and a Zipf-like [4] behavior in the
tail, p(vk | y<t) ∝k−λ/T , where k denotes the rank of token vk in the sorted vocabulary, T is the
temperature and λ controls the sharpness of the distribution.
These two properties together cause the shape calibration issue: the distribution is always very sharp
over a very small portion of the head, even in tasks where we expect to observe an exact uniform
distribution on valid tokens. Temperature scaling is therefore often used to flatten the distribution
head, increasing the probability of valid regions outside the head. However, temperature scaling
comes with a necessary caveat. Although each invalid token remains with a small probability, the
accumulated probability of invalid tokens especially grows very quickly with temperature scaling,
leading to an unwanted validity–diversity trade-off.
While understanding how distributional miscalibration arises from LLM training and design pipeline
is an important question [9, 5], we focus on its implications for the diversity-validity trade-off. We
emphasize that characterizing the exact geometric form is not intended as a literal empirical claim,
but as an analytically convenient proxy for heavy-tailed distributions.
5.1
How severely does distribution shape affect validity–diversity trade-off?
Although temperature is the most basic way of injecting randomness into decoding, in practice,
higher temperatures often fail to recover a broad set of valid outputs. Our goal in this subsection is
to characterize this limitation by attributing the failure to distribution sharpness. In fact, we show
that even if the order calibration disappears, sharp LLM conditionals induce heavy validity–diversity
trade-offs. For simplicity of the proof, we further impose the following assumption:
Assumption 5.1 (Invariant valid branching). Assume that all valid sequences for a task have a fixed
length d. For every valid prefix y<t, the number of valid next-token choices depends only on the
position t, not on the particular prefix. That is, there exist integers v1, . . . , vd such that for every
valid prefix y<t,
|G(y<t)| = vt.
Furthermore, we define the branching length as the number of positions at which there is more than
one valid continuation:
m := |{t ∈[d] : vt ≥2}| .
Assumption 5.1 fixes the generation length and removes prefix-level heterogeneity, allowing the
diversity loss to be expressed in terms of the effective branching length m.
Theorem 5.2 (Validity–Diversity trade-off). Consider a length-d generation task with a valid set
V . Suppose that, at each valid prefix, the model’s ranked next-token distribution is geometrically
decaying, and suppose the valid next tokens occupy the top ranks. Then any temperature-scaled
distribution satisfying
Val(p) ≥1 −ϵ
also satisfies
Div(p) ≤e−mc(ϵ),
for some positive constant c(ϵ) > 0, where c(ϵ) →ln 2 as ϵ →0.
7
0.00
0.25
0.50
0.75
1.00
Validity
0.00
0.25
0.50
0.75
1.00
Diversity
Unconstrained RNG
0.00
0.25
0.50
0.75
1.00
Validity
Constrained RNG
d = 2
d = 3
d = 4
1
200
400
600
800
1000
10 20
10 16
10 12
10 8
10 4
100
Tail
Sequence Index (sorted by probability)
Probability
T=0.5
T=1.0
T=1.6
T=4.0
Uniform
Figure 5: Effects of temperature scaling in random number generation on Olmo-3-7B-Instruct.
(Left) Validity–diversity trade-offs for unconstrained and constrained random-number generation
tasks across sequence lengths d. Longer generations exhibit a stronger validity–diversity trade-off.
(Right) Valid sequence probabilities for the length-3 unconstrained random-number generation task.
Interpretation. The theorem shows that temperature scaling pays a local diversity price at every
branching step. To achieve high validity, the distribution must be sharp enough that invalid tokens
receive little mass. At the same time, this sharpness makes the conditional distribution over valid
tokens non-uniform, concentrating probability on the highest-ranked valid continuations. These
per-step entropy losses add across the sequence; after exponentiating entropy to obtain diversity,
they yield an exponential decay in m. Moreover, the rate c(ϵ) increases as the validity requirement
becomes stricter. In the high-validity regime, the bound approaches m, and can be stronger when
many steps contain several valid continuations. We provide the formal proof in Appendix F.
5.2
Empirical Investigation
Controlled random generation testbed. Investigating the diversity–validity trade-off as a function
of distribution shape requires us to calculate the probabilities of every valid sequence. Sweeping all
the conditionals on open-ended generation is infeasible. To address this, we propose two tasks with
known valid sets as controlled testbeds: random-number generation and naming a random US state.
We consider two variants of the random number generation task in Figure 5. In the unconstrained
setting, the model is asked to generate a length-d sequence of i.i.d. digits, where each digit lies in
{0, . . . , 9}. Thus, every sequence in {0, . . . , 9}d is valid. We expect the model to impose a uniform
distribution on each conditional, given independence. In the constrained setting, the model is asked to
generate a length-d sequence of digits whose sum equals a specified target N. Appendix C provides
further details, including exact prompts and our experimental setup.
These tasks offer several key advantages. First, we can compute the exact generation probability for
each valid sequence, since the entire valid set is known. Second, we objectively expect each valid
sequence to have the same generation probability. Thus, any deviation from uniform distribution leads
to a systematic validity–diversity trade-off. Moreover, the unconstrained random-number generation
task satisfies Assumption 5.1, serving as a proper testbed for our theorem.
Sequence validity–diversity trade-offs. For each candidate sequence in V , we therefore feed the
corresponding prefixes into the LLM and extract the next-token logits. We then apply different
temperatures to these logits and compute, exactly over the known sequence space, both the probability
mass assigned to the valid region and the entropy of the model’s distribution conditioned on validity.
This gives the validity–diversity curve induced by temperature scaling alone.
The left panel shows the validity–diversity frontier for random-number generation across sequence
lengths d ∈{2, 3, 4}. As the length increases, the frontier becomes sharper: maintaining high validity
requires a larger reduction in diversity. This is consistent with Theorem 5.2, where each branching
position contributes a local entropy loss and these losses compound across the sequence. The
constrained setting exhibits an even stronger trade-off, despite violating Assumption 5.1, suggesting
the broader applicability of our result.
Shape calibration in sequence-level. Although we have studied the shape of the conditional dis-
tribution, its implications at the sequence level are less transparent. The right panel of Figure 5
provides a sequence-level view of temperature scaling trade-off. We plot the probabilities of each
valid sequence in the unconstrained length-3 task, and show the magnitude of the invalid sequence
mass. We observe that the distribution is already highly concentrated: a small number of sequences
receive orders-of-magnitude larger probability than the rest. At the same time, many sequences lie in a
long, low-probability tail. Raising the temperature can indeed move probability mass toward this tail,
thereby increasing diversity among rare valid outputs. However, the invalid sequence mass dominates
even more as temperature increases. Therefore, shifting mass toward the tail improves diversity only
8
0.0
0.5
1.0
Validity
0.00
0.25
0.50
0.75
1.00
Diversity
Name a State
0.0
0.5
1.0
Validity
Unconstrained RNG
no filtering
top-k
top-p
min-p
oracle
Figure 6: Validity–diversity Pareto frontiers for
top-token filtering methods on generation tasks
from Llama-3.1-8B-Instruct. (Left) Name a
random state in the US. (Right) Unconstrained
random number. Each sampling method is swept
over both temperature and its own truncation pa-
rameter. The oracle-size cutoff retains the top
|G(y<t)| tokens at each prefix.
at the cost of reduced validity. Thus, the empirical behavior mirrors the theory: temperature can
flatten the distribution, but it cannot selectively recover valid diversity.
5.3
When shape and order miscalibration interact
Top-token filtering is often applied after temperature scaling to suppress invalid tail mass. However,
this does not remove the calibration problem; it couples shape calibration with order calibration. A
cutoff rule retains a prefix of the ranked distribution, so to preserve valid diversity while maintaining
validity, this prefix must approximate the valid-token set G(y<t). This requires two conditions: valid
tokens must be concentrated near the top of the ranked distribution, and the cutoff rule must adapt to
the local boundary of the valid set. Different methods encode different boundary assumptions: top-k
assumes a roughly fixed support size, top-p assumes a stable cumulative-mass boundary, and min-p
assumes a stable relative-probability gap from the top token.
Comparing validity–diversity trade-offs. We test these assumptions on controlled tasks, including
random number generation and random state generation tasks, where the valid set is known exactly.
Figure 6 reports the trade-offs on both tasks, and more results are found in Appendix C. For each
cutoff strategy, we sweep both temperature and the method-associated parameter, since different
methods can achieve their best validity–diversity trade-off at different temperatures [50]. Comparing
methods at a single fixed temperature can therefore be misleading: poor performance may reflect a
bad choice of temperature rather than a limitation of the filtering rule itself.
Cutoff Oracle Strategy. To study the miscalibration, we include a cutoff oracle strategy in Figure 6.
Given that our generation task has a known ground truth, we directly compute the valid size at
each generation step. At each step, the oracle cutoff rule knows only the number of valid tokens,
g⋆
t = |G(y<t)|, and retains the top g⋆
t ranked tokens. However, the oracle does not know which
tokens are valid, and therefore remains a rank-based cutoff rule. On the random state generation task,
the cutoff oracle achieves the ideal point (1.0, 1.0), indicating that the model is order-calibrated in
this controlled setting. Therefore, the remaining gap reflects a failure of the methods’ implicit shape
assumptions: fixed top-k, cumulative-mass, or relative-probability thresholds do not identify the valid-
token boundary. On the random-number generation task, the cutoff oracle also does not immediately
achieve high diversity, showing that shape miscalibration is coupled with order miscalibration.
6
Future Work
This paper attributes the LLM validity–diversity trade-off to two distributional properties: order
and shape calibration. Through empirical demonstrations and theoretical analysis, we show that
miscalibration is a recurring bottleneck across model families, sizes, and controlled generation tasks.
Finally, as a preliminary piece of future work, in Appendix H we observe that order and shape
calibration can potentially provide insights into domains beyond open-ended diversity generation.
Several directions remain open. First, our results suggest that future decoding methods should move
beyond top-token filtering rules. Calibration-aware decoders could instead incorporate auxiliary
validity signals. Second, it remains important to understand where these calibration failures come
from. Pretraining, instruction tuning, preference optimization, and safety alignment may each affect
the sharpness of the distribution and the rank ordering of valid alternatives. Studying these effects
could suggest training objectives that preserve broader valid support without sacrificing quality.
9
References
[1] David H. Ackley, Geoffrey E. Hinton, and Terrence J. Sejnowski. A learning algorithm for
boltzmann machines. Cognitive Science, 9(1):147–169, 1985.
[2] Danial Alihosseini, Ehsan Montahaei, and Mahdieh Soleymani Baghshah. Jointly measuring
diversity and quality in text generation models. In Proceedings of the Workshop on Methods for
Optimizing and Evaluating Neural Language Generation, pages 90–98, 2019.
[3] Amin Banayeeanzade, Qingchuan Yang, Deqing Fu, Spencer Hong, Erin Babinsky, Alfy Samuel,
Anoop Kumar, Robin Jia, and Sai Praneeth Karimireddy. Epsvec: Efficient and private synthetic
data generation via dataset vectors, 2026.
[4] Sourya Basu, Govardana Sachitanandam Ramachandran, Nitish Shirish Keskar, and Lav R.
Varshney. Mirostat: A neural text decoding algorithm that directly controls perplexity. In
International Conference on Learning Representations, 2021.
[5] Haw-Shiuan Chang and Andrew McCallum. Softmax bottleneck makes language models unable
to represent multi-mode word distributions. In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 8048–8073, 2022.
[6] Jiaju Chen, Chongming Gao, Shuai Yuan, Shuchang Liu, Qingpeng Cai, and Peng Jiang. Dlcrec:
A novel approach for managing diversity in llm-based recommender systems. In Proceedings of
the Eighteenth ACM International Conference on Web Search and Data Mining, page 857–865,
2025.
[7] John Joon Young Chung, Vishakh Padmakumar, Melissa Roemmele, Yuqian Sun, and Max
Kreminski. Modifying large language model post-training for diverse creative writing. In
Second Conference on Language Modeling, 2025.
[8] Angela Fan, Mike Lewis, and Yann Dauphin. Hierarchical neural story generation. In Proceed-
ings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 889–898, 2018.
[9] Matthew Finlayson, John Hewitt, Alexander Koller, Swabha Swayamdipta, and Ashish Sab-
harwal. Closing the curious case of neural text degeneration. In The Twelfth International
Conference on Learning Representations, 2024.
[10] Bijean Ghafouri. The variance paradox: How ai reduces diversity but increases novelty, 2026.
[11] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li,
Yinghan Shen, Shengjie Ma, Honghao Liu, Saizhuo Wang, Kun Zhang, Zhouchi Lin, Bowen
Zhang, Lionel Ni, Wen Gao, Yuanzhuo Wang, and Jian Guo. A survey on llm-as-a-judge. The
Innovation, page 101253, 2026.
[12] Yanzhu Guo, Guokan Shang, and Chloé Clavel. Benchmarking linguistic diversity of large
language models. Transactions of the Association for Computational Linguistics, 13:1507–1526,
2025.
[13] John Hewitt, Christopher Manning, and Percy Liang. Truncation sampling as language model
desmoothing. In Findings of the Association for Computational Linguistics: EMNLP 2022,
pages 3414–3427, 2022.
[14] M. O. Hill. Diversity and evenness: A unifying notation and its consequences. Ecology, 54(2):
427–432, 1973.
[15] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural
text degeneration. In International Conference on Learning Representations, 2020.
[16] Mete Ismayilzada, Antonio Laverghetta Jr., Simone A. Luchini, Reet Patel, Antoine Bosselut,
Lonneke Van Der Plas, and Roger E. Beaty. Creative preference optimization. In Findings of
the Association for Computational Linguistics: EMNLP 2025, pages 9580–9609, 2025.
10
[17] Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Ar-
mando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination
free evaluation of large language models for code. In The Thirteenth International Conference
on Learning Representations, 2025.
[18] Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia
Tsvetkov, Maarten Sap, and Yejin Choi. Artificial hivemind: The open-ended homogeneity of
language models (and beyond). In The Thirty-ninth Annual Conference on Neural Information
Processing Systems Datasets and Benchmarks Track, 2025.
[19] Lou Jost. Entropy and diversity. Oikos, 113(2):363–375, 2006.
[20] Aayush Karan and Yilun Du. Reasoning with sampling: Your base model is smarter than you
think. In The Fourteenth International Conference on Learning Representations, 2026.
[21] Rabimba Karanjai, Yang Lu, Ranjith Chodavarapu, Lei Xu, and Weidong Shi. Evaluating the
quality of randomness and entropy in tasks supported by large language models, 2025.
[22] Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward
Grefenstette, and Roberta Raileanu. Understanding the effects of RLHF on LLM generalisation
and diversity. In The Twelfth International Conference on Learning Representations, 2024.
[23] Klaus Krippendorff. Content analysis: An introduction to its methodology. 1980.
[24] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu,
Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large lan-
guage model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium
on Operating Systems Principles, 2023.
[25] Tianjian Li, Yiming Zhang, Ping Yu, Swarnadeep Saha, Daniel Khashabi, Jason Weston, Jack
Lanchantin, and Tianlu Wang. Jointly reinforcing diversity and quality in language model
generations, 2025.
[26] Ziniu Li, Congliang Chen, Tian Xu, Zeyu Qin, Jiancong Xiao, Zhi-Quan Luo, and Ruoyu Sun.
Preserving diversity in supervised fine-tuning of large language models. In The Thirteenth
International Conference on Learning Representations, 2025.
[27] Clara Meister, Tiago Pimentel, Gian Wiher, and Ryan Cotterell. Locally typical sampling.
Transactions of the Association for Computational Linguistics, 11, 2023.
[28] Nguyen Nhat Minh, Andrew Baker, Clement Neo, Allen G Roush, Andreas Kirsch, and Ravid
Shwartz-Ziv. Turning up the heat: Min-p sampling for creative and coherent LLM outputs. In
The Thirteenth International Conference on Learning Representations, 2025.
[29] Kou Misaki and Takuya Akiba. String seed of thought: Prompting LLMs for distribution-
faithful and diverse generation. In The Fourteenth International Conference on Learning
Representations, 2026.
[30] Sonia Krishna Murthy, Tomer Ullman, and Jennifer Hu. One fish, two fish, but not the whole
sea: Alignment reduces language models’ conceptual diversity. In Proceedings of the 2025
Conference of the Nations of the Americas Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume 1: Long Papers), 2025.
[31] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic
evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association
for Computational Linguistics, pages 311–318, 2002.
[32] Max Peeperkorn, Tom Kouwenhoven, Dan Brown, and Anna Jordanous. Mind the gap: Con-
formative decoding to improve output diversity of instruction-tuned large language models,
2025.
[33] Erfan Baghaei Potraghloo, Seyedarmin Azizi, Souvik Kundu, and Massoud Pedram. Top-h
decoding: Adapting the creativity and coherence with bounded entropy in text generation. In
The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2026.
11
[34] Rylan Schaeffer, Joshua Kazdan, and Yegor Denisov-Blanch. Min-p, max exaggeration: A
critical analysis of min-p sampling in language models, 2025.
[35] Alexander Shypula, Shuo Li, Botong Zhang, Vishakh Padmakumar, Kayo Yin, and Osbert
Bastani. Evaluating the diversity and quality of LLM generated content. In Second Conference
on Language Modeling, 2025.
[36] Zhivar Sourati, Farzan Karimi-Malekabadi, Meltem Ozcan, Colin McDaniel, Alireza Ziabari,
Jackson Trager, Ala Tak, Meng Chen, Fred Morstatter, and Morteza Dehghani. The shrinking
landscape of linguistic diversity in the age of large language models, 2025.
[37] Yixuan Su and Nigel Collier. Contrastive search is what you need for neural text generation.
Transactions on Machine Learning Research, 2023.
[38] Sergey Troshin, Wafaa Mohammed, Yan Meng, Christof Monz, Antske Fokkens, and Vlad
Niculae. Control the temperature: Selective sampling for diverse and high-quality LLM outputs.
In Second Conference on Language Modeling, 2025.
[39] Guancheng Tu, Shiyang Zhang, Tianyu Zhang, Yi Zhang, and Diji Yang. Shared nature, unique
nurture: Prism for pluralistic reasoning via in-context structure modeling, 2026.
[40] Ashwin Vijayakumar, Michael Cogswell, Ramprasaath Selvaraju, Qing Sun, Stefan Lee, David
Crandall, and Dhruv Batra. Diverse beam search for improved description of complex scenes.
Proceedings of the AAAI Conference on Artificial Intelligence, Apr. 2018.
[41] Qihan Wang, Shidong Pan, Tal Linzen, and Emily Black. Multilingual prompting for improving
LLM generation diversity. In Proceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing, pages 6367–6389, 2025.
[42] Yichen Wang, Chenghao Yang, Tenghao Huang, Muhao Chen, Jonathan May, and Mina Lee.
Optimizing diversity and quality through base-aligned model collaboration, 2025.
[43] Peter West and Christopher Potts. Base models beat aligned models at randomness and creativity.
In Second Conference on Language Modeling, 2025.
[44] Weijia Xu, Nebojsa Jojic, Sudha Rao, Chris Brockett, and Bill Dolan. Echoes in ai: Quantifying
lack of plot diversity in llm outputs. Proceedings of the National Academy of Sciences, 2025.
[45] Chenghao Yang, Sida Li, and Ari Holtzman. Llm probability concentration: How alignment
shrinks the generative horizon, 2026.
[46] Sunny Yu, Ahmad Jabbar, Robert Hawkins, Dan Jurafsky, and Myra Cheng. Generation space
size: Understanding and calibrating open-endedness of llm generations, 2025.
[47] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao
Huang. Does reinforcement learning really incentivize reasoning capacity in LLMs beyond
the base model? In The Thirty-ninth Annual Conference on Neural Information Processing
Systems, 2026.
[48] Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D.
Manning, and Weiyan Shi. Verbalized sampling: How to mitigate mode collapse and unlock
llm diversity, 2025.
[49] Yiming Zhang, Harshita Diddee, Susan Holm, Hanchen Liu, Xinyue Liu, Vinay Samuel, Barry
Wang, and Daphne Ippolito. Noveltybench: Evaluating creativity and diversity in language
models. In Second Conference on Language Modeling, 2025.
[50] Yuxuan Zhou, Margret Keuper, and Mario Fritz. Balancing diversity and risk in LLM sampling:
How to select your method and parameter for open-ended text generation. In Proceedings of
the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 26352–26365, 2025.
[51] Wenhong Zhu, Hongkun Hao, Zhiwei He, Yiming Ai, and Rui Wang. Improving open-ended
text generation via adaptive decoding. In Forty-first International Conference on Machine
Learning, 2024.
12
A
LLM-as-a-judge Details
A.1
Prompt and Model
Token validity is scored based on the greedy-decoding completion. We use Qwen3.5-35B-A3B-FP8
with thinking enabled as our judge. The prompts used are documented below.
LLM-as-a-judge Prompts
System Prompt
You are a strict language quality judge. You will first see a question and a generated
answer. Your task is to evaluate the quality of the generated answer.
Evaluation Instructions
Evaluate the quality of the generated answer based on the following criteria:
1) grammar, spelling and punctuation,
2) semantic soundness, validity, and relevance to the question,
3) overall quality.
When evaluating grammar, check for spelling mistakes, punctuation errors, and grammatical
issues. If spaces are missing between words, extra punctuations in the middle of
sentences, or incorrect capitalization, that should be considered a grammar error.
Additionally, if the generation contains non-English characters, that should be
considered a grammar error and scored low on grammar, even if the rest of the generation
is grammatically correct.
When evaluating semantics, check if the answer is relevant to the question, if it makes
sense, and if it is factually correct. An answer that is fluent but does not make sense
or is not relevant to the question should be scored low on semantics.
Be concise and nitpicky in your evaluation. Short responses are acceptable, as long as
they are grammatically correct and semantically sound.
First provide an explanation of your evaluation, then give a score for each category.
Score each category on a scale of 1 to 10, where 1 is very poor and 10 is excellent.
Any non-English text in the generation should be considered a grammar error and scored
low on grammar, even if it’s semantically correct.
The generation does not need to be fully finished to be considered as valid. Only look at
the part of the generation that is present and evaluate that. If the generation is cut
off in the middle of a sentence, evaluate the part that is present and ignore the fact
that it is cut off.
Return only valid JSON with this exact schema:
{
"reason": <brief explanation>,
"grammar": <int 1-10>,
"semantic": <int 1-10>,
"overall": <int 1-10>
}
Here is the question:
‘‘‘
{question}
’’’
And here is the generated answer to evaluate:
‘‘‘
{shot}
’’’
Your evaluation:
13
A.2
Evaluating LLM-as-a-judge
To assess the inter-annotator reliability, three authors independently annotated 100 generations using
the rubric in Appendix A.1.
We compute inter-annotator agreement on the overall validity scores using Krippendorff’s alpha [23],
obtaining α = 0.759. This indicates reasonably strong agreement among annotators, suggesting that
the rubric yields consistent human judgments.
To
contrast
our
LLM-based
evaluation
against
human
judgment,
we
compared
Qwen3.5-35B-A3B-FP8 predictions against human labels from different annotators for 100
generations. We use a threshold of 9 on grammar, semantic and overall score. We treat the judge
model score above this threshold as a positive prediction (valid token) and scores below the
threshold as negative predictions (invalid tokens). Under this rule, Qwen3.5-35B-A3B-FP8 achieves
80.90% accuracy and 79.60% F1 when compared to humans. We also compare GPT-5.4 against
Qwen3.5-35B-A3B-FP8 under the same rule, obtaining 73.40% accuracy and 61.45% F1. These
results suggest that our LLM-based evaluation can approximate human judgment and GPT-5.4.
A.3
Greedy Decoding Robustness
Our token-validity annotation procedure uses greedy decoding after forcing a candidate token, treating
the validity of the resulting completion as a proxy for whether that token preserves access to a valid
continuation. One concern is that a token deemed invalid under greedy decoding may still admit
a valid sampled continuation, and vice versa. To test this, Figure 7 reports an ablation in which
we replace the greedy continuation with model suggested sampling parameters when constructing
token-level validity labels. We sample 10 continuations for each token, and then recompute the
resulting precision–recall curves under the same cutoff strategies. The curves are nearly unchanged,
indicating that the estimated precision and recall are not driven by the particular choice of greedy
decoding. This supports using greedy continuation as a computationally efficient proxy for token
validity in the main experiments.
10000
20000
30000
40000
50000
Cutoff Index
0.0
0.2
0.4
0.6
0.8
1.0
Prompt: Write a creative story.
     Response: In _________
Recall - Greedy
Precision - Greedy
Recall - Sampling
Precision - Sampling
Figure 7: Robustness of token-validity estimates to the continuation procedure. We compare
local precision–recall curves computed from token labels obtained by greedy decoding after each
forced candidate token with labels obtained from stochastic sampling. The resulting curves nearly
overlap across cutoff indices, indicating that our estimated precision–recall trade-off is not sensitive
to using greedy decoding as the continuation procedure.
B
Order Calibration Trade-offs
B.1
Generation Setup
We use a variety of LLMs in our experiments, each documented in the subsection below. We
randomly select 5 open-ended generation categories from NoveltyBench, ranging from story-telling,
joke-telling, poems, and item selection [49].
14
B.2
Sweep Generation Experiment
Experiments were repeated 10 times for reproducibility. The cost of exhaustive sweeping grows
as N d, where d is the sweeping depth and N is the number of candidate tokens evaluated at each
conditional. To keep the oracle evaluation computationally tractable, we sweep only three consecutive
conditionals. At each conditional, we consider candidates up to rank 1000 and subsample every tenth
token, yielding N = 100 candidates per conditional and 1003 evaluated branches in total.
In Table 2, we provide examples of tokens swept in the story generation task. We sweep up to depth
3 from randomly selected starting token positions. All examples are generated with Qwen3.5-35B.
Table 2: Generation examples from the creative story generation task. The sweeping is performed on
the second token after “In”. For each candidate token, we force the model to continue from the prefix
with that token, greedily decode the remaining sequence, and evaluate the resulting completion with
the judge.
Index
Token
Generated sequence
Judge Score
1
2045
In 2045, the last library was a single glass pod floating above the
clouds, where an old librarian read stories to a child who had never
seen a paper book.
10
43
edible
Inedible, the clock on the wall began to tick backwards, unspooling
the day until the coffee cup in my hand was whole again, the steam
rising into the past.
8
201
Obsidian
In Obsidian City, the streetlamps were made of captured starlight,
and the baker sold loaves of warm silence to quiet the noisy crowds.
One rainy Tuesday, a little girl bought a loaf, but when she bit into it,
she heard the sound of a thousand birds singing in a language she had
never known. She smiled, realizing the city wasn’t just quiet; it was
waiting for her to listen.
10
208
eeded
Ineeded to write a story, so I did.
7
507
ebriated
Inebriated by the scent of rain on hot asphalt, the old streetlamp
blinked its last, dreaming of a sky it would never see again.
10
508
忘却
In忘却of a forgotten clock tower, a tiny mouse named Pip found a
gear that could rewind time by one second. Every day, he used it to fix
his mistakes, until he realized he had no memories of the past, only
the endless, perfect present.
5
10002 Eco-Station In Eco-Station 42, the last human, Elara, watered a single, glowing
fern that hummed a lullaby to the empty room.
10
23606
gone
In gone, the clock struck thirteen, and the moon turned into a giant,
glowing cheese wheel that the city’s cats began to chase, leaving trails
of stardust in their wake.
7
35007
Darth
In Darth Vader’s castle, a tiny droid named BEEP-7 found a single,
glowing blue flower growing in a crack of the floor. He spent his
entire existence protecting it from the stormtroopers, watering it with
his own coolant, until the day the Emperor arrived. BEEP-7 stood
before the dark lord, not with a weapon, but with the flower, and for
a moment, the dark side of the Force faltered, remembering a time
before the fall.
10
42101

In  the quietest corner of the world, a tiny snowflake named Pippin
decided to dance instead of fall, turning the gray sky into a swirling
ballroom of silver light.
8
42273
cartoons
In cartoons, the sky is always blue, but in the real world, it is a canvas
of shifting grays and golds. One day, a little girl named Elara found a
paintbrush that could touch the sky. She dipped it in the color of her
favorite sunset and painted a dragon made of fire across the clouds.
The dragon roared, not with sound, but with warmth, and the world
below smiled as the cold winter faded into an eternal spring.
10
B.3
Model Size Experiments
Figure 8 provides a detailed view of the models used for our experiment.
15
Model Size
0.0
0.2
0.4
0.6
0.8
1.0
Average AUC
0.5B
1B
2B
4B
8B
16B
32B
64B
128B
Model Size
0.0
0.2
0.4
0.6
0.8
1.0
Recall (at P=0.8)
Qwen3-0.6B
Qwen3-0.6B-Base
Qwen3.5-0.8B
Qwen3.5-0.8B-Base
Llama-3.2-1B-Instruct
Qwen3.5-2B
Qwen3.5-2B-Base
Qwen3-4B
Qwen3-4B-Base
Olmo-3-7B-Instruct
Qwen3-8B
Llama-3.1-8B-Instruct
Qwen3-8B-Base
Qwen3.5-9B
Qwen3.5-9B-Base
Qwen3.5-27B
Olmo-3.1-32B-Instruct
Qwen3.5-35B-A3B
Qwen3.5-35B-A3B-Base
Meta-Llama-3.1-70B-Instruct
Qwen3.5-122B-A10B
Figure 8: Detailed view of Figure 4. We evaluate models across 3 families with various sizes.
Diamond represents pre-trained only models; circle represents post-trained Qwen models; square
represents post-trained Olmo models; triangle represents post-trained Llama models.
B.4
Oracle Sampling Experiments
For all our oracle generations, we only sweep the first two decoding steps. We sweep the first
conditional to obtain 1000 valid tokens. We then uniformly sample from these 1000 tokens to obtain
the second-step conditionals and repeat the sweep once.
In Table 3, we report the parameter ranges we swept for each cutoff strategy. For each parameter,
we sample 1000 generations to compute the semantic and lexical diversity. While there are multiple
methods for measuring semantic and lexical diversity, we select embedding diversity and Self-BLEU
as representatives.
Table 3: Parameter grids used for decoding sweeps. For each parameter setting, we sample 1000
generations to report semantic and lexical diversity.
Decoding strategy
Parameter
Values swept
Temperature sampling
T
{0.01, 0.3, 0.6, 0.8, 1.0, 1.2,
1.4, 1.6, 1.8, 2.0, 2.5, 3.0}
top-k
k
{10, 20, 50, 80, 100, 500}
top-p
p
{0.1, 0.5, 0.7, 0.9, 0.95}
min-p
pmin
{0.01, 0.1, 0.5, 0.9}
Embedding Diversity For each generated sequence, we obtain an embedding vector ei from
Qwen3-Embedding-8B. We compute pairwise cosine distances and define embedding diversity
as
Embedding Diversity =
2
n(n −1)
X
i<j
(1 −cos(ei, ej)).
The range is between [0, 1], with higher values indicating higher semantic diversity.
Self-BLEU [2] Given generations {y1, . . . , yn} for a single task, we compute
Self-BLEU = 1
n
n
X
i=1
BLEU(yi, {yj}j̸=i) ∈[0, 1].
where BLEU [31] measures the n-gram overlap between a candidate output and a set of reference
outputs. In Self-BLEU, lower values indicate higher lexical diversity. We use n = 4 in our
experiments.
16
C
Shape Calibration Trade-offs
C.1
Random Number Generation
Random Number Generation Prompts
Unconstrained Generation
Generate {n} random integers between {start} and {end} (inclusive). Your response should
be {n} integers separated by commas and no white spaces. Answer:
Constrained Generation
Generate {n} random integers between {start} and {end} (inclusive) that sum to at most {
sum_value}. Your response should be {n} integers separated by commas and no white spaces.
Answer:
0.0
0.2
0.4
0.6
0.8
1.0
Sum-Constrained RNG
Diversity
Llama-3.1-8B-Instruct
Olmo-3-7B-Instruct
Qwen3-4B
Qwen3-8B
0.0
0.5
1.0
Validity
0.0
0.2
0.4
0.6
0.8
1.0
Unconstrained RNG
Diversity
0.0
0.5
1.0
Validity
0.0
0.5
1.0
Validity
0.0
0.5
1.0
Validity
no filtering
top-k
top-p
min-p
oracle
Figure 9: Validity–Diversity trade-off frontiers for constrained and unconstrained random number
generation across 4 model families.
Figure 9 shows the validity–diversity trade-off frontiers across all four model families. The cutoff
oracle helps disentangle the effects of shape and order calibration. In the unconstrained setting, the
oracle often approaches the ideal point (1.0, 1.0), suggesting that the main gap stems from standard
top-token filters’ inability to infer the correct support size. In contrast, in the sum-constrained setting,
the oracle itself remains separated from (1.0, 1.0), indicating stronger order miscalibration. The addi-
tional gap between standard top-token filtering methods and the oracle reflects shape miscalibration,
since fixed top-k, cumulative-mass, and relative-probability thresholds do not reliably recover the
correct valid-token boundary. Together, these results show that shape and order miscalibration jointly
contribute to the validity–diversity trade-off, with their interaction becoming more pronounced under
compositional constraints.
C.2
Random State Generation
Name a Random State Prompt
Randomly name a US state with no additional explanation. Answer:
Figure 10 shows sequence-level probabilities under different temperatures on the random state
generation task. As in Figure 5, the distribution is highly concentrated and heavy-tailed: a small
number of valid sequences receive much larger probability than the rest. Increasing temperature
flattens the valid-sequence distribution, but it also shifts substantial probability mass into the invalid
17
region before the model approaches a uniform distribution over valid states. Thus, temperature
scaling again improves valid diversity only by sacrificing validity.
10
20
30
40
10 4
10 3
10 2
10 1
100
Tail
Sequence Index (sorted by probability)
Probability
T=0.5
T=1.0
T=1.6
T=2.0
Uniform
Figure 10: Sequence probability for random state generation task. Sequences are sorted by probability,
and probabilities are plotted in log-space. The “tail” section represents the total probability mass of
the invalid region.
D
Formal Definitions of Calibration
A decoding rule achieves high validity if it assigns high probability only on valid tokens at each time
step and it achieves high diversity if it explores many distinct tokens in G rather than concentrating
on only a few of them. Therefore, we define order and shape calibration as:
Definition D.1 (Calibration). Given y<t ∈Vt−1 and an LLM conditional distribution p,
1. (Order Calibration) p is order calibrated if for any valid token v ∈V and invalid token w ∈V,
it assigns a higher probability to the valid token, i.e., p(v | y<t) ≥p(w | y<t).
2. (Shape Calibration) p is shape calibrated if for any token v ∈V, it assigns probability mass to v
according to the number of valid continuations starting with v, i.e., p(v | y<t) ∝N(y<t ◦v).
Note that shape calibration is stronger than order calibration: even if order calibration is resolved,
shape calibration can still persist. However, perfect shape calibration is strictly harder than order
calibration.
Our notation of “calibration” is not directly related to LLM confidence calibration literature.
E
Analysis of Theorem 4.2
In this section, we provide a formal analysis of how local truncation decisions affect sequence-level
behavior. We restate the key definitions for completeness and give full proofs of the results in
Section 4.
E.1
Setup and notation
Fix a valid set V ⊆Vd. At each decoding step t, a rule retains a nonempty subset St(y<t) ⊆V and
samples
Yt ∼Unif(St(Y<t)).
Let QS denote the induced distribution over full sequences.
Let G(y<t) denote the set of valid next tokens, and let N(y<t) denote the number of valid completions
extending y<t.
Local precision and recall. For a prefix y<t, define
Prect(S; y<t) := |St(y<t) ∩G(y<t)|
|St(y<t)|
,
and
Rect(S; y<t) :=
P
v∈St(y<t)∩G(y<t) N(y<t ◦v)
N(y<t)
.
Sequence-level precision and recall.
Precseq(S) = QS(Y ∈V ),
Recseq(S) = |{y ∈V : yt ∈St(y<t) ∀t}|
|V |
.
18
E.2
Multiplicative decomposition
Theorem E.1 (Exact multiplicative decomposition).
Precseq(S) =
d
Y
t=1
αt(S),
Recseq(S) =
d
Y
t=1
βt(S),
where
αt(S) := EQS[Prect(S; Y<t) | Ys ∈G(Y<s) ∀s < t] ,
and
βt(S) := EUV [Rect(S; Y<t) | Ys ∈Ss(Y<s) ∀s < t] .
Proof. Define
Ft := {Ys ∈G(Y<s) for all s ≤t}.
A sequence is valid if and only if it preserves access to a valid continuation at every step, hence
{Y ∈V } = Fd. By the chain rule,
Precseq(S) = QS(Fd) =
d
Y
t=1
QS(Ft | Ft−1).
Conditioned on Ft−1 and Y<t, the next token is sampled uniformly from St(y<t), yielding
QS(Ft | Ft−1, Y<t) = Prect(S; y<t).
Taking expectations gives αt(S).
For recall, let UV denote the uniform distribution over V and define
Et := {Ys ∈Ss(Y<s) for all s ≤t}.
Then
Recseq(S) = UV (Ed) =
d
Y
t=1
UV (Et | Et−1).
Conditioned on Y<t, the next token under UV is distributed proportionally to continuation counts,
yielding Rect(S; y<t). Taking expectations gives βt(S).
Local trade-off view. The multiplicative decomposition shows that sequence-level precision and
recall are governed by accumulated local log-losses,
ut(S) := −log αt(S),
vt(S) := −log βt(S).
Thus, maintaining high sequence-level precision imposes a small total budget on the precision losses
P
t ut(S). Theorem E.3 formalizes the consequence: if many steps necessarily incur nontrivial recall
loss whenever their precision loss is small, then sequence-level recall must decay exponentially.
E.3
Compounding effect of hard decoding steps
Formalization of Theorem 4.2. The main text theorem states that if many decoding steps incur
an unavoidable loss in recall when enforcing high precision, then sequence-level recall decays
exponentially. We now formalize this statement.
Definition E.2 ((η, ρ)-hard step). Fix η, ρ > 0. A step t is (η, ρ)-hard if, for every decoding rule S,
ut(S) ≤η
=⇒
vt(S) ≥ρ.
Equivalently, whenever the local precision loss at step t is at most η, the local recall loss is at least ρ.
Theorem E.3 (Compounding effect of hard decoding steps). Suppose at least m decoding steps are
(η, ρ)-hard. Then any decoding rule satisfying
Precseq(S) ≥1 −δ
also satisfies
Recseq(S) ≤exp
 
−ρ

m −−log(1 −δ)
η

+
!
.
19
Proof. By the multiplicative decomposition,
d
X
t=1
ut(S) = −log Precseq(S) ≤−log(1 −δ).
Among the m hard steps, fewer than −log(1 −δ)/η steps can have ut(S) > η; otherwise the total
precision loss would exceed the budget. Therefore at least

m −−log(1 −δ)
η

+
hard steps satisfy ut(S) ≤η. For each such step, hardness implies vt(S) ≥ρ. Hence
−log Recseq(S) =
d
X
t=1
vt(S) ≥ρ

m −−log(1 −δ)
η

+
.
Exponentiating gives the result.
Interpretation. Maintaining high sequence-level precision imposes a constant total precision-loss
budget across all decoding steps. As the sequence length grows, most steps must operate in a
near-perfect regime. If many such steps still incur a fixed recall loss, these losses accumulate
multiplicatively, causing an exponential decay in the set of reachable valid sequences.
F
Analysis of Theorem 5.2
The main point is simple: if a model must place very high probability on valid tokens at each step,
then its next-token distribution must become sharper. But sharper distributions are less uniform
over the valid choices, which reduces validity-conditioned diversity. Since entropy losses add over
sequence positions, the diversity loss compounds with length.
Definition F.1 (Discrete geometric ranked model). Fix a temperature T > 0. At each valid prefix y<t,
assume that after sorting tokens by decreasing probability, the next-token distribution is geometric in
rank:
P (T )
t
(i | y<t) = (1 −qt)qi
t,
i = 0, 1, 2, . . . , |V| −1
where
qt = exp(−λt/T),
λt > 0.
Equivalently,
P (T )
t
(i | y<t) ∝exp(−λti/T).
For each position t, define the normalized sharpness
zt := λtvt
T .
This quantity measures how much the ranked distribution decays across the valid interval {0, . . . , vt −
1}.
For v ∈N+ and a > 0, define Hv(a) as the entropy of the tilted distribution
pv,a(i) =
exp(−ai/v)
Pv−1
j=0 exp(−aj/v)
,
i = 0, . . . , v −1.
When a = 0, this distribution is uniform over v tokens and has entropy ln v. When a > 0, it is tilted
toward smaller ranks, so its entropy is smaller.
Define the per-step entropy loss
∆v(a) := ln v −Hv(a).
This measures how much diversity is lost, at one step, relative to being uniform over the v valid
choices.
Definition F.2 (Diversity). Let Y ∼P (T )(· | x), and let V be the set of valid sequences. Define
Div(P (T )) := exp(H(Y | Y ∈V ))
|V |
.
This quantity equals 1 when the model is uniform over valid sequences after conditioning on validity.
It decreases when the conditional distribution over valid sequences becomes more concentrated.
20
Lemma F.3 (Entropy loss increases with sharpness). For every fixed v, the entropy loss
∆v(a) = ln v −Hv(a)
is nondecreasing in a. Moreover, if v ≥2 and a > 0, then
∆v(a) > 0.
Proof. Write θ = a/v and
Z(θ) =
v−1
X
j=0
e−θj.
For pθ(i) ∝e−θi,
Hv(a) = log Z(θ) + θEθ[i].
Hence
d
dθHv(a) = θ d
dθEθ[i] = −θ Varθ(i) ≤0.
Since θ = a/v, Hv(a) is nonincreasing in a, so ∆v(a) = log v −Hv(a) is nondecreasing. If v ≥2
and a > 0, then pv,a is nonuniform, so Hv(a) < log v and ∆v(a) > 0.
Theorem F.4 (discrete validity–diversity trade-off). Assume the discrete geometric ranked model
and invariant valid branching. Let
L := ln ϵ−1.
If
Val(P (T )) ≥1 −ϵ,
then
Div(P (T )) ≤exp
 
−
d
X
t=1
∆vt(L)
!
.
Equivalently,
Div(P (T )) ≤exp
 
−
d
X
t=1
 ln vt −Hvt(ln ϵ−1)

!
.
In particular, stricter validity requirements force a smaller upper bound on validity-conditioned
diversity: as ϵ decreases, L = ln ϵ−1 increases, and each entropy-loss term ∆vt(L) increases.
Proof. At position t, the valid next tokens are the first vt ranked tokens. Therefore, the local
probability of choosing a valid next token is
P (T )
t
(Yt ∈Gt(y<t) | y<t) =
vt−1
X
i=0
(1 −qt)qi
t
= 1 −qvt
t .
Since
qt = exp(−λt/T),
we have
qvt
t = exp(−λtvt/T) = e−zt.
Thus the local validity probability is
1 −e−zt.
By invariant valid branching, the full-sequence validity factorizes:
Val(P (T )) =
d
Y
t=1
(1 −e−zt).
Suppose
Val(P (T )) ≥1 −ϵ.
Since the product is no larger than any individual factor, for every t,
1 −ϵ ≤
d
Y
s=1
(1 −e−zs) ≤1 −e−zt.
21
Therefore
e−zt ≤ϵ,
which implies
zt ≥ln ϵ−1 = L.
Now condition on the event that the generated sequence is valid. At position t, conditioned on
choosing one of the vt valid tokens, the rank distribution is
pvt,zt(i) =
exp(−zti/vt)
Pvt−1
j=0 exp(−ztj/vt)
,
i = 0, . . . , vt −1.
Its entropy is Hvt(zt).
By the chain rule for entropy,
H(Y | Y ∈V ) =
d
X
t=1
Hvt(zt).
Also, by invariant valid branching,
|V | =
d
Y
t=1
vt.
Therefore
Div(P (T )) = exp(H(Y | Y ∈V ))
|V |
= exp
 d
X
t=1
Hvt(zt) −
d
X
t=1
ln vt
!
= exp
 
−
d
X
t=1
 ln vt −Hvt(zt)

!
.
By Lemma F.3, entropy loss is nondecreasing in sharpness. Since zt ≥L, we have
ln vt −Hvt(zt) ≥ln vt −Hvt(L) = ∆vt(L).
Plugging this into the previous display gives
Div(P (T )) ≤exp
 
−
d
X
t=1
∆vt(L)
!
.
This proves the desired bound.
Finally, because each ∆vt(L) is nondecreasing in L, and because L = ln ϵ−1 increases as ϵ decreases,
stricter validity requirements force a smaller upper bound on validity-conditioned diversity.
Corollary F.5 (Exponential diversity loss in branching length). Let
m := |{t ∈[d] : vt ≥2}|
be the branching length, and define
cV(ϵ) :=
min
2≤v≤|V| ∆v(ln ϵ−1).
For every ϵ ∈(0, 1), we have cV(ϵ) > 0 and
Div(P (T )) ≤exp(−m cV(ϵ)) .
In particular, if every position has at least two valid next-token choices, then m = d, and validity-
conditioned diversity decays exponentially in sequence length.
Proof. Theorem F.4 gives
Div(P (T )) ≤exp
 
−
d
X
t=1
∆vt(ln ϵ−1)
!
.
22
Terms with vt = 1 contribute no branching diversity. For every term with vt ≥2,
∆vt(ln ϵ−1) ≥cV(ϵ).
There are m such terms, so
d
X
t=1
∆vt(ln ϵ−1) ≥m cV(ϵ).
Finally, cV(ϵ) > 0 because it is the minimum of finitely many strictly positive entropy losses. This
proves the claim.
Corollary F.6 (Two regimes of the diversity loss). Let L := ln ϵ−1, and define
cV(ϵ) :=
min
2≤v≤|V| ∆v(L).
Then
Div(P (T )) ≤exp(−m cV(ϵ)) .
Moreover, cV(ϵ) has the following two regimes:
cV(ϵ) = 1
32L2 + O(L3),
L →0,
and
cV(ϵ) →ln 2,
L →∞.
Equivalently, in the weak-validity regime,
Div(P (T )) ≤exp

−m
 1
32L2 + O(L3)

,
while in the stringent-validity regime,
Div(P (T )) ≤exp(−m(ln 2 −o(1))) = 2−m+o(m).
Proof. The first inequality follows directly from Corollary F.5 with c(ϵ) replaced by the finite-
vocabulary minimum cV(ϵ).
We now prove the two asymptotic regimes. Recall that
∆v(L) = DKL(pv,L ∥Uv) ,
where Uv is uniform on {0, . . . , v −1} and pv,L(i) ∝e−Li/v.
For L →0, pv,L is a small exponential tilt of Uv. The standard second-order expansion of KL
divergence gives
∆v(L) = L2
2 VarUv
 i
v

+ O(L3).
Since
VarUv
 i
v

= v2 −1
12v2 ,
we obtain
∆v(L) = v2 −1
24v2 L2 + O(L3).
The coefficient
v2 −1
24v2
is increasing in v ≥2, so the minimum over 2 ≤v ≤|V| is attained at v = 2. Hence
cV(ϵ) = ∆2(L) = 1
32L2 + O(L3).
For L →∞, fix any finite v. Then pv,L concentrates on the top-ranked token, so
Hv(L) →0,
∆v(L) = ln v −Hv(L) →ln v.
Because the minimum is over the finite set {2, . . . , |V|}, we may pass the limit through the minimum:
cV(ϵ) =
min
2≤v≤|V| ∆v(L) →
min
2≤v≤|V| ln v = ln 2.
23
Valparaíso, Chile
Valparaíso, Chile.
Lisbon, Portugal.
Lisbon, Portugal
Reykjavík, Iceland.
Reykjavík, Iceland
Kyoto, Japan
Tbilisi, Georgia.
Melbourne, Australia
Valencia, Spain.
Medellín, Colombia
Copenhagen, Denmark
Marrakesh, Morocco
Porto, Portugal.
Quito, Ecuador
Copenhagen, Denmark.
Busan, South Korea.
Osaka, Japan
Tallinn, Estonia
Kyoto, Japan.
Others
Model Outputs
0
100
200
300
400
500
Count
Figure 11: Prompting GPT-5.5 to randomly name a city in the world. The vast majority of answers,
with or without user chat history, collapses to “Valparaíso, Chile.” This shows a strong collapse in
diversity.
Substituting these two asymptotics into
Div(P (T )) ≤exp(−m cV(ϵ))
gives the claimed diversity bounds.
Interpretation. The result shows that high validity requires every local invalid-token probability to
be small. In the geometric ranked model, this forces large normalized sharpness zt. After conditioning
on validity, the distribution over the vt valid choices is therefore tilted rather than uniform, causing
an entropy loss ∆vt(zt) at each branching position. Since entropy losses add over positions, the
exponentiated diversity decays multiplicatively, yielding
Div(P (T )) ≤exp(−m cV(ϵ)).
G
Experiments with Production-Level Models
In Figure 11, we prompted GPT-5.5 with the prompt “Name a random city in the world”, with default
thinking level and temperature. The models response almost always lie in a limited set of few cities.
H
Case Study: Calibration in Coding
We examine the distributional properties of LLMs in a simple coding setting. Although diversity
is not inherently the primary objective in coding tasks, prior work has shown that greedy decoding
is often suboptimal. Instead, Yue et al. [47] advocate evaluating models using the pass@k metric,
which measures whether at least one of k sampled solutions correctly solves the task. This highlights
the importance of effective sampling even in domains where a single correct answer suffices.
Figure 12 illustrates sequence-level probability distributions on a coding task from Live-
CodeBench [17]. We observe clear evidence of both order and shape miscalibration. Valid solutions
are interspersed with invalid ones throughout the ranked distribution [20], indicating poor order
calibration. At the same time, probability mass is unevenly concentrated across valid solutions, with
a small subset dominating the distribution, reflecting shape miscalibration.
These results show that our framework helps diagnose model failures beyond diversity alone, provid-
ing a lens to understand why sampling-based improvements such as higher pass@k remain difficult
to achieve in practice.
24
0
10
20
30
40
50
Sequence Index (sorted by log probability)
0.0
0.5
1.0
1.5
2.0
2.5
Sequence-Log Probabilities
Valid
Invalid
Figure 12: Sequence-level probability distribution for a coding task from LiveCodeBench [17], with
sequences sorted by log-probability. Valid and invalid solutions are intermixed across the ranking
(order miscalibration), and probability mass is concentrated on a small subset of valid solutions
(shape miscalibration).
I
Empirical Analysis of Logits
To investigate the logits distribution, we fit the logits at each generation conditional to a piecewise
model, defined as
f(k) =
mk + b,
k ≤c,
A + B log(k + C),
k > c,
where k refers to the logit index and f(k) the corresponding logit value. To find c, we sweep over
all token indexes. Figures 13, 14, 15 show the curve fit and MSE, R2 of fitting to various tasks and
conditionals. Results show that LLM conditionals are consistently sharp-headed and heavy-tailed.
J
Limitations
Our work studies diversity collapse through the lens of validity–diversity calibration. This perspec-
tive is useful because it connects output-level diversity failures to local properties of the model’s
conditional distributions. However, several limitations should be noted.
Controlled tasks are diagnostic rather than exhaustive. A substantial part of our empirical analysis
uses controlled random-number generation tasks, where the valid set can be characterized exactly.
This allows us to compute validity and diversity without relying on noisy semantic judgments, and
makes it possible to isolate the effects of shape and order calibration. However, these tasks are not
intended to capture the full complexity of open-ended generation. In domains such as creative writing,
scientific ideation, dialogue, or planning, validity is semantic, context-dependent, and often graded
rather than binary. Therefore, our controlled experiments should be interpreted as diagnostics for
specific distributional mechanisms, not as a complete account of all diversity failures in realistic
generation settings.
Token-level validity labels are approximate in open-ended settings. For open-ended tasks, the
valid-token set is not directly observable. Our empirical procedure approximates token validity by
extending a prefix with a candidate token, greedily decoding a completion, and then evaluating the
final sequence with an LLM judge. This provides a practical estimate of whether a token preserves
access to a valid continuation, but it is not an exact characterization of the true valid-token set: a
token that leads to an invalid greedy continuation may still admit valid continuations under another
decoding path.
To assess the reliability of this approximation, we conduct a human validation study comparing
judge-based labels against human annotations. This helps quantify the extent to which the LLM
judge agrees with human judgments and reduces concern that our precision–recall estimates are
artifacts of a particular judge model. Nevertheless, the labels remain approximate, since both human
and model judgments depend on the task rubric, validity threshold, and the particular continuation
used for evaluation. Our controlled random-number experiments avoid this source of noise by using
algorithmically known validity.
25
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.12709
R²: 0.96355
Cutoff: 18
Query: What is 3+6?          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.02121
R²: 0.99620
Cutoff: 6
Query: Name a random city in the world.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.00785
R²: 0.99814
Cutoff: 12
Query: Write a creative story.          Model Response: In a world where_______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.15679
R²: 0.96825
Cutoff: 2
Query: Generate a random integer in the range 1 to 10.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.15954
R²: 0.96604
Cutoff: 2
Query: Generate a random integer in the range 1 to 20.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.25578
R²: 0.95653
Cutoff: 26
Query: Generate 3 random integers in the range 1 to 20.          Model Response: 1,_______
Figure 13: Logit fitting on Llama-3.1-8B-Instruct
The theoretical models isolate mechanisms under stylized assumptions. Our theoretical results
are designed to formalize clean mechanisms rather than to fully model all LLM distributions. In
particular, the shape calibration analysis uses a ranked geometric distribution and, in its cleanest form,
assumes invariant valid branching across prefixes. These assumptions make it possible to show how
local sharpness and entropy losses compound across sequence positions. Real LLM conditionals
26
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.01531
R²: 0.99386
Cutoff: 2
Query: What is 3+6?          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.00319
R²: 0.99928
Cutoff: 7
Query: Name a random city in the world.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.00893
R²: 0.99754
Cutoff: 18
Query: Write a creative story.          Model Response: In a world where_______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.10603
R²: 0.95869
Cutoff: 17
Query: Generate a random integer in the range 1 to 10.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.11054
R²: 0.95894
Cutoff: 15
Query: Generate a random integer in the range 1 to 20.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
30
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
30
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
30
MSE: 0.07768
R²: 0.96685
Cutoff: 15
Query: Generate 3 random integers in the range 1 to 20.          Model Response: 1,_______
Figure 14: Logit fitting on Qwen3.5-35B-A3B
may have heterogeneous branching factors, non-geometric tails, prefix-dependent valid sets, and
interactions between syntax, semantics, and instruction-following constraints. The theory should
therefore be read as a mechanistic explanation of why validity–diversity trade-offs can arise, rather
than as a literal generative model of all LLM behavior.
27
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.05179
R²: 0.97631
Cutoff: 2
Query: What is 3+6?          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.02803
R²: 0.98727
Cutoff: 56
Query: Name a random city in the world.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.00103
R²: 0.99959
Cutoff: 14
Query: Write a creative story.          Model Response: In a world where_______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.06204
R²: 0.97616
Cutoff: 13
Query: Generate a random integer in the range 1 to 10.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.20224
R²: 0.94744
Cutoff: 28
Query: Generate a random integer in the range 1 to 20.          Model Response: _______
1
25
50
75
100
Token Index (sorted by logit value)
10
0
10
20
Logit Value
1
250
500
750
1000
Token Index (sorted by logit value)
10
0
10
20
1
500
1000
1500
2000
Token Index (sorted by logit value)
10
0
10
20
MSE: 0.34680
R²: 0.93408
Cutoff: 27
Query: Generate 3 random integers in the range 1 to 20.          Model Response: 1,_______
Figure 15: Logit fitting on Olmo-3-7B-Instruct
Oracle baselines are diagnostic, not deployable. Several experiments use oracle information, such
as the ground-truth valid-token set size or exact validity constraints in controlled tasks. These oracle
baselines are not meant to be practical decoding methods. Their purpose is to separate failure modes.
For example, an oracle-size cutoff tests whether a rank-based method would improve if it knew the
correct local support size, while still failing when valid and invalid tokens are interleaved in rank.
28
Thus, oracle performance should be interpreted as evidence about the source of the bottleneck, not as
a directly available inference-time algorithm.
Sequence-level experiments are limited by sequence depth. Exact validity–diversity computation
becomes expensive as sequence length grows, because the number of possible continuations increases
rapidly. This limits the lengths and branching structures that can be exhaustively evaluated in
controlled settings. Our experiments therefore emphasize short-to-moderate horizons where exact
computation is feasible. The theory predicts that the relevant losses compound with the number of
branching positions, but larger-scale empirical validation over longer sequences remains an important
direction for future work.
This work diagnoses rather than solves the bottleneck. Our goal is to identify distributional
mechanisms that constrain validity and diversity during decoding. We do not propose a new decoding
algorithm or training objective that fully resolves these issues. The results suggest that effective
solutions may need to improve the model’s conditional calibration directly, or use auxiliary validity
signals that go beyond probability rank. Designing such calibration-aware training or decoding
methods is left for future work.
K
Compute Resources
We conduct our experiments on 8 NVIDIA A6000 GPUs. For experiments on commercial models,
we use the corresponding official API endpoints. Open-source LLM inference is conducted through
the vLLM [24] package. The total computing time required to reproduce all our generations and
evaluate the results is around 1 week.
L
Societal Impacts
Our work directly addresses the frontiers of LLM inference. In particular, our work aims to understand
the validity and diversity of LLM-generated outputs through fine-grained token control. Although we
observe no evidence for harmful content in our experiments, the token-level control could potentially
lead to instances where sensitive/harmful content is produced. However, our method does not attempt
to jailbreak or induce unsafe behavior in any model.
On a high level, work incentivizing LLM generation diversity can produce novel ideas and solutions to
societal problems, but also increase risk of biased content. Advancing model diversity and capability
while guaranteeing trustworthiness and safety remains a high priority in this and all future works.
29
