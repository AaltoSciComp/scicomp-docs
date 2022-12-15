Running damBreak example
~~~~~~~~~~~~~~~~~~~~~~~~

One popular simple example is an example of a dam breaking in two
dimensions. For more information on the example, see
`this article <https://doc.cfd.direct/openfoam/user-guide-v9/dambreak>`_.

First, we need to take our own copy of the example::

    module load openfoam-org/9-openmpi-metis
    cp -r $FOAM_TUTORIALS/multiphase/interFoam/laminar/damBreak/damBreak .

Second, we need to write a Slurm script
:download:`run_dambreak.sh </triton/examples/openfoam/dambreak/run_dambreak.sh>`:

.. literalinclude:: /triton/examples/openfoam/dambreak/run_dambreak.sh

After this we can submit the Slurm script to the queue with
``sbatch run_dambreak.sh``. The program will run in the queue and we will get
results in ``damBreak.out`` and in the simulation folder.

Do note that some programs (``blockMesh``, ``decomposePar``) do not
require multiple MPI tasks. Thus these are run without ``srun``. By
contrast, the program call that does the main simulation
(``interFoam -parallel``) uses multiple MPI tasks and thus is called
via ``srun``. 
