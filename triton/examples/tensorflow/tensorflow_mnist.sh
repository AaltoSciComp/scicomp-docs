#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00

module load scicomp-python-env

python tensorflow_mnist.py
