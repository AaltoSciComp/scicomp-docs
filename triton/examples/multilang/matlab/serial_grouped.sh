#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --array=1-10
#SBATCH --mem=3G
#SBATCH --output=matlab_array_%a.out


module load matlab



# size of each batch
BATCHSIZE=10
n=$SLURM_ARRAY_TASK_ID

# generate the sequence of indices used by each batch
indexes=`seq $((n*BATCHSIZE)) $(((n + 1)*BATCHSIZE - 1))`

# run your program for each value
for i in $indexes
do
   export i #to access i within the python interpreter we need to export it.
   srun matlab -nodisplay -r serial_array
done



