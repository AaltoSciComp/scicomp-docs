#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=500M
#SBATCH --job-name=pi-array-parameter
#SBATCH --output=pi-array-parameter_%a.out
#SBATCH --array=1-4

n=$SLURM_ARRAY_TASK_ID
iteration=`sed -n "${n} p" iterations.txt`      # Get n-th line (1-indexed) of the file
srun python3 slurm/pi.py ${iteration} > pi_iter_${iteration}.json
