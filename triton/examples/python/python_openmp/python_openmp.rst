Running Python with OpenMP parallelization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Various Python packages such as Numpy, Scipy and pandas can utilize OpenMP
to run on multiple CPUs. As an example, let's run the python script
:download:`python_openmp.py<https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/python/python_openmp/python_openmp.py>`
that calculates multiplicative inverse of five symmetric matrices of
size 2000x2000.

.. literalinclude:: /triton/examples/python/python_openmp/python_openmp.py
   :lines: 8-19
   :language: python

The full code for the example is in
`HPC examples-repository <https://github.com/AaltoSciComp/hpc-examples>`_.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/python/python_openmp/python_openmp.py
  module load scicomp-python-env
  export OMP_PROC_BIND=true
  srun --cpus-per-task=2 --mem=2G --time=00:15:00 python python_openmp.py

or with ``sbatch`` by submitting
:download:`python_openmp.sh<https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/python/python_openmp/python_openmp.sh>`:

.. literalinclude:: /triton/examples/python/python_openmp/python_openmp.sh
   :language: slurm

.. important::

   Python has a global interpreter lock (GIL), which forces some operations to
   be executed on only one thread and when these operations are occuring, other
   threads will be idle. These kinds of operations include reading files and
   doing print statements. Thus one should be extra careful with multithreaded
   code as it is easy to create seemingly parallel code that does not actually
   utilize multiple CPUs.

   There are ways to minimize effects of GIL on your Python code and if you're
   creating your own multithreaded code, we recommend that you take this into
   account.
