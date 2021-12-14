#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=2G
#SBATCH --output=int_parallel.out

module load matlab
srun time -p matlab_multithread -nojvm -nosplash -r "int_parallel() ; exit(0)"
