The following example uses example codes stored in
`the hpc-examples-repository <https://github.com/AaltoSciComp/hpc-examples>`_.
You can get the repository with the following command::

  git clone https://github.com/AaltoSciComp/hpc-examples/

Loading module::

  module load gcc/12.3.0      # GCC
  module load openmpi/4.1.6  # OpenMPI

Compiling the code:

.. tabs::

  .. group-tab:: C

    C code is compiled with ``mpicc``:

    .. code-block:: bash

      cd hpc-examples/mpi/hello_mpi/
      mpicc    -O2 -g hello_mpi.c -o hello_mpi

  .. group-tab:: Fortran

    Fortran code is compiled with ``mpifort``:

    .. code-block:: bash

      cd hpc-examples/mpi/hello_mpi_fortran/  # fortran
      mpifort  -O2 -g hello_mpi_fortran.f90 -o hello_mpi_fortran # Fortran code

For testing one might be interested in running the program with srun::

  srun --time=00:05:00 --mem-per-cpu=200M --ntasks=4 ./hello_mpi

For actual jobs this is obviously not recommended as any problem
with the login node can crash the whole MPI job. Thus we'll want to run the
program with a slurm script:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --ntasks=4           # 4 processes

  module load openmpi/4.1.6  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi

.. important::

   It is important to use ``srun`` when you launch your program.
   This allows for the MPI libraries to obtain task placement information
   (nodes, number of tasks per node etc.) from the slurm queue.

