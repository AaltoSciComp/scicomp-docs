========
Training
========

Scientific computing and data science require special, practical
skills in programming and computer use.  However, these aren't often
learned in courses.

This page is your portal for training.  The focus is practical,
hands-on courses for scientists, not theoretical academic courses.  As
a broad classification, we divide the skills a scientist would need
into four big levels A-D:

.. list-table::

   * * **A (basics)**
     * Having a basic knowledge of university resources, so that you use the right tool for the right job and don't lose your data.
   * * **B (scientific computing)**
     * When you are doing science but existing software isn't enough: you have to connect things together (or make your own).
   * * **C (high performance computing)**
     * Using large computer clusters for large-scale analysis.  Basically, at Aalto, :doc:`Triton <../triton/index>`.
   * * **D (advanced high performance computing)**
     * Catch-all for everything past level C.
   * * **Special tracks**
     * Programming, scientific papers/posters/presentations, etc.  Can be at any level.

For course announcements at Aalto, see :doc:`the Scientific Computing
in Practice courses page <scip/index>`.

.. toctree::
   :maxdepth: 1

   scip/index
   scicomp-announcements-maillist

If you're starting research, ask your advisor what level of skill they
expect you to have.  There are both courses and self-study materials
below.  A few hours now can save you days of time during your career.

Subpages:

.. toctree::
   :maxdepth: 1

   linux-shell-tutorial
   python-scicomp/index


A: Basics
=========

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * A01

       University IT systems

     * This covers the basics of research facilities at Aalto and how to use them.


     * For now see :doc:`../aalto/welcomeresearchers`.

     *

   * * A10

       Configuring Mac for scientific work

     * Getting your Mac computer set up for scientific computing
       tasks.  After this, you can follow most of the other
       instructions below which assume a Linux-like system.

     *

     *

   * * A11
       Configuring Windows for scientific work

     * Like A10, but for Windows.  (Why isn't there a Linux course?
       Because these are to get you close enough to Linux to have the
       power you need for computing.)

     *

     *

..
  Lapiokurssi - computer as a tool.  What the different computational
  options are, and how to get your systems set up to do this.  how to
  not get into a rut of doing the same things all the time.




B: Scientific computing
=======================

..
  https://training.linuxfoundation.org/linux-courses/system-administration-training/introduction-to-linux%20

**Core courses:**

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * B10

       Basic shell
     * Let's face it: the linux command line is the basis of most data
       science if you are doing more than running other people's
       programs.

     * `Software Carpentry shell-novice sections
       1-4 <https://swcarpentry.github.io/shell-novice/>`__.  Our
       :doc:`shell course <linux-shell-tutorial>` covers this at the
       beginning, too.

     *

   * * B14

       Data management
     * If you do the obvious thing, your data will turn into a huge
       mess and you won't be able to work anymore.  This course gives
       some practical hints.

     * (For now, check out :doc:`the data section <../data/index>`)

     *

   * * B23

       Text editors and IDEs
     * Your best friend is a good text editor - sometimes you just
       need to edit things quickly on some remote system.

     * `Software Carpentry
       shell-novice, part of section 3
       <https://swcarpentry.github.io/shell-novice/>`__.

     *

   * * B20

       Shell scripting
     * If you can do it on the Linux shell, you can automate it.

     * Continue with the :doc:`Science-IT Linux shell tutorial
       <linux-shell-tutorial>`.

     *

   * * B21

       Version control for you
     * Version control lets you track changes, go back in time, and
       collaborate on code and papers: an absolute requirement for
       scientific computing.

     * `CodeRefinery Introduction to version
       control <https://coderefinery.org/lessons/>`__

     *

   * * B22

       SSH and remote access
     * A short but important course: how to do work remotely.
       Different expert tips for making ssh better, too.

     *

     *

**Other courses:**

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * B30

       Makefiles
     * Makefiles are like smart shell scripts.  We learn some about
       them and in the process, become ever more efficient.

     * `Software
       Carpentry make-novice
       <https://swcarpentry.github.io/make-novice/>`__.

     *

   * * B50

       Version control for teams
     * Previously, you learned only the basics.  Now for the real
       stuff.

     * `CodeRefinery collaborative distributed version control
       lesson <https://coderefinery.org/lessons/>`__

     *

   * * B51

       Jupyter Notebooks
     * Notebooks are an efficient way to make self-documenting code
       and scripts and do data science well.

     * `CodeRefinery Jupyter
       course <https://coderefinery.org/lessons/>`__.

     *

