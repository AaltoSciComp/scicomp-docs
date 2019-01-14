============
Applications
============

The previous tutorial taught you about :doc:`modules <modules>`.
Here, we talk a bit more about the overall process of finding,
building, and compiling software.  These days, installing and managing
scientific software is taking more and more time, thus we need to
specifically talk about it some.

.. seealso::

   This assumes that you have read the previous tutorial about
   :doc:`modules <modules>`.

   Main article: :doc:`../apps/index`


Available software
==================

You can find what software we have available in different ways:

* First, you should check our :doc:`applications page <../apps/index>`
  and see if the software you need is already available and if it has
  instructions.
* You should also search this site to see what you can find (though
  not that not everything is in the Triton section here - some applies
  to Aalto workstations or own computers).
* Then, you should search the `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ to see if
  there are previous issues about it - not everything is always
  updated.
* Check the available modules with ``module spider`` and ``module
  avail`` (next section) to see what's available but undocumented.

If you find software available, you will usually load it via a module:


Modules
=======

As you learned in the :doc:`previous tutorial <modules>`, ``module`` is
a command that allows you to get and remove access to other software -
because not everything can be available at once.  Refer to the section
on :doc:`modules <modules>` for info - basically ``module load
$NAME``.

Not all of the software we have available is documented.  You can
``module spider $NAME`` to try to see if you can find a module
that way.  Note that this is *partially* case sensitive so it can
be hard to find things - you might need to look through ``module
avail`` some, too.  To see just what a module does, remember ``module
show``.


Singularity containers
======================

.. seealso::

   Main article: :doc:`../usage/singularity`

Some software has gotten so hard that it just can't be installed, and
for that we use containers.  A software container is basically a
complete self-contained operating system environment.  Another
advantage of containers is that it makes it easy to move installed
software from system to system, so that you can have the same
environment everywhere.

You can read about :doc:`singularity from its page
<../usage/singularity>`.  For now, realize that, after you load some
modules, you may need to run ``singularity_wrapper`` to use them.


Compilers and toolchains
========================

.. seealso::

   Main article: :doc:`../usage/toolchains`

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

Toolchains change often - check back for latest info if you need to
use one.



Requesting new software
=======================

We aim to install a good base of software for our users - but it's not
possible to keep up with all requests.  If you need something, submit
a request to our :ref:`issue tracker <issuetracker>`, but be aware
that despite best efforts, we can't do everything.  See the :doc:`main
applications info page <../apps/index>`.



Exercises
=========

1. Figure out how to use ``tensorflow`` (this is not a software
   problem, but a searching the documentation problem).  Make it work
   enough to do ``python`` and ``import tensorflow`` -- though you
   will get an error which you will learn to solve in a later lesson.

2. Figure out how to run ``openfoam``.  Run ``foamExec`` so that it
   fails with the error message ``no application specified``.


Next steps
==========

The next tutorial is :doc:`data storage <storage>`
