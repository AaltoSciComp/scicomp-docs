==================
Parallel computing
==================

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=z-F25Er_-tw&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=19>`__

Parallel computing is what HPC is really all about: processing things on
more than one processor at once. By now, you should have read all of the previous
tutorials.

.. highlight:: bash



Parallel programming models
---------------------------

Parallel programming is used to create programs that can execute
instructions on multiple processors at a same time. Most of our users that
run their programs in parallel utilize existing parallel execution features
that are present in their programs and thus do not need to learn how to create
parallel programs. But even when one is running programs in parallel,
it is important to understand different models of parallel execution.

The two main models are:

* Shared memory (or multithreaded/multiprocess) programs run multiple
  independent workers on the same machine. As the name suggests, all of
  the computer's memory has to be accessible to all of the processes.
  **Thus programs that utilize this model should request one node,
  one task and multiple CPUs.**
  Likewise, the maximum number of workers is usually the number of CPU cores
  available on the computational node. The code is easier to implement
  and the same   code can still be run in a serial mode. Example applications
  that utilize this model: Matlab, R, Python multithreading/multiprocessing,
  OpenMP applications, BLAS libraries, FFTW libraries, typical
  multithreaded/multiprocess parallel desktop programs.

* Message passing programming (e.g. MPI, message passing interface)
  can run on multiple nodes interconnected with the network via passing
  data through MPI software libraries. Almost all large-scale scientific
  programs utilize MPI. MPI can scale to thousands of CPU cores, but
  depending on the case it can be harder to implement from the
  programmer's point of view. **Programs that utilize this model should
  request single/multiple nodes with multiple tasks each. You should
  not request multiple CPUs per task.** Example applications that utilize this
  model: CP2K, GPAW, LAMMPS, OpenFoam.

Both models, MPI and shared memory, can be combined in one application, in
this case we are talking about hybrid parallel programming model.
**Programs that utilize this model can require both multiple tasks
and multiple CPUs per task.**

Most historical scientific code is MPI, but these days more and more
people are using shared memory models.

.. important::

   Normal serial code can't just be run in parallel without
   modifications. As a user it is your responsibility to
   understand what parallel model implementation your code has, if any.

   When deciding whether using parallel programming is worth
   the effort, one should be mindful of
   `Amdahl's law <https://en.wikipedia.org/wiki/Amdahl%27s_law>`_ and
   `Gustafson's law <https://en.wikipedia.org/wiki/Gustafson%27s_law>`_.
   All programs have some parts that can only be executed in serial and
   thus the theoretical speedup that one can get from using parallel
   programming depends on two factors:

     1. How much of programs' execution could be done in parallel?
     2. What would be the speedup for that parallel part?

   Thus if your program runs mainly in serial but has a small parallel
   part, running it in parallel might not be worth it. Sometimes, doing
   data parallelism with e.g. :doc:`array jobs <array>` is much more
   fruitful approach.

   Another important note regarding parallelism is that all the applications
   scale good up to some upper limit which depends on application implementation,
   size and type of problem you solve and some other factors. The best practice
   is to benchmark your code on different number of CPU cores before
   you start actual production runs.

   **If you want to run some program in parallel, you have to know
   something about it - is it shared memory or MPI?  A program doesn't
   magically get faster when you ask more processors if it's not designed
   to.**



Shared memory: OpenMP/multithreaded/multiprocess
------------------------------------------------

Diffence between multithreaded and multiprocess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shared memory programs usually parallelize by using multiple threads or
processes. Processes are individual program executions while threads are
basically smaller program executions within a process. Processes can
launch both subprocesses and threads. Slurm reservations for both methods
behave similarly.

Depending on a program, you might have multiple processes (Matlab parallel
pool, R parallel-library, Python multiprocessing) or have multiple threads
(OpenMP threads of BLAS libraries that R/numpy use).

.. warning::

   Some programs (e.g. R) can utilize both multithread and multiprocess
   parallelism. For example, R has parallel-library for running multiple
   processes, but BLAS libraries that R uses can utilize multiple threads.
   If you encounter bad performace when you use parallel processes
   try setting ``OMP_NUM_THREADS=1`` in your slurm script.

Running multithreaded/multiprocess applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic slurm option that specifies how many CPUs your job requires is
``--cpus-per-task=N`` (or ``-c N``). If your memory requirement scales
with the number of cores, use ``--mem-per-core=M``, if you
require a fixed amount of memory (per node regardless of number of
processors), use ``--mem=M``. We recommend starting with ``--mem=M`` if
you do not know how your problem scales.

.. important::

   The number of threads/processes you launch should match the
   number of requested processors. If you create a lower number, you will
   not utilize all CPUs. If you launch a larger number, you will
   oversubscribe the CPUs and the code will run slower as different
   threads/processes will have to swap in/out of the CPUs.

.. warning::

   Normally you should **not** use ``--ntasks=N`` when you want to
   run shared memory codes. The number of tasks is only relevant to MPI codes
   and by specifying it you might launch multiple copies of your program
   that all compete on the reserved CPUs.

   Only hybrid parallelization codes should have both ``--ntasks=N`` and
   ``--cpus-per-task=C`` set to be greater than one.

Running a typical OpenMP program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenMP is a standard de facto for the multithreading implementations. There
are many others, but this one is the most common, supported by all known
compiler suits. For other implementations of shared memory parallelism,
please consult your code docs.

Let's consider
`hello_omp-example <https://github.com/AaltoSciComp/hpc-examples/tree/master/openmp/hello_omp>`_
from HPC examples repository.

Simple code compiling::

  wget https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/openmp/hello_omp/hello_omp.c
  module load gcc/9.2.0
  gcc -fopenmp -O2 -g hello_omp.c -o hello_omp

