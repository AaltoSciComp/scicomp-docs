==================
Parallel computing
==================

.. admonition:: Video

   Watch this in our courses: `2022 February
   <https://www.youtube.com/watch?v=GHbrpg75qbQ&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=22>`__,
   `2022 February real example with MPI
   <https://www.youtube.com/watch?v=Y71eftXpyfs&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=11>`__,
   `2021 January <https://www.youtube.com/watch?v=z-F25Er_-tw&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=19>`__

Parallel computing is what HPC is really all about: processing things on
more than one processor at once. By now, you should have read all of the previous
tutorials.

.. admonition:: Cheatsheet

   * You need to figure out what parallelization paradigm your program
     uses, otherwise you won't know which options to use.

     * Embarrassingly parallel: use :doc:`array jobs <array>`.
     * Multithreaded (OpenMP) or multiple tasks (like Python's
       multiprocessing): ``--cpus-per-task=N``, ``--mem-per-core=M``
       (if memory scales per CPU)
     * MPI: compile to link with our Slurm and MPI libraries,
       ``--ntasks=N``, always use ``srun`` to launch your job.
       ``module load`` a MPI version for both compiling and running.

   * You must always :doc:`monitor jobs <monitoring>` to make sure they are using all the
     resources you request (``seff JOBID``).
   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.


.. highlight:: bash


Parallel programming models
---------------------------

Parallel programming is used to create programs that can execute
instructions on multiple processors at a same time. Most of our users that
run their programs in parallel utilize existing parallel execution features
that are present in their programs and thus do not need to learn how to create
parallel programs. But even when one is running programs in parallel,
it is important to understand different models of parallel execution.

The two main models are:

* (Embarrassingly parallel - :doc:`array jobs <array>`.)
* Shared memory (or multithreaded/multiprocess) programs run multiple
  independent workers on the same machine. As the name suggests, all of
  the computer's memory has to be accessible to all of the processes.
  **Thus programs that utilize this model should request one node,
  one task and multiple CPUs.**
  Likewise, the maximum number of workers is usually the number of CPU cores
  available on the computational node. The code is easier to implement
  and the same   code can still be run in a serial mode. Example applications
  that utilize this model: Matlab, R, Python multithreading/multiprocessing,
  OpenMP applications, BLAS libraries, FFTW libraries, typical
  multithreaded/multiprocess parallel desktop programs.

* Message passing programming (e.g. MPI, message passing interface)
  can run on multiple nodes interconnected with the network via passing
  data through MPI software libraries. Almost all large-scale scientific
  programs utilize MPI. MPI can scale to thousands of CPU cores, but
  depending on the case it can be harder to implement from the
  programmer's point of view. **Programs that utilize this model should
  request single/multiple nodes with multiple tasks each. You should
  not request multiple CPUs per task.** Example applications that utilize this
  model: CP2K, GPAW, LAMMPS, OpenFoam.

Both models, MPI and shared memory, can be combined in one application, in
this case we are talking about hybrid parallel programming model.
**Programs that utilize this model can require both multiple tasks
and multiple CPUs per task.**

Most historical scientific code is MPI, but these days more and more
people are using shared memory models.

.. important::

   **Normal serial code can't just be run in parallel without
   modifications.** As a user it is your responsibility to
   understand what parallel model implementation your code has, if any.

   When deciding whether using parallel programming is worth
   the effort, one should be mindful of
   `Amdahl's law <https://en.wikipedia.org/wiki/Amdahl%27s_law>`_ and
   `Gustafson's law <https://en.wikipedia.org/wiki/Gustafson%27s_law>`_.
   All programs have some parts that can only be executed in serial and
   thus the theoretical speedup that one can get from using parallel
   programming depends on two factors:

     1. How much of programs' execution could be done in parallel?
     2. What would be the speedup for that parallel part?

   Thus if your program runs mainly in serial but has a small parallel
   part, running it in parallel might not be worth it. Sometimes, doing
   data parallelism with e.g. :doc:`array jobs <array>` is much more
   fruitful approach.

   Another important note regarding parallelism is that all the applications
   scale good up to some upper limit which depends on application implementation,
   size and type of problem you solve and some other factors. The best practice
   is to benchmark your code on different number of CPU cores before
   you start actual production runs.

   **If you want to run some program in parallel, you have to know
   something about it - is it shared memory or MPI?  A program doesn't
   magically get faster when you ask more processors if it's not designed
   to.**



