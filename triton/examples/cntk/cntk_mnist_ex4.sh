#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00

module load nvidia-cntk

# Create temporary directory to ramdisk
# export DATA_DIR=$(mktemp -d -p /dev/shm)

# OR

# Create temporary directory to $TMPDIR
export DATA_DIR=$(mktemp -d -p $TMPDIR)

echo 'Data dir is '$DATA_DIR

# Copy datasets to DATA_DIR
cp /scratch/scip/data/cntk/MNIST/*.txt $DATA_DIR

singularity_wrapper exec python cntk_mnist_ex4.py

# Remove old DATA_DIR
rm -r $DATA_DIR
