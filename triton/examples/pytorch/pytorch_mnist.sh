#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --gpus=1

module load scicomp-python-env

python pytorch_mnist.py
