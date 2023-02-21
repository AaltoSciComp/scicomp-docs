LAMMPS indent-example
~~~~~~~~~~~~~~~~~~~~~

Let's run a simple example from
`LAMMPS examples <https://docs.lammps.org/Examples.html>`_.
This specific model represents a spherical indenter into a 2D solid.

First, we need to get the example:

.. code-block:: sh

  # Obtain source code and go to the code folder
  wget https://download.lammps.org/tars/lammps-23Jun2022.tar.gz
  tar xf lammps-23Jun2022.tar.gz
  cd lammps-23Jun2022/examples/indent/

After this we can launch LAMMPS with a slurm script like this:

.. literalinclude:: /triton/examples/lammps/indent/lammps_indent.sh
   :language: slurm
