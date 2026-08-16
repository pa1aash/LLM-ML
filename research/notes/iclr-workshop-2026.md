---
title: ICLR Workshop 2026
id: iclr-workshop-2026
tags:
- llm-nas-feedback-positioning-7125b1
- venue-cfp
- negative-results
created: '2026-08-16T15:48:16.347925Z'
updated: '2026-08-16T15:51:06.915534Z'
source: https://sites.google.com/view/icbinb-2026
source_domain: sites.google.com
fetched_at: '2026-08-16T15:48:16.345784Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'ICBINB (''I Can''t Believe It''s Not Better: Where Large Language Models
  Need to Improve'') 2026 edition is a workshop AT ICLR 2026 in Rio de Janeiro, Brazil
  — NOT a NeurIPS workshop. In-person session held April 26th/27th 2026 (already past
  as of this fetch), Room 201C. Explicitly part of the broader ICBINB initiative (''there
  is more to machine learning research than tables with bold numbers''; prior editions
  themed ''ideas motivated by beauty'' and ''gaps between theory and practice in probabilistic
  ML''), which also runs a monthly seminar series. Scope solicits (a) work explicitly
  showcasing an LLM limitation and (b) work that attempted a promising fix but fell
  short (negative results), across reasoning, alignment, agents, efficiency/scaling,
  and hallucination topics. States plainly: ''current publication mechanism tends
  to prioritize positive over negative results'' and frames the workshop as a corrective
  venue. Because the 2026 edition is calendared to ICLR (not NeurIPS) and its submission
  deadline (per companion CFP page) has already elapsed relative to today''s date,
  this specific workshop instance is NOT a live NeurIPS 2026 submission target — any
  positioning argument for this venue would need to reference a hypothetical/future
  NeurIPS-affiliated ICBINB edition or track historical rotation across venues, not
  this page.'
---

