================
Software Modules
================

There are hundreds of people using Triton.  They all have different
software needs, including conflicting versions required!  How do we
handle this without making a mess?

The answer is the standard "module" system `Lmod <https://lmod.readthedocs.io/en/latest/>`__.
It allows us to
have unlimited number of different software packages installed, and the
user can select what they want.  Modules include everything from
compilers (+their required development files), libraries, and programs.
If you need a program installed, we will put it in the module system.

In a system the size of Triton, it just isn't possible to install all
software by default for every user.

The summary
-----------

A module lets you adjust what software is available.  For example,
let's see what our Python is::

  $ which python3
  /usr/bin/python3
  $ python3 -V
  Python 3.4.9

Now let's load the ``anaconda`` module, a more up to date Python with a
lot of libraries already included::

  $ module load anaconda
  $ which python3
  /share/apps/anaconda-ci/fgci-centos7-generic/software/anaconda/2020-01-tf2/0251cd77/bin/python3
  $ python3 -V
  Python 3.7.6

As you see, we have a newer Python.  Let's go back to blank::

  $ module purge



What is a module?
-----------------

Let's look at ``py-gpaw`` module (abbreviated output
shown):

.. code-block:: none

    $ module show py-gpaw
    ------------------------------------------------------------------------------------------------------------------
       /share/apps/spack/modules/linux-centos7-x86_64/Core/py-gpaw/1.3.0-openmpi-scalapack-python3.lua:
    ------------------------------------------------------------------------------------------------------------------
    whatis("Name : py-gpaw")
    whatis("Version : 1.3.0")
    whatis("Short description : GPAW is a density-functional theory (DFT) Python code based on the projector-augmented wave (PAW) method and the atomic simulation environment (ASE).")
    help([[GPAW is a density-functional theory (DFT) Python code based on the
    projector-augmented wave (PAW) method and the atomic simulation
    environment (ASE).]])
    load("py-scipy/1.1.0-python3")
    load("libxc/3.0.0")
    load("python/3.6.3")
    load("fftw/3.3.8-openmpi")
    load("py-ase/3.15.0-python3")
    load("py-numpy/1.14.3-python3")
    load("netlib-scalapack/2.0.2-openmpi")
    load("openmpi/2.1.5")
    load("openblas/0.3.2")
    prepend_path("PATH","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/bin")
    prepend_path("LIBRARY_PATH","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/lib")
    prepend_path("LD_LIBRARY_PATH","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/lib")
    prepend_path("CMAKE_PREFIX_PATH","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/")
    prepend_path("PYTHONPATH","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/lib/python3.6/site-packages")
    prepend_path("CPATH","/share/apps/spack/software/libxml2/2.9.8/f4u6mya/include/libxml2")
    setenv("PY_GPAW_ROOT","/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i")


You can see that it has some meta-info, then adjusts various environment
paths, so that when you run ``gpaw`` it runs the program from
``/share/apps/spack/software/py-gpaw/1.3.0/vmhtg6i/bin``.  This is
almost magic: we can have many versions of any software installed, and
everyone can pick what they want, with no conflicts.

You can search for modules using the command ``module spider``.

You can list currently loaded modules using ``module list``.

What's going on under the hood here?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Linux systems, different environment variables like ``$PATH`` and
``$LD_LIBRARY_PATH`` help figure out how to run programs.  Modules just
cleverly manipulate these so that you can find the software you need,
even if there are multiple versions available.

Exercise: where is Matlab?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you want to use Matlab.  You log in and try::

  $ matlab
  -bash: matlab: command not found

So first search for it::

  module spider matlab

  ----------------------------------------------------------------------------
    matlab:
  ----------------------------------------------------------------------------
       Versions:
          ...
          matlab/r2016a
          matlab/r2016b
          matlab/r2017b
          matlab/r2018a
          matlab/r2018b
          matlab/r2019a


We see there are a lot of versions available.

Load the latest version of Matlab as::

  module load matlab

Run it to check the version you got, then close it and swap the version with an older one.


Loading modules
---------------

Normally, you run ``module load MODULE_NAME``. Do it in your open shell,
your scripts, etc.  You could put it in your
``~/.bash_profile``, but then it will always automatically load it -
perhaps even if you don't expect it.  Watch out for this if you get
un-explainable bugs - it may be best to explicitely load what you
need.  You can load any number of modules, and there is a basic
dependency/conflict system.

Each time you load a module, it resolves all the dependencies.  This
can mean that loading module takes a long time, but there is a
solution: ``module save $collection_name`` and ``module restore
$collection_name``

Exercise: make a module collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Try loading the ``graph-tool`` module. How long does it take?  Use ``module
list`` to see how many things were actually loaded::

  module load graph-tool             # 600 seconds!
  module list                        # 72 modules!

Then, do ``module save my-collection``.  Then ``module purge`` to
unload everything.  Now, do ``module restore my-collection``::

  module save my-gt
  module purge
  module restore my-gt               # only 3 seconds
  module list                        # same 72 modules

Was it much faster?

You may occasionally need to rebuild your collections if we
re-organize things (it will tell you, just re-save).


Full reference
--------------

.. include:: ../ref/modules.rst



But what about *the software*?
------------------------------

You know how to load modules software now, but what about specific software
packages?  See the upcoming :doc:`Applications 
<applications>` tutorial for more info.


Final notes
-----------

If you have loaded modules when you build/install software, remember
to load the same modules when you run the software (also in Slurm
jobs).  You'll learn about running jobs later, but the ``module load``
should usually be put into the job script.

The modules used to compile and run a program become part of its
environment and must always be loaded.

If you are compiling things and want them to work in the future, load a
particular version of the module (``module load $name/$version``)
Then, things will keep working even if we upgrade in the meantime (in
fact, this is a primary advantage of modules)

We use the `Lmod <https://lmod.readthedocs.io/en/latest/>`__ system.

Lmod uses environment variables.  Thus, they must be
**sourced** by a shell and are only transferred to child processes.
Anything that clears the environment clears the loaded modules too. Module
loading is done by special functions (not scripts) that are
shell-specific and set environment variables.

Some modules are provided by Aalto Science-IT, some by CSC.  You could
even make your own user modules if needed.



Exercises
---------

Before each exercise, ``module purge`` to clear all modules.

1. ``module avail`` and check what you see.  Find a software that has 
   many different versions available.  
   Load the oldest version. 

2. ``PATH`` is an environment variable that shows from where programs
   are run.  See it's current value using ``echo $PATH``.  Then, load
   some toolchain module such as ``goolfc/triton-2017a``  List what
   it loaded.  Check the value of ``PATH`` again.  Why is there so
   much stuff?

3. (Advanced) Same as number 2, but use ``env | sort >
   filename`` to store environment variables, then swap to
   ``goolfc/triton-2016a``.  Do the same, and compare the two outputs
   using ``diff``

4. Load a module with many dependencies, such as
   ``R/3.3.2-iomkl-triton-2017a-libX11-1.6.3`` and save it as a
   collection.  Compare the time needed to load the module and the
   collection.  (Does ``time`` not work?  Change your shell to bash,
   see the previous tutorial)

5. (Advanced) Load GROMACS.  Use ``which`` to find where command ``gmx`` is
   and then use ``ldd`` to find out what libraries it uses. Load
   incompatible toolchain e.g. goolf. Check ``ldd`` output again.


What's next?
------------

Next, move on to the :doc:`Applications <applications>` tutorial.
