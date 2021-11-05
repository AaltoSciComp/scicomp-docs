Parallel Matlab with Matlab's internal parallelization
------------------------------------------------------

Matlab has internal parallelization that can be activated by requesting
more than one cpu per task in the
:download:`Slurm script </triton/examples/multilang/matlab/parallel_fun.slurm>` 
and using the ``matlab_multithread`` to start the interpreter.

.. literalinclude:: /triton/examples/multilang/matlab/parallel_fun.slurm
   :language: slurm
   
An example function is provided in 
:download:`this script <//triton/examples/multilang/matlab/parallel_fun.slurm>`

.. literalinclude:: /triton/examples/multilang/matlab/parallel_fun.slurm
  :language: matlab
