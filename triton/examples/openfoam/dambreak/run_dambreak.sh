#!/bin/bash -l
#SBATCH --time=00:05:00
#SBATCH --mem=4G
#SBATCH --ntasks=4
#SBATCH --output=damBreak.out

set -e

module load openfoam-org/9-openmpi-metis

cd damBreak

blockMesh
decomposePar

srun interFoam -parallel
