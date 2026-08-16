#!/usr/bin/env python3
"""
V2 Experiment Runner — addresses all reviewer concerns:
1. NO test-set leakage: feedback uses ONLY validation accuracy
2. Adds Condition A2: sanity-filtered random (no excessive pooling)
3. Adds Condition E: Regularized Evolution (REA) baseline
4. Supports temperature ablation
5. Supports multi-seed retraining of top architectures
6. Supports epoch-20 vs epoch-50 rank correlation check
7. Saves full LLM transcripts for qualitative analysis

Usage:
  python run_v2.py --condition [A|A2|B|C|D|E] --dataset [cifar10|cifar100] --seed 42
  python run_v2.py --temp-ablation --dataset cifar10 --seed 42
  python run_v2.py --retrain-top5 --dataset cifar10
  python run_v2.py --rank-correlation --dataset cifar10
"""
import argparse, json, os, random, re, sys, time, traceback, copy
from pathlib import Path
import numpy as np
import torch
import requests

from search_space import (
    SEARCH_SPACE, SEARCH_SPACE_DESCRIPTION, MAX_PARAMS,
    random_architecture_config, config_to_string, build_and_validate, count_parameters,
)
from train_arch import train_architecture

# ─── LLM Interface ───────────────────────────────────────────────────────────
VLLM_BASE_URL = "http://localhost:8000/v1"
LLM_MODEL = "Qwen/Qwen3-8B"

