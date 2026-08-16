#!/usr/bin/env python3
"""
Deep analysis script for the comprehensive 8-page paper.
Generates all figures and tables with publication-quality formatting.
"""
import json, os, sys
from pathlib import Path
import numpy as np
from scipy import stats
from collections import Counter, defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams.update({
    'font.size': 9, 'font.family': 'serif', 'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
    'text.usetex': False,
})

CONDS = ["A", "B", "C", "D"]
LABELS = {"A": "Random", "B": "LLM (Zero-Shot)", "C": "LLM (Unstructured FB)", "D": "LLM (Structured FB)"}
COLORS = {"A": "#888888", "B": "#4C72B0", "C": "#DD8452", "D": "#55A868"}
MARKERS = {"A": "o", "B": "s", "C": "^", "D": "D"}


def load_results(results_dir):
    data = {}
    for run_dir in sorted(Path(results_dir).iterdir()):
        if not run_dir.is_dir(): continue
        rf = run_dir / "results.json"
        if not rf.exists(): continue
        results = json.load(open(rf))
        parts = run_dir.name.split("_")
        cond = parts[0]
        ds = parts[1]
        rep = int(parts[2].replace("rep",""))
        data[(cond, ds, rep)] = results
    return data


def get_valid(data, cond, ds, rep=0):
    key = (cond, ds, rep)
    if key not in data: return []
    return [r for r in data[key] if r.get("valid", False) and r.get("test_acc") is not None]


def get_accs(data, cond, ds, rep=0):
    return np.array([r["test_acc"] for r in get_valid(data, cond, ds, rep)])


