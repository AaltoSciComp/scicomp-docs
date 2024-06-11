===
MPI
===

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

Message Passing Interface (MPI) is used in high-performance computing (HPC)
clusters to facilitate big parallel jobs that utilize multiple compute nodes.

MPI and Slurm
*************

For a tutorial on how to do Slurm reservations for MPI jobs, check out the
:ref:`MPI section<parallel-mpi>` of the parallel computing-tutorial.

Installed MPI versions
**********************

There are multiple installed MPI versions in the cluster, but due to updates
to the underlying network and the operating system some older ones might not
be functional.

Therefore it is highly recommended to use the recommended and tested versions
of MPI.

Each MPI version will use some underlying compiler by default. Please check
:ref:`here <mpi-changing-compilers>` for information on how to change the
underlying compiler.

.. csv-table::
   :delim: |
   :header-rows: 1

   MPI provider | MPI version | GCC compiler | Module name   | Extra notes
   OpenMPI      | 4.1.5       | gcc/11.3.0   | openmpi/4.1.5 |
   OpenMPI      | 4.0.5       | gcc/8.4.0    | openmpi/4.0.5 | There are known issues with this version, we do not recommend using this for new compilations

.. include:: /triton/ref/mpi-warning.rst

Usage
*****

Compiling and running an MPI Hello world-program
------------------------------------------------

.. include:: /triton/examples/mpi/hello.rst

.. _mpi-changing-compilers:

Overwriting default compiler of an MPI installation
---------------------------------------------------

Typically one should use the compiler that the MPI installation has been
compiled with. Thus if you encounter a situation where you would like to
use a different compiler, it might be best to ask the administrators to
install a different version of MPI with a different compiler.

However sometimes one can try to overwrite the default compiler. This will
obviously be faster than installing newer MPI versions. However, if you
encounter problems after switching the complier, you should not use it.

Changing complier when using OpenMPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The procedure of changing compilers for OpenMPI is documented in
`OpenMPI's FAQ <https://www.open-mpi.org/faq/?category=mpi-apps#override-wrappers-after-v1.0>`_.
Environment variables such as ``OMPI_MPICC`` and ``OMPI_MPIFC`` can be
set to overwrite the default compiler. See the article for full list
of environment variables.

For example, one could use an
:doc:`Intel compiler </triton/apps/intelcompilers>`
to compile the Hello world!-example by setting ``OMPI_MPICC``- and
``OMPI_MPIFC``-environment variables.

.. tabs::

  .. group-tab:: C

    Intel C compiler is ``icc``:

    .. code-block:: bash

      module load gcc/11.3.0
      module load openmpi/4.1.5
      module load intel-oneapi-compilers/2021.4.0

      export OMPI_MPICC=icc  # Overwrite the C compiler

      mpicc    -O2 -g hello_mpi.c -o hello_mpi

  .. group-tab:: Fortran

    Intel Fortran compiler is ``ifort``:

    .. code-block:: bash

      module load gcc/11.3.0
      module load openmpi/4.1.5
      module load intel-oneapi-compilers/2021.4.0

      export OMPI_MPIFC=ifort  # Overwrite the Fortran compiler

      mpicc    -O2 -g hello_mpi.c -o hello_mpi
