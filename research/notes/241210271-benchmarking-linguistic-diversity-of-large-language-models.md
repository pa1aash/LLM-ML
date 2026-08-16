---
title: '[2412.10271] Benchmarking Linguistic Diversity of Large Language Models'
id: 241210271-benchmarking-linguistic-diversity-of-large-language-models
tags:
- llm-nas-feedback-positioning-7125b1
- quantization-diversity
- output-diversity
- mode-collapse
created: '2026-08-16T16:50:55.133604Z'
updated: '2026-08-16T16:53:48.508831Z'
source: https://arxiv.org/abs/2412.10271
source_domain: arxiv.org
fetched_at: '2026-08-16T16:50:55.133167Z'
fetch_provider: builtin
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Benchmarks lexical, syntactic, and semantic diversity of LLM outputs (Llama-3.1,
  Mistral-Nemo, OLMo, Falcon, Gemma-2, Qwen2.5) across five NLG tasks and isolates
  the causal effect of post-training 4-bit quantization on diversity using Qwen2.5
  at multiple scales (0.5B-32B). Directly answers the target gap: quantizing Qwen2.5
  to 4-bit with bitsandbytes (vs. bf16) does NOT affect semantic diversity but REDUCES
  both syntactic and lexical diversity; the lexical-diversity drop is more pronounced
  in smaller models while the syntactic-diversity drop is more pronounced in larger
  models, indicating quantization degrades diversity of linguistic FORM (word choice,
  sentence structure) rather than content/meaning. Also finds preference tuning (DPO)
  reduces syntactic diversity while raising lexical diversity, and that all six state-of-the-art
  LLMs fall well short of human diversity on the story-generation task specifically
  -- the same task category (creative, open-ended generation) as architecture proposal.'
---

