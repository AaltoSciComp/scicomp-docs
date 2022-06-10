#!/bin/bash -l
#SBATCH --time=00:05:00
#SBATCH --mem=500M
#SBATCH --cpus-per-task=4
#SBATCH --output=hello_omp.out

module load gcc/8.4.0

export OMP_PROC_BIND=true
srun hello_omp
