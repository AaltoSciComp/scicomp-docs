======================
How big is my program?
======================

.. admonition:: Abstract

   * You can use your workstation / laptop as a base measuring stick:
     If the code runs on your machine, as a first guess you can reserve
     the same amount of CPUs & RAM as your machine has.

   * Similarly for running time: if you have run it on your machine,
     you should reserve similar time in the cluster.

   * Natural unit of program size in Triton is 1 CPU & 4 GB of RAM.
     If your program needs a lot of RAM, but does not utilize the
     CPUs, you should try to optimize it.

   * If your program does the same thing more than once, you can estimate
     that the total run time is
     :math:`T \approx n_{\textrm{steps}} \cdot t_{\textrm{step}}`,
     where :math:`t_{\textrm{step}}` is the time taken by each
     step.

   * Likewise, if your program runs multiple parameters, the total time
     needed is
     :math:`T_{\textrm{total}} \approx n_{\textrm{parameters}} \cdot T_{\textrm{single}}`,
     where :math:`T_{\textrm{single}}` is time needed to run the program
     with some parameters.

   * You can also run a smaller version of the problem and try to estimate
     how the program will scale when you make the problem bigger.

   * You should always :doc:`monitor jobs </triton/tut/monitoring>` to find out what
     were the actual resources you requested (``seff JOBID``).

   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.



Why should you care?
--------------------

There are many reasons why you should care about this question.

.. collapse:: By knowing how big your program is you can more accurately
   request the resources you need and you will get a higher priority
   in the queue.

   A cluster environment is shared among multiple users and thus
   all users will get their own share of the cluster resources.

   The queue system will calculate your fair share of the resources
   based on the resource requirements you have specified.

   This means that if you request more than you need, you will
   waste resources and you will get less resources in the near
   future.

.. collapse:: Knowing how your program behaves can help you organize your work.

   If, for example, you have a program that takes a day to run a single
   computation and you have thousands of computations you need to do,
   you can estimate that you can save a lot of time optimizing the
   program before starting the computations.

   Likewise you can find out that it is not worth the effort to
   optimize something you will only run once.

   You can also find that something is unfeasible with the method
   you have chosen before you've invested a lot of time in
   implementating it.

.. collapse:: If you know how big your program is you can more easily recognize
   when it isn't running as it should.

   If, for example, you have a program that you assume should finish
   in an hour, but it does not finish in an hour, you can infer
   that either the assumption was incorrect or that the program did
   not behave as it should.

   This can often happen when program is transferred from a desktop
   environment into the cluster and the program is not aware of this
   change.

   Quite often a program can appear to be running slower than it should be
   because it **is** running slower than it should be and something is
   holding it back. Recognizing that is important.

How do you measure program size?
--------------------------------

The program size can be measured in couple of ways:

- How many CPUs does my program use?
- How much RAM does my program use?
- How long does it take to run my program?
- How many times do I need to run a program?

These question can seem complicated to answer.
:doc:`Monitoring </triton/tut/monitoring>` and profiling is one way of getting
concrete numbers, but there are couple of tricks you can use to get a
estimate.


How to estimate CPU and RAM usage?
----------------------------------

Simple measuring stick: Your own computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you know nothing of your program, you can still probaly answer this question:

**Does the program run on my own computer?**

This can give you a good baseline on how big your program is.
In general, you can use the following estimates to approximate your computer:

- A typical laptop computer |laptop| is about 4 CPUs and 16GB of RAM.
- A typical workstation computer |desktop| is about 8 CPUs and 32GB of RAM.
- A typical compute node |server| starts from about 32 CPUs and 128GB of RAM,
  but they can range up to 128 CPUs and 512GB of RAM.

So if, for example, the program runs on your laptop (|laptop|), you'll know
that it should work with a request of 4 CPUs and 16GB.

In general, you can say that:
|server| :math:`\approx 4 \: \cdot` |desktop| :math:`\approx 8 \: \cdot` |laptop| or more.
This will give you a good initial measuring scale.

.. |desktop| image:: https://upload.wikimedia.org/wikipedia/commons/5/56/Black_computer_icon.png
   :width: 40
.. |laptop| image:: https://upload.wikimedia.org/wikipedia/commons/8/8b/Laptop_World.png
   :width: 40
.. |server| image:: https://upload.wikimedia.org/wikipedia/commons/9/9b/Server_icon_CC0.svg
   :width: 40


Getting a better CPU / RAM estimate: check your task manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A simple way of getting a better estimate is to check your
computer's task manager when you are running the program.

- In Windows you can open **Task manager** from the start menu or by pressing
  CTRL + ALT + DEL.
- In Mac OS X you can use finder to launch **Activity monitor**
  or press CMD + ALT + ESC.
