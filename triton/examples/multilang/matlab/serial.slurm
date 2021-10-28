#!/bin/bash 
#SBATCH --time=00:30:00
#SBATCH --array=1-100
#SBATCH --mem=500M
#SBATCH --output=r_array_%a.out

module load matlab

srun matlab -nodisplay -r serial
