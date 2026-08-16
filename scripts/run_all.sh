#!/bin/bash
# Run all experimental conditions.
# Usage: bash run_all.sh
# Runs in a screen session so it survives disconnects.

set -e

export PYTHONUNBUFFERED=1

echo "============================================================"
echo "LLM-Guided Architecture Design: Full Experiment Suite"
echo "Start time: $(date)"
echo "============================================================"

mkdir -p results logs

# Phase 1: Condition A (Random Search) — no API needed, can run all replications
echo ""
echo ">>> PHASE 1: Condition A (Random Search)"
for dataset in cifar10 cifar100; do
    for rep in 0 1 2; do
        echo "  Running A_${dataset}_rep${rep}..."
        python -u run_experiment.py --condition A --dataset $dataset --replication $rep \
            2>&1 | tee logs/A_${dataset}_rep${rep}.log
    done
done

# Phase 2: Condition B (LLM No-Feedback) — independent calls, can batch
echo ""
echo ">>> PHASE 2: Condition B (LLM No-Feedback)"
for dataset in cifar10 cifar100; do
    for rep in 0 1 2; do
        echo "  Running B_${dataset}_rep${rep}..."
        python -u run_experiment.py --condition B --dataset $dataset --replication $rep \
            2>&1 | tee logs/B_${dataset}_rep${rep}.log
    done
done

# Phase 3: Condition C (LLM Unstructured Feedback) — sequential per run
echo ""
echo ">>> PHASE 3: Condition C (LLM Unstructured Feedback)"
for dataset in cifar10 cifar100; do
    for rep in 0 1 2; do
        echo "  Running C_${dataset}_rep${rep}..."
        python -u run_experiment.py --condition C --dataset $dataset --replication $rep \
            2>&1 | tee logs/C_${dataset}_rep${rep}.log
    done
done

# Phase 4: Condition D (LLM Structured Feedback) — sequential per run
echo ""
echo ">>> PHASE 4: Condition D (LLM Structured Feedback)"
for dataset in cifar10 cifar100; do
    for rep in 0 1 2; do
        echo "  Running D_${dataset}_rep${rep}..."
        python -u run_experiment.py --condition D --dataset $dataset --replication $rep \
            2>&1 | tee logs/D_${dataset}_rep${rep}.log
    done
done

echo ""
echo "============================================================"
echo "ALL EXPERIMENTS COMPLETE"
echo "End time: $(date)"
echo "============================================================"
