===========
Serial Jobs
===========

.. admonition:: Video

   Watch this in our courses: `2022 February <https://www.youtube.com/watch?v=AJgWuKDSOFY&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=13>`__, `2021 January <https://www.youtube.com/watch?v=I79KLHb-7T0&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=14>`__

.. admonition:: Abstract

   * Batch scripts let you run work non-interactively, which is
     important for scaling.  You create a **batch script**, which runs
     in the background.  You come back later and see the results.

   * Example batch script, submit with ``sbatch the_script.sh``:

     .. code:: slurm

	#!/bin/bash -l
	#SBATCH --time=01:00:00
	#SBATCH --cpus-per-task=2
	#SBATCH --mem=4G

	module load anaconda
	python my_script.py

   * See the :doc:`quick reference <../ref/index>` for complete list
     of options.



.. highlight:: shell-session

Prerequisites
-------------

* :doc:`prerequisites`
* :doc:`connecting`



Why batch scripts?
------------------

You learned, in :doc:`slurm`,
how all Triton users must do their computation by submitting jobs
to the Slurm batch system to ensure efficient resource sharing.  This
lets you run many things at once without having to watch each one
separately - the true power of the cluster.

A batch script is simply a **shell script** (remember
:doc:`cluster-shell`?), where you put your **resource requests** and
**job steps**.



Your first job script
---------------------

A job script is simply a shell script (Bash). And so the first line in
the script should be the `shebang
<https://en.wikipedia.org/wiki/Shebang_(Unix)>`_ directive (``#!``)
followed by the full path to the executable binary of the shell's
interpreter, which is Bash in our case. What then follow are the
resource requests, and then the job steps.

Let's take a look at the following script

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:05:00
   #SBATCH --mem-per-cpu=100M
   #SBATCH --output=hello.out

   echo "Hello $USER! You are on node $HOSTNAME.  The time is $(date)."

   # For the next line to work, you need to be in the
   # hpc-examples directory.
   srun python slurm/pi.py 10000

Let's name it ``hello.sh`` (create a file using your editor of choice,
e.g. ``nano``; write the script above and save it)

The symbol ``#`` is a **comment** in the **bash script**, and Slurm
understands ``#SBATCH`` as parameters, determining the resource
requests. Here, we have requested a time limit of 5 minutes, along
with 100 MB of RAM per CPU.

Resource requests are followed by job steps, which are the actual
tasks to be done. Each ``srun`` within the a slurm script is a job
step, and appears as a separate row in your history - which is useful
for monitoring.

Having written the script, you need to submit the job to Slum through
the ``sbatch`` command.  Since the command is ``python slurm/pi.py``,
you need to be in the hpc-examples directory from our :ref:`sample
project <triton-tut-example-repo>`::

   $ cd hpc-examples       # wherever you have hpc-examples
   $ sbatch hello.sh
   Submitted batch job 52428672

.. warning::

   You must use ``sbatch``, not ``bash`` to submit the job since it is
   Slurm that understands the ``SBATCH`` directives, not Bash.

When the job enters the queue successfully, the response that the job
has been submitted is printed in your terminal, along with the *jobid*
assigned to the job.

You can check the status of you jobs using ``slurm q``/``slurm queue`` (or
``squeue -u $USER``)::

   $ slurm q
   JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
   52428672           debug     hello.sh              0:00              N/A  PENDING (None)

Once the job is completed successfully, the state changes to
*COMPLETED* and the output is then saved to ``hello.out`` in the
current directory. You can also wildcards like ``%u`` for your
username and ``%j`` for the jobid in the output file name. See the
`documentation of sbatch <https://slurm.schedmd.com/sbatch.html>`__
for a full list of available wildcards.



Setting resource parameters
---------------------------

The resources were discussed in :doc:`slurm`, and barely need to be
mentioned again here - the point is they are the same.  Always keep
the :doc:`reference page <../ref/index>` close for looking these up.



Monitoring your jobs
--------------------

Once you submit your jobs, it goes into a queue. The two most useful
commands to see the status of your jobs with are ``slurm q``/``slurm
queue`` and ``slurm h``/``slurm history`` (or ``squeue -u $USER`` and
``sacct -u $USER``).

More information is in the :doc:`monitoring
tutorial<../tut/monitoring>`.



Cancelling a job
----------------

You can cancel jobs with ``scancel JOBID``. To obtain job id, use the
monitoring commands.



Full reference
--------------

The `reference page <../ref/index>` contains it all, or expand it below.

.. admonition:: Slurm quick ref
   :class: toggle

   .. include:: ../ref/slurm.rst




Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Serial-1: Basic batch job

   Submit a batch job that just runs ``hostname``.

   a. Set time to 1 hour and 15 minutes, memory to 500MB.
   b. Change the job's name and output file.
   c. Check the output.  Does the printed hostname
      match the one given by ``slurm history``/``sacct -u $USER``?

.. exercise:: Serial-2: Submitting and cancelling a job

   Create a batch script which does nothing (or some pointless
   operation for a while), for example ``sleep 300``. Check the queue to see
   when it starts running.  Then, cancel the job.  What output is produced?

.. exercise:: Serial-3: Checking output

   Create a slurm script that runs the following program::

     for i in $(seq 30); do
       date
       sleep 10
     done

   a. Submit the job to the queue.
   b. Log out from Triton. Log back in and use
      ``slurm queue``/``squeue -u $USER`` to check the job status.
   c. Use ``cat NAME_OF_OUTPUTFILE`` to check at the output
      periodically.  You can use ``tail -f NAME_OF_OUTPUTFILE`` to
      view the progress in real time as new lines are added (Control-C
      to cancel)
   d. Cancel the job once you're finished.

.. exercise:: (advanced) Serial-4: Why you use ``sbatch``, not ``bash``.

   (Advanced) What happens if you submit a batch script with ``bash`` instead of
   ``sbatch``?  Does it appear to run?  Does it use all the Slurm
   options?

.. exercise:: (advanced) Serial-5: Interpreters other than bash

   (Advanced) Create a batch script that runs in another language
   using a different ``#!`` line.
   Does it run?  What are some of the advantages and problems here?

.. exercise:: (advanced) Serial-6: Job environment variables.

   Either make a ``sbatch`` script that runs the command ``env | sort``, or
   use ``srun env | sort``.  The ``env`` utility prints all
   environment variables, and ``sort`` sorts it (and ``|`` connects
   the output of ``env`` to the input of ``sort``.)

   This will show all of the environment variables that are set in the
   job.  Note the ones that start with ``SLURM_``.  Notice how they
   reflect the job parameters.  You can use these in your jobs if
   needed (for example, a job that will adapt to the number of
   allocated CPUs).

What's next?
============

There are various tools one can use to do
:doc:`job monitoring<../tut/monitoring>`.