- In Linux you can use **System Monitor** to see your processes.

When you're running a program these tools will easily tell you
how many CPUs the processes are using and how much memory they
are using. CPU usage is a percentage of total CPU capacity. So
if your machine has 4 CPUs and you see an usage of 25%,
that means your program is using 1 CPU. Similarly, the memory
usage is reported as a percentage of the total available memory.

In a cluster environment you can use ``seff JOBID`` for seeing how
much of the reserved CPU and RAM your program used.
For more information, see the :doc:`monitoring documentation </triton/tut/monitoring>`.

Natural unit of scale: 1 CPU = 4GB of RAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the previous section we can notice an interesting observation:
in HPC clusters, there is usually around 1 CPU for each 4 GB of RAM.

.. figure:: /images/slot-explanation.svg

This is **not** an universal law, but a coincidence that has been
true for couple of years due to economic reasons: these numbers
give usually the best "bang for the buck".

In other HPC clusters the ratio might be different, but it is
important to know this ratio as that is the ratio that the Slurm queue
system uses when it determines the size of a job. It is very easy to calculate:
just divide the available RAM with the amount of CPUs.

When determining how big your job is it is useful to round up to the nearest slot:

.. figure:: /images/slot-queue.svg

If your program requires a lot of RAM, but it does not utilize
multiple CPUs, it is usually good idea to check whether the RAM usage
can be lowered or whether you can utilize multiple CPUs via
:doc:`shared memory parallelism <../tut/parallel-shared>`. Otherwise
you're getting billed for resources that you're not actively using, which
lowers your queue priority.



How to estimate execution time?
-------------------------------

Simple measuring stick: Your own computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have run the problem on your computer, you'll want to use that as
a measuring stick. First good assumption is that given the same resources,
the program should run in the same time in the compute node.

Programs that do iterations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, a program does the same thing more than once.
For example:

- Physics simulation codes will usually integrate equations
  in discrete time steps.
- Markov chains do the same calculation for each node in the chain.
- Deep learning training does training over multiple epochs and the
  epochs themselves consist of multiple training steps.
- Running the same program with different inputs.

If this is the case, it is usually enough to measure the time
taken by few iterations and from that information extrapolate the
total runtime.

If the time taken by each step is :math:`t_{\textrm{step}}`, then the total runtime
:math:`T` is approximately :math:`T \approx n_{\textrm{steps}} \cdot t_{\textrm{step}}`.

.. figure:: /images/program-iteration.svg

Do note that if you're planning on running the same calculation
multiple times with different parameters and/or datasets you can
estimate that the time needed for running it
:math:`T_{\textrm{total}} \approx n_{\textrm{parameters}} \cdot T_{\textrm{single}}`.
In these cases :doc:`array jobs </triton/tut/array>` can often be used to split
the calculation into multiple jobs.


Programs that run a single calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For programs that run a single calculation you can estimate the runtime by
solving smaller problems. By running a smaller problem on your
own computer and then estimating how much bigger the bigger problem is,
you can usually get a good estimate on how much time it takes to solve the bigger
problem.


For example, let's consider a situation where you need to calculate
various matrix operations such as multiplications, inversions etc..
Now if a smaller problem uses a matrix of size :math:`n^{2}` and bigger
problem uses a matrix of size :math:`m^{2}`, you can calculate that the
ratio of the bigger problem to the initial problem is :math:`r = (m / n)^{2}`.

.. figure:: /images/problem-scaling.svg

So if solving the smaller problem takes time :math:`T_{\textrm{small}}`,
then you could estimate that the time taken by the bigger problem is at least
:math:`T_{\textrm{large}} \approx r \cdot T_{\textrm{small}} = (m / n)^{2} \cdot T_{\textrm{small}}`.

This estimate is **most likely a bad estimate** (most linear algebra algorithms
do not scale with :math:`O(n^{2})` complexity), but **it is a better estimate
than no estimate at all**.

It is especially important to notice if your problem scales as :math:`O(n!)`.
These kinds of problems can quickly become very time consuming. Problems that
involve permutations such as the
`travelling salesman problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
are famous for their complexity.

.. figure:: /images/problem-permutations.svg
    :width: 60%
    :align: center


If you're interested on the topic, a good introduction is this
`excellent blog-series on Big O notation <https://jarednielsen.com/big-o-factorial-time-complexity/>`__.



Image sources
-------------

- Desktop image: Kahniel, `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>`__, via `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Black_computer_icon.png>`__
- Laptop image: Halfwitty, `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>`__, via `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Desktop_monitor_white.svg>`__
- Server image: Markus Suhr, `CC 0 <https://creativecommons.org/share-your-work/public-domain/cc0/>`__, via `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Server_icon_CC0.svg>`__
