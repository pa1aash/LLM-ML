#!/usr/bin/env python3
"""
Analysis script: Generate figures and statistics for the paper.
Run after all experiments complete.

Usage: python analyze_results.py --results_dir results/ --output_dir figures/
"""

import argparse
import json
import os
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams.update({
    'font.size': 10,
    'font.family': 'serif',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
})

CONDITION_LABELS = {
    "A": "Random Search",
    "B": "LLM (No Feedback)",
    "C": "LLM (Unstructured)",
    "D": "LLM (Structured)",
}

CONDITION_COLORS = {
    "A": "#888888",
    "B": "#4C72B0",
    "C": "#DD8452",
    "D": "#55A868",
}


def load_all_results(results_dir):
    """Load all experiment results into a structured dict."""
    data = {}
    results_path = Path(results_dir)

    for run_dir in sorted(results_path.iterdir()):
        if not run_dir.is_dir():
            continue

        results_file = run_dir / "results.json"
        metadata_file = run_dir / "metadata.json"

        if not results_file.exists():
            continue

        with open(results_file) as f:
            results = json.load(f)
        
        metadata = {}
        if metadata_file.exists():
            with open(metadata_file) as f:
                metadata = json.load(f)

        condition = metadata.get("condition", run_dir.name.split("_")[0])
        dataset = metadata.get("dataset", run_dir.name.split("_")[1])
        replication = metadata.get("replication", int(run_dir.name.split("rep")[-1]))

        key = (condition, dataset, replication)
        data[key] = {
            "results": results,
            "metadata": metadata,
        }

    return data


def get_test_accuracies(data, condition, dataset):
    """Get all valid test accuracies for a condition/dataset across replications."""
    all_accs = []
    for rep in range(3):
        key = (condition, dataset, rep)
        if key in data:
            accs = [r["test_acc"] for r in data[key]["results"]
                    if r.get("valid", False) and r.get("test_acc") is not None]
            all_accs.extend(accs)
    return np.array(all_accs)


def get_per_replication_accs(data, condition, dataset):
    """Get test accuracies grouped by replication."""
    rep_accs = {}
    for rep in range(3):
        key = (condition, dataset, rep)
        if key in data:
            accs = [r["test_acc"] for r in data[key]["results"]
                    if r.get("valid", False) and r.get("test_acc") is not None]
            rep_accs[rep] = np.array(accs)
    return rep_accs


def get_best_so_far(data, condition, dataset, replication):
    """Get best-so-far accuracy curve for a single run."""
    key = (condition, dataset, replication)
    if key not in data:
        return []
    
    results = data[key]["results"]
    best = 0
    curve = []
    for r in results:
        if r.get("valid", False) and r.get("test_acc") is not None:
            best = max(best, r["test_acc"])
        curve.append(best)
    return curve


def get_invalid_rates(data, condition, dataset):
    """Get fraction of invalid architectures."""
    total = 0
    invalid = 0
    for rep in range(3):
        key = (condition, dataset, rep)
        if key in data:
            for r in data[key]["results"]:
                total += 1
                if not r.get("valid", False):
                    invalid += 1
    return invalid / total if total > 0 else 0


def cohens_d(group1, group2):
    """Compute Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0
    return (np.mean(group1) - np.mean(group2)) / pooled_std


def figure1_box_plots(data, output_dir):
    """Figure 1: Box plots of test accuracy by condition (main result)."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    for idx, dataset in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]
        conditions = ["A", "B", "C", "D"]
        box_data = []
        labels = []

        for cond in conditions:
            accs = get_test_accuracies(data, cond, dataset)
            if len(accs) > 0:
                box_data.append(accs)
                labels.append(CONDITION_LABELS[cond])
            else:
                box_data.append([0])
                labels.append(CONDITION_LABELS[cond])

        bp = ax.boxplot(box_data, labels=labels, patch_artist=True, widths=0.6,
                       medianprops=dict(color='black', linewidth=1.5))

        for patch, cond in zip(bp['boxes'], conditions):
            patch.set_facecolor(CONDITION_COLORS[cond])
            patch.set_alpha(0.7)

        ax.set_ylabel("Test Accuracy (%)")
        title = "CIFAR-10" if dataset == "cifar10" else "CIFAR-100"
        ax.set_title(title)
        ax.tick_params(axis='x', rotation=20)
        ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "figure1_accuracy_boxplots.pdf"))
    plt.savefig(os.path.join(output_dir, "figure1_accuracy_boxplots.png"))
    plt.close()
    print("Saved Figure 1: Accuracy box plots")


