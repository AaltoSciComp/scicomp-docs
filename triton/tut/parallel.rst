==================
Parallel computing
==================

Parallel computing is what HPC is really all about: processing things on
more than one CPU at once. By now, you should have read most of the previous
tutorials.

Parallel programming models
---------------------------

**Parallel programming** is a completely different way of programming.  Most
Triton users don't need to write their own
applications, at most they will be running existing programs, but in
order to understand things, we start with some introduction.

The two main models are:

* **Shared memory program (or multithreading)** runs on only one node
  because, like the name says, all the memory has to be accessible to
  all the processes.  Thus, scaleability is limited to a number of CPU
  cores available within one computational node. The code is
  easier to implement and the same code can still be run in a serial mode.
  Examples of application that utilize this model: Matlab, R, OpenMP
  applications, typical parallel desktop programs.

* **Message passing programming** (e.g. **MPI**, message passing interface)
  can run on multiple nodes interconnected with the network via passing
  data through MPI software libraries. The large-scale scientific programs
  are MPI. MPI can scale to thousands of CPU cores, but it's harder to
  implement from the programmer point of view.

Both models, MPI and shared memory, can be combined in one application, in
this case we are talking about hybrid parallel programming model.

Most historical scientific code is MPI, but these days more and more
people are using shared memory models.

The choice above isn't a choice you make - *it is part of the software
design itself*.  You *can't* just take serial code and run it as
parallel without fundamentally changing it. As a user it is your
responsibility to
understand what parallel model implementation your code has, if any.
Knowing this, you can proceed with the instructions below.

Another important note regarding parallelism is that all the applications
scale good up to some upper limit which depends on application implementation,
size and type of problem you solve and some other factors. The best practice
is to benchmark your code on different number of CPU cores before actual
production run.

**If you want to run some program in parallel, you have to know
something about it - is it shared memory or MPI?  A program doesn't
magically get faster when you ask more processors if it's not designed
to.**

Shared memory: OpenMP programs
------------------------------

**OpenMP** is a standard de facto for the multithreading implementations. There
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


What to use in practice?
------------------------

.. csv-table::
   :header-rows: 1
   :delim: |

   Method   | Minimal Slurm options to use  | notes
   OpenMP   | ``-c`` only | Limited to one node
   MPI      | ``-n`` only usually    |
   Hybrid   | ``-c`` and ``-n``      | Somewhat special case
   Other programs doing it themselves | Usually only `-c` | **Must** configure program to use environment variable ``$SLURM_CPUS_PER_TASK`` threads/processes, which is set to the ``-c`` option.


Monitoring performance
----------------------

You can use the ``seff`` program (with a jobid) to list what percent
of available processors and memory you used.  If your processor usage
is far below, your code may not be working correctly in a parallel
environment.


Exercises
---------

In ``triton-examples`` (at ``/scratch/scip/examples``), you find some
examples.

1. Find the files ``openmp/hello_omp.c`` and ``openmp/hello_omp.slrm``
   that have a short
   example of OpenMP.  Compile and run it - a slurm script is included.

2. Find the files ``mpi/hello_mpi.c`` and ``mpi/hello_mpi.slrm`` that
   have a short example
   of MPI.  Compile and run it - a slurm script is included.

Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`