Running an OpenMP code::

  export OMP_PROC_BIND=TRUE
  module load gcc/9.2.0
  srun --cpus-per-task=4 --mem=500M --time=00:05:00 hello_omp

The
:download:`slurm script<https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/openmp/hello_omp/hello_omp.slrm>`
will look similar:

.. literalinclude:: /triton/examples/openmp/hello_omp/hello_omp.slrm
   :language: slurm

It is good to know that OpenMP is both an environment and set of libraries, but
those libraries always come as part of the compiler. Thus during runtime
you should load the same compiler that you used for compiling the code.

.. include:: /triton/examples/python/python_openmp/python_openmp.rst


Message passing programs: MPI
-----------------------------

For compiling/running an MPI job one has to pick up one of the MPI library
suites. There are various different MPI libraries that all implement the
MPI standard. We recommend that you use either:

  - OpenMPI (e.g. ``openmpi/3.1.4``)
  - Intel's MPI (e.g. ``intel-parallel-studio/cluster.2020.0-intelmpi``)

Some libraries/programs might have already existing requirement for a certain
MPI version. If so, use that version or ask for administrators to create
a version of the library with dependency on the MPI version you require.

.. warning::

   Different versions of MPI are not compatible with each other. Each
   version of MPI will create code that will run correctly with only
   that version of MPI. Thus if you create code with a certain version,
   you will need to load the same version of the library when you are
   running the code.

   Also, the MPI libraries are usually linked to slurm and network
   drivers. Thus, when slurm or driver versions are updated, some
   older versions of MPI might break. If you're still using said
   versions, let us know. If you're just starting a new project, it
   is recommended to use our recommended MPI libraries.

For basic use of MPI programs, you will need to use the
``-n N``/``--ntasks=N``-option to specify the number of MPI workers.

Running a typical MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following use ``hpc-examples`` from
:ref:`the previous exercises <triton-tut-exercise-repo>`.

Loading module::

  # GCC + OpenMPI
  module load gcc/9.2.0      # GCC
  module load openmpi/3.1.4  # OpenMPI

  # Intel compilers + Intel's MPI
  module load intel-parallel-studio/cluster.2019.3-intelmpi

Compiling the code (depending on module and language)::

  # OpenMPI
  mpicc    -O2 -g hello_mpi.c -o hello_mpi # C code
  mpifort  -O2 -g hello_mpi_fortran.f90 -o hello_mpi_fortran # Fortran code

  # Intel MPI
  mpiicc   -O2 -g hello_mpi.c -o hello_mpi # C code
  mpiifort -O2 -g hello_mpi_fortran.f90 -o hello_mpi_fortran # Fortran code

Running the program with srun (for testing)::

  srun --time=00:05:00 --mem-per-cpu=200M --ntasks=4 ./hello_mpi

Running an MPI code in the batch mode:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --ntasks=4           # 4 processes
  #SBATCH --constraint=avx     # set constraint for processor architecture

  module load openmpi/3.1.4  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi

Triton has multiple architectures around (12, 20, 24, 40 CPU cores per node),
even though SLURM optimizes resources usage and allocate CPUs within one node,
which gives better performance for the app, it still makes sense to put
constraints explicitly.

.. important::

   It is important to use ``srun`` when you launch your program.
   This allows for the MPI libraries to obtain task placement information
   (nodes, number of tasks per node etc.) from the slurm queue.

Spreading MPI workers evenly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases you might require more than one node during your job's runtime.

When this is the case, it is usually recommended to split the number of
workers somewhat evenly among the nodes. To do this, one can use
``-N N``/``--nodes=N`` and ``--ntasks-per-node=n``. For example, the previous example
could be written as:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=2            # 2 nodes
  #SBATCH --ntasks-per-node=2  # 2 processes per node * 2 nodes = 4 processes in total
  #SBATCH --constraint=avx     # set constraint for processor architecture

  module load openmpi/3.1.4  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi

This way the number of workers is distributed more evenly, which in turn
reduces communication overhead between workers.



Monitoring performance
----------------------

You can use the ``seff`` program (with a jobid) to list what percent
of available processors and memory you used.  If your processor usage
is far below 100%, your code may not be working correctly in a parallel
environment. If your memory usage is far below 100%, you might have a
problem with your requirements.

.. important::

   When making job reservations it is important to distinguish
   between requirements for the whole job (such as ``--mem``) and
   requirements for **each individual task/cpu** (such as ``--mem-per-cpu``).
   E.g. requesting ``--mem-per-cpu=2G`` with ``--ntasks=2`` and ``--cpus-per-task=4``
   will create a total memory reservation of
   (2 tasks)*(4 cpus / task)*(2GB / cpu)=16GB.



Exercises
---------

1. Run ``srun --cpus-per-task=4 hostname``, ``srun --ntasks=4 hostname``, and ``srun --nodes=4
   hostname``.  What's the difference and why?

The following use ``hpc-examples`` from :ref:`the previous exercises <triton-tut-exercise-repo>`:

2. Find the files ``hpc-examples/openmp/hello_omp/hello_omp.c`` and
   ``hpc-examples/hello_omp/hello_omp.slrm`` that have a short example of OpenMP.
   Compile and run it - a slurm script is included.

3. Find the files in ``hpc-examples/python/python_openmp``. Try running the
   example with a few different ``--constraint=X`` and ``--cpus-per-task=C``.
   In your opinion, what architecture / cpu number combination would provide the
   best efficiency? Use ``seff`` to verify.

4. Find the files ``hpc-examples/mpi/hello_mpi/hello_mpi.c`` and
   ``hpc-examples/mpi/hello_mpi/hello_mpi.slrm`` that
   have a short example of MPI.
   Compile and run it - a slurm script is included.



Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`
