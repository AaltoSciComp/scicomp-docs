Parallel Matlab with Matlab's internal parallelization
------------------------------------------------------

Matlab has internal parallelization that can be activated by setting
the number of OpenMP-threads in a 
:download:`Slurm script </triton/examples/matlab/int_parallel.slrm>` 
and using the `matlab_multithread` for starting the interpreter.

.. literalinclude:: /triton/examples/matlab/int_parallel.slrm

An example function is provided in 
:download:`this script </triton/examples/matlab/int_parallel.m>`

.. literalinclude:: /triton/examples/matlab/int_parallel.m
  :language: matlab
