#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --array=1-100
#SBATCH --mem=500M
#SBATCH --output=r_array_%a.out

# Load the version of R you want to use
module load r

# Run your R script
srun Rscript serial.r