Embarrassingly parallel: array jobs
-----------------------------------

The :doc:`array jobs <array>` we have already discussed.  Don't forget
that this is one of the most common ways to parallelize!  A large
amount of work these days is "array jobs" + "shared memory for these jobs"



Shared memory: OpenMP/multithreaded/multiprocess
------------------------------------------------

Diffence between multithreaded and multiprocess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shared memory programs usually parallelize by using multiple threads or
processes. Processes are individual program executions while threads are
basically smaller program executions within a process. Processes can
launch both subprocesses and threads. Slurm reservations for both methods
behave similarly.

Depending on a program, you might have multiple processes (Matlab parallel
pool, R parallel-library, Python `multiprocessing <https://docs.python.org/library/multiprocessing.html>`__) or have multiple threads
(OpenMP threads of BLAS libraries that R/numpy use).

.. warning::

   Some programs (e.g. R) can utilize both multithread and multiprocess
   parallelism. For example, R has parallel-library for running multiple
   processes, but BLAS libraries that R uses can utilize multiple threads.
   If you encounter bad performace when you use parallel processes
   try setting ``OMP_NUM_THREADS=1`` in your slurm script.

Running multithreaded/multiprocess applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic slurm option that specifies how many CPUs your job requires is
``--cpus-per-task=N`` (or ``-c N``). If your memory requirement scales
with the number of cores, use ``--mem-per-core=M``, if you
require a fixed amount of memory (per node regardless of number of
processors), use ``--mem=M``. We recommend starting with ``--mem=M`` if
you do not know how your problem scales.

.. important::

   The number of threads/processes you launch should match the
   number of requested processors. If you create a lower number, you will
   not utilize all CPUs. If you launch a larger number, you will
   oversubscribe the CPUs and the code will run slower as different
   threads/processes will have to swap in/out of the CPUs.

.. warning::

   Normally you should **not** use ``--ntasks=N`` when you want to
   run shared memory codes. The number of tasks is only relevant to MPI codes
   and by specifying it you might launch multiple copies of your program
   that all compete on the reserved CPUs.

   Only hybrid parallelization codes should have both ``--ntasks=N`` and
   ``--cpus-per-task=C`` set to be greater than one.

Running a typical OpenMP program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenMP is a standard de facto for the multithreading implementations. There
are many others, but this one is the most common, supported by all known
compiler suits. For other implementations of shared memory parallelism,
please consult your code docs.

Let's consider
`hello_omp-example <https://github.com/AaltoSciComp/hpc-examples/tree/master/openmp/hello_omp>`_
from HPC examples repository.

Simple code compiling::

  wget https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/openmp/hello_omp/hello_omp.c
  module load gcc/8.4.0
  gcc -fopenmp -O2 -g hello_omp.c -o hello_omp

Running an OpenMP code::

  export OMP_PROC_BIND=TRUE
  module load gcc/8.4.0
  srun --cpus-per-task=4 --mem=500M --time=00:05:00 hello_omp

The
:download:`slurm script<https://raw.githubusercontent.com/AaltoSciComp/hpc-examples/master/openmp/hello_omp/hello_omp.sh>`
will look similar:

.. literalinclude:: /triton/examples/openmp/hello_omp/hello_omp.sh
   :language: slurm

It is good to know that OpenMP is both an environment and set of libraries, but
those libraries always come as part of the compiler. Thus during runtime
you should load the same compiler that you used for compiling the code.

.. include:: /triton/examples/python/python_openmp/python_openmp.rst


.. _parallel-mpi:

Message passing programs: MPI
-----------------------------

For compiling/running an MPI job one has to pick up one of the MPI library
suites. There are various different MPI libraries that all implement the
MPI standard. We recommend that you use our OpenMPI installation
(``openmpi/4.0.5``). For information on other installed versions, see the
:doc:`MPI applications-page<../apps/mpi>`.

.. include:: /triton/ref/mpi-warning.rst

