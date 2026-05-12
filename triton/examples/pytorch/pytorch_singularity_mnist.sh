#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --gpus=1

module load nvidia-pytorch/20.02-py3

singularity_wrapper exec python pytorch_mnist.py
