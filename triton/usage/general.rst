==========================
Running programs on Triton
==========================


Triton differs somewhat from your regular desktop computer. The large
numbers and complex examples may give the impression of something far
more special than it actually is: a bunch of computers. Fundamentally
these are just slightly more powerful computers, with much more memory
and a faster network in between. Where the major differences begin,
though, is that they are shared by around 100 people from different
departments with an unusual scale and variation of applications and
needs. In order to even begin to accommodate everyone on the cluster, we
have to use an intermediate resource manager and scheduler through which
certain policies can be put into effect. The *cluster* is a combination
of the compute nodes, our site policies, and the scheduler software
which works it all out in practice.

This guide tries to give an idea of how to run programs in the cluster
through the Slurm scheduler. While this certainly does not cover all the
use cases, you're welcome to ask any questions in the `Issue
Tracker <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`__.

Scheduling policy and queues
============================

The cluster nodes (computers) are grouped into *partitions* (the
scheduler's concept). While the default *batch* partition may always be
in full use, other partitions act as boundaries that keep specialized
nodes, such as the GPU machines, ready and immediately available for
jobs with special requirements.

.. include:: ../ref/partitions.rst

The debug partition and its 60 minute time limit exists for developing
code and testing job scripts and simply getting used to the cluster
commands.  Don't run anything here unless it is your current work focus.

**Most of the time, you should not need to specify any partition (debug,
interactive, or your group's dedicated partitions).** When you submit a
job, there is a script (job\_submit.lua) that runs in the background and
automatically selects partitions.  If you notice the script doing
something wrong, submit an issue and we can look at it.  It roughly uses
this logic:

-  Do you use ``--gres=gpu`` ?  If so, do GPU partitions.
-  Otherwise, default to batch
-  If your time limit is less than the short time limit, also add in the
   short partitions, too
-  If you use large amounts of memory, add hugemem.

It can be worth looking at your job's partition list to make sure it is
optimal: "slurm j $jobid"

Interactive logins
==================

Triton mainly runs non-interactive batch jobs in its current
configuration. There is a (small) partition which is meant for
interactive jobs. There are two main options for running interactive
shells:

-  Cluster frontend (login) machine ``triton.aalto.fi`` for editing,
   compiling and testing code.
-  Interactive jobs started with the "sinteractive" command.

We ask you to refrain from running multi-GB, many-core applications of
the frontend. The login machine ``triton.aalto.fi`` is mainly intended
for editing code and submission scripts, sorting your files, checking
jobs and of course submitting the jobs scripts through Slurm to the
actual execution nodes (called ``cn``-something, ivy\*, ``gpu``\ \* or
``tb``\ \*).

Interactive and computationally intensive applications should be run on
``the interactive partition``. Still, to maximise the resource usage
it's best to structure you workflow such that you can use normal batch
jobs.

You can access ``an interactive shell with the "sinteractive" command``
from the frontend machine ``tri``\ ``ton.aalto.fi``:

Launch 2 hour interactive session

::

    $ sinteractive -t 2:0

See also the interactive usage section below for advanced examples.

Job examples
============


Submit a short batch job
^^^^^^^^^^^^^^^^^^^^^^^^

Batch job is by default a single-CPU job that will run specified
commands in series and optionally save output into a file.

A number of nodes have been dedicated for jobs that run under four
hours, which makes it more likely that resources are immediately
available.

Short batch example

::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH --time=04:00:00      # 4 hours
    #SBATCH --mem-per-cpu=1000   # 1G of memory

    cd $WRKDIR/mydata/
    srun myprog params
    srun myprog2 other params
    srun myprog3

A batch job can have as many "srun" steps as needed or just one. At the
end of the day SBATCH script is just a BASH script with a set of
specific directives for SBATCH. Being so, the script can be as simple as
a few #SBATCH lines plus "srun" or may consists of hundreds of BASH
lines. The best practice is to join the tasks into the same job and
avoid short runs (that take seconds or minutes).

Submit an array job (batch job for repeated tasks)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slurm supports so-called array jobs, where one can easily handle a large
number of similar jobs. An array job is essentially a set of independent
jobs. In this example we run an array job consisting of 30 different
array tasks. In the job script, the environment variable
SLURM\_ARRAY\_TASK\_ID is the ID of the current task. In the example
below, this is used to make the application read the correct input file,
and to generate output in a unique directory.

::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=0-29
     
    cd $SLURM_ARRAY_TASK_ID
    srun ./my_application -input input_data_$SLURM_ARRAY_TASK_ID
    cd ..

The array indices need not be sequential. E.g. if you discover that
after the above array job is finished, the job task id's 7 and 19
failed, you can relaunch just those jobs with ``--array=7,19``. While the
array job above is a set of serial jobs, parallel array jobs are
possible. For more information, see the `Slurm job array
documentation <https://slurm.schedmd.com/job_array.html>`__.

