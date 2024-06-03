================
Software modules
================

.. include:: /triton/ref/videos.rst

There are hundreds of people using every cluster.  They all have different
software needs, including conflicting versions required for different
projects!  How do we handle this without making a mess, or one person
breaking the cluster for everyone?

This is actually a very hard, but solved within certain parameters,
problem.  Software installation and management takes up a huge amount
of our time, but we try to make it easy for our users.  Still, it can
end up taking a lot of your effort as well.

.. admonition:: Abstract

   * We use the standard `Lmod module system
     <https://lmod.readthedocs.io/>`__, which makes more software
     available by adjusting environment variables like ``PATH``.
   * ``module spider NAME`` searches for NAME.
   * ``module load NAME`` loads the module of that name.  Sometimes,
     it can't until you ``module load`` something else (read the
     ``module spider`` message carefully).
   * See the :doc:`../ref/index` for a ``module`` command cheatsheet.

.. admonition:: Local differences

   Almost every site uses modules, and most use the same Lmod system
   we use here.  But, the exact module names you can load will be
   different.



Introduction to modules
-----------------------

The answer is the standard "module" system `Lmod <https://lmod.readthedocs.io/en/latest/>`__.
It allows us to
have unlimited number of different software packages installed, and the
user can select what they want.  Modules include everything from
compilers (+their required development files), libraries, and programs.
If you need a program installed, we will put it in the module system.

In a system the size of Triton, it just isn't possible to install all
software by default for every user.

A module lets you adjust what software is available,
and makes it easy to switch between different versions.

As an example, let's inspect the ``triton_base_python`` module with ``module
show scicomp-python-env``:

.. highlight:: console

.. code-block:: console

    $ module show scicomp-python-env
    ----------------------------------------------------------------------------
      /appl/scibuilder-mamba/aalto-rhel9/prod/modules/scicomp-python-env/2024-01.lua:
    ----------------------------------------------------------------------------
    whatis("Name : scicomp-python-env")
    whatis("Version : 2024-01")
    help([[This is an Aalto Scientific Computing managed Python environment with various packages.]])
    family("conda")
    prepend_path("PATH","/appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564/bin")
    setenv("CONDA_PREFIX","/appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564")
    setenv("GUROBI_HOME","/appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564")
    setenv("GRB_LICENSE_FILE","/appl/manual_installations/software/gurobi/license/gurobi.lic")
    setenv("OMPI_MCA_btl_openib_allow_ib","true")
    setenv("SLURM_MPI_TYPE","pmix")
    setenv("PMIX_MCA_psec","^munge")


The command shows some meta-info (name of the module, its version, etc.)
When you load this module, it adjusts various environment paths (as
you see there),
so that when you type ``python`` it runs the program from
``/appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564/bin``.
This is almost magic: we can have many versions of any software installed,
and everyone can pick what they want, with no conflicts.



Loading modules
---------------

Let's dive right into an example and load a module.

.. admonition:: Local differences

   If you are not at Aalto, you need to figure out what modules exist
   for you.  The basic princples probably work on almost any cluster.

Let's assume you've written a Python script that is only compatible
with Python version 3.7.0 or higher. You open a shell to find out
where and what version our Python is. The ``type`` program looks up
the current detected version of a program - very useful when testing
modules (if this doesn't work, use ``which``).::

  $ type python3
  python3 is /usr/bin/python3
  $ python3 -V
  Python 3.9.18

But you need a newer version of Python.  To this end, you can **load**
the ``scicomp-python-env`` module using the ``module load scicomp-python-env`` command,
that has a more up to date Python with lots of libraries already
included::

  $ module load scicomp-python-env
  $ type python3
  python3 is /appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564/bin/python
  $ python3 -V
  Python 3.11.9

As you see, you now have a newer version of Python, in a different
directory.

You can see a list of the all the loaded modules in our working shell
using the ``module list`` command::

  $ module list
  Currently Loaded Modules:
    1) scicomp-python-env/2023-01

.. note::
  The ``module load`` and ``module list`` commands can be abbreviated as ``ml``


Let's  use the ``module purge`` command to **unload** all the loaded
modules::

  $ module purge

Or explicitly unload the ``scicomp-python-env`` module by using the ``module
unload scicomp-python-env`` command::

  $ module unload scicomp-python-env

You can load any number of modules in your open shell, your scripts,
etc.  You could load modules in your ``~/.bash_profile``, but then it
will always automatically load it - this causes unexplainable bugs
regularly!

