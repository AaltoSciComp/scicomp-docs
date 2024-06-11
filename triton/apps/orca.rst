ORCA
====

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

ORCA is a scientific software that provides cutting-edge methods in the
fields of density functional theory and correlated wave-function based methods.

Basic Usage
-----------

You can do a simple run with ORCA with the
:download:`following script</triton/examples/orca/orca_example.sh>`.

.. literalinclude:: /triton/examples/orca/orca_example.sh
   :language: slurm

This script performs a parallel run of ORCA to simulate the behavior of water
molecule. The input file for this simulation is called ``water.inp``, which is
written to by the cat command.

To run this script, download it and submit into the queue using ``sbatch``:

.. code-block:: console

  $ wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/orca/orca_example.sh
  $ sbatch orca_example.sh

How to launch ORCA when using MPI parallelism
---------------------------------------------

When doing parallel runs you should always launch ORCA with

.. code-block:: sh

   $(command -v orca) input_file.inp

in your Slurm scripts. This is because ORCA will need the executable to be
launched with the full path of the executable and it will launch the MPI
tasks independently. For more information, see
`this documentation page <https://www.orcasoftware.de/tutorials_orca/first_steps/trouble_install.html#using-openmpi>`__.

Setting the number of MPI tasks
-------------------------------

The example given above asked for 4 MPI tasks by setting
``#SBATCH --ntasks-per-node=4`` in the Slurm batch script and then told
ORCA to use 4 tasks by setting ``!PAL4`` in the input file.

When asking for more than 8 tasks you need use ``%PAL NPROCS 16 END`` to
set the number of tasks in ORCA input (here, the line would specify 16 tasks).

For more information please refer to ORCA's
`documentation page on parallel calculations <https://www.orcasoftware.de/tutorials_orca/first_steps/parallel.html>`__.
