====================================
MPI parallelism: multi-task programs
====================================

.. _parallel-mpi:

.. include:: /triton/ref/videos.rst

.. admonition:: Abstract

   * Verify that your program can use MPI.

   * Compile to link with our MPI libraries. Remember to load
     the same modules in your Slurm script.

   * Use ``--nodes=1`` and ``--ntasks=n`` to reserve :math:`n` tasks
     for your job.

   * Start your application via ``srun`` if using module installed
     MPI or ``mpirun`` if you have your own installation of MPI.

   * For spreading tasks evenly across nodes, use ``--nodes=N``
     and ``--ntasks-per-node=n`` for getting
     :math:`N \cdot n` tasks.

   * You must always :doc:`monitor jobs <monitoring>` to make sure they are using all the
     resources you request (``seff JOBID``).

   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.

.. figure:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/cluster-schematic/cluster-schematic-mpi.png
   :alt: Schematic of cluster with current discussion points highlighted; see caption or rest of lesson.

   MPI parallelism lets you scale to many nodes on the cluster, at the
   cost of extra programming work.

.. highlight:: console



What is MPI parallelism?
------------------------

`MPI or message passing interface <https://en.wikipedia.org/wiki/Message_Passing_Interface>`_
is a standard for creating communication between many tasks that collectively
run a program in parallel. Programs using MPI can scale up to thousands of
nodes.

Programs using MPI need to be written so that they utilize the MPI communication.
**Thus typical programs that are not written around MPI cannot use MPI without
major modifications.**

.. figure:: /images/parallel-mpi.svg
    :width: 80%
    :align: center

MPI programs typically work in the following way:

1. Same program is started in multiple separate **tasks**.
2. All tasks join a communication layer with MPI.
3. Each tasks gets their own **rank** (basically and ID number).
4. Based on their ranks tasks execute their part of the code and communicate to
   other tasks. Rank 0 is usually the "main program" that prints output for
   monitoring.
5. After the program finishes communication layer is stopped.

When using module installed installations of MPI the MPI ranks will automatically
get information on their ranks from Slurm via library called
`PMIx <https://pmix.github.io/>`_. If the MPI used is some other version,
they might not connect with the Slurm correctly.



Running a typical MPI program
-----------------------------


Compiling a MPI program
~~~~~~~~~~~~~~~~~~~~~~~

For compiling/running an MPI job one has to pick up one of the MPI library
suites. There are various different MPI libraries that all implement the
MPI standard. We recommend that you use our OpenMPI installation
(``openmpi/4.1.6``). For information on other installed versions, see the
:doc:`MPI applications page<../apps/mpi>`.

.. include:: /triton/ref/mpi-warning.rst

Reserving resources for MPI programs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For basic use of MPI programs, you will need to use the
``--nodes=1`` and ``--ntasks=N``-options to specify the number of MPI workers.
The ``--nodes=1`` option is recommended so that your jobs will run in the
same machine for maximum communication efficiency. You can also run
without it, but this can result in worse performance.

In many cases you might require more tasks than one node has CPUs.
When this is the case, it is recommended to split the number of
workers evenly among the nodes. To do this, one can use
``--nodes=N`` and ``--ntasks-per-node=n``. This would give you
:math:`N \cdot n` tasks in total.

Each task will get a default of 1 CPU. See section on
:ref:`hybrid parallelisation <mpi-hybrid-parallelisation>` for
information on whether you can give each task more than one CPU.

Running and example MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../ref/examples-repo.rst

For this example, let's consider
`pi-mpi.c <https://github.com/AaltoSciComp/hpc-examples/blob/master/slurm/pi-mpi.c>`_-example
in the ``slurm``-folder.
It estimates pi with Monte Carlo methods and
can utilize multiple MPI tasks for calculating the trials.

First off, we need to compile the program with a suitable OpenMPI version. Let's use the
recommended version ``openmpi/4.1.6``::

   $ module load openmpi/4.1.6

   $ mpicc -o pi-mpi slurm/pi-mpi.c

The program can now be run with ``srun ./pi-mpi N``, where ``N`` is the number of
iterations to be done by the algorithm.

Let's ask for resources and run the program with two processes using ``srun``::

 $ srun --nodes=1 --ntasks=2 --time=00:10:00 --mem=500M ./pi-mpi 1000000

This worked because we had the correct modules already loaded.
Using a slurm script setting the requirements and loading the correct modules becomes easier:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:10:00
   #SBATCH --mem=500M
   #SBATCH --output=pi-mpi.out
   #SBATCH --nodes=1
   #SBATCH --ntasks=2

   module load openmpi/4.1.6

   srun ./pi-mpi 1000000

Let's call this script ``pi-mpi.sh``. You can submit it with::

  $ sbatch pi-mpi.sh



Special cases and common pitfalls
---------------------------------

