#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=200M
#SBATCH --output=array_example_%A_%a.out
#SBATCH --array=0-15

# You may put the commands below:

# Job step
srun echo "I am array task number" $SLURM_ARRAY_TASK_ID