.. warning::

  We regularly see problems caused by something in ``~/.bash_profile`` /
  ``~/.bash_rc`` affecting other unrelated software in
  hard-to-understand ways.  Be very cautious about anything in your
  shell startup files, and always remove it as a first debugging step.


Module versions
---------------

What's the difference between ``module load scicomp-python-env`` and
``module load scicomp-python-env/2024-01``?

The first ``scicomp-python-env`` loads the version that Lmod assumes to
be the latest one - which might change someday!  Suddenly, things don't
work anymore and you have to fix them.

The second loading ``scicomp-python-env/2024-01`` loads that exact version,
which won't change.  Once you want stability (possibly from day one!), it's
usually a good idea to load specific version, so that your environment
will stay the same until you are done.



Hierarchical modules
--------------------

Hierarchical modules means that you have to load one module before you
can load another.  This is usually a compiler:

**Warning: This example is not yet updated for new-Triton and won't work
anymore.  The concept still applies.**

For example, let's load a newer version of R:

.. code-block:: console
  :emphasize-lines: 3-4

  $ module load r/4.2.2
  Lmod has detected the following error:  These module(s) or
  extension(s) exist but cannot be loaded as requested: "r/4.2.2"
     Try: "module spider r/4.2.2" to see how to load the module(s).

Lmod says that the modules exist but can't be loaded, but gives a hint
for what to do next.  Let's do that:

.. code-block:: console
   :emphasize-lines: 7-9

   $ module spider r/4.2.2

   ----------------------------------------------------------------------------
     r: r/4.2.2
   ----------------------------------------------------------------------------

       You will need to load all module(s) on any one of the lines below before the "r/4.2.2" module is available to load.

   gcc/11.3.0

       Help:
       ...

So now we can load it (we can do it in one line)::

  $ module load gcc/11.3.0 r/4.2.2
  $ R --version
  R version 4.2.2 (2022-10-31) -- "Innocent and Trusting"




What's going on under the hood here?
------------------------------------

In Linux systems, different environment variables like ``$PATH`` and
``$LD_LIBRARY_PATH`` help figure out how to run programs.  Modules
just cleverly manipulate these so that you can find the software you
need, even if there are multiple versions available.  You can see
these variables with the **echo** command, e.g. ``echo $PATH``.

When you load a module in a shell, the module command changes the
current shell's environment variables, and the environment variables
are passed on to all the child processes.

You can explore more with ``module show NAME``.



Making a module collection
--------------------------

There is a basic dependency/conflict system to handle module
dependency. Each time you load a module, it resolves all the
dependencies. This can result in long loading times or be annoying to
do each time you log in to the system. However, there is a solution:
``module save COLLECTION_NAME`` and ``module restore COLLECTION_NAME``

Let's see how to do this in an example.  **Warning: This example is not
yet updated for new-Triton and won't work anymore.  The concept still
applies.**

Let's say that for compiling / running your program you need:

  - a compiler
  - CMake
  - MPI libraries
  - FFTW libraries
  - BLAS libraries

You could run this each time you want to compile/run your code::

  $ module load gcc/9.2.0 cmake/3.15.3 openmpi/3.1.4 fftw/3.3.8-openmpi openblas/0.3.7
  $ module list           # 15 modules

Let's say this environment works for you. Now you can save it with
``module save MY-ENV-NAME``.  Then ``module purge`` to unload
everything.  Now, do ``module restore MY-ENV-NAME``::

  $ module save my-env
  $ module purge
  $ module restore my-env
  $ module list           # same 15 modules

Generally, it is a good idea to save your modules as a collection to
have your desired modules all set up each time you want to
re-compile/re-build.

So the subsequent times that you want to compile/build, you simply
``module restore my-env`` and this way you can be sure you have the
same previous environment.

.. note::
  You may occasionally need to rebuild your collections in case we
  re-organize things (it will prompt you to rebuild your collection
  and you simply save it again).



Full reference
--------------

.. include:: ../ref/modules.rst



Final notes
-----------

If you have loaded modules when you build/install software, remember
to load the same modules when you run the software (also in Slurm
jobs).  You'll learn about running jobs later, but the ``module load``
should usually be put into the job script.

The modules used to compile and run a program become part of its
environment and must always be loaded.

We use the Lmod system and Lmod works by changing environment variables.
Thus, they must be *sourced* by a shell and are only transferred to child processes.
Anything that clears the environment clears the loaded modules too. Module
loading is done by special functions (not scripts) that are
shell-specific and set environment variables.

Triton modules are also available on Aalto Linux: use ``module load
triton-modules`` to make them available.

