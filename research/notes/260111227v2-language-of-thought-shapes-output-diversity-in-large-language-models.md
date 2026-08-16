---
title: '[2601.11227v2] Language of Thought Shapes Output Diversity in Large Language
  Models'
id: 260111227v2-language-of-thought-shapes-output-diversity-in-large-language-models
tags:
- llm-nas-feedback-positioning-7125b1
- output-diversity
- mode-collapse
- rival-explanation
- decoding-strategy
created: '2026-08-16T15:44:17.652883Z'
updated: '2026-08-16T15:47:25.791038Z'
source: https://arxiv.org/abs/2601.11227v2
source_domain: arxiv.org
fetched_at: '2026-08-16T15:44:17.652439Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Xu & Zhang (submitted Jan 2026, revised Apr 2026, ACL 2026) show that the
  ''language of thought'' used during an LLM''s internal reasoning is a structural,
  controllable lever on output diversity independent of the final output language:
  switching the thinking language from English to non-English languages consistently
  increases output diversity, with languages farther from English in ''thinking space''
  yielding larger diversity gains, and aggregating samples across multiple thinking
  languages compounds the effect (raising the model''s diversity ceiling). Relevant
  as rival-explanation literature for Q2/mode-collapse: it demonstrates that generation-time/prompting-side
  factors (here, latent ''thinking language'') independently modulate output diversity
  in ways separable from model scale or quantization, reinforcing that diversity collapse
  (e.g., a small quantized model producing near-identical architecture proposals)
  cannot be attributed to a single cause without ruling out such confounds — decoding/thinking-space
  choices, not just RLHF or quantization, can suppress or restore diversity.'
---

