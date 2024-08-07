Building a version of LAMMPS with most packages
***********************************************

Many packages in LAMMPS need other external libraries such as BLAS and FFTW
libraries. These extra libraries can be given to LAMMPS via flags mentioned
in `this documentation <https://docs.lammps.org/Build_settings.html>`__, but in
most cases loading the appropriate modules from the module system is enough for
CMake to find the libraries.

To include extra packages in the build one can either use flags mentioned
in `this documentation <https://docs.lammps.org/Build_package.html>`__ or one
can use developer maintained
`CMake presets <https://docs.lammps.org/Build_package.html#cmake-presets-for-installing-many-packages>`__
for installing a collection of packages.

Below is an example that installs LAMMPS with "most packages"-collection enabled:

.. code-block:: sh

  # Obtain source code and go to the code folder
  wget https://download.lammps.org/tars/lammps-23Jun2022.tar.gz
  tar xf lammps-23Jun2022.tar.gz
  cd lammps-23Jun2022

  # Create a build folder and go to it
  mkdir build
  cd build

  # Activate CMake and OpenMPI modules needed by LAMMPS
  module load cmake gcc/13.2.0 openmpi/4.1.6 fftw/3.3.10 openblas/0.3.24 eigen/3.4.0 ffmpeg/6.0 zstd/1.5.5
  # Not on new-triton-2024: voropp/0.4.6

  # Configure LAMMPS packages and set install folder
  cmake ../cmake -C ../cmake/presets/most.cmake -D BUILD_MPI=yes -D BUILD_OMP=yes -D CMAKE_INSTALL_PREFIX=../../lammps-mpi-most-23Jun2022

  # Build LAMMPS
  make -j 2

  # Install LAMMPS
  make install

  # Go back to starting folder
  cd ../..

  # Add installed LAMMPS to the executable search path
  export PATH=$PATH:$PWD/lammps-mpi-most-23Jun2022/bin

Now we can verify that we have a working LAMMPS installation with the following command:

.. code-block:: bash

  echo "info configuration" | srun lmp

The output should look something like this:

.. code-block:: bash

  srun: job 13235690 queued and waiting for resources
  srun: job 13235690 has been allocated resources
  LAMMPS (23 Jun 2022 - Update 2)
  OMP_NUM_THREADS environment is not set. Defaulting to 1 thread. (src/comm.cpp:98)
    using 1 OpenMP thread(s) per MPI task

  Info-Info-Info-Info-Info-Info-Info-Info-Info-Info-Info
  Printed on Tue Feb 07 11:41:05 2023

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
  -DLAMMPS_FFMPEG
  -DLAMMPS_SMALLBIG

  Available compression formats:

  Extension: .gz     Command: gzip
  Extension: .bz2    Command: bzip2
  Extension: .xz     Command: xz
  Extension: .lzma   Command: xz
  Extension: .lz4    Command: lz4


  Installed packages:

  ASPHERE BOCS BODY BPM BROWNIAN CG-DNA CG-SDK CLASS2 COLLOID COLVARS COMPRESS
  CORESHELL DIELECTRIC DIFFRACTION DIPOLE DPD-BASIC DPD-MESO DPD-REACT
  DPD-SMOOTH DRUDE EFF ELECTRODE EXTRA-COMPUTE EXTRA-DUMP EXTRA-FIX
  EXTRA-MOLECULE EXTRA-PAIR FEP GRANULAR INTERLAYER KSPACE MACHDYN MANYBODY MC
  MEAM MISC ML-IAP ML-SNAP MOFFF MOLECULE OPENMP OPT ORIENT PERI PHONON PLUGIN
  POEMS QEQ REACTION REAXFF REPLICA RIGID SHOCK SPH SPIN SRD TALLY UEF VORONOI
  YAFF

  Info-Info-Info-Info-Info-Info-Info-Info-Info-Info-Info

  Total wall time: 0:00:00

