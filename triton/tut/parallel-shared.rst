===========================================================
Shared memory parallelism: multithreading & multiprocessing
===========================================================


.. admonition:: Abstract

   * Verify that your program can utilize multiple CPUs.

   * Use ``--cpus-per-task=C`` to reserve multiple CPUs for your job.

   * If you use ``srun`` to launch your program in your sbatch-script and
     want your program to utilize all of the allocated CPUs, run
     ``export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK`` in your script
     before calling ``srun``.

   * You must always :doc:`monitor jobs <monitoring>` to make sure they are using all the
     resources you request (``seff JOBID``).

   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.



What is shared memory parallelism?
----------------------------------

In shared memory parallelism a program will launch multiple processes
or threads so that it can leverage multiple CPUs available in the machine.

**Slurm reservations for both methods behave similarly.** This document
will talk about processes, but everything mentioned would be applicable to threads
as well. See section on
:ref:`difference between processes and threads<threads-vs-processes>`
for more information on who proceseses and threads differ.

Communication between processes happends via shared memory. This means
that all processes need to run on the same machine.

.. figure:: /images/parallel-shared.png
    :width: 80%
    :align: center


Depending on a program, you might have multiple processes (Matlab parallel
pool, R parallel-library, Python multiprocessing) or have multiple threads
(OpenMP threads of BLAS libraries that R/numpy use).



Running a typical multiprocess program
--------------------------------------

Reserving resources for shared memory programs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reserving resources for shared memory programs is easy: you'll only need to
specify how many CPUs you want via ``--cpus-per-task=C``-flag.

For most programs using ``--mem=M`` is the correct way to reserve memory,
but in some cases the amount of memory needed scales with the number of
processors. This might happen, for example, if each process opens a different
dataset or runs its own simulation that needs extra memory allocations.
In these cases you can use ``--mem-per-core=M`` to specify a memory allocation
that scales with the number of CPUs. We recommend starting with ``--mem=M``
if you do not know how your program scales.

Running an example shared memory parallel program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this example, let's consider
`pi.py <https://github.com/AaltoSciComp/hpc-examples/blob/master/slurm/pi.py>`_-example
from the
`hpc-examples <https://github.com/AaltoSciComp/hpc-examples>`_-repository.
It estimates pi using Monte Carlo methods and can utilize multiple processes for calculating
the trials.

You can clone the repository with ``git clone https://github.com/AaltoSciComp/hpc-examples.git``.

The script is in the ``slurm``-folder. You can call the script with
``python pi.py --nprocs=C N``, where ``N`` is the number of iterations to be done by the
algorithm and ``C`` is the number of processors to be used for the parallel calculation.

Let's run the program with two processes using ``srun``::

  srun --cpus-per-task=2 --time=00:10:00 --mem=1G python pi.py --nprocs=2 1000000

**It is vitally important to notice that the program needs to be told the amount of
processes it should use.** The program does not obtain this information from the
queue system automatically. For more information, see the section on
:ref:`CPU over- and undersubscription<cpu-mismatch>`.

Using a slurm script setting the number becomes easier:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:10:00
   #SBATCH --mem=1G
   #SBATCH --output=pi.out
   #SBATCH --cpus-per-task=2

   python pi.py --nprocs=$SLURM_CPUS_PER_TASK 1000000

Let's call this script ``pi-sharedmemory.sh``. You can submit it with::

  sbatch pi-sharedmemory.sh

The environment variable ``$SLURM_CPUS_PER_TASK`` is set during program runtime
and it is set based on the number of ``--cpus-per-task`` requested. For more tricks
on how to set the number of processors, see the
:ref:`section on using it effectively<effective-cpus-per-task>`.



Special cases and common pitfalls
---------------------------------

Monitoring CPU utilization for parallel programs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/monitoring/seff.rst



.. _threads-vs-processes:

Multithreaded vs. multiprocess and double-booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Processes are individual program executions while threads are basically
small work executions within a process. Processes have their own memory
allocations and can work independently from the main process. Threads, on the
other hand, are smaller parallel executions within the main process.
Processes are slower to launch, but due to their independent nature
they won't block each other's execution as easily as threads can.

