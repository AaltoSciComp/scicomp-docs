============
Applications
============

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=_YMO-1dPc1E&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=8>`__

In this tutorial, we talk about the overall process of finding,
building, and compiling software.  These days, installing and managing
scientific software is taking more and more time, thus we need to
specifically talk about it.

Clusters, being a shared systems, has more complicated software
requirements.  In this tutorial, you will learn how to use
existing software.  Be aware that installing your own is possible (and
people do it all the time), but does require some attention to
details.  Either way, you will need to know the basics of software on
Linux.

.. admonition:: Cheatsheet

   * There are many ways to get software on Triton: we use the
     standard module system, have Singularity containers, and you can
     install your own.
   * :doc:`Modules <modules>` allow you to activate a lot of software.
   * :doc:`Singularity containers <../usage/singularity>` allow you to
     run other hard-to-install software.
   * Ask us to install software if you need it.  You can also install
     software yourself, but you need to update instructions to do a
     user install (as opposed to admin install).

.. seealso::

   Main article: :doc:`../apps/index`

.. admonition:: Local differences

   Almost every site will use modules.  The exact module names, and
   anything beyond that, will be different.  Containers are becoming
   more common, but they are less standardized.



How to find the software you need
---------------------------------

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
* Ask other users in the :ref:`Zulip chat <chat>`. We hope that we can facilitate user
  group meetings and discussion among users of similar software suites.
* Ask us admins/Research Software Engineers in `garage </help/garage>`.

Throughout this process, try to remember these things:

1. Scientific software, like scientific process itself, is collaborative.
   Work on sharing and seeking knowledge among other users. They might have
   the answer you need.
2. Interesting problems draw people together independently. If you're working
   on a certain type of a problem, it is quite likely that some other
   researcher is working on a similar problem. You might not be alone with
   your problem.
3. Try to form connections between users of similar software. The same software
   that you use can be used by a researcher in completely different field. Many
   software suites e.g. statistical modelling, machine learning, is common to
   many other fields. If you cannot find similar users within your field, look
   across fields.
4. If you find something useful or interesting, share it. If you do not know
   who to share it with, share it with us in SciComp. When we hear of a tool,
   a method, a success story or a problem encountered by one of our users, we
   often try to share it among other researchers.



Common applications are available as modules
--------------------------------------------

.. important::

   This is Aalto-specific.  Some of these will work if you ``module
   load fgci-common`` at other Finnish sites (but not CSC).  This is
   introduced in the next lesson.

Here is a sample of our most commonly used software:

.. include:: ../ref/software.rst

If one of these ``module load`` commands does not work at your site,
try ``module spider $NAME`` and see if you can find it.  More information
on these commands will be 
actually covered under the upcoming :doc:`modules <modules>` tutorial.

We try to install commonly used software for all of our users, so that
everyone can benefit from them. If you cannot find what you're looking for,
do let us know.



Singularity containers
----------------------

.. seealso::

   Main article: :doc:`../usage/singularity`

Some software packages are either very complicated to install or they
have been designed with certain operating systems in mind. For these
kinds of software we often use containers. A software container is basically a
complete self-contained operating system environment. Another advantage of
containers is that they make it easy to move installed software from system
to system, so that you can have the same environment everywhere.

If your program is usually deployed using Docker or it is hard to maintain,
do read our documentation on Singularity containers and contact us for
more information.

We also provide :doc:`some containers built by NVIDIA <../apps/nvidiacontainers>`.
These containers are from NVIDIA's NGC-repository and meant for GPU
computations.



Requesting new software
-----------------------

We aim to install a good base of software for our users - but it's not
possible to keep up with all requests.  If you need something, submit
a request to our :ref:`issue tracker <issuetracker>`, but be aware
that despite best efforts, we can't do everything.
See the main :doc:`Applications <../apps/index>` page for more information.



Writing software
----------------

Not everyone has to, but many people either write there own software
or writ scripts to automate the running and analysis.  Yet, these
skills are often not developed as well as they should be.  Contact the
:doc:`Research Software Engineers </rse/index>` (part of Science-IT)
for help here - basic service is free.



A plea: make your software reusable!
------------------------------------

Five years from now, when you are releasing your own software that you
want others to use, :doc:`make it easy to install and reusable
</scicomp/packaging-software>`.



Exercises
---------

If you are at Aalto, everything will work.  Otherwise, if you are in
Finland (but not at CSC) ``module load fgci-common`` will make our
modules available on your cluster.

.. exercise:: Applications-1: Tensorflow

   Figure out how to use ``tensorflow`` (this is not a software
   problem, but an "assignment zero" searching the documentation problem).  Make it work
   enough to run ``python`` and ``import tensorflow``.

.. exercise:: Applications-2: Check your needs

   Find the Applications page link above, and check the list for ways
   to find out if we already have your software installed.  See if we have
   what you need, using any of the strategies on that list.

.. exercise:: (optional) Applications-3: Spack package list

   From the Applications page, find the Spack package list
   (warning: it's a very long page and takes a while to load).  Does
   it have anything useful to you?

.. exercise:: (optional) Applications-4: Your group's needs

   Discuss among your group what software you need, if it's available,
   and how you might get it.  Can they tell you how to get started?

What's next?
------------

The next tutorial covers :doc:`software modules <modules>` in more detail.
