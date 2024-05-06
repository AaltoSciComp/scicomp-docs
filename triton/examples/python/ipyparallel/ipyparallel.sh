#!/bin/bash
#SBATCH --nodes=4

module load scicomp-python-env
set -x

ipcontroller --ip="*" &
sleep 5
# Run the engines in slurm job steps (makes four of them, since we use
# the --nodes=4 slurm option)...
srun ipengine --location=$(hostname -f) &

sleep 5
# Put the actual Python isn't in a job step.  This is assuming that
# most work happens in engines
python3 <<EOF
import os
import ipyparallel
client = ipyparallel.Client()
result = client[:].apply_async(os.getpid)
pid_map = result.get_dict()
print(pid_map)
EOF
