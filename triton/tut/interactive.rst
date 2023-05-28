================
Interactive jobs
================

.. admonition:: Video

   Watch this in our courses: `2022 February <https://www.youtube.com/watch?v=nguLuKJ1gm0&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=12>`__, `2021 January <https://www.youtube.com/watch?v=xhX_u2OA89s&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=11>`__

.. admonition:: Abstract

   * Interactive jobs allow you to quickly test code (before scaling
     up) or getting more resources for manual analysis.
   * See the :doc:`quick reference <../ref/index>` for the local
     options you need if you know Slurm or batch systems already.
   * To run a single command interactively

     * ``srun [SLURM OPTIONS] COMMAND ...`` to run any COMMAND in
       Slurm

   * To get an interactive shell

     * ``srun [SLURM OPTIONS] --pty bash`` (general Slurm)
     * ``sinteractive`` (Triton specific)



.. highlight:: shell-session



Why interactive jobs?
---------------------

In the next session, we will learn about :doc:`batch scripts
<serial>`.  Those get submitted and you see the results later.  *But
what if you want to see the results now, for testing, development, or
one-time things?* You don't want to run on the login node, so
interactive jobs let you do that.  This tutorial walks you through
running your jobs interactively, and :doc:`the next tutorial on serial
jobs <serial>` will go through serial jobs.

.. admonition:: HPC Diner metaphor: doing testing.

  You go to a restaurant and usually you order something known from
  the menu: you make your order, send it to the back, do something
  else, and your food comes.  This is the **serial jobs**.

  But if you are developing something new, do you keep sending
  different orders back until you get it right?  You could ask to go
  to the back and cook it yourself (not that health codes would allow
  it).  This is like getting the **interactive session**.

Interactive jobs let you:

* Run a single job in the Slurm environment to test parameters and
  make sure it works (which is easier than constantly modifying batch
  scripts).

* Get a large amount of resources for some manual data analysis.



Interactive jobs
----------------

Let's say you want to run the following command.  If you just do it
like this, it runs on the login node and someone might request you
stop::

    $ python3 slurm/pi.py 10000

You can submit this program to Slurm using ``srun``. All input/output
still goes to your terminal::

    $ srun --mem=100M --time=0:10:00 python3 slurm/pi.py 10000
    srun: job 52204499 queued and waiting for resources

Here, we are asking for 100 Megabytes of memory (``--mem=100M``) for a
duration of ten minutes (``--time=0:10:00``) (See the :doc:`quick
reference <../ref/index>` or :doc:`slurm` for more options). While
your job - with **jobid** 52204499 - is waiting to be allocated
resources, your shell waits for it to finish.

You can open a new shell on the cluster and run the command ``squeue
-u $USER`` or ``slurm q`` to see all the jobs you currently have
waiting in queue::

  $ slurm q
  JOBID              PARTITION NAME                  TIME       START_TIME    STATE NODELIST(REASON)
  52204499           short-ivb python3               0:00              N/A  PENDING (None)

You can see information such as the state, which partition the
requested node reside in, etc.  Once resources are allocated to your
job, you see the name of the machine in the Triton cluster your
program ran on, output to your terminal::

  srun: job 52204499 has been allocated resources
  Calculating Pi via 10000 stochastic trials
  {"successes": 7815, "pi_estimate": 3.126, "iterations": 10000}



Interactive shell
-----------------

What if you want an actual shell to do things interactively, and not
have to wait for resources each time? Put more precisely, you want
access to a node in the cluster through an interactive bash shell,
with many resources available, that will let you run commands such as
Python and let do some basic work. For this, you just need srun's
``--pty`` option coupled with the shell you want.  In the demo below,
we see we got the node named pe5::

  $ srun -p interactive --time=2:00:00 --mem=600M --pty bash
  srun: job 18836568 queued and waiting for resources
  srun: job 18836568 has been allocated resources
  USER@pe5$

The command prompt will appear when the job starts. And you will have
a bash shell runnnig on one of the computation nodes with at least 600
Megabytes of memory, for a duration of 2 hours, where you run anything
you want. The option ``-p interactive`` requests a node in the
interactive **partition** (group of nodes) which is dedicated to
interactive usage (more on this later).

.. warning::

  Remember to exit the shell when you are done! The shell will be
  running if you don't and it will count towards your usage. This
  wastes resources and effectively means your priority will degrade in
  the future.



Interactive shell with graphics
-------------------------------

``sinteractive`` is very similar to ``srun``, but more clever and thus
allows you to do X forwarding. It starts a `screen session
<https://en.wikipedia.org/wiki/GNU_Screen>`__ on the node,
then sshes to there and connects to the shell::

     $ sinteractive --time=1:00:00 --mem=1000M

This morks when you have connected to the cluster with ``ssh -X`` from
a system that supports Linux graphics.  If you don't have this, try
using :ref:`triton-tut-vdi` to connect via ssh.  Graphical
applications run slowly across the general Internet, so this might be
a good idea anyway.

.. warning::

  Just like with ``srun --pty bash``, remember to exit the shell when
  done, otherwise it wastes resources.



Monitoring and setting resource parameters
------------------------------------------

If you need more resources, the options we discussed in :doc:`slurm`
and the :doc:`quick reference </triton/ref/index>`.

You might wonder "how much time/memory do I need?".  We went over this
in :doc:`slurm`.  In short, make a guess, and see if it worked.  If it
fails, see why it failed (what resource was too low), and increase
that.  A good starting point is "about as long as your other computer
needs" and "something less than computer's amount of memory". In
:doc:`monitoring` we will see how to check, but for now:

The command ``slurm history`` (or ``sacct --long | less``) gives you
information such as the actual memory used by your recent jobs, total
CPU time, etc.  You will learn more about these commands later on.

