#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00

module load nvidia-pytorch/20.02-py3

singularity_wrapper exec python pytorch_mnist.py
