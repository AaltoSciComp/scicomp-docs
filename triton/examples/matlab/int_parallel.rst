Parallel Matlab with Matlab's internal parallelization
------------------------------------------------------

Matlab has internal parallelization that can be activated by requesting
more than one cpu per task in the
:download:`Slurm script </triton/examples/multilang/matlab/parallel_fun.sh>`.

.. literalinclude:: /triton/examples/multilang/matlab/parallel_fun.sh
   :language: slurm
   
An example function is provided in 
:download:`this script </triton/examples/multilang/matlab/parallel_fun.sh>`

.. literalinclude:: /triton/examples/multilang/matlab/parallel_fun.sh
  :language: matlab
