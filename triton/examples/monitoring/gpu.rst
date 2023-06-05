When running a GPU job, you should check that the GPU is being fully
utilized.

When your job has started, you can ``ssh`` to the node and run
``nvidia-smi``. It should be close to 100%.

Once the job has finished, you can use ``slurm history`` to obtain the
``jobID`` and run::

   $ sacct -j JOBID -o comment -p
   {"gpu_util": 99.0, "gpu_mem_max": 1279.0, "gpu_power": 204.26, "ncpu": 1, "ngpu": 1}|


This also shows the GPU utilization.

If the GPU utilization of your job is low, you should check whether
its CPU utilization is close to 100% with ``seff JOBID``. Having a high
CPU utilization and a low GPU utilization can indicate that the CPUs are
trying to keep the GPU occupied with calculations, but the workload
is too much for the CPUs and thus GPUs are not constantly working.

Increasing the number of CPUs you request can help, especially in tasks
that involve data loading or preprocessing, but your program must know how
to utilize the CPUs.

However, you shouldn't request too many CPUs: There wouldn't be enough CPUs
for everyone to use the GPUs and they would go to waste (all of our nodes
have 4-12 CPUs for each GPU).
