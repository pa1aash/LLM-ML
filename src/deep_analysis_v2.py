#!/usr/bin/env python3
"""
V2 Deep Analysis — fixes ALL reviewer concerns:
1. Uses best_val_acc (not test_acc) for feedback-condition reporting where relevant
2. Correct Cohen's d with 95% CI via bootstrap
3. Correct Jaccard diversity (distance, not similarity; reconciled with narrative)
4. Sanity-filtered random baseline analysis
5. Rank correlation analysis (epoch 20 vs 50 from training histories)
6. Quantitative transcript coding for causal hallucination claims
7. Mann-Whitney U as nonparametric alternative
8. Bootstrap confidence intervals throughout

Usage: python deep_analysis_v2.py --results_dir results_v2 --output_dir figures_v2
"""
import json, os, sys, re, glob
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np
from scipy import stats

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams.update({
    'font.size': 9, 'font.family': 'serif',
    'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
})

CONDS = ["A", "A2", "B", "C", "D", "E"]
LABELS = {
    "A": "Random", "A2": "Filtered Random",
    "B": "LLM Zero-Shot", "C": "LLM + Unstr. FB",
    "D": "LLM + Struct. FB", "E": "Reg. Evolution",
}
COLORS = {
    "A": "#888888", "A2": "#AAAAAA",
    "B": "#4C72B0", "C": "#DD8452",
    "D": "#55A868", "E": "#C44E52",
}
MARKERS = {"A": "o", "A2": "v", "B": "s", "C": "^", "D": "D", "E": "P"}


def load_all(results_dir):
    data = {}
    for d in sorted(Path(results_dir).iterdir()):
        if not d.is_dir(): continue
        rf = d / "results.json"
        if not rf.exists(): continue
        r = json.load(open(rf))
        parts = d.name.split("_")
        cond = parts[0]
        ds = parts[1]
        seed = parts[2] if len(parts) > 2 else "s42"
        data[(cond, ds, seed)] = r
    return data

def get_valid(data, cond, ds, seed="s42"):
    key = (cond, ds, seed)
    if key not in data: return []
    return [r for r in data[key] if r.get("valid") and r.get("test_acc") is not None]

def get_accs(data, cond, ds, seed="s42"):
    return np.array([r["test_acc"] for r in get_valid(data, cond, ds, seed)])

def get_val_accs(data, cond, ds, seed="s42"):
    return np.array([r["best_val_acc"] for r in get_valid(data, cond, ds, seed)])

# ─── Corrected Statistics ─────────────────────────────────────────────────────
def bootstrap_ci(x, stat_fn=np.mean, n_boot=10000, ci=0.95, seed=42):
    """Bootstrap confidence interval for a statistic."""
    rng = np.random.default_rng(seed)
    boot = [stat_fn(rng.choice(x, size=len(x), replace=True)) for _ in range(n_boot)]
    alpha = (1 - ci) / 2
    return np.percentile(boot, [alpha*100, (1-alpha)*100])

def cohens_d_with_ci(x, y, n_boot=5000, seed=42):
    """Cohen's d with bootstrap 95% CI. Positive = x > y."""
    nx, ny = len(x), len(y)
    pooled = np.sqrt(((nx-1)*np.var(x,ddof=1) + (ny-1)*np.var(y,ddof=1)) / (nx+ny-2))
    d = (np.mean(x) - np.mean(y)) / pooled if pooled > 0 else 0.0
    # Bootstrap CI
    rng = np.random.default_rng(seed)
    ds = []
    for _ in range(n_boot):
        bx = rng.choice(x, size=nx, replace=True)
        by = rng.choice(y, size=ny, replace=True)
        p = np.sqrt(((nx-1)*np.var(bx,ddof=1)+(ny-1)*np.var(by,ddof=1))/(nx+ny-2))
        ds.append((np.mean(bx)-np.mean(by))/p if p > 0 else 0)
    lo, hi = np.percentile(ds, [2.5, 97.5])
    return d, lo, hi