**Software development track:** Do you do programming?  These courses are
for you.  This does *not* teach you how to program: you need to find
your own course for that, but this will make sure you can do
scientific programming well.

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * B60

       Modular code development

     *

     * `CodeRefinery lesson <https://coderefinery.org/lessons/>`__

     *

   * * B61

       Software testing

     *

     * `CodeRefinery lesson <https://coderefinery.github.io/testing/>`__

     *

   * * B62

       Profiling

     *

     * See :doc:`../triton/usage/profiling` for now.

     *

   * * B63

       Debugging

     *

     * Aalto course, for example `course by Janne <https://users.aalto.fi/~jblomqvi/scip/2016/scip-slides/debugging.html>`__

     *

   * * B02

       Software Licensing
     *

     * `CodeRefinery lesson <https://cicero.xyz/v2/remark/github/coderefinery/software-licensing/master/talk.md/>`__

     *


C: High performance computing
=============================

When your own computer is not enough, you need more power.  For that,
high-performance computing is your next step.  Level C is about using
HPC, level D is about programming it yourself.

**Core courses:**

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * C01

       What is HPC?

     * Before you can use larger resources, you need to understand the
       difference from your own computers

     * :doc:`training by Science-IT <scip/index>`,
       :doc:`../triton/tut/intro`

     *

   * * C20

       Modules and software

     * Using and installing software on a cluster is different from
       your own computer, because hundreds of people are sharing it.
       Modules are the solution.

     * :doc:`Scientific Computing in Practice training by Science-IT <scip/index>` or
       :doc:`../triton/tut/modules`

     *

   * * C21

       Slurm

     * On a cluster, you have to share resources with others.  Slurm
       is one batch queuing system that makes it possible.

     * See :doc:`Scientific Computing in Practice training by Science-IT <scip/index>` or
       :doc:`interactive <../triton/tut/interactive>`,
       :doc:`serial <../triton/tut/serial>`,
       :doc:`array <../triton/tut/array>`

     *

   * * C22

       HPC Storage

     * Storage turns out to be just as important as computing power.
       There are different places available, each with different
       advantages.

     * See :doc:`Scientific Computing in Practice training by Science-IT <scip/index>`  or
       :doc:`storage basics <../triton/tut/storage>`,
       :doc:`lustre <../triton/usage/lustre>`,
       :doc:`local storage <../triton/usage/localstorage>`,
       :doc:`small files <../triton/usage/smallfiles>`

     *

   * * C23

       Parallel computing

     * The point of a cluster is to run things in parallel.  How does
       this work?

     * See :doc:`Scientific Computing in Practice training by Science-IT <scip/index>`, and
       :doc:`../triton/tut/parallel`.

     *

   * * C24

       Advanced shell scripting and automation

     * Hands-on shell scripting, putting everything together to
       automate large computations on the cluster.

     * Various courses,
       finishing the :doc:`linux shell tutorial
       <linux-shell-tutorial>` is a good start.

     *



D: Advanced high performance computing
======================================

.. list-table::
   :header-rows: 1

   * *

     *

     * Reading

     * Video

   * * Dxx

       Parallel programming computers

     * This is an academic course taught in the CS department.  It
       mainly covers OpenMP and CUDA.  Usually taught in 5th period
       (Apr-May), `search MyCourses/Oodi for CS-E4580
       <https://oodi.aalto.fi/a/opintjakstied.jsp?html=1&Kieli=6&Tunniste=CS-E4580>`__.

     *

     *

   * * Dxx

       GPU Programming
     * This was an advanced guest course, useful if you want to know
       how to program GPU applications.

     * `Materials here
       <http://science-it.aalto.fi/scip/gpu-computing-fall-2017/>`__.

     *

   * * Dxx

       MPI Programming
     * This was an advanced guest course, useful if you want to know
       internals of MPI or program MPI applications.

     * `Materials here
       <http://science-it.aalto.fi/scip/mpi-intro-spring-2018/>`__.

     *

   * * Dxx

       HTCondor
     * Condor allows you to use many workstations as a high throughput
       cluster, ideal for mid-range embarrassingly parallel problems.

     * `Materials here
       <http://science-it.aalto.fi/scip/condor2017/>`__.

     *

Also see the `Science-IT training archive
<http://science-it.aalto.fi/scip/>`__ for more level D courses.

Recommended programming courses
===============================

Need to learn programming?  We will include some recommended
online programming courses here.

..
  Recommended programming courses.  what's current bleeding edge?

  Python
  R
  Matlab
  shell
