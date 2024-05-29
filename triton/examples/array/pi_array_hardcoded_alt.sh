#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=500M
#SBATCH --job-name=pi-array-hardcoded
#SBATCH --output=pi-array-hardcoded_%a.out
#SBATCH --array=0-4

SEEDS=(123 38 22 60 432)
SEED=${SEEDS[SLURM_ARRAY_TASK_ID]}

srun python slurm/pi.py 2500000 --seed=$SEED > pi_$SEED.json
