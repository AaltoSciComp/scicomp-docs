#!/bin/bash 
#SBATCH --time=00:30:00
#SBATCH --array=1-100
#SBATCH --mem=2G
#SBATCH --output=r_array_%a.out

module load matlab

srun matlab -nodisplay -r serial
