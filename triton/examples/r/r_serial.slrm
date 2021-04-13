#!/bin/bash -l
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --mem=100M
#SBATCH --output=r_serial.out

module load r
n=3
m=2
srun Rscript --vanilla r_serial.R $n $m
