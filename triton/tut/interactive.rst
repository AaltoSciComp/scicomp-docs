================
Interactive jobs
================

Introduction
============

Triton is a large system that combines many different individual
computers. At the same time, hundreds of people are using it. Thus, we
don't just have machines sitting around to run directly on. You need to
share resources among everyone by applying for them using the queuing
system, slurm. As you will see, this is very fast and lets you get
basically whatever you need.

This page discusses what is necessary to use Triton interactively. This
means no scripts, no overhead. You "**just add srun!**". For the small
jobs that you would use this for, you will almost always get your time
right away. Still, you have to request the resources you need
(time/cores/memory). It also means that if you don't do things
properly, it is inefficient because you request more than you need. You
should start here, but once you need more go to more advanced usage.

.. note::

  Advantages of interactive running:  It's good for getting started
  quickly and scaling up: "just add srun!". It's good when task is so
  small that scripting isn't worth it.

  Downsides include: You have to be there and wait for things to run. If
  your shell connection gets interrupted, you lose the process. If you
  don't stop interactive shells, they will continue it will count against
  your fairshare quota, making your jobs run slower in the future.


Single process
==============

The simplest way is to use srun. Let's say you run some program like
this:

::

    python3 -c 'import os; print("hi from", os.uname().nodename)'

You switch to use srun. All input/output still goes to your terminal
(but note X forwarding for graphical applications doesn't work - see
below for that).

::

    srun --mem=50G --time=5:00:00 python3 -c 'import os; print("hi from", os.uname().nodename)'

This has some possible problems: it is connected to your shell. If your
shell quits, the process gets lost. Also, this runs only one single
process. If you need to do multiple things in a row, then you have to
wait before each one starts. Note: srun is used directly with a command
to run, not batch scripts like sbatch is (though of course you could run
a shell script). srun does not look at the #SBATCH options inside of
scripts.

How do you find the right time/CPU/memory requirements?  Slurm (the
queuing system) has extensive reporting. For example,
``slurm history`` will show you the actual run time and actual memory
used of your job.  You generally make a guess and adjust based on what
you see.  There is a little bit about this below and more in
the next tutorial.


Interactive shell
=================

So, let's say you need to do something a bit fancier: what if you want
an actual shell to do things interactively? You just need the extra
``--pty`` and run ``bash``.  The ``-p interactive`` says "give me a
partition dedicated to interactive usage (more on this later).  Full
example::

    srun -p interactive --time=HH:MM:SS --mem=nnG --pty bash

Now you have a shell... do whatever you need to do. **Close the shell
when you are done!  If you don't, the process will keep running until
your time limit. All of this time will be counted against your usage.
It doesn't cost money, but does mean that your priority will go down in
the future.**  (Note that we specify the interactive partition with "-p
interactive". More on this below.)


Interactive shell with graphics
===============================

sinteractive is very similar to srun, however it is more clever and thus
allows you to do X forwarding. In the background, it starts the job,
starts a screen session on the node, then sshes to there and connects to
the screen. You can also ssh to this node again and connect to the
process again.

::

     sinteractive --time=HH:MM:SS --mem=nnG

**Just like with** ``srun --pty``, **remember to close the process when done.
However, it's even harder than before. Since there is a separate screen
session running, just closing the terminal isn't enough. Exit all
shells in the screen session on the node (C-d or ``exit``), or cancel
the process (see below).**


More options
============

**Time/CPU/memory requirements:** The commands srun/sinteractive have
many more options that let you specific resources. The most important
for interactive running are probably ``--mem``, ``--cpus-per-task`` (``-c``),
and ``--time`` (``-t``).

**How much time/memory/CPU resources should you request?**  The less
you request, the faster you are likely to run. As for all you need, but
not ridiculously large amounts. If you request something slightly less
than a node size (note that we have different size nodes) or partition
limit (see below), you are more likely to fit into a spare spot. We
have many nodes with 12 cores, and some with 20 or 24. If you request
24, you have very limited options. If you request 10, or 18, you will
have a lot more options. Same with memory: most common cutoffs are 48,
64, 128, 256GB. Use smaller values when interactive testing, then more
for batch running overnight.

**Configure your program well:** Also, note that requesting more CPUs
doesn't magically mean that your program becomes parallel. Make sure
you turn that on in your code to enable that. Also specify how many
CPUs to use (matching how many you request with slurm). If you don't
get an entire node, your program might try to use all CPUs, and the OS
will limit the number you can use (with cgroups, if you are
interested). This leads to inefficiency.

**Partitions:** Now almost always automatically set, but used to be
important.  Partitions are groups of nodes reserved for different
purposes.  For example, ``-p interactive`` tells us to us the
interactive partition - which should always be available for quick
tests.  ``-p debug`` is a short partition for debugging.  See a bit
more in the :doc:`serial tutorial <serial>`.



Monitoring your usage
=====================

When you start running in the queue, you need to be able to get
information on how much time, memory, etc is being used. Without this,
you won't know how much time and memory to request. You always want to
request the least possible, so that your stuff can run faster. The `next tutorial (about batch jobs) <serial>` goes into this in more detail. You probably want to be checking things like slurm history even if you aren't running batch, to see how many resources you are actually using.

The command ``slurm q`` will tell you the currently running processes (a good way to make sure you have stopped everything). ``slurm history`` will tell you about recent jobs, including how much total memory they used and their total CPU time.

The command ``scancel`` will cancel a job by job-id (useful is something keeps running after you don't need it anymore).

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



What's next
===========

Read the next tutorial on `serial batch
jobs <serial>`. You can put these same
commands into a script to run many things in the background, without you
having to wait.
