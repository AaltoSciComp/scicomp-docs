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

  Advantages of interactive running:  It's good for getting started
  quickly and scaling up: "just add srun!". It's good when task is so
  small that scripting isn't worth it.

  Downsides include: You have to be there and wait for things to run. If
  your shell connection gets interrupted, you lose the process. If you
  don't stop interactive shells, they will continue it will count against
  your fairshare quota, making your jobs run slower in the future.


srun (single process)
=====================

The simplest way is to use srun. Let's say you run some program like
this:

::

    ./my_code 5000 1.1 1-5 

You switch to use srun. All input/output still goes to your terminal
(but note X forwarding for graphical applications doesn't work - see
below for that).

::

    srun --mem=50G --time=5:00:00 ./my_code 5000 1.1 1-5 

This has some possible problems: it is connected to your shell. If your
shell quits, the process gets lost. Also, this runs only one single
process. If you need to do multiple things in a row, then you have to
wait before each one starts. Note: srun is used directly with a command
to run, not batch scripts like sbatch is (though of course you could run
a shell script). srun does not look at the #SBATCH options inside of
scripts.

How do you find the right time/CPU/memory requirements?  Slurm (the
queuing system) has extensive reporting. For example,
"``slurm history`` will show you the actual run time and actual memory
used of your job. There is a little bit about this below and more in
the next tutorial.


srun ``--pty`` (shell)
======================

So, let's say you need to go one step up. You want an actual shell to
do several things. You can do that this way:

::

    srun -p interactive --time=HH:MM:SS --mem=nnG --pty bash

Now you have a shell... do whatever you need to do. **Close the shell
when you are done!  If you don't, the process will keep running until
your time limit. All of this time will be counted against your usage.
It doesn't cost money, but does mean that your priority will go down in
the future.**  (Note that we specify the interactive partition with "-p
interactive". More on this below.)


sinteractive (shell)
====================

sinteractive is very similar to srun, however it is more clever and thus
allows you to do X forwarding. In the background, it starts the job,
starts a screen session on the node, then sshes to there and connects to
the screen. You can also ssh to this node again and connect to the
process again.

::

     sinteractive --time=HH:MM:SS --mem=nnG

**Just like with ``srun --pty``, remember to close the process when done.
However, it's even harder than before. Since there is a separate screen
session running, just closing the terminal isn't enough. Exit all
shells in the screen session on the node (C-d or ``exit``), or cancel
the process (see below).**


More options
============

**Partitions:** You have many different options for running the jobs.
First off, there are different *partitions* to run in. Each partition
specifies a different type of nodes, and different limits.

-  For example, the above examples used the "interactive" partition
   which means that you have lower limits for time/CPU/memory, but can
   get resources faster which is good for your own development (it is
   also oversubscribed, which means that we assume not everyone is using
   CPU 100% of the time).
-  Otherwise, debug/short/batch give you progressively more resources
   but possibly longer waiting.
-  The are dedicated partitions for GPUs.

In regular usage, this is usually decided automatically (based on time
and memory requirements), but if you are doing stuff with an interactive
shell, it's important to specify *interactive*. You don't need to do
this if you are   You specify a partition with *-p partition* like
above. We recommend interactive for things that start a shell for
interactive running, otherwise leave it off and it will pick all
available options based on your time/CPU/memory. If you need to go
faster, try reducing the resources to the next lowest partition. The
partitions are:

.. include:: ../ref/partitions.rst

**time/CPU/memory requirements:** The commands srun/sinteractive have
many more options that let you specific resources. The most important
for interactive running are probably *--mem*, *--cpus-per-task* *(-c)*,
and *--time* *(-t)*.


.. include:: ../ref/slurm.rst

****How much time/memory/CPU resources should you request?****  The less
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

**Your own group node:** It's possible to purchase get a dedicated node
for your group or for several groups. This gives you a place where you
can run interactive jobs for as long as you want (shells open forever,
etc), including computation directly on the node. When you need more
power, you can "just add srun!" or create batch scripts from that node.
Contact us to discuss.

 

Monitoring your usage
=====================

When you start running in the queue, you need to be able to get
information on how much time, memory, etc is being used. Without this,
you won't know how much time and memory to request. You always want to
request the least possible, so that your stuff can run faster. The `next tutorial (about batch jobs) <serial>` goes into this in more detail. You probably want to be checking things like slurm history even if you aren't running batch, to see how many resources you are actually using.

The command ``slurm q`` will tell you the currently running processes (a good way to make sure you have stopped everything). slurm history will tell you about recent jobs, including how much total memory they used and their total CPU time.

The command ``slurm cancel`` will cancel a job by job-id (useful is something keeps running after you don't need it anymore).


What's next
===========

Read the next tutorial on `serial batch
jobs <serial>`. You can put these same
commands into a script to run many things in the background, without you
having to wait.
