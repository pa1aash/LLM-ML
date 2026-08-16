#!/bin/bash
# V2 Full Experiment Suite — addresses ALL reviewer concerns
# Run inside screen on the GPU server: screen -S expv2 bash run_all_v2.sh
set -e
export PYTHONUNBUFFERED=1
LOG=v2_master.log

echo "============================================================" | tee $LOG
echo "V2 EXPERIMENT SUITE — $(date)" | tee -a $LOG
echo "Fixes: test leakage, adds REA/filtered-random, temp ablation" | tee -a $LOG
echo "============================================================" | tee -a $LOG

mkdir -p results_v2 logs_v2

# ─── Phase 1: Core conditions (6 conditions × 2 datasets × seed=42) ─────────
echo ">>> PHASE 1: Core experiments (seed=42)" | tee -a $LOG
for cond in A A2 B C D E; do
  for ds in cifar10 cifar100; do
    echo "  Running ${cond}_${ds}_s42 at $(date)" | tee -a $LOG
    python3 -u run_v2.py --condition $cond --dataset $ds --seed 42 --n 20 \
      2>&1 | tee logs_v2/${cond}_${ds}_s42.log
    echo "  Done ${cond}_${ds}_s42 at $(date)" | tee -a $LOG
  done
done

# ─── Phase 2: Second seed for robustness (seed=137) ─────────────────────────
echo ">>> PHASE 2: Robustness replications (seed=137)" | tee -a $LOG
for cond in A A2 B C D E; do
  for ds in cifar10 cifar100; do
    echo "  Running ${cond}_${ds}_s137 at $(date)" | tee -a $LOG
    python3 -u run_v2.py --condition $cond --dataset $ds --seed 137 --n 20 \
      2>&1 | tee logs_v2/${cond}_${ds}_s137.log
    echo "  Done ${cond}_${ds}_s137 at $(date)" | tee -a $LOG
  done
done

# ─── Phase 3: Temperature ablation ──────────────────────────────────────────
echo ">>> PHASE 3: Temperature ablation" | tee -a $LOG
for ds in cifar10 cifar100; do
  python3 -u run_v2.py --temp-ablation --dataset $ds --seed 42 --n 20 \
    2>&1 | tee logs_v2/temp_${ds}.log
done
echo "  Done temp ablation at $(date)" | tee -a $LOG

# ─── Phase 4: Rank correlation ──────────────────────────────────────────────
echo ">>> PHASE 4: Rank correlation (20 vs 50 epochs)" | tee -a $LOG
for ds in cifar10 cifar100; do
  python3 -u run_v2.py --rank-correlation --dataset $ds --seed 42 \
    2>&1 | tee logs_v2/rank_${ds}.log
done
echo "  Done rank correlation at $(date)" | tee -a $LOG

# ─── Phase 5: Retrain top-5 with 3 seeds ────────────────────────────────────
echo ">>> PHASE 5: Retrain top-5 (3 seeds)" | tee -a $LOG
for ds in cifar10 cifar100; do
  python3 -u run_v2.py --retrain-top5 --dataset $ds \
    2>&1 | tee logs_v2/retrain_${ds}.log
done
echo "  Done retrain at $(date)" | tee -a $LOG

# ─── Phase 6: Analysis ──────────────────────────────────────────────────────
echo ">>> PHASE 6: Deep analysis" | tee -a $LOG
python3 -u deep_analysis_v2.py --results_dir results_v2 --output_dir figures_v2 \
  2>&1 | tee logs_v2/analysis.log
echo "  Done analysis at $(date)" | tee -a $LOG

echo "============================================================" | tee -a $LOG
echo "ALL V2 EXPERIMENTS COMPLETE — $(date)" | tee -a $LOG
echo "============================================================" | tee -a $LOG
