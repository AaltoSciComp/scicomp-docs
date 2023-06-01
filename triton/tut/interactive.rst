================
Interactive jobs
================

.. admonition:: Video

   Watch this in our courses: `2022 February <https://www.youtube.com/watch?v=nguLuKJ1gm0&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=12>`__, `2021 January <https://www.youtube.com/watch?v=xhX_u2OA89s&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=11>`__

.. admonition:: Abstract

   * We use the standard (and dominant) Slurm batch queuing system,
     all standard commands will work.
   * See the :doc:`quick reference <../ref/index>` for the reference you
     need if you know Slurm or batch systems already.
   * Interactive jobs allow you to quickly test code (before scaling
     up) or getting more resources for manual analysis.
   * To run a single command interactively

     * ``srun [SLURM OPTIONS] COMMAND ...`` to run before any COMMAND
       to run it in Slurm

   * To get an interactive shell

     * ``srun [SLURM OPTIONS] --pty bash`` (general Slurm)
     * ``sinteractive`` (Triton specific)



.. highlight:: shell-session


Why interactive jobs?
---------------------

There are two ways you can submit your jobs to Slurm queue system:
either interactively using ``srun`` or by submitting a script
using ``sbatch``.  This tutorial walks you through running your jobs
interactively, and :doc:`the next tutorial on serial jobs <serial>`
will go through serial jobs.

Some people say "the cluster is for batch computing", but really it is
to help you get your work done.  **Interactive jobs let you:**

* Run a single job in the Slurm environment to test parameters and
  make sure it works (which is easier than constantly modifying batch
  scripts).

* Get a large amount of resources for some manual data analysis.



Interactive jobs
----------------


Let's say you want to run the following command::

    $ python3 slurm/pi.py 10000

You can submit this program to Triton using ``srun``. All input/output still goes to your terminal
(but note that graphical applications don't work this way - see
below)::

    $ srun --mem=100M --time=0:10:00 python3 slurm/pi.py
    srun: job 52204499 queued and waiting for resources

Here, we are asking for 100 Megabytes of memory (``--mem=100M``) for a
duration of ten minutes (``--time=0:10:00``) (See the :doc:`quick
reference <../ref/index>` or below for more options).
While your job - with **jobid** 52204499 - is waiting to be allocated resources, your shell
blocks while it is waiting to continue.

You can open a new shell (ssh again) on triton and run the command
``squeue -u $USER`` or ``slurm q`` to see all the jobs
you currently have waiting in queue::

  $ slurm q
  JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
  52204499           short-ivb python3               0:00              N/A  PENDING (None)

You can see information such as the state, which partition the requested node reside in, etc.

Once resources are allocated to your job, you see the name of the machine
in the Triton cluster your program ran on, output to your terminal::

  srun: job 52204499 has been allocated resources
  {"pi_estimate": 3.126, "iterations": 10000, "successes": 7815}

To show it's running on a diferent computer, you can ``srun
hostname`` (in this case, it runs on ``csl42``)::

  $ hostname
  login3.triton.aalto.fi
  $ srun hostname
  srun: job 19039411 queued and waiting for resources
  srun: job 19039411 has been allocated resources
  csl42.int.triton.aalto.fi


.. admonition:: Disadvantages

   Interactive jobs are useful for debugging purposes, to test your setup
   and configurations before you put your tasks in a batch script for later execution.

   The major disadvantages include:

   - It blocks your shell until it finishes
   - If your connection to Triton gets interrupted, you lose the job
     and its output.

   Keep in mind that you shouldn't open 20 shells to run 20 ``srun`` jobs at once.
   Please have a look at the :doc:`next tutorial about serial jobs <serial>`.



Interactive shell
-----------------

What if you want an actual shell to do things interactively?
Put more precisely, you want access to a node in the cluster
through an interactive bash shell, with many resources available, that
will let you run commands such as Python and let do some basic work.
For this, you just need srun's ``--pty`` option coupled with the shell
you want::

  $ srun -p interactive --time=2:00:00 --mem=600M --pty bash

The command prompt will appear when the job starts.
And you will have a bash shell runnnig on one of the
computation nodes with at least 600 Megabytes of memory,
for a duration of 2 hours, where you can run your programs in.
The option ``-p interactive`` requests a node in the interactive
**partition** (group of nodes) which is dedicated to interactive usage
(more on this later).

.. warning::

  Remember to exit the shell when you are done!
  The shell will be running if you don't and
  it will count towards your usage.
  This wastes resources and effectively means your priority will degrade
  in the future.

.. note::

  you can use ``sinfo`` to see information such as the available partitions,
  number of nodes in each, their time limits, etc.



Interactive shell with graphics
-------------------------------

