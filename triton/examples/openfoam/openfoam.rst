OpenFOAM (with ParaView)
========================

OpenFOAM and ParaView have been installed from the Ubuntu 16.04 Docker
image provided by OpenFOAM people. It has minimal amount of other
software installed.

Parallelization is done against Triton's OpenMPI, so using this container
with other OpenMPI modules is discouraged.

Within the container OpenFOAM is installed under ``/opt/openfoam4/`` and
ParaView under ``/opt/paraviewopenfoam50/``. PATH is automatically appended
with their respective paths so all program calls are available
automatically.

Usage
~~~~~

This example shows how you can run damBreak example. Firstly, let's load
the OpenFOAM module and create a folder for the example::

    module use /share/apps2/singularity/modules
    module load OpenFOAM
    mkdir damBreak
    cd damBreak

Secondly, let's use singularity shell to copy example data files to the
folder and to initialize the simulation.::

    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/0 .
    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system .
    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/constant .
    blockMesh
    decomposePar
    exit

After this one can submit the following slurm :download:`script </triton/examples/openfoam/openfoam.slrm>` with sbatch to solve the problem:

.. literalinclude:: /triton/examples/openfoam/openfoam.slrm

Paraview can be started similarly with this :download:`script </triton/examples/openfoam/paraview.slrm>`:

.. literalinclude:: /triton/examples/openfoam/paraview.slrm