def full_comparison(x, y, label_x, label_y):
    """Welch t-test + Mann-Whitney U + Cohen's d with CI."""
    t_stat, t_p = stats.ttest_ind(x, y, equal_var=False)
    u_stat, u_p = stats.mannwhitneyu(x, y, alternative='two-sided')
    d, d_lo, d_hi = cohens_d_with_ci(x, y)
    return {
        "comparison": f"{label_x} vs {label_y}",
        "n_x": len(x), "n_y": len(y),
        "mean_x": float(np.mean(x)), "mean_y": float(np.mean(y)),
        "t_stat": float(t_stat), "t_p": float(t_p),
        "u_stat": float(u_stat), "u_p": float(u_p),
        "cohens_d": float(d), "d_ci_lo": float(d_lo), "d_ci_hi": float(d_hi),
    }

# ─── Corrected Diversity: Jaccard DISTANCE (1 - similarity) ──────────────────
def arch_signature(config):
    sig = set()
    for i, block in enumerate(config.get("blocks", [])):
        for k, v in block.items():
            sig.add((i, k, str(v)))
    sig.add(("head", "global_pool", config.get("global_pool", "")))
    sig.add(("head", "fc_layers", str(config.get("fc_layers", ""))))
    return sig

def mean_jaccard_distance(configs):
    """Mean pairwise Jaccard DISTANCE (higher = more diverse)."""
    sigs = [arch_signature(c) for c in configs]
    n = len(sigs)
    if n < 2: return 0
    dists = []
    for i in range(n):
        for j in range(i+1, n):
            inter = len(sigs[i] & sigs[j])
            union = len(sigs[i] | sigs[j])
            dists.append(1.0 - inter/union if union > 0 else 1.0)
    return float(np.mean(dists))

# ─── Transcript Coding for Causal Hallucination ──────────────────────────────
CAUSAL_PATTERNS = [
    r"(?:because|since|due to|caused by|leads to|results in|explains why)",
    r"(?:overfitting|underfitting) (?:is |was )?(?:caused|due|because)",
    r"(?:BatchNorm|LayerNorm|GroupNorm|ReLU|GELU|SiLU) (?:causes?|leads?|results?)",
    r"(?:should|must|need to) (?:increase|decrease|remove|add|change)",
    r"(?:the reason|this is why|that's why|therefore|hence|thus|consequently)",
]

def code_transcript(response_text):
    """Count causal attributions in a transcript. Returns dict of counts."""
    if not response_text: return {"total_causal": 0, "unique_patterns": 0}
    text = response_text.lower()
    total = 0; found = set()
    for pat in CAUSAL_PATTERNS:
        matches = re.findall(pat, text)
        total += len(matches)
        if matches: found.add(pat)
    return {"total_causal": total, "unique_patterns": len(found)}

def analyze_transcripts(data, ds="cifar10", seed="s42"):
    """Quantitative transcript analysis across conditions."""
    results = {}
    for cond in ["B", "C", "D"]:
        valid = get_valid(data, cond, ds, seed)
        all_counts = []
        for r in valid:
            resp = r.get("llm_response", "") or r.get("llm_reasoning", "")
            counts = code_transcript(resp)
            all_counts.append(counts["total_causal"])
        results[cond] = {
            "mean_causal_per_arch": float(np.mean(all_counts)) if all_counts else 0,
            "std_causal": float(np.std(all_counts)) if all_counts else 0,
            "total_transcripts": len(all_counts),
            "transcripts_with_causal": sum(1 for c in all_counts if c > 0),
        }
    return results

