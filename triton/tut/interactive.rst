================
Interactive jobs
================

Introduction to slurm
=====================

Triton is a large system that combines many different individual
computer nodes. Hundreds of people are using Triton simultaneously.
Thus, resources (CPU time, memory, etc.) need to be shared among everyone.

This resource sharing is done by a software called a job scheduler or
workload manager. Triton's workload manager is **slurm**. 
Triton users submit jobs which are then scheduled and allocated
resources by the workload manager. 


There are two ways you can submit your jobs to slurm queue system:
either interactively using ``srun`` or by submitting a script
using ``sbatch``. 

This tutorial walks you through running your jobs interactively.
And in the next tutorial we will go through the more common and
advanced way of submitting jobs, batch scripts.


Your first interactive job
==========================

Let's say you want to run the following program

::

    python3 -c 'import os; print("hi from", os.uname().nodename)'

You can submit this program to Triton using ``srun``. All input/output still goes to your terminal
(but note X forwarding for graphical applications doesn't work - see
below).

:: 

    $ srun --mem=100M --time=1:00:00 python3 -c 'import os; print("hi from", os.uname().nodename)'
    srun: job 52204499 queued and waiting for resources

Here, we are asking for 100 Megabytes of memory for a duration of an hour. 
While your job - with **jobID** 52204499 - is waiting to be allocated resources, your shell
effectively become non-interactive. 

You can open a new shell on triton and run the command ``slurm q`` to see all the jobs
you have submitted to the queue

::

  $ slurm q
  JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
  52204499           short-ivb python3               0:00              N/A  PENDING (None)

You can see information such as the state, which partition the requested node reside in, etc.

.. note::

  The fact that we had to open another shell can be impractical 
  if you need to run other jobs or just simply use the current shell. 
  Additionally, if your shell quits while waiting (your internet may disconnect), 
  the process cancels and you have to run the ``srun`` command again. 

Once resources are allocated to your job, you see the name of the machine
in the Triton cluster your program ran on, output to your terminal

::

  srun: job 52204499 has been allocated resources
  hi from ivb17.int.triton.aalto.fi

.. note::

   Interactive jobs are useful for debugging purposes, to test your setup 
   and configurations before you put your tasks in a batch script for later execution.
   Or if you need graphical applications - such as Matlab, RStudio, etc. 
   Additionally, if your task is small and not worth writing a batch script for, 
   interactive job is the way to go.


Interactive shell
=================

What if you want an actual shell to do things interactively? 
Put more precisely, you want access to a node in the cluster
through an interactive bash shell. 
For this, you just need srun's ``--pty`` option coupled with the shell
you want

::

  srun -p interactive --time=2:00:00 --mem=600 --pty bash 

The command prompt will appear when the job starts.
And you will have a bash shell runnnig on one of the 
computation nodes with at least 600 Megabytes of memory,
for a duration of 2 hours, where you can run your programs in. 

The option ``-p interactive`` requests a node in the interactive
partition which is dedicated to interactive usage (more on this later). 

.. note::

  you can use ``sinfo`` to see information such as the available partitions,
  number of nodes in each, their time limits etc. 

.. warning::
  
  Remember to exit the shell when you are done!
  The shell will be running if you don't and
  it will count towards your usage. 
  This effectively means your priority will degrade
  in the future.
  

Interactive shell with graphics
===============================

``sinteractive`` is very similar to ``srun``, but more clever and thus
allows you to do X forwarding. It starts a screen session on the node, 
then sshes to there and connects to the screen. 
You can also ssh to this node again and connect to the
process again.

::

     sinteractive --time=1:00:00 --mem=1000

.. warning::

  Just like with ``srun --pty bash``, remember to exit the shell.
  Since there is a separate screen session running, just closing the terminal isn't enough. 
  Exit all shells in the screen session on the node (C-d or ``exit``), or cancel
  the process (see below).

.. note::

  If you are off-campus, you might want to use https://vdi.aalto.fi as a
  virtual desktop to connect to Triton to run graphical programs.
  Otherwise, expect things to be very slow.