[2412.10271] Benchmarking Linguistic Diversity of Large Language Models
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Computation and Language
arXiv:2412.10271
(cs)
[Submitted on 13 Dec 2024 (
v1
), last revised 25 Jul 2025 (this version, v2)]
Title:
Benchmarking Linguistic Diversity of Large Language Models
Authors:
Yanzhu Guo
,
Guokan Shang
,
Chloé Clavel
View a PDF of the paper titled Benchmarking Linguistic Diversity of Large Language Models, by Yanzhu Guo and 2 other authors
View PDF
HTML (experimental)
Abstract:
The development and evaluation of Large Language Models (LLMs) has primarily focused on their task-solving capabilities, with recent models even surpassing human performance in some areas. However, this focus often neglects whether machine-generated language matches the human level of diversity, in terms of vocabulary choice, syntactic construction, and expression of meaning, raising questions about whether the fundamentals of language generation have been fully addressed. This paper emphasizes the importance of examining the preservation of human linguistic richness by language models, given the concerning surge in online content produced or aided by LLMs. We propose a comprehensive framework for evaluating LLMs from various linguistic diversity perspectives including lexical, syntactic, and semantic dimensions. Using this framework, we benchmark several state-of-the-art LLMs across all diversity dimensions, and conduct an in-depth case study for syntactic diversity. Finally, we analyze how different development and deployment choices impact the linguistic diversity of LLM outputs.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2412.10271
[cs.CL]
(or
arXiv:2412.10271v2
[cs.CL]
for this version)
https://doi.org/10.48550/arXiv.2412.10271
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Yanzhu Guo [
view email
]
[v1]
Fri, 13 Dec 2024 16:46:03 UTC (9,227 KB)
[v2]
Fri, 25 Jul 2025 21:23:51 UTC (118 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Benchmarking Linguistic Diversity of Large Language Models, by Yanzhu Guo and 2 other authors
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
2024-12
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

Benchmarking Linguistic Diversity of Large Language Models
Yanzhu Guo∗
ALMAnaCH
Inria Paris
Guokan Shang
IFM Paris
MBZUAI
yanzhu.guo@inria.fr
guokan.shang@mbzuai.ac.ae
chloe.clavel@inria.fr
Chloé Clavel
ALMAnaCH
Inria Paris
Abstract
The development and evaluation of Large
Language Models (LLMs) has primarily
focused on their task-solving capabilities,
with recent models even surpassing hu-
man performance in some areas.
How-
ever, this focus often neglects whether
machine-generated language matches the
human level of diversity, in terms of vo-
cabulary choice, syntactic construction, and
expression of meaning, raising questions
about whether the fundamentals of language
generation have been fully addressed. This
paper emphasizes the importance of exam-
ining the preservation of human linguistic
richness by language models, given the con-
cerning surge in online content produced or
aided by LLMs. We adapt a comprehensive
framework for evaluating LLMs from vari-
ous linguistic diversity perspectives includ-
ing lexical, syntactic, and semantic dimen-
sions. Using this framework, we benchmark
several state-of-the-art LLMs across all di-
versity dimensions, and conduct an in-depth
analysis for syntactic diversity. Finally, we
analyze how the design, development and
deployment choices of LLMs impact the lin-
guistic diversity of their outputs, focusing
on the creative task of story generation.
1
Introduction
Recent Large Language Models (LLMs) have
exhibited outstanding capabilities in generating
both natural and formal language (Brown et al.,
2020; Touvron et al., 2023), while also achieving
human-level performance in language understand-
ing, commonsense reasoning, and various other
tasks (Hendrycks et al., 2020).
This has led to
evaluations that predominantly focus on these spe-
cific abilities (Wang et al., 2024).
Meanwhile,
other evaluation studies address well-recognized
∗This work was partially done during the author’s affil-
iation with École Polytechnique.
issues in LLMs, such as factuality (Maynez et al.,
2020), safety (Zhang et al., 2024), and fairness
(Gallegos et al., 2024), which remain focal points
of ongoing research.
However, there is a no-
table lack of attention paid to linguistic perspec-
tives, particularly in diversity (Guo et al., 2024b),
despite the fundamental objective of natural lan-
guage generation being to produce outputs that are
not only accurate but also diverse (Tevet and Be-
rant, 2021).
Recent studies have highlighted concerns re-
garding the linguistic diversity of LLM outputs.
By comparing human and model-generated con-
tent, researchers have shown that models fre-
quently struggle to reflect the nuances and vari-
ations found in human expression (Shaib et al.,
2024a; Giulianelli et al., 2023).
Additionally,
these concerns are reinforced by findings that
training language models on synthetic text can
lead to a further decline in linguistic diversity
(Guo et al., 2024b).
In fact, LLMs tend to be inherently conserva-
tive in producing diverse content. During train-
ing, models undergo homogenization to the most
frequent patterns in the training data, where cre-
ative outlier narratives, views, styles, and knowl-
edge are often underrepresented (Kandpal et al.,
2023). Unlike models, human language produc-
tion involves a complex interplay of factors that
go beyond merely optimizing probabilities (Holtz-
man et al., 2020). It is therefore crucial to empha-
size evaluating output diversity in language mod-
els and systematically consider these metrics to
guide future model design, development and de-
ployment decisions.
Currently, principled and comprehensive stud-
ies on evaluating linguistic diversity are lacking
in the literature (Shaib et al., 2024a).
While
some works on Natural Language Generation
(NLG) report diversity metrics, they typically fo-
cus on a single diversity aspect (e.g., lexical diver-
1
arXiv:2412.10271v2  [cs.CL]  25 Jul 2025
sity (Chakrabarty et al., 2022)), often experiment-
ing within a single domain and task (e.g., news
summarization (Shaib et al., 2024a)). This narrow
focus is problematic since diversity varies across
aspects and depends on the domain (Guo et al.,
2024b). Although some efforts have been made
to assess the influence of reinforcement learning
from human feedback (RLHF) on diversity (Kirk
et al., 2024), the impact of other key design and
development stages—such as model scale, quan-
tization, decoding strategy, and prompt formula-
tion—remains unexplored. Additionally, there is a
limited understanding of how LLMs develop the
capability to generate diverse language through
successive pretraining checkpoints. Ultimately, no
study has benchmarked the diversity performance
of state-of-the-art LLMs across different aspects
and domains.
In this work, we first establish a framework for
evaluating linguistic diversity of LLM outputs on
a corpus level. We then benchmark six prominent
LLMs on five NLG tasks, and compare the diver-
sity of their outputs across three different aspects:
lexical, syntactic, and semantic. We place partic-
ular emphasis on story generation, the most cre-
ative task where linguistic diversity plays a cru-
cial role, conducting a deeper analysis in this con-
text. Specifically, we examine syntactic diversity
through a case study comparing the distribution
of dependency trees in human-written and LLM-
generated texts. Finally, we also investigate how
LLM output diversity changes across different de-
velopment stages, and with varying decisions of
deployment.
The main research questions we address are as
follows:
1. What are the key aspects of LLM output diver-
sity, and how can they be evaluated? (See § 3)
2. How do state-of-the-art LLMs perform in terms
of diversity across different tasks? (See § 5)
3. How does diversity change during each LLM
development stage (e.g., pretraining, super-
vised fine-tuning (SFT), preference tuning)?
(See § 6.1)
4. How do different design (e.g., model scale,
training data) and deployment (e.g., decod-
ing strategy, prompt formulation, quantization)
choices affect diversity? (See § 6.2, § 6.3 and
§ 6.4)
It is worth noting that we study linguistic diver-
sity in a monolingual context, focusing on the En-
glish language. However, the evaluation method-
ology is language agnostic and could easily be ex-
tended to other languages, given that employed
NLP toolkits (e.g., dependency parsers, sentence
embeddings) exist for the language. Furthermore,
our approach to analyzing the influence of vari-
ous factors on LLM outputs is adaptable to other
dimensions, such as linguistic naturalness (Guo
et al., 2024a).
The code for our research is available at
https://github.com/YanzhuGuo/
llm-diversity.
2
Related Work
In this section, we review methods for evaluat-
ing and analyzing linguistic diversity. We define
linguistic diversity as the natural variation in hu-
man language across core linguistic properties, in-
cluding vocabulary usage, grammatical structures,
and semantic nuances. In contrast, a separate line
of research focuses on socio-linguistic diversity
(Hayati et al., 2023; Lahoti et al., 2023), which
falls beyond the scope of our study.
2.1
Evaluation of Human Language
Early metrics for linguistic diversity, proposed by
linguists, were developed for studies of language
acquisition and language disorder detection. For
example, Fergadiotis et al. (2013) employed lexi-
cal diversity metrics to identify symptoms of apha-
sia, while McNamara et al. (2010) showed that
both syntactic complexity and lexical diversity can
predict essay quality. Another study by Clercq and
Housen (2017) manually annotated a small cor-
pus of texts produced by second language learners
for syntactic features such as syntactic length and
clause types, considering their variation as a di-
versity index. However, these metrics are limited
to evaluating human-written texts and either focus
exclusively on lexical diversity or lack scalability
due to the need for manual annotation.
The evaluation of linguistic diversity in model-
generated language has emerged as a relatively
recent focus of research.
This development is
driven, in part, by growing concerns over the
increasing online prevalence of model-generated
or model-influenced content (Geng and Trotta,
2024), prompting questions about whether LLMs
can reflect the linguistic richness characteristic of
human language (Guo et al., 2024b). However,
assessing linguistic diversity is meaningful only
2
when the generated text meets basic standards of
quality. For instance, a randomly initialized model
might produce token sequences with high lexi-
cal diversity, but such outputs lack any practical
value (Uchendu et al., 2023). Recent advances in
language generation quality have brought model
outputs closer than ever to human-like coherence
and plausibility, making the evaluation of linguis-
tic diversity more relevant and necessary than be-
fore.
2.2
Evaluation of Generated Language
To the best of our knowledge, Tevet and Be-
rant (2021) were the first authors to systemati-
cally evaluate diversity in NLG. They proposed
to create diversity metrics from any two-sentence
similarity measure, defining diversity as the in-
verse of the mean similarity score across all un-
ordered pairs. N-gram-based metrics were used to
assess form diversity, while model-based metrics
like Sentence-BERT similarity measured content
diversity. They concluded that a notable dispar-
ity exists between automatic metrics and human
judgment, and that human evaluation of diversity
becomes challenging in sets with more than ten
sentences.
Since then, additional metrics have been pro-
posed to capture linguistic diversity, including se-
mantic diversity metrics based on natural language
inference (Stasaski and Hearst, 2022) or semantic
entropy (Han et al., 2022), and syntactic diversity
metrics derived from n-grams of Part-of-Speech
(POS) tags (Giulianelli et al., 2023) or graph sim-
ilarity kernels of syntax trees (Guo et al., 2024b).
Another relevant research direction involves
divergence-based metrics that compare the distri-
butions of human-written and machine-generated
text. Examples included MAUVE (Pillutla et al.,
2021), which leveraged distributions of GPT-2
embeddings, as well as later approaches based
on specific linguistic features (Guo et al., 2024a).
While such metrics do not explicitly measure lin-
guistic diversity, they can offer insights into dis-
tributional differences, of which diversity is a key
component.
2.3
Impact of LLMs on Linguistic Diversity
Diverging from the above research focused on de-
veloping methods to evaluate linguistic diversity,
another line of work explores how LLM-generated
content impact future models or human writing
patterns, often demonstrating a decline in diver-
sity. Guo et al. (2024b) showed that iteratively
training LLMs on synthetic data generated by ear-
lier models leads to a consistent decline in lexi-
cal, syntactic, and semantic diversity, especially
for tasks requiring high creativity. Similarly, Pad-
makumar and He (2024) reported a statistically
significant reduction in linguistic diversity when
humans write with InstructGPT. This reduction
in linguistic diversity is also observed in other
contexts: Liang et al. (2024) identified a signifi-
cant frequency shift toward LLM-preferred words
in academic writing, while Luo et al. (2024) re-
ported reduced morphosyntactic diversity in ma-
chine translations compared to human transla-
tions.
Closely related to our work, Kirk et al. (2024)
examined how SFT and preference tuning affect
LLM generalization and diversity.
They found
that preference tuning substantially reduces lexi-
cal and semantic diversity compared to SFT. Our
research also explores the factors that influence di-
versity while broadening the analysis to include
a wider range of diversity aspects, models, tasks
and factors.
However, our findings on the im-
pact of preference tuning differ from those of Kirk
et al. (2024), likely due to differences in task do-
main, accentuating the importance of contextual-
izing conclusions.
3
Metrics for Linguistic Diversity
In this section, we present the three types of di-
versity central to our study: lexical, syntactic, and
semantic diversity.
According to Tevet and Berant (2021), diversity
can be divided into two primary dimensions: form
diversity and content diversity. Lexical and syn-
tactic diversity are sub-aspects within form diver-
sity, whereas semantic diversity pertains to content
diversity.
While additional sub-aspects of form
diversity, such as style diversity, exist and could
potentially be measured through style representa-
tions (Soto et al., 2024), these aspects are gener-
ally less interpretable and often overlap with other
dimensions of diversity. For instance, style diver-
sity inherently intersects with lexical and syntac-
tic diversity, as stylistic choices typically involve
preferences in vocabulary and grammar. There-
fore, in this study, we concentrate on the three di-
versity aspects (lexical, syntactic, and semantic)
that are clearly defined, straightforward to inter-
3
pret, and exhibit relatively low mutual correlation
(further detailed in Section 5.1).
In terms of evaluation protocol, Kirk et al.
(2024) distinguish between across-input diversity
and per-input diversity.
Across-input diversity
refers to the diversity of outputs across different
inputs, with only one output generated per input.
In contrast, per-input diversity evaluates the capa-
bility of the model to produce diverse outputs for
a single input.
In our study, we choose to measure across-
input diversity, as we focus on general linguis-
tic patterns across a broad range of generations.
Formally, given a set of generated outputs S =
{s1, s2, . . . , sn}, we compute Div(S) differently
depending on the aspect of diversity: for lexical
diversity, S is treated as a set of n-grams, while
for syntactic and semantic diversity, S is consid-
ered as a set of sentences.
We build on the linguistic diversity evaluation
framework and preprocessing methods of Guo
et al. (2024b), but shift the focus from studying
the effects of recursive synthetic training on OPT
(Zhang et al., 2022) to comparing linguistic diver-
sity across a range of state-of-the-art LLMs. We
also investigate how various design choices such
as model scale and training data, and deployment
factors such as decoding strategy, prompt formula-
tion and quantization, impact diversity. In princi-
ple, the same research protocol could be extended
to examine per-input diversity, allowing for the in-
vestigation of uncertainty and variability in text
generation (Giulianelli et al., 2023). Although this
lies beyond the scope of the current study, it rep-
resents a promising direction for future work.
In the following sections, we describe each as-
pect of diversity and the specific metrics used to
assess them.
3.1
Lexical Diversity
Lexical diversity is a measure of the variety of
vocabulary used within a text or set of texts. In
essence, it assesses the richness or variability of
word choices. High lexical diversity indicates a
broad range of unique words, while low lexical di-
versity suggests repetitive or limited vocabulary.
We employ Unique-n (Johnson, 1944; Templin,
1957), established for evaluating lexical diversity.
It is calculated as the ratio of unique n-grams to
the total number of n-grams. When n = 1, it is
equivalent to Type-Token Ratio (Johnson, 1944;
Templin, 1957). We report the average Unique-
n across unigrams, bigrams, and trigrams. Origi-
nally used in child language research, Unique-n is
useful for assessing language development, where
a lower value might indicate limited lexical vari-
ety (Miller, 1981). We use the global Unique-n
measure rather than the moving average Unique-
n because we are interested in the overall diver-
sity capabilities of LLMs across different inputs
rather than their performance on individual inputs.
Moving average methods might miss global lexi-
cal repetitions due to their localized nature (Best-
gen, 2023). To mitigate the influence of output
length on Unique-n, we always randomly choose
40K samples to constitute the set of n-grams for
each n.
3.1.1
Syntactic Diversity
Syntactic diversity refers to the range and variety
of sentence structures used in a text or set of texts.
It assesses how flexibly and creatively different
grammatical structures, such as phrases, clauses,
and sentence types, are employed. High syntac-
tic diversity suggests varied sentence forms, while
low syntactic diversity indicates repetitive or sim-
plistic sentence structures. Syntactic diversity is
a crucial but often neglected aspect of language.
Exposure to a variety of syntactic structures helps
language learners and models develop a richer un-
derstanding of language (Aggarwal et al., 2022).
Diverse syntactic forms enhance expressiveness
and subtlety in text, impacting its style and tone
(Edwards and Bastiaanse, 1998). While research
on syntactic diversity exists, it typically relies on
manual annotation, which can be both costly and
error-prone (Clercq and Housen, 2017).
To address this limitation, we employ a graph-
based metric for quantifying syntactic diversity
(Guo et al., 2024b). This metric relies on a neu-
ral parser (Qi et al., 2020) to generate dependency
trees from sentences, following the universal de-
pendencies framework. In these trees, nodes rep-
resent words and edges capture syntactic depen-
dencies, with nodes labeled by the corresponding
part-of-speech (PoS) tags. The Weisfeiler-Lehman
(WL) graph kernel (Shervashidze et al., 2011;
Siglidis et al., 2020) is applied to map these trees
into a reproducing kernel Hilbert space, where
structurally similar graphs are positioned closer
together based on the WL isomorphism test. Syn-
tactic diversity is then computed as the average
pairwise distance between these graphs, formal-
4
Instruction
Input
Output
Language Modeling (LM)
Not applicable (no instruction)
Block of 128 tokens from Wikipedia
Prediction of the next block
Machine Translation (MT)
Translate from French to English
News story sentence in French
Corresponding English translation
Summarization (Summ)
Summarize the following article
Full news article from the BBC
Summary of the news article
Next Utterance Generation (NUG)
Continue the following dialogue
Scripted dialogue on general topics
Next utterance of the dialogue
Automatic Story Generation (ASG)
Continue the following story
Story prompt shared by Reddit users
Story continuation based on the prompt
Table 1: Summary of instructions, inputs, and outputs for benchmarked NLG tasks. Task instructions are
placed in the system input when supported, otherwise prepended to the user input.
ized as: Divsyn(S) =
1
(n
2)
P
1≤i<j≤n WL(si, sj).
3.1.2
Semantic Diversity
Semantic diversity refers to the range and vari-
ety of meanings or ideas conveyed within a text
or set of texts.
It evaluates how broadly and
uniquely different concepts, topics, or ideas are
expressed, reflecting the depth and scope of the
content. Low semantic diversity often indicates
repetition or a narrow focus, whereas high seman-
tic diversity typically suggests coverage of a wide
array of topics. However, texts should meet a ba-
sic quality standard before being evaluated for se-
mantic diversity, since high semantic diversity can
also arise from noisy or irrelevant content. Re-
cent studies (Tevet and Berant, 2021; Stasaski and
Hearst, 2022) have pointed out that traditional lex-
ical metrics may not fully capture semantic diver-
sity. Similar words can convey different meanings,
and different words can convey similar meanings
(Yarats and Lewis, 2018).
To address this, we first convert sentences
into semantically meaningful embeddings using
Sentence-BERT (Reimers and Gurevych, 2019).
Semantic diversity is then quantified as the dis-
persion of these embeddings in the semantic
space, measured by the average pairwise co-
sine distance (scaled to the range [0, 1]) be-
tween all embedding vectors:
Divsem(S)
=
1
(n
2)
P
1≤i<j≤n
dcos(e(si),e(sj))
2
, where e represents
Sentence-BERT embeddings.
4
Settings for Diversity Benchmarking
We outline the tasks and models used to estab-
lish our linguistic diversity benchmark. We de-
code the outputs for all tasks and models using a
combination of nucleus sampling (t=0.6) and top-
k sampling (k=0.9). We further analyze in Section
6.2 the impact of different decoding parameters on
output diversity.
4.1
Generation Tasks
To effectively compare the linguistic diversity of
LLM outputs across various scenarios, we choose
five tasks with progressively increasing levels of
“creativity”. The inputs, outputs, and instructions
for each task are summarized in Table 1. To main-
tain general model behavior and avoid overly in-
fluencing responses through prompt design, we
keep the instructions minimal.
For each task, we randomly select 10K sam-
ples from the original dataset. While our exper-
iments are conducted using a single dataset per
task, we deliberately select the most representa-
tive for each. Nonetheless, the conclusions drawn
from our experiments should be interpreted within
the context of these datasets. We now provide a
detailed introduction to each task and its associ-
ated dataset.
Language Modeling (LM) involves predicting
the next token in a sequence based on the preced-
ing tokens and is fundamental to all NLG applica-
tions. We use the Wikitext-2 dataset (Merity et al.,
2017) to evaluate general purpose language mod-
eling. Derived from Wikipedia articles, Wikitext-2
offers a rich corpus with around 2 million tokens
across diverse topics. We chunk texts into blocks
of 128 tokens and ask the models to predict the
next 128 tokens. Language modeling serves as the
basis of all other tasks, so it is considered as the
least creative.
Machine translation (MT) aims to transfer text
from one language to another while maintaining
the original meaning. We use the WMT-14 dataset
(Bojar et al., 2014) which contains parallel corpora
for multiple language pairs. For our experiments,
we focus on a subset of this benchmark that in-
cludes French-to-English sentence pairs from mul-
tiple sources. We classify this task as having a low
level of creativity, as the output is expected to con-
vey exactly the same meaning as the input.
Summarization (Summ) is the process of gen-
erating concise summaries of lengthy texts, pre-
5
LM
MT
Summ
NUG
ASG
0.40
0.45
0.50
0.55
0.60
0.65
Lexical Diversity
LM
MT
Summ
NUG
ASG
0.30
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
0.75
Syntactic Diversity
LM
MT
Summ
NUG
ASG
0.41
0.42
0.43
0.44
0.45
0.46
0.47
0.48
Semantic Diversity
Human
Input
Qwen2.5(7B)
Mistral-Nemo(12B)
OLMo(7B)
Falcon(7B)
Llama-3.1(8B)
Gemma-2(9B)
Figure 1: Linguistic diversity benchmarking results for NLG tasks detailed in Table 1.
serving key information while minimizing redun-
dancy. We use the XLSUM dataset (Hasan et al.,
2021), which features news articles in various lan-
guages along with their summaries. Our experi-
ments focus on the English portion of the dataset.
While we also categorize this task as low in cre-
ativity, it allows slightly more flexibility than ma-
chine translation, as the model must decide which
information to prioritize and include in the sum-
mary.
Next Utterance Generation (NUG) aims to pro-
duce natural utterances in conversations while
maintaining contextual relevance. For this task,
we use the DailyDialog dataset (Sai et al., 2020),
a human-curated multi-turn dialogue corpus de-
signed to cover a broad range of topics relevant
to everyday interactions. In our setup, the model
is always prompted to predict the final utterance
based on all preceding dialogue turns. We con-
sider next utterance generation to be a creative
task, as there is a large space of possible and co-
herent utterances in response to a certain dialog
context. However, the everyday nature and struc-
ture of the dataset place some limits on the level
of creativity.
Automatic Story Generation (ASG) centers on
producing engaging and coherent narratives from
story prompts or initial contexts. We employ the
WritingPrompts dataset (Fan et al., 2018), which
comprises prompts and corresponding stories con-
tributed by Reddit users. It includes a wide va-
riety of prompts in different formats, encourag-
ing diverse and creative responses. Among our
tasks, we consider story generation to be the most
creative, as the prompts typically impose minimal
constraints on narrative structure and content, al-
lowing for maximal expressive freedom.
4.2
Language Models
We evaluate the following families of models:
Llama (Dubey et al., 2024), Mistral (Jiang et al.,
2023), Olmo (Groeneveld et al., 2024), Gemma
(Team et al., 2024), Qwen (Yang et al., 2024) and
Falcon (Almazrouei et al., 2023). The comparison
of these models across various key characteristics
is provided in Table 4 in Appendix A.
To ensure comparability, we select the latest
version of each model family that is closest in
scale to 7 billion parameters. The scale selected
for each model is specified in the legend of Fig-
ure 1. We purposefully include models developed
by organizations from different countries to be
culturally inclusive. For language modeling, we
use base models. For all other tasks, we employ
instruction-tuned versions.
5
Results of Diversity Benchmarking
Figure 1 visualizes the benchmarking results of
linguistic diversity across various tasks.
Round
dots represent the diversity of model outputs,
6
Perplexity
(LM)
COMET
(MT)
BERTScore
(Summ)
BERTScore
(NUG)
BERTScore
(ASG)
Lexical
Diversity
Syntactic
Diversity
Semantic
Diversity
0.31
0.35
0.68
0.13
-0.43
-0.64
0.12
-0.63
-0.36
-0.73
0.28
0.48
-0.015
0.36
0.1
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Figure 2: Pearson correlation matrix between diversity
metrics and quality metrics.
Lexical
Diversity
Syntactic
Diversity
Semantic
Diversity
Lexical
Diversity
Syntactic
Diversity
Semantic
Diversity
1
0.13
-0.14
0.13
1
0.55
-0.14
0.55
1
0.0
0.2
0.4
0.6
0.8
1.0
Figure 3: Pearson correlation matrix be-
tween different diversity metrics.
while solid lines represent human reference out-
puts.
Dashed lines depict the diversity of task-
specific inputs (as detailed in Table 1), reflecting
the conditions under which the outputs were gen-
erated. Tasks are organized in ascending order of
creativity level. The detailed numerical results are
provided in Table 5 in Appendix B.
For the machine translation task, the inputs are
in French; hence, semantic diversity is measured
using a multilingual SentenceBERT (Reimers and
Gurevych, 2020), and syntactic diversity is evalu-
ated with a French-specific dependency parser. As
a result, these scores may not be directly compa-
rable to those for English. The diversity of human
reference outputs serves as a baseline for interpret-
ing whether the model under or over represents the
diversity for each task.
In this section, we first analyze metric correla-
tions in Section 5.1, then compare diversity scores
across tasks and models in Section 5.2. Finally,
in Section 5.3, we perform a case study on syntac-
tic diversity in story generation, comparing human
and model outputs.
5.1
Correlation Study
Correlation between diversity and quality. We
manually verify that all models produce plausi-
ble and coherent text that meets the basic require-
ments for diversity evaluation across all tasks.
Building on this, we examine more specific qual-
ities of the model outputs.
Figure 2 illustrates
the correlation between diversity and quality in
model outputs, using task-specific automatic met-
rics as quality indicators. For the language model-
ing task, perplexity is used to evaluate the model’s
performance on reference text continuations. For
machine translation, we use COMET (Rei et al.,
2020), which takes into account both the source
text and reference translation. For the remaining
three tasks, BERTScore (Zhang et al., 2020) is
used to measure the relevance between inputs and
outputs. Due to the inherently subjective nature
of these tasks, automatic metrics generally exhibit
weak correlations with human judgments (Liu
et al., 2023) and should be interpreted cautiously.
Nonetheless, we adopt BERTScore as an approx-
imate quality indicator, as embedding-based met-
rics of this kind demonstrate the strongest system-
level correlation with human evaluations among
available automatic measures (Chhun et al., 2022).
Our results show a positive correlation between
quality and lexical as well as semantic diversity
in model outputs. In contrast, syntactic diversity
often exhibits negative correlations, where higher
syntactic diversity is associated with lower quality
scores. This may be attributed to the tested do-
mains inherently exhibiting low ground-truth syn-
tactic diversity (e.g., in language modeling) or to
the limitations of quality metrics in recognizing
the value of syntactic variation (e.g., in summa-
rization, automatic story generation, and next ut-
terance generation). These findings highlight the
need to report diversity metrics alongside quality
metrics for comprehensive evaluation, as the rela-
tionship between the two is not consistent across
tasks or aspects.
Correlation between diversity aspects. The cor-
relations between different diversity aspects are
shown in Figure 3, revealing a moderate positive
correlation between syntactic and semantic diver-
sity (0.55).
However, lexical diversity shows a
weak positive relationship with syntactic diversity
(0.13) and a slight negative correlation with se-
mantic diversity (-0.14), indicating that the rich-
ness of vocabulary is independent from the variety
of grammatical structures and meaning.
7
Llama
Mistral
Qwen
Gemma
Falcon
OLMo
Precision
99.20
99.20
99.47
99.07
99.63
99.73
Recall
35.20
65.87
75.27
37.97
75.00
39.40
Table 2: Comparison of dependency tree distribu-
tions between humans and models for the story
generation task.
5.2
Comparison Across Tasks and Models
We now examine the results in Figure 1 to as-
sess human diversity results across tasks, com-
pare model diversity against human diversity, and
finally evaluate the diversity performance across
different models.
Human output diversity. Human-level diversity
varies across tasks, with no clear correlation ob-
served among different aspects.
Notably, utter-
ances in human dialogs exhibit the lowest lexical
diversity and the highest syntactic diversity, unlike
the written text present in the remaining four tasks.
The low lexical diversity may be attributed to the
conversations being specifically scripted for En-
glish learners to practice daily-life dialog. These
dialogs focus on generic topics, leading to a lim-
ited range of vocabulary. In contrast, the high syn-
tactic diversity can be explained by the inherent
spontaneity of conversational language, where dif-
ferent speakers tend to vary significantly in their
use of syntactic structures (Healey et al., 2014;
Dubuisson Duplessis et al., 2017). Human sum-
maries show limited lexical and syntactic variation
but exhibit the highest semantic diversity, suggest-
ing a narrow range in form but a broad range in
content. In contrast, human translations score low-
est in semantic diversity, reflecting the restricted
topical scope of the source texts. Wikipedia-based
language modeling displays high topic diversity,
while human-written stories tend to be diverse
across all three dimensions.
Model output diversity.
LLMs lack diversity
compared to humans for tasks demanding high
levels of creativity, such as story generation. Over-
all, the scores of different LLMs across tasks and
diversity aspects tend to resemble each other, po-
tentially due to the use of similar development pro-
cedures, architectures, and datasets. However, this
remains an assumption, as most LLM developers
do not fully disclose their training data or proto-
cols, even when the models themselves are open-
weight. The extent to which LLMs under- or over-
represent diversity compared to humans varies sig-
nificantly by the task domain.
For the task of
story generation, which demands the highest lev-
els of creativity and freedom of expression, LLMs
consistently lag behind humans in all three diver-
sity aspects. In contrast, for tasks like next utter-
ance generation, LLMs surpass human references
in both lexical and semantic diversity. This dis-
crepancy arises because the DailyDialog dataset
focuses on generic, everyday topics designed for
English language learning, while LLMs, uncon-
strained by this context, frequently steer conversa-
tions toward more complex topics.
LLM comparisons.
While the overall perfor-
mance of the models appears to be similar, in-
depth comparisons showcase notable differences.
Models pretrained on fewer tokens, such as Fal-
con and OLMo, consistently generate outputs with
lower lexical diversity. Specifically, Falcon and
OLMo are pretrained on 1.5T and 2.7T tokens,
respectively, compared to Llama-3.1, which is
trained on 15T tokens. However, this effect is not
observed for syntactic or semantic diversity. Mod-
els with less strict data filtration exhibit greater di-
versity in creative tasks, such as story generation.
For example, Qwen2.5, which filters data exclu-
sively for quality, exhibits significantly higher di-
versity in story generation across all aspects com-
pared to Llama-3.1, Gemma-2, and OLMo, whose
data is extensively filtered for quality, privacy, and
safety.
5.3
Comparing Syntactic Diversity Between
Humans and Models
To further compare humans and models, we con-
duct a case study on syntactic diversity using de-
pendency tree distribution. Syntactic diversity is
chosen as it is less explored than lexical and se-
mantic diversity. Moreover, syntactic patterns re-
flected by POS tag n-grams are more generalizable
than lexicon n-grams and more interpretable than
semantic embeddings.
We adopt the Precision-Recall framework pro-
posed by Le Bronnec et al. (2024). This frame-
work relies on GPT-2 embeddings, followed by
Principal Component Analysis (PCA) and K-
means clustering, to estimate the supports of text
distributions. In our study, we replace the orig-
inal GPT-2 embeddings with the implicit distri-
bution of dependency tree embeddings induced
by the WL graph kernel. Precision is defined as
the proportion of dependency trees from model-
8
Human
Language Models
POS tag n-gram
Example
POS tag n-gram
Example
n=3
(ADV, ADV, ADP)
right along with
(PRON, NOUN, ADJ)
her voice soft
n=4
(VERB, ADP, DET, NOUN)
picking up the pieces
(NOUN, CCONJ, NOUN, PRON)
carvings and symbols that
n=5
(DET, NOUN, ADP, DET, NOUN)
the cackling of the fire
(PRON, NOUN, VERB, ADP, NOUN)
its feathers stained with blood
n=6
DET, ADJ, NOUN, ADP, DET, NOUN)
the old woman down the street
(ADJ, NOUN, ADP, NOUN, CCONJ, NOUN)
particular focus on time and space
Table 3: Examples of syntactic patterns favored by either humans or models are illustrated using n-grams
of POS tags. Human patterns are derived from human dependency trees that are not within the model
dependency tree neighborhoods, while model patterns have high frequency in model dependency trees
and low frequency in human dependency trees.
0B
2B
4B
6B
8B
10B
12B
20B
31B
62B
129B
257B
530B
1027B
2000B
SFT
DPO
Token Count/Alignment Stage
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Score
Lexical Diversity
Syntactic Diversity
Semantic Diversity
BERTScore
Figure 4: Linguistic diversity metrics after different LLM training stages. The pretraining stage is broken
into various steps with increasing token counts, which are presented on a log scale for visualization.
Experiments are conducted with the OLMo model on the story generation task.
Qwen2.5
Mistral-Nemo
OLMo
Falcon
Llama-3.1
Gemma-2
0.45
0.50
0.55
0.60
0.65
Diversity Score
Lexical Diversity - Base
Syntactic Diversity - Base
Semantic Diversity - Base
Lexical Diversity - Instruct
Syntactic Diversity - Instruct
Semantic Diversity - Instruct
Figure 5: Impact of instruction tuning.
generated text that lie within the support of de-
pendency trees from human-written text. A high
precision indicates that the model-generated struc-
tures are more plausible and human-like, thus re-
flecting their quality. Recall, on the other hand,
measures the proportion of dependency trees from
human-written text that fall within the support
of the model-generated distribution. A high re-
call suggests that the model captures the full di-
versity of human-written structures. The method
for computing pairwise distances between depen-
dency trees is described in Section 3.1.1, which
serves as the basis for constructing the distance
matrix. All other hyper-parameters remain con-
sistent with the original work (Le Bronnec et al.,
2024).
Table 2 presents the precision and recall scores
for all evaluated models on the story generation
task.
The results reveal that all models exhibit
near-perfect precision, indicating that almost all
generated sentences are syntactically plausible. In
contrast, recall scores are substantially lower than
precision scores across all models, revealing their
limited capacity to capture the full breadth of hu-
man syntactic diversity. This points to a notable
gap between models and humans in syntactic di-
versity for the story generation task where high
creativity is required.
To further illustrate these findings, Table 3 lists
examples of syntactic patterns (POS tag n-grams)
that are frequently found in human dependency
trees but are missing from the model-generated
9
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Temperature
0.48
0.50
0.52
0.54
0.56
0.58
0.60
Lexical Diversity
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Temperature
0.50
0.52
0.54
0.56
0.58
Syntactic Diversity
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Temperature
0.415
0.420
0.425
0.430
0.435
0.440
Semantic Diversity
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Temperature
0.81
0.82
0.83
0.84
BERTScore
Qwen2.5
OLMo
Mistral-Nemo
Falcon
Llama-3.1
Gemma-2
Figure 6: Impact of decoding parameters. Experiments are conducted on the story generation task.
ones. Conversely, we also identify syntactic pat-
terns that models over-generate but are less com-
mon in human outputs.
Recent studies (Shaib
et al., 2024b) indicate that models often memorize
syntactic templates encountered during pretrain-
ing, which are rarely overwritten during SFT and
preference tuning. This suggests that the observed
gap in syntactic patterns may stem from a mis-
match between pretraining and downstream task
domains. For instance, in the pretraining corpus of
OLMo, over 80% of the data originates from web
pages in Common Crawl, while less than 0.3%
comes from Project Gutenberg books, one of the
only sources potentially aligned with the narrative
style required for story generation (Soldaini et al.,
2024).
6
Factors Influencing LLM Diversity
In this section, we explore key factors that may
influence the diversity of LLM outputs. The fac-
tors under consideration include pretraining token
counts, instruction tuning, decoding parameters,
prompt formulation, model scale, and quantiza-
tion. For decoding parameters, prompt formula-
tion and instruction tuning, we conduct experi-
ments across all models. We employ OLMo for
assessing the impact of pretraining token counts
since it provides full access to its pretraining
datasets and model weights at various checkpoints
throughout its development. Since OLMo mod-
els are available in only two sizes, we additionally
leverage Qwen2.5 models (Yang et al., 2024) to
investigate the effects of model scale and quanti-
zation.
All experiments in this section are conducted on
the story generation task, where linguistic diver-
sity plays a central role. Its minimal input con-
straints and strong emphasis on creativity make it
an ideal benchmark for evaluating linguistic diver-
sity. Moreover, as shown in Figure 1, all models
fall significantly short of human performance in
terms of diversity on this task, highlighting the im-
portance of identifying which factors contribute to
this gap. We emphasize that the conclusions drawn
in this section are specific to the story genera-
tion task and should not be generalized to broader
LLM behavior without further investigation.
6.1
Impact of Training Stages
Pretraining. We choose OLMo, pretrained on the
Dolma corpus (Soldaini et al., 2024), to study the
evolution of linguistic diversity during pretrain-
ing. This is because OLMo is the only model in
our benchmark with publicly available intermedi-
10
ate checkpoints during pretraining. The results are
presented in Figure 4. Intitially, lexical diversity
is exceptionally high, as expected for an untrained
model that generates random tokens. This met-
ric drops sharply after the first checkpoint (2B to-
kens) but then gradually increases throughout the
pretraining process, without reaching saturation.
In contrast, syntactic diversity also experiences a
sharp decline early on; however, it saturates much
more quickly, fluctuating within a narrow range
afterward. Semantic diversity shows a steady in-
crease from the beginning but also saturates rel-
atively quickly. These observations suggest that
while increasing training data generally improves
lexical diversity, alternative strategies are needed
to enhance syntactic and semantic diversity.
Instruction tuning. We now move on to study
the impact of instruction tuning on linguistic diver-
sity. After pretraining, OLMo underwent super-
vised fine-tuning (SFT) on Tulu v2 (Ivison et al.,
2023) and direct preference optimization (DPO)
(Rafailov et al., 2023) on Ultrafeedback (Cui et al.,
2024), with DPO applied on top of SFT. We ob-
serve that SFT has minimal impact on any di-
versity metric, while DPO leads to a decrease in
syntactic diversity and an increase in lexical di-
versity, potentially reflecting characteristics of the
SFT and DPO datasets.
Since all models in our benchmark provide
both base and instruction-tuned versions, we ex-
tend our analysis to assess the impact of instruc-
tion tuning across the full set. As shown in Fig-
ure 5, the results mirror those observed for OLMo:
instruction-tuned versions show higher lexical di-
versity compared to their base counterparts but ex-
hibit reductions in syntactic and semantic diver-
sity. Notably, the decline in syntactic diversity is
more pronounced than that in semantic diversity.
These findings indicate that while additional train-
ing—regardless of the stage—enhances vocabu-
lary richness, aligning models with human prefer-
ences tends to constrain them to a narrower range
of grammatical structures and meanings.
6.2
Impact of Decoding Parameters
Achieving a balance between quality and diversity
in LLM outputs is a known challenge, as there is
often a trade-off between these two aspects (Cac-
cia et al., 2020). The choice of decoding strat-
egy plays a crucial role in controlling this trade-
off (Zhang et al., 2021).
Here, we investigate
Qwen2.5
Mistral-Nemo
OLMo
Falcon
Llama-3.1
Gemma-2
0.425
0.450
0.475
0.500
0.525
0.550
0.575
Diversity Score
Lexical Diversity - Standard
Syntactic Diversity - Standard
Semantic Diversity - Standard
Lexical Diversity - Creative
Syntactic Diversity - Creative
Semantic Diversity - Creative
Figure 7: Impact of prompt formulation.
how varying the decoding temperature affects the
outputs in the story generation task, with results
visualized in Figure 6.
Output quality is esti-
mated based on their relevance to the inputs, using
BERTScore as a metric.
The
results
show
that
increasing
the
temperature—making decoding less restrictive—
leads to greater lexical diversity, with only a
minor reduction in relevance to the inputs.
It
might be due to the creative nature of the story
generation task that the quality-diversity trade-off
is so subtle. For syntactic diversity, while most
models show fluctuating performance within a
certain range, some exhibit a clear downward
trend, specially OLMo and Falcon, which are
trained on significantly fewer tokens compared to
the other models. However, no consistent trends
are observed for semantic diversity metric as
decoding parameters change.
This aligns with
the observations of Tevet and Berant (2021),
which indicate that adjusting decoding parameters
tends to affect the form of the text rather than its
meaning.
Furthermore, we note that, across most models,
the relative ranking of diversity scores remains sta-
ble as the temperature varies. This suggests that
conducting experiments with a fixed temperature
is sufficient for consistent evaluation. Based on
our findings, we set the temperature to 0.6 for all
other experiments. Figure 6 shows that at a tem-
perature of 0.6, the relevance to the inputs remains
relatively high while diversity scores significantly
improve compared to lower temperatures.
6.3
Impact of Prompt Formulation
Previous studies have established that LLMs ex-
hibit considerable sensitivity to prompt formu-
lations, particularly affecting their performance
11
0.5B
1.5B
3B
7B
14B
32B
0.40
0.42
0.44
0.46
0.48
0.50
0.52
0.54
0.56
Diversity Score
Lexical Diversity - 16 bit
Syntactic Diversity - 16 bit
Semantic Diversity - 16 bit
Lexical Diversity - 4 bit
Syntactic Diversity - 4 bit
Semantic Diversity - 4 bit
Figure 8: Impact of model scale and quantization.
on discriminative downstream tasks (Sclar et al.,
2024; Wahle et al., 2024).
Here, we explore
whether the linguistic diversity of stories gener-
ated by LLMs is similarly influenced by varia-
tions in the formulation of prompts. We conduct
experiments across the full range of models, and
the results are depicted in Figure 7.
The solid
lines represent results obtained using the standard
prompt, consisting of the task-specific instruc-
tion “Please continue the following story” com-
bined with sample-specific inputs from the Writ-
ingPrompts dataset. To evaluate prompt sensitiv-
ity, we modify the prompt to explicitly encourage
creativity by changing the instruction to “Please
continue the following story and be as creative as
possible”. Results from these modified prompts
are shown as dash-dot lines in Figure 7.
Our analysis indicates that altering the prompt
formulation has minimal impact on the diver-
sity of generated stories across all three evalu-
ated aspects.
This suggests that the linguistic
patterns exhibited by LLMs across creative gen-
erations represent inherent model characteristics
that are less sensitive to prompt variations com-
pared to accuracy-based performance on discrim-
inative tasks. Consequently, enhancing linguistic
diversity in LLM outputs through straightforward
prompt engineering alone would be challenging.
6.4
Impact of Model Scale and Quantization
We now study the impact of model scale on
linguistic diversity with the Qwen2.5 model.
Qwen2.5 has been released in various sizes, rang-
ing from 0.5B to 72B parameters. Due to compu-
tational resource constraints, we limit our explo-
ration of linguistic diversity to models up to 32B
parameters. The results are presented in Figure 8.
We observe that lexical diversity consistently in-
creases with model size, while semantic diversity
remains stable throughout.
In contrast, syntac-
tic diversity remains relatively stable overall but
exhibits an initial increase followed by a decline,
peaking at 7B parameters, indicating that scaling
up is not always the solution to higher linguistic
diversity.
We further investigate the impact of post-
training quantization on linguistic diversity. We
quantize the Qwen2.5 models of various scales
to 4-bit precision with the bitsandbytes library1,
whereas the original models were run with bf16.
As shown in Figure 8, quantization does not affect
semantic diversity but reduces both syntactic and
lexical diversity. The reduction in lexical diversity
is more pronounced in smaller models, while the
effect on syntactic diversity becomes more evident
in larger models. This finding suggests that quan-
tization has greater impact on the diversity of form
rather than content.
7
Conclusion
Our study offers crucial insights into the linguis-
tic diversity of current LLMs.
By leveraging a
comprehensive evaluation framework focused on
lexical, syntactic, and semantic diversity, we pro-
vide a fresh perspective beyond traditional qual-
ity metrics. Our analysis reveals that, despite the
impressive capabilities of LLMs in generating co-
herent and plausible text, there is a significant gap
when it comes to replicating the linguistic rich-
ness of human language for creative tasks such as
story generation. Furthermore, we find that fac-
tors like pretraining data volume, instruction tun-
ing, decoding strategies, model scale, and quanti-
zation significantly influence diversity metrics. In
particular, while instruction tuning improves lex-
ical diversity, it constrains syntactic and seman-
tic diversity, indicating a narrowing of expressive
flexibility. These findings raise an important con-
cern: as LLMs become more prevalent in content
creation, their outputs may trend towards homog-
enization, risking a loss of linguistic richness. Our
research highlights the necessity of a more holistic
and forward-looking approach in developing lan-
guage models, one that prioritizes the preservation
of linguistic diversity alongside optimizing perfor-
mance metrics.
1https://huggingface.co/docs/bitsandbytes/index
12
Acknowledgments
We thank Professor Michalis Vazirgiannis for pro-
viding the computational resources that supported
this project. This research was partially funded by
the ANR-23-CE23-0033-01 SINNet project and
the ANR-TSIA HELAS chair.
References
Arshiya Aggarwal, Jiao Sun, and Nanyun Peng.
2022. Towards robust NLG bias evaluation with
syntactically-diverse prompts.
In Findings of
the Association for Computational Linguistics:
EMNLP 2022, pages 6022–6032, Abu Dhabi,
United Arab Emirates. Association for Compu-
tational Linguistics.
Ebtesam Almazrouei, Hamza Alobeidli, Abdu-
laziz Alshamsi, Alessandro Cappelli, Ruxan-
dra Cojocaru,
Mérouane Debbah,
Étienne
Goffinet,
Daniel
Hesslow,
Julien
Launay,
Quentin Malartic, et al. 2023. The falcon se-
ries of open language models. arXiv preprint
arXiv:2311.16867.
Yves Bestgen. 2023. Measuring lexical diversity
in texts: The twofold length problem.
Lan-
guage Learning.
Ondˇrej Bojar, Christian Buck, Christian Feder-
mann, Barry Haddow, Philipp Koehn, Johannes
Leveling, Christof Monz, Pavel Pecina, Matt
Post, Herve Saint-Amand, Radu Soricut, Lucia
Specia, and Aleš Tamchyna. 2014. Findings of
the 2014 workshop on statistical machine trans-
lation. In Proceedings of the Ninth Workshop
on Statistical Machine Translation, pages 12–
58, Baltimore, Maryland, USA. Association for
Computational Linguistics.
Tom Brown,
Benjamin Mann,
Nick Ryder,
Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, et al. 2020.
Language models are few-shot learners.
Ad-
vances in neural information processing sys-
tems, 33:1877–1901.
Massimo Caccia, Lucas Caccia, William Fedus,
Hugo Larochelle, Joelle Pineau, and Laurent
Charlin. 2020.
Language gans falling short.
In International Conference on Learning Rep-
resentations.
Tuhin Chakrabarty, Vishakh Padmakumar, and
He He. 2022.
Help me write a poem - in-
struction tuning as a vehicle for collaborative
poetry writing.
In Proceedings of the 2022
Conference on Empirical Methods in Natural
Language Processing, pages 6848–6863, Abu
Dhabi, United Arab Emirates. Association for
Computational Linguistics.
Cyril
Chhun,
Pierre
Colombo,
Fabian
M.
Suchanek, and Chloé Clavel. 2022.
Of hu-
man criteria and automatic metrics: A bench-
mark of the evaluation of story generation.
In Proceedings of the 29th International Con-
ference on Computational Linguistics, pages
5794–5836, Gyeongju, Republic of Korea. In-
ternational Committee on Computational Lin-
guistics.
Bastien De Clercq and Alex Housen. 2017.
A
cross-linguistic perspective on syntactic com-
plexity in l2 development: Syntactic elaboration
and diversity. The Modern Language Journal,
101(2):315–334.
Ganqu Cui, Lifan Yuan, Ning Ding, Guanming
Yao, Bingxiang He, Wei Zhu, Yuan Ni, Guo-
tong Xie, Ruobing Xie, Yankai Lin, et al. 2024.
Ultrafeedback: Boosting language models with
scaled ai feedback. In Forty-first International
Conference on Machine Learning.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav
Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Amy Yang, Angela Fan, et al. 2024.
The llama 3 herd of models.
arXiv preprint
arXiv:2407.21783.
Guillaume Dubuisson Duplessis, Chloé Clavel,
and Frédéric Landragin. 2017.
Automatic
measures to characterise verbal alignment in
human-agent interaction. In Proceedings of the
18th Annual SIGdial Meeting on Discourse and
Dialogue, pages 71–81, Saarbrücken, Germany.
Association for Computational Linguistics.
Susan Edwards and Roelien Bastiaanse. 1998.
Diversity in the lexical and syntactic abili-
ties of fluent aphasic speakers.
Aphasiology,
12(2):99–117.
Angela Fan, Mike Lewis, and Yann Dauphin.
2018. Hierarchical neural story generation. In
13
Proceedings of the 56th Annual Meeting of the
Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 889–898, Mel-
bourne, Australia. Association for Computa-
tional Linguistics.
G Fergadiotis, HH Wright, and TM West. 2013.
Measuring lexical diversity in narrative dis-
course of people with aphasia. American Jour-
nal of Speech-language Pathology, 22(2):S397–
408.
Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow,
Md Mehrab Tanjim, Sungchul Kim, Franck
Dernoncourt, Tong Yu, Ruiyi Zhang, and Nes-
reen K. Ahmed. 2024. Bias and fairness in large
language models: A survey.
Computational
Linguistics, 50(3):1097–1179.
Mingmeng Geng and Roberto Trotta. 2024.
Is
chatgpt transforming academics’ writing style?
arXiv preprint arXiv:2404.08627.
Mario Giulianelli,
Joris Baan,
Wilker Aziz,
Raquel Fernández, and Barbara Plank. 2023.
What comes next?
evaluating uncertainty in
neural text generators against human production
variability.
In Proceedings of the 2023 Con-
ference on Empirical Methods in Natural Lan-
guage Processing, pages 14349–14371, Singa-
pore. Association for Computational Linguis-
tics.
Dirk Groeneveld, Iz Beltagy, Pete Walsh, Ak-
shita Bhagia, Rodney Kinney, Oyvind Tafjord,
Ananya Harsh Jha, Hamish Ivison, Ian Magnus-
son, Yizhong Wang, Shane Arora, David Atkin-
son, Russell Authur, Khyathi Raghavi Chandu,
Arman Cohan, Jennifer Dumas, Yanai Elazar,
Yuling Gu, Jack Hessel, Tushar Khot, William
Merrill, Jacob Morrison, Niklas Muennighoff,
Aakanksha Naik, Crystal Nam, Matthew E. Pe-
ters, Valentina Pyatkin, Abhilasha Ravichan-
der, Dustin Schwenk, Saurabh Shah, Will
Smith, Emma Strubell, Nishant Subramani,
Mitchell Wortsman, Pradeep Dasigi, Nathan
Lambert, Kyle Richardson, Luke Zettlemoyer,
Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A.
Smith, and Hannaneh Hajishirzi. 2024. Olmo:
Accelerating the science of language models.
Yanzhu Guo, Simone Conia, Zelin Zhou, Min Li,
Saloni Potdar, and Henry Xiao. 2024a. Do large
language models have an english accent? eval-
uating and improving the naturalness of multi-
lingual llms. arXiv preprint arXiv:2410.15956.
Yanzhu Guo, Guokan Shang, Michalis Vazirgian-
nis, and Chloé Clavel. 2024b.
The curious
decline of linguistic diversity:
Training lan-
guage models on synthetic text.
In Findings
of the Association for Computational Linguis-
tics: NAACL 2024, pages 3589–3604, Mexico
City, Mexico. Association for Computational
Linguistics.
Seungju Han, Beomsu Kim, and Buru Chang.
2022. Measuring and improving semantic di-
versity of dialogue generation.
In Findings
of the Association for Computational Linguis-
tics: EMNLP 2022, pages 934–950, Abu Dhabi,
United Arab Emirates. Association for Compu-
tational Linguistics.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful
Islam, Kazi Mubasshir, Yuan-Fang Li, Yong-
Bin Kang, M. Sohel Rahman, and Rifat Shahri-
yar. 2021. XL-sum: Large-scale multilingual
abstractive summarization for 44 languages. In
Findings of the Association for Computational
Linguistics: ACL-IJCNLP 2021, pages 4693–
4703, Online. Association for Computational
Linguistics.
Shirley Anugrah Hayati, Minhwa Lee, Dheeraj
Rajagopal, and Dongyeop Kang. 2023.
How
far can we extract diverse perspectives from
large language models? criteria-based diversity
prompting! arXiv preprint arXiv:2311.09799.
Patrick GT Healey, Matthew Purver, and Christine
Howes. 2014.
Divergence in dialogue.
PloS
one, 9(6):e98598.
Dan Hendrycks, Collin Burns, Steven Basart,
Andy Zou, Mantas Mazeika, Dawn Song, and
Jacob Steinhardt. 2020.
Measuring massive
multitask language understanding. In Interna-
tional Conference on Learning Representations.
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,
and Yejin Choi. 2020. The curious case of neu-
ral text degeneration. In International Confer-
ence on Learning Representations.
Hamish Ivison, Yizhong Wang, Valentina Pyatkin,
Nathan Lambert,
Matthew Peters,
Pradeep
14
Dasigi, Joel Jang, David Wadden, Noah A.
Smith, Iz Beltagy, and Hannaneh Hajishirzi.
2023. Camels in a changing climate: Enhanc-
ing lm adaptation with tulu 2.
Albert Q Jiang, Alexandre Sablayrolles, Arthur
Mensch, Chris Bamford, Devendra Singh Chap-
lot, Diego de las Casas, Florian Bressand,
Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, et al. 2023. Mistral 7b. arXiv preprint
arXiv:2310.06825.
Wendell Johnson. 1944. Studies in language be-
havior: A program of research. Psychological
Monographs, 56(2):1–15.
Nikhil Kandpal, Haikang Deng, Adam Roberts,
Eric Wallace, and Colin Raffel. 2023.
Large
language models struggle to learn long-tail
knowledge.
In International Conference
on Machine Learning, pages 15696–15707.
PMLR.
Robert Kirk, Ishita Mediratta, Christoforos Nalm-
pantis, Jelena Luketina, Eric Hambro, Edward
Grefenstette, and Roberta Raileanu. 2024. Un-
derstanding the effects of RLHF on LLM gener-
alisation and diversity. In The Twelfth Interna-
tional Conference on Learning Representations.
Preethi Lahoti,
Nicholas Blumm,
Xiao Ma,
Raghavendra Kotikalapudi, Sahitya Potluri, Qi-
jun Tan, Hansa Srinivasan, Ben Packer, Ahmad
Beirami, Alex Beutel, and Jilin Chen. 2023.
Improving diversity of demographic represen-
tation in large language models via collective-
critiques and self-voting.
In Proceedings of
the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 10383–
10405, Singapore. Association for Computa-
tional Linguistics.
Florian Le Bronnec, Alexandre Verine, Benjamin
Negrevergne, Yann Chevaleyre, and Alexandre
Allauzen. 2024.
Exploring precision and re-
call to assess the quality and diversity of LLMs.
In Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics
(Volume 1: Long Papers), pages 11418–11441,
Bangkok, Thailand. Association for Computa-
tional Linguistics.
Weixin Liang, Yaohui Zhang, Zhengxuan Wu,
Haley Lepp, Wenlong Ji, Xuandong Zhao,
Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang,
Diyi Yang, Christopher Potts, Christopher D
Manning, and James Y. Zou. 2024. Mapping
the increasing use of LLMs in scientific papers.
In First Conference on Language Modeling.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,
Ruochen Xu, and Chenguang Zhu. 2023.
G-
eval: NLG evaluation using gpt-4 with better
human alignment. In Proceedings of the 2023
Conference on Empirical Methods in Natural
Language Processing, pages 2511–2522, Sin-
gapore. Association for Computational Linguis-
tics.
Jiaming Luo, Colin Cherry, and George Foster.
2024.
To diverge or not to diverge: A mor-
phosyntactic perspective on machine translation
vs human translation. Transactions of the Asso-
ciation for Computational Linguistics, 12:355–
371.
Joshua Maynez, Shashi Narayan, Bernd Bohnet,
and Ryan McDonald. 2020. On faithfulness and
factuality in abstractive summarization. In Pro-
ceedings of the 58th Annual Meeting of the As-
sociation for Computational Linguistics, pages
1906–1919, Online. Association for Computa-
tional Linguistics.
Danielle S McNamara, Scott A Crossley, and
Philip M McCarthy. 2010. Linguistic features
of writing quality.
Written communication,
27(1):57–86.
Stephen Merity, Caiming Xiong, James Bradbury,
and Richard Socher. 2017.
Pointer sentinel
mixture models.
In International Conference
on Learning Representations.
J.F. Miller. 1981. Assessing Language Production
in Children: Experimental Procedures. Assess-
ing communicative behavior. University Park
Press.
Vishakh Padmakumar and He He. 2024.
Does
writing with language models reduce content
diversity?
Krishna Pillutla, Swabha Swayamdipta, Rowan
Zellers, John Thickstun, Sean Welleck, Yejin
Choi, and Zaid Harchaoui. 2021. Mauve: Mea-
suring the gap between neural text and human
text using divergence frontiers.
In Advances
15
in Neural Information Processing Systems, vol-
ume 34, pages 4816–4828. Curran Associates,
Inc.
Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason
Bolton, and Christopher D. Manning. 2020.
Stanza: A python natural language processing
toolkit for many human languages. In Proceed-
ings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics: System
Demonstrations, pages 101–108, Online. Asso-
ciation for Computational Linguistics.
Rafael Rafailov, Archit Sharma, Eric Mitchell,
Christopher D Manning, Stefano Ermon, and
Chelsea Finn. 2023.
Direct preference opti-
mization: Your language model is secretly a re-
ward model. In Thirty-seventh Conference on
Neural Information Processing Systems.
Ricardo Rei, Craig Stewart, Ana C Farinha, and
Alon Lavie. 2020. COMET: A neural frame-
work for MT evaluation.
In Proceedings of
the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages
2685–2702, Online. Association for Computa-
tional Linguistics.
Nils
Reimers
and
Iryna
Gurevych.
2019.
Sentence-BERT:
Sentence
embeddings
us-
ing Siamese BERT-networks. In Proceedings
of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th
International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages
3982–3992, Hong Kong, China. Association
for Computational Linguistics.
Nils Reimers and Iryna Gurevych. 2020. Making
monolingual sentence embeddings multilingual
using knowledge distillation. In Proceedings of
the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages
4512–4525, Online. Association for Computa-
tional Linguistics.
Ananya B. Sai, Akash Kumar Mohankumar, Sid-
dhartha Arora, and Mitesh M. Khapra. 2020.
Improving dialog evaluation with a multi-
reference adversarial dataset and large scale
pretraining. Transactions of the Association for
Computational Linguistics, 8:810–827.
Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and
Alane Suhr. 2024. Quantifying language mod-
els’ sensitivity to spurious features in prompt
design or: How i learned to start worrying about
prompt formatting.
In The Twelfth Interna-
tional Conference on Learning Representations.
Chantal Shaib, Joe Barrow, Jiuding Sun, Alexa F.
Siu, Byron C. Wallace, and Ani Nenkova.
2024a. Standardizing the measurement of text
diversity: A tool and a comparative analysis of
scores.
Chantal Shaib, Yanai Elazar, Junyi Jessy Li, and
Byron C Wallace. 2024b. Detection and mea-
surement of syntactic templates in generated
text.
In Proceedings of the 2024 Conference
on Empirical Methods in Natural Language
Processing, pages 6416–6431, Miami, Florida,
USA. Association for Computational Linguis-
tics.
Nino
Shervashidze,
Pascal
Schweitzer,
Erik
Jan
van
Leeuwen,
Kurt
Mehlhorn,
and Karsten M. Borgwardt. 2011. Weisfeiler-
lehman graph kernels.
J. Mach. Learn. Res.,
12(null):2539–2561.
Giannis Siglidis, Giannis Nikolentzos, Stratis
Limnios, Christos Giatsidis, Konstantinos Skia-
nis, and Michalis Vazirgiannis. 2020. Grakel:
A graph kernel library in python.
Journal of
Machine Learning Research, 21(54):1–5.
Luca Soldaini, Rodney Kinney, Akshita Bha-
gia, Dustin Schwenk, David Atkinson, Rus-
sell Authur, Ben Bogin, Khyathi Chandu, Jen-
nifer Dumas, Yanai Elazar, Valentin Hofmann,
Ananya Jha, Sachin Kumar, Li Lucy, Xinxi
Lyu, Nathan Lambert, Ian Magnusson, Ja-
cob Morrison, Niklas Muennighoff, Aakanksha
Naik, Crystal Nam, Matthew Peters, Abhilasha
Ravichander, Kyle Richardson, Zejiang Shen,
Emma Strubell, Nishant Subramani, Oyvind
Tafjord, Evan Walsh, Luke Zettlemoyer, Noah
Smith, Hannaneh Hajishirzi, Iz Beltagy, Dirk
Groeneveld, Jesse Dodge, and Kyle Lo. 2024.
Dolma:
an open corpus of three trillion to-
kens for language model pretraining research.
In Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics
(Volume 1: Long Papers), pages 15725–15788,
Bangkok, Thailand. Association for Computa-
tional Linguistics.
16
Rafael Alberto Rivera Soto, Kailin Koch, Aleem
Khan, Barry Y. Chen, Marcus Bishop, and
Nicholas Andrews. 2024. Few-shot detection of
machine-generated text using style representa-
tions. In The Twelfth International Conference
on Learning Representations.
Katherine Stasaski and Marti Hearst. 2022. Se-
mantic diversity in dialogue with natural lan-
guage inference.
In Proceedings of the 2022
Conference of the North American Chapter of
the Association for Computational Linguistics:
Human Language Technologies, pages 85–98,
Seattle, United States. Association for Compu-
tational Linguistics.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya
Bhupatiraju, Léonard Hussenot, Thomas Mes-
nard, Bobak Shahriari, Alexandre Ramé, et al.
2024.
Gemma 2: Improving open language
models at a practical size.
arXiv preprint
arXiv:2408.00118.
Mildred C. Templin. 1957.
Certain Language
Skills in Children: Their Development and In-
terrelationships, ned - new edition edition, vol-
ume 26. University of Minnesota Press.
Guy Tevet and Jonathan Berant. 2021. Evaluating
the evaluation of diversity in natural language
generation. In Proceedings of the 16th Confer-
ence of the European Chapter of the Association
for Computational Linguistics: Main Volume,
pages 326–346, Online. Association for Com-
putational Linguistics.
Hugo Touvron, Louis Martin, Kevin Stone, Pe-
ter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal
Bhargava, Shruti Bhosale, et al. 2023. Llama
2: Open foundation and fine-tuned chat models.
arXiv preprint arXiv:2307.09288.
Adaku Uchendu, Jooyoung Lee, Hua Shen, Thai
Le, Dongwon Lee, et al. 2023.
Does human
collaboration enhance the accuracy of identify-
ing llm-generated deepfake texts? In Proceed-
ings of the AAAI Conference on Human Com-
putation and Crowdsourcing, volume 11, pages
163–174.
Jan Philip Wahle, Terry Ruas, Yang Xu, and Bela
Gipp. 2024.
Paraphrase types elicit prompt
engineering capabilities.
In Proceedings of
the 2024 Conference on Empirical Methods in
Natural Language Processing, pages 11004–
11033, Miami, Florida, USA. Association for
Computational Linguistics.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng
Ni, Abhranil Chandra, Shiguang Guo, Weiming
Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al.
2024. Mmlu-pro: A more robust and challeng-
ing multi-task language understanding bench-
mark. arXiv preprint arXiv:2406.01574.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu,
Chang Zhou,
Chengpeng Li,
Chengyuan Li, Dayiheng Liu, Fei Huang, et al.
2024. Qwen2 technical report. arXiv preprint
arXiv:2407.10671.
Denis Yarats and Mike Lewis. 2018. Hierarchical
text generation and planning for strategic dia-
logue. In Proceedings of the 35th International
Conference on Machine Learning, volume 80
of Proceedings of Machine Learning Research,
pages 5591–5599. PMLR.
Hugh Zhang, Daniel Duckworth, Daphne Ippolito,
and Arvind Neelakantan. 2021. Trading off di-
versity and quality in natural language genera-
tion. In Proceedings of the Workshop on Hu-
man Evaluation of NLP Systems (HumEval),
pages 25–33, Online. Association for Compu-
tational Linguistics.
Susan Zhang, Stephen Roller, Naman Goyal,
Mikel Artetxe, Moya Chen, Shuohui Chen,
Christopher Dewan, Mona Diab, Xian Li,
Xi Victoria Lin, Todor Mihaylov, Myle Ott,
Sam Shleifer, Kurt Shuster, Daniel Simig,
Punit Singh Koura, Anjali Sridhar, Tianlu
Wang, and Luke Zettlemoyer. 2022. Opt: Open
pre-trained transformer language models.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kil-
ian Q. Weinberger, and Yoav Artzi. 2020.
Bertscore: Evaluating text generation with bert.
In International Conference on Learning Rep-
resentations.
Zhexin Zhang, Leqi Lei, Lindong Wu, Rui Sun,
Yongkang Huang, Chong Long, Xiao Liu, Xu-
anyu Lei, Jie Tang, and Minlie Huang. 2024.
SafetyBench: Evaluating the safety of large lan-
guage models. In Proceedings of the 62nd An-
17
nual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers),
pages 15537–15553, Bangkok, Thailand. Asso-
ciation for Computational Linguistics.
18
A
Comparison of Benchmarked LLMs
Llama-3.1-8B
Mistral-NeMo-12B
Qwen2.5-7B
Gemma-2-9b
Falcon-7b
OLMo-7B
Organization
Meta
Mistral
Alibaba
Google
TII
Ai2
Country
USA
France
China
USA
UAE
USA
Open weights
yes
yes
yes
yes
yes
yes
Open data
no
no
no
no
partially
yes
Tokenization
BPE (Tiktoken)
BPE (Tiktoken)
BPE
SentencePiece
BPE
BPE
Vocabulary size
128K
128K
151K
256K
65K
50K
#tokens
15T
unknown
18T
8T
1.5T
2.7T
Data filter
quality,
privacy, safety
unknown
quality
quality,
privacy, safety
quality
quality,
privacy, safety
Synthetic data
post-training
unknown
pre/post-training
post-training
unknown
post-training
Multilinguality
yes
yes
yes
(over 29 languages) not in particular
yes
(Latin alphabet)
no
Alignment
rejection sampling,
SFT, DPO
SFT
SFT, DPO
SFT, PPO
SFT
SFT, DPO
Release date
July 2024
July 2024
September 2024
June 2024
May 2023
February 2024
Table 4: Comparison of benchmarked LLMs.
We provide a comprehensive comparison of the LLMs included in our benchmark in Table 4, high-
lighting several key characteristics relevant to their design, development, and deployment.
B
Detailed Results of Linguistic Diversity Benchmarking
Human
Input
Qwen2.5
Mistral-Nemo
OLMo
Falcon
Llama-3.1
Gemma-2
LM
67.08
66.92
55.52
60.82
60.45
58.63
58.62
63.12
MT
61.18
61.83
59.07
59.38
57.19
57.51
58.36
58.40
Summ
58.98
62.76
63.90
65.56
63.51
61.81
62.23
62.30
NUG
40.25
50.27
50.53
48.32
50.00
40.68
46.69
45.45
Lexical
Diversity
ASG
59.04
41.19
55.95
56.90
52.46
52.94
52.28
56.24
LM
59.31
58.45
67.39
63.57
59.26
63.85
68.22
58.83
MT
56.43
43.47
49.42
48.71
57.72
56.66
47.67
48.62
Summ
46.27
54.52
34.10
38.27
50.50
56.87
33.88
39.52
NUG
72.03
68.39
65.63
69.76
65.63
68.80
60.21
69.87
Syntactic
Diversity
ASG
65.35
59.86
55.47
58.12
53.76
52.58
55.62
57.58
LM
47.14
47.14
45.34
47.57
47.66
47.40
41.90
47.62
MT
42.49
33.58
42.72
42.71
42.24
44.01
42.55
42.57
Summ
47.33
46.15
46.20
46.22
45.69
43.93
46.31
46.71
NUG
44.38
45.68
45.98
45.46
45.74
45.25
46.69
45.65
Semantic
Diversity
ASG
44.90
44.15
43.19
43.01
42.71
43.91
42.32
41.90
Table 5: Linguistic diversity benchmarking results for NLG tasks detailed in Table 1. For each type of
diversity, the highest model score for each task is highlighted in bold.
We present the detailed results of our linguistic diversity benchmarking experiments in Table 5. These
results are also visualized in Figure 1.
19
