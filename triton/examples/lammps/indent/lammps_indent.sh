#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=2G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --output=lammps_indent.out


# Load modules used for building the LAMMPS binary
module load cmake gcc/8.4.0 openmpi/4.0.5 fftw/3.3.10-openmpi-openmp openblas/0.3.17-openmp eigen/3.4.0 ffmpeg/4.3.2  voropp/0.4.6 zstd/1.5.0

# Set path to LAMMPS executable
export PATH=$PATH:$PWD/../../../lammps-mpi-most-23Jun2022/bin

# Run simulation
srun lmp < in.indent
