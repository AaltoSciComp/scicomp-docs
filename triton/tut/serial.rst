===========
Serial Jobs
===========

Introduction
============

Triton is a large system that combines many different individual
computers. At the same time, hundreds of people are using it. Thus, we
must use a batch queuing system (slurm) in order to allocate resources.

The queue system takes computation requests from everyone, figures out
the optimal use of resources, and allocates code to nodes. You have to
start your code in a structured way in order for this to work. Our
`previous tutorial <interactive>` showed how to
run things directly from the command line, without any scripting needed.
Now let's see how to put these into scripts for making things more
automated and reproducible.

A basic script
==============

Let's say we want to run "``echo 'hello world'``". We have to tell the
system how to run it

Simple submission scriptbash

::

    #!/bin/bash
    #SBATCH --time=0-00:05:00    # 5 mins
    #SBATCH --mem-per-cpu=500    # 500MB of memory

    # Defaults to directory of when submitted.  Explicit cd if needed (slurm defaults
    # to submission directory).
    cd $WRKDIR/myproject/

    # output goes into hello.out
    # If you use srun for each command, the mem/cpu usage of each step
    # can be seen individually with "slurm history"
    srun echo 'hello, world'

Then run it with ``sbatch``:

Submit the job

::

    $ sbatch hello.sh

This sends it to the queue to wait. Since the time requested is short,
it will probably run on the debug partition, which is reserved for small
test jobs (see below). Let's see if it is in the queue:

Checking job status

::

    $ slurm q
    JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
    13031249           debug     hello.sh              0:00              N/A  PENDING (None)

Keep rerunning ``slurm q`` until you see it finish.

The output is then saved to ``slurm-13031249.out`` in your current
directory (the number being the job ID).

Job parameters
~~~~~~~~~~~~~~

As you can see, the above script is limited to 5 minutes and 500MB of
memory. All scripts have to have limits, otherwise they can't be
efficiently scheduled. If you exceed the limits, the jobs will be
killed. At least you need to set ``--time``, ``--mem-per-cpu`` or
``--mem``.

See the :doc:`reference page <../ref/index>` or the :doc:`details page
<../usage/general>` for more information and advanced usage.

The same parameters can be used in

-  The sbatch script, prefixed by ``#SBATCH``
-  The ``sbatch`` command line program directly (like ``-p debug``
   above)
-  ``sinteractive``/``srun`` from the command line, which lets you run
   programs without a batch script.

It is important to note that slurm is a declarative system. You declare
what you need, and slurm handles finding the resources without you
having to worry about details. The more resources you request, the
harder it will be to schedule and the longer you may have to wait. So,
you should ask for what you need to ensure it runs, but after you get
experience with your code reduce resources to just what is needed.

In general, you don't want to go submitting too short jobs (under 5
minutes) because there is a lot of startup, accounting, and scheduling
overhead. If you are testing, short things are fine, but once you get to
bulk production try to have each job take at least 30 minutes if
possible. If you have lots of things to run, combine them into fewer
jobs.

Status of the jobs
==================

Once you submit jobs, it goes into a queue. You need to be able to see
the status of jobs. There are commands to do this.

+--------------------------------------+--------------------------------------+
| Command                              |                                      |
+======================================+======================================+
| slurm j <jobid>                      | Status on single job (still running) |
+--------------------------------------+--------------------------------------+
| slurm history [2hours\|5days\|...]   | Info on completed jobs, including    |
|                                      | mem/cpu usage.                       |
+--------------------------------------+--------------------------------------+

See the full list of status commands on the reference page

Partitions
==========

There are different *partitions*, which have different limits. The
"debug" partition is for short debugging, so is designed to always be
available. The "batch" partition is designed for all the normal long
jobs. There are also partitions for GPUs, huge memory nodes, interactive
shells, and so on. Most of the time, you should leave the partition off,
and slurm will use all possible partitions. You can specify your
partitions with "``-p PARTITION_NAME``" to whatever command you are
running, which is mainly needed if you want to force interactive or GPU
partitions. The available partitions are listed below and on the
reference page. For the fastest running, consider if you code can be
right below one of the limits you see here.

.. include:: ../ref/partitions.rst

Exercises
=========

1. Basics

   a.  Submit a batch job
   b. Set time to 1 hour and 15 minutes, memory to 500MB.
   c. Change the job's name and output file
   d. Monitor the job with ``slurm watch queue``

2. Create a simple batch script with multiple job steps (``srun``s):
   e.g. ``hostname``, ``echo Hello, world!``, and ``date``.  How does
   this appear in ``slurm history``.  When would you use extra
   ``srun`` commands, and when not?

3. Create a batch script which does nothing (or some pointless
   operation for a while), for example ``sleep 300`` (wait for 300
   seconds) in the ``debug`` partition.  Check the queue to see when
   it starts running.  Then, cancel the job.  What output is produced?

4. (Advanced) Create a batch script that runs in another language.
   Does it run?  What are some of the advantages and problems here?


Next steps
==========

There is a full description of `running jobs on
Triton <../usage/general>`, and the `reference
page <../ref/index>` lists many useful commands.


