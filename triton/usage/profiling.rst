=========
Profiling
=========

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

Input/output profiling
----------------------

This will tell you how much time is spent reading and writing data,
where, and what type of patterns it has (big reads, random access, etc).
Note that you can see the time information when CPU profiling: if
input/output functions take a lot of time, you need to improve IO.

Lowest level: use strace to print the time taken in every system call
that accesses files. This is not that great.

::

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


