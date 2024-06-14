#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=3G
#SBATCH -o parpool_parallel.out

module load matlab

srun matlab -nodisplay -r "parpool_parallel($SLURM_CPUS_PER_TASK) ; exit(0)"