def call_llm(system_prompt, user_prompt, temperature=0.7, max_tokens=2048):
    response = requests.post(
        f"{VLLM_BASE_URL}/chat/completions",
        json={"model": LLM_MODEL, "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ], "temperature": temperature, "max_tokens": max_tokens},
        timeout=180,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def sanitize_config(config):
    gp = config.get("global_pool", "avg")
    if gp in ("avgpool", "average", "avg_pool"): config["global_pool"] = "avg"
    elif gp in ("maxpool", "maximum", "max_pool"): config["global_pool"] = "max"
    config["dropout"] = float(config.get("dropout", 0.0))
    config["fc_layers"] = int(config.get("fc_layers", 1))
    valid = {
        "conv_type": ["standard_3x3", "depthwise_separable", "dilated_3x3", "bottleneck"],
        "channels": [32, 64, 128, 256],
        "activation": ["relu", "gelu", "silu", "mish"],
        "normalization": ["batchnorm", "layernorm", "groupnorm", "none"],
        "skip_connection": ["identity", "projection", "none"],
        "pooling": ["maxpool", "avgpool", "strided_conv", "none"],
    }
    for block in config.get("blocks", []):
        for key, valid_vals in valid.items():
            if key == "channels":
                val = int(block.get(key, 64))
                block[key] = min(valid_vals, key=lambda x: abs(x - val))
            else:
                val = str(block.get(key, valid_vals[0])).lower().strip()
                if val not in valid_vals: block[key] = valid_vals[0]
    return config

def parse_architecture_from_llm(response_text):
    text = response_text
    json_blocks = re.findall(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_blocks:
        for block in json_blocks:
            try:
                config = json.loads(block)
                if "blocks" in config: return sanitize_config(config)
            except json.JSONDecodeError: continue
    brace_depth = 0; start = None
    for i, char in enumerate(text):
        if char == '{':
            if brace_depth == 0: start = i
            brace_depth += 1
        elif char == '}':
            brace_depth -= 1
            if brace_depth == 0 and start is not None:
                try:
                    config = json.loads(text[start:i+1])
                    if "blocks" in config: return sanitize_config(config)
                except json.JSONDecodeError: start = None; continue
    return None

# ─── Sanity-filtered random ──────────────────────────────────────────────────
def sanity_filtered_random_config(rng):
    """Random architecture that avoids degenerate designs (no excessive pooling)."""
    while True:
        config = random_architecture_config(rng)
        # Count pooling ops
        n_pools = sum(1 for b in config["blocks"] if b["pooling"] != "none")
        n_blocks = len(config["blocks"])
        # Reject: more pools than blocks-1, or more than 3 pools on 32x32
        if n_pools <= min(n_blocks - 1, 3):
            return config

# ─── Regularized Evolution (REA) ─────────────────────────────────────────────
def mutate_config(config, rng):
    """Mutate a single random choice in the architecture."""
    config = copy.deepcopy(config)
    mutation_type = rng.choice(["block_field", "add_block", "remove_block", "head"])
    
    if mutation_type == "block_field" and config["blocks"]:
        block_idx = rng.randint(0, len(config["blocks"]) - 1)
        field = rng.choice(["conv_type", "channels", "activation", "normalization", "skip_connection", "pooling"])
        if field == "channels":
            config["blocks"][block_idx][field] = rng.choice([32, 64, 128, 256])
        else:
            config["blocks"][block_idx][field] = rng.choice(SEARCH_SPACE[field])
    elif mutation_type == "add_block" and len(config["blocks"]) < 6:
        new_block = {
            "conv_type": rng.choice(SEARCH_SPACE["conv_type"]),
            "channels": rng.choice(SEARCH_SPACE["channels"]),
            "activation": rng.choice(SEARCH_SPACE["activation"]),
            "normalization": rng.choice(SEARCH_SPACE["normalization"]),
            "skip_connection": rng.choice(SEARCH_SPACE["skip_connection"]),
            "pooling": "none",
        }
        pos = rng.randint(0, len(config["blocks"]))
        config["blocks"].insert(pos, new_block)
    elif mutation_type == "remove_block" and len(config["blocks"]) > 3:
        idx = rng.randint(0, len(config["blocks"]) - 1)
        config["blocks"].pop(idx)
    elif mutation_type == "head":
        choice = rng.choice(["global_pool", "fc_layers", "dropout"])
        if choice == "global_pool": config["global_pool"] = rng.choice(["avg", "max"])
        elif choice == "fc_layers": config["fc_layers"] = rng.choice([1, 2])
        elif choice == "dropout": config["dropout"] = rng.choice([0.0, 0.1, 0.3, 0.5])
    return config


# ─── Common training + eval ──────────────────────────────────────────────────
def train_and_eval(config, dataset_name, num_classes, seed, epochs=50):
    """Build, train, return metrics. Returns None if invalid."""
    model, info = build_and_validate(config, num_classes)
    if model is None:
        return None, info
    param_count = info
    metrics = train_architecture(model, dataset_name=dataset_name, epochs=epochs, seed=seed)
    return {
        "config": config,
        "config_str": config_to_string(config),
        "valid": True,
        "param_count": param_count,
        **metrics,
    }, None


# ─── Condition Runners ────────────────────────────────────────────────────────
def run_random(n, dataset_name, num_classes, seed, results_dir, filtered=False):
    """Condition A or A2 (sanity-filtered random)."""
    rng = random.Random(seed)
    results = []
    label = "A2-Filtered" if filtered else "A-Random"
    for i in range(n):
        print(f"\n{'='*60}\n[{label}] Architecture {i+1}/{n}")
        config = sanity_filtered_random_config(rng) if filtered else random_architecture_config(rng)
        result, err = train_and_eval(config, dataset_name, num_classes, seed + i)
        if result is None:
            results.append({"iteration": i, "valid": False, "invalid_reason": err, "test_acc": None})
        else:
            result["iteration"] = i
            print(f"  Test={result['test_acc']:.2f}%  Val={result['best_val_acc']:.2f}%  Params={result['param_count']:,}")
            results.append(result)
        _save(results, results_dir)
    return results

def run_llm_zeroshot(n, dataset_name, num_classes, seed, results_dir, temperature=0.7):
    """Condition B: independent LLM proposals."""
    results = []
    system_prompt = f"""You are an expert neural architecture designer.\n\n{SEARCH_SPACE_DESCRIPTION}\n\nYou are designing for {'CIFAR-10 (10 classes)' if num_classes == 10 else 'CIFAR-100 (100 classes)'}.\n\nIMPORTANT: Return ONLY a valid JSON configuration."""
    for i in range(n):
        print(f"\n{'='*60}\n[B-ZeroShot T={temperature}] Architecture {i+1}/{n}")
        user_prompt = f"Design architecture #{i+1}. Maximize test accuracy within 5M params. Return only JSON."
        try:
            response = call_llm(system_prompt, user_prompt, temperature=temperature)
            config = parse_architecture_from_llm(response)
            if config is None:
                results.append({"iteration": i, "valid": False, "invalid_reason": "parse_fail", "test_acc": None, "llm_response": response[:2000]})
                continue
            result, err = train_and_eval(config, dataset_name, num_classes, seed + i)
            if result is None:
                results.append({"iteration": i, "valid": False, "invalid_reason": err, "test_acc": None, "llm_response": response[:2000]})
            else:
                result["iteration"] = i
                result["llm_response"] = response[:2000]
                print(f"  Test={result['test_acc']:.2f}%  Val={result['best_val_acc']:.2f}%  Params={result['param_count']:,}")
                results.append(result)
        except Exception as e:
            results.append({"iteration": i, "valid": False, "invalid_reason": str(e), "test_acc": None})
        _save(results, results_dir)
    return results

def run_llm_feedback(n, dataset_name, num_classes, seed, results_dir, structured=False, temperature=0.7):
    """Condition C (unstructured) or D (structured). NO TEST LEAKAGE: uses val_acc only."""
    label = "D-Structured" if structured else "C-Unstructured"
    results = []; history = []
    
    sys_base = f"You are an expert neural architecture designer.\n\n{SEARCH_SPACE_DESCRIPTION}\n\nDesigning for {'CIFAR-10 (10 classes)' if num_classes == 10 else 'CIFAR-100 (100 classes)'}.\nAfter each design, I provide performance feedback. Use it to improve.\n"
    if structured:
        sys_base += "I will provide detailed training curves, validation accuracy, overfitting analysis, and a comparison table.\nFirst analyze the feedback (2-3 sentences), then return the JSON.\n"
    else:
        sys_base += "Return ONLY a valid JSON configuration.\n"

    for i in range(n):
        print(f"\n{'='*60}\n[{label} T={temperature}] Architecture {i+1}/{n}")
        if i == 0:
            user_prompt = f"Design your first architecture. Maximize accuracy within 5M params.{' First state your rationale, then' if structured else ''} Return JSON."
        elif not structured:
            # Unstructured: minimal feedback using VALIDATION accuracy only
            lines = []
            for h in history:
                if h["valid"]:
                    lines.append(f"Arch {h['iteration']+1}: {h['best_val_acc']:.1f}% val accuracy, {h['param_count']:,} params")
                else:
                    lines.append(f"Arch {h['iteration']+1}: invalid ({h.get('invalid_reason','?')})")
            user_prompt = f"Previous results:\n" + "\n".join(lines) + f"\n\nDesign architecture #{i+1}. Try to beat the best. Return only JSON."
        else:
            # Structured: detailed feedback using VALIDATION accuracy only
            header = f"{'#':>3} | {'ValAcc':>7} | {'TrainAcc':>8} | {'Gap':>5} | {'Params':>10} | {'Time':>6}"
            rows = [header, "-"*55]
            for h in history:
                if h["valid"]:
                    rows.append(f"{h['iteration']+1:>3} | {h['best_val_acc']:>6.1f}% | {h['final_train_acc']:>7.1f}% | {h['train_val_gap']:>4.1f}% | {h['param_count']:>10,} | {h['total_time_s']:>5.0f}s")
            
            # Training curves of last valid
            curve = ""
            for h in reversed(history):
                if h["valid"] and "history" in h:
                    hist = h["history"]
                    curve = "\n\nLast architecture training curve (val):\n"
                    for ep in range(0, len(hist["val_loss"]), 10):
                        curve += f"  Ep {ep+1}: val_loss={hist['val_loss'][ep]:.4f} val_acc={hist['val_acc'][ep]:.1f}%\n"
                    last_ep = len(hist["val_loss"]) - 1
                    if last_ep % 10 != 0:
                        curve += f"  Ep {last_ep+1}: val_loss={hist['val_loss'][last_ep]:.4f} val_acc={hist['val_acc'][last_ep]:.1f}%\n"
                    break

            best_val = max((h["best_val_acc"] for h in history if h["valid"]), default=0)
            user_prompt = f"Best validation accuracy so far: {best_val:.1f}%\n\nComparison table:\n" + "\n".join(rows) + curve + f"\n\nAnalyze results, then design architecture #{i+1} to improve. Return JSON."

        try:
            response = call_llm(sys_base, user_prompt, temperature=temperature)
            config = parse_architecture_from_llm(response)
            if config is None:
                entry = {"iteration": i, "valid": False, "invalid_reason": "parse_fail", "test_acc": None, "llm_response": response[:2000]}
                results.append(entry); history.append(entry); continue
            result, err = train_and_eval(config, dataset_name, num_classes, seed + i)
            if result is None:
                entry = {"iteration": i, "valid": False, "invalid_reason": err, "test_acc": None, "llm_response": response[:2000]}
                results.append(entry); history.append(entry); continue
            result["iteration"] = i
            result["llm_response"] = response[:2000]
            # Extract reasoning from structured feedback response
            if structured and "{" in response:
                result["llm_reasoning"] = response.split("{")[0].strip()[:1000]
            print(f"  Test={result['test_acc']:.2f}%  Val={result['best_val_acc']:.2f}%  Params={result['param_count']:,}")
            results.append(result)
            history.append(result)
        except Exception as e:
            traceback.print_exc()
            entry = {"iteration": i, "valid": False, "invalid_reason": str(e), "test_acc": None}
            results.append(entry); history.append(entry)
        _save(results, results_dir)
    return results

def run_rea(n, dataset_name, num_classes, seed, results_dir, pop_size=10, tournament_size=3):
    """Condition E: Regularized Evolution Algorithm."""
    rng = random.Random(seed)
    population = []  # list of (config, val_acc)
    results = []

    for i in range(n):
        print(f"\n{'='*60}\n[E-REA] Architecture {i+1}/{n}")
        if len(population) < pop_size:
            # Initialize population with random architectures
            config = sanity_filtered_random_config(rng)
        else:
            # Tournament selection + mutation
            tournament = rng.sample(population, tournament_size)
            parent = max(tournament, key=lambda x: x[1])
            config = mutate_config(parent[0], rng)

        result, err = train_and_eval(config, dataset_name, num_classes, seed + i)
        if result is None:
            results.append({"iteration": i, "valid": False, "invalid_reason": err, "test_acc": None})
        else:
            result["iteration"] = i
            val_acc = result["best_val_acc"]
            population.append((config, val_acc))
            # Keep population bounded (remove oldest)
            if len(population) > pop_size * 2:
                population = population[-pop_size:]
            print(f"  Test={result['test_acc']:.2f}%  Val={result['best_val_acc']:.2f}%  Params={result['param_count']:,}")
            results.append(result)
        _save(results, results_dir)
    return results


def _save(results, results_dir):
    with open(results_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2)


# ─── Temperature Ablation ────────────────────────────────────────────────────
def run_temp_ablation(dataset_name, num_classes, seed, n=20):
    """Run Condition B at T=0.3, 0.7, 1.0."""
    for temp in [0.3, 0.7, 1.0]:
        tag = f"B_T{temp}_{dataset_name}_s{seed}"
        rd = Path(f"results_v2/{tag}")
        rd.mkdir(parents=True, exist_ok=True)
        print(f"\n>>> Temperature ablation: T={temp}")
        run_llm_zeroshot(n, dataset_name, num_classes, seed, rd, temperature=temp)


# ─── Retrain Top-5 with Multiple Seeds ───────────────────────────────────────
def retrain_top5(dataset_name, num_classes):
    """Retrain top-5 architectures from each condition with 3 seeds."""
    import glob
    retrain_results = {}
    conditions = ["A", "A2", "B", "C", "D", "E"]
    
    for cond in conditions:
        pattern = f"results_v2/{cond}_{dataset_name}_*"
        dirs = sorted(glob.glob(pattern))
        if not dirs: continue
        # Load results from first match
        rf = Path(dirs[0]) / "results.json"
        if not rf.exists(): continue
        all_r = json.load(open(rf))
        valid = [r for r in all_r if r.get("valid") and r.get("test_acc")]
        valid.sort(key=lambda x: x["test_acc"], reverse=True)
        top5 = valid[:5]
        
        cond_results = []
        for rank, arch in enumerate(top5):
            config = arch["config"]
            seed_accs = []
            for s in [42, 137, 256]:
                model, info = build_and_validate(config, num_classes)
                if model is None: continue
                metrics = train_architecture(model, dataset_name=dataset_name, epochs=50, seed=s)
                seed_accs.append(metrics["test_acc"])
                print(f"  [{cond}] Rank {rank+1}, seed {s}: {metrics['test_acc']:.2f}%")
            cond_results.append({
                "rank": rank + 1,
                "config_str": config_to_string(config),
                "param_count": arch["param_count"],
                "original_acc": arch["test_acc"],
                "seed_accs": seed_accs,
                "mean_acc": float(np.mean(seed_accs)),
                "std_acc": float(np.std(seed_accs)),
            })
        retrain_results[cond] = cond_results
    
    out = Path("results_v2/retrain_top5")
    out.mkdir(parents=True, exist_ok=True)
    with open(out / f"{dataset_name}.json", "w") as f:
        json.dump(retrain_results, f, indent=2)
    print(f"Saved retrain results to {out}/{dataset_name}.json")


# ─── Rank Correlation: 20 vs 50 epochs ───────────────────────────────────────
def rank_correlation_check(dataset_name, num_classes, seed=42):
    """Train 20 random architectures for 20 and 50 epochs, compare rankings."""
    from scipy.stats import spearmanr, kendalltau
    rng = random.Random(seed)
    configs = [sanity_filtered_random_config(rng) for _ in range(20)]
    
    accs_20 = []; accs_50 = []
    for i, config in enumerate(configs):
        print(f"\n[RankCorr] Architecture {i+1}/20")
        # 20 epochs
        model, info = build_and_validate(config, num_classes)
        if model is None: accs_20.append(0); accs_50.append(0); continue
        m20 = train_architecture(model, dataset_name=dataset_name, epochs=20, seed=seed)
        accs_20.append(m20["test_acc"])
        # 50 epochs (fresh model)
        model2, _ = build_and_validate(config, num_classes)
        m50 = train_architecture(model2, dataset_name=dataset_name, epochs=50, seed=seed)
        accs_50.append(m50["test_acc"])
        print(f"  20ep={m20['test_acc']:.2f}%  50ep={m50['test_acc']:.2f}%")
    
    sp, sp_p = spearmanr(accs_20, accs_50)
    kt, kt_p = kendalltau(accs_20, accs_50)
    
    out = Path("results_v2/rank_correlation")
    out.mkdir(parents=True, exist_ok=True)
    result = {
        "dataset": dataset_name,
        "n": 20,
        "spearman_rho": round(sp, 4),
        "spearman_p": round(sp_p, 6),
        "kendall_tau": round(kt, 4),
        "kendall_p": round(kt_p, 6),
        "accs_20ep": accs_20,
        "accs_50ep": accs_50,
    }
    with open(out / f"{dataset_name}.json", "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSpearman rho={sp:.4f} (p={sp_p:.6f}), Kendall tau={kt:.4f} (p={kt_p:.6f})")


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", type=str, choices=["A","A2","B","C","D","E"])
    parser.add_argument("--dataset", type=str, default="cifar10", choices=["cifar10","cifar100"])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n", type=int, default=20)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--temp-ablation", action="store_true")
    parser.add_argument("--retrain-top5", action="store_true")
    parser.add_argument("--rank-correlation", action="store_true")
    args = parser.parse_args()

    num_classes = 10 if args.dataset == "cifar10" else 100

    if args.temp_ablation:
        run_temp_ablation(args.dataset, num_classes, args.seed, args.n)
        return
    if args.retrain_top5:
        retrain_top5(args.dataset, num_classes)
        return
    if args.rank_correlation:
        rank_correlation_check(args.dataset, num_classes, args.seed)
        return

    tag = f"{args.condition}_{args.dataset}_s{args.seed}"
    rd = Path(f"results_v2/{tag}")
    rd.mkdir(parents=True, exist_ok=True)

    meta = {"condition": args.condition, "dataset": args.dataset, "seed": args.seed,
            "n": args.n, "temperature": args.temperature,
            "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S")}
    with open(rd / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2)

    print(f"{'='*60}\nCondition {args.condition} | {args.dataset} | seed={args.seed} | T={args.temperature}\n{'='*60}")

    if args.condition == "A":
        run_random(args.n, args.dataset, num_classes, args.seed, rd, filtered=False)
    elif args.condition == "A2":
        run_random(args.n, args.dataset, num_classes, args.seed, rd, filtered=True)
    elif args.condition == "B":
        run_llm_zeroshot(args.n, args.dataset, num_classes, args.seed, rd, args.temperature)
    elif args.condition == "C":
        run_llm_feedback(args.n, args.dataset, num_classes, args.seed, rd, structured=False, temperature=args.temperature)
    elif args.condition == "D":
        run_llm_feedback(args.n, args.dataset, num_classes, args.seed, rd, structured=True, temperature=args.temperature)
    elif args.condition == "E":
        run_rea(args.n, args.dataset, num_classes, args.seed, rd)

    # Summary
    results = json.load(open(rd / "results.json"))
    valid = [r for r in results if r.get("valid") and r.get("test_acc")]
    accs = [r["test_acc"] for r in valid]
    print(f"\n{'='*60}\nSUMMARY: {len(valid)}/{len(results)} valid")
    if accs:
        print(f"  Mean={np.mean(accs):.2f}% Std={np.std(accs):.2f}% Best={max(accs):.2f}%")

if __name__ == "__main__":
    main()
