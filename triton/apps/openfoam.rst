========
OpenFoam
========

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

OpenFoam is a popular open source CFD software.
There are two main forks of the same software available:

- OpenFOAM maintained by OpenCFD (affiliate of ESI Group).
  Their website is `www.openfoam.com <https://www.openfoam.com/>`_
  and the source code is maintained in
  `their own GitLab repository <https://develop.openfoam.com/Development/openfoam>`_.
  They use version numbers based on the year and the month of the
  release e.g. ``1906``.
- OpenFOAM maintained by OpenFOAM Foundation.
  Their website is `www.openfoam.org <https://openfoam.org/>`_
  and their source code is maintained in
  `various repositories in GitHub <https://github.com/OpenFOAM?tab=repositories>`_.
  They use integer version numbers e.g. ``8``.

There are various installations of these installed in Triton.

OpenFOAM installations
----------------------

Below is a list of installed OpenFOAM versions:

.. list-table::
   :header-rows: 1
   :widths: 1 1 2

   * * OpenFOAM provider
     * Version
     * Module name

   * * openfoam.com
     * v1906
     * openfoam/1906-openmpi-metis

   * * openfoam.org
     * 9
     * openfoam-org/9-openmpi-metis

   * * openfoam.org
     * 8
     * openfoam-org/8-openmpi-metis

   * * openfoam.org
     * 7
     * openfoam-org/7-openmpi-metis

Running OpenFOAM
----------------

OpenFOAM installations are built using OpenMPI and thus
one should reserve the resources following the
:ref:`MPI instructions<parallel-mpi>`.

When running the MPI enabled programs, one should launch them
with ``srun``. This enables SLURM to allocate the tasks correctly.

Some programs included in the OpenFOAM installation (such as
``blockMesh`` and ``decomposePar``) do simulation initialization
in a serial fashion and should be called without using ``srun``.

Examples
--------

.. include:: /triton/examples/openfoam/dambreak/dambreak_example.rst
