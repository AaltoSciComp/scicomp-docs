#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=500M
#SBATCH --job-name=pi-array-hardcoded
#SBATCH --output=pi-array-hardcoded_%a.out
#SBATCH --array=0-4

case $SLURM_ARRAY_TASK_ID in
   0)  SEED=123 ;;
   1)  SEED=38  ;;
   2)  SEED=22  ;;
   3)  SEED=60  ;;
   4)  SEED=432 ;;
esac

srun python3 slurm/pi.py 2500000 --seed=$SEED > pi_$SEED.json
