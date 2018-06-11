=========
Profiling
=========

.. note::

   Also see :doc:`debugging`.

You have code, you want it to run fast. This is what Triton is for. But
how do you know if your code is running as fast as it can? We are
scientists, and if things aren't quantified we can't do science on them.
Programming can often seem like a black box: modern computers are
extremely complicated, and people can't predict what is actually making
code fast or slow anymore. Thus, you need to *profile* your code: get
detailed performance measurements. These measurements let you know how
to make it run faster.

There are many tools for profiling, and it really is one of the
fundamental principles for any programming language. You really should
learn how to do quick profile just to make sure things are OK, even if
you aren't trying to optimize things: you might find a quick win even if
you didn't write the code yourself (for example, 90% of your time is
spent on input/output).

This page is under development, but so far serves as an introduction. We
hope to expand it with specific Triton examples.


Summary: profiling on Linux
---------------------------

First off, look at your language-specific profiling tools.

-  Generic Linux profiling tools (big and comprehensive list, also some
   presentations):\ http://www.brendangregg.com/linuxperf.html
-  Profiling in C and Python (introduction + examples):
   http://rkd.zgib.net/scicomp/profiling/profiling.html

CPU profiling
-------------

This can give you a list of where all your processor time is going,
either per-function or per-line. Generally, most of your time is in a
very small region of your code, and you need to know what this is in
order to improve *just* that part.

See the C and Python profiling example above.


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
later on, at no performance cost)::

  $ gfortran -Wall -g -O3 mymatmul.f90

Run the program via the profiler to generate profile data::

  $ perf record ./a.out

Now we can look at the profile::

 $ perf report
 # Samples: 1251
 #
 # Overhead Command Shared Object Symbol
 # ........ .............. ............................. ......
 #
 85.45% a.out ./a.out [.] MAIN\_\_
 4.24% a.out /usr/lib/libgfortran.so.3.0.0 [.] \_gfortran\_arandom\_r4
 3.12% a.out /usr/lib/libgfortran.so.3.0.0 [.] kiss\_random\_kernel

So 85% of the runtime is spent in the main program (symbol MAIN\_\_),
and most of the rest is in the random number generator, which the
program calls in order to generate the input matrices.

Now, lets take a closer look at the main program::

  $ perf annotate MAIN__
  ------------------------------------------------
  Percent \| Source code & Disassembly of a.out
  ------------------------------------------------
  :
  :
  :
  : Disassembly of section .text:
  :
  : 00000000004008b0 <MAIN__>:

... ::

  : c = 0.
  :
  : do j = 1, n
  : do k = 1, n
  : do i = 1, n
  : c(i,j) = c(i,j) + a(i,k) \* b(k,j)
  30.12 : 400a40: 0f 28 04 01 movaps (%rcx,%rax,1),%xmm0
  4.92 : 400a44: 0f 59 c1 mulps %xmm1,%xmm0
  12.36 : 400a47: 0f 58 04 02 addps (%rdx,%rax,1),%xmm0
  40.73 : 400a4b: 0f 29 04 02 movaps %xmm0,(%rdx,%rax,1)
  9.65 : 400a4f: 48 83 c0 10 add $0x10,%rax

Unsurprisingly, the inner loop kernel takes up practically all the time.

For more information on using perf, see the perf tutorial at

https://perf.wiki.kernel.org/index.php/Tutorial


Input/output profiling
----------------------

This will tell you how much time is spent reading and writing data,
where, and what type of patterns it has (big reads, random access, etc).
Note that you can see the time information when CPU profiling: if
input/output functions take a lot of time, you need to improve IO.

``/usr/bin/time -v`` prints some useful info about IO operations and
statistics.

Lowest level: use strace to print the time taken in every system call
that accesses files. This is not that great.::

    #  Use strace to print the total bytes
    strace -e trace=desc $command |& egrep 'write' | awk --field-separator='='  '{ x+=$NF } END { print x }'
    strace -e trace=desc $command |& egrep 'read' | awk --field-separator='='  '{ x+=$NF } END { print x }'

    # Number of calls only
    strace -e trace=file -c  $command


Memory profiling
----------------

Less common, but it can tell you something about what memory is being
used.

If you are making your own algorithms, memory profiling becomes more
important because you need to be sure that you are using the memory
hierarchy efficiently. There are tools for this.


MPI and parallel profiling
--------------------------

mpiP
^^^^

mpiP: Lightweight, Scalable MPI Profiling http://mpip.sourceforge.net/.
Collects statistical information about MPI functions. mpiP is a
link-time library, that means that it can be linked to the object file,
though it is recommended that you have recompiled the code with -g.
Debugging information is used to decode the program counters to a source
code filename and line number automatically. mpiP will work without -g,
but mileage may vary.


Usage example::

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
MPIP environment variables to change the profiler behavior. Example::

    export MPIP="-t 10.0 -k 2"


Scalasca
^^^^^^^^

Available through module load scalasca