ICLR Workshop 2026
Search this site
Embedded Files
Skip to main content
Skip to navigation
I Can't Believe It's Not Better:
Where Large Language Models Need to Improve
Current LLMs still fall short in surprising ways.
Let’s face those gaps, learn from failures, and move the field forward together!
Key Dates
Paper S
ubmission
Deadline:
January 31st, 2026
(Check
Call For Papers
)
Review Period
:
February 3th,
202
6
-
February 25th, 2026
Paper Acceptance Notification:
March 1st, 2026
Camera Ready:
March 8th, 2026
Poster Submission:
April
16
th, 2026
In-Person Workshop:
April 2
7
th
, 2026, at Room 201C
The specified due dates are set for 11:59 pm AOE (Anywhere on Earth).
The success of Large Language Models (LLMs) has reshaped natural language processing and, increasingly, machine learning at large. Trained on vast amounts of data, they are able to achieve impressive performances on tasks such as translation [1], multimodal understanding [2–5], reasoning [6–8], and increasingly open-ended and self-evolving agentic behaviors [9–11] that empower applications across many domains, such as tool use and code agents [12–15] or scientific discovery [16, 17]. In some cases, these performances can even match or surpass those of humans [18, 19].
But at the same time, it’s becoming increasingly clear that LLMs are not infallible. Recent studies have shown limitations and even risks associated with their deployment in critical settings, such as clinical decision-making [20], biosecurity [21] and factual knowledge assessment [22]. Furthermore, it is well-known that LLMs can hallucinate [23, 24], and the mechanisms behind these inaccuracies remain an active area of research [25]. Additionally, LLM alignment remains brittle in the face of shifting goals and adversarial prompting [26–30], while new benchmarks question their reasoning capabilities and show limitations thereof [31, 32].
Ideally, findings about such limitations can be used to immediately improve LLMs and their capabilities, but this might not always be possible, due to computational limitations of academic researchers or because the approaches taken might not have been fruitful. In that case, it is hard to share the found insights about the limitations of LLMs (or failed attempts in resolving them) since the current publication mechanism tends to prioritize positive over negative results. However, sharing and discussing limitations of LLMs and failed attempts to resolve them can be valuable for the community to find a way to ultimately overcome these limitations.
We propose to organise this workshop as a platform to investigate important limitations of current LLMs both through works that
explicitly showcase a limitation
(as the ones cited above), as well as through works that
aim to overcome such current limitations through a promising approach but struggled to do so
(negative results).
We invite papers that focus on the negative results, which may include, but are not limited to,
Reasoning
(Work that surfaces brittle logic, shallow chains of thought, or domain-specific reasoning limitations)
Alignment
(Misalignment between user intent and model behavior, or failures in safety tuning and adversarial robustness)
Agents
(Challenges in multi-step planning, tool use, memory, or self-reflection within agentic systems)
Efficiency and scaling
(Limitations in training, inference, and fine-tuning LLMs under real-world compute constraints, with particular emphasis on high energy consumption and sustainability challenges)
Hallucinations
(Studies of factual inaccuracies, phantom citations, or trust calibration).
Additionally, we welcome any well-supported finding that challenges prevailing assumptions or exposes key limitations of LLMs.
I Can't Believe It's Not Better Initiative
This workshop forms one workshop in a series as part of the larger
I Can't Believe It's Not Better (ICBINB)
activities. We are a diverse group of researchers promoting the idea that there is more to machine learning research than tables with bold numbers. We believe that understanding in machine learning can come through more routes than iteratively improving upon previous methods and as such this workshop aims to focus on understanding through negative results. Previous workshops have focused on
ideas motivated by beauty
and
gaps
between theory and practice in probabilistic ML
, we also run a
monthly seminar series
aiming to crack open the research process and showcase what goes on behind the curtain. Read more about our activities and our members
here
.
Accessibility and Contact
ICBINB aims to foster an inclusive and welcoming community. If you have any questions, comments, or concerns, please
contact us at:
cant.believe.it.is.not.better@gmail.com
Whilst we will have a range of fantastic speakers appearing in person at the workshop we understand that many people are not able to travel to ICLR at this moment in time. It is our aim to make this workshop accessible to all, all talks will be viewable remotely.
References
[1] Joint speech and text machine translation for up to 100 languages. Nature, 637(8046):587–593, 2025.
[2] Gemini Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530, 2024. URL https://arxiv.org/abs/2403.05530.
[3] Shuai Bai et al. Qwen2.5-vl technical report. arXiv preprint arXiv:2502.13923, 2025. URL https://arxiv.org/abs/2502.13923.
[4] Bo Li et al. LLaVA-onevision: Easy visual task transfer. arXiv preprint arXiv:2408.03326,2024. URL https://arxiv.org/abs/2408.03326.
[5] OpenAI. GPT-4v(ision) system card. https://openai.com/index/gpt-4v-system-card/, September 2023. System card describing the deployment and evaluation of GPT-4 with vision.
[6] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35:24824–24837, 2022.
[7] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. Advances in neural information processing systems, 36:11809–11822, 2023.
[8] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In International Conference
on Learning Representations (ICLR), 2023.
[9] Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. Darwin godel machine: Open-ended evolution of self-improving agents. arXiv preprint arXiv:2505.22954, 2025.
[10] Jiahao Qiu, Xuan Qi, Tongcheng Zhang, Xinzhe Juan, Jiacheng Guo, Yifu Lu, Yimin Wang, Zixin Yao, Qihan Ren, Xun Jiang, et al. Alita: Generalist agent enabling scalable agentic reasoning with minimal predefinition and maximal self-evolution. arXiv preprint arXiv:2505.20286, 2025.
[11] Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, et al. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046, 2025.
[12] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, et al. Toolllm: Facilitating large language models to master 16000+ real-world apis. arXiv preprint arXiv:2307.16789, 2023.
[13] Niels Mündler, Mark Müller, Jingxuan He, and Martin Vechev. Swt-bench: Testing and validating real-world bug-fixes with code agents. Advances in Neural Information Processing Systems, 37:81857–81887, 2024.
[14] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. Executable code actions elicit better llm agents. In Forty-first International Conference on Machine Learning, 2024.
[15] Hongru Wang, Cheng Qian, Manling Li, Jiahao Qiu, Boyang Xue, Mengdi Wang, Heng Ji, and Kam-Fai Wong. Toward a theory of agents as tool-use decision-makers. arXiv preprint arXiv:2506.00886, 2025.
[16] Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong. Stella: Self-evolving llm agent for biomedical research. arXiv preprint arXiv:2507.02004, 2025.
[17] Pingchuan Ma, Tsun-Hsuan Wang, Minghao Guo, Zhiqing Sun, Joshua B Tenenbaum, Daniela Rus, Chuang Gan, and Wojciech Matusik. Llm and simulation as bilevel optimizers: A new paradigm to advance physical scientific discovery. arXiv preprint arXiv:2405.09783, 2024.
[18] Jiahao Qiu, Jingzhe Shi, Xinzhe Juan, Zelin Zhao, Jiayi Geng, Shilong Liu, Hongru Wang, Sanfeng Wu, and Mengdi Wang. Physics supernova: Ai agent matches elite gold medalists at ipho 2025. arXiv preprint arXiv:2509.01659, 2025.
[19] Xiaoliang Luo, Akilles Rechardt, Guangzhi Sun, Kevin K Nejad, Felipe Yáñez, Bati Yilmaz, Kangjoo Lee, Alexandra O Cohen, Valentina Borghesani, Anton Pashkov, et al. Large language models surpass human experts in predicting neuroscience results. Nature human behaviour, 9 (2):305–315, 2025.
[20] Paul Hager, Friederike Jungmann, Robbie Holland, Kunal Bhagat, Inga Hubrecht, Manuel Knauer, Jakob Vielhauer, Marcus Makowski, Rickmer Braren, Georgios Kaissis, et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature medicine, 30(9):2613–2622, 2024.
[21] Zaixi Zhang, Zhenghong Zhou, Ruofan Jin, Le Cong, and Mengdi Wang. Genebreaker: Jailbreak attacks against dna language models with pathogenicity guidance. arXiv preprint arXiv:2505.23839, 2025.
[22] Lexin Zhou, Wout Schellaert, Fernando Martínez-Plumed, Yael Moros-Daval, Cèsar Ferri, and José Hernández-Orallo. Larger and more instructable language models become less reliable. Nature, 634(8032):61–68, 2024.
[23] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Yulong Chen, et al. Siren’s song in the ai ocean: A survey on hallucination in large language models. Computational Linguistics, pages 1–46, 2025.
[24] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al. A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. ACM Transactions on Information Systems, 43(2):1–55, 2025.
[25] Adam Tauman Kalai, Ofir Nachum, Santosh S Vempala, and Edwin Zhang. Why language models hallucinate. arXiv preprint arXiv:2509.04664, 2025.
[26] Anthropic-Team. Agentic misalignment: How LLMs could be an insider threat. https:// www.anthropic.com/research/agentic-misalignment, June 2025. Anthropic Research.
[27] Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, and Peter Henderson. Safety alignment should be made more than just a few tokens deep. In The Thirteenth International Conference on Learning Representations, 2025.
[28] Maksym Andriushchenko, Francesco Croce, and Nicolas Flammarion. Jailbreaking leading safety-aligned llms with simple adaptive attacks. In The Thirteenth International Conference on Learning Representations, 2025.
[29] Yotam Wolf, Noam Wies, Oshri Avnery, Yoav Levine, and Amnon Shashua. Fundamental limitations of alignment in large language models. In Proceedings of the 41st International Conference on Machine Learning, pages 53079–53112, 2024.
[30] U Anwar, A Saparov, J Rando, D Paleka, M Turpin, P Hase, ES Lubana, E Jenner, S Casper, O Sourbut, et al. Foundational challenges in assuring alignment and safety of large language models. Transactions on Machine Learning Research, 2024.
[31] Parshin Shojaee, Iman Mirzadeh, Keivan Alizadeh, Maxwell Horton, Samy Bengio, and Mehrdad Farajtabar. The illusion of thinking: Understanding the strengths and limitations of reasoning models via the lens of problem complexity. arXiv preprint arXiv:2506.06941, 2025.
[32] Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar. Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models. arXiv preprint arXiv:2410.05229, 2024.
Google Sites
Report abuse
Page details
Page updated
Google Sites
Report abuse