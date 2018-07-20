============
Applications
============

The previous tutorial taught you about :doc:`modules <modules>`.
Here, we talk a bit more about the overall process of finding,
building, and compiling software.  In modern times, the difficulty of
configuring and compiling software is taking up more and more time,
thus the need to cover it.


Available software
==================

First, you should check our :doc:`applications page <../apps/index>`
and see if the software you need is already available and if it has
instructions.  You should also search this site to see what you can
find (though not that not everything is in the Triton section here -
some applies to Aalto workstations or own computers).

If you find software available, you will usually load it via a module:


Modules
=======

As you learned in the :doc:`previous section <modules>`, ``module`` is
a command that allows you to get and remove access to other software -
because not everything can be available at once.  Refer to the section
on :doc:`modules <modules>` for info - basically ``module load
$NAME``.

Not all of the software we have available is documented.  You should
also ``module spider $NAME`` to try to see if you can find a module
that way.  Note that this is case sensitive in a weird away so it can
be hard to find things - you might need to look through ``module
avail`` some, too.


Singularity containers
======================

Some software has gotten so hard that it just can't be installed, and
for that we use containers.  A software container is basically a
complete self-contained operating system environment.

You can read about :doc:`singularity from its page on scicomp
<../usage/singularity>`.  For now, realize that, after you load some
modules, you may need to run `singularity_wrapper` to use them.


Compilers and toolchains
========================

Some people need to compile your own code.  You can try to use the
operating system ``gcc``, but it is likely too old and doesn't have
the necessary libraries.  Instead, load a :doc:`toolchain
<../usage/toolchains>` which contains a fixed compiler and support
libraries.

For GCC-based tool chains, check ``module spider goolf`` and, for
example, ``module load goolf/triton-2017a``.  For Inter-based
compilers, try ``module spider iomkl`` and, for example, ``module load
iomkl/triton-2017a``.  (These stand for "gcc openmpi openblas lapack
fftw" and "intel openmpi intel-mkl")

For more info, see ``toolchain``


Exercises
=========

1. Figure out how to use ``tensorflow``.  Make it work enough to do
   ``python`` and ``import tensorflow`` -- though you will get an
   error which you will learn to solve in a later lesson.

2. Figure out how to run ``openfoam``.  Run ``foamExec`` so that it
   fails with the error message ``no application specified``.


Next steps
==========

The next tutorial is :doc:`data storage <storage>`