Submit a multithreaded job
^^^^^^^^^^^^^^^^^^^^^^^^^^

Programs using multiple threads must have their behaviour described to
Slurm in terms of the number of threads needed. To launch a
multithreaded job we tell slurm that we want a single task, but that
that one task requires several CPU's. This is done with the
``--cpus-per-task=``\ *N* (or the short form ``-c`` *N*) option and should match the
number of computational threads used by your application.

When moving a program from a Linux workstation to the cluster, please
note than simply increasing the Slurm reservation size usually does not
affect the running behavior of the program. Take a moment to see how
many threads were using CPU on a workstation, and use that as a starting
point (try the ``top`` command and press the H key to see separate
threads). Not all tasks scale well to 12 (or 20, 24) threads, so run a
few benchmarks in the play partition (``-p debug``) to test things
before committing a lot of cluster resources to an application that may
not utilize all of it. Amount of threads should be no more than number
of CPU cores on the node.

For OpenMP programs the information about Slurm reservation size is
passed with environment variable OMP\_NUM\_THREADS, which controls how
many OpenMP threads will be used for the job (equal to ``-n #``).
However by default all allocated threads are used, so you need to
specify OMP\_NUM\_THREADS only if you want to launch a job step using
fewer than the allocated CPU's. Other multi-threaded programs may have
similar ways to control the number of threads launched. When using
OpenMP, additionally one should bind threads to CPU's with the
OMP\_PROC\_BIND environment variable.

OpenMP example

::

    #!/bin/bash
    #SBATCH --cpus-per-task=12
    #SBATCH --time=40:00
    #SBATCH --mem-per-cpu=2000
    export OMP_PROC_BIND=true
    srun /path/to/openMP_executable

Submit a MPI job
^^^^^^^^^^^^^^^^

Slurm's "srun" works as a wrapper to traditional "mpirun" command, it
takes care of setting up a correct environment for MPI. For more
information, see the `slurm MPI
guide <https://slurm.schedmd.com/mpi_guide.html>`__.

Triton has several generations of different architectures, as of Oct
2018 we have Westmere, IvyBridge, Haswell, and Broadwell Xeons.  They
have different number on CPU cores per node: 12 for Westmere, 20 on
IvyBridge, 24 on Haswell, and 28 on Broadwell.

Submit a small MPI job
^^^^^^^^^^^^^^^^^^^^^^

A job that fit to one node: *single-node job*. Here we use the "-N 1"
option which tells slurm to allocate all tasks on a single node. The "-n
X" tells to SLURM how many MPI tasks you want to run.

Small MPI example using mvapich2

::

    #!/bin/bash
    #SBATCH -N 1                 # on one node
    #SBATCH -n 4                 # 4 processes
    #SBATCH --time=4:00:00       # 4 hours
    #SBATCH --mem-per-cpu=2000   # 2GB per process
     
    module load gmvolf/triton-2016a   # MVAPICH + GCC + math libs modules
    srun /path/to/mpi_program params

For "-n" less or equal to 12 this job will fit on any of the available
nodes, if you put something more that 12 but below 20, it will go to
either Haswell or IvyBridge nodes, and in case of up to 24 to Haswell
only. Independently on the requested ``--n X`` one can always define the
``--constraint=`` and explicitly request specific CPU arch. See large MPI
jobs examples below.

Submit a large MPI job
^^^^^^^^^^^^^^^^^^^^^^

Large MPI-job, the one that does not fit to a single node. You should
ask for a number of tasks that is a multiple of number of CPU cores on
the node. Use the "exclusive" option to ensure that entire nodes are
allocated, removing interference from other jobs and minimizing the
number of nodes required to fulfill the allocation. One must specify
type of requested CPU, number of tasks and corresponding number of nodes
in the SBATCH script.

MPI example using Open MPI

::

    #!/bin/bash
    #SBATCH --time=2:00:00       # two hours job
    #SBATCH --mem-per-cpu=1500   # 1.5GB of memory per process
    #SBATCH --exclusive          # allocate whole node
    #SBATCH --constraint=hsw     # require Haswell CPUs with 24 cores per node 
    #SBATCH -N 2                 # on two nodes 
    #SBATCH -n 48                # 48 processes to run (2 x 24 = 48)

     
    module load goolf/triton-2016a    # OpenMPI + GCC + math libs
    srun /path/to/mpi/program  params

     
    ----------------- 12 CPU cores case ---------------------------------------
     
    #SBATCH --constraint=wsm     # require Westemers, 12 cores per node 
    #SBATCH -N 4                 # on four nodes 
    #SBATCH -n 48                # 48 processes to run (4 x 12 = 48)
     
     
    ----------------- 20 CPU cores case ---------------------------------------
     
    #SBATCH --constraint=ivb    # require IvyBridges, 20 cores per node 
    #SBATCH -N 2                 # on two nodes 
    #SBATCH -n 40                # 40 processes to run (2 x 20 = 40)

Submit a hybrid MPI/OpenMP job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Batch file for running an application using a hybrid parallelization
scheme with both MPI and OpenMP. Each MPI rank (process) runs a number
of OpenMP threads. From the slurm perspective, this is essentially a
combination of the above examples of parallel and multithreaded jobs. In
this example we launch 8 MPI processes, and each MPI process runs 6
threads. The job thus uses a total of 8\*6=48 cores. We explicitly
require Haswell CPUs to run 4 MPI processes per node. You need to
experiment with your application to see what is the best combination. 
Example below uses goolf-2016a with OpenMPI and GCC.

Hybrid MPI/OpenMP example using Open MPI

::

    #!/bin/bash
    #SBATCH --time=30:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --exclusive
    #SBATCH --constraint=hsw    # Haswells only
    #SBATCH --ntasks=8          # -n, number of MPI tasks
    #SBATCH --cpus-per-task=6   # -c, number of threads per MPI task
    #SBATCH --nodes=2           # -N, amount of nodes
     
    module load goolf/triton-2016a    # here we use OpenMPI as an example
    export OMP_PROC_BIND=true
    srun /path/to/MPI_OpenMP_program params

For mvapich2 you need to disable affinity, as mvapich2 has no way of
specifying that each MPI rank needs N processors. One also cannot use
the OpenMP affinity features, as the lack of any MPI affinity otherwise
causes all MPI ranks on a node to be bound to the same cores. Example
script below:

Hybrid MPI/OpenMP example using mvapich2

::

    #!/bin/bash
    #SBATCH --time=30:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --exclusive
    #SBATCH --constraint=[opt|wsm]
    #SBATCH -n 8
    #SBATCH -c 6
    #SBATCH -N 4
     
    module load gmvolf/triton-2016a
    export MV2_ENABLE_AFFINITY=0
    srun /path/to/MPI_OpenMP_program params

If using other MPI flavors, please check the manual and do some tests to
verify that CPU binding works correctly.

Submit a parallel (non-MPI) job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to launch parallel jobs that do not use MPI. However in
this case you are responsible for setting up any necessary communication
between the different tasks (processes) in the job. Depending on the job
script, resources may be allocated on several nodes, so your application
must be prepared to communicate over the network. The slurm "srun"
command can be used to launch a number of identical executables, one for
each task. Example:

Parallel job

::

    #!/bin/bash
    #SBATCH --time=01:00 --mem-per-cpu=500
    #SBATCH --exclusive
    #SBATCH --constraint=[hsw|ivb|wsm]
    #SBATCH -N 4
    srun -N 4 hostname

This will print out the 4 allocated hostnames. The "-N 4" ensures that
we run a task on all 4 allocated nodes. If we instead want to launch one
process per allocated CPU, we can instead do "srun -n 48 executable"
(4\*12=48).

In a case where the program in question uses Master-Worker-paradigm,
where there exists a single worker that coordinates the rest,
see \ :doc:`Compute node local
drives <localstorage>`

Most of the compute nodes are equipped with one SATA disk drive though
there are some with 2 and 4. See  ``slurm features``  for the full list.
 A node with a specific amount of drives can be requested as:

::

    #SBATCH --gres=spindle:4

GPU cards with ``--gres=``
^^^^^^^^^^^^^^^^^^^^^^^^^^

See details at :doc:`Slurm commands <../ref/slurm>`

Links and other additional materials
====================================

-  `Quick Start User Guide <https://slurm.schedmd.com/quickstart.html>`__
   at https://slurm.schedmd.com/.
-  `SLURM: Simple Linux Utility for Resource
   Management <https://slurm.schedmd.com/>`__
