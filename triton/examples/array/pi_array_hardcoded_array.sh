#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=500M
#SBATCH --job-name=pi-array-hardcoded-case
#SBATCH --output=pi-array-hardcoded-case_%a.out
#SBATCH --array=0-4

SEED_ARRAY=(
   123
   38
   22
   60
   432
)

SEED=${SEED_ARRAY[$SLURM_ARRAY_TASK_ID]}

srun python3 slurm/pi.py 2500000 --seed=$SEED > pi_$SEED.json
