When running a GPU job, you should check that the GPU is being fully
utilized.

When your job has started, you can ``ssh`` to the node and run
``nvidia-smi``. You can find your process by e.g. using ``htop``
and inspect the ``GPU-Util`` column. It should be close to 100%.

Once the job has finished, you can use ``slurm history`` to obtain the
``jobID`` and run::

   $ sacct -j JOBID -o comment -p
   {"gpu_util": 99.0, "gpu_mem_max": 1279.0, "gpu_power": 204.26, "ncpu": 1, "ngpu": 1}|


This also shows the GPU utilization.

.. note::

   There are factors to be considered regarding efficient use of GPUs.
   For instance, is your code itself efficient enough? Are you using the
   framework pipelines in the intended fashion? Is it only using GPU
   for a small portion of the entire task?  `Amdahl's law
   <https://en.wikipedia.org/wiki/Amdahl's_law>`__ of parallelization
   speedup is relevant here.

If the GPU utilization of your job is low, you should check whether
its CPU utilization is close to 100% with ``seff JOBID``. This can
indicate that the CPUs are trying to keep the GPU occupied with calculations,
but the lack of CPU performance will cause a bottleneck on the GPU
utilization.

Please keep in mind that when using a GPU, you need to also
request enough CPUs to supply the data to the process.
So, you can increase the number of CPUs you request so that
enough data is provided for the GPU. However, you shouldn't request
too many: There wouldn't be enough CPUs for everyone to use the GPUs,
and they would go to waste (all of our nodes have 4-6 CPUs for each GPU).
