#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks=4

module load Python/2.7.11-goolf-triton-2016b
mpiexec -n $SLURM_NTASKS python mpi4py.py
