#!/usr/bin/env python3
"""
Main experiment runner: LLM-Guided Architecture Design with Iterative Feedback.

Runs 4 conditions × 20 architectures × 2 datasets × 3 replications.
Usage: PYTHONUNBUFFERED=1 python -u run_experiment.py --condition [A|B|C|D] --dataset [cifar10|cifar100] --replication [0|1|2]
"""

import argparse
import json
import os
import random
import sys
import time
import traceback
from pathlib import Path

import numpy as np
import torch

from search_space import (
    SEARCH_SPACE, SEARCH_SPACE_DESCRIPTION, MAX_PARAMS,
    random_architecture_config, config_to_string, build_and_validate, count_parameters,
)
from train_arch import train_architecture

# ─── LLM Interface ───────────────────────────────────────────────────────────

import requests

# Local vLLM server (OpenAI-compatible API)
VLLM_BASE_URL = "http://localhost:8000/v1"
LLM_MODEL = "Qwen/Qwen3-8B"


def call_llm(system_prompt, user_prompt, temperature=0.7, max_tokens=2048):
    """Call local vLLM server (OpenAI-compatible API) and return response text."""
    response = requests.post(
        f"{VLLM_BASE_URL}/chat/completions",
        json={
            "model": LLM_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def sanitize_config(config):
    """Fix common LLM mistakes in config values."""
    # Fix global_pool naming
    gp = config.get("global_pool", "avg")
    if gp in ("avgpool", "average", "avg_pool"):
        config["global_pool"] = "avg"
    elif gp in ("maxpool", "maximum", "max_pool"):
        config["global_pool"] = "max"

    # Fix dropout to float
    config["dropout"] = float(config.get("dropout", 0.0))

    # Fix fc_layers to int
    config["fc_layers"] = int(config.get("fc_layers", 1))

    # Validate and fix block values
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
                # Snap to nearest valid channel count
                val = int(block.get(key, 64))
                block[key] = min(valid_vals, key=lambda x: abs(x - val))
            else:
                val = str(block.get(key, valid_vals[0])).lower().strip()
                if val not in valid_vals:
                    block[key] = valid_vals[0]  # default to first option

    return config


def parse_architecture_from_llm(response_text):
    """Extract JSON architecture config from LLM response."""
    text = response_text

    # Look for ```json ... ``` blocks first
    import re
    json_blocks = re.findall(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_blocks:
        for block in json_blocks:
            try:
                config = json.loads(block)
                if "blocks" in config:
                    return sanitize_config(config)
            except json.JSONDecodeError:
                continue

    # Try to find raw JSON object
    brace_depth = 0
    start = None
    for i, char in enumerate(text):
        if char == '{':
            if brace_depth == 0:
                start = i
            brace_depth += 1
        elif char == '}':
            brace_depth -= 1
            if brace_depth == 0 and start is not None:
                try:
                    config = json.loads(text[start:i+1])
                    if "blocks" in config:
                        return sanitize_config(config)
                except json.JSONDecodeError:
                    start = None
                    continue

    return None


# ─── Condition Runners ────────────────────────────────────────────────────────

def run_condition_A(n_architectures, dataset_name, num_classes, seed, results_dir):
    """Condition A: Random Search (baseline)."""
    rng = random.Random(seed)
    results = []

    for i in range(n_architectures):
        print(f"\n{'='*60}")
        print(f"[Condition A - Random] Architecture {i+1}/{n_architectures}")

        # Sample random architecture
        config = random_architecture_config(rng)
        model, info = build_and_validate(config, num_classes)

        if model is None:
            print(f"  Invalid: {info}")
            results.append({
                "iteration": i,
                "config": config,
                "config_str": config_to_string(config),
                "valid": False,
                "invalid_reason": info,
                "test_acc": None,
                "param_count": None,
            })
            continue

        param_count = info
        print(f"  Config: {config_to_string(config)}")
        print(f"  Parameters: {param_count:,}")

        # Train
        metrics = train_architecture(model, dataset_name=dataset_name, seed=seed + i)
        print(f"  Test Acc: {metrics['test_acc']:.2f}%  |  Val Acc: {metrics['best_val_acc']:.2f}%  |  Time: {metrics['total_time_s']:.1f}s")

        result = {
            "iteration": i,
            "config": config,
            "config_str": config_to_string(config),
            "valid": True,
            "param_count": param_count,
            **metrics,
        }
        results.append(result)

        # Save incrementally
        with open(results_dir / "results.json", "w") as f:
            json.dump(results, f, indent=2)

    return results


def run_condition_B(n_architectures, dataset_name, num_classes, seed, results_dir):
    """Condition B: LLM Zero-Shot (no feedback)."""
    results = []
    system_prompt = f"""You are an expert neural architecture designer. Your task is to design CNN architectures for image classification.

{SEARCH_SPACE_DESCRIPTION}

You are designing for {'CIFAR-10 (10 classes)' if num_classes == 10 else 'CIFAR-100 (100 classes)'}.

IMPORTANT: Return ONLY a valid JSON configuration. No explanation needed, just the JSON."""

    for i in range(n_architectures):
        print(f"\n{'='*60}")
        print(f"[Condition B - LLM No-Feedback] Architecture {i+1}/{n_architectures}")

        user_prompt = f"""Design architecture #{i+1} for {'CIFAR-10' if num_classes == 10 else 'CIFAR-100'}.
Try to achieve the highest possible test accuracy within the 5M parameter constraint.
Return only the JSON configuration."""

        try:
            response = call_llm(system_prompt, user_prompt)
            config = parse_architecture_from_llm(response)

            if config is None:
                print(f"  Failed to parse LLM response")
                results.append({
                    "iteration": i,
                    "valid": False,
                    "invalid_reason": "Failed to parse JSON from LLM response",
                    "llm_response": response[:500],
                    "test_acc": None,
                })
                continue

            model, info = build_and_validate(config, num_classes)
            if model is None:
                print(f"  Invalid architecture: {info}")
                results.append({
                    "iteration": i,
                    "config": config,
                    "config_str": config_to_string(config),
                    "valid": False,
                    "invalid_reason": info,
                    "llm_response": response[:500],
                    "test_acc": None,
                })
                continue

            param_count = info
            print(f"  Config: {config_to_string(config)}")
            print(f"  Parameters: {param_count:,}")

            metrics = train_architecture(model, dataset_name=dataset_name, seed=seed + i)
            print(f"  Test Acc: {metrics['test_acc']:.2f}%  |  Val Acc: {metrics['best_val_acc']:.2f}%  |  Time: {metrics['total_time_s']:.1f}s")

            result = {
                "iteration": i,
                "config": config,
                "config_str": config_to_string(config),
                "valid": True,
                "param_count": param_count,
                "llm_response": response[:500],
                **metrics,
            }
            results.append(result)

        except Exception as e:
            print(f"  Error: {e}")
            traceback.print_exc()
            results.append({
                "iteration": i,
                "valid": False,
                "invalid_reason": f"Exception: {str(e)}",
                "test_acc": None,
            })

        # Save incrementally
        with open(results_dir / "results.json", "w") as f:
            json.dump(results, f, indent=2)

    return results


def run_condition_C(n_architectures, dataset_name, num_classes, seed, results_dir):
    """Condition C: LLM + Unstructured Feedback."""
    results = []
    history_summary = []

    system_prompt = f"""You are an expert neural architecture designer. Your task is to design CNN architectures for image classification.

{SEARCH_SPACE_DESCRIPTION}

You are designing for {'CIFAR-10 (10 classes)' if num_classes == 10 else 'CIFAR-100 (100 classes)'}.

After each architecture you design, I will tell you how it performed. Use this information to improve your next design.

IMPORTANT: Return ONLY a valid JSON configuration. No explanation needed, just the JSON."""

    for i in range(n_architectures):
        print(f"\n{'='*60}")
        print(f"[Condition C - LLM Unstructured Feedback] Architecture {i+1}/{n_architectures}")

        if i == 0:
            user_prompt = f"""Design your first architecture for {'CIFAR-10' if num_classes == 10 else 'CIFAR-100'}.
Try to achieve the highest possible test accuracy within the 5M parameter constraint.
Return only the JSON configuration."""
        else:
            feedback_lines = []
            for h in history_summary:
                feedback_lines.append(
                    f"Architecture {h['iteration']+1}: {'achieved ' + str(h['test_acc']) + '% test accuracy with ' + str(h['param_count']) + ' parameters' if h['valid'] else 'was invalid (' + h.get('invalid_reason', 'unknown') + ')'}"
                )
            feedback_text = "\n".join(feedback_lines)

            user_prompt = f"""Here are the results of your previous architectures:
{feedback_text}

Design architecture #{i+1}. Try to do better than before.
Return only the JSON configuration."""

        try:
            response = call_llm(system_prompt, user_prompt)
            config = parse_architecture_from_llm(response)

            if config is None:
                print(f"  Failed to parse LLM response")
                entry = {
                    "iteration": i,
                    "valid": False,
                    "invalid_reason": "Failed to parse JSON from LLM response",
                    "llm_response": response[:500],
                    "test_acc": None,
                }
                results.append(entry)
                history_summary.append(entry)
                continue

            model, info = build_and_validate(config, num_classes)
            if model is None:
                print(f"  Invalid architecture: {info}")
                entry = {
                    "iteration": i,
                    "config": config,
                    "config_str": config_to_string(config),
                    "valid": False,
                    "invalid_reason": info,
                    "llm_response": response[:500],
                    "test_acc": None,
                }
                results.append(entry)
                history_summary.append(entry)
                continue

            param_count = info
            print(f"  Config: {config_to_string(config)}")
            print(f"  Parameters: {param_count:,}")

            metrics = train_architecture(model, dataset_name=dataset_name, seed=seed + i)
            print(f"  Test Acc: {metrics['test_acc']:.2f}%  |  Val Acc: {metrics['best_val_acc']:.2f}%  |  Time: {metrics['total_time_s']:.1f}s")

            result = {
                "iteration": i,
                "config": config,
                "config_str": config_to_string(config),
                "valid": True,
                "param_count": param_count,
                "llm_response": response[:500],
                **metrics,
            }
            results.append(result)
            history_summary.append({
                "iteration": i, "valid": True,
                "test_acc": metrics["test_acc"], "param_count": param_count,
            })

        except Exception as e:
            print(f"  Error: {e}")
            traceback.print_exc()
            entry = {
                "iteration": i, "valid": False,
                "invalid_reason": f"Exception: {str(e)}", "test_acc": None,
            }
            results.append(entry)
            history_summary.append(entry)

        with open(results_dir / "results.json", "w") as f:
            json.dump(results, f, indent=2)

    return results


def run_condition_D(n_architectures, dataset_name, num_classes, seed, results_dir):
    """Condition D: LLM + Structured Feedback."""
    results = []
    history_table = []

    system_prompt = f"""You are an expert neural architecture designer. Your task is to iteratively design CNN architectures for image classification, learning from detailed training feedback.

{SEARCH_SPACE_DESCRIPTION}

You are designing for {'CIFAR-10 (10 classes)' if num_classes == 10 else 'CIFAR-100 (100 classes)'}.

After each architecture, I will provide structured feedback including:
- Full training/validation loss and accuracy curves
- Parameter count and efficiency metrics
- Overfitting analysis (train-val gap)
- A comparison table of all architectures tried so far

Use this information to reason about *why* architectures performed well or poorly, and design better architectures based on your analysis.

IMPORTANT: First, briefly analyze the feedback (2-3 sentences about what you learn from it), then return the JSON configuration."""

    for i in range(n_architectures):
        print(f"\n{'='*60}")
        print(f"[Condition D - LLM Structured Feedback] Architecture {i+1}/{n_architectures}")

        if i == 0:
            user_prompt = f"""Design your first architecture for {'CIFAR-10' if num_classes == 10 else 'CIFAR-100'}.
Try to achieve the highest possible test accuracy within the 5M parameter constraint.
First briefly state your design rationale, then return the JSON configuration."""
        else:
            # Build structured feedback
            table_header = f"{'#':>3} | {'Valid':>5} | {'TestAcc':>7} | {'ValAcc':>7} | {'TrainAcc':>8} | {'Gap':>5} | {'Params':>10} | {'Time(s)':>7}"
            table_sep = "-" * len(table_header)
            table_rows = [table_header, table_sep]

            for h in history_table:
                if h["valid"]:
                    table_rows.append(
                        f"{h['iteration']+1:>3} | {'Yes':>5} | {h['test_acc']:>6.2f}% | {h['best_val_acc']:>6.2f}% | {h['final_train_acc']:>7.2f}% | {h['train_val_gap']:>4.1f}% | {h['param_count']:>10,} | {h['total_time_s']:>7.1f}"
                    )
                else:
                    table_rows.append(
                        f"{h['iteration']+1:>3} | {'No':>5} | {'N/A':>7} | {'N/A':>7} | {'N/A':>8} | {'N/A':>5} | {'N/A':>10} | {'N/A':>7}  Reason: {h.get('invalid_reason', 'unknown')[:50]}"
                    )

            # Include last architecture's training curves (sampled every 5 epochs)
            last_valid = None
            for h in reversed(history_table):
                if h["valid"]:
                    last_valid = h
                    break

            curve_info = ""
            if last_valid and "history" in last_valid:
                hist = last_valid["history"]
                curve_info = f"""

### Training Curves for Architecture #{last_valid['iteration']+1} (most recent valid):
Epoch | TrainLoss | ValLoss | TrainAcc | ValAcc
"""
                for epoch_idx in range(0, len(hist["train_loss"]), 5):
                    curve_info += f"  {epoch_idx+1:>3}  | {hist['train_loss'][epoch_idx]:>9.4f} | {hist['val_loss'][epoch_idx]:>7.4f} | {hist['train_acc'][epoch_idx]:>7.2f}% | {hist['val_acc'][epoch_idx]:>6.2f}%\n"
                # Always include last epoch
                if (len(hist["train_loss"]) - 1) % 5 != 0:
                    last = len(hist["train_loss"]) - 1
                    curve_info += f"  {last+1:>3}  | {hist['train_loss'][last]:>9.4f} | {hist['val_loss'][last]:>7.4f} | {hist['train_acc'][last]:>7.2f}% | {hist['val_acc'][last]:>6.2f}%\n"

            best_acc = max([h["test_acc"] for h in history_table if h["valid"]], default=0)

            user_prompt = f"""### Results So Far
Best test accuracy achieved: {best_acc:.2f}%

### Comparison Table
{chr(10).join(table_rows)}
{curve_info}

### Task
Analyze the results above. What patterns do you see? What worked well and what didn't?
Then design architecture #{i+1} to improve on the best result.
First state your analysis and rationale (2-3 sentences), then return the JSON configuration."""

        try:
            response = call_llm(system_prompt, user_prompt)
            config = parse_architecture_from_llm(response)

            if config is None:
                print(f"  Failed to parse LLM response")
                entry = {
                    "iteration": i,
                    "valid": False,
                    "invalid_reason": "Failed to parse JSON from LLM response",
                    "llm_response": response[:1000],
                    "test_acc": None,
                }
                results.append(entry)
                history_table.append(entry)
                continue

            model, info = build_and_validate(config, num_classes)
            if model is None:
                print(f"  Invalid architecture: {info}")
                entry = {
                    "iteration": i,
                    "config": config,
                    "config_str": config_to_string(config),
                    "valid": False,
                    "invalid_reason": info,
                    "llm_response": response[:1000],
                    "test_acc": None,
                }
                results.append(entry)
                history_table.append(entry)
                continue

            param_count = info
            print(f"  Config: {config_to_string(config)}")
            print(f"  Parameters: {param_count:,}")

            metrics = train_architecture(model, dataset_name=dataset_name, seed=seed + i)
            print(f"  Test Acc: {metrics['test_acc']:.2f}%  |  Val Acc: {metrics['best_val_acc']:.2f}%  |  Time: {metrics['total_time_s']:.1f}s")

            # Save LLM reasoning (first part of response before JSON)
            reasoning = response.split("{")[0].strip() if "{" in response else ""

            result = {
                "iteration": i,
                "config": config,
                "config_str": config_to_string(config),
                "valid": True,
                "param_count": param_count,
                "llm_response": response[:1000],
                "llm_reasoning": reasoning[:500],
                **metrics,
            }
            results.append(result)
            history_table.append({
                "iteration": i, "valid": True,
                "test_acc": metrics["test_acc"],
                "best_val_acc": metrics["best_val_acc"],
                "final_train_acc": metrics["final_train_acc"],
                "train_val_gap": metrics["train_val_gap"],
                "param_count": param_count,
                "total_time_s": metrics["total_time_s"],
                "history": metrics["history"],
            })

        except Exception as e:
            print(f"  Error: {e}")
            traceback.print_exc()
            entry = {
                "iteration": i, "valid": False,
                "invalid_reason": f"Exception: {str(e)}", "test_acc": None,
            }
            results.append(entry)
            history_table.append(entry)

        with open(results_dir / "results.json", "w") as f:
            json.dump(results, f, indent=2)

    return results


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="LLM-Guided Architecture Design Experiment")
    parser.add_argument("--condition", type=str, required=True, choices=["A", "B", "C", "D"],
                        help="Experimental condition: A=Random, B=LLM-NoFeedback, C=LLM-Unstructured, D=LLM-Structured")
    parser.add_argument("--dataset", type=str, required=True, choices=["cifar10", "cifar100"])
    parser.add_argument("--replication", type=int, required=True, choices=[0, 1, 2],
                        help="Replication index (0, 1, or 2)")
    parser.add_argument("--n_architectures", type=int, default=20,
                        help="Number of architectures to evaluate per condition")
    args = parser.parse_args()

    # Deterministic seed per replication
    base_seed = [42, 137, 256][args.replication]

    # Results directory
    results_dir = Path(f"results/{args.condition}_{args.dataset}_rep{args.replication}")
    results_dir.mkdir(parents=True, exist_ok=True)

    print(f"{'='*60}")
    print(f"Experiment: Condition {args.condition} | {args.dataset} | Replication {args.replication}")
    print(f"Seed: {base_seed} | N architectures: {args.n_architectures}")
    print(f"Results dir: {results_dir}")
    print(f"Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")
    print(f"{'='*60}")

    # Save experiment metadata
    metadata = {
        "condition": args.condition,
        "dataset": args.dataset,
        "replication": args.replication,
        "base_seed": base_seed,
        "n_architectures": args.n_architectures,
        "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
        "pytorch_version": torch.__version__,
        "start_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    with open(results_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    num_classes = 10 if args.dataset == "cifar10" else 100

    condition_fn = {
        "A": run_condition_A,
        "B": run_condition_B,
        "C": run_condition_C,
        "D": run_condition_D,
    }[args.condition]

    results = condition_fn(args.n_architectures, args.dataset, num_classes, base_seed, results_dir)

    # Summary
    valid = [r for r in results if r.get("valid", False)]
    invalid = [r for r in results if not r.get("valid", False)]
    accs = [r["test_acc"] for r in valid if r.get("test_acc") is not None]

    print(f"\n{'='*60}")
    print(f"SUMMARY: Condition {args.condition} | {args.dataset} | Rep {args.replication}")
    print(f"  Valid: {len(valid)}/{len(results)}")
    print(f"  Invalid: {len(invalid)}/{len(results)}")
    if accs:
        print(f"  Mean Test Acc: {np.mean(accs):.2f}%")
        print(f"  Std Test Acc: {np.std(accs):.2f}%")
        print(f"  Best Test Acc: {max(accs):.2f}%")
        print(f"  Worst Test Acc: {min(accs):.2f}%")
    print(f"{'='*60}")

    # Save final summary
    metadata["end_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    metadata["n_valid"] = len(valid)
    metadata["n_invalid"] = len(invalid)
    metadata["mean_acc"] = round(np.mean(accs), 2) if accs else None
    metadata["std_acc"] = round(np.std(accs), 2) if accs else None
    metadata["best_acc"] = round(max(accs), 2) if accs else None
    with open(results_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    main()
