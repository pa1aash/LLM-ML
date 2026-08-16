#!/bin/bash
# Run ONLY the LLM conditions (B, C, D) + temp ablation that failed
# Also runs Phase 2 seed=137 for B, C, D
set -e
export PYTHONUNBUFFERED=1
LOG=v2_master.log

echo ">>> LLM conditions rerun at $(date)" >> $LOG

# Phase 1 LLM conditions (seed=42)
for cond in B C D; do
  for ds in cifar10 cifar100; do
    echo "  Running ${cond}_${ds}_s42 at $(date)" | tee -a $LOG
    python3 -u run_v2.py --condition $cond --dataset $ds --seed 42 --n 20 \
      2>&1 | tee logs_v2/${cond}_${ds}_s42.log
    echo "  Done ${cond}_${ds}_s42 at $(date)" | tee -a $LOG
  done
done

# Phase 2: Second seed for ALL conditions
echo ">>> PHASE 2: seed=137 replications at $(date)" >> $LOG
for cond in A A2 B C D E; do
  for ds in cifar10 cifar100; do
    echo "  Running ${cond}_${ds}_s137 at $(date)" | tee -a $LOG
    python3 -u run_v2.py --condition $cond --dataset $ds --seed 137 --n 20 \
      2>&1 | tee logs_v2/${cond}_${ds}_s137.log
    echo "  Done ${cond}_${ds}_s137 at $(date)" | tee -a $LOG
  done
done

# Temperature ablation
echo ">>> Temp ablation at $(date)" >> $LOG
for ds in cifar10 cifar100; do
  python3 -u run_v2.py --temp-ablation --dataset $ds --seed 42 --n 20 \
    2>&1 | tee logs_v2/temp_${ds}.log
done

# Rank correlation
echo ">>> Rank correlation at $(date)" >> $LOG
for ds in cifar10; do
  python3 -u run_v2.py --rank-correlation --dataset $ds --seed 42 \
    2>&1 | tee logs_v2/rank_${ds}.log
done

# Analysis
echo ">>> Analysis at $(date)" >> $LOG
python3 -u deep_analysis_v2.py --results_dir results_v2 --output_dir figures_v2 \
  2>&1 | tee logs_v2/analysis.log

echo "=== LLM RERUN + EXTENSIONS COMPLETE at $(date) ===" >> $LOG
