#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --array=1-100
#SBATCH --mem=500M
#SBATCH --output=python_array_%a.out


module load anaconda # use the normal anaconda environment for python

srun python serial.py