[2601.11227v2] Language of Thought Shapes Output Diversity in Large Language Models
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2601.11227v2
(cs)
[Submitted on 16 Jan 2026 (
v1
), last revised 16 Apr 2026 (this version, v2)]
Title:
Language of Thought Shapes Output Diversity in Large Language Models
Authors:
Shaoyang Xu
,
Wenxuan Zhang
View a PDF of the paper titled Language of Thought Shapes Output Diversity in Large Language Models, by Shaoyang Xu and 1 other authors
View PDF
HTML (experimental)
Abstract:
Output diversity is crucial for Large Language Models as it underpins pluralism and creativity. In this work, we reveal that controlling the language used during model thinking-the language of thought-provides a novel and structural source of output diversity. Our preliminary study shows that different thinking languages occupy distinct regions in a model's thinking space. Based on this observation, we study two repeated sampling strategies under multilingual thinking-Single-Language Sampling and Mixed-Language Sampling-and conduct diversity evaluation on outputs that are controlled to be in English, regardless of the thinking language used. Across extensive experiments, we demonstrate that switching the thinking language from English to non-English languages consistently increases output diversity, with a clear and consistent positive correlation such that languages farther from English in the thinking space yield larger gains. We further show that aggregating samples across multiple thinking languages yields additional improvements through compositional effects, and that scaling sampling with linguistic heterogeneity expands the model's diversity ceiling. Finally, we show that these findings translate into practical benefits in pluralistic alignment scenarios, leading to broader coverage of cultural knowledge and value orientations in LLM outputs. Our code is publicly available at
this https URL
.
Comments:
acl2026
Subjects:
Computation and Language (cs.CL)
; Computers and Society (cs.CY)
Cite as:
arXiv:2601.11227
[cs.CL]
(or
arXiv:2601.11227v2
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2601.11227
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Shaoyang Xu [
view email
]
[v1]
Fri, 16 Jan 2026 12:14:16 UTC (317 KB)
[v2]
Thu, 16 Apr 2026 10:50:27 UTC (319 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Language of Thought Shapes Output Diversity in Large Language Models, by Shaoyang Xu and 1 other authors
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
2026-01
Change to browse by:
cs
cs.CY
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

## Full text (recovered via direct extraction)

Language of Thought Shapes Output Diversity in Large Language Models
Shaoyang Xu, Wenxuan Zhang*
iNLP Lab, Singapore University of Technology and Design
shaoyang_xu@mymail.sutd.edu.sg, wxzhang@sutd.edu.sg
Abstract
Output diversity is crucial for Large Language
Models as it underpins pluralism and creativ-
ity. In this work, we reveal that controlling the
language used during model thinking—the lan-
guage of thought—provides a novel and struc-
tural source of output diversity. Our prelim-
inary study shows that different thinking lan-
guages occupy distinct regions in a model’s
thinking space.
Based on this observation,
we study two repeated sampling strategies un-
der multilingual thinking—Single-Language
Sampling and Mixed-Language Sampling—and
conduct diversity evaluation on outputs that
are controlled to be in English, regardless of
the thinking language used.
Across exten-
sive experiments, we demonstrate that switch-
ing the thinking language from English to
non-English languages consistently increases
output diversity, with a clear and consistent
positive correlation such that languages far-
ther from English in the thinking space yield
larger gains.
We further show that aggre-
gating samples across multiple thinking lan-
guages yields additional improvements through
compositional effects, and that scaling sam-
pling with linguistic heterogeneity expands the
model’s diversity ceiling. Finally, we show that
these findings translate into practical benefits
in pluralistic alignment scenarios, leading to
broader coverage of cultural knowledge and
value orientations in LLM outputs. Our code
is publicly available at https://github.com/
iNLP-Lab/Multilingual-LoT-Diversity.
1
Introduction
Large Language Models (LLMs) have been glob-
ally adopted due to their extensive knowledge and
strong reasoning capabilities. Beyond the correct-
ness of individual responses, this widespread use
has drawn increasing attention to the diversity of
LLM-generated outputs. Formally, output diversity
*Corresponding author
quantifies a model’s ability to generate multiple
distinct responses to open-ended questions without
ground-truth answers (Jiang et al., 2025; Zhang
et al., 2025b). It is recognized as a fundamental ob-
jective in pluralistic alignment research (Sorensen
et al., 2024; Conitzer et al., 2024), where low
diversity can lead to homogenization—often re-
ferred to as mode collapse (Jiang et al., 2025;
Zhang et al., 2025b; Lagzian et al., 2025)—and
the over-representation of dominant cultural val-
ues (AlKhamissi et al., 2024; Wang et al., 2024).
Moreover, diversity is a key indicator of whether
AI systems exhibit human-like creativity (Pépin
et al., 2024), laying the foundation for innovative
problem-solving (Ye et al., 2025; Tian et al., 2024;
Chen et al., 2025b; Han et al., 2025), open-ended
exploration, and the generation of novel ideas (Guo
et al., 2025a; Ruan et al., 2024).
To improve output diversity, temperature scal-
ing is commonly utilized by increasing sampling
randomness (Pépin et al., 2024; Tevet and Berant,
2021; Peeperkorn et al., 2024). Other work ex-
plored advanced decoding methods (Peeperkorn
et al., 2025), aggregating outputs from multiple
LLMs (Liang et al., 2024a; Shur-Ofry et al., 2024;
Tekin et al., 2024), or increasing prompt varia-
tion (Shur-Ofry et al., 2024; Lagzian et al., 2025;
Wang et al., 2025a). At training time, several stud-
ies proposed diversity-driven RLHF and SFT ob-
jectives to encourage more varied generations (Li
et al., 2025b; Sun et al., 2025).
Despite their promise, most existing work fo-
cuses on English-only or multilingual input set-
tings (Wang et al., 2025a).
In contrast, lever-
aging the inherently multilingual nature of mod-
ern LLMs (Zhao et al., 2025b; Zhang et al.,
2025a; Yang et al., 2025; Zhang, 2026), we in-
vestigate whether the language used during inter-
mediate thinking—referred to as the language of
thought—can serve as a controllable and structural
source of output diversity. Our investigation is mo-
arXiv:2601.11227v2  [cs.CL]  16 Apr 2026

tivated by two observations. First, insights from
cognitive science suggest that multilingualism pro-
motes divergent thinking and creativity, as different
languages encode distinct conceptual and structural
biases (Blasi et al., 2022; Kharkhurin et al., 2023).
According to the Sapir–Whorf hypothesis (Whorf,
2012), language can shape how concepts are or-
ganized and related during thinking. Second, re-
cent studies have demonstrated that modern LLMs
are capable of explicit reasoning in multiple lan-
guages, with performance differences across lan-
guages (Yong et al., 2025; Qi et al., 2025). To-
gether, these insights motivate us to study language
of thought as a structural property of the model’s
thinking process, and to examine how varying this
property influences output diversity.
To this end, we begin with a preliminary study
that explores whether different thinking languages
induce structural differences in the model’s think-
ing space (§3). Specifically, given the same En-
glish input, we control the thinking process to be
conducted in different languages and collect the
resulting hidden representations. By visualizing
these multilingual thinking representations, we ob-
serve that different languages correspond to distinct
regions in the model’s thinking space. Moreover,
non-English languages exhibit substantial variation
in their distances to English thinking. These ob-
servations reveal geometric differences induced by
different languages of thought.
Building on these observations, we next exam-
ine whether the thinking-space shifts induced by
different languages of thought help output diver-
sity (§4&5). Although the thinking process is con-
trolled to be conducted in different languages, we
further control the model’s final outputs to English
for fair output diversity evaluation (§4.1). Based on
this setup, we perform repeated sampling and ag-
gregate the resulting English outputs for diversity
evaluation. Specifically, we explore two sampling
strategies. The first, Single-Language Sampling,
performs repeated sampling within a single think-
ing language (§4.2). The second, Mixed-Language
Sampling, aggregates English outputs generated
through thinking in different languages (§4.3).
We conduct experiments on two benchmarks us-
ing two different diversity metrics. Multiple LLMs
and 15 thinking languages are evaluated (§5.1).
Our main findings are as follows.
First, under Single-Language Sampling, we ob-
serve that simply switching the language of thought
from English to non-English languages consis-
tently leads to higher output diversity.
By fur-
ther computing the correlation between output
diversity and the thinking-space distance to En-
glish across non-English languages, we identify
a clear positive relationship: thinking languages
that are geometrically farther from English consis-
tently achieve higher output diversity. These re-
sults demonstrate that sampling within thinking re-
gions outside the English-dominant space can sys-
tematically mitigate output homogenization. We
also evaluate output quality and find that thinking
in non-English languages incurs only negligible
degradation (§5.2).
Second, we further find that Mixed-Language
Sampling yields additional gains in output diversity.
This result indicates that sampling from distinct
thinking regions induced by linguistic heterogene-
ity can further enhance output diversity beyond a
single region. Further analysis reveals clear compo-
sitional effects among languages: while removing
any single language has a relatively small impact,
removing multiple languages leads to substantially
greater degradation in diversity (§5.3).
Third, we analyze the effects of the sampling
number and temperature, and find that Mixed-
Language Sampling exhibits a pronounced advan-
tage over Single-Language Sampling when fur-
ther scaling the sampling number, highlighting the
role of linguistic heterogeneity in expanding the
model’s diversity ceiling (§5.4).
Finally, we extend our analysis to pluralistic
alignment scenarios (§6). Our results show that
Mixed-Language Sampling leads to broader cov-
erage of cultural knowledge and values in LLMs,
outperforming other sampling strategies, includ-
ing English sampling, high-temperature decoding,
explicit diversity requests, and multilingual prompt-
ing. These results highlight the practical utility of
our findings in real-world applications.
Overall, our findings establish the language of
thought as a novel and effective control axis for
enhancing output diversity.
2
Related Work
Output Diversity of LLMs
Many studies have
shown that LLMs often exhibit limited output di-
versity (Padmakumar and He, 2024; Liang et al.,
2024b; Luo et al., 2024; Giorgi et al., 2024). Output
diversity evaluation typically considers lexical, syn-
tactic, and semantic dimensions (Guo et al., 2024,
2025b; Lagzian et al., 2025), and employs tools

such as Self-BLEU (Zhu et al., 2018) and Sentence-
BERT (Reimers and Gurevych, 2019) to compute
diversity metrics in NLG tasks (Guo et al., 2024).
Moreover, diversity is often evaluated alongside
novelty and creativity in more complex generation
settings (Zhang et al., 2025b; Lagzian et al., 2025;
Pépin et al., 2024; Ye et al., 2025; Tian et al., 2024).
Recently, NOVELTYBENCH (Zhang et al., 2025b)
and INFINITY-CHAT (Jiang et al., 2025) were in-
troduced to assess the ability of LLMs to produce
distinct outputs in open-domain dialogue.
Existing approaches to improve output diver-
sity include aggregating outputs from multiple
LLMs (Liang et al., 2024a; Shur-Ofry et al., 2024),
increasing prompt variation (Liang et al., 2024a;
Lagzian et al., 2025; Wang et al., 2025a), and de-
veloping diversity-driven RLHF and SFT objec-
tives (Li et al., 2025b; Sun et al., 2025). Unlike
these approaches, our work explores the inherent
multilingual properties of LLMs as a structural
source of output diversity.
Multilingual Reasoning
Modern LLMs are
trained to perform explicit intermediate reason-
ing before producing final answers (Muennighoff
et al., 2025; Zeng et al., 2025; DeepSeek-AI et al.,
2025). As LLMs increasingly exhibit a shared—yet
still imbalanced—thought space across different
languages (Chen et al., 2025c; Zhao et al., 2024,
2025a), many studies have explored the multilin-
gual generalization of LLM reasoning (Son et al.,
2025; Yong et al., 2025; Wang et al., 2025b; Ba-
jpai and Chakraborty, 2025; Qi et al., 2025; Tam
et al., 2025; Khairi et al., 2025). Other work has
investigated whether multilingualism can improve
the performance (Li et al., 2025a; Gao et al., 2025,
2026) and efficiency (Ahuja et al., 2025; Chen et al.,
2025a) of reasoning. However, none of these stud-
ies have examined whether multilingual thinking
can enhance the output diversity of LLMs.
3
Language Geometry of Thinking Space
We first conduct a preliminary study to examine
whether different thinking languages induce struc-
tural differences in the model’s thinking space.
3.1
Thinking Language Control
All of our investigations focus on reasoning-
capable LLMs. Given an English input prompt,
the model first performs intermediate thinking T,
enclosed within <think>...</think>, and then
generates the final output o, both in English by
default.
To control the LLM to perform its intermediate
thinking in a target language l, we follow exist-
ing multilingual reasoning techniques (Yong et al.,
2025; Qi et al., 2025). Specifically, we insert a short
prefix, “Okay, the user is asking”—translated
into l— immediately after the <think> token, guid-
ing the subsequent thinking process to be con-
ducted in the target language. The translated pre-
fixes, together with a sanity check of the language
control, are provided in Appendix A.1.
3.2
Visualizing Multilingual Thinking Space
Collecting Hidden States
Given a set of English
input questions, we apply thinking language con-
trol to encourage the model to perform thinking in
language l for each sample. For a single sample, let
the thinking process consist of N tokens {t(l)
i }N
i=1,
and let h(l)
i,j denote the hidden state of token t(l)
i
at
layer j. To obtain a compact representation of the
model’s thinking behavior, we first average hidden
states across all thinking tokens within a sample,
and then further average across all samples. This
yields a single vector representation h(l)
j
that sum-
marizes the model’s thinking behavior in language
l at layer j. Repeating this process for all think-
ing languages produces a set of language-specific
thinking representations at each layer.
PCA Visualization
To visualize the geometry
of multilingual thinking space, we first normal-
ize all language representations using ℓ2 normal-
ization. Viewing English as the anchor, we then
compute the cosine distance between each non-
English language l and English at layer j as
dj(l, en) = 1 −cos

h(l)
j , h(en)
j

. Finally, we ap-
ply PCA to the centered representations to obtain
a two-dimensional layout for visualization. In the
resulting plot, PCA determines only the angular ar-
rangement of languages, while the radial distance
of each point is explicitly fixed to its cosine dis-
tance to English, i.e., dj(l, en).
3.3
Observations
We select 14 non-English languages together with
English that are officially supported by Qwen3-
8B (Yang et al., 2025) to analyze the multilingual
thinking space of the model. Figure 1 shows the
resulting geometry at several representative model
layers.

Figure 1: Language geometry of thinking space on
Qwen3-8B, with different distance scales across lay-
ers for visualization purposes.
Geometric Separation across Thinking Lan-
guages
We first observe clear geometric sepa-
ration among thinking representations induced by
different thinking languages: representations cor-
responding to different languages tend to occupy
separable regions in the model’s thinking space.
This separation holds consistently across model
layers, including intermediate layers that are often
assumed to be relatively abstract and less language-
specific (Pires et al., 2019). These observations
indicate the presence of language-correlated geo-
metric structure in the model’s thinking space.
Varied Distances to English Thinking
We fur-
ther observe systematic variation in the geometric
distance between non-English languages and En-
glish. Some languages (e.g., zh, fr, es, de) con-
sistently appear closer to English, whereas others
(e.g., iw, bg, tl) are embedded farther away. Over-
all, these results indicate that different languages
of thought occupy distinct regions of the model’s
thinking space, with varied distances to English.
4
Repeated Sampling under Multilingual
Thinking
In this and following sections, we further inves-
tigate whether the thinking-space shifts induced
by different languages of thought translate into
greater output diversity. In this section, we first
introduce a controlled output setting and two re-
peated sampling strategies. The resulting outputs
are used for diversity evaluation in Section 5.
4.1
Output Language Control
Although the model’s intermediate thinking T is
controlled to be conducted in a specific language
and enclosed within <think>...</think> (Sec-
tion 3.1), we further constrain the final output o
to English to enable fair output diversity evalua-
tion. This is achieved by inserting an additional
English prefix immediately after </think>—Let
me provide my answer in English only:—
to guide the model to generate the final response
in English. Only the English final outputs are col-
lected for subsequent output diversity evaluation.
Appendix A.1 provides a sanity check indicating
that both the thinking and output segments largely
follow the intended language control.
4.2
Single-Language Sampling
Section 3.3 shows that different non-English lan-
guages occupy distinct thinking regions with vary-
ing distances from English. This motivates us to ex-
amine whether switching to a thinking region away
from English and performing repeated sampling
within that region leads to increased output diver-
sity. To this end, we introduce the first repeated
sampling strategy, Single-Language Sampling.
Given an English input, the model’s intermediate
thinking is constrained to a fixed thinking language
l, while the final output is generated in English. We
then sample the model M times under this fixed
thinking language, and aggregate the resulting En-
glish outputs into a set Ol for diversity evaluation.
4.3
Mixed-Language Sampling
We further examine whether sampling from distinct
thinking regions induced by different languages
can yield additional gains in output diversity. This
setting allows us to investigate the compositional
effects of multiple thinking languages on output
diversity. We thus introduce our second repeated
sampling strategy, Mixed-Language Sampling.
Specifically, given an English input, we sam-
ple the model M times, each time controlling the
model to perform intermediate thinking in a dif-
ferent language, while keeping the final output in
English. The resulting outputs are aggregated into
a set of outputs Omixed, on which the same diversity
evaluation is conducted.

en
it
ms
zh
ru
de
iw
bg
da
no
sv
es
tl
oc
fr
avg (non-en)
Distinct Score ↑
Qwen3-8B
28.55
34.60
33.47
29.00
34.14
35.67
41.33
39.80
36.03
39.69
36.73
32.33
38.35
38.87
33.93
36.00
Qwen3-14B
26.20
30.67
29.23
28.80
31.40
28.93
36.87
32.13
30.13
34.55
32.33
29.73
32.68
33.26
29.53
31.45
Qwen3-32B
35.00
39.33
37.78
37.80
38.67
39.73
43.38
39.93
40.67
40.22
41.80
39.73
41.41
42.96
40.80
40.30
DeepSeek-14B
38.33
43.47
38.07
41.33
44.60
41.14
49.63
47.13
51.85
52.40
50.60
43.60
52.42
45.93
42.27
46.03
Similarity Score ↓
Qwen3-8B
87.28
85.43
86.53
86.73
85.57
85.14
83.66
84.89
84.79
83.93
85.14
85.76
83.20
80.79
84.57
84.72
Qwen3-14B
87.82
86.68
87.30
86.89
87.20
87.78
85.04
86.94
86.81
86.17
86.46
87.35
87.36
85.72
87.19
86.78
Qwen3-32B
82.10
80.59
81.76
81.61
80.67
78.00
79.64
81.45
79.78
79.54
79.06
79.84
79.71
77.65
80.62
79.99
DeepSeek-14B
81.15
79.98
83.28
82.11
80.17
81.08
76.16
81.34
77.56
77.61
79.27
81.12
76.70
79.81
81.88
79.86
Output Quality ↑
Qwen3-8B
96.82
95.86
95.72
95.53
96.11
96.69
95.53
96.04
95.09
95.00
96.82
95.72
95.70
95.59
95.40
95.80
Qwen3-14B
96.93
94.94
95.48
95.03
94.70
96.03
96.50
96.00
96.10
96.78
96.16
95.79
95.49
95.87
95.75
95.80
Qwen3-32B
97.36
96.08
95.85
96.22
95.36
94.47
95.57
97.07
95.52
96.87
95.96
94.97
96.04
96.19
94.26
95.70
DeepSeek-14B
95.84
94.75
93.94
94.71
93.69
93.27
89.17
94.52
92.95
92.60
93.66
94.93
90.73
95.45
95.80
93.60
Table 1: Distinct Score (%), Similarity Score (%), and Output Quality across models and thinking languages under
Single-Language Sampling on NOVELTYBENCH. For each row, the best and worst language results are highlighted.
5
How Does Language of Thought Shape
Output Diversity?
5.1
Experiment Settings
Datasets and Evaluation Metrics
We evalu-
ate output diversity on two benchmarks, NOVEL-
TYBENCH (Zhang et al., 2025b) and INFINITY-
CHAT (Jiang et al., 2025), each containing 100
open-ended questions without ground-truth an-
swers. Given an input question, we sample the
model M times to obtain a set of outputs O and
evaluate their diversity and quality. Following the
evaluation protocols of the original datasets, we
consider two output diversity metrics and one out-
put quality metric, as described below.
Metric 1: Distinct Score. We compute Distinct
Score to measure the functional distinctiveness of
O following Zhang et al. (2025b). Specifically, the
deberta-v3-large-generation-similarity1
model is used to sequentially judge whether
two outputs are functionally equivalent.
Each
output oi is compared with all previous outputs
{o1, . . . , oi−1}. If oi is judged equivalent to any
oj (j < i), it is assigned to the same equivalence
class; otherwise, it forms a new class. The M
outputs are thus clustered into C equivalence
classes, and the Distinct Score is defined as C/M.
Metric 2: Similarity Score. We also compute
the Similarity Score following Jiang et al. (2025),
which captures semantic similarity among outputs
in O. Sentence-level embeddings are first obtained
for all generated outputs, and cosine similarity is
computed for all output pairs. The final score is
obtained by averaging cosine similarities across all
1https://huggingface.co/yimingzhang/deberta-v3-large-
generation-similarity
pairs. We use Qwen3-Embedding-8B2 for embed-
ding extraction.
Metric 3: Output Quality. To assess whether
improvements in output diversity come at the cost
of output quality, we evaluate the quality of re-
sponses in O using gpt-4o-mini, with scores rang-
ing from 0 to 100. The evaluation considers two
dimensions: instruction adherence and overall re-
sponse quality. Details of the evaluation prompting
are provided in Appendix A.2.
Languages and LLMs
We conduct experiments
on the thinking mode of the Qwen3 family (Yang
et al., 2025) with model sizes 8B, 14B, and
32B, as well as DeepSeek-R1-Distill-Qwen-14B
(DeepSeek-14B) (DeepSeek-AI et al., 2025). We
select 15 thinking languages for evaluation: en,
it, ms, zh, ru, de, iw, bg, da, no, sv, es, tl, oc,
and fr, from the supported languages of the tested
models.
Sampling Parameters
Unless otherwise speci-
fied, the decoding temperature is set to 0.6. For fair
comparison across sampling strategies, the number
of samples M is set equal to the number of thinking
languages, i.e., M = 15.
5.2
Results on Single-Language Sampling
Main Diversity Results
Table 1 summarizes the
output diversity results on NOVELTYBENCH. On
average, switching the thinking language from En-
glish to non-English languages yields an improve-
ment of 5.3 to 7.7 points in Distinct Score and a
reduction of 1.04 to 2.56 points in Similarity Score.
These results suggest that sampling from thinking
2https://huggingface.co/Qwen/Qwen3-Embedding-8B

Figure 2: Correlation between the Distinct Score and
the thinking distance to English across languages. Pear-
son’s r and Spearman’s ρ are reported for each model.
Distinct Scores are obtained under Single-Language
Sampling on NOVELTYBENCH. Thinking distances are
normalized to the range [0, 1].
regions outside the English-dominant space pro-
vides a systematic advantage in output diversity.
We also observe substantial variation in output
diversity across thinking languages. Besides en,
some languages such as ms and zh consistently ex-
hibit lower diversity, whereas others, including iw,
no, and oc, achieve substantially higher diversity
across models and metrics. In some cases, individ-
ual languages lead to particularly large gains. For
example, thinking in iw on Qwen3-8B improves
the Distinct Score by 12.78 points compared to en.
Taken together with the geometric findings from
Section 3.3, these results highlight the strong po-
tential of specific thinking languages— especially
those farther from English in the thinking space—
for enhancing output diversity.
Correlation with Thinking Distance to English
We further examine the relationship between the
geometric properties of the thinking space and out-
put diversity. For each language l, we compute its
thinking distance to English, d(l, en), by averaging
the layer-wise distances dj(l, en) across all model
layers (Section 3.2), where English has distance
zero. To ensure comparability between languages,
we normalize the thinking distances to the range
of [0, 1]. We then analyze the correlation between
these thinking distances and the output diversity
under Single-Language Sampling. Figure 2 reports
the Pearson and Spearman correlations on NOVEL-
TYBENCH, with output diversity measured by the
Distinct Score.
We observe a strong positive correlation across
Model
S-en
S-non-en avg
S-best
Mixed
NOVELTYBENCH
Qwen3-8B
28.55
36.00
41.33
43.73
Qwen3-14B
26.20
31.45
36.87
38.00
Qwen3-32B
35.00
40.30
43.38
46.53
DeepSeek-14B
38.33
46.03
52.42
52.07
INFINITY-EVAL
Qwen3-8B
20.67
22.54
24.51
28.13
Qwen3-14B
20.40
22.60
27.07
26.73
Qwen3-32B
27.00
27.52
28.66
31.47
DeepSeek-14B
25.27
31.84
39.61
35.33
Table 2: Distinct score (%) comparison of Mixed-
Language Sampling and Single-Language Sampling on
NOVELTYBENCH and INFINITY-CHAT. Bold indicates
the best-performing sampling setting for each model
and benchmark.
different models, with Pearson’s r ranging from
0.72 to 0.88 and Spearman’s ρ ranging from 0.58
to 0.89. These results corroborate our earlier ob-
servations, indicating that the distance to English
in the thinking space is informative of the output
diversity achievable under Single-Language Sam-
pling. More specifically, languages that are geo-
metrically farther from English tend to correspond
to more distinct thinking regions, and repeated sam-
pling within such regions is associated with higher
output diversity.
Output Diversity vs. Quality
Table 1 also re-
ports the output quality results.
We observe a
mild trade-off between output diversity and qual-
ity. While English generally achieves higher output
quality, there is no clear pattern in which languages
with the highest output diversity consistently suffer
the lowest output quality. In some cases, specific
languages such as sv and oc achieve strong per-
formance on both dimensions. Overall, thinking
in non-English languages results in only a modest
decrease of 1.02 to 2.24 points in output quality.
Appendix A.3 provides results on INFINITY-
CHAT, which also exhibits similar patterns.
5.3
Results on Mixed-Language Sampling
Comparison with Single-Language Sampling
Table 2 compares Mixed-Language Sampling with
three Single-Language Sampling settings: English
sampling (S-en), the average performance over
non-English sampling (S-non-en avg), and the
best-performing single-language sampling (S-best).
Across both benchmarks, Mixed-Language Sam-
pling consistently improves output diversity over

Figure 3: Relative deviation in Distinct Score under the
removal of k languages in Mixed-Language Sampling.
S-en and S-non-en avg.
Moreover, Mixed-Language Sampling often
matches or even exceeds the performance of the
S-best setting. These results indicate that Mixed-
Language Sampling provides a robust strategy for
improving output diversity without requiring prior
knowledge of which single language performs best.
This advantage arises from the structural differ-
ences among languages in the thinking space (Sec-
tion 3.3): sampling from multiple distinct think-
ing regions and aggregating the resulting outputs
exploits the compositional effects of different lan-
guages.
Results based on the Similarity Score are re-
ported in Appendix A.4 and show the same trend.
Compositional Effects of Different Languages
To further explore the compositional effects of
different languages in Mixed-Language Sampling,
we conduct an ablation study on Qwen3-8B by
progressively removing k languages from Mixed-
Language Sampling (k = 1, . . . , 5). For each value
of k, we enumerate all possible combinations of
language removal and measure the relative devia-
tion of the Distinct Score from the original result,
to quantify the effect of language removal.
Figure 3 shows the relative deviation in Distinct
Score. We first observe that removing a single
language leads to only a small change (2.7% on av-
erage), indicating that Mixed-Language Sampling
does not rely on any individual language to achieve
its diversity gains. However, as k increases, the
diversity degradation grows rapidly and in a super-
linear manner. This suggests that the contributions
of different languages are not merely additive; in-
stead, languages provide complementary diversity
benefits through their joint participation. Together,
these results demonstrate that output diversity un-
der Mixed-Language Sampling emerges from the
0
50
100
150
200
Sampling Number
0
10
20
30
40
Distinct Sample Count
(a) Effect of Sampling Number
en
zh
bg
iw
mixed
0.2
0.6
1.0
1.4
1.8 2.0
Temperature
30
40
50
60
Distinct Score (%)
(b) Effect of Temperature
en
zh
iw
bg
mixed
Figure 4: Effects of sampling parameters on output
diversity. (a) Distinct sample count as a function of the
sampling number M at a fixed temperature (0.6). (b)
Distinct Score (%) under different temperatures with a
fixed sampling number (M = 15).
compositional interaction of multiple languages,
rather than from any single dominant language.
5.4
Other Analysis
Two parameters are important in repeated sampling:
the sampling number M and the temperature. By
default, we set M = 15 and the temperature to
0.6. In this section, we vary these parameters using
Qwen3-8B to examine their effects on two sam-
pling strategies. For Single-Language Sampling,
we select four representative languages for analy-
sis: en and zh (lower-performing), and bg and iw
(higher-performing).
5.4.1
Scaling Sampling Number
We first vary the sampling number M from 1 to
200 while keeping the temperature fixed at 0.6. For
Mixed-Language Sampling, we utilize the full lan-
guage pool supported by Qwen3 (approximately
100 languages) and randomly select one language
as the thinking language for each sampling. Rather
than Distinct Score C/M, Figure 4(a) directly re-
ports the number of distinct samples C.
Across all settings, we observe that the growth
of C slows down as M increases, suggesting the
existence of an upper bound on achievable output
diversity. However, Mixed-Language Sampling ex-
hibits a much slower saturation rate compared to
Single-Language Sampling. As M increases, its
advantage over all Single-Language Sampling set-
tings continues to widen.
This behavior indicates that Mixed-Language
Sampling effectively expands the model’s diver-
sity ceiling. Such an expansion arises from the
increased coverage of distinct thinking regions en-
abled by linguistic heterogeneity. Although we
explore over 100 languages, further unlocking the
benefits of linguistic diversity remains an interest-

Model
Method
Blend
WVS
Qwen3-8B
ES
67.9
40.0
HT
68.0 (+0.1)
39.0 (-1.0)
RD
73.3 (+5.4)
52.7 (+12.7)
MP
76.1 (+9.2)
52.0 (+12.0)
MLS
76.7 (+8.8)
59.0 (+19.0)
Qwen3-14B
ES
66.7
31.6
HT
67.1 (+0.4)
32.7 (+1.1)
RD
68.4 (+1.7)
38.0 (+6.4)
MP
72.7 (+6.0)
45.1 (+13.5)
MLS
74.0 (+7.3)
48.4 (+16.8)
Qwen3-32B
ES
67.5
40.1
HT
69.2 (+1.7)
43.6 (+3.5)
RD
72.8 (+5.3)
53.4 (+13.3)
MP
73.4 (+5.9)
46.1 (+6.0)
MLS
74.6 (+7.1)
50.4 (+10.3)
DeepSeek-8B
ES
78.6
52.3
HT
80.7 (+2.1)
60.1 (+7.8)
RD
78.6 (+0.0)
54.7 (+2.4)
MP
80.6 (+2.0)
67.2 (+14.9)
MLS
83.0 (+4.4)
73.3 (+21.0)
Table 3: Cultural pluralism performance (entropy nor-
malized to 0–100). Methods: ES (English Sampling),
HT (High Temperature), RD (Request Diversity), MP
(Multilingual Prompting), MLS (Mixed-Language Sam-
pling). Parentheses show absolute gains/losses relative
to ES within each model and benchmark. Bold indicates
the best-performing setting per model and benchmark.
ing direction for future work.
5.4.2
Varying Temperatures
We next fix the sampling number M at 15 and vary
the temperature over {0.2, 0.6, 1.0, 1.4, 1.8, 2.0}.
The results are shown in Figure 4(b).
We observe a compositional effect between our
language of thought and temperature scaling: while
switching the language of thought from English
to other languages already improves output diver-
sity, increasing the temperature further yields ad-
ditional gains. Moreover, we observe clear advan-
tages of Single-Language Sampling with specific
non-English languages and Mixed-Language Sam-
pling. For instance, Mixed-Language Sampling at
temperature 1.0 achieves diversity comparable to
English sampling at temperature 2.0.
6
Application: Pluralistic Alignment
In this section, we explore the practical utility of
Mixed-Language Sampling, given its advantages.
Specifically, we focus on pluralistic alignment sce-
narios, where LLM outputs are expected to reflect
cultural pluralism (Cao et al., 2023; Sorensen et al.,
2024; Xu et al., 2025; Ying et al., 2025).
6.1
Settings
Data
We consider two types of cultural plural-
ism: cultural knowledge and cultural values, eval-
uated using the BLEND (Myung et al., 2024) and
WVS (Haerpfer et al., 2022) datasets, respectively.
Both datasets consist of multiple-choice questions.
Evaluation
Following Wang et al. (2025a), for
each cultural question, we perform repeated sam-
pling to obtain M responses and measure cultural
pluralism based on the resulting output distribution.
For BLEND, where each option is associated with
one or more countries, we map the sampled outputs
to countries and compute the entropy over the coun-
try distribution. For WVS, we directly compute the
entropy over the output distribution, which charac-
terizes the diversity of value orientations reflected
in the model responses.
LLMs
Experiments are conducted on Qwen3-
8B, Qwen3-14B, Qwen3-32B, and DeepSeek-R1-
Distill-Llama-8B (DeepSeek-8B), with tempera-
ture set to 0.6 by default.
Sampling Strategies
We compare the following
sampling strategies: (1) English Sampling, where
the language of thought is English; (2) High Tem-
perature, where the temperature is increased to 1.0
while keeping English as the thinking language; (3)
Request Diversity, where the model is explicitly
instructed to generate novel responses; (4) Mul-
tilingual Prompting (Wang et al., 2025a), where
each cultural question is translated into the same
15 languages used in previous experiments; and (5)
Mixed-Language Sampling, where the language of
thought varies across the same 15 languages used
in previous experiments.
The sampling number M is set to 15 for all
strategies. For Multilingual Prompting and Mixed-
Language Sampling, each language is sampled
once.
Additional details on the datasets, evaluation pro-
tocols, and baselines are provided in Appendix A.5.
6.2
Results
The results in Table 3 clearly demonstrate the
practical advantage of Mixed-Language Sampling
for pluralistic alignment.
Across benchmarks
and models, Mixed-Language Sampling consis-
tently achieves the highest cultural pluralism per-
formance, enabling LLMs to reflect more diverse
cultural knowledge and value orientations.

In contrast, simply increasing the temperature,
explicitly requesting diversity, or using multilin-
gual inputs does not yield improvements compa-
rable to Mixed-Language Sampling. These results
highlight the practical value of diversifying the
language of thought as a means of more fully ex-
ploiting the model’s thinking space for pluralistic
alignment.
7
Conclusion
In this paper, we establish that controlling the lan-
guage of thought provides a structural source of
output diversity in LLMs. We find that switching
the thinking language from English to non-English
languages consistently increases output diversity,
with stronger gains observed for languages farther
from English in the thinking space. We further
demonstrate that aggregating samples across multi-
ple thinking languages yields additional diversity
improvements through their compositional effects,
and that scaling the sampling number with linguis-
tic heterogeneity effectively expands the model’s di-
versity ceiling. Finally, we show that these findings
translate into broader coverage of cultural knowl-
edge and values of LLMs in pluralistic alignment.
8
Limitations
This work has two main limitations.
First, while we observe a positive correlation be-
tween the geometric distance of non-English think-
ing languages from English and the output diversity
achieved under repeated sampling, there are still
several open questions that are not addressed in
this work. For example, many cross-lingual align-
ment methods explicitly aim to align non-English
representations toward English. An important ques-
tion is whether such alignment procedures may
inadvertently reduce the output diversity associ-
ated with aligned non-English languages, and if so,
what mechanisms or strategies could mitigate this
effect. Addressing these questions would require
controlled interventions on the model, which we
leave for future work.
Second, although we demonstrate the practical
utility of our findings in pluralistic alignment set-
tings, our evaluation relies on output entropy as
a proxy for cultural pluralism. This experimental
setup remains an abstraction of real-world deploy-
ment scenarios. In practice, pluralistic alignment
often requires models to align with multiple spe-
cific and context-dependent cultural values under
explicit constraints. The sampling strategies stud-
ied in this work would likely need to be further
adapted—e.g., by incorporating culturally contex-
tualized language-of-thought routing—to be effec-
tive in such settings, which we leave for future
investigation.
References
Sanchit Ahuja, Praneetha Vaddamanu, and Barun Pa-
tra. 2025. Efficientxlang: Towards improving token
efficiency through cross-lingual reasoning. In Find-
ings of the Association for Computational Linguistics:
EMNLP 2025, Suzhou, China, November 4-9, 2025,
pages 15612–15624. Association for Computational
Linguistics.
Badr AlKhamissi, Muhammad N. ElNokrashy, Mai
Alkhamissi, and Mona T. Diab. 2024. Investigat-
ing cultural alignment of large language models. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), ACL 2024, Bangkok, Thailand, August
11-16, 2024, pages 12404–12422. Association for
Computational Linguistics.
Prasoon Bajpai and Tanmoy Chakraborty. 2025. Multi-
lingual test-time scaling via initial thought transfer.
CoRR, abs/2505.15508.
Damián E. Blasi, Joseph Henrich, Evangelia Adamou,
David Kemmerer, and Asifa Majid. 2022.
Over-
reliance on english hinders cognitive science. Trends
in Cognitive Sciences, 26(12):1153–1170.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello,
Min Chen, and Daniel Hershcovich. 2023.
As-
sessing cross-cultural alignment between chatgpt
and human societies: An empirical study. CoRR,
abs/2303.17466.
Kang Chen, Mengdi Zhang, and Yixin Cao. 2025a.
Less data less tokens: Multilingual unification learn-
ing for efficient test-time reasoning in llms. CoRR,
abs/2506.18341.
Xiaoyang Chen, Xinan Dai, Yu Du, Qian Feng, Naixu
Guo, Tingshuo Gu, Yuting Gao, Yingyi Gao, Xudong
Han, Xiang Jiang, Yilin Jin, Hongyi Lin, Shisheng
Lin, Xiangnan Li, Yuante Li, Yixing Li, Zhentao
Lai, Zilu Ma, Yingrong Peng, and 12 others. 2025b.
Deepmath-creative: A benchmark for evaluating
mathematical creativity of large language models.
CoRR, abs/2505.08744.
Yuxin Chen, Yiran Zhao, Yang Zhang, An Zhang,
Kenji Kawaguchi, Shafiq Joty, Junnan Li, Tat-Seng
Chua, Michael Qizhe Shieh, and Wenxuan Zhang.
2025c. The emergence of abstract thought in large
language models beyond any language.
CoRR,
abs/2506.09890.

Vincent Conitzer, Rachel Freedman, Jobst Heitzig,
Wesley H. Holliday, Bob M. Jacobs, Nathan Lam-
bert, Milan Mossé, Eric Pacuit, Stuart Russell, Hai-
ley Schoelkopf, Emanuel Tewolde, and William S.
Zwicker. 2024. Position: Social choice should guide
AI alignment in dealing with diverse human feedback.
In Forty-first International Conference on Machine
Learning, ICML 2024, Vienna, Austria, July 21-27,
2024.
DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang,
Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu,
Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang,
Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhi-
hong Shao, Zhuoshu Li, Ziyi Gao, and 81 others.
2025. Deepseek-r1: Incentivizing reasoning capa-
bility in llms via reinforcement learning.
CoRR,
abs/2501.12948.
Changjiang Gao, Xu Huang, Wenhao Zhu, Shujian
Huang, Lei Li, and Fei Yuan. 2025. Could think-
ing multilingually empower LLM reasoning? CoRR,
abs/2504.11833.
Changjiang Gao, Zixian Huang, Kaichen Yang, Jiajun
Chen, Jixing Li, and Shujian Huang. 2026. Explang:
Improved exploration and exploitation in LLM rea-
soning with on-policy thinking language selection.
CoRR, abs/2602.21887.
Salvatore Giorgi, Tingting Liu, Ankit Aich, Kelsey Is-
man, Garrick Sherman, Zachary Fried, João Sedoc,
Lyle H. Ungar, and Brenda Curtis. 2024. Modeling
human subjectivity in llms using explicit and implicit
human factors in personas. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2024,
Miami, Florida, USA, November 12-16, 2024, pages
7174–7188. Association for Computational Linguis-
tics.
Sikun Guo, Amir Hassan Shariatmadari, Guangzhi
Xiong, Albert Huang, Myles Kim, Corey M.
Williams, Stefan Bekiranov, and Aidong Zhang.
2025a. Ideabench: Benchmarking large language
models for research idea generation. In Proceedings
of the 31st ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, V.2, KDD 2025, Toronto
ON, Canada, August 3-7, 2025, pages 5888–5899.
ACM.
Yanzhu Guo, Guokan Shang, and Chloé Clavel. 2025b.
Benchmarking linguistic diversity of large language
models. Trans. Assoc. Comput. Linguistics, 13:1507–
1526.
Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and
Chloé Clavel. 2024. The curious decline of linguistic
diversity: Training language models on synthetic text.
In Findings of the Association for Computational Lin-
guistics: NAACL 2024, Mexico City, Mexico, June
16-21, 2024, pages 3589–3604. Association for Com-
putational Linguistics.
Christian Haerpfer,
Ronald Inglehart,
Alejandro
Moreno, Christian Welzel, Kseniya Kizilova, Jaime
Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bjorn Puranen. 2022. World values
survey: Round seven-country-pooled datafile version
5.0. Madrid, Spain & Vienna, Austria: JD Systems
Institute & WVSA Secretariat, 12(10):8.
Simeng Han, Stephen Xia, Grant Zhang, Howard
Dai, Chen Liu, Lichang Chen, Hoang Huy Nguyen,
Hongyuan Mei, Jiayuan Mao, and R. Thomas McCoy.
2025. Creativity or brute force? using brainteasers as
a window into the problem-solving abilities of large
language models. CoRR, abs/2505.10844.
Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu,
Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten
Sap, Alon Albalak, and Yejin Choi. 2025. Artificial
hivemind: The open-ended homogeneity of language
models (and beyond). CoRR, abs/2510.22954.
Ammar Khairi, Daniel D’souza, Ye Shen, Julia Kreutzer,
and Sara Hooker. 2025. When life gives you sam-
ples: The benefits of scaling up inference compute for
multilingual llms. In Proceedings of the 2025 Con-
ference on Empirical Methods in Natural Language
Processing, EMNLP 2025, Suzhou, China, Novem-
ber 4-9, 2025, pages 27559–27583. Association for
Computational Linguistics.
Anatoliy V. Kharkhurin, Valeriya Koncha, and Morteza
Charkhabi. 2023. The effects of multilingual and
multicultural practices on divergent thinking. impli-
cations for plurilingual creativity paradigm. Bilin-
gualism: Language and cognition, 26(3):592–609.
Arash Lagzian, Srinivas Anumasa, and Dianbo Liu.
2025. Multi-novelty: Improve the diversity and nov-
elty of contents generated by large language models
via inference-time multi-views brainstorming. CoRR,
abs/2502.12700.
Yihao Li, Jiayi Xin, Miranda Muqing Miao, Qi Long,
and Lyle H. Ungar. 2025a. The impact of language
mixing on bilingual LLM reasoning. In Proceedings
of the 2025 Conference on Empirical Methods in
Natural Language Processing, EMNLP 2025, Suzhou,
China, November 4-9, 2025, pages 32531–32548.
Association for Computational Linguistics.
Ziniu Li, Congliang Chen, Tian Xu, Zeyu Qin, Jiancong
Xiao, Zhi-Quan Luo, and Ruoyu Sun. 2025b. Pre-
serving diversity in supervised fine-tuning of large
language models. In The Thirteenth International
Conference on Learning Representations, ICLR 2025,
Singapore, April 24-28, 2025. OpenReview.net.
Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang,
Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, and
Zhaopeng Tu. 2024a. Encouraging divergent think-
ing in large language models through multi-agent
debate. In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
EMNLP 2024, Miami, FL, USA, November 12-16,
2024, pages 17889–17904. Association for Computa-
tional Linguistics.

Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley
Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao,
Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christo-
pher Potts, Christopher D. Manning, and James Y.
Zou. 2024b. Mapping the increasing use of llms in
scientific papers. CoRR, abs/2404.01268.
Jiaming Luo, Colin Cherry, and George F. Foster. 2024.
To diverge or not to diverge: A morphosyntactic per-
spective on machine translation vs human translation.
Trans. Assoc. Comput. Linguistics, 12:355–371.
Niklas Muennighoff, Zitong Yang, Weijia Shi, Xi-
ang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke
Zettlemoyer, Percy Liang, Emmanuel J. Candès, and
Tatsunori Hashimoto. 2025. s1: Simple test-time
scaling. In Proceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing,
EMNLP 2025, Suzhou, China, November 4-9, 2025,
pages 20275–20321. Association for Computational
Linguistics.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin,
Rifki Afina Putri, Dimosthenis Antypas, Hsuvas
Borkakoty, Eunsu Kim, Carla Pérez-Almendros,
Abinew Ali Ayele, Víctor Gutiérrez-Basulto, Yazmín
Ibáñez-García, Hwaran Lee, Shamsuddeen Hassan
Muhammad, Ki-Woong Park, Anar Rzayev, Nina
White, Seid Muhie Yimam, Mohammad Taher Pile-
hvar, and 3 others. 2024. Blend: A benchmark for
llms on everyday knowledge in diverse cultures and
languages. In Advances in Neural Information Pro-
cessing Systems 38: Annual Conference on Neural
Information Processing Systems 2024, NeurIPS 2024,
Vancouver, BC, Canada, December 10 - 15, 2024.
Vishakh Padmakumar and He He. 2024. Does writing
with language models reduce content diversity? In
The Twelfth International Conference on Learning
Representations, ICLR 2024, Vienna, Austria, May
7-11, 2024. OpenReview.net.
Max Peeperkorn, Tom Kouwenhoven, Dan Brown, and
Anna Jordanous. 2024. Is temperature the creativity
parameter of large language models? In Proceedings
of the 15th International Conference on Computa-
tional Creativity, ICCC 2024, Jönköping, Sweden,
June 17-21, 2024, pages 226–235. Association for
Computational Creativity (ACC).
Max Peeperkorn, Tom Kouwenhoven, Dan Brown,
and Anna Jordanous. 2025.
Mind the gap: Con-
formative decoding to improve output diversity of
instruction-tuned large language models.
CoRR,
abs/2507.20956.
Antoine Bellemare Pépin, François Lespinasse, Philipp
Thölke, Yann Harel, Kory W. Mathewson, Jay A. Ol-
son, Yoshua Bengio, and Karim Jerbi. 2024. Diver-
gent creativity in humans and large language models.
CoRR, abs/2405.13012.
Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
How multilingual is multilingual bert?
In Pro-
ceedings of the 57th Conference of the Association
for Computational Linguistics, ACL 2019, Florence,
Italy, July 28- August 2, 2019, Volume 1: Long Pa-
pers, pages 4996–5001. Association for Computa-
tional Linguistics.
Jirui Qi, Shan Chen, Zidi Xiong, Raquel Fernández,
Danielle S. Bitterman, and Arianna Bisazza. 2025.
When models reason in your language: Controlling
thinking language comes at the cost of accuracy. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2025, Suzhou, China, November
4-9, 2025, pages 20279–20296. Association for Com-
putational Linguistics.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert:
Sentence embeddings using siamese bert-networks.
In Proceedings of the 2019 Conference on Empiri-
cal Methods in Natural Language Processing and
the 9th International Joint Conference on Natural
Language Processing, EMNLP-IJCNLP 2019, Hong
Kong, China, November 3-7, 2019, pages 3980–3990.
Association for Computational Linguistics.
Kai Ruan, Xuan Wang, Jixiang Hong, Peng Wang, Yang
Liu, and Hao Sun. 2024. Liveideabench: Evaluating
llms’ divergent thinking for scientific idea generation
with minimal context. CoRR, abs/2412.17596.
Michal Shur-Ofry, Bar Horowitz-Amsalem, Adir Ra-
hamim, and Yonatan Belinkov. 2024. Growing a tail:
Increasing output diversity in large language models.
CoRR, abs/2411.02989.
Guijin Son, Jiwoo Hong, Hyunwoo Ko, and James
Thorne. 2025. Linguistic generalizability of test-time
scaling in mathematical reasoning. In Proceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
ACL 2025, Vienna, Austria, July 27 - August 1, 2025,
pages 14333–14368. Association for Computational
Linguistics.
Taylor
Sorensen,
Jared
Moore,
Jillian
Fisher,
Mitchell
L.
Gordon,
Niloofar
Mireshghallah,
Christopher Michael Rytting, Andre Ye, Liwei Jiang,
Ximing Lu, Nouha Dziri, Tim Althoff, and Yejin
Choi. 2024.
Position: A roadmap to pluralistic
alignment. In Forty-first International Conference
on Machine Learning, ICML 2024, Vienna, Austria,
July 21-27, 2024. OpenReview.net.
Haoran Sun, Yekun Chai, Shuohuan Wang, Yu Sun,
Hua Wu, and Haifeng Wang. 2025. Curiosity-driven
reinforcement learning from human feedback. In
Proceedings of the 63rd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), ACL 2025, Vienna, Austria, July 27 -
August 1, 2025, pages 23517–23534. Association for
Computational Linguistics.
Zhi Rui Tam, Cheng-Kuang Wu, Yu Ying Chiu,
Chieh-Yen Lin, Yun-Nung Chen, and Hung-yi Lee.
2025. Language matters: How do multilingual input
and reasoning paths affect large reasoning models?
CoRR, abs/2505.17407.