Monitoring your usage
=====================

When your jobs enter the queue, you need to be able to get
information on how much time, memory, etc. your jobs are using 
in order to know what requirements to ask for. 

The command ``slurm history`` gives you information such as the actual memory used by your recent jobs, total CPU time, etc.
You will learn more about these command later on. 

As shown in a previous example, the command ``slurm queue`` will tell you the currently running processes,
which is a good way to make sure you have stopped everything. 

.. note::
  
  Generally, estimating the amount of time or memory you need comes down to 
  monitoring you slurm history and utilizing command-line tools such as 
  ``time`` on a few of your jobs and averaging. This is basically a trial and error process.

Setting resource parameters
===========================

Slurm comes with a multitude of parameters which you can specify to
ensure you will be allocated enough memory, CPU cores, time, etc.
You saw two of them in use in the above examples (``--mem`` and ``--time``)
and you will learn more in the following tutorials. 

Because you are sharing resource with other users, **you should always estimate the amount of time, memory, etc.
you need and then request them accordingly** for efficiency reasons.
Moreover, the default memory and time limits are intentionally set low and may not be 
sufficient for your jobs to run/finish. 

The general rule of thumb is to request the least possible, so that your stuff can run faster. 
That is because the **less you request, the faster you are likely to be allocated resources.** 
If you request something slightly less than a node size (note that we have different size nodes) 
or partition limit, you are more likely to fit into a spare spot. 

For example, we have many nodes with 12 cores, and some with 20 or 24. If you request 24 cores, 
you have very limited options. However, you are more likely to be allocated a node if you request 10 cores.
The same applies to memory: most common cutoffs are 48, 64, 128, 256GB. 
It's best to use smaller values when submitting interactive jobs, and more for batch scripts.


The `next tutorial <serial>` covers more resource parameters and how to estimate them in more detail. 

Exercises
=========

1. The program ``/scratch/scip/examples/slurm/memory-hog.py``
   uses up a lot of memory to do nothing.  Let's play with it.  It's
   run like this: ``python
   /scratch/scip/examples/slurm/memory-hog.py 50M``, where the
   last argument is however much memory you want to eat.  (also
   available from `triton-examples/slurm
   <https://github.com/AaltoScienceIT/triton-examples/tree/master/slurm>`__)

   a) Try running the program with ``50M``

   b) Run the program with ``50M`` and ``srun --mem=500M``.

   c) Increase the amount of memory allocated until the job fails.
      What happens?

   d) Play around with different parameters: how much memory can you
      use?

   e) Look at the job history using ``slurm history`` - can you see
      how much memory it actually used?

2. The program ``/scratch/scip/examples/slurm/pi.py`` (also
   available from `triton-examples/slurm
   <https://github.com/AaltoScienceIT/triton-examples/tree/master/slurm>`__)
   calculates pi using a simple stochastic algorithm.  You give it one
   argument: the number of trials.

   The ``time`` program allows you to time any program.  e.g. you can
   ``time python x.py`` to print the amount of time it takes.

   a) Run the program, timing it with ``time``, a few times,
      increasing the number of trials, until it takes about 10
      seconds: ``time python /scratch/scip/examples/slurm/pi.py
      500`` and so on.

   b) Add ``srun`` in front (``srun python ...``).  What changes?

   c) Tell srun to use five CPUs (``-c 5``).  Does it go any faster?

   d) Use the ``--threads=5`` option to the Python program to tell it
      to also use five threads.  ``... python .../pi.py --threads=5``

   e) Play around with it some.  What do you find?

   f) Look at the job history using ``slurm history`` - can you see
      how much time each process used?  What's the relation between
      TotalCPUTime and WallTime?

3. Check out some of these commands: ``sinfo``, ``squeue``.  Run
   ``slurm job $jobid`` on some running job - does anything
   look interesting?

4. Run ``scontrol show node wsm1``  What is this?



What's next?
============

In the next tutorial on `serial batch jobs <serial>` you will learn how to put the above-mentioned 
commands in a script, namely a batch script that allows for a multitude of jobs to run unattended. 
