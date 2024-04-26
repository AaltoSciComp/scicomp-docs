#!/bin/bash
#SBATCH --cpus-per-task 1       # The number of CPUs your code can use, if in doubt, use 1 for CPU only code or 6 if you run on GPUs (since code running on GPUs commonly allows parallelization of data provision to the GPU)
#SBATCH --mem 10G               # The amount of memory you expect your code to need. Format is 10G for 10 Gigabyte, 500M for 500 Megabyte etc
#SBATCH --time=01:00:00         # Time in HH:MM:SS or DD-HH of your job. the maximum is 120 hours or 5 days.
#SBATCH --gres=gpu:1            # Additional specific ressources can be requested via gres. Mainly used for requesting GPUs format is: gres=RessourceType:Number
module load python-scicomp-env  # or `module load mamba` if you use your own environment.
source activate yourEnvironment # if you use your own environment
python yourScriptName.py ARG    