Selim F. Tekin, Fatih Ilhan, Tiansheng Huang, Sihao Hu,
and Ling Liu. 2024. LLM-TOPLA: efficient LLM
ensemble by maximising diversity. In Findings of the
Association for Computational Linguistics: EMNLP
2024, Miami, Florida, USA, November 12-16, 2024,
pages 11951–11966. Association for Computational
Linguistics.
Guy Tevet and Jonathan Berant. 2021. Evaluating the
evaluation of diversity in natural language genera-
tion. In Proceedings of the 16th Conference of the
European Chapter of the Association for Computa-
tional Linguistics: Main Volume, EACL 2021, Online,
April 19 - 23, 2021, pages 326–346. Association for
Computational Linguistics.
Yufei Tian, Abhilasha Ravichander, Lianhui Qin, Ro-
nan Le Bras, Raja Marjieh, Nanyun Peng, Yejin Choi,
Thomas L. Griffiths, and Faeze Brahman. 2024. Mac-
gyver: Are large language models creative problem
solvers?
In Proceedings of the 2024 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), NAACL 2024,
Mexico City, Mexico, June 16-21, 2024, pages 5303–
5324. Association for Computational Linguistics.
Qihan Wang, Shidong Pan, Tal Linzen, and Emily Black.
2025a. Multilingual prompting for improving LLM
generation diversity. In Proceedings of the 2025 Con-
ference on Empirical Methods in Natural Language
Processing, EMNLP 2025, Suzhou, China, November
4-9, 2025, pages 6367–6389. Association for Com-
putational Linguistics.
Wenxuan Wang, Wenxiang Jiao, Jingyuan Huang, Ruyi
Dai, Jen-tse Huang, Zhaopeng Tu, and Michael R.
Lyu. 2024. Not all countries celebrate thanksgiving:
On the cultural dominance in large language models.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), ACL 2024, Bangkok, Thailand, Au-
gust 11-16, 2024, pages 6349–6384. Association for
Computational Linguistics.
Yiming Wang, Pei Zhang, Jialong Tang, Haoran Wei,
Baosong Yang, Rui Wang, Chenshu Sun, Feitong
Sun, Jiran Zhang, Junxuan Wu, Qiqian Cang,
Yichang Zhang, Fei Huang, Junyang Lin, Fei Huang,
and Jingren Zhou. 2025b.
Polymath:
Evaluat-
ing mathematical reasoning in multilingual contexts.
CoRR, abs/2504.18428.
Benjamin Lee Whorf. 2012. Language, Thought, and
Reality: Selected Writings of Benjamin Lee Whorf.
MIT Press.
Shaoyang Xu, Yongqi Leng, Linhao Yu, and Deyi Xiong.
2025. Self-pluralising culture alignment for large
language models. In Proceedings of the 2025 Con-
ference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human
Language Technologies, NAACL 2025 - Volume 1:
Long Papers, Albuquerque, New Mexico, USA, April
29 - May 4, 2025, pages 6859–6877. Association for
Computational Linguistics.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025.
Qwen3 technical report.
CoRR,
abs/2505.09388.
Junyi Ye, Jingyi Gu, Xinyun Zhao, Wenpeng Yin, and
Grace Guiling Wang. 2025. Assessing the creativity
of llms in proposing novel solutions to mathematical
problems. In AAAI-25, Sponsored by the Associa-
tion for the Advancement of Artificial Intelligence,
February 25 - March 4, 2025, Philadelphia, PA, USA,
pages 25687–25696. AAAI Press.
Jiahao Ying, Wei Tang, Yiran Zhao, Yixin Cao,
Yu Rong, and Wenxuan Zhang. 2025. Disentangling
language and culture for evaluating multilingual large
language models. In Proceedings of the 63rd An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), ACL 2025, Vi-
enna, Austria, July 27 - August 1, 2025, pages 22230–
22251. Association for Computational Linguistics.
Zheng-Xin Yong, Muhammad Farid Adilazuarda,
Jonibek Mansurov, Ruochen Zhang, Niklas Muen-
nighoff, Carsten Eickhoff, Genta Indra Winata, Julia
Kreutzer, Stephen H. Bach, and Alham Fikri Aji.
2025. Crosslingual reasoning through test-time scal-
ing. CoRR, abs/2505.05408.
Zhiyuan Zeng, Qinyuan Cheng, Zhangyue Yin, Yun-
hua Zhou, and Xipeng Qiu. 2025. Revisiting the
test-time scaling of o1-like models: Do they truly
possess test-time scaling capabilities? In Proceed-
ings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), ACL 2025, Vienna, Austria, July 27 - August
1, 2025, pages 4651–4665. Association for Computa-
tional Linguistics.
Wenxuan Zhang. 2026. Towards inclusive AI: advanc-
ing multilingual large language models. In Fortieth
AAAI Conference on Artificial Intelligence, Thirty-
Eighth Conference on Innovative Applications of Ar-
tificial Intelligence, Sixteenth Symposium on Educa-
tional Advances in Artificial Intelligence, AAAI 2026,
Singapore, January 20-27, 2026, page 39848. AAAI
Press.
Wenxuan Zhang, Hou Pong Chan, Yiran Zhao, Mahani
Aljunied, Jianyu Wang, Chaoqun Liu, Yue Deng,
Zhiqiang Hu, Weiwen Xu, Yew Ken Chia, Xin Li,
and Lidong Bing. 2025a. Seallms 3: Open foun-
dation and chat multilingual large language models
for southeast asian languages. In Proceedings of
the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, NAACL
2025 - System Demonstrations, Albuquerque, New
Mexico, USA, April 29 - May 4, 2025, pages 96–105.
Association for Computational Linguistics.
Yiming Zhang, Harshita Diddee, Susan Holm, Hanchen
Liu, Xinyue Liu, Vinay Samuel, Barry Wang, and