``sinteractive`` is very similar to ``srun``, but more clever and thus
allows you to do X forwarding. It starts a `screen session
<https://en.wikipedia.org/wiki/GNU_Screen>`__ on the node,
then sshes to there and connects to the shell::

     $ sinteractive --time=1:00:00 --mem=1000M

.. warning::

  Just like with ``srun --pty bash``, remember to exit the shell.
  Since there is a separate screen session running, just closing the terminal isn't enough.
  Exit all shells in the screen session on the node (C-d or ``exit``) or cancel
  the job.

.. admonition:: Use remote desktop if off campus

  If you are off-campus, you might want to use https://vdi.aalto.fi as a
  virtual desktop to connect to Triton to run graphical programs: ssh
  from there to Triton with ``ssh -XY``.  Graphical programs run very
  slowly when sent across the general Internet.



Checking your jobs
------------------

When your jobs enter the queue, you need to be able to get information
on how much time, memory, etc. your jobs are using in order to know
what requirements to ask for.  We'll see this later in
:doc:`monitoring`.

The command ``slurm history`` (or ``sacct --long | less``) gives you
information such as the actual memory used by your recent jobs, total
CPU time, etc.  You will learn more about these commands later on.

As shown in a previous example, the command ``slurm queue`` (or
``squeue -u $USER``) will tell you the currently running processes,
which is a good way to make sure you have stopped everything.



Setting resource parameters
---------------------------

Remember to set the resources you need well, otherwise your are
wasting resources and lowering your priority.  We went over this in :doc:`slurm`.



.. _triton-tut-exercise-repo:

Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Interactive-1: Basic Slurm options

   The program ``hpc-examples/slurm/memory-use.py``
   uses up a lot of memory to do nothing.  Let's play with it.
   It's run as follows:
   ``python hpc-examples/slurm/memory-use.py 50M``, where the
   last argument is however much memory you want to eat.  You can use
   ``--help`` to see the options of the program.

   a) Try running the program with ``50M``.

   b) Run the program with ``50M`` and ``srun --mem=500M``.

   c) Increase the amount of memory the Python process tries to use (not the
      amount of memory Slurm allocates).  How much memory can
      you use before the job fails?

   d) Look at the job history using ``slurm history`` - can you see
      how much memory it actually used? - Note that Slurm only measures memory
      every 60 seconds or so.
      To make the program last longer, so that the memory used can be measured,
      give the ``--sleep`` option to the Python process, like this:
      ``python hpc-examples/slurm/memory-use.py 50M --sleep=60`` -
      keep it available.

.. exercise:: Interactive-2: Time scaling

   The program ``hpc-examples/slurm/pi.py``
   calculates pi using a simple stochastic algorithm.  The program takes
   one positional argument: the number of trials.

   The ``time`` program allows you to time any program,  e.g. you can
   ``time python x.py`` to print the amount of time it takes.

   a) Run the program, timing it with ``time``, a few times,
      increasing the number of trials, until it takes about 10
      seconds: ``time python hpc-examples/slurm/pi.py
      500``, then 5000, then 50000, and so on.

   b) Add ``srun`` in front (``srun python ...``).  Use the ``seff JOBID``
      command to see how much time the program took to run.
      (If you'd like to use the ``time`` command, you can run
      ``srun --mem=MEM --time=TIME time python hpc-examples/slurm/pi.py ITERS``)

   c) Look at the job history using ``slurm history`` - can you see
      how much time each process used?  What's the relation between
      TotalCPUTime and WallTime?

.. exercise:: Interactive-3: Info commands

   Run ``squeue -a`` to see what is running, and then run ``slurm job
   JOBID`` on some running job - does anything look interesting?

.. exercise:: Interactive-4: Showing node information

   Run ``scontrol show node csl1``  What is this?  (``csl1`` is the
   name of a node on Triton - if you are not on Triton, look at the
   ``sinfo -N`` command and try one of those names).

.. exercise:: Interactive-5: Why not script ``srun``

   Some people are clever and use shell scripting to run ``srun`` many
   times in a loop (using ``&`` to background it so that they all run
   at the same time).  Can you list some advantages and disadvantages
   to this?

  .. solution::

    In does work, but it's fragile: if the login node dies, everything
    gets lost.  It's actually more work than doing it properly
    (:doc:`array`).  And Slurm knows all array jobs are the same, so
    it takes less resources to manage them - if someone scripts too
    many ``srun``\ s, it can actually block other jobs from running
    when they could otherwise.


What's next?
------------

In the next tutorial on `serial batch jobs <serial>`, you will learn how to put the above-mentioned
commands in a script, namely a batch script (a.k.a submission script)
that allows for a multitude of jobs to run unattended.
