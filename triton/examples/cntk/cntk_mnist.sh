#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --gpus=1

module load nvidia-cntk

singularity_wrapper exec python cntk_mnist.py
