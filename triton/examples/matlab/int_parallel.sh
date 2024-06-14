#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=3G
#SBATCH --output=int_parallel.out

module load matlab
srun time -p matlab -nojvm -nosplash -r "int_parallel() ; exit(0)"
