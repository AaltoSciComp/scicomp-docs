#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00

module load nvidia-tensorflow/20.02-tf1-py3

singularity_wrapper exec python tensorflow_mnist.py