def figure2_convergence(data, output_dir):
    """Figure 2: Best-so-far accuracy curves (convergence analysis)."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    for idx, dataset in enumerate(["cifar10", "cifar100"]):
        ax = axes[idx]

        for cond in ["A", "B", "C", "D"]:
            curves = []
            for rep in range(3):
                curve = get_best_so_far(data, cond, dataset, rep)
                if curve:
                    curves.append(curve)

            if curves:
                # Pad to same length
                max_len = max(len(c) for c in curves)
                padded = []
                for c in curves:
                    if len(c) < max_len:
                        c = c + [c[-1]] * (max_len - len(c))
                    padded.append(c)

                curves_arr = np.array(padded)
                mean_curve = np.mean(curves_arr, axis=0)
                std_curve = np.std(curves_arr, axis=0)
                iters = np.arange(1, len(mean_curve) + 1)

                ax.plot(iters, mean_curve, color=CONDITION_COLORS[cond],
                       label=CONDITION_LABELS[cond], linewidth=1.5)
                ax.fill_between(iters, mean_curve - std_curve, mean_curve + std_curve,
                              color=CONDITION_COLORS[cond], alpha=0.15)

        ax.set_xlabel("Architecture Evaluation")
        ax.set_ylabel("Best Test Accuracy So Far (%)")
        title = "CIFAR-10" if dataset == "cifar10" else "CIFAR-100"
        ax.set_title(title)
        ax.legend(fontsize=8, loc='lower right')
        ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "figure2_convergence.pdf"))
    plt.savefig(os.path.join(output_dir, "figure2_convergence.png"))
    plt.close()
    print("Saved Figure 2: Convergence curves")


def figure3_invalid_rates(data, output_dir):
    """Figure 3: Invalid architecture rate by condition."""
    fig, ax = plt.subplots(figsize=(6, 3.5))

    conditions = ["A", "B", "C", "D"]
    datasets = ["cifar10", "cifar100"]

    x = np.arange(len(conditions))
    width = 0.35

    for i, dataset in enumerate(datasets):
        rates = [get_invalid_rates(data, cond, dataset) * 100 for cond in conditions]
        offset = (i - 0.5) * width
        bars = ax.bar(x + offset, rates, width, label="CIFAR-10" if dataset == "cifar10" else "CIFAR-100",
                      color=[CONDITION_COLORS[c] for c in conditions], alpha=0.6 + 0.3 * i,
                      edgecolor='black', linewidth=0.5)

    ax.set_ylabel("Invalid Architecture Rate (%)")
    ax.set_xticks(x)
    ax.set_xticklabels([CONDITION_LABELS[c] for c in conditions], rotation=15)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, max(ax.get_ylim()[1], 10))

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "figure3_invalid_rates.pdf"))
    plt.savefig(os.path.join(output_dir, "figure3_invalid_rates.png"))
    plt.close()
    print("Saved Figure 3: Invalid rates")


def compute_statistics(data, output_dir):
    """Compute and save all statistical tests."""
    stats_report = []

    for dataset in ["cifar10", "cifar100"]:
        stats_report.append(f"\n{'='*60}")
        stats_report.append(f"Dataset: {'CIFAR-10' if dataset == 'cifar10' else 'CIFAR-100'}")
        stats_report.append(f"{'='*60}")

        condition_accs = {}
        for cond in ["A", "B", "C", "D"]:
            accs = get_test_accuracies(data, cond, dataset)
            condition_accs[cond] = accs
            n_valid = len(accs)
            n_total = sum(
                len(data.get((cond, dataset, rep), {}).get("results", []))
                for rep in range(3)
            )
            if len(accs) > 0:
                stats_report.append(f"\n{CONDITION_LABELS[cond]}:")
                stats_report.append(f"  N valid: {n_valid}/{n_total}")
                stats_report.append(f"  Mean: {np.mean(accs):.2f}% (+/- {np.std(accs):.2f}%)")
                stats_report.append(f"  Median: {np.median(accs):.2f}%")
                stats_report.append(f"  Best: {np.max(accs):.2f}%")
                stats_report.append(f"  Worst: {np.min(accs):.2f}%")

        # Pairwise Welch's t-tests with Bonferroni correction
        stats_report.append(f"\nPairwise Welch's t-tests (Bonferroni-corrected, 6 comparisons, alpha=0.0083):")
        pairs = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D")]
        for c1, c2 in pairs:
            if len(condition_accs[c1]) > 1 and len(condition_accs[c2]) > 1:
                t_stat, p_val = stats.ttest_ind(condition_accs[c1], condition_accs[c2], equal_var=False)
                d = cohens_d(condition_accs[c2], condition_accs[c1])  # positive = c2 better
                sig = "***" if p_val < 0.001 else "**" if p_val < 0.0083 else "*" if p_val < 0.05 else "ns"
                stats_report.append(
                    f"  {CONDITION_LABELS[c1]} vs {CONDITION_LABELS[c2]}: "
                    f"t={t_stat:.3f}, p={p_val:.4f} {sig}, Cohen's d={d:.3f}"
                )

    report = "\n".join(stats_report)
    print(report)

    with open(os.path.join(output_dir, "statistics_report.txt"), "w") as f:
        f.write(report)
    print(f"\nSaved statistics report to {output_dir}/statistics_report.txt")

    return report


def generate_latex_table(data, output_dir):
    """Generate LaTeX table for the paper."""
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Mean test accuracy (\%) across conditions and datasets. "
                 r"$\pm$ indicates standard deviation across architectures and replications. "
                 r"Best result per dataset in \textbf{bold}.}")
    lines.append(r"\label{tab:main_results}")
    lines.append(r"\begin{tabular}{lcccc}")
    lines.append(r"\toprule")
    lines.append(r"& \multicolumn{2}{c}{Test Accuracy (\%)} & \multicolumn{2}{c}{Invalid Rate (\%)} \\")
    lines.append(r"\cmidrule(lr){2-3} \cmidrule(lr){4-5}")
    lines.append(r"Condition & CIFAR-10 & CIFAR-100 & CIFAR-10 & CIFAR-100 \\")
    lines.append(r"\midrule")

    best_c10 = 0
    best_c100 = 0
    results_data = {}

    for cond in ["A", "B", "C", "D"]:
        for dataset in ["cifar10", "cifar100"]:
            accs = get_test_accuracies(data, cond, dataset)
            inv_rate = get_invalid_rates(data, cond, dataset) * 100
            mean_acc = np.mean(accs) if len(accs) > 0 else 0
            std_acc = np.std(accs) if len(accs) > 0 else 0
            results_data[(cond, dataset)] = (mean_acc, std_acc, inv_rate)

            if dataset == "cifar10":
                best_c10 = max(best_c10, mean_acc)
            else:
                best_c100 = max(best_c100, mean_acc)

    for cond in ["A", "B", "C", "D"]:
        m10, s10, i10 = results_data[(cond, "cifar10")]
        m100, s100, i100 = results_data[(cond, "cifar100")]

        c10_str = f"{m10:.1f} $\\pm$ {s10:.1f}"
        c100_str = f"{m100:.1f} $\\pm$ {s100:.1f}"

        if abs(m10 - best_c10) < 0.01:
            c10_str = r"\textbf{" + c10_str + "}"
        if abs(m100 - best_c100) < 0.01:
            c100_str = r"\textbf{" + c100_str + "}"

        lines.append(f"{CONDITION_LABELS[cond]} & {c10_str} & {c100_str} & {i10:.0f} & {i100:.0f} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    table = "\n".join(lines)
    with open(os.path.join(output_dir, "table_main_results.tex"), "w") as f:
        f.write(table)
    print(f"Saved LaTeX table to {output_dir}/table_main_results.tex")

    return table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", type=str, default="results")
    parser.add_argument("--output_dir", type=str, default="figures")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print("Loading results...")
    data = load_all_results(args.results_dir)
    print(f"Loaded {len(data)} experiment runs")

    if len(data) == 0:
        print("No results found! Check the results directory.")
        return

    # Show what we have
    for key in sorted(data.keys()):
        cond, dataset, rep = key
        n = len(data[key]["results"])
        n_valid = sum(1 for r in data[key]["results"] if r.get("valid", False))
        print(f"  {cond}_{dataset}_rep{rep}: {n_valid}/{n} valid architectures")

    print("\nGenerating figures...")
    figure1_box_plots(data, args.output_dir)
    figure2_convergence(data, args.output_dir)
    figure3_invalid_rates(data, args.output_dir)

    print("\nComputing statistics...")
    compute_statistics(data, args.output_dir)

    print("\nGenerating LaTeX table...")
    generate_latex_table(data, args.output_dir)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
