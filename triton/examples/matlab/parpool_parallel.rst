Parallel Matlab with parpool
----------------------------

Often one uses Matlab's parallel pool for parallelization. When
using ``parpool`` one needs to specify the number of workers. This
number should match the number of CPUs requested. ``parpool`` uses
JVM so when launching the interpreter one needs to use ``-nodisplay``
instead of ``-nojvm``. Example 

.. admonition::Important note about parfor

   ``parfor`` has a quite big overhead. This can slow down your code a lot, 
   if inexpensive operations are put into a parfor loop. This is particularily 
   true if the operations inside the parfor loop are matrix operations, which are
   already parallelized in matlab. Doing those in a parfor loop is likely to 
   actually lead to a speed decrease, since the parfor overhead is added and 
   the internal parallelization of the operations shut down, or worse, interfering with
   each other. 
    
:download:`Slurm script </triton/examples/multilang/matlab/parallel.slurm>`:

.. literalinclude:: /triton/examples/multilang/matlab/parallel.slurm

An example function is provided in 
:download:`this script </triton/examples/multilang/matlab/parallel.m>`

.. literalinclude:: /triton/examples/multilang/matlab/parallel.m
  :language: matlab

