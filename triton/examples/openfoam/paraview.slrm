#!/bin/bash
#SBATCH -p short
#SBATCH -t 00:10:00
#SBATCH -n 1
#SBATCH --mem=8G

module use /share/apps2/singularity/modules
module purge
module load OpenFOAM

singularity_wrapper exec paraview
