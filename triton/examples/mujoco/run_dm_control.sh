#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --mem=2G
#SBATCH --cpus-per-task=1

module purge
module load triton-dev/spack
module load mujoco/2.1.1  mesa/21.2.3-opengl-osmesa-python3-llvm gcc/8.4.0 anaconda

# Use OSMesa for rendering
export MUJOCO_GL="osmesa"
# Use faster llvmpipe for rendering
export GALLIUM_DRIVER=llvmpipe

# Set path to mujoco library
export MJLIB_PATH="$MUJOCO_ROOT/lib/libmujoco.so"

python test_osmesa.py