Some modules are provided by Aalto Science-IT, and on some clusters
they could be provided by others, too.  You could even `make your own
user modules
<https://lmod.readthedocs.io/en/latest/020_advanced.html>`__.



Exercises
---------

Before each exercise, run ``module purge`` to clear all modules.

If you aren't at Aalto, many of these things won't work - you'll have
to check your local documentation for what the equivalents are.

.. exercise:: Modules-1: Basics

   ``module avail`` and check what you see.  Find a software that has
   many different versions available.
   Load the oldest version.

   .. solution::

      Let's use scicomp-python-env as an example. To see all available
      versions of scicomp-python-env, we can either use ``module avail
      scicomp-python-env`` or the better option ``module spider
      scicomp-python-env``. The oldest version of the module is
      ``scicomp-python-env/2024-01``. We can load it using ``module load
      scicomp-python-env/2024-01``.

.. exercise:: Modules-2: Modules and PATH

   ``PATH`` is an environment variable that shows from where programs
   are run.  See it's current value using ``echo $PATH``.

   ``type`` is a command line tool (a shell builtin, so your shell may
   not support it, but ``bash`` and ``zsh`` do) which tells you the
   full path of what will be run for a given command name - basically
   it looks up the command in ``PATH``

   * Run ``echo $PATH`` and ``type python3``.
   * ``module load scicomp-python-env``
   * Re-run ``echo $PATH`` and ``type python3``.  How does it change?

   .. solution::

      Did you remember to reset your modules before starting?  Do this
      before every exercise, even if we don't say it every time.

      ::

        $ module purge

      The initial state should look something like this.  Your PATH is
      most likely longer and doesn't have to look exactly like this::

        $ echo $PATH
         .../usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/ibutils/bin...
        $ type python
        python is /usr/bin/python

      Then we load our module::

        $ module load scicomp-python-env

      Then we look at our final state::

        $ echo $PATH
        /appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/darstr1/bin
        $ type python3
        python3 is /appl/scibuilder-mamba/aalto-rhel9/prod/software/scicomp-python-env/2024-01/f56a564/bin/python3

      We see that ``$PATH`` and ``python3`` have been adjusted.



.. exercise:: Modules-3: Complex module and PATH

   Check the value of ``$PATH``.  Then, load the module ``cmake``.
   List what it loaded.  Check the value of ``PATH`` again.  Why is
   there so much stuff?  Can you find a module command that explains
   it?

   .. solution::

      Running ``module list`` shows you that 11 modules have been
      loaded. All of these are dependencies of ``cmake``, and as such
      were loaded alongside it. You can see dependencies of a module
      using ``module show NAME``. In the case of ``module show cmake``
      you can see that ``cmake`` loads several other modules when it
      is loaded. Some of these models also load their own depedencies.

.. exercise:: Hierarchical modules

   How can you load the module ``quantum-espresso/7.2``::

     $ module load quantum-espresso/7.2
     Lmod has detected the following error:  These module(s) or
     extension(s) exist but cannot be loaded as requested: "quantum-espresso/7.2"
        Try: "module spider quantum-espresso/7.2" to see how to load the module(s).


   .. solution::

      This is a double-hierarchical module, that is built using two
      different toolchains, so you have a choice to make when loading::

        $ module spider quantum-espresso/7.2
        ...
        You will need to load all module(s) on any one of the lines
        below before the "openfoam-org/11" module is available to load.

        openmpi/4.1.6
        scibuilder-spack-dev/2024-01  openmpi/4.1.6

      So here we go, loaded and we use ``which`` to verify one of the
      programs can be found::

         $ module load openmpi/4.1.6 quantum-espresso/7.2
         $ which pw.x
         /appl/scibuilder-spack/aalto-rhel9-dev/2024-01/software/linux-rhel9-haswell/gcc-12.3.0/quantum-espresso-7.2-kmqslxn/bin/pw.x



.. exercise:: Modules-5: Modules and dependencies

   Load a module with many dependencies, such as ``geant4`` and
   save it as a collection.  Purge your modules, and restore the
   collection.

   .. solution::

      Save the collection with ``module save my_env``. After ``module purge``
      you can load your collection again with ``module restore my_env``. Making a
      collection can be particularily useful if you have a job that depends on a large
      number of separate modules, in which case a collection saves you the trouble of
      loading them one by one.



See also
--------

* Lmod documentation https://lmod.readthedocs.io/en/latest/

  * The "User documentation" https://lmod.readthedocs.io/en/latest/010_user.html



What's next?
------------

The next tutorial covers :doc:`data storage <storage>`.