Some programs can utilize both multithread and multiprocess
parallelism. For example, R has parallel-library for running multiple
processes while BLAS libraries that R uses can utilize multiple threads.

When running a program that can parallelise through processes and through
threads, you should be careful to check that only one method of
parallisation is in effect.

Using both can result in double-booked parallelism where you launch
:math:`N` processes and each process launches :math:`N` threads, which
results in :math:`N^2` threads. This will usually tank the performance
of the code as the CPUs are overbooked.

Often threading is done in a lower level library when they have been
implemented using OpenMP. If you encounter bad performace or you
see a huge number of threads appearing when you use parallel processes
try setting ``export OMP_NUM_THREADS=1`` in your Slurm script.



.. _cpu-mismatch:

Over- and undersubscription of CPUs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of threads/processes you launch should match the
number of requested processors. If you create a lower number, you will
not utilize all CPUs. If you launch a larger number, you will
oversubscribe the CPUs and the code will run slower as different
threads/processes will have to swap in/out of the CPUs and compete
for the same resources.

Using threads and processes at the same time can also result in
:ref:`double-booking<threads-vs-processes>`.



.. _effective-cpus-per-task:

Using SLURM_CPUS_PER_TASK effectively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The environment variable ``$SLURM_CPUS_PER_TASK`` can be utilized in multiple
ways in your scripts. Below are few examples:

- Setting a number of workers when ``$SLURM_CPUS_PER_TASK``  is not set:

  ``$SLURM_CPUS_PER_TASK`` is only set when ``--cpus-per-task`` has 
  been specified. If you want to run the same code in your own machine
  and in the cluster it might be useful to set a variable like
  ``export NCORES=${SLURM_CPUS_PER_TASK:-4}`` and use that in your scripts.

  Here ``$NCORES`` is set to the number specified by ``$SLURM_CPUS_PER_TASK``
  if it has been set. Otherwise, it will be set to 4 via Bash's syntax for
  setting default values for unset variables.

- In Python you can use the following for obtaining the environment
  variable:

  .. code-block:: python

      import os

      ncpus=int(os.environ.get("SLURM_CPUS_PER_TASK", 1))

  For more information on parallelisation in Python see our
  :doc:`Python documentation </triton/apps/python>`.

- In R you can use the following for obtaining the environment
  variable:

  .. code-block:: r

      ncpus <- as.integer(Sys.getenv("SLURM_CPUS_PER_TASK", unset=1))

  For more information on parallelisation in R see our
  :doc:`R documentation </triton/apps/r>`.

- In Matlab you can use the following for obtaining the environment
  variable:

  .. code-block:: matlab

      ncpus=str2num(getenv("SLURM_CPUS_PER_TASK"))

  For more information on parallelisation in Matlab see our
  :doc:`Matlab documentation </triton/apps/matlab>`.


Lack of parallelisation when using srun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since Slurm version 22.05, job steps run with ``srun`` will not
automatically inherit the ``--cpus-per-task``-value that is requested
by ``sbatch``. This was done to make it easier to start multiple job
steps with different CPU allocations within one job.

If you want to give all CPUs to ``srun`` you can either call ``srun``
in the script with ``srun --cpus-per-task=$SLURM_CPUS_PER_TASK`` or
set:

.. code-block:: sh

     export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK


For more information see documentation pages for
`srun <https://slurm.schedmd.com/srun.html>`_ and
`sbatch <https://slurm.schedmd.com/sbatch.html>`_.


Asking for multiple tasks when code does not use MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normally you should **not** use ``--ntasks=n`` when you want to
run shared memory codes. The number of tasks is only relevant to MPI codes
and by specifying it you might launch multiple copies of your program
that all compete on the reserved CPUs.

Only hybrid parallelization codes should have both ``--ntasks=n`` and
``--cpus-per-task=C`` set to be greater than one.



What's next?
------------

The next tutorial is about :doc:`MPI parallelism <parallel-mpi>`.

