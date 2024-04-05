#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=500M
#SBATCH --cpus-per-task=4
#SBATCH --output=ParallelOut

module load scicomp-python-env # use the normal scicomp environment for python
srun python parallel.py

