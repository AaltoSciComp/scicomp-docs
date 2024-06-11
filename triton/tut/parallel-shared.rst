===========================================================
Shared memory parallelism: multithreading & multiprocessing
===========================================================

.. include:: /triton/ref/videos.rst

.. admonition:: Abstract

   * Verify that your program can use multiple CPUs.

   * Use ``--cpus-per-task=C`` to reserve ``C`` CPUs for your job.

   * In your program set the number of used CPUs to match the number
     of requested CPUs. You can use ``$SLURM_CPUS_PER_TASK`` environment
     variable to get this number dynamically.

   * You must always :doc:`monitor jobs <monitoring>` to make sure they are using all the
     resources you request (``seff JOBID``).

   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.

.. figure:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/cluster-schematic/cluster-schematic-sharedmem.png
   :alt: Schematic of cluster with current discussion points highlighted; see caption or rest of lesson.

   Shared-memory parallelism and multiprocessing lets you scale to the
   size of one node.  For purposes of illustration, the picture isn't
   true to life: we call the whole stack one node, but in reality each
   node is one of the rows.

.. highlight:: console



What is shared memory parallelism?
----------------------------------

In shared memory parallelism a program will launch multiple processes
or threads so that it can leverage multiple CPUs available in the machine.

**Slurm reservations for both methods behave similarly.** This document
will talk about processes, but everything mentioned would be applicable to threads
as well. See section on
:ref:`difference between processes and threads <threads-vs-processes>`
for more information on who proceseses and threads differ.

Communication between processes happens via shared memory. This means
that all processes need to run on the same machine.

.. figure:: /images/parallel-shared.svg
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


For this example, let's again use the
`slurm/pi.py <https://github.com/AaltoSciComp/hpc-examples/blob/master/slurm/pi.py>`__
-script that estimates pi with Monte Carlo methods.

To utilize parallelism written into the script you can run it with the arguments
``python3 slurm/pi.py --nprocs=C N``, where ``N`` is the number of iterations to be done by the
algorithm and ``C`` is the number of processors to be used for the parallel calculation.

Let's run the program with two processes using ``srun``::

  $ srun --cpus-per-task=2 --time=00:10:00 --mem=1G python3 slurm/pi.py --nprocs=2 1000000

**It is vitally important to notice that the program needs to be told the amount of
processes it should use.** The program does not obtain this information from the
queue system automatically. If the program does not know how many CPUs to use, it
might try to use too many or too few. For more information, see the section on
:ref:`CPU over- and undersubscription <cpu-mismatch>`.

Using a slurm script giving the number of CPUs to the program becomes easier:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:10:00
   #SBATCH --mem=1G
   #SBATCH --output=pi.out
   #SBATCH --cpus-per-task=2

   srun python3 slurm/pi.py --nprocs=$SLURM_CPUS_PER_TASK 1000000

Let's call this script ``pi-sharedmemory.sh``. You can submit it with::

  $ sbatch pi-sharedmemory.sh

The environment variable ``$SLURM_CPUS_PER_TASK`` is set during program runtime
and it is set based on the number of ``--cpus-per-task`` requested. For more tricks
on how to set the number of processors, see the
:ref:`section on using it effectively <effective-cpus-per-task>`.


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

Using ``$SLURM_CPUS_PER_TASK`` is the best way of letting your program
know how many CPUs it should use.
See :ref:`section on using it effectively <effective-cpus-per-task>`
for more information.



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



Asking for multiple tasks when code does not use MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normally you should **not** use ``--ntasks=n`` when you want to
run shared memory codes. The number of tasks is only relevant to MPI codes
and by specifying it you might launch multiple copies of your program
that all compete on the reserved CPUs.

Only hybrid parallelization codes should have both ``--ntasks=n`` and
``--cpus-per-task=C`` set to be greater than one.



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Shared memory parallelism 1: Test the example's scaling

   Run the example with a bigger number of trials (``100000000`` or :math:`10^{8}`)
   and with 1, 2 and 4 CPUs.  Check the running time and CPU
   utilization for each run.

   .. solution::

      You can run the program without parallelization with:

      .. code-block:: bash

         srun --time=00:10:00 --mem=1G python3 slurm/pi.py 100000000

      Afterwards you can use ``seff JOBID`` to get the utilization.
      You can run the program with multiple CPUs with:

      .. code-block:: bash

         srun --cpus-per-task=2 --time=00:10:00 --mem=1G python3 slurm/pi.py --nprocs=2 100000000
         srun --cpus-per-task=4 --time=00:10:00 --mem=1G python3 slurm/pi.py --nprocs=4 100000000

      You should see that the time needed to run the program
      ("Job Wall-clock time") ) is basically
      divided by the number of processors while the CPU utilization
      time ("CPU Utilized") remains the same.

.. exercise:: Shared memory parallelism 2: Test scaling for a program that has a serial part

   ``pi.py`` can be called with an argument ``--serial=0.1`` to run a
   fraction of the trials in a serial fashion (here, 10%).

   Run the example with a bigger number of trials (``100000000`` or :math:`10^{8}`),
   4 CPUs and a varying serial fraction (``0.1``, ``0.5``, ``0.8``). Check the running time and CPU
   utilization for each run.

   .. solution::

      You can run the program with 10% serial execution using the following:

      .. code-block:: bash

         srun --cpus-per-task=4 --time=00:10:00 --mem=1G python3 slurm/pi.py --serial=0.1 --nprocs=4 100000000

      Afterwards you can use ``seff JOBID`` to get the utilization.

      Doing the run with different serial portion should show that a bigger the
      serial portion, the less benefit the parallelization gives.


.. exercise:: Shared memory parallelism 3: More parallel :math:`\neq` fastest solution

   ``pi.py`` can be called with an argument ``--optimized`` to run an optimized
   version of the code that utilizes `NumPy <https://numpy.org/>`__
   for vectorized calculations.

   Run the example with a bigger number of trials (``100000000`` or :math:`10^{8}`) and with
   4 CPUs. Now run the optimized example with the same amount of trials and with 1 CPU.
   Check the CPU utilization and running time for each run.

   .. solution::

      You can run the program with 4 CPUs using the following:

      .. code-block:: bash

         srun --cpus-per-task=4 --time=00:10:00 --mem=1G python3 slurm/pi.py --nprocs=4 100000000

      You can run the optimized version with the following:

      .. code-block:: bash

         srun --time=00:10:00 --mem=1G python3 slurm/pi.py --optimized 100000000

      Afterwards you can use ``seff JOBID`` to get the utilization.

      The optimized version, which uses NumPy to create a big batch of random numbers at a time
      and calculates the hits for all of the random numbers at a same time should be significantly
      faster. NumPy itself uses libraries written in C and Fortran that make the calculations
      a lot faster than Python would.

      Using libraries and coding practices that are better suited for the task can
      provide bigger performance boost that using multiple CPUs.

.. exercise:: Shared memory parallelism 4: Your program

   Think of your program. Do you think it can use shared-memory parallelism?

   If you do not know, you can check the program's documentation for words such as:

   - nprocs
   - nworkers
   - num_workers
   - njobs
   - OpenMP
   - ...

   These usually point towards some method of shared-memory parallel execution.



What's next?
------------

The next tutorial is about :doc:`MPI parallelism <parallel-mpi>`.
