#!/bin/bash
#SBATCH -t 00:10:00
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --mem=8G

module load singularity-openpose/v1.5.1

# Print out usage flags
singularity_wrapper exec openpose --help

# Run example
singularity_wrapper exec openpose --video /opt/openpose/examples/media/video.avi --display 0 --write_video $(pwd)/openpose.avi
