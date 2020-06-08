==================
Parallel computing
==================

Parallel computing is what HPC is really all about: processing things on
more than one processor at once. By now, you should have read all of the previous
tutorials.

Parallel programming models
---------------------------

Parallel programming is used to create programs that can execute
instructions on multiple processors at a same time. Most of our users that
run their programs in parallel utilize existing parallel execution features
that are present in their programs and thus do not need to learn how to create
parallel programs. But even when one is running programs in parallel,
it is important to understand different models of parallel execution.

The two main models are:

* Shared memory (or multithreaded) programs run multiple independent
  workers on the same machine. As the name suggests, all of the computer's
  memory has to be accessible to all of the processes. **Thus programs
  that utilize this model are limited to one node only.** Likewise, the
  maximum number of workers is usually the number of CPU cores available
  on the computational node. The code is easier to implement and the same
  code can still be run in a serial mode. Example applications that
  utilize this model: Matlab, R, Python multithreading/multiprocessing,
  OpenMP applications, BLAS libraries, FFTW libraries, typical
  multithreaded parallel pesktop programs.

* Message passing programming (e.g. MPI, message passing interface)
  can run on multiple nodes interconnected with the network via passing
  data through MPI software libraries. Almost all large-scale scientific
  programs utilize MPI. MPI can scale to thousands of CPU cores, but
  depending on the case it can be harder to implement from the
  programmer's point of view. Example applications that utilize this
  model: CP2K, GPAW, LAMMPS, OpenFoam.

Both models, MPI and shared memory, can be combined in one application, in
this case we are talking about hybrid parallel programming model.

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

Shared memory: OpenMP/multithreaded
-----------------------------------

OpenMP is a standard de facto for the multithreading implementations. There
are many others, but this one is the most common, supported by all known
compiler suits. For other implementations of shared memory parallelism,
please consult your code docs.

Running a typical OpenMP program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simple code compiling::

  gcc -fopenmp -O2 -g omp_program.c -o omp_program

Running an OpenMP code::

  export OMP_PROC_BIND=TRUE
  srun --cpus-per-task=4 --mem-per-cpu=2000 --time=00:30:00 omp_program

The basic slurm options you need are ``--cpus-per-task=N`` (or ``-c N``) to specify the number of
cores to use within one node.  If your memory needs scale with the number of cores,
use ``--mem-per-core=``, if you require a fixed amount of memory (per
node regardless of number of processors), use ``--mem``.

The SLURM batch file will look similar::

  #!/bin/bash -l
  #SBATCH --cpus-per-task=4
  #SBATCH  --mem-per-cpu=2000
  #SBATCH --time=00:30:00

  export OMP_PROC_BIND=TRUE
  srun omp_program

Good to know that OpenMP is both an environment and set of libraries, but
those libraries always come as part of the compiler. Thus during runtime
you should load the same compiler that you used for compiling the code.

.. warning::

   Normally you should **not** use ``--ntasks=N`` when you want to
   run shared memory codes. The number of tasks is only relevant to MPI codes
   and by specifying it you might launch multiple copies of your program
   that all compete on the reserved CPUs.

   Only hybrid parallelization codes should have both ``--ntasks=N`` and
   ``--cpus-per-task=C`` set to be greater than one.

Other programs and multithreading
---------------------------------

Some programs use multiple threads for their parallel computations. A good
example of this kind of program is MATLAB, that user parallel pool of workers;
or R, which uses the ``parallel``-package for its parallel applys.
Threaded applications behave similarly to OpenMP applications in that one
needs to specify the number of cores per task and amount of memory per core.

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

   Also, the MPI libraries are usually linked to Slurm and network
   drivers. Thus, when Slurm or driver versions are updated, some
   older versions of MPI might break. If you're still using said
   versions, let us know. If you're just starting a new project, it
   is recommended to use our recommended MPI libraries.

For basic use of MPI programs, you will need to use the
``-n N``/``--ntasks=N``-option to specify the number of MPI workers.

Running a typical MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loading module::

  module load gcc/9.2.0      # GCC
  module load openmpi/3.1.4  # OpenMPI

Compiling the code (depending on module and language)::

  mpifort  -O2 -g mpi_prog.f -o mpi_prog # OpenMPI   + Fortran code
  mpicc    -O2 -g mpi_prog.c -o mpi_prog # OpenMPI   + C code
  mpiifort -O2 -g mpi_prog.f -o mpi_prog # Intel MPI + Fortran code
  mpiicc   -O2 -g mpi_prog.c -o mpi_prog # Intel MPI + C code

Running an MPI code in the batch mode::

  #!/bin/bash
  #SBATCH -n 16                # 16 processes
  #SBATCH --constraint=avx     # run on nodes with AVX instructions
  #SBATCH --time=04:00:00      # takes 4 hours all together
  #SBATCH --mem-per-cpu=2000   # 2GB per process

  module load openmpi/3.1.4  # NOTE: should be the same as you used to compile the code
  srun ./mpi_prog


Triton has multiple architectures around (12, 20, 24, 40 CPU cores per node),
even though SLURM optimizes resources usage and allocate CPUs within one node,
which gives better performance for the app, it still makes sense to put
constraints explicitly.

Spreading MPI workers evenly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases you might require more than one node during your job's runtime.

When this is the case, it is usually recommended to split the number of
workers somewhat evenly among the workers. To do this, one can use
``-N N``/``--nodes=N`` and ``--ntasks-per-node=n``. For example, the previous example
could be written as::

  #!/bin/bash
  #SBATCH --nodes=2            # 2 nodes
  #SBATCH --ntasks-per-node=8  # 8 processes per node * 2 nodes = 16 processes in total
  #SBATCH --constraint=avx     # run on nodes with AVX instructions
  #SBATCH --time=04:00:00      # takes 4 hours all together
  #SBATCH --mem-per-cpu=2000   # 2GB per process

  module load openmpi/3.1.4  # NOTE: should be the same as you used to compile the code
  srun ./mpi_prog

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

1. Run ``srun -c 4 hostname``, ``srun -n 4 hostname``, and ``srun -N 4
   hostname``.  What's the difference and why?

In ``hpc-examples`` (at ``/scratch/scip/hpc-examples``), you find some
examples.

2. Find the files ``openmp/hello_omp/hello_omp.c`` and 
   ``openmp/hello_omp/hello_omp.slrm`` that have a short example of OpenMP.
   Compile and run it - a slurm script is included.

3. Find the files in ``python/python_openmp``. Try running the
   example with a few different ``--constraint=X`` and ``--cpus-per-task=C``.
   In your opinion, what architecture / cpu number combination would provide the
   best efficiency? Use ``seff`` to verify.

4. Find the files ``mpi/hello_mpi/hello_mpi.c`` and
   ``mpi/hello_mpi/hello_mpi.slrm`` that
   have a short example of MPI.
   Compile and run it - a slurm script is included.

Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`