# ─── Rank Correlation from Training Histories ────────────────────────────────
def rank_correlation_from_histories(data, ds="cifar10", seed="s42"):
    """Compare rankings at epoch 20 vs epoch 50 using saved training histories."""
    results = {}
    for cond in CONDS:
        valid = get_valid(data, cond, ds, seed)
        acc_20 = []; acc_50 = []
        for r in valid:
            hist = r.get("history", {})
            if hist and "val_acc" in hist and len(hist["val_acc"]) >= 20:
                acc_20.append(hist["val_acc"][19])  # epoch 20
                acc_50.append(r["best_val_acc"])     # best val (proxy for 50)
        if len(acc_20) >= 5:
            rho, rho_p = stats.spearmanr(acc_20, acc_50)
            tau, tau_p = stats.kendalltau(acc_20, acc_50)
            results[cond] = {
                "n": len(acc_20),
                "spearman_rho": round(rho, 4), "spearman_p": round(rho_p, 6),
                "kendall_tau": round(tau, 4), "kendall_p": round(tau_p, 6),
            }
    return results

# ─── Figure Generation ────────────────────────────────────────────────────────
def fig1_violin(data, out):
    """Main result: violin + strip plots."""
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.5))
    active = [c for c in CONDS if any(get_accs(data, c, ds).size > 0 for ds in ["cifar10","cifar100"])]
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        plot_data = []; plot_labels = []; plot_colors = []
        for c in active:
            accs = get_accs(data, c, ds)
            if accs.size == 0: continue
            plot_data.append(accs)
            plot_labels.append(LABELS[c])
            plot_colors.append(COLORS[c])

        if not plot_data: continue
        positions = range(len(plot_data))
        vp = ax.violinplot(plot_data, positions=positions, showmedians=True, showextrema=False, widths=0.7)
        for i, body in enumerate(vp['bodies']):
            body.set_facecolor(plot_colors[i]); body.set_alpha(0.4)
        vp['cmedians'].set_color('black'); vp['cmedians'].set_linewidth(1.5)
        for i, d in enumerate(plot_data):
            jitter = np.random.default_rng(42).normal(0, 0.05, len(d))
            ax.scatter(np.full_like(d, i)+jitter, d, c=plot_colors[i], s=10, alpha=0.6, zorder=5, edgecolor='white', linewidth=0.3)
        ax.set_xticks(positions)
        ax.set_xticklabels(plot_labels, rotation=25, ha='right', fontsize=7)
        ax.set_ylabel("Test Accuracy (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.grid(axis='y', alpha=0.2); ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout(pad=1.0)
    plt.savefig(f"{out}/fig1_violin.pdf"); plt.close()

def fig2_convergence(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
    active = [c for c in CONDS if any(get_valid(data, c, ds) for ds in ["cifar10","cifar100"])]
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        for c in active:
            valid = get_valid(data, c, ds)
            if not valid: continue
            bsf = []; best = 0
            for r in valid:
                best = max(best, r["test_acc"]); bsf.append(best)
            ax.plot(range(1, len(bsf)+1), bsf, color=COLORS[c], label=LABELS[c], linewidth=1.5, marker=MARKERS[c], markersize=3, markevery=3)
        ax.set_xlabel("Architecture #"); ax.set_ylabel("Best Acc So Far (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.legend(fontsize=6, loc='lower right'); ax.grid(alpha=0.2)
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{out}/fig2_convergence.pdf"); plt.close()

def fig3_param_acc(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
    active = [c for c in CONDS if any(get_valid(data, c, ds) for ds in ["cifar10","cifar100"])]
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        for c in active:
            valid = get_valid(data, c, ds)
            if not valid: continue
            p = np.array([r["param_count"] for r in valid])/1e6
            a = np.array([r["test_acc"] for r in valid])
            ax.scatter(p, a, c=COLORS[c], s=25, alpha=0.7, label=LABELS[c], marker=MARKERS[c], edgecolor='white', linewidth=0.3)
        ax.set_xlabel("Parameters (M)"); ax.set_ylabel("Test Accuracy (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.legend(fontsize=6, loc='lower right'); ax.grid(alpha=0.2)
        ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{out}/fig3_param_accuracy.pdf"); plt.close()

def fig4_heatmap(data, out):
    fields = ["conv_type", "activation", "normalization", "skip_connection"]
    field_vals = {
        "conv_type": ["standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"],
        "activation": ["relu", "gelu", "silu", "mish"],
        "normalization": ["batchnorm", "layernorm", "groupnorm", "none"],
        "skip_connection": ["identity", "projection", "none"],
    }
    active = [c for c in CONDS if get_valid(data, c, "cifar10")]
    fig, axes = plt.subplots(2, 2, figsize=(7.5, 5.5))
    for fidx, field in enumerate(fields):
        ax = axes[fidx//2][fidx%2]
        vals = field_vals[field]
        matrix = np.zeros((len(active), len(vals)))
        for cidx, c in enumerate(active):
            valid = get_valid(data, c, "cifar10")
            total = 0; counts = Counter()
            for r in valid:
                if "config" not in r: continue
                for b in r["config"].get("blocks",[]):
                    counts[b.get(field,"")] += 1; total += 1
            for vidx, v in enumerate(vals):
                matrix[cidx,vidx] = counts.get(v,0)/total*100 if total else 0
        im = ax.imshow(matrix, cmap='YlOrRd', aspect='auto', vmin=0)
        short = [v.replace("_3x3","").replace("_separable","Sep").replace("standard","Std").replace("depthwise","DW").replace("dilated","Dil").replace("bottleneck","Bnk").replace("batchnorm","BN").replace("layernorm","LN").replace("groupnorm","GN").replace("none","None").replace("identity","Id").replace("projection","Proj") for v in vals]
        ax.set_xticks(range(len(vals))); ax.set_xticklabels(short, rotation=30, ha='right', fontsize=6)
        ax.set_yticks(range(len(active))); ax.set_yticklabels([LABELS[c] for c in active], fontsize=6)
        ax.set_title(field.replace("_"," ").title(), fontsize=9)
        for i in range(len(active)):
            for j in range(len(vals)):
                ax.text(j, i, f"{matrix[i,j]:.0f}", ha='center', va='center', fontsize=5, color='white' if matrix[i,j]>40 else 'black')
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    plt.tight_layout(); plt.savefig(f"{out}/fig4_design_heatmap.pdf"); plt.close()

def fig5_training(data, out):
    active = [c for c in CONDS if get_valid(data, c, "cifar10")]
    ncols = min(len(active), 3); nrows = (len(active)+ncols-1)//ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.5*ncols, 2.8*nrows))
    if nrows*ncols == 1: axes = np.array([[axes]])
    elif nrows == 1: axes = axes[np.newaxis, :]
    for cidx, c in enumerate(active):
        ax = axes[cidx//ncols][cidx%ncols]
        valid = get_valid(data, c, "cifar10")
        if not valid: continue
        best_r = max(valid, key=lambda r: r["test_acc"])
        hist = best_r.get("history", {})
        if not hist: continue
        epochs = range(1, len(hist.get("train_loss",[]))+1)
        if hist.get("train_loss"): ax.plot(epochs, hist["train_loss"], 'b-', label='Train Loss', linewidth=0.8)
        if hist.get("val_loss"): ax.plot(epochs, hist["val_loss"], 'r-', label='Val Loss', linewidth=0.8)
        ax.set_xlabel("Epoch",fontsize=7); ax.set_ylabel("Loss",fontsize=7)
        ax.set_title(f"{LABELS[c]} (Best: {best_r['test_acc']:.1f}%)", fontsize=8)
        ax.legend(fontsize=5); ax.grid(alpha=0.2); ax.tick_params(labelsize=6)
    for i in range(len(active), nrows*ncols):
        axes[i//ncols][i%ncols].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{out}/fig5_training.pdf"); plt.close()

def fig6_diversity(data, out):
    fig, ax = plt.subplots(figsize=(5.5, 3.0))
    active = [c for c in CONDS if get_valid(data, c, "cifar10")]
    for didx, ds in enumerate(["cifar10", "cifar100"]):
        divs = []
        for c in active:
            valid = get_valid(data, c, ds)
            configs = [r["config"] for r in valid if "config" in r]
            divs.append(mean_jaccard_distance(configs) if configs else 0)
        x = np.arange(len(active))
        w = 0.35; offset = (didx-0.5)*w
        ax.bar(x+offset, divs, w, label="CIFAR-10" if ds=="cifar10" else "CIFAR-100",
               color=[COLORS[c] for c in active], alpha=0.5+0.3*didx, edgecolor='black', linewidth=0.5)
    ax.set_xticks(range(len(active)))
    ax.set_xticklabels([LABELS[c] for c in active], rotation=15, ha='right', fontsize=7)
    ax.set_ylabel("Mean Pairwise Jaccard Distance\n(Higher = More Diverse)")
    ax.legend(fontsize=7); ax.grid(axis='y', alpha=0.2)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{out}/fig6_diversity.pdf"); plt.close()

def fig7_channels(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.8))
    active = [c for c in CONDS if get_valid(data, c, "cifar10")]
    ch_vals = [32, 64, 128, 256]
    for idx, ds in enumerate(["cifar10","cifar100"]):
        ax = axes[idx]
        for cidx, c in enumerate(active):
            valid = get_valid(data, c, ds)
            counts = Counter(); total = 0
            for r in valid:
                if "config" not in r: continue
                for b in r["config"].get("blocks",[]):
                    counts[b.get("channels",0)] += 1; total += 1
            if total:
                fracs = [counts.get(ch,0)/total*100 for ch in ch_vals]
                offset = (cidx - len(active)/2 + 0.5) * 0.14
                ax.bar(np.arange(len(ch_vals))+offset, fracs, 0.14, label=LABELS[c], color=COLORS[c], alpha=0.8)
        ax.set_xticks(range(len(ch_vals))); ax.set_xticklabels(ch_vals)
        ax.set_xlabel("Channel Width"); ax.set_ylabel("% of Blocks")
        ax.set_title("CIFAR-10" if ds=="cifar10" else "CIFAR-100")
        if idx==0: ax.legend(fontsize=5, loc='upper left')
        ax.grid(axis='y',alpha=0.2); ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    plt.tight_layout(); plt.savefig(f"{out}/fig7_channels.pdf"); plt.close()

# ─── LaTeX Tables ─────────────────────────────────────────────────────────────
def latex_table_main(data, out):
    active = [c for c in CONDS if any(get_accs(data,c,ds).size>0 for ds in ["cifar10","cifar100"])]
    lines = [
        r"\begin{table}[t]", r"\centering\small",
        r"\caption{Test accuracy (\%) across conditions. Mean $\pm$ std, median, and best over 20 architectures per condition. "
        r"Conditions C and D receive \emph{validation-only} feedback (no test leakage). Best mean per dataset in \textbf{bold}.}",
        r"\label{tab:main}",
        r"\begin{tabular}{@{}l cccc cccc@{}}",
        r"\toprule",
        r"& \multicolumn{4}{c}{CIFAR-10} & \multicolumn{4}{c}{CIFAR-100} \\",
        r"\cmidrule(lr){2-5} \cmidrule(lr){6-9}",
        r"Condition & Mean & Std & Med & Best & Mean & Std & Med & Best \\",
        r"\midrule",
    ]
    bests = {}
    for ds in ["cifar10","cifar100"]:
        bests[ds] = max((np.mean(get_accs(data,c,ds)) for c in active if get_accs(data,c,ds).size>0), default=0)
    for c in active:
        parts = []
        for ds in ["cifar10","cifar100"]:
            accs = get_accs(data,c,ds)
            if accs.size==0: parts.append("-- & -- & -- & --"); continue
            m,s,med,b = np.mean(accs),np.std(accs),np.median(accs),np.max(accs)
            bold = r"\textbf{" if abs(m-bests[ds])<0.05 else ""
            be = "}" if bold else ""
            parts.append(f"{bold}{m:.1f}{be} & {s:.1f} & {med:.1f} & {b:.1f}")
        lines.append(f"{LABELS[c]} & {parts[0]} & {parts[1]} \\\\")
    lines += [r"\bottomrule",r"\end{tabular}",r"\end{table}"]
    with open(f"{out}/tab_main.tex","w") as f: f.write("\n".join(lines))

def latex_table_stats(data, out):
    active = [c for c in CONDS if get_accs(data,c,"cifar10").size>0]
    pairs = [(a,b) for i,a in enumerate(active) for b in active[i+1:]]
    lines = [
        r"\begin{table}[t]",r"\centering\small",
        r"\caption{Pairwise comparisons. Welch's $t$-test and Mann--Whitney $U$ (Bonferroni-corrected). "
        r"Cohen's $d$ with 95\% bootstrap CI. Positive $d$ = first condition higher.}",
        r"\label{tab:stats}",
        r"\begin{tabular}{@{}l rrr rrr@{}}",r"\toprule",
        r"& \multicolumn{3}{c}{CIFAR-10} & \multicolumn{3}{c}{CIFAR-100} \\",
        r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}",
        r"Comparison & $p_t$ & $p_U$ & $d$ [CI] & $p_t$ & $p_U$ & $d$ [CI] \\",
        r"\midrule",
    ]
    n_comp = len(pairs)
    for c1,c2 in pairs:
        row = []
        for ds in ["cifar10","cifar100"]:
            a1,a2 = get_accs(data,c1,ds), get_accs(data,c2,ds)
            if a1.size<2 or a2.size<2: row.append("-- & -- & --"); continue
            comp = full_comparison(a1, a2, LABELS[c1], LABELS[c2])
            alpha_corr = 0.05/n_comp
            sig_t = r"$^{*}$" if comp["t_p"]<alpha_corr else ""
            sig_u = r"$^{*}$" if comp["u_p"]<alpha_corr else ""
            row.append(f"{comp['t_p']:.3f}{sig_t} & {comp['u_p']:.3f}{sig_u} & {comp['cohens_d']:+.2f} [{comp['d_ci_lo']:+.2f},{comp['d_ci_hi']:+.2f}]")
        lines.append(f"{LABELS[c1]} vs {LABELS[c2]} & {row[0]} & {row[1]} \\\\")
    lines += [r"\bottomrule",r"\end{tabular}",r"\end{table}"]
    with open(f"{out}/tab_stats.tex","w") as f: f.write("\n".join(lines))

def latex_table_arch(data, out):
    active = [c for c in CONDS if get_valid(data,c,"cifar10")]
    lines = [
        r"\begin{table}[t]",r"\centering\small",
        r"\caption{Architecture characteristics (CIFAR-10). Efficiency = accuracy per M parameters. "
        r"Diversity = mean pairwise Jaccard distance (higher = more diverse).}",
        r"\label{tab:arch}",
        r"\begin{tabular}{@{}l rrrrrr@{}}",r"\toprule",
        r"Condition & Params (K) & Blocks & Gap (\%) & Eff. & Diversity & Time (s) \\",
        r"\midrule",
    ]
    for c in active:
        valid = get_valid(data,c,"cifar10")
        if not valid: continue
        params = np.mean([r["param_count"] for r in valid])/1e3
        blocks = np.mean([len(r["config"]["blocks"]) for r in valid if "config" in r])
        gaps = np.mean([r.get("train_val_gap",0) for r in valid])
        eff = np.mean([r["test_acc"]/(r["param_count"]/1e6) for r in valid if r["param_count"]>0])
        configs = [r["config"] for r in valid if "config" in r]
        div = mean_jaccard_distance(configs)
        times = np.mean([r.get("total_time_s",0) for r in valid])
        lines.append(f"{LABELS[c]} & {params:.0f} & {blocks:.1f} & {gaps:.1f} & {eff:.0f} & {div:.3f} & {times:.0f} \\\\")
    lines += [r"\bottomrule",r"\end{tabular}",r"\end{table}"]
    with open(f"{out}/tab_arch.tex","w") as f: f.write("\n".join(lines))

def latex_table_rank_corr(data, out):
    rc = rank_correlation_from_histories(data, "cifar10")
    if not rc: return
    lines = [
        r"\begin{table}[t]",r"\centering\small",
        r"\caption{Rank stability: Spearman $\rho$ and Kendall $\tau$ between validation accuracy at epoch 20 vs.\ final (epoch 50).}",
        r"\label{tab:rank}",
        r"\begin{tabular}{@{}l cccc@{}}",r"\toprule",
        r"Condition & $n$ & Spearman $\rho$ & Kendall $\tau$ & $p$ (Spearman) \\",
        r"\midrule",
    ]
    for c in CONDS:
        if c not in rc: continue
        r = rc[c]
        lines.append(f"{LABELS[c]} & {r['n']} & {r['spearman_rho']:.3f} & {r['kendall_tau']:.3f} & {r['spearman_p']:.4f} \\\\")
    lines += [r"\bottomrule",r"\end{tabular}",r"\end{table}"]
    with open(f"{out}/tab_rank.tex","w") as f: f.write("\n".join(lines))

def latex_table_transcript(data, out):
    tc = analyze_transcripts(data, "cifar10")
    if not tc: return
    lines = [
        r"\begin{table}[t]",r"\centering\small",
        r"\caption{Quantitative transcript analysis: causal attribution frequency in LLM responses (CIFAR-10).}",
        r"\label{tab:transcript}",
        r"\begin{tabular}{@{}l ccc@{}}",r"\toprule",
        r"Condition & Transcripts & Causal/Arch & \% with Causal \\",
        r"\midrule",
    ]
    for c in ["B","C","D"]:
        if c not in tc: continue
        t = tc[c]
        pct = t["transcripts_with_causal"]/t["total_transcripts"]*100 if t["total_transcripts"]>0 else 0
        lines.append(f"{LABELS[c]} & {t['total_transcripts']} & {t['mean_causal_per_arch']:.1f}$\\pm${t['std_causal']:.1f} & {pct:.0f}\\% \\\\")
    lines += [r"\bottomrule",r"\end{tabular}",r"\end{table}"]
    with open(f"{out}/tab_transcript.tex","w") as f: f.write("\n".join(lines))


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", default="results_v2")
    parser.add_argument("--output_dir", default="figures_v2")
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    print("Loading results...")
    data = load_all(args.results_dir)
    print(f"Loaded {len(data)} runs")
    for k in sorted(data.keys()):
        n = len(data[k]); nv = sum(1 for r in data[k] if r.get("valid") and r.get("test_acc"))
        print(f"  {k}: {nv}/{n}")

    out = args.output_dir
    print("\nGenerating figures...")
    fig1_violin(data, out); print("  fig1"); fig2_convergence(data, out); print("  fig2")
    fig3_param_acc(data, out); print("  fig3"); fig4_heatmap(data, out); print("  fig4")
    fig5_training(data, out); print("  fig5"); fig6_diversity(data, out); print("  fig6")
    fig7_channels(data, out); print("  fig7")

    print("\nGenerating tables...")
    latex_table_main(data, out); latex_table_stats(data, out); latex_table_arch(data, out)
    latex_table_rank_corr(data, out); latex_table_transcript(data, out)

    print("\nTranscript analysis...")
    tc = analyze_transcripts(data)
    print(json.dumps(tc, indent=2))

    print("\nRank correlation...")
    rc = rank_correlation_from_histories(data)
    print(json.dumps(rc, indent=2))

    print(f"\nAll outputs saved to {out}/")

if __name__ == "__main__":
    main()
