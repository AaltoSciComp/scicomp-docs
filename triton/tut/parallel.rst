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

Shared memory: OpenMP programs
------------------------------

OpenMP is a standard de facto for the multithreading implementations. There
are many others, but this one is the most common, supported by all known
compiler suits. For other implementations of shared memory parallelism,
please consult your code docs.

Simple code compiling::

  gcc -fopenmp -O2 -g omp_program.c -o omp_program

Running an OpenMP code::

  export OMP_PROC_BIND=TRUE
  srun --cpus-per-task=12 --mem-per-cpu=2000 --time=45:00 omp_program

The basic slurm options you need are ``--cpus-per-task=N`` (or ``-c N``) to specify the number of
cores to use within one node.  If your memory needs scale with the number of cores,
use ``--mem-per-core=``, if you require a fixed amount of memory (per
node regardless of number of processors), use ``--mem``.

The SLURM batch file will look similar::

  #!/bin/bash -l
  #SBATCH --cpus-per-task=12
  #SBATCH  --mem-per-cpu=2000
  #SBATCH --time=45:00
  export OMP_PROC_BIND=TRUE
  srun omp_program

Good to know that OpenMP is both an environment and set of libraries, but
those libraries always come as part of the compiler, thus no need to
load extra modules if you compile with the default ``gcc``.


Other programs and multithreading
---------------------------------

Some programs use multiple threads for their parallel computations. A good
example of this kind of program is MATLAB, that user parallel pool of workers;
or R, which uses the ``parallel``-package for its parallel applys.
Threaded applications behave similarly to OpenMP applications in that one
needs to specify the number of cores per task and amount of memory per core.

Message passing programs: MPI
-----------------------------

For compiling/running an MPI job one has to pick up one of the MPI library suites.
Big vendors provide their own (Cray, Intel) while there are other popular MPI
flavors available. To compile and run code you need to pick one. Since most of
the MPI codes will also use math libs, makes sense to pick a toolchain that
provides all at once.

For basic use of MPI programs, you usually need the ``-n`` option to
specify the number of MPI threads.

Loading module::

  module load openmpi  # GCC + OpenMPI

Compiling a code::

  mpif90 -O2 -g mpi_prog.f -o mpi_prog

Running an MPI code in the batch mode::

  #!/bin/bash
  #SBATCH -n 16                # 16 processes
  #SBATCH --constraint=avx     # run on nodes with AVX instructions
  #SBATCH --time=4:00:00       # takes 4 hours all together
  #SBATCH --mem-per-cpu=4000   # 4GB per process

  module load openmpi  # NOTE: should same as you used to compile the code
  srun ./mpi_prog


Triton has multiple architectures around (12, 20, 24, 40 CPU cores per node),
even though SLURM optimizes resources usage and allocate CPUs within one node, which
gives better performance for the app, it still makes sense to put constraints
explicitly.


Monitoring performance
----------------------

You can use the ``seff`` program (with a jobid) to list what percent
of available processors and memory you used.  If your processor usage
is far below, your code may not be working correctly in a parallel
environment.


Exercises
---------

1. Run ``srun -c 4 hostname``, ``srun -n 4 hostname``, and ``srun -N 4
   hostname``.  What's the difference and why?

In ``hpc-examples`` (at ``/scratch/scip/hpc-examples``), you find some
examples.

2. Find the files ``openmp/hello_omp.c`` and ``openmp/hello_omp.slrm``
   that have a short
   example of OpenMP.  Compile and run it - a slurm script is included.

3. Find the files ``mpi/hello_mpi.c`` and ``mpi/hello_mpi.slrm`` that
   have a short example
   of MPI.  Compile and run it - a slurm script is included.

Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`