Language
Prefix inserted after <think> token
English (en)
Okay, the user is asking
Italian (it)
Va bene, l’utente sta chiedendo
Malay (ms)
Baiklah, pengguna sedang bertanya
Chinese (zh)
好的，用户在问
Russian (ru)
Хорошо, пользователь спрашивает
German (de)
Okay, der Benutzer fragt
Hebrew (iw)בסדר, המשתמש שואל
Bulgarian (bg)
Добре, потребителят пита
Danish (da)
Okay, brugeren spørger
Norwegian (no)
Greit, brukeren spør
Swedish (sv)
Okej, användaren frågar
Spanish (es)
De acuerdo, el usuario pregunta
Tagalog (tl)
Sige, nagtatanong ang gumagamit
Occitan (oc)
Bon, l’utilizaire demanda
French (fr)
D’accord, l’utilisateur demande
Figure 5: Prefix translations used for Thinking Lan-
guage Control.
Daphne Ippolito. 2025b. Noveltybench: Evaluating
language models for humanlike diversity. CoRR,
abs/2504.05228.
Weixiang Zhao, Jiahe Guo, Yang Deng, Tongtong Wu,
Wenxuan Zhang, Yulin Hu, Xingyu Sui, Yanyan
Zhao, Wanxiang Che, Bing Qin, Tat-Seng Chua,
and Ting Liu. 2025a. When less language is more:
Language-reasoning disentanglement makes llms bet-
ter multilingual reasoners. CoRR, abs/2505.15257.
Yiran Zhao, Chaoqun Liu, Yue Deng, Jiahao Ying,
Mahani Aljunied, Zhaodonghui Li, Lidong Bing,
Hou Pong Chan, Yu Rong, Deli Zhao, and Wenx-
uan Zhang. 2025b. Babel: Open multilingual large
language models serving over 90% of global speak-
ers. CoRR, abs/2503.00865.
Yiran Zhao, Wenxuan Zhang, Guizhen Chen, Kenji
Kawaguchi, and Lidong Bing. 2024. How do large
language models handle multilingualism?
In Ad-
vances in Neural Information Processing Systems
38: Annual Conference on Neural Information Pro-
cessing Systems 2024, NeurIPS 2024, Vancouver, BC,
Canada, December 10 - 15, 2024.
Yaoming Zhu, Sidi Lu, Lei Zheng, Jiaxian Guo, Weinan
Zhang, Jun Wang, and Yong Yu. 2018. Texygen: A
benchmarking platform for text generation models.
In The 41st International ACM SIGIR Conference on
Research & Development in Information Retrieval,
SIGIR 2018, Ann Arbor, MI, USA, July 08-12, 2018,
pages 1097–1100. ACM.
Model
Lang
Think-Target (%)
Output-EN (%)
Qwen3-8B
en
100.00
98.29
non-en
99.88 ± 0.25
98.28 ± 1.31
Qwen3-14B
en
100.00
98.37
non-en
99.57 ± 1.45
99.50 ± 0.35
Qwen3-32B
en
100.00
100.00
non-en
99.54 ± 1.47
98.61 ± 0.69
DeepSeek-14B
en
100.00
96.10
non-en
98.70 ± 2.57
95.32 ± 1.51
Table 4: Sanity-check verification of thinking and output
language control. Results for English thinking are re-
ported individually, while results for non-English think-
ing are averaged over multiple languages and reported
as mean ± standard deviation.
A
Appendix
A.1
Language Control Details
Figure 5 presents the translated prefixes used for
Thinking Language Control across 15 languages.
By inserting the corresponding prefix immediately
after the <think> token, the model is guided to
conduct its intermediate thinking in the target lan-
guage.
Combined with Output Language Control, the
model is guided to thinking in a specified language
while producing English responses. As a sanity
check, we apply an off-the-shelf language iden-
tification tool3 to the thinking content within the
<think> . . . </think> span, as well as to the final
output following </think>.
Table 4 summarizes the averaged results on NOV-
ELTYBENCH and INFINITY-CHAT. Across models,
the thinking segments are predominantly detected
as the target thinking language, and the output seg-
ments are predominantly detected as English. Al-
though language identification may introduce some
noise, these results indicate that the intended lan-
guage control signals are largely reflected in the
generated text.
A.2
Output Quality Evaluation Details
Table 5 shows the complete prompt used for output
quality evaluation. The total quality score is com-
puted as the sum of the two evaluation dimensions.
For each task instance, all sampled responses are
evaluated independently, and we report the average
quality score across samples.
3https://github.com/pemistahl/lingua-py

