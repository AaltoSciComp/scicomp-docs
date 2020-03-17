===========
Serial Jobs
===========

.. seealso::

   This assumes you have read :doc:`the interactive jobs tutorial
   <interactive>` first.

Introduction
============

Triton is a large system that combines many different individual
computers. At the same time, hundreds of people are using it. Thus, we
must use a batch queuing system (slurm) in order to allocate resources.

The queue system takes computation requests from everyone, figures out
the optimal use of resources, and allocates code to nodes. You have to
start your code in a structured way in order for this to work. Our
:doc:`previous tutorial <interactive>` showed how to
run things directly from the command line, without any scripting needed.

Now let's see how to put these into scripts.  A **shell script** takes
any commands that you might type directly into a shell and automates
them.  The **slurm scripts** that we make in this lesson do do this.
Scripts allow jobs to run asynchronously, in batch, and without human
supervision.



A basic script
==============

Let's say we want to run ``echo 'hello world'``. We have to tell the
system how to run it.  Here is a simple submission script, put it in a
file called ``hello.slrm`` (you can use the editor nano: ``nano
hello.slrm``)::

    #!/bin/bash
    #SBATCH --time=0-00:05:00    # 5 mins
    #SBATCH --mem-per-cpu=500    # 500MB of memory

    srun echo 'hello, world'

**Whatever your application or programming language requires, you put
it in the script.**

Each ``srun`` is a job step, and appears as a separate row in your
history - which is useful for monitoring.  Then submit it with
``sbatch``::

    $ sbatch hello.slrm

.. warning:: You must use ``sbatch``, not ``bash`` to submit the job
   to process the ``#SBATCH`` headers and run in the background.

This sends it to the queue to wait. Since the time requested is short,
it will probably run on the debug partition, which is reserved for small
test jobs (see below). Let's see if it is in the queue:

Checking job status with ``slurm q``::

    $ slurm q
    JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
    13031249           debug     hello.slrm            0:00              N/A  PENDING (None)

Keep rerunning ``slurm q`` until you see it finish.

You can use ``scancel`` with that jobid to cancel the job before it
finishes.

The output is then saved to ``slurm-13031249.out`` in your current
directory (the number being the job ID).



Loading modules in scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~

Need to load modules for your software?  Do it in the batch scripts.
In general, anything you can do from the shell, you can do here::

    #!/bin/bash
    #SBATCH --time=0-00:05:00    # 5 mins
    #SBATCH --mem-per-cpu=500    # 500MB of memory

    module load anaconda
    python -V

**Exercise**: Try the Python version-printing script above.  Try
changing to different modules, ``anaconda2``, ``Python``, and others
if you can find them.



Job parameters
~~~~~~~~~~~~~~

As you can see, the above script is limited to 5 minutes and 500MB of
memory. All scripts have to have limits, otherwise they can't be
efficiently scheduled. If you exceed the limits, the jobs will be
killed. At least you need to set ``--time``, ``--mem-per-cpu`` or
``--mem``.

See the :doc:`previous tutorial <interactive>`, the :doc:`reference
page <../ref/index>` or the :doc:`details page
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
you should ask for enough to make sure your job can complete, but once
you get experience with your code reduce resources to just what is needed.

In general, you don't want to go submitting too short jobs (under 5
minutes) because there is a lot of startup, accounting, and scheduling
overhead. If you are testing, short things are fine, but once you get to
bulk production try to have each job take at least 30 minutes if
possible. If you have lots of things to run, combine them into fewer
jobs.



Full slurm reference
====================

.. include:: ../ref/slurm.rst


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

.. include:: ../ref/slurm_status.rst

See the full list of status commands on the :doc:`reference page
<../ref/index>`.



Partitions
==========

There are different *partitions*, which have different limits. The
"debug" partition is for short debugging, so is designed to always be
available. The "batch" partition is designed for all the normal long
jobs. There are also partitions for GPUs, huge memory nodes, interactive
shells, and so on. Most of the time, you should leave the partition off,
and slurm will use all possible partitions. You can specify your
partitions with ``-p PARTITION_NAME`` to whatever command you are
running, which is mainly needed if you want to force interactive or a
test partition. The available partitions are listed on the
reference page.

You can see the partitions in the :doc:`quick
reference<../ref/index>`.

Exercises
=========

1. Basics

   a. Submit a batch job that just runs ``hostname``.
   b. Set time to 1 hour and 15 minutes, memory to 500MB.
   c. Change the job's name and output file.
   d. Monitor the job with ``slurm watch queue``.
   e. Check the output.  Does it match ``slurm history``?

2. Create a simple batch script using ``pi.py`` based on the pi
   calculation of the :doc:`interactive job tutorial exercises
   <interactive>`.  Create multiple job steps (separate ``srun``
   lines), each of which runs ``pi.py`` with a greater and greater
   number of tries.  How does this appear in ``slurm history``.  When
   would you use extra ``srun`` commands, and when not?

3. Create a batch script which does nothing (or some pointless
   operation for a while), for example ``sleep 300`` (waits for 300
   seconds) in the ``debug`` partition.  Check the queue to see when
   it starts running.  Then, cancel the job.  What output is produced?

4. What happens if you submit a batch script with ``bash`` instead of
   ``sbatch``?  Does it appear to run?  Does it use all the Slurm
   options?

4. (Advanced) Create a batch script that runs in another language.
   Does it run?  What are some of the advantages and problems here?


Next steps
==========

There is a full description of `running jobs on
Triton <../usage/general>`, and the `reference
page <../ref/index>` lists many useful commands.

Running multiple instances of a ``sbatch`` script is easier with
:doc:`array jobs<../tut/array>`.

