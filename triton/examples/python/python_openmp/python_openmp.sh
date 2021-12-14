#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1G
#SBATCH -o python_openmp.out

module load anaconda/2020-03-tf2

export OMP_PROC_BIND=true

echo 'Running on: '$HOSTNAME

srun python python_openmp.py
