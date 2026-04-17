#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --gpus=1
#SBATCH --gres=min-cuda-cc:80

module load scicomp-pytorch-env/2026.1

python pytorch_mnist.py
