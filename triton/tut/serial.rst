===========
Serial jobs
===========

Introduction
============

Triton is a large system that combines many different individual
computers.  At the same time, hundreds of people are using it.  Thus, we
must use a batch queuing system (slurm) in order to allocate resources.

The queue system takes computation requests from everyone, figures out
the optimal use of resources, and allocates code to nodes.  You have to
start your code in a structured way in order for this to work.  Our
`Slurm commands <LINK/Slurm%20commands>`__

The same parameters can be used in

-  The sbatch script, prefixed by ``#SBATCH``
-  The ``sbatch`` command line program directly (like ``-p debug``
   above)
-  ``sinteractive``/``srun`` from the command line, which lets you run
   programs without a batch script.

It is important to note that slurm is a declarative system.  You declare
what you need, and slurm handles finding the resources without you
having to worry about details.  The more resources you request, the
harder it will be to schedule and the longer you may have to wait.  So,
you should ask for what you need to ensure it runs, but after you get
experience with your code reduce resources to just what is needed.

In general, you don't want to go submitting too short jobs (under 5
minutes) because there is a lot of startup, accounting, and scheduling
overhead.  If you are testing, short things are fine, but once you get
to bulk production try to have each job take at least 30 minutes if
possible.  If you have lots of things to run, combine them into fewer
jobs.

Status of the jobs
==================

Once you submit jobs, it goes into a queue.  You need to be able to see
the status of jobs.  There are commands to do this.

+--------------------------------------+----------------------------------------------------+
| Command                              |                                                    |
+======================================+====================================================+
| slurm j <jobid>                      | Status on single job (still running)               |
+--------------------------------------+----------------------------------------------------+
| slurm history [2hours\|5days\|...]   | Info on completed jobs, including mem/cpu usage.   |
+--------------------------------------+----------------------------------------------------+

See the full list of status commands on the reference page

 

Partitions
==========

There are different *partitions*, which have different limits.  The
"debug" partition is for short debugging, so is designed to always be
available.  The "batch" partition is designed for all the normal long
jobs.  There are also partitions for GPUs, huge memory nodes,
interactive shells, and so on.  Most of the time, you should leave the
partition off, and slurm will use all possible partitions.  You can
specify your partitions with "``-p PARTITION_NAME``" to whatever command
you are running, which is mainly needed if you want to force interactive
or GPU partitions.  The available partitions are listed below and on the
reference page.  For the fastest running, consider if you code can be
right below one of the limits you see here.

true\ `Slurm partitions <LINK/Slurm%20partitions>`__

 

Next steps
==========

There is a full description of `running jobs on
Triton <LINK/Running%20programs%20on%20Triton>`__, and the `reference
page <LINK/Reference>`__ lists many useful commands.

 
