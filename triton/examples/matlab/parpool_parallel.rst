Parallel Natlab with parpool
----------------------------

Often one uses Matlab's parallel pool for parallelization. When
using ``parpool`` one needs to specify the number of workers. This
number should match the number of CPUs requested. ``parpool`` uses
JVM so when launching the interpreter one needs to use ``-nodisplay``
instead of ``-nojvm``. Example 
:download:`Slurm script </triton/examples/matlab/parpool_parallel.slrm>`:

.. literalinclude:: /triton/examples/matlab/parpool_parallel.slrm

An example function is provided in 
:download:`this script </triton/examples/matlab/parpool_parallel.m>`

.. literalinclude:: /triton/examples/matlab/parpool_parallel.m
  :language: matlab