Output Quality Evaluation Prompt
You are an evaluator assessing the quality of a single re-
sponse to a task instruction.
You will be given:
(1) A task instruction
(2) A response
Evaluate the response along the following two dimensions:
1. Instruction Adherence (0–50)
To what extent does the response follow the task instruc-
tion?
Note that if the response explicitly refuses to perform the
task, this should NOT be penalized.
You only need to judge the degree to which the response is
relevant to the task instruction.
2. Response Quality (0–50)
Assess the overall quality of the response in terms of clarity,
fluency, and grammatical correctness.
Scoring:
- Each dimension should be scored from 0 to 50 (integer
only).
- Total Score = sum of the two dimensions (0–100).
Output format (strict JSON only):
{
"Instruction Adherence": <score>,
"Response Quality": <score>,
"Total Score": <score>
}
Table 5: Prompt template used for output quality evalu-
ation with gpt-4o-mini.
A.3
Additional Results on Single-Language
Sampling
Table 6 reports the results of Single-Language Sam-
pling on INFINITY-CHAT. Overall, we observe
several consistent trends that align with the main
findings. First, switching the language of thought
from English to non-English languages generally
leads to higher output diversity across models, as
reflected by higher Distinct Score and lower Sim-
ilarity Score. Second, there exists notable vari-
ation across thinking languages: languages such
as en, ru, and fr tend to exhibit lower diversity,
whereas others, including iw, tl, and oc, consis-
tently achieve higher diversity. Finally, we do not
observe a clear or systematic trade-off between out-
put diversity and quality across languages. Several
non-English languages achieve improved diversity
while maintaining comparable output quality.
Figure 6 further reports the correlation between
output diversity and the thinking distance to En-
glish across languages on INFINITY-CHAT. Con-
sistent with our main results, we observe a strong
positive correlation for most models. This result
further corroborates that repeated sampling within
thinking regions farther from English is associated
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Thinking Distance to English
0.200
0.225
0.250
0.275
0.300
0.325
0.350
0.375
0.400
Distinct Score
r = 0.79
 = 0.81