As shown in a previous example, the command ``slurm queue`` (or
``squeue -u $USER``) will tell you the currently running processes,
which is a good way to make sure you have stopped everything.



Disadvantages of interactive jobs
---------------------------------

Interactive jobs are useful for debugging purposes, to test your setup
and configurations before you put your tasks in a batch script for
later execution.

The major disadvantages include:

- It blocks your shell until it finishes
- If your connection to Triton gets interrupted, you lose the job and
  its output.

Don't get clever and script 20 shells to run 20 ``srun`` jobs at once.
Please have a look at the :doc:`next tutorial about serial jobs
<serial>`.



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Interactive-1: Basic Slurm options

   The program ``hpc-examples/slurm/memory-hog.py``
   uses up a lot of memory to do nothing.  Let's play with it.
   It's run as follows:
   ``python hpc-examples/slurm/memory-hog.py 50M``, where the
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
      ``python hpc-examples/slurm/memory-hog.py 50M --sleep=60`` -
      keep it available.

  .. solution::

    $ python slurm/memory-hog.py 50M
    Trying to hog 50000000 bytes of memeory
    Using 6041600 bytes so far (allocated: 2)
    Using 6144000 bytes so far (allocated: 4)
    Using 6144000 bytes so far (allocated: 8)
    ...
    Using 39477248 bytes so far (allocated: 33554432)
    Using 73269248 bytes so far (allocated: 67108864)
    $ srun --mem=500M python slurm/memory-hog.py 50M
    srun: job 18839900 queued and waiting for resources
    (same output as above)
    $ srun --mem=500M python slurm/memory-hog.py 500M    # works
    $ srun --mem=500M python slurm/memory-hog.py 2000M   # works
    $ srun --mem=5000M python slurm/memory-hog.py 5000M  # fails!
    ...
    slurmstepd: error: Detected 1 oom-kill event(s) in StepId=18839905.0. Some of your processes may have been killed by the cgroup out-of-memory handler.
    srun: error: csl41: task 0: Out Of Memory
    srun: launch/slurm: _step_signal: Terminating StepId=18839905.0

  Triton's Slurm only records the memory usage every 60 seconds, so
  our program has an option to make it slow enough to measure:

    $ srun --mem=5000M python slurm/memory-hog.py 2000M --sleep=60  # fails!

  This 60-second measurement interval in Slurm isn't ideal, because it
  means that you can't as easily see when you have run out of memory.
  Here is what it says without sleep, and with::

    $ slurm history
    18839906    python               05-29 00:50:08     500M       -    00:01.373    00:00:02  none   1 1   0:0 COMP  csl41
    └─ extern   *                    05-29 00:50:08               1M    00:00.002    00:00:02     1   1 1   0:0 COMP  csl41
    └─ 0        python               05-29 00:50:08               1M    00:01.371    00:00:02     1   1 1   0:0 COMP  csl41
    18839907    python               05-29 00:51:55     500M       -    00:01.399    00:01:02  none   1 1   0:0 COMP  csl41
    └─ extern   *                    05-29 00:51:55               1M    00:00.002    00:01:02     1   1 1   0:0 COMP  csl41
    └─ 0        python               05-29 00:51:55            2054M    00:01.397    00:01:02     1   1 1   0:0 COMP  csl41




.. exercise:: Interactive-2: Time scaling

   The program ``hpc-examples/slurm/pi.py``
   calculates pi using a simple stochastic algorithm.  The program takes
   one positional argument: the number of trials.

   The ``time`` program allows you to time any program,  e.g. you can
   ``time python pi.py`` to print the amount of time it takes.

   a) Run the program, timing it with ``time``, a few times,
      increasing the number of trials, until it takes about 10
      seconds: ``time python hpc-examples/slurm/pi.py
      500``, then 5000, then 50000, and so on.

   b) Add ``srun`` in front (``srun python ...``).  Use the ``seff JOBID``
      command to see how much time the program took to run.
      (If you'd like to use the ``time`` command, you can run
      ``srun --mem=MEM --time=TIME time python hpc-examples/slurm/pi.py ITERS``)

   c) Tell srun to use five CPUs (``-c 5``).  Does it go any faster?

   d) Use the ``--threads=5`` option to the Python program to tell it
      to also use five threads.  ``... python .../pi.py --threads=5``

   e) Look at the job history using ``slurm history`` - can you see
      how much time each process used?  What's the relation between
      TotalCPUTime and WallTime?

.. exercise:: Interactive-3: Info commands

   Check out some of these commands: ``sinfo``, ``sinfo -N``, ``squeue``.  Run
   ``slurm job JOBID`` on some running job - does anything
   look interesting?

.. exercise:: Interactive-4: Showing node information

   Run ``scontrol show node csl1``  What is this?  (``csl1`` is the
   name of a node on Triton - if you are not on Triton, look at the
   ``sinfo -N`` command and try one of those names).

.. exercise:: Interactive-5: Why not script ``srun``

   Some people are clever and use shell scripting to run ``srun`` many
   times in a loop (sometimes using ``&`` to background it so that they all run
   at the same time).  Can you list some advantages and disadvantages
   to this?

   .. solution::

    * First off, it's harder than doing it properly with batch scripts
      and array jobs.
    * It's more fragile: if something goes wrong with your shell, all
      output and jobs can get lost.
    * You have to understand your script and the command, instead of
      things being self-contained in the batch file
    * Because they are independent jobs, Slurm can handle them less
      efficiently.  It's less good for the whole cluster.



What's next?
------------

In the next tutorial on `serial batch jobs <serial>`, you will learn how to put the above-mentioned
commands in a script, namely a batch script (a.k.a submission script)
that allows for a multitude of jobs to run unattended.
