#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --ntasks=4
#SBATCH --mem=4G

module use /share/apps2/singularity/modules
module purge
module load OpenFOAM

srun singularity_wrapper exec interFoam -parallel