r = 0.60
 = 0.66
r = 0.33
 = 0.44
r = 0.85
 = 0.84
Qwen3-8B
Qwen3-14B
Qwen3-32B
Deepseek-14B
Figure 6: Correlation between the Distinct Score and
the thinking distance to English across languages. Pear-
son’s r and Spearman’s ρ are reported for each model.
Distinct Scores are obtained under Single-Language
Sampling on INFINITY-CHAT. Thinking distances are
normalized to the range [0, 1] for visualization.
with higher output diversity.
A.4
Additional Results on Mixed-Language
Sampling
Table 7 compares Mixed-Language Sampling with
three Single-Language Sampling settings using the
Similarity Score.
Consistent with the main re-
sults, Mixed-Language Sampling consistently out-
performs S-en and S-non-en avg, and in several
cases matches or exceeds the S-best setting. This
shows that its advantage lies in improving diversity
without requiring the selection of a single best-
performing language.
A.5
Culture Evaluation Details
Datasets
For BLEND, we extract the set of
unique questions from the original large-scale
dataset and merge all answer options into each
question, resulting in a multiple-choice dataset with
402 questions. For WVS, the original dataset con-
tains 290 questions. We remove 8 questions with-
out predefined options, yielding a final set of 282
multiple-choice questions.
Evaluation Protocols
In BLEND, each answer
option is associated with one or more countries.
For each sampled response, we extract the selected
option and increment the count of its associated
country (or countries). Let p(c) denote the em-
pirical distribution over countries aggregated from
M samples. Cultural pluralism is measured as the

