Building a basic version of LAMMPS
**********************************

LAMMPS is typically built based on the specific needs of the simulation.
When building LAMMPS one can enable and disable various different packages
that enable commands when LAMMPS is run.

LAMMPS has an `extensive guide <https://docs.lammps.org/Build.html>`_ on
how to build LAMMPS. The recommended way of building LAMMPS is
`with CMake <https://docs.lammps.org/Build_cmake.html>`_.

Below are instructions on how to do a
`basic build of LAMMPS <https://docs.lammps.org/Build_basics.html>`_
with OpenMP and MPI parallelizations enabled.

One can obtain LAMMPS source code either from
`LAMMPS download page <https://www.lammps.org/download.html>`_
or from
`LAMMPS source repository <https://github.com/lammps/lammps>`_. Here
we'll be using the version 22Jun2022.

.. code-block:: bash

  # Obtain source code and go to the code folder
  wget https://download.lammps.org/tars/lammps-23Jun2022.tar.gz
  tar xf lammps-23Jun2022.tar.gz
  cd lammps-23Jun2022

  # Create a build folder and go to it
  mkdir build
  cd build

  # Activate CMake and OpenMPI modules needed by LAMMPS
  module load cmake gcc/13.2.0 openmpi/4.1.6

  # Configure LAMMPS packages and set install folder
  cmake ../cmake -D BUILD_MPI=yes -D BUILD_OMP=yes -D CMAKE_INSTALL_PREFIX=../../lammps-mpi-23Jun2022

  # Build LAMMPS
  make -j 2

  # Install LAMMPS
  make install

  # Go back to starting folder
  cd ../..

  # Add installed LAMMPS to the executable search path
  export PATH=$PATH:$PWD/lammps-mpi-23Jun2022/bin

Now we can verify that we have a working LAMMPS installation with the following command:

.. code-block:: bash

  echo "info configuration" | srun lmp

The output should look something like this:

.. code-block:: bash

  srun: job 11839786 queued and waiting for resources
  srun: job 11839786 has been allocated resources
  LAMMPS (23 Jun 2022 - Update 2)
  OMP_NUM_THREADS environment is not set. Defaulting to 1 thread. (src/comm.cpp:98)
    using 1 OpenMP thread(s) per MPI task

  Info-Info-Info-Info-Info-Info-Info-Info-Info-Info-Info
  Printed on Thu Jan 19 17:20:21 2023

  LAMMPS version: 23 Jun 2022 / 20220623

  OS information: Linux "CentOS Linux 7 (Core)" 3.10.0-1160.71.1.el7.x86_64 x86_64

  sizeof(smallint): 32-bit
  sizeof(imageint): 32-bit
  sizeof(tagint):   32-bit
  sizeof(bigint):   64-bit

  Compiler: GNU C++ 8.4.0 with OpenMP 4.5
  C++ standard: C++11

  Active compile time flags:

  -DLAMMPS_GZIP
  -DLAMMPS_PNG
  -DLAMMPS_SMALLBIG

  Available compression formats:

  Extension: .gz     Command: gzip
  Extension: .bz2    Command: bzip2
  Extension: .xz     Command: xz
  Extension: .lzma   Command: xz
  Extension: .lz4    Command: lz4


  Installed packages:



  Info-Info-Info-Info-Info-Info-Info-Info-Info-Info-Info

  Total wall time: 0:00:00
