You can use ``seff JOBID`` to see what percent of available CPUs and RAM was
utilized. Example output is given below::

  $ seff 60985042
  Job ID: 60985042
  Cluster: triton
  User/Group: tuomiss1/tuomiss1
  State: COMPLETED (exit code 0)
  Nodes: 1
  Cores per node: 2
  CPU Utilized: 00:00:29
  CPU Efficiency: 90.62% of 00:00:32 core-walltime
  Job Wall-clock time: 00:00:16
  Memory Utilized: 1.59 MB
  Memory Efficiency: 0.08% of 2.00 GB

If your processor usage is far below 100%, your code may not be working
correctly. If your memory usage is far below 100% or above 100%, you might
have a problem with your RAM requirements. You should set the RAM limit to
be a bit above the RAM that you have utilized.

You can also monitor individual job steps by calling ``seff`` with the syntax
``seff JOBID.JOBSTEP``.

.. important::

   When making job reservations it is important to distinguish
   between requirements for the whole job (such as ``--mem``) and
   requirements for **each individual task/cpu** (such as ``--mem-per-cpu``).
   E.g. requesting ``--mem-per-cpu=2G`` with ``--ntasks=2`` and ``--cpus-per-task=4``
   will create a total memory reservation of
   (2 tasks)*(4 cpus / task)*(2GB / cpu)=16GB.
