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

If you're starting research, ask your advisor what level of skill they
expect you to have.  There are both courses and self-study materials
below.  A few hours now can save you days of time during your career.

Subpages:

.. toctree::
   :maxdepth: 1

   by-science-it
   linux-shell-tutorial


A: Basics
=========

.. list-table::

   * * A01
       University IT systems

     * This covers the basics of research facilities at Aalto and how to use them.

       There is not currently a dedicated course, but, but all of our
       information is found at :doc:`../aalto/welcomeresearchers`.

..
  Lapiokurssi - computer as a tool.  What the different computational
  options are, and how to get your systems set up to do this.  how to
  not get into a rut of doing the same things all the time.




B: Scientific computing
=======================

..
  https://training.linuxfoundation.org/linux-courses/system-administration-training/introduction-to-linux%20

Core courses:

.. list-table::

   * * B10

       Basic shell
     * Let's face it: the linux command line is the basis of most data
       science.  `Check out Software Carpentry shell-novice sections 1-3
       <http://swcarpentry.github.io/shell-novice/>`__

   * * B14

       Data management
     * If you do the obvious thing, your data will turn into a huge
       mess and you won't be able to work anymore.  This course gives
       some practical hints.  (For now, check out :doc:`the data section <../data/index>`)

   * * B23

       Text editors and IDEs
     * Your best friend is a good text editor.  `Software Carpentry
       shell-novice, part of section 3 <http://swcarpentry.github.io/shell-novice/>`__.

   * * B20

       Shell scripting
     * If you can do it on the Linux shell, you can automate it.
       Continue with `Software Carpentry shell-novice above section 4-end
       <http://swcarpentry.github.io/shell-novice/>`__

   * * B21

       Version control
     * Version control lets you track changes, go back in time, and
       collaborate on code and papers: an absolute requirement for
       scientific computing.  `CodeRefinery Introduction to version
       control <http://coderefinery.org/lessons/>`__

   * * B22

       SSH and remote access
     * A short but important course: how to do work remotely.
       Different expert tips for making ssh better, too.


Other courses:

.. list-table::

   * * B30

       Makefiles
     * Makefiles are like smart shell scripts.  We learn some about
       them and in the process, become ever more efficient.  `Software
       Carpentry make-novice <http://swcarpentry.github.io/make-novice/>`__.

   * * B50

       Advanced version control
     * Previously, you learned only the basics.  Now for the real stuff.

   * * B51

       Jupyter Notebooks
     * Notebooks are an efficient way to make self-documenting code
       and scripts and do data science well.  `CodeRefinery jupyter
       course <http://coderefinery.org/lessons/>`__.

Software development track: Do you do programming?  These courses are
for you.  This does *not* teach you how to program: you need to find
your own course for that, but this will make sure you can do
scientific programming well.

.. list-table::

   * * B60

       Modular code development
     * `CodeRefinery lesson <http://coderefinery.org/lessons/>`__

   * * B61

       Software testing
     * `CodeRefinery lesson <https://coderefinery.github.io/testing/>`__

   * * B62

       Profiling
     * Aalto course, see :doc:`../triton/usage/profiling` for now.

   * * B63

       Debugging
     * Aalto course, for example `course by Janne <https://users.aalto.fi/~jblomqvi/scip/2016/scip-slides/debugging.html>`__

   * * B02

       Software Licensing
     * `CodeRefinery lesson <http://cicero.xyz/v2/remark/github/coderefinery/software-licensing/master/talk.md/>`__



C: High performance computing
=============================


.. list-table::

   * * C01

       What is HPC?
     * See :doc:`training by Science-IT <by-science-it>`
   * * C20

       Modules and software
     * See :doc:`training by Science-IT <by-science-it>` or
       :doc:`../triton/tut/modules`
   * * C21

       Slurm
     * See :doc:`training by Science-IT <by-science-it>` or
       :doc:`../triton/tut/modules`
   * * C22

       HPC Storage
     * See :doc:`training by Science-IT <by-science-it>`  or
       :doc:`../triton/tut/modules`
   * * C23

       Parallel computing
     * See :doc:`training by Science-IT <by-science-it>`
   * * C24

       Advanced shell scripting and automation
     * Hands-on, putting everything together.


D: Advanced high performance computing
======================================

.. list-table::

   * * Dxx

       Parallel programming computers
     * This is an academic course taught in the CS department.  It
       mainly covers OpenMP and CUDA.  Usually taught in 5th period
       (Apr-May), `search MyCourses/Oodi for CS-E4580
       <https://oodi.aalto.fi/a/opintjakstied.jsp?html=1&Kieli=6&Tunniste=CS-E4580>`__.

   * * Dxx

       GPU Programming
     * This was an advanced guest course, useful if you want to know
       how to program GPU applications `Materials here
       <http://science-it.aalto.fi/scip/gpu-computing-fall-2017/>`__.

   * * Dxx

       MPI Programming
     * This was an advanced guest course, useful if you want to know
       internals of MPI or program MPI applications.  `Materials here
       <http://science-it.aalto.fi/scip/mpi-intro-spring-2018/>`__.

Also see the `Science-IT training archive
<http://science-it.aalto.fi/scip/>`__ for more level 3 courses.

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
