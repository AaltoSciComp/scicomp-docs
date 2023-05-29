====================================
MPI parallelism: multi-task programs
====================================

.. _parallel-mpi:

.. admonition:: Abstract

   * You need to figure out what parallelization paradigm your program
     uses, otherwise you won't know which options to use.

     * Embarrassingly parallel: use :doc:`array jobs <array>`.
     * Multithreaded (OpenMP) or multiple processes (like Python's
       multiprocessing): use :doc:`shared memory parallelism <parallel-shared>`.
     * MPI: compile to link with our Slurm and MPI libraries,
       use ``--ntasks=n`` and always use ``srun`` to launch your job.
       ``module load`` a MPI version for both compiling and running.

   * You must always :doc:`monitor jobs <monitoring>` to make sure they are using all the
     resources you request (``seff JOBID``).
   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.

Message passing programs: MPI
-----------------------------

For compiling/running an MPI job one has to pick up one of the MPI library
suites. There are various different MPI libraries that all implement the
MPI standard. We recommend that you use our OpenMPI installation
(``openmpi/4.0.5``). For information on other installed versions, see the
:doc:`MPI applications-page<../apps/mpi>`.

.. include:: /triton/ref/mpi-warning.rst

For basic use of MPI programs, you will need to use the
``-n N``/``--ntasks=N``-option to specify the number of MPI workers.


Compiling and running an MPI Hello world-program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /triton/examples/mpi/hello.rst


Spreading MPI workers evenly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases you might require more than one node during your job's runtime.

When this is the case, it is usually recommended to split the number of
workers evenly among the nodes. To do this, one can use
``-N N``/``--nodes=N`` and ``--ntasks-per-node=n``. For example, you could
distribute the previously requested four tasks to two nodes with:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=2            # 2 nodes
  #SBATCH --ntasks-per-node=2  # 2 processes per node * 2 nodes = 4 processes in total
  #SBATCH --constraint=avx     # set constraint for processor architecture

  module load openmpi/4.0.5  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi


This way the number of workers is distributed more evenly, which in turn
reduces communication overhead between workers. The total number of tasks is
``--nodes`` times the ``--ntasks-per-node``.


Setting a constraint for a specific CPU architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of CPUs/tasks one can specify for a single parallel job depends
usually on the underlying algorithm. In many codes, such as many
finite-difference codes, the workers are set in a grid-like structure. The user
of said codes has then a choice of choosing the dimensions of the simulation
grid aka. how many workers are in x-, y-, and z-dimensions.

For best perfomance one should reserve half or full nodes when possible. In
heterogeneous clusters this can be a bit more complicated as different CPUs
can have different numbers of cores.

In Triton CPU partitions there are machines with 24, 28 and 40 CPUs. See the
list of :ref:`available nodes<hardware-list>` for more information.

However, one can make the reservations easier by specifying a CPU architecture
with ``--constraint=ARCHITECTURE``. This tells Slurm to look for nodes that
satisfy a specific feature. To list available features, one can use
``slurm features``.

For example, one could limit the code to the Haswell-architecture with the
following script:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=1            # 1 node
  #SBATCH --ntasks-per-node=24 # 24 processes as that is the number in the machine
  #SBATCH --constraint=hsw     # set constraint for processor architecture

  module load openmpi/4.0.5  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi

Monitoring performance
----------------------

.. include:: ../examples/monitoring/seff.rst

Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Parallel-1: Explore and understand basic Slurm options

   Run ``srun --cpus-per-task=4 hostname``, ``srun --ntasks=4 hostname``, and ``srun --nodes=4
   hostname``.  What's the difference and why?

.. exercise:: Parallel-2: OpenMP with Python

   Find the files ``hpc-examples/openmp/hello_omp/hello_omp.c`` and
   ``hpc-examples/hello_omp/hello_omp.sh`` that have a short example of OpenMP.
   Compile and run it - a Slurm script is included.

.. exercise:: Parallel-3: OpenMP

   Find the files in ``hpc-examples/python/python_openmp``. Try running the
   example with a few different ``--constraint=X`` and ``--cpus-per-task=C``.
   In your opinion, what architecture / cpu number combination would provide the
   best efficiency? Use ``seff`` to verify.

.. exercise:: Parallel-4: MPI

   Find the files ``hpc-examples/mpi/hello_mpi/hello_mpi.c`` and
   ``hpc-examples/mpi/hello_mpi/hello_mpi.sh`` that
   have a short example of MPI.
   Compile and run it - a Slurm script is included.



See also
--------

* The :doc:`Research Software Engineers </rse/index>` can help in all
  aspects of parallel computing - we'd recommend anyone getting to
  this point set up a consultation to make sure your work is as
  efficient as it can be.



What's next?
------------


The next tutorial is about :doc:`shared memory parallelism <parallel-shared>`.
