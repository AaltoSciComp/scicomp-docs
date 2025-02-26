When running a GPU job, you should check that the GPU is being fully
utilized.

When your job has started, you can ``ssh`` to the node and run
``nvidia-smi``. It should be close to 100%.

Once the job has finished, you can use ``slurm history`` to obtain the
``jobID`` and run::

   $ module load seff-gpu
   $ seff JOBID
   seff 5817422
   Job ID: 5817422
   Cluster: triton
   User/Group: tuomiss1/tuomiss1
   State: COMPLETED (exit code 0)
   Nodes: 1
   Cores per node: 2
   CPU Utilized: 00:08:25
   CPU Efficiency: 63.28% of 00:13:18 core-walltime
   Job Wall-clock time: 00:06:39
   Memory Utilized: 2.10 GB
   Memory Efficiency: 26.31% of 8.00 GB
   GPUs reserved: v100 (x1)
   GPU Utilized: 10%
   GPU VRAM Utilized: 15114 MB

Alternatively, you can run::

   $ sacct -j JOBID -o TRESUsageInAve -p
   cpu=00:08:24,energy=95240,fs/disk=147861134,gres/gpumem=15114M,gres/gpuutil=10,mem=2207116K,pages=3473,vmem=0|

This shows the GPU utilization.

In the example, you can see that the GPU utilization is low.

If this is the case you should check whether job's CPU utilization is close
to 100% with ``seff JOBID``. Having a high CPU utilization and a low GPU
utilization can indicate that the CPUs are trying to keep the GPU occupied
with calculations, but the workload is too much for the CPUs and thus GPUs
are not constantly working.

Increasing the number of CPUs you request can help, especially in tasks
that involve data loading or preprocessing, but your program must know how
to utilize the CPUs.

However, you shouldn't request too many CPUs: There wouldn't be enough CPUs
for everyone to use the GPUs and they would go to waste (all of our nodes
have 4-12 CPUs for each GPU).
