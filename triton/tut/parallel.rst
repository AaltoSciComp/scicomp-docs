==================
Parallel computing
==================

Parallel computing is what HPC is really all about: being able to use
many CPUs at once.  By now, you should have read all of the previous
tutorials.

Parallel programming models
---------------------------

Parallel programming is a completely different way of programming (and
a normal, serial code can't just be run as parallel without
modifications).  Most Triton users don't need to write their own
applications, at most they will be running existing programs, but in
order to understand things, we start with some introduction.

The two main models are:

* Shared memory programming (e.g. OpenMP) runs on only one node
  because, like the name says, all the memory has to be accessible to
  all the processes.  Thus, scaleability is limited but it is much
  easier.  Most typical parallel desktop programs use shared memory
  models.

* Message passing programming (e.g. MPI, message passing interface)
  can run on multiple nodes via passing data through MPI software
  libraries.  The largest-scale scientific programs are usually MPI.
  MPI can scale better, but it's harder to get started.

Then, there are all sorts of combinations of these.

Most historical scientific code is MPI, but these days more and more
people are using shared memory models.

You can't just use the options on this page with any old code.  The
code has to be able to use the multiple nodes and processors you
offer.  Some programs will automatically do this if built and compiled
the right way, but you always want to make sure for your particular
circumstance.



OpenMP and single-node parallel programs
----------------------------------------

We start with OpenMP (multithreaded) programs first since they are
simpler.  These instructions apply to OpenMP programs as well as other
multithreaded programs.

The first step is always to figure out how to how to make your
programs use multiple CPU cores.  OpenMP programs automatically use
the right number of processors (using the slurm environment
variables).  For other programs, might be worth checking
yourself. (TODO).

The basic slurm options you need are ``-c`` to specify the number of
cores to use.  If your memory needs scale with the number of cores,
use ``--mem-per-core``, if you require a fixed amount of memory (per
node regardless of number of processors), use ``--mem``.

``--exclusive``

compiling:
  ``gcc -fomp hello_omp.c -o hello_omp``





MPI and multi-node software
---------------------------
``-N``, ``-c``, ``--exclusive``, ``--mem-per-core``, ``--mem``,



Special software
----------------

Matlab
^^^^^^
``matlab_multithread``, see :doc: `../apps/matlab`.

Python
^^^^^^

GPU and deep learning
^^^^^^^^^^^^^^^^^^^^^

See :doc:`the gpu tutorial <gpu>` and :doc:`reference <../usage/gpu>`.



Monitoring performance
----------------------

You can use the ``seff`` program (with a jobid) to list what percent
of available processors and memory you used.  If your processor usage
is far below, your code may not be working correctly in a parallel
environment.


Quick reference
---------------

As a reminder, here is the quick reference of all slurm options

.. include:: ../ref/slurm


Next steps
----------

See the next pages:

* You can check the :doc:`../usage/general` page for the reference
  information on running jobs.  This contains the general reference
  information.

* :doc:`../usage/mpilibs`

External links:

*
