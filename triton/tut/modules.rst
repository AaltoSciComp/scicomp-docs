================
Software Modules
================

There are hundreds of people using Triton.  They all have different
software needs, including conflicting versions required!  How do we
handle this without making a mess?

The answer is the standard "environment module" system.  It allows us to
have unlimited number of different software packages installed, and the
user can select what they want.  Modules include everything from
compilers (+their required development files), libraries, and programs.
If you need a program installed, we will put it in the module system.

What is a module?
-----------------

Let's look at ``Python/2.7.12-foss-2016.04`` module (abbreviated output
shown):

::

    $ module show Python/3.5.2-foss-2016b

    whatis("Description: Python is a programming language that lets you work more quickly and integrate your systems  more effectively. - Homepage: http://python.org/ ")
    conflict("Python")
    load("foss/2016b")
    ...
    prepend_path("CPATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/include")
    prepend_path("LD_LIBRARY_PATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/lib")
    prepend_path("LIBRARY_PATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/lib")
    prepend_path("MANPATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/share/man")
    prepend_path("PATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/bin")
    prepend_path("PKG_CONFIG_PATH","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/lib/pkgconfig")
    ...
    setenv("EBROOTPYTHON","/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b")
    ...

You can see that it has some meta-info, then adjusts various environment
paths, so that when you run ``python`` it runs the program from
``/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/bin``.

You can search for modules using the command ``module spider``

You can list currently loaded modules using ``module list``.

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
          matlab/r2014a
          matlab/r2015b
          matlab/r2016a
          matlab/r2016b
          matlab/r2017b

We see there are a lot of versions available.


Loading modules
---------------

Normally, you run ``module load MODULE_NAME``. Do it in your open shell,
your scripts, or whatever.  You could put it in your
``~.bash_profile``, but then it will always automatically load it -
perhaps even if you don't expect it.  Watch out for this if you get
un-explainable bugs - it may be best to explicitely load what you
need.  You can load any number of modules, and there is a basic
dependency/conflict system.

Each time you load a module, it resolves all the dependencies.  This
can mean that loading module takes a long time, but there is a
solution: ``module save $collection_name`` and ``module restore
$collection_name``.

Exercise: make a module collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Try loading the ``...`` module.  How long does it take?  Use ``module
list`` to see how many things were actually loaded.::

  module load graph-tool             # 600 seconds!
  module list                        # 72 modules!

Then, do ``module save my-collection``.  Then ``module purge`` to
unload everything.  Now, do ``module restore my-collection``.  Was it
much faster?::

  module save my-gt
  module purge
  module restore my-gt               # only 3 seconds
  module list                        # same 72 modules

You may occasionally need to rebuild your collections if we
re-organize things (it will tell you, just re-save).


Full reference
--------------

.. include:: ../ref/modules.rst

Final notes
-----------

The modules used to compile and run a program become part of its
environment and must always be specified.

If you are compiling things and want it to work in the future, load a
particular version of the module (``module load $name/$version``).
Then, things will keep working even if we upgrade in the meantime (in
fact, this is a primary advantage of modules).

environment-modules use environment variables.  Thus, they must be
**sourced** by a shell and are are only transferred to child processes.
Anything that clears the environment clears loaded modules.  Module
loading is done by special functions (not scripts) that are
shell-specific and set environment variables.

Some modules are provided by Aalto Science-IT, some by CSC.  You could
even make your own user modules if needed.

We use the `Lmod <https://lmod.readthedocs.io/en/latest/>`__ system.


