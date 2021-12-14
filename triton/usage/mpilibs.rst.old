MPI on Triton
=============

The basic parallel programming model for PC-clusters is message passing.
MPI (Message Passing Interface) is a library specification for
message-passing, proposed, nowadays, as a standard. OpenMPI and MVAPICH
are two different (but doing the same) MPI implemetaions, both are
installed on triton. MVAPICH is the recommended one. MPI is suitable for
both distributed memory computers (thus through interconnect between
nodes) and shared memory architectures (computing within one node).

Check out the latest version of MVAPICH / OpenMPI with

::

    $ module avail

By setting up your environment with ``module``, you will set all the
variables like ``$MPIRUN``, ``$MPIHOME`` etc.

Load MVAPICH2:

::

    $ module load mvapich2/1.8a2-gcc-4.4.6

Load OpenMPI (for software compiled on recently updated SL6.2):

::

    $ module load openmpi/1.4.5-gcc-4.4.6

Load OpenMPI (for software compiled on SL6.1):

::

    $ module load compat-openmpi-x86_64

Compiling after that is quite straight forward:

::

    $ mpif90 your_code.f90 -o your_code
    $ mpicc your_code.c -o your code

Parallel programs are to be run as batch jobs, even test runs. See
Executing jobs / Batch system for examples of running in parallel.

Additional links
~~~~~~~~~~~~~~~~

-  `MVAPICH at
   mvapich.cse.ohio-state.edu <http://mvapich.cse.ohio-state.edu/>`__
-  `OpenMPI at www.open-mpi.org <http://www.open-mpi.org/>`__
