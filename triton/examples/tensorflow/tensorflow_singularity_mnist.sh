#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --mem=4G
#SBATCH --gpus=1

module load nvidia-tensorflow/20.02-tf1-py3

singularity_wrapper exec python tensorflow_mnist.py