For basic use of MPI programs, you will need to use the
``-n N``/``--ntasks=N``-option to specify the number of MPI workers.

Compiling and running an MPI Hello world-program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /triton/examples/mpi/hello.rst

Spreading MPI workers evenly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases you might require more than one node during your job's runtime.

When this is the case, it is usually recommended to split the number of
workers evenly among the nodes. To do this, one can use
``-N N``/``--nodes=N`` and ``--ntasks-per-node=n``. For example, you could
distribute the previously requested four tasks to two nodes with:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=2            # 2 nodes
  #SBATCH --ntasks-per-node=2  # 2 processes per node * 2 nodes = 4 processes in total
  #SBATCH --constraint=avx     # set constraint for processor architecture

  module load openmpi/4.0.5  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi


This way the number of workers is distributed more evenly, which in turn
reduces communication overhead between workers. The total number of tasks is
``--nodes`` times the ``--ntasks-per-node``.


Setting a constraint for a specific CPU architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of CPUs/tasks one can specify for a single parallel job depends
usually on the underlying algorithm. In many codes, such as many
finite-difference codes, the workers are set in a grid-like structure. The user
of said codes has then a choice of choosing the dimensions of the simulation
grid aka. how many workers are in x-, y-, and z-dimensions.

For best perfomance one should reserve half or full nodes when possible. In
heterogeneous clusters this can be a bit more complicated as different CPUs
can have different numbers of cores.

In Triton CPU partitions there are machines with 24, 28 and 40 CPUs. See the
list of :ref:`available nodes<hardware-list>` for more information.

However, one can make the reservations easier by specifying a CPU architecture
with ``--constraint=ARCHITECTURE``. This tells Slurm to look for nodes that
satisfy a specific feature. To list available features, one can use
``slurm features``.

For example, one could limit the code to the Haswell-architecture with the
following script:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:05:00      # takes 5 minutes all together
  #SBATCH --mem-per-cpu=200M   # 200MB per process
  #SBATCH --nodes=1            # 1 node
  #SBATCH --ntasks-per-node=24 # 24 processes as that is the number in the machine
  #SBATCH --constraint=hsw     # set constraint for processor architecture

  module load openmpi/4.0.5  # NOTE: should be the same as you used to compile the code
  srun ./hello_mpi

Monitoring performance
----------------------

.. include:: ../examples/monitoring/seff.rst

Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: Parallel-1: Explore and understand basic Slurm options

   Run ``srun --cpus-per-task=4 hostname``, ``srun --ntasks=4 hostname``, and ``srun --nodes=4
   hostname``.  What's the difference and why?

.. exercise:: Parallel-2: OpenMP with Python

   Find the files ``hpc-examples/openmp/hello_omp/hello_omp.c`` and
   ``hpc-examples/hello_omp/hello_omp.sh`` that have a short example of OpenMP.
   Compile and run it - a slurm script is included.

.. exercise:: Parallel-3: OpenMP

   Find the files in ``hpc-examples/python/python_openmp``. Try running the
   example with a few different ``--constraint=X`` and ``--cpus-per-task=C``.
   In your opinion, what architecture / cpu number combination would provide the
   best efficiency? Use ``seff`` to verify.

.. exercise:: Parallel-4: MPI

   Find the files ``hpc-examples/mpi/hello_mpi/hello_mpi.c`` and
   ``hpc-examples/mpi/hello_mpi/hello_mpi.sh`` that
   have a short example of MPI.
   Compile and run it - a slurm script is included.



See also
--------

* The :doc:`Research Software Engineers </rse/index>` can help in all
  aspects of parallel computing - we'd recommend anyone getting to
  this point set up a consultation to make sure your work is as
  efficient as it can be.



What's next?
------------

You have now seen the basics - but applying these in practice is still
a difficult challenge!  There is plenty to figure out while combining
your own software, the Linux environment, and Slurm.

Your time is the most valuable thing you have.  If you aren't fully
sure of how to use the tools, it is much better to ask that struggle
forever.  Contact us the :doc:`Research Software Engineers
</rse/index>` early - for example in our :doc:`daily garage
</help/garage>`, and we can help you get set up well.  Then, you can
continue your learning while your projects are progressing.