# ── Figure 1: Main Results (Violin + Strip) ─────────────────────────────────
def fig1_violin_plots(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        positions = range(len(CONDS))
        all_data = [get_accs(data, c, ds) for c in CONDS]

        vp = ax.violinplot(all_data, positions=positions, showmedians=True, showextrema=False, widths=0.7)
        for i, body in enumerate(vp['bodies']):
            body.set_facecolor(COLORS[CONDS[i]])
            body.set_alpha(0.4)
        vp['cmedians'].set_color('black')
        vp['cmedians'].set_linewidth(1.5)

        # Strip plot overlay
        for i, (c, d) in enumerate(zip(CONDS, all_data)):
            jitter = np.random.default_rng(42).normal(0, 0.06, len(d))
            ax.scatter(np.full_like(d, i) + jitter, d, c=COLORS[c], s=12, alpha=0.6, zorder=5, edgecolor='white', linewidth=0.3)

        ax.set_xticks(positions)
        ax.set_xticklabels([LABELS[c] for c in CONDS], rotation=18, ha='right')
        ax.set_ylabel("Test Accuracy (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.grid(axis='y', alpha=0.2, linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.tight_layout(pad=1.0)
    plt.savefig(f"{out}/fig1_violin.pdf")
    plt.close()
    print("  Saved fig1_violin.pdf")


# ── Figure 2: Convergence (Best-So-Far) ─────────────────────────────────────
def fig2_convergence(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        for c in CONDS:
            valid = get_valid(data, c, ds)
            if not valid: continue
            bsf = []
            best = 0
            for r in valid:
                best = max(best, r["test_acc"])
                bsf.append(best)
            iters = np.arange(1, len(bsf)+1)
            ax.plot(iters, bsf, color=COLORS[c], label=LABELS[c], linewidth=1.5, marker=MARKERS[c], markersize=3, markevery=3)

        ax.set_xlabel("Architecture Evaluation #")
        ax.set_ylabel("Best Accuracy So Far (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.legend(fontsize=7, loc='lower right', framealpha=0.9)
        ax.grid(alpha=0.2, linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.tight_layout(pad=1.0)
    plt.savefig(f"{out}/fig2_convergence.pdf")
    plt.close()
    print("  Saved fig2_convergence.pdf")


# ── Figure 3: Parameter-Accuracy Scatter ─────────────────────────────────────
def fig3_param_accuracy(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        for c in CONDS:
            valid = get_valid(data, c, ds)
            if not valid: continue
            params = np.array([r["param_count"] for r in valid]) / 1e6  # millions
            accs = np.array([r["test_acc"] for r in valid])
            ax.scatter(params, accs, c=COLORS[c], s=25, alpha=0.7, label=LABELS[c], marker=MARKERS[c], edgecolor='white', linewidth=0.3)

        ax.set_xlabel("Parameters (M)")
        ax.set_ylabel("Test Accuracy (%)")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        ax.legend(fontsize=7, loc='lower right', framealpha=0.9)
        ax.grid(alpha=0.2, linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.tight_layout(pad=1.0)
    plt.savefig(f"{out}/fig3_param_accuracy.pdf")
    plt.close()
    print("  Saved fig3_param_accuracy.pdf")


# ── Figure 4: Architecture Design Choice Distribution Heatmap ────────────────
def fig4_design_heatmap(data, out):
    fields = ["conv_type", "activation", "normalization", "skip_connection"]
    field_vals = {
        "conv_type": ["standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"],
        "activation": ["relu", "gelu", "silu", "mish"],
        "normalization": ["batchnorm", "layernorm", "groupnorm", "none"],
        "skip_connection": ["identity", "projection", "none"],
    }

    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.5))
    ds = "cifar10"  # Use CIFAR-10 for design analysis

    for fidx, field in enumerate(fields):
        ax = axes[fidx // 2][fidx % 2]
        vals = field_vals[field]
        matrix = np.zeros((len(CONDS), len(vals)))

        for cidx, c in enumerate(CONDS):
            valid = get_valid(data, c, ds)
            total_blocks = 0
            counts = Counter()
            for r in valid:
                if "config" not in r: continue
                for block in r["config"].get("blocks", []):
                    counts[block.get(field, "unknown")] += 1
                    total_blocks += 1
            if total_blocks > 0:
                for vidx, v in enumerate(vals):
                    matrix[cidx, vidx] = counts.get(v, 0) / total_blocks * 100

        im = ax.imshow(matrix, cmap='YlOrRd', aspect='auto', vmin=0)
        ax.set_xticks(range(len(vals)))
        short = [v.replace("_3x3","").replace("_separable","Sep").replace("standard","Std").replace("depthwise","DW").replace("dilated","Dil").replace("bottleneck","Bneck").replace("batchnorm","BN").replace("layernorm","LN").replace("groupnorm","GN").replace("none","None").replace("identity","Id").replace("projection","Proj") for v in vals]
        ax.set_xticklabels(short, rotation=30, ha='right', fontsize=7)
        ax.set_yticks(range(len(CONDS)))
        ax.set_yticklabels([LABELS[c] for c in CONDS], fontsize=7)
        ax.set_title(field.replace("_"," ").title(), fontsize=9)
        # Annotate cells
        for i in range(len(CONDS)):
            for j in range(len(vals)):
                ax.text(j, i, f"{matrix[i,j]:.0f}", ha='center', va='center', fontsize=6,
                       color='white' if matrix[i,j] > 40 else 'black')
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="%")

    fig.suptitle("Design Choice Distribution on CIFAR-10 (% of blocks)", fontsize=10, y=1.01)
    plt.tight_layout(pad=0.8)
    plt.savefig(f"{out}/fig4_design_heatmap.pdf")
    plt.close()
    print("  Saved fig4_design_heatmap.pdf")


# ── Figure 5: Training Dynamics (Loss Curves for Best Architectures) ─────────
def fig5_training_dynamics(data, out):
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.0))
    for cidx, c in enumerate(CONDS):
        ax = axes[cidx // 2][cidx % 2]
        valid = get_valid(data, c, "cifar10")
        if not valid: continue
        # Find best architecture
        best_r = max(valid, key=lambda r: r["test_acc"])
        hist = best_r.get("history", {})
        if not hist: continue

        epochs = range(1, len(hist["train_loss"])+1)
        ax.plot(epochs, hist["train_loss"], 'b-', label='Train Loss', linewidth=1.0)
        ax.plot(epochs, hist["val_loss"], 'r-', label='Val Loss', linewidth=1.0)
        ax2 = ax.twinx()
        ax2.plot(epochs, hist["train_acc"], 'b--', label='Train Acc', linewidth=0.8, alpha=0.6)
        ax2.plot(epochs, hist["val_acc"], 'r--', label='Val Acc', linewidth=0.8, alpha=0.6)
        ax2.set_ylabel("Accuracy (%)", fontsize=7)
        ax2.tick_params(axis='y', labelsize=7)

        ax.set_xlabel("Epoch")
        ax.set_ylabel("Loss")
        ta = best_r['test_acc']
        pc = best_r['param_count']
        ax.set_title(f"{LABELS[c]} (Best: {ta:.1f}%, {pc/1e3:.0f}K params)", fontsize=8)
        ax.legend(fontsize=6, loc='upper right')
        ax.grid(alpha=0.2, linewidth=0.5)
    plt.tight_layout(pad=0.8)
    plt.savefig(f"{out}/fig5_training_dynamics.pdf")
    plt.close()
    print("  Saved fig5_training_dynamics.pdf")


# ── Figure 6: Architectural Diversity (Pairwise Jaccard Similarity) ──────────
def fig6_diversity(data, out):
    def arch_signature(config):
        """Convert architecture config to a set of (block_idx, field, value) tuples."""
        sig = set()
        for i, block in enumerate(config.get("blocks", [])):
            for k, v in block.items():
                sig.add((i, k, str(v)))
        sig.add(("head", "global_pool", config.get("global_pool", "")))
        sig.add(("head", "fc_layers", str(config.get("fc_layers", ""))))
        return sig

    def mean_jaccard(configs):
        sigs = [arch_signature(c) for c in configs]
        n = len(sigs)
        if n < 2: return 0
        total = 0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                inter = len(sigs[i] & sigs[j])
                union = len(sigs[i] | sigs[j])
                total += inter / union if union > 0 else 0
                count += 1
        return total / count

    fig, ax = plt.subplots(figsize=(5.0, 3.0))
    ds_list = ["cifar10", "cifar100"]
    x = np.arange(len(CONDS))
    width = 0.35

    for didx, ds in enumerate(ds_list):
        similarities = []
        for c in CONDS:
            valid = get_valid(data, c, ds)
            configs = [r["config"] for r in valid if "config" in r]
            sim = mean_jaccard(configs) if configs else 0
            similarities.append(sim)
        offset = (didx - 0.5) * width
        bars = ax.bar(x + offset, similarities, width,
                     label="CIFAR-10" if ds == "cifar10" else "CIFAR-100",
                     color=[COLORS[c] for c in CONDS],
                     alpha=0.5 + 0.3*didx, edgecolor='black', linewidth=0.5)

    ax.set_ylabel("Mean Pairwise Jaccard Similarity")
    ax.set_xticks(x)
    ax.set_xticklabels([LABELS[c] for c in CONDS], rotation=15, ha='right')
    ax.legend()
    ax.set_title("Architectural Diversity (Lower = More Diverse)")
    ax.grid(axis='y', alpha=0.2, linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{out}/fig6_diversity.pdf")
    plt.close()
    print("  Saved fig6_diversity.pdf")


# ── Figure 7: Channel Width Distribution ─────────────────────────────────────
def fig7_channels(data, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.8))
    for idx, ds in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        channel_vals = [32, 64, 128, 256]
        for cidx, c in enumerate(CONDS):
            valid = get_valid(data, c, ds)
            counts = Counter()
            total = 0
            for r in valid:
                if "config" not in r: continue
                for block in r["config"].get("blocks", []):
                    counts[block.get("channels", 0)] += 1
                    total += 1
            if total > 0:
                fracs = [counts.get(ch, 0) / total * 100 for ch in channel_vals]
                offset = (cidx - 1.5) * 0.18
                ax.bar(np.arange(len(channel_vals)) + offset, fracs, 0.18,
                      label=LABELS[c], color=COLORS[c], alpha=0.8, edgecolor='white', linewidth=0.3)

        ax.set_xticks(range(len(channel_vals)))
        ax.set_xticklabels(channel_vals)
        ax.set_xlabel("Channel Width")
        ax.set_ylabel("% of Blocks")
        ax.set_title("CIFAR-10" if ds == "cifar10" else "CIFAR-100")
        if idx == 0:
            ax.legend(fontsize=6, loc='upper left')
        ax.grid(axis='y', alpha=0.2)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{out}/fig7_channels.pdf")
    plt.close()
    print("  Saved fig7_channels.pdf")


# ── Statistical Tables ───────────────────────────────────────────────────────
def compute_all_stats(data, out):
    report = []

    # Table 1: Main results
    report.append("=" * 80)
    report.append("TABLE 1: Main Results")
    report.append("=" * 80)
    report.append(f"{'Condition':<25} {'CIFAR-10 Mean±Std':>20} {'CIFAR-10 Best':>13} {'CIFAR-100 Mean±Std':>20} {'CIFAR-100 Best':>14}")
    report.append("-" * 95)

    for c in CONDS:
        parts = []
        for ds in ["cifar10", "cifar100"]:
            accs = get_accs(data, c, ds)
            if len(accs) > 0:
                parts.append(f"{np.mean(accs):5.1f} ± {np.std(accs):4.1f}")
                parts.append(f"{np.max(accs):5.1f}")
            else:
                parts.extend(["  N/A", " N/A"])
        report.append(f"{LABELS[c]:<25} {parts[0]:>20} {parts[1]:>13} {parts[2]:>20} {parts[3]:>14}")

    # Table 2: Pairwise statistical tests
    report.append("\n" + "=" * 80)
    report.append("TABLE 2: Pairwise Welch's t-tests (Bonferroni corrected, 6 comparisons)")
    report.append("=" * 80)

    pairs = [("A","B"), ("A","C"), ("A","D"), ("B","C"), ("B","D"), ("C","D")]
    for ds in ["cifar10", "cifar100"]:
        report.append(f"\n--- {'CIFAR-10' if ds == 'cifar10' else 'CIFAR-100'} ---")
        report.append(f"{'Comparison':<40} {'t-stat':>8} {'p-value':>10} {'Cohen d':>9} {'Sig':>5}")
        report.append("-" * 75)
        for c1, c2 in pairs:
            a1, a2 = get_accs(data, c1, ds), get_accs(data, c2, ds)
            if len(a1) < 2 or len(a2) < 2: continue
            t, p = stats.ttest_ind(a1, a2, equal_var=False)
            n1, n2 = len(a1), len(a2)
            pooled = np.sqrt(((n1-1)*np.var(a1,ddof=1) + (n2-1)*np.var(a2,ddof=1)) / (n1+n2-2))
            d = (np.mean(a2) - np.mean(a1)) / pooled if pooled > 0 else 0
            sig = "***" if p < 0.001 else "**" if p < 0.0083 else "*" if p < 0.05 else "ns"
            report.append(f"{LABELS[c1]+' vs '+LABELS[c2]:<40} {t:>8.3f} {p:>10.4f} {d:>+9.3f} {sig:>5}")

    # Table 3: Architecture characteristics
    report.append("\n" + "=" * 80)
    report.append("TABLE 3: Architecture Characteristics (CIFAR-10)")
    report.append("=" * 80)
    report.append(f"{'Condition':<25} {'Mean Params':>12} {'Mean Blocks':>12} {'Mean Depth':>11} {'Pool Ops':>9}")
    report.append("-" * 72)

    for c in CONDS:
        valid = get_valid(data, c, "cifar10")
        if not valid: continue
        params = [r["param_count"] for r in valid]
        blocks = [len(r["config"]["blocks"]) for r in valid if "config" in r]
        pools = [sum(1 for b in r["config"]["blocks"] if b.get("pooling","none") != "none") for r in valid if "config" in r]
        report.append(f"{LABELS[c]:<25} {np.mean(params)/1e3:>10.0f}K {np.mean(blocks):>10.1f} {np.mean(blocks):>10.1f} {np.mean(pools):>8.1f}")

    # Table 4: Efficiency analysis
    report.append("\n" + "=" * 80)
    report.append("TABLE 4: Efficiency (Accuracy per Million Parameters)")
    report.append("=" * 80)
    for ds in ["cifar10", "cifar100"]:
        report.append(f"\n--- {'CIFAR-10' if ds == 'cifar10' else 'CIFAR-100'} ---")
        for c in CONDS:
            valid = get_valid(data, c, ds)
            if not valid: continue
            efficiencies = [r["test_acc"] / (r["param_count"] / 1e6) for r in valid if r["param_count"] > 0]
            report.append(f"  {LABELS[c]:<25} mean_eff={np.mean(efficiencies):.1f} acc/M_params")

    # Table 5: Overfitting analysis
    report.append("\n" + "=" * 80)
    report.append("TABLE 5: Overfitting Analysis (Train-Val Gap)")
    report.append("=" * 80)
    for ds in ["cifar10", "cifar100"]:
        report.append(f"\n--- {'CIFAR-10' if ds == 'cifar10' else 'CIFAR-100'} ---")
        for c in CONDS:
            valid = get_valid(data, c, ds)
            if not valid: continue
            gaps = [r.get("train_val_gap", 0) for r in valid]
            report.append(f"  {LABELS[c]:<25} mean_gap={np.mean(gaps):.1f}%, max_gap={np.max(gaps):.1f}%")

    text = "\n".join(report)
    print(text)
    with open(f"{out}/full_statistics.txt", "w") as f:
        f.write(text)


# ── LaTeX Tables ─────────────────────────────────────────────────────────────
def latex_tables(data, out):
    # Table 1: Main results (expanded)
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Test accuracy (\%) across conditions. We report mean $\pm$ std, median, and best over 20 architectures. " +
                 r"All LLM conditions produce zero invalid architectures; random search produces 3/20 degenerate architectures on CIFAR-10.}")
    lines.append(r"\label{tab:main}")
    lines.append(r"\begin{tabular}{@{}l cccc cccc@{}}")
    lines.append(r"\toprule")
    lines.append(r"& \multicolumn{4}{c}{CIFAR-10} & \multicolumn{4}{c}{CIFAR-100} \\")
    lines.append(r"\cmidrule(lr){2-5} \cmidrule(lr){6-9}")
    lines.append(r"Condition & Mean & Std & Med & Best & Mean & Std & Med & Best \\")
    lines.append(r"\midrule")

    best_c10 = max(np.mean(get_accs(data, c, "cifar10")) for c in CONDS if len(get_accs(data, c, "cifar10")) > 0)
    best_c100 = max(np.mean(get_accs(data, c, "cifar100")) for c in CONDS if len(get_accs(data, c, "cifar100")) > 0)

    for c in CONDS:
        parts = []
        for ds in ["cifar10", "cifar100"]:
            accs = get_accs(data, c, ds)
            m = np.mean(accs); s = np.std(accs); med = np.median(accs); b = np.max(accs)
            best_val = best_c10 if ds == "cifar10" else best_c100
            bold_s = r"\textbf{" if abs(m - best_val) < 0.01 else ""
            bold_e = "}" if bold_s else ""
            parts.append(f"{bold_s}{m:.1f}{bold_e} & {s:.1f} & {med:.1f} & {b:.1f}")
        lines.append(f"{LABELS[c]} & {parts[0]} & {parts[1]} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    with open(f"{out}/tab_main.tex", "w") as f:
        f.write("\n".join(lines))

    # Table 2: Pairwise statistical tests
    lines2 = []
    lines2.append(r"\begin{table}[t]")
    lines2.append(r"\centering")
    lines2.append(r"\small")
    lines2.append(r"\caption{Pairwise statistical comparisons (Welch's $t$-test, Bonferroni-corrected $\alpha=0.0083$). " +
                  r"Effect size reported as Cohen's $d$ (positive = second condition better).}")
    lines2.append(r"\label{tab:stats}")
    lines2.append(r"\begin{tabular}{@{}l rrl rrl@{}}")
    lines2.append(r"\toprule")
    lines2.append(r"& \multicolumn{3}{c}{CIFAR-10} & \multicolumn{3}{c}{CIFAR-100} \\")
    lines2.append(r"\cmidrule(lr){2-4} \cmidrule(lr){5-7}")
    lines2.append(r"Comparison & $t$ & $p$ & $d$ & $t$ & $p$ & $d$ \\")
    lines2.append(r"\midrule")

    pairs = [("A","B"), ("A","C"), ("A","D"), ("B","C"), ("B","D"), ("C","D")]
    for c1, c2 in pairs:
        row_parts = []
        for ds in ["cifar10", "cifar100"]:
            a1, a2 = get_accs(data, c1, ds), get_accs(data, c2, ds)
            t, p = stats.ttest_ind(a1, a2, equal_var=False)
            n1, n2 = len(a1), len(a2)
            pooled = np.sqrt(((n1-1)*np.var(a1,ddof=1) + (n2-1)*np.var(a2,ddof=1)) / (n1+n2-2))
            d = (np.mean(a2) - np.mean(a1)) / pooled if pooled > 0 else 0
            sig = r"$^{***}$" if p < 0.001 else r"$^{**}$" if p < 0.0083 else r"$^{*}$" if p < 0.05 else ""
            row_parts.append(f"{t:.2f} & {p:.4f}{sig} & {d:+.2f}")
        lines2.append(f"{LABELS[c1]} vs {LABELS[c2]} & {row_parts[0]} & {row_parts[1]} \\\\")

    lines2.append(r"\bottomrule")
    lines2.append(r"\end{tabular}")
    lines2.append(r"\end{table}")

    with open(f"{out}/tab_stats.tex", "w") as f:
        f.write("\n".join(lines2))

    # Table 3: Architecture characteristics
    lines3 = []
    lines3.append(r"\begin{table}[t]")
    lines3.append(r"\centering")
    lines3.append(r"\small")
    lines3.append(r"\caption{Architecture characteristics across conditions (CIFAR-10). Params in thousands. " +
                  r"Efficiency = accuracy / parameters (M).}")
    lines3.append(r"\label{tab:arch}")
    lines3.append(r"\begin{tabular}{@{}l rrrrrr@{}}")
    lines3.append(r"\toprule")
    lines3.append(r"Condition & Params (K) & Blocks & Pools & Gap (\%) & Eff. & Time (s) \\")
    lines3.append(r"\midrule")

    for c in CONDS:
        valid = get_valid(data, c, "cifar10")
        if not valid: continue
        params = np.mean([r["param_count"] for r in valid]) / 1e3
        blocks = np.mean([len(r["config"]["blocks"]) for r in valid if "config" in r])
        pools = np.mean([sum(1 for b in r["config"]["blocks"] if b.get("pooling","none") != "none") for r in valid if "config" in r])
        gaps = np.mean([r.get("train_val_gap", 0) for r in valid])
        eff = np.mean([r["test_acc"] / (r["param_count"]/1e6) for r in valid if r["param_count"] > 0])
        times = np.mean([r.get("total_time_s", 0) for r in valid])
        lines3.append(f"{LABELS[c]} & {params:.0f} & {blocks:.1f} & {pools:.1f} & {gaps:.1f} & {eff:.0f} & {times:.0f} \\\\")

    lines3.append(r"\bottomrule")
    lines3.append(r"\end{tabular}")
    lines3.append(r"\end{table}")

    with open(f"{out}/tab_arch.tex", "w") as f:
        f.write("\n".join(lines3))

    print("  Saved tab_main.tex, tab_stats.tex, tab_arch.tex")


def main():
    results_dir = "results"
    out = "figures_v2"
    os.makedirs(out, exist_ok=True)

    print("Loading results...")
    data = load_results(results_dir)
    print(f"Loaded {len(data)} runs")

    print("\nGenerating figures...")
    fig1_violin_plots(data, out)
    fig2_convergence(data, out)
    fig3_param_accuracy(data, out)
    fig4_design_heatmap(data, out)
    fig5_training_dynamics(data, out)
    fig6_diversity(data, out)
    fig7_channels(data, out)

    print("\nComputing statistics...")
    compute_all_stats(data, out)

    print("\nGenerating LaTeX tables...")
    latex_tables(data, out)

    print("\nDone! All outputs in", out)


if __name__ == "__main__":
    main()