MPI workers do not see each other
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using our installations of MPI the MPI ranks will automatically
get information on their ranks from Slurm via library called
`PMIx <https://pmix.github.io/>`_. If the MPI used is some other version,
they might not connect with the Slurm correctly.

If you have your own installation of MPI you might try setting
``export SLURM_MPI_TYPE=pmix_v2`` in your job before calling ``srun``.
This will tell Slurm to use PMIx for connecting with the MPI installation.

Setting a constraint for a specific CPU architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of CPUs/tasks one can specify for a single parallel job depends
usually on the underlying algorithm. In many codes, such as many
finite-difference codes, the workers are set in a grid-like structure. The user
of said codes has then a choice of choosing the dimensions of the simulation
grid aka. how many workers are in x-, y-, and z-dimensions.

For best perfomance one should reserve half or full nodes when possible. In
heterogeneous clusters this can be a bit more complicated as different CPUs
can have different numbers of cores.

In Triton CPU partitions there are machines with 24, 28 and 40 CPUs. See the
list of :ref:`available nodes<hardware-list>` for more information.

However, one can make the reservations easier by specifying a CPU architecture
with ``--constraint=ARCHITECTURE``. This tells Slurm to look for nodes that
satisfy a specific feature. To list available features, one can use
``slurm features``.

For example, one could limit the code to the Haswell-architecture with the
following script:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:10:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=1            # 1 node
  #SBATCH --ntasks-per-node=24 # 24 processes as that is the number in the machine
  #SBATCH --constraint=hsw     # set constraint for processor architecture

  module load openmpi/4.1.6  # NOTE: should be the same as you used to compile the code
  srun ./pi-mpi 1000000

Monitoring performance
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/monitoring/seff.rst


.. _mpi-hybrid-parallelisation:

Hybrid parallelization aka. giving more than one CPU to each MPI task
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When MPI and shared memory parallelism are done by the same application
it is usually called hybrid parallelization.
**Programs that utilize this model can require both multiple tasks
and multiple CPUs per task.**

For example, CP2K compiled to ``psmp``-target has hybrid parallelization enabled
while ``popt``-target has only MPI parallelization enabled. The best ratio between
MPI tasks and CPUs per tasks depends on the program and needs to be measured.

Remember that the number of CPUs in a machine is hardware dependent.
The total number of CPUs per node when you request ``--ntasks-per-node=n`` and
``--cpus-per-task=C`` is :math:`n \cdot C`. This number needs to be equal or less than
the total number of CPUs in the machine.



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: MPI parallelism 1: Explore and understand basic Slurm options

   Run ``srun --cpus-per-task=4 hostname``, ``srun --ntasks=4 hostname``, and ``srun --nodes=4
   hostname``.  What's the difference and why?

   .. solution::

      ``--cpus-per-task=4`` does exactly what it says, and gives each tasks 4 cpus. Since we
      have not requested any additional tasks, we run ``hostname`` once on a single node,
      but using 4 cpus.

      By comparison, ``ntasks=4`` creates 4 MPI workers that each run ``hostname`` once.
      These all run on a single node, and use one cpu each since we didn't request anything
      more.

      Finally ``srun --nodes=4 hostname`` runs ``hostname`` once each on four separate nodes.

      If we were to for example combine all of these, we would run ``hostname`` four times, on
      four nodes each for total 16 tasks, with each task using 4 cpus.


.. exercise:: MPI parallelism 2: Test the example with various options

   Compile the example ``pi-mpi.c``. Now try running it with a bigger number of trials
   (``2000000000`` or :math:`2 \cdot 10^{9}`) and with the following Slurm options:

   1. ``--ntasks=4`` without specifying ``--nodes=1``.
   2. ``--ntasks-per-node=4``
   3. ``--nodes=2`` and ``--ntasks-per-node=2``.

   Do you see any difference in the output?

   .. solution::

      You can run the commands with:

      .. code-block:: bash

         srun --ntasks=4 --time=00:10:00 --mem=500M ./pi-mpi 2000000000
         srun --ntasks-per-node=4 --time=00:10:00 --mem=500M ./pi-mpi 2000000000
         srun --nodes=2 --ntasks-per-node=2 --time=00:10:00 --mem=500M ./pi-mpi 2000000000

      In all cases you should see output from four different tasks and output showing
      the estimate for pi.

      In the first case, you might be allocated tasks from different nodes.

      In the second case, all tasks should be running in a single node.

      In the third case, two of the tasks should be running on the first node and two on the second one.

.. exercise:: MPI parallelism 3: Your program

   Think of your program. Do you think it can use MPI parallelism?

   If you do not know, you can check the program's documentation for words such as:

   - MPI
   - message-passing interface
   - mpirun
   - mpiexec
   - ...

   These usually point towards some method of MPI parallel execution.



What's next?
------------

The next tutorial is about :doc:`GPU parallelism <gpu>`.
