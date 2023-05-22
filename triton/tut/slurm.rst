Slurm: the queuing system
=========================

What is a cluster?
------------------

Triton is a large system that combines many different individual
computer nodes. Hundreds of people are using Triton simultaneously.
Thus resources (CPU time, memory, etc.) need to be shared among everyone.

This resource sharing is done by a software called a job scheduler or
workload manager, and Triton's workload manager is **Slurm** (which is
also the dominant in the world one these days).
Triton users submit jobs which are then scheduled and allocated
resources by the workload manager.

.. admonition:: An analogy: the HPC Diner

   You're eating out at the HPC Diner.  What happens when you arrive?

   - A host greets you and takes your party size and estimated dining
     time.
   - You are given a number and asked to wait a bit.
   - The host looks at who is currently waiting.
   - If you are two people, you might squeeze in soon.
   - If you are a lot of people, the host will try to slowly free up
     enough tables to join to eat together.
   - If you are a really large party, you might need an advance
     reservation (or have to wait a really long time).
   - They want everyone to get a fair share of their food.  Thus,
     people that have visited more often are asked to wait slightly
     longer for their table, as a balancing mechanic.

   Thanks to `HPC Carpentry
   <https://carpentries-incubator.github.io/hpc-intro/13-scheduler/index.html>`__
   / `Sabry Razick <https://github.com/Sabryr>`__ for the idea.



The resources available to you
------------------------------

Slurm comes with a multitude of parameters which you can specify to
ensure you will be allocated enough memory, CPU cores, time, etc.
You saw two of them in use in the above examples (``--mem`` and ``--time``)
and you will learn more in the following tutorials.

Because you are sharing resource with other users, **you should always estimate the amount of time, memory, etc.
you need and then request them accordingly** for efficiency reasons;
the default memory and time limits are intentionally set low and may not be
sufficient for your jobs to run/finish.

The general rule of thumb is to request the least possible, so that your stuff can run faster.
That is because the **less you request, the faster you are likely to be allocated resources.**
If you request something slightly less than a node size (note that we have different size nodes)
or partition limit, you are more likely to fit into a spare spot.

For example, we have many nodes with 12 cores, and some with 20 or 24. If you request 24 cores,
you have very limited options. However, you are more likely to be allocated a node if you request 10 cores.
The same applies to memory: most common cutoffs are 48, 64, 128, 256GB.
It's best to use smaller values when submitting interactive jobs, and more for batch scripts.

The basic resources are:

* CPUs (also known as "processors" or "(processor) cores"): Processor cores.  This resource lets you do things in parallel
  the classic way, by adding processors.  Depending on how the
  parallelism works, there are different ways to request the CPUs -
  see :doc:`parallel`.
  CPUs.
* Memory: Memory is needed for data in jobs.  If you run out of
  processors, your job is slow, but if you run out of memory, then
  everything dies.
* GPUs: Graphical Processing Units are modern, highly parallel compute
  units.  We will discuss requesting them in :doc:`gpu`.
* Time: While not exactly a resources, you need to specify the
  expacted usage time (run time) of each job for scheduling purposes.
  If you go over by too much, your job will be killed.
* If you did even larger work on larger clusters, input/output
  bandwidth and licenses are also possible resources.

.. seealso::

   This `reference page <https://slurm.schedmd.com/sbatch.html>`_ covers the existing resource parameters
   and options you can use in both your interactive jobs and `batch jobs <serial>` which you will learn about
   in the next tutorial.


How many resources to request?
------------------------------

Obviously, this is one of the 


The basic Slurm commands
------------------------

The basic Slurm commands are ``sbatch`` (to submit asynchronous jobs,
see :doc:`serial`), and ``srun`` to submit interactive jobs (see
:doc:`interactive`, the next lesson).  Both of these command take the
same options to request resources, such as ``--cpus-per-task`` for
CPUs or ``--mem`` for memory per node.  For example, you could run
(don't do this yet, you will learn next):

* ``srun --mem=5G --time=5:00:00 ...`` to request 5 hours and 5GB of memory.
* Or this batch script template:

  .. code:: slurm

    #!/bin/bish
    #SBATCH --mem=5G
    #SBATCH --time=5:00:00

You'll learn exactly how this works next.

Next, see :doc:`interactive`.



What's next?
------------

We move on to running :doc:`interactive jobs <interactive>`.