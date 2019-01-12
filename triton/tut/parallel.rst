==================
Parallel computing
==================

.. note::

   This page is still under development.

Parallel computing is what HPC is really all about: processing things on
more than one CPU at once. By now, you should have read all of the previous
tutorials.

Parallel programming models
---------------------------

Parallel programming is a completely different way of programming.  Most
Triton users don't need to write their own
applications, at most they will be running existing programs, but in
order to understand things, we start with some introduction.

The two main models are:

* Shared memory program (or multithreading) runs on only one node
  because, like the name says, all the memory has to be accessible to
  all the processes.  Thus, scaleability is limited to a number of CPU
  cores available within one computational node. The code is  
  easier to implement and the same code can still be run in a serial mode.
  Examples of application that utilize this model: Matlab, R, OpenMP
  applications, typical parallel desktop programs.

* Message passing programming (e.g. MPI, message passing interface)
  can run on multiple nodes interconnected with the network via passing
  data through MPI software libraries. The large-scale scientific programs
  are MPI. MPI can scale to thousands of CPU cores, but it's harder to
  implement from the programmer point of view.

Both models, MPI and shared memory, can be combined in one application, in
this case we are talking about hybrid parallel programming model.

Most historical scientific code is MPI, but these days more and more
people are using shared memory models.

The important note is that a normal, serial code can't just be run as
parallel without modifications. As a user it is your responsibility to 
understand what parallel model implementation your code has, if any.
Knowing this, you can proceed with the instructions below.

Another important note regarding parallelizm is that all the applications 
scale good up to some upper limit which depends on apllication implementation,
size and type of problem you solve and some other factors. The best practice
is to benchmark your code on different number of CPU cores before actual
production run.

OpenMP programs
---------------

OpenMP is a standard de facto for the multithreading implementations. There
are many others, but this one is the most common, suppported by all known 
compiler suits. For other implementations of shared memory parallelism,
please consult your code docs.

Simple code compiling::

  gcc -fomp omp_program.c -o omp_program

Running an OpenMP code::

  export OMP_PROC_BIND=TRUE
  srun --cpus-per-task=12 --mem-per-cpu=2000 --time=45:00 omp_program

The basic slurm options you need are ``--cpus-per-task=N`` (or ``-c N``) to specify the number of
cores to use within one node.  If your memory needs scale with the number of cores,
use ``--mem-per-core=``, if you require a fixed amount of memory (per
node regardless of number of processors), use ``--mem``.

SLURM batch file will look similarly::

  #!/bin/bash -l
  #SBATCH --cpus-per-task=12
  #SBATCH  --mem-per-cpu=2000
  #SBATCH --time=45:00 
  export OMP_PROC_BIND=TRUE
  srun omp_program

Good to know that OpenMP is both an environment and set of libraries, but
those librarries always come as part of the compiler, thus no need to 
load extra modules if you complie with the default ``gcc``.


Other programs and multithreading
---------------------------------

Some programs use multiple threads for their parallel computations. A good
example of this kind of program is MATLAB, that user parallel pool of workers;
or R, which uses the ``parallel``-package for its parallel applys.
Threaded applications behave similarly to OpenMP applications in that one
needs to specify the number of cores per task and amount of memory per core.

MPI runs
--------

For compiling/running an MPI job one has to pick up one of the MPI library suit.
Big vendors provide their own (Cray, Intel) while there are other popular MPI
flavors available. To compile and run code you need to pick one. Since most of
the MPI codes will also use math libs, makes sense to pick a toolchain that
provides all at once.

Loading module::

  module load ioolf  # Intel Composer + MKL + OpenMPI

Compiling a code::

  mpif90 mpi_prog.f -o mpi_prog
  
Running an MPI code in the batch mode::

  #!/bin/bash
  #SBATCH -N 2                 # on two compute nodes
  #SBATCH -n 48                # 24 processes
  #SBATCH --constraint=hsw     # run on pe[] nodes only
  #SBATCH --time=4:00:00       # takes 4 hours all together
  #SBATCH --mem-per-cpu=4000   # 4GB per process

  module load ioolf  # NOTE: should same as you used to compile the code
  srun mpi_prog

In the example above we request two nodes with the Haswell CPUs (24 CPU cores each).
Small MPI jobs will perfectly run also within one node.

Triton has multiple architechtures around (12, 20, 24, 40 CPU cores per node),
even though SLURM optimizes resources usage and allocate CPUs within one node, which
gives better performance for the app, it still makes sense to put constraints
explicitly.


Monitoring performance
----------------------

You can use the ``seff`` program (with a jobid) to list what percent
of available processors and memory you used.  If your processor usage
is far below, your code may not be working correctly in a parallel
environment.


Quick reference
---------------

As a reminder, here is the quick reference of all slurm options

.. include:: ../ref/slurm.rst


Exercises
---------

In ``triton-examples`` (at ``/scratch/scip/examples``), you find some
examples.  You may need some help from :doc:`../usage/general` to do
these:

1. Find the files ``openmp/hello_omp.{c.slrm}`` that have a short
   example of OpenMP.  Compile and run it - a slurm script is included.

2. Find the files ``mpi/hello_mpi.{c.slrm}`` that have a short example
   of MPI.  Compile and run it - a slurm script is included.

Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`
