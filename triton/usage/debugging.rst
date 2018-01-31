=========
Debugging
=========

.. note::

   Also see :doc:`profiling`.


Debugging is one of the most fundamental things you can do while using
software: debuggers allow you to see inside of running programs, and
this is a requirement of developing with any software.  Any reasonable
programming language will have a debugger made as one of the first
tasks when it is being created.

Serial code debugging
---------------------

`GDB <http://sourceware.org/gdb/current/onlinedocs/gdb/>`__ is the usual
GNU debugger.

Note: the latest version of gcc/gfortran available through module
require ``-gdwarf-2`` option along with the ``-g`` to get it to work with the
default gdb command. Otherwise the default version 4.4 should work
normally with just ``-g``.

`Valgrind <http://valgrind.org/docs/manual/quick-start.html>`__ is
another tool that helps you to debug and profile your serial code on
Triton.




MPI debugging & profiling
-------------------------

GDB with the MPI code
^^^^^^^^^^^^^^^^^^^^^


Compile your MPI app with -g, run GDB for every single MPI rank with::

    salloc -­p play ­­--nodes 1 ­­--ntasks 4 srun xterm ­-e gdb mpi_app

You should get 4 xterm windows to follow, from now on you have full
control of you MPI app with the serial debugger.

PADB
^^^^

A Parallel Debugging Tool. Works on top of SLURM, support OpenMPI or
MPICH only (as of June 2015), that is MVAPICH2 is not supported. Do not
require code re-compilation, just run your MPI code normally, and then
launch padb separately to analyze the code behavior.

Usage summary (for full list and explanations please consult
http://padb.pittman.org.uk/)::

    # assume you have your openmpi module loaded already
    module load padb
    padb --create-secret-file    # for the very first time only

    # Show all your current active jobs in the SLURM queue
    padb -show-jobs

    # Target a specific jobid, and reports its process state
    padb  --proc-summary
    # or, for all running jobs
    padb --all --proc-summary

    # Target a specific jobid, and report its MPI message queue, stack traceback, etc.
    padb --full-report=

    # Target a specific jobid, and report its stack trace for a given MPI process (rank)
    padb  --stack-trace --tree --rank 

    # Target a specific jobid, and report its stack trace including information about parameters and local variables for a given MPI process (rank)
    padb  --stack-trace --tree --rank  -Ostack-shows-locals=1 -Ostack-
    shows-params=1

    # Target a specific jobid, and reports its MPI message queues
    padb  --mpi-queue

    # Target a specific jobid, and report its MPI process progress (queries in loop over and over again)
    padb  --mpi-watch --watch -Owatch-clears-screen=no
