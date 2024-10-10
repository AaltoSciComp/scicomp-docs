==========================================
Monitoring job progress and job efficiency
==========================================

.. include:: /triton/ref/videos.rst

.. admonition:: Abstract

   * You must always monitor jobs to make sure they are using all the
     resources you request.
   * Test scaling: double resources, if it doesn't run almost twice as
     fast, it's not worth it.
   * ``seff JOBID`` shows efficiency and performance of a single jobs
   * ``slurm queue`` shows waiting and running jobs (this is a custom command)
   * ``slurm history`` shows completed jobs (also custom command)
   * GPU efficiency: A job's ``TRESUsageInAve`` field shows GPU
     performance info
     and , ``sacct -j JOBID -o TRESUsageInAve -p`` shows this. (custom setup
     at Aalto, won't work on others).



Introduction
------------

When running jobs, one usually wants to do monitoring at various
different stages:

- Firstly, when job is submitted, one wants to monitor the position of the
  job in the queue and expected starting time for the job.
- Secondly, when job is running, one wants to monitor the jobs state and
  how the simulations is performing.
- Thirdly, once the job has finished, one wants to monitor the job's
  performance and resource usage.

There are various tools available for each of these steps.

.. seealso::

   Please ensure you have read :doc:`interactive` and :doc:`serial`
   before you proceed with this tutorial.

.. highlight:: shell-session



Monitoring during queueing
--------------------------

The command ``slurm q``/``slurm queue`` (or ``squeue -u $USER``) can be used
to monitor the status of your jobs in the queue. An example output is given below::

  $ slurm q
  JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
  60984785           interacti _interactive          0:29 2021-06-06T20:41  RUNNING pe6
  60984796           batch-csl hostname              0:00              N/A  PENDING (Priority)

Here the output are as follows:

- ``JOBID`` shows the id number that Slurm has assigned for your job.
- ``PARTITION`` shows the partition(s) that the job has been assigned to.
- ``NAME`` shows the name of the submission script / job step / command.
- ``TIME`` shows the amount of time of the job has run so far.
- ``START_TIME`` shows the start time of the job. If job isn't currently
  running, Slurm will try to form an estimate on when the job will run.
- ``STATE`` shows the state of the job. Usually it is ``RUNNING`` or ``PENDING``.
- ``NODES`` shows the names of the nodes where the program is running. If the
  job isn't running, Slurm tries to give a reason why the job is not running.


When submitting a job one often wants to see if job starts successfully.
This can be made easier by running ``slurm w q``/``slurm watch queue``
or (``watch -n 15 squeue -u $USER``).
This opens a watcher that prints the output of ``slurm queue`` every 15
seconds. This watcher can be closed with ``<CTRL> + C``. Do remember to
close the watcher when you're not watching the output interactively.

To see all of the information that Slurm sees, one can use the command
``scontrol show -d jobid JOBID``.

The ``slurm queue`` is a wrapper built around ``squeue``-command. One can also
use it directly to get more information on the job's status. See
`squeue's documentation <https://slurm.schedmd.com/squeue.html>`_ for more
information.

There are other commands to ``slurm`` that you can use to monitor the
cluster status, job history etc.. A list of examples is given below:

.. admonition:: Slurm status info reference
   :class: toggle

   .. include:: ../ref/slurm_status.rst



Monitoring a job while it is running
------------------------------------

As the most common way of using HPC resources is to run non-interactive
jobs, it is usually a good idea to make certain that the program that will be
run will produce some output that can be used to monitor the jobs' progress.

The typical way of monitoring the progress is to add print-statements that produce
output to the standard output. This output is then redirected to the Slurm
output file (``-o FILE``, default ``slurm-JOBID.log``) where it can be
read by the user.  This file is updated while the job is running, but after some
delay (every few KB written) because of buffering.

It is important to differentiate between different types of output:

- **Monitoring output** is usually print statements and it describes what the
  program is doing (e.g. "Loading data", "Running iteration 31"), what is
  the state of the simulation (e.g. "Total energy is 4.232 MeV",
  "Loss is 0.432") and to get timing information (e.g. "Iteration 31 took
  182s"). This output can then be used to see if the program works, if the
  simulation converges and to determine how long does it take to do different
  calculations.
- **Debugging output** is similar to monitoring output, but it is usually
  more verbose and writes the internal state of the program (e.g. values of
  variables). This is usually required during development stage of a program,
  but once the program works and longer simulations are needed, printing
  debugging output is not recommended.
- **Checkpoint output** can be used to resume the current state of the
  simulation in the case of unexpected situations such as bugs, network problems
  or hardware failures. These should be in binary data as this keeps the
  accuracy of the floating point numbers intact. In big simulations checkpoints
  can be large, so the frequency of taking checkpoints should not be too high.
  In iterative processes e.g. Markov chain, taking checkpoints can be very quick
  and can be done more frequently. In smaller applications it is usually good
  to take checkpoints if the program starts a different phase of the simulation
  (e.g. plotting after simulation). This minimizes loss of simulation time due
  to programming bugs.
- **Simulation output** is something that the program outputs when the simulation
  is done. When doing long simulations it is important to consider what output
  parameters do you want to output. One should include all parameters that
  might be needed so that the simulations do not need to be run again. When
  doing time series output this is even more important as e.g. averages,
  statistical moments cannot necessarily be recalculated after the simulation
  has ended. It is usually good idea to save a checkpoint at the end as well.

When creating monitoring output it is usually best to write it in a
human-readable format and human-readable quantities. This makes it easy to see
the state of the program.



Checking job history after completion
-------------------------------------

The command ``slurm h``/``slurm history`` can be used to check the history
of your jobs. Example output is given below::

  $ slurm h
  JobID         JobName              Start            ReqMem  MaxRSS TotalCPUTime    WallTime Tasks CPU Ns Exit State Nodes
  60984785      _interactive         06-06 20:41:31    500Mc       -    00:01.739    00:07:36  none   1 1   0:0 CANC  pe6
    └─ batch    *                    06-06 20:41:31    500Mc      6M    00:01.737    00:07:36     1   1 1   0:0 COMP  pe6
    └─ extern   *                    06-06 20:41:31    500Mc      1M    00:00.001    00:07:36     1   1 1   0:0 COMP  pe6
  60984796      hostname             06-06 20:49:36    500Mc       -    00:00.016    00:00:00  none  10 10  0:0 CANC  csl[3-6,9,14,17-18,20,23]
    └─ extern   *                    06-06 20:49:36    500Mc      1M    00:00.016    00:00:01    10  10 10  0:0 COMP  csl[3-6,9,14,17-18,20,23]

Here the output are as follows:

- ``JobID`` shows the id number that Slurm has assigned for your job.
- ``JobName`` shows the name of the submission script / job step / command.
- ``Start`` shows the start time of the job.
- ``ReqMem`` shows the amount of memory requested by the job. The format is an
  an amount in megabytes or gigabytes followed by ``c`` or ``n`` for memory per
  core or memory per node respectively.
- ``MaxRSS`` shows the maximum memory usage of the job as calculated by Slurm.
  This is measured in set intervals.
- ``TotalCPUTime`` shows the total CPU time used by the job. It shows the
  amount of seconds the CPUs were at full utilization. For single CPU jobs,
  this should be close to the ``WallTime``. For jobs that use multiple CPUs,
  this should be close to the number of CPUs reserved times ``WallTime``.
- ``WallTime`` shows the runtime of the job in seconds.
- ``Tasks`` shows the number of MPI tasks reserved for the job.
- ``CPU`` shows the number of CPUs reserved for the job.
- ``Ns`` shows the number of nodes reserved for the job.
- ``Exit State`` shows the `exit code <https://tldp.org/LDP/abs/html/exit-status.html>`_
  of the command. Successful run of the program should return 0 as the exit code.
- ``Nodes`` shows the names of the nodes where the program ran.

The ``slurm history``-command is a wrapper built around ``sacct``-command. One
can also use it directly to get more information on the job's status. See
`sacct's documentation <https://slurm.schedmd.com/sacct.html>`_ for more
information.

For example, command
``sacct --format=jobid,elapsed,ncpus,ntasks,state,MaxRss --jobs=JOBID``
which will show information as indicated in the ``--format`` option (jobid,
elapsed time, number of reserved CPUs, etc.). You can specify any field of
interest to be shown using ``--format``.

.. _monitoring-seff:

CheckingCPU and RAM efficiency after completion
-----------------------------------------------

.. include:: ../examples/monitoring/seff.rst



Monitoring a job's GPU utilization
----------------------------------

.. seealso::

  :doc:`gpu`.  We will talk about how to request GPUs later, but it's
  kept here for clarity.

.. include:: ../examples/monitoring/gpu.rst



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Monitoring-1: Adding more verbosity into your scripts

   ``echo`` is a shell command which prints something - the equivalent of "print debugging".

   ``date`` is a shell command that prints the current date and time. It is useful for getting
   timestamps.

   Modify one of the scripts from :doc:`serial` with a lot of ``echo MY LINE OF TEXT`` commands
   to be able to verify what it's doing.  Check the output.

   Now change the script and add ``date``-command below the ``echo``-commands.
   Run the script and check the output. What do you see?

   Now change the script, remove the echos, and add "set -x" below the
   ``#SBATCH``-comments. Run the script again. What do you see?

   .. solution::

      Using ``echo``-commands is a good way of verifying what part
      of the script is being executed.

      Using ``date``-commands in your script is a good way of checking
      when something was executed.

      Using ``set -x`` will cause the shell to print every command it
      executes before it executes them. It is useful for debugging
      complex scripts with if-else-clauses, where you might not know
      what is exactly being executed:

      .. code-block:: slurm

	 #!/bin/bash
	 #SBATCH --time=0:10:00

	 set -x

	 srun python3 slurm/pi.py 10000

      The output (notice the ``+srun python3 ...`` line.  This is
      automatically printed right before the command runs.)::

	 $ cat slurm-19207417.out
	 + srun python3 slurm/pi.py 10000
	 Calculating pi via 10000 stochastic trials
	 {"pi_estimate": 3.126, "iterations": 10000, "successes": 7815}


.. exercise:: Monitoring-2: Basic monitoring example

   Using our standard ``pi.py`` example,

     a. Create a slurm script that runs the algorithm with 100000000 (:math:`10^8`)
        iterations. Submit it to the queue and use ``slurm queue``,
        ``slurm history`` and ``seff`` to monitor the job's performance.
     b. Add multiple job steps (separate ``srun`` lines), each of which runs
        the algorithm ``pi.py`` with increasing number of iterations (from range
        100 - 10000000 (:math:`10^7`). How does this appear in
        ``slurm history``?

.. exercise:: Monitoring-3: Using ``seff``

     Continuing from the example above,

     c. Use ``seff`` to check performance of individual job steps. Can you
        explain why the CPU utilization numbers change between steps?

     This is really one of the most important take-aways from this
     lesson.

     .. solution::

        Using ``seff JOBID.STEPID`` allows you to check efficiency of specific steps.
        You should see that steps with low number of iterations had very low cpu
        efficiency, while higher amount of iterations had better efficiency.

        The important thing to note here is that each srun step has to finish before
        next one can start. This means if you have steps with different resource
        requirements in one job, lot of the resources you requested will be going to waste.


.. exercise:: Monitoring-4: Multiple processors

   The script ``pi.py`` has been written so that it can be run using
   multiple processors. Run the script with multiple processors and
   :math:`10^8` iterations with::

     $ srun --cpus-per-task=2 python3 pi.py --nprocs=2 100000000

   After you have run the script, do the following:

    a. Use ``slurm history`` to check the ``TotalCPUTime`` and
       ``WallTime``. Compare them to the timings for the single CPU
       run with :math:`10^8` iterations.
    b. Use ``seff`` to check CPU performance of the job.


.. exercise:: Monitoring-5: No output

  You submit a job, and it should be writing some stuff to the output.
  But nothing is appearing in the output file.  What's wrong?

  .. solution::

    If it's only been a few minutes, output is probably still
    buffered.  This happens to avoid writing to disk for every line,
    which would otherwise slow down a program a lot.

    FYI, interactive programs are usually line-buffered (display to
    terminal after each line) and non-interactive programs usually
    fully buffered (output after every few kB.)  Search "[language]
    flush buffers" to see how to force it to write sooner - but remove
    this after debugging!



What's next?
------------

Next tutorial is about different ways of doing :doc:`parallel computing <parallel>`.
