===========
Serial Jobs
===========


Introduction to batch scripts
=============================

You learned, in the :doc:`interactive jobs <interactive>`
how all Triton users must do their computation by submitting jobs
to the Slurm batch system to ensure efficient resource sharing.

You additionally learned the interactive way to submit jobs,
e.g. you could simply have an interative Bash session on a
compute node. This proves useful for tests and debugging.
Slurm jobs, however, are normally batch jobs, meaning that
they are run unattended and asynchronously, without human
supervision.

To create a batch job, you need to create a job script and subsequently
submit it to Slurm. A job script is simply a **shell script**,
e.g. Bash, where you put your **resource requests** and **job steps**.
You will see what these two components are shortly.
You have already seen how to do these interactively; and in this tutorial
you will learn how to bundle them in your job scripts.

.. seealso::

   Please refer to the :doc:`interactive jobs
   <interactive>` tutorial to learn the basics
   of Slurm.

Your first job script
=====================

A job script is simply a shell script (Bash). And so the first line
in the script should be the `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`_ directive (``#!``) followed by the
full path to the executable binary of the shell's interpreter, which is
Bash in our case. What then follow are the resource requests and the job steps.

Let's take a look at the following script

.. code-block:: bash

   #!/bin/bash
   #SBATCH --time=00:05:00
   #SBATCH --mem-per-cpu=100
   #SBATCH --output=/scratch/work/%u/hello.%j.out
   #SBATCH --partition debug

   srun echo "Hello $USER! You are on node $HOSTNAME"

Let's name it ``hello.sh`` (create a file using your editor of choice, e.g.nano;
write the script above and save it)

The symbol ``#`` followed by the *SBATCH* directives are understood
by Slurm as parameters, determining the resource requests.
Here, we have requested a time limit of 5 minutes, along with 100 MB of RAM per CPU.

Resource requests are followed by job steps, which are the actual
tasks to be done. Each ``srun`` is a job step, and appears as a separate row in your
history - which is useful for monitoring.

Having written the script, you need to submit the job to Slum through the ``sbatch`` command::

   $ sbatch hello.sh
   Submitted batch job 52428672

.. warning::

   You must use ``sbatch``, not ``bash`` to submit the job
   to process the ``#SBATCH`` headers and run in the background.

When the job enters the queue successfully, the response that the job has been submitted
is printed in your terminal, along with the *job ID* assigned to the job.

You can check the status of you jobs using ``slurm q``::

   $ slurm q
   JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
   52428672           debug     hello.sh              0:00              N/A  PENDING (None)

Once the job is completed successfully, the state changes to *COMPLETED* and the
output is then saved to ``hello.%j.out`` in your work
directory ("%j" is replaced by the jobID).

Setting resource parameters
===========================

In both the above example and the tutorial on :doc:`interactive jobs <interactive>`, you learned
that resources are requested through job parameters such as ``--mem``, ``--time``, etc.

.. seealso::

   See :doc:`interactive jobs <interactive>`, the :doc:`reference
   page <../ref/index>` or the :doc:`details page
   <../usage/general>` for more information and advanced usage.

Please keep in mind that these parameters are hard values. If, for example, you request 5 GB of memory
and your job uses substantially more, Slurm will kill your job.

.. note::

   Actually, there is a little bit of grace period in killing jobs
   (about an hour), and you can go over memory a little bit.  But, if
   you go over the memory limit and the node runs out, you will be the
   first one to be killed!  Don't count on this.

We recommend you be as specific as possible when setting your resource parameters
as they determine how fast your jobs will run.
Therefore, please try to gain more understanding on how much resources your code needs
to fine-tune your requested resources.

.. note::

   In general, please do not submit too short jobs (under 5
   minutes) unless you are debugging. For your bulk production, try to
   have each job take at least 30 minutes, if possible.
   The reason behind this is that there is a big amount of startup, accounting, and scheduling overhead.

Monitoring your jobs
====================

Once you submit your jobs, it goes into a queue. The two most useful commands to see
the status of your jobs with are ``slurm q`` and ``slurm h`` (You've seen both in use).

For example, command ``scontrol show -d jobid <jobid>`` provides you detailed information
on a job. Information such as where *stderr* and *stdout* will be redirected to. These information
can be particularly beneficial for troubleshooting.

Another example could be the command ``sacct --format=jobid,elapsed,ncpus,ntasks,state,MaxRss``
which will show information as indicated in the ``--format`` option (job ID, the elapsed time,
number of occupied CPUs, etc.). You can specify any field of interest to be shown using ``--format``.

You can see more commands below.

.. include:: ../ref/slurm_status.rst

Partitions
==========

A partition is a set of computing nodes dedicated to a specific purpose.
Examples include partitions assigned to debugging("debug" partition),
batch processing("batch" partition), GPUs("gpu" partition), etc.

Command ``sinfo`` lists the available partitions. Let's see the first 4 partitions listed
for the sake of brevity::

   $ sinfo | head -n 5
   PARTITION     AVAIL  TIMELIMIT  NODES  STATE NODELIST
   interactive      up 1-00:00:00      2   drng pe[1-2]
   jupyter-long     up 10-00:00:0      2   drng pe[1-2]
   jupyter-short    up 1-00:00:00      2   drng pe[1-2]
   grid             up 3-00:00:00      1  drain pe76

You can specify a partition to be listed by ``sinfo``::

   $ sinfo --partition=debug
   PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
   debug        up    1:00:00      1 drain* wsm1
   debug        up    1:00:00      1  drain pe3
   debug        up    1:00:00      1   idle pe83

Take a look at the manpage using ``man sinfo`` for more details.

Generally, you don't need to specify the partition; Slurm will
use any posssible partition. However, you can do so with ``-p PARTITION_NAME``
This is mainly needed if you want to force interactive or
debug partition (Slurm usually runs short jobs on the debug partition).

.. seealso::

   You can see the partitions in the :doc:`quick
   reference<../ref/index>`.

Full reference
==============
.. include:: ../ref/slurm.rst

.. seealso::

   There is a full description of `running jobs on
   Triton <../usage/general>`, and the `reference
   page <../ref/index>` lists many useful commands.

Exercises
=========

1. Submit a batch job that just runs ``hostname``.

   a. Set time to 1 hour and 15 minutes, memory to 500MB.
   b. Change the job's name and output file.
   c. Monitor the job with ``slurm watch queue``.
   d. Check the output.  Does it match ``slurm history``?

2. Create a simple batch script using ``pi.py`` based on the pi
   calculation of the :doc:`interactive job tutorial exercises
   <interactive>`.  Create multiple job steps (separate ``srun``
   lines), each of which runs ``pi.py`` with a greater and greater
   number of tries.  How does this appear in ``slurm history``?  When
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

What's next?
============

Running multiple instances of a ``sbatch`` script is easier with
:doc:`array jobs<../tut/array>`.
