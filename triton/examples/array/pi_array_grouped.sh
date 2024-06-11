#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=500M
#SBATCH --job-name=pi-array-grouped
#SBATCH --output=pi-array-grouped_%a.out
#SBATCH --array=1-4

# Lets create a new folder for our output files
mkdir -p json_files

CHUNKSIZE=10
n=$SLURM_ARRAY_TASK_ID
indexes=`seq $((n*CHUNKSIZE)) $(((n + 1)*CHUNKSIZE - 1))`

for i in $indexes
do
   srun python3 slurm/pi.py 1500000 --seed=$i > json_files/pi_$i.json
done
