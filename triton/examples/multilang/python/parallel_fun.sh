#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=500M
#SBATCH --cpus-per-task=4
#SBATCH --output=ParallelOut

module load anaconda # use the normal anaconda environment for python
srun python parallel_fun.py

