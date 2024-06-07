#!/bin/bash 
#SBATCH --time=00:15:00
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=4
#SBATCH --output=matlab_parallel.out

module load matlab

srun matlab -nodisplay -r parallel
