===========
Serial Jobs
===========

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=I79KLHb-7T0&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=14>`__

.. admonition:: Generic instructions

   * Batch scripts let you run work non-interactively, which is
     important for scaling.

   * Example batch script:

     .. code:: slurm

	#!/bin/bash -l
	#SBATCH --time=01:00:00
	#SBATCH --mem-per-cpu=1G

	module load anaconda
	python my_script.py

   * See the :doc:`quick reference <../ref/index>` for more.


Introduction to batch scripts
=============================

You learned, in the :doc:`interactive jobs <interactive>`,
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
You will see what these two components are in this tutorial.
You have already seen how to do these interactively; and in this tutorial
you will learn how to bundle them in your job scripts.

.. seealso::

   Please refer to the :doc:`interactive jobs
   <interactive>` tutorial to learn the basics
   of Slurm.

.. highlight:: console

Your first job script
=====================

A job script is simply a shell script (Bash). And so the first line
in the script should be the `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`_ directive (``#!``) followed by the
full path to the executable binary of the shell's interpreter, which is
Bash in our case. What then follow are the resource requests and the job steps.

Let's take a look at the following script

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:05:00
   #SBATCH --mem-per-cpu=100M
   #SBATCH --output=hello.out

   srun echo "Hello $USER! You are on node $HOSTNAME. The time is $(date). "

.. date added to check if submitting multiple times gives different outputs.

Let's name it ``hello.sh`` (create a file using your editor of choice, e.g. ``nano``;
write the script above and save it)

The symbol ``#`` is a comment in a **bash script**, and Slurm
understands ``#SBATCH`` as parameters, determining the resource
requests.
Here, we have requested a time limit of 5 minutes, along with 100 MB of RAM per CPU.

Resource requests are followed by job steps, which are the actual
tasks to be done. Each ``srun`` within the a slurm script is a job
step, and appears as a separate row in your
history - which is useful for monitoring.

Having written the script, you need to submit the job to Slum through
the ``sbatch`` command::

   $ sbatch hello.sh
   Submitted batch job 52428672

.. warning::

   You must use ``sbatch``, not ``bash`` to submit the job
   since it is Slurm that understands the ``SBATCH`` directives,
   not Bash.

When the job enters the queue successfully, the response that the job has been submitted
is printed in your terminal, along with the *jobid* assigned to the job.

You can check the status of you jobs using ``slurm q``/``slurm queue`` (or
``squeue -u $USER``)::

   $ slurm q
   JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
   52428672           debug     hello.sh              0:00              N/A  PENDING (None)

Once the job is completed successfully, the state changes to *COMPLETED* and the
output is then saved to ``hello.out`` in the current directory. You can also
wildcards like ``%u`` for your username and ``%j`` for the jobid in the output
file name. See the
`documentation of sbatch <https://slurm.schedmd.com/sbatch.html>`__ for a full
list of available wildcards.

Setting resource parameters
===========================

In both the above example and the tutorial on :doc:`interactive jobs <interactive>`, you learned
that resources are requested through job parameters such as ``--mem``, ``--time``, etc.

.. seealso::

   See :doc:`interactive jobs <interactive>` or the :doc:`reference
   page <../ref/index>`.

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
the status of your jobs with are ``slurm q``/``slurm queue`` and
``slurm h``/``slurm history`` (or ``squeue -u $USER`` and ``sacct -u $USER``).

More information is in the
:doc:`monitoring tutorial<../tut/monitoring>`.

Cancelling your jobs
====================

You can cancel jobs with ``scancel <jobid>``. To obtain job id, use the
monitoring commands.

Partitions
==========

A **slurm partition** is a set of computing nodes dedicated to a specific purpose.
Examples include partitions assigned to debugging("debug" partition),
batch processing("batch" partition), GPUs("gpu" partition), etc.

Command ``sinfo -s`` lists a summary of the available partitions. For the sake
of brevity, let's see the first 4 partitions

.. tabs::

   .. code-tab:: bash Aalto

           $ sinfo -s | head -n 5
           PARTITION     AVAIL  TIMELIMIT   NODES(A/I/O/T)  NODELIST
           interactive      up 1-00:00:00          4/0/0/4  pe[4-7]
           jupyter-long     up 10-00:00:0          4/0/0/4  pe[4-7]
           jupyter-short    up 1-00:00:00          4/0/0/4  pe[4-7]
           grid             up 3-00:00:00       29/18/1/48  pe[9-48,74-81]

   .. code-tab:: bash Helsinki

         $ sinfo -s | head -n 5
         PARTITION AVAIL  TIMELIMIT   NODES(A/I/O/T)  NODELIST
         short        up 1-00:00:00        31/4/7/42  kac[02-19],kam01,kas[01-23]
         medium       up 7-00:00:00        24/0/2/26  kac[02-08],kas[05-23]
         long         up 14-00:00:0        13/0/1/14  kas[01-04,14-23]
         test*        up      10:00          0/0/1/1  kag01

  

Take a look at the manpage using ``man sinfo`` for more details.

Generally, you don't need to specify the partition; Slurm will
use any posssible partition (though this is Aalto-specific, however
other sites may have other requirements here). However, you can do so
with ``-p PARTITION_NAME``.
This is mainly needed if you want to force interactive or
debug partition (Slurm usually runs short jobs on the debug partition).

.. seealso::

   You can see the partitions in the :doc:`quick
   reference<../ref/index>`.

Full reference
==============

.. include:: ../ref/slurm.rst

.. seealso::

   The `reference page <../ref/index>` lists many useful commands.

Exercises
=========

.. include:: ../ref/examples-repo.rst

1. Submit a batch job that just runs ``hostname``.

   a. Set time to 1 hour and 15 minutes, memory to 500MB.
   b. Change the job's name and output file.
   c. Check the output.  Does the printed hostname
      match the one given by ``slurm history``/``sacct -u $USER``?

2. Create a batch script which does nothing (or some pointless
   operation for a while), for example ``sleep 300``. Check the queue to see
   when it starts running.  Then, cancel the job.  What output is produced?

3. Create a slurm script that runs the following program::

     for i in $(seq 30); do
       date
       sleep 10
     done

   a. Submit the job to the queue.
   b. Log out from Triton. Log back in and use
      ``slurm queue``/``squeue -u $USER`` to check the job status.
   c. Use ``cat name_of_outputfile`` to check at the output periodically.
   d. Cancel the job once you're finished.

4. (Advanced) What happens if you submit a batch script with ``bash`` instead of
   ``sbatch``?  Does it appear to run?  Does it use all the Slurm
   options?

5. (Advanced) Create a batch script that runs in another language
   using a different ``#!`` line.
   Does it run?  What are some of the advantages and problems here?

What's next?
============

There are various tools one can use to do
:doc:`job monitoring<../tut/monitoring>`.
