#!/bin/bash
#SBATCH --time=00:5:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=500M
#SBATCH --output=r_parallel.out

# Set the number of OpenMP-threads to 1,
# as we're using parallel for parallelization
export OMP_NUM_THREADS=1

# Load the version of R you want to use
module load r

# Run your R script
srun Rscript parallel_fun.R