en
it
ms
zh
ru
de
iw
bg
da
no
sv
es
tl
oc
fr
avg (non-en)
Distinct Score ↑
Qwen3-8B
20.67
21.89
22.15
20.13
20.47
22.87
23.98
23.64
23.10
24.51
22.65
20.73
23.71
24.47
21.27
22.54
Qwen3-14B
20.40
22.40
20.88
21.93
21.53
22.40
27.07
21.47
23.67
24.47
22.80
21.00
23.85
23.23
19.73
22.60
Qwen3-32B
27.00
27.60
27.67
27.20
25.73
26.27
27.05
26.07
28.60
27.78
28.47
28.47
28.66
28.66
27.00
27.52
DeepSeek-14B
25.27
30.53
29.00
28.80
29.33
30.33
35.76
30.88
34.40
34.00
35.20
27.93
39.61
31.99
28.00
31.84
Similarity Score ↓
Qwen3-8B
89.05
88.69
88.80
88.80
89.30
87.83
87.36
88.09
88.12
87.47
88.30
88.75
88.26
86.78
88.64
88.23
Qwen3-14B
89.53
88.89
89.13
88.50
89.36
89.12
87.77
88.83
88.53
88.18
88.60
89.36
88.81
88.37
89.58
88.79
Qwen3-32B
85.24
81.97
84.98
82.89
84.27
76.49
86.22
85.52
82.54
84.10
79.24
80.83
85.72
83.77
82.31
82.92
DeepSeek-14B
85.97
83.16
85.52
85.74
84.09
83.06
79.11
83.31
80.85
80.15
82.64
85.46
79.30
83.11
85.19
82.91
Output Quality ↑
Qwen3-8B
96.82
95.86
95.72
95.53
96.11
96.69
95.53
96.04
95.09
95.00
96.82
95.72
95.70
95.59
95.40
95.77
Qwen3-14B
96.93
94.94
95.48
95.03
94.70
96.03
96.50
96.00
96.10
96.78
96.16
95.79
95.49
95.87
95.75
95.76
Qwen3-32B
97.36
96.08
95.85
96.22
95.36
94.47
95.57
97.07
95.52
96.87
95.96
94.97
96.04
96.19
94.26
95.74
DeepSeek-14B
88.46
89.45
88.99
89.44
90.71
86.79
86.51
80.12
87.24
82.13
85.06
87.52
87.13
83.99
90.07
86.80
Table 6: Distinct Score (%), Similarity Score (%), and Output Quality across models and thinking languages under
Single-Language Sampling on INFINITY-CHAT. For each row, the best and worst language results are highlighted.
Model
S-en
S-non-en avg
S-best
Mixed
NOVELTYBENCH
Qwen3-8B
87.28
84.72
80.79
82.84
Qwen3-14B
87.82
86.78
85.04
85.29
Qwen3-32B
82.10
79.99
77.65
79.44
DeepSeek-14B
81.15
79.86
76.16
77.64
INFINITY-CHAT
Qwen3-8B
89.05
88.23
86.78
86.47
Qwen3-14B
89.53
88.79
87.77
87.87
Qwen3-32B
85.24
82.92
76.49
80.29
DeepSeek-14B
85.97
82.91
79.11
82.15
Table 7: Similarity score (%) comparison of Mixed-
Language Sampling and Single-Language Sampling on
NOVELTYBENCH and INFINITY-CHAT. Bold indicates
the best-performing sampling setting for each model
and benchmark.
normalized entropy:
HBlend = −P
c p(c) log p(c)
log |C|
where C denotes the set of all countries appearing
in the answer options for the question. The reported
results are averaged over all questions.
In WVS, each sampled response corresponds
to a discrete value option. Let p(o) denote the
empirical distribution over predicted options across
M samples. Cultural pluralism is defined as the
normalized entropy:
HWVS = −P
o p(o) log p(o)
log |O|
where O denotes the set of possible value options
for the question. The reported results are averaged
over all questions.
Baselines
The Request Diversity baseline ap-
pends the following sentence to the original in-
struction: “Please try to provide a novel answer.”
For Multilingual Prompting, we use Google
Translate to translate each original question from
English into the same set of 14 non-English lan-
guages used in the main experiments.
