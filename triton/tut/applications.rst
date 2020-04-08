============
Applications
============

In this tutorial, we talk about the overall process of finding,
building, and compiling software.  These days, installing and managing
scientific software is taking more and more time, thus we need to
specifically talk about it some.

.. seealso::

   Main article: :doc:`../apps/index`


Available softwares
===================

You can find what softwares we have available in different ways:

* First, you should check our :doc:`Applications  <../apps/index>` page
  and see if the software you need is already available and has
  instructions.
* If you find the software you need available, you can usually load it via a module.
  The next tutorial, :doc:`Software modules <modules>` explains what modules
  are and how to work with them.
* You can also search this tutorial to see what you can find (though
  note that not everything is in the Triton section here - some applies
  to Aalto workstations or own computers).
* It's always a good idea to search the `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ to see if
  there are previous issues about it - not everything is always
  updated.



Modules
=======

You can learn about modules on the :doc:`Software modules <modules>` tutorial.
But generally, ``module`` is a command that allows you to get and remove 
access to other software - because not everything can be available at once.  
The :doc:`Software modules <modules>` tutorial teaches how to
load modules using the command ``module load $NAME``, etc.

Not all of the software we have available is documented.  You can
``module spider $NAME`` to try to see if you can find a module
that way.  Note that this is *partially* case sensitive so it can
be hard to find things - you might need to look through ``module
avail`` too, to find all the available modules.


Common applications
^^^^^^^^^^^^^^^^^^^

For reference, here are the most common softwares:

* **Python:** ``module load anaconda`` for the Anaconda distribution
  of Python 3, including a lot of useful packages.  :doc:`More info
  <../apps/python>`.

* **R:** ``module load r`` for a basic R package.  :doc:`More info
  <../apps/r>`.

* **Matlab:** ``module load matlab`` for the latest Matlab version.
  :doc:`More info <../apps/matlab>`.


Singularity containers
======================

.. seealso::

   Main article: :doc:`../usage/singularity`

Some softwares have become so complicated that they just can't be installed, 
and for that we use containers.  A software container is basically a
complete self-contained operating system environment.  Another
advantage of containers is that they make it easy to move installed
software from system to system, so that you can have the same
environment everywhere.

You can read about singularity containers :doc:`here <../usage/singularity>`.  
If you load a module that uses singularity, nothing will happen at first.  
You execute your software using ``singularity_wrapper exec``, 
or use ``singularity_wrapper shell`` to get a shell in there.


Requesting new software
=======================

We aim to install a good base of software for our users - but it's not
possible to keep up with all requests.  If you need something, submit
a request to our :ref:`issue tracker <issuetracker>`, but be aware
that despite best efforts, we can't do everything.  
See the main :doc:`Applications <../apps/index>` page for more information.



Exercises
=========

1. Figure out how to use ``tensorflow`` (this is not a software
   problem, but a searching the documentation problem).  Make it work
   enough to do ``python`` and ``import tensorflow`` -- though you
   will get an error which you will learn to solve in a later lesson.

2. Figure out how to run ``openfoam`` by searching the docs (use the
   new image).  Using ``singularity_wrapper``, run ``foamExec`` so
   that it fails with the error message ``no application specified``.
   Try ``singularity_wrapper shell``, too.


What's next?
============

The next tutorial covers :doc:`software modules <modules>` in more detail.
