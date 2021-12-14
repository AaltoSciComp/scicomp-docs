#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=2G
#SBATCH --output=r_openmp.out

module load r
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
time srun Rscript --default-packages=methods,utils,stats R-benchmark-25.R
