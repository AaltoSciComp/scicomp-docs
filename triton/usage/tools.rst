Debugging
~~~~~~~~~

`GDB <http://sourceware.org/gdb/current/onlinedocs/gdb/>`__ is the usual
GNU debugger.

Note: the latest version of gcc/gfortran available through module
require "-gdwarf-2" option along with the -g to get it to work with the
default gdb command. Otherwise the default version 4.4 should work
normally with just -g.

`Valgrind <http://valgrind.org/docs/manual/quick-start.html>`__ is
another tool that helps you to debug and profile your serial code on
Triton.

Serial code profilers
~~~~~~~~~~~~~~~~~~~~~

GNU gprof
^^^^^^^^^

`gprof <http://sourceware.org/binutils/docs/gprof/>`__ is a profiler
based on instrumenting your code (build with -pg). It has relatively
high overhead, but gives exact information e.g. for the number of times
a function is called.

Perf
^^^^

`perf <https://perf.wiki.kernel.org/index.php/Tutorial>`__ is a
*sampling profiler*, which periodically samples *events* originating
e.g. from the CPU performance monitoring unit (PMU). This generates a
statistical profile, but the advantage is that the overhead is very low
(single digit %), and one can get timings at the level of individual asm
instructions. For a simple example, consider a (naive) matrix
multiplication program:

Compile the program (-g provides debug symbols which will be useful
later on, at no performance cost)

$ gfortran -Wall -g -O3 mymatmul.f90

Run the program via the profiler to generate profile data:

$ perf record ./a.out

Now we can look at the profile:

| $ perf report
| # Samples: 1251
| #
| # Overhead         Command                  Shared Object  Symbol
| # ........  ..............  .............................  ......
| #
|     85.45%           a.out  ./a.out                        [.]
  MAIN\_\_
|      4.24%           a.out  /usr/lib/libgfortran.so.3.0.0  [.]
  \_gfortran\_arandom\_r4
|      3.12%           a.out  /usr/lib/libgfortran.so.3.0.0  [.]
  kiss\_random\_kernel

So 85% of the runtime is spent in the main program (symbol MAIN\_\_),
and most of the rest is in the random number generator, which the
program calls in order to generate the input matrices.

Now, lets take a closer look at the main program:

| $ perf annotate MAIN\_\_
| ------------------------------------------------
|  Percent \|      Source code & Disassembly of a.out
| ------------------------------------------------
|          :
|          :
|          :
|          :      Disassembly of section .text:
|          :
|          :      00000000004008b0 <MAIN\_\_>:

...

|          :        c = 0.
|          :
|          :        do j = 1, n
|          :           do k = 1, n
|          :              do i = 1, n
|          :                 c(i,j) = c(i,j) + a(i,k) \* b(k,j)
|    30.12 :        400a40:       0f 28 04 01             movaps
  (%rcx,%rax,1),%xmm0
|     4.92 :        400a44:       0f 59 c1                mulps 
  %xmm1,%xmm0
|    12.36 :        400a47:       0f 58 04 02             addps
  (%rdx,%rax,1),%xmm0
|    40.73 :        400a4b:       0f 29 04 02             movaps
  %xmm0,(%rdx,%rax,1)
|     9.65 :        400a4f:       48 83 c0 10             add   
  $0x10,%rax

Unsurprisingly, the inner loop kernel takes up practically all the time.

For more information on using perf, see the perf tutorial at

https://perf.wiki.kernel.org/index.php/Tutorial

MPI debugging & profiling
~~~~~~~~~~~~~~~~~~~~~~~~~

GDB with the MPI code
^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div>

Compile your MPI app with -g, run GDB for every single MPI rank with

.. raw:: html

   </div>

.. raw:: html

   <div>

 

::

    salloc -­p play ­­--nodes 1 ­­--ntasks 4 srun xterm ­-e gdb mpi_app

 

.. raw:: html

   </div>

.. raw:: html

   <div>

You should get 4 xterm windows to follow, from now on you have full
control of you MPI app with the serial debugger.

.. raw:: html

   </div>

PADB
^^^^

A Parallel Debugging Tool. Works on top of SLURM, support OpenMPI or
MPICH only (as of June 2015), that is MVAPICH2 is not supported.  Do not
require code re-compilation, just run your MPI code normally, and then
launch padb separately to analyze the code behavior.

Usage summary (for full list and explanations please consult
http://padb.pittman.org.uk/)

.. raw:: html

   <div>

 

::

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

 

.. raw:: html

   </div>

mpiP
^^^^

.. raw:: html

   <div>

mpiP: Lightweight, Scalable MPI Profiling  http://mpip.sourceforge.net/.
Collects statistical information about MPI functions. mpiP is a
link-time library, that means that it can be linked to the object file,
though it is recommended that you have recompiled the code with -g.
Debugging information is used to decode the program counters to a source
code filename and line number automatically. mpiP will work without -g,
but mileage may vary.

.. raw:: html

   </div>

.. raw:: html

   <div>

Usage example:

.. raw:: html

   </div>

::

    # assume you have you MPI flavor module loaded
    module load mpip/3.4.1

    # link or compile your code from scratch with -g
    mpif90 ­-g ­-o my_app my_app.f90 ­-lmpiP ­-lm ­-lbfd ­-liberty ­-lunwind
    # or
    mpif90 ­-o my_app my_app.o ­-lmpiP ­-lm ­-lbfd ­-liberty ­-lunwind

    # run the code normally (either interactively with salloc or as usual with sbatch) 
    salloc ­-p play ­-n 4 srun mpi_app

If everything works, you will see the mpiP header preceding your program
stdout, and there will be generated a text report file in your work
directory. File is small, no worries about quota. Please, consult the
link above for the file content explanation. During runtime, one can set
MPIP environment variables to change the profiler behavior. Example:

::

    export MPIP="-t 10.0 -k 2"

Scalasca
^^^^^^^^

Available through module load scalasca

 
