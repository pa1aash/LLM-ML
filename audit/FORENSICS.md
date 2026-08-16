# FORENSICS — five targeted questions

S0 ground-truth audit. Every answer is sourced to `file:line` in the repository.
Where the repository cannot answer, the answer is "cannot determine", with the
reason.

---

## F1 — Generation configuration

**Verdict: thinking mode was suppressed by configuration. The paper's "zero
causal attributions" result is a property of the harness, not of the model.**

| Setting | Value | Evidence |
|---|---|---|
| Chat template | `tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)` | [llm_server_small.py:41](../src/llm_server_small.py#L41) |
| **Thinking mode** | **`enable_thinking=False`** | [llm_server_small.py:43](../src/llm_server_small.py#L43), [llm_server.py:46](../src/llm_server.py#L46) |
| `max_new_tokens` | `max_tokens`, default 2048 | [llm_server_small.py:39,48](../src/llm_server_small.py#L39) |
| Sampling | `temperature=max(T,0.01)`, `do_sample=T>0`, `top_p=0.9` | [llm_server_small.py:49-50](../src/llm_server_small.py#L49) |
| Messages sent | `[system, user]` only — no assistant turns | [run_v2.py:37-40](../src/run_v2.py#L37) |

`llm_server.py:46` carries the comment `# Disable thinking for faster/cleaner
output`. So the suppression was deliberate.

### Three ways output could be silently lost or altered

1. **Truncation is invisible.** The server hardcodes
   `"finish_reason": "stop"` on every response
   ([llm_server_small.py:54](../src/llm_server_small.py#L54)). A generation that
   ran into the 2048-token cap is reported as a clean stop. Nothing downstream
   can distinguish the two.

2. **Transcripts are truncated to 2000 characters before storage.** Every
   storage path writes `response[:2000]`
   ([run_v2.py:187](../src/run_v2.py#L187), [191](../src/run_v2.py#L191),
   [194](../src/run_v2.py#L194), [254](../src/run_v2.py#L254),
   [258](../src/run_v2.py#L258), [261](../src/run_v2.py#L261)). The transcript
   analysis therefore reads at most the first 2000 characters
   ([deep_analysis_v2.py:160](../src/deep_analysis_v2.py#L160)).

3. **Malformed output is silently rewritten, not discarded.** `sanitize_config`
   coerces any out-of-vocabulary field to `valid_vals[0]`
   ([run_v2.py:52-67](../src/run_v2.py#L52)) — see F2, which is where this
   matters most.

Generation exceptions and parse failures are recorded as invalid rather than
dropped ([run_v2.py:187](../src/run_v2.py#L187),
[197](../src/run_v2.py#L197)), so failures are counted, not hidden.

### Consequence for the paper's claim

The paper reports zero causal attributions across all 60 transcripts
(`tab_transcript.tex`) and interprets it as evidence that "the LLM may lack the
causal reasoning capacity to translate performance metrics into actionable
modifications" ([main.tex:718](../paper/main.tex#L718)). Limitation (iv) attributes
it to "the small model's minimal text output" ([main.tex:766](../paper/main.tex#L766)).

Neither framing discloses that reasoning was **disabled at the chat-template
level** and that stored transcripts were **truncated to 2000 characters**. The
measurement cannot distinguish "the model cannot reason causally" from "the model
was configured not to emit reasoning." As written, the claim is not supported.

---

## F2 — The identical-design check

**Verdict: cannot be performed. The condition-B specifications do not exist in
this repository.** What can be established is stronger than it looks.

### The specs are gone

`run_v2.py` would have written the 20 configs to
`results_v2/B_{dataset}_s{seed}/results.json`
([run_v2.py:308-310](../src/run_v2.py#L308), [438](../src/run_v2.py#L438)). No
such file exists anywhere in the tree or in either archive zip. Field-by-field
byte comparison is therefore impossible.

### The Jaccard function, and what 0.022 implies

```python
def arch_signature(config):           # deep_analysis_v2.py:111
    sig = set()
    for i, block in enumerate(config.get("blocks", [])):
        for k, v in block.items():
            sig.add((i, k, str(v)))   # (block_index, field, value)
    sig.add(("head", "global_pool", config.get("global_pool", "")))
    sig.add(("head", "fc_layers", str(config.get("fc_layers", ""))))
    return sig

def mean_jaccard_distance(configs):   # deep_analysis_v2.py:120
    ...  dists.append(1.0 - inter/union) ... return float(np.mean(dists))
```

The signature is a set of `(block_index, field, value)` triples plus two head
triples. Note `dropout` is **not** in the signature.

**Identical configurations produce identical signature sets, so
`inter == union`, so the distance is exactly 0.000.** The reported 0.022
(`tab_arch.tex`, [main.tex:531](../paper/main.tex#L531)) is therefore
*mathematically incompatible* with 20 byte-identical designs.

Quantitatively, with the paper's own K=4 blocks the signature has
4 × 6 + 2 = 26 elements. Two configs differing in exactly one field give
distance 2/27 = 0.0741. Over C(20,2) = 190 pairs, a mean of 0.022 implies a total
pairwise distance of ≈ 4.18 — which is matched almost exactly by **17 identical
designs plus 3 one-field variants** (51 × 0.0741 + 3 × 0.1429 = 4.21 → mean
0.0222). So the data are consistent with *approximately 17 of 20 identical*, not
20 of 20.

### Reconciling with "parameter std = 0K" — recovered from Figure 4

`fig4_design_heatmap.pdf` annotates every cell with its percentage
([deep_analysis_v2.py:290](../src/deep_analysis_v2.py#L290)), so those values
survive even though the underlying data does not. Extracted, condition B reads:

| Field | Condition B distribution |
|---|---|
| conv_type | Std **100**, DWSep 0, Dil 0, Bnk 0 |
| activation | relu **100**, gelu 0, silu 0, mish 0 |
| normalization | BN **100**, LN 0, GN 0, None 0 |
| **skip_connection** | **Id 50, Proj 50, None 0** |

The skip split is the key. In the builder, `identity` with matched channels costs
**zero** parameters while `projection` inserts a 1×1 conv costing `in_c × out_c`
([search_space.py:110-115](../src/search_space.py#L110)).

- If the 50/50 split were **across** architectures (some all-identity, some
  all-projection), parameter counts would differ substantially — contradicting
  `std = 0K`.
- Therefore the split must be **within** each architecture: every one of the 20
  carries the same *multiset* of skip choices (for K=4, two identity and two
  projection).

But identical multisets still give Jaccard 0 **only if the positions match**,
because `arch_signature` keys every triple by block index
([deep_analysis_v2.py:115](../src/deep_analysis_v2.py#L115)). Permuting which
blocks are identity vs projection — `[Id,Id,Proj,Proj]` vs `[Id,Proj,Id,Proj]` —
leaves the parameter count untouched (equal channel widths) while changing the
signature.

**The most parsimonious reading consistent with every surviving number is that
the 20 condition-B designs share one template and one parameter count, but differ
in the ordering of design choices across blocks.** That satisfies
`parameter std = 0K`, `Jaccard = 0.022`, `conv/act/norm = 100%`, and
`skip = 50/50` simultaneously. The magnitude of 0.022 corresponds to roughly 3 of
20 deviating by a single positional swap.

Under this reading the paper's Table 1, Table 4 and Figure 4 are all internally
consistent, and it is specifically the *prose* — "identical", "zero structural
variance", "the same skip-connection configuration" — that overstates them.

**This is a reconstruction, not a measurement.** Confirming it requires the specs.

### The smoking gun that must be ruled out

`sanitize_config` is applied to **every** parsed LLM configuration
([run_v2.py:77](../src/run_v2.py#L77), [89](../src/run_v2.py#L89)) and to **no**
random configuration. Any unrecognised categorical value is replaced by
`valid_vals[0]` ([run_v2.py:67](../src/run_v2.py#L67)):

| Field | `valid_vals[0]` — the silent default |
|---|---|
| `conv_type` | **`standard_3x3`** |
| `activation` | **`relu`** |
| `normalization` | **`batchnorm`** |
| `skip_connection` | `identity` |
| `pooling` | `maxpool` |

The paper's headline template is "standard 3×3 convolutions, ReLU, BatchNorm"
([abstract](../paper/main.tex#L52), [main.tex:560](../paper/main.tex#L560)).
**That is exactly the sanitiser's fallback triple.** A model emitting malformed
or out-of-vocabulary fields would be silently converted into precisely the
"narrow prior" the paper reports.

Because the sanitiser runs on the LLM arms only, the headline
diversity comparison (B: 0.022 vs A: 0.856) is between one arm that passes
through a value-collapsing normaliser and one that does not. This is a
confound in the paper's central measurement, and the stored artifacts cannot
distinguish the two explanations. Resolving it requires re-running condition B
with the raw pre-sanitisation output logged.

---

## F3 — Independence

**Verdict: condition B is independent by construction; C and D are not, and the
tests applied assume independence for all of them.**

### Condition B — fresh context, but not seed-controlled

Each iteration issues a single stateless call with only
`[system_prompt, user_prompt]`; no history is threaded
([run_v2.py:184](../src/run_v2.py#L184)). The prompts differ **only** by the
architecture index: `f"Design architecture #{i+1}. Maximize test accuracy within
5M params. Return only JSON."` ([run_v2.py:182](../src/run_v2.py#L182)).

So contexts are genuinely fresh. But: **there is no RNG control over LLM
sampling anywhere.** The server never seeds `torch` before `generate`, and it
runs in a separate process from the trainer's `torch.manual_seed`. The 20 draws
are independent, but not reproducible — and 20 near-identical prompts to a
4-bit-quantised 1.7B model at T=0.7 is exactly the regime where mode collapse is
expected. That is a rival explanation the design cannot separate from a
"strong prior."

### Conditions C and D — accumulated history, single stream

`history` accumulates across iterations and is serialised into each user prompt
([run_v2.py:205](../src/run_v2.py#L205), [219-248](../src/run_v2.py#L219)).
Architecture *i+1* is conditioned on the measured outcomes of architectures
1…*i*. Note this is **not** a multi-turn conversation — each call still sends
only `[system, user]`, with the history flattened into the user text. The
dependence is real regardless.

**The 20 accuracies within condition C, and within condition D, are not
independent observations.**

### What the tests assume

| Test | Location | Assumption |
|---|---|---|
| Welch's *t* | [deep_analysis_v2.py:98](../src/deep_analysis_v2.py#L98) | independent observations within each group |
| Mann–Whitney *U* | [deep_analysis_v2.py:99](../src/deep_analysis_v2.py#L99) | independent observations within each group |
| Bootstrap CI on *d* | [deep_analysis_v2.py:86-93](../src/deep_analysis_v2.py#L86) | i.i.d. resampling within each group |

All three treat *n*=20 as 20 independent units. For A, A2, B and E that is
defensible. **For C and D it is false**, and the affected comparisons are exactly
the ones carrying the paper's thesis (B vs C, B vs D). The bootstrap compounds
it: resampling a sequentially-generated trajectory with replacement does not
reproduce its dependence structure, so the CIs on *d* are too narrow.

The correct estimand under a fixed search budget is expected-best-of-*k*, not the
mean of a dependent sequence. See `CLAIM_TRACE.md` §4.

---

## F4 — Selection hygiene

**Verdict: the feedback loop is clean. Test accuracy enters selection in the
top-5 retraining path, and enters the convergence figure.**

### Where the test split is constructed

`get_cifar_loaders` builds train/val by `random_split` seeded with `seed`, and
uses the untouched CIFAR test split for `test_loader`
([train_arch.py:37-51](../src/train_arch.py#L37)). Test evaluation happens once
per architecture, after training ([train_arch.py:137-150](../src/train_arch.py#L137)).

**The split is not fixed across architectures.** `seed + i` varies per
architecture, so the 90/10 train/val boundary moves for each one. It is balanced
across conditions (architecture *i* sees the same split in every condition), but
Algorithm 1 depicts a single split before the loop
([main.tex:329](../paper/main.tex#L329)), which is not what the code does. The
test set itself is fixed and never resampled.

### Feedback messages — clean

| Condition | Feedback field | Evidence |
|---|---|---|
| C (unstructured) | `best_val_acc` | [run_v2.py:222](../src/run_v2.py#L222) |
| D (structured) | `best_val_acc`, `final_train_acc`, `train_val_gap`, `param_count`, `total_time_s`, val curves | [run_v2.py:232](../src/run_v2.py#L232), [241](../src/run_v2.py#L241), [247](../src/run_v2.py#L247) |
| E (REA tournament) | `best_val_acc` | [run_v2.py:297](../src/run_v2.py#L297) |

**No test accuracy reaches any prompt.** The v2 no-leakage claim holds for the
feedback loop, as advertised.

### Two places test accuracy does enter

1. **Top-5 retraining selects on test accuracy.**
   ```python
   valid.sort(key=lambda x: x["test_acc"], reverse=True)   # run_v2.py:340
   top5 = valid[:5]
   ```
   The architectures retrained across seeds {42, 137, 256} are the ones that
   scored highest **on the test set**. Any mean/std reported from that path is
   conditioned on test-set ranking and is optimistically biased. This sits inside
   the v2 "reviewer fixes."

2. **The convergence figure plots best-so-far *test* accuracy.**
   ```python
   best = max(best, r["test_acc"])                          # deep_analysis_v2.py:235
   ```
   Figure 2 ([main.tex:508](../paper/main.tex#L508)) is captioned "Best-so-far
   test accuracy," so it is not concealed — but it means the convergence evidence
   for H2 is a test-set trajectory, while the search itself ran on validation.

Neither contaminates the search. Both should be disclosed.

---

## F5 — Effect sizes and metrics

### Where each metric lives

| Metric | Location | Definition used |
|---|---|---|
| Cohen's *d* | [deep_analysis_v2.py:80](../src/deep_analysis_v2.py#L80) | **pooled**-SD denominator |
| Bootstrap CI | [deep_analysis_v2.py:73](../src/deep_analysis_v2.py#L73), [86](../src/deep_analysis_v2.py#L86) | percentile; 10 000 for means, **5 000** for *d* |
| Jaccard distance | [deep_analysis_v2.py:120](../src/deep_analysis_v2.py#L120) | mean pairwise 1 − \|∩\|/\|∪\| |
| Efficiency | [deep_analysis_v2.py:438](../src/deep_analysis_v2.py#L438) | `test_acc / (param_count/1e6)` |

### Cohen's *d* is not well defined here

```python
pooled = np.sqrt(((nx-1)*np.var(x,ddof=1) + (ny-1)*np.var(y,ddof=1)) / (nx+ny-2))
d = (np.mean(x) - np.mean(y)) / pooled
```

This is the **equal-variance** pooled estimator. The A-vs-B comparison it is
applied to has σ_A = 22.6 and σ_B = 0.7 — a variance ratio over 1000:1. The
pooled denominator evaluates to ≈ 16.0, essentially σ_A alone, so *d* = −0.71
describes the random arm's spread and is nearly insensitive to condition B.
Meanwhile Welch's *t* is computed with `equal_var=False`
([deep_analysis_v2.py:98](../src/deep_analysis_v2.py#L98)). **The paper reports a
Welch test and a pooled-SD effect size side by side**, which are contradictory
variance assumptions on the same comparison. Glass's Δ or a rank-based measure is
the appropriate choice.

Two further discrepancies:
- The paper states Cohen's *d* CIs use **10 000** resamples
  ([main.tex:311](../paper/main.tex#L311)); the code uses **5 000**
  ([deep_analysis_v2.py:80](../src/deep_analysis_v2.py#L80)).
- Bootstrapping *d* over C and D resamples dependent sequences (see F3).

### A rank-based alternative is available

**Mann–Whitney *U* is already computed and already reported** — `u_stat` and
`u_p` ([deep_analysis_v2.py:99](../src/deep_analysis_v2.py#L99),
[106](../src/deep_analysis_v2.py#L106)), printed as the `p_U` column.

Cliff's δ and A₁₂ are **not** implemented, but both are exact functions of the
stored *U* statistic:

```
A₁₂ = U / (n₁ · n₂)          Cliff's δ = 2·A₁₂ − 1
```

With n₁ = n₂ = 20 (n₁n₂ = 400), any reported *U* converts directly. **But `u_stat`
was never persisted** — `tab_stats.tex` stores only `u_p`, and `results.json` is
gone. So Cliff's δ is computable *in principle* from the design, and **not
computable from what survives**. It requires either re-running the analysis on
recovered data or re-running the experiment.

Given the 1000:1 variance ratio and the non-normal, bimodal random-search
distribution the paper itself describes ([main.tex:498](../paper/main.tex#L498)),
a rank-based effect size should be the headline, not pooled *d*.

### Efficiency

`accuracy / params_in_millions` is a ratio of an accuracy to a size, dominated by
the denominator. Condition D's "lowest efficiency (137)" is largely a restatement
of it having the most parameters (727 K). It carries little independent evidential
weight.
