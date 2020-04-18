================
Software Modules
================

What is a module?
-----------------

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

A module lets you adjust what software is available, 
and makes it easy to switch between different versions. 

As an example, let's inspect the ``gcc`` module (abbreviated output
shown)

.. code-block:: none

    $ module show gcc
    ----------------------------------------------------------------------------------------------
       /share/apps/spack/envs/fgci-centos7-generic/lmod/linux-centos7-x86_64/all/gcc/9.2.0.lua:
    ----------------------------------------------------------------------------------------------
    whatis("Name : gcc")
    whatis("Version : 9.2.0")
    whatis("Short description : The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, and Go, as well as libraries for these languages.")
    whatis("Configure options : --disable-multilib --enable-languages=c,c++,fortran --with-mpfr=/share/apps/spack/envs/fgci-centos7-generic/software/mpfr/3.1.6/m6xmzws --with-gmp=/share/apps/spack/envs/fgci-centos7-generic/software/gmp/6.1.2/mnsg5g2 --enable-lto --with-quad --with-system-zlib --with-mpc=/share/apps/spack/envs/fgci-centos7-generic/software/mpc/1.1.0/uaijipe --with-isl=/share/apps/spack/envs/fgci-centos7-generic/software/isl/0.19/indu5p6")
    help([[The GNU Compiler Collection includes front ends for C, C++, Objective-C,
    Fortran, Ada, and Go, as well as libraries for these languages.]])
    family("compiler")
    prepend_path("PATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/bin")
    prepend_path("MANPATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/share/man")
    prepend_path("LIBRARY_PATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/lib")
    prepend_path("LD_LIBRARY_PATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/lib")
    prepend_path("LIBRARY_PATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/lib64")
    prepend_path("LD_LIBRARY_PATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/lib64")
    prepend_path("CPATH","/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/include")
    ...

The command ``module show gcc`` shows some meta-info (name of the module, its version, etc.)
And then adjusts various environment paths, 
so that when you run ``gcc`` it runs the program from
``/share/apps/spack/envs/fgci-centos7-generic/software/gcc/9.2.0/dnrscms/bin/gcc``.  
This is almost magic: we can have many versions of any software installed, 
and everyone can pick what they want, with no conflicts.

Loading modules
---------------

Let's dive right into an example and load a module.

Let's assume you've written a Python script that is only compatible with Python version 3.7.0 or higher.
You open a shell to find out where and what version our Python is. The
**which** program looks up the current detected version of a program -
very useful when testing modules.::

  $ which python3
  /usr/bin/python3
  $ python3 -V
  Python 3.6.8

But you need a newer version of Python.  To this end, you can **load** the ``anaconda`` module 
using the ``module load anaconda`` command, 
that has a more up to date Python with lots of libraries already included::

  $ module load anaconda
  $ which python
  /share/apps/anaconda-ci/fgci-centos7-generic/software/anaconda/2020-01-tf2/0251cd77/bin/python3
  $ python -V
  Python 3.7.6

As you see, you now have a newer version of Python, in a different directory. 

You can see a list of the all the loaded modules in our working shell using the ``module list`` command::

  $ module list
  Currently Loaded Modules:
    1) anaconda/2020-02-tf2

.. note::
  The ``module load`` and ``module list`` commands can be abbreviated as ``ml``


Let's  use the ``module purge`` command to **unload** all the loaded modules (``anaconda`` in this case)::

  $ module purge

Or explicitly unload the ``anaconda`` module by using the ``module unload anaconda`` command::

  $ module unload anaconda

You can load any number of modules in your open shell,
your scripts, etc.  You could load modules in your
``~/.bash_profile``, but then it will always automatically load it -
perhaps even if you don't expect it.  Watch out for this if you get
un-explainable bugs - it may be best to explicitly load what you
need. 


Exercise: Where is Matlab?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you want to use Matlab.  You log in and try in the shell::

  $ matlab
  -bash: matlab: command not found

So first search for it using the ``module spider`` command::

  $ module spider matlab

  ----------------------------------------------------------------------------
    matlab:
  ----------------------------------------------------------------------------
       Versions:
          matlab/r2012a
          matlab/r2014a
          matlab/r2015b
          matlab/r2016a
          matlab/r2016b
          matlab/r2017b
          matlab/r2018a
          matlab/r2018b
          matlab/r2019a
          matlab/r2019b


We see there are a lot of versions available.

Load the latest version of Matlab as::

  $ module load matlab

It never hurts to double check the version and in fact is recommended. So let's do just that::

  $ module list
  Currently Loaded Modules:
    1) matlab/r2019b


Exercise: Where is R?
^^^^^^^^^^^^^^^^^^^^^^^^^^
If you don't specify the version - just as the above Matlab example - the default version of the module is usually loaded, whichis usually the latest version. 
The default version, however,is not always latest version.  To see an example, let's see what versions of R are available::

  $ module spider r

  ----------------------------------------------------------------------------
    r:
  ----------------------------------------------------------------------------
       Versions:
          r/3.4.3-python-2.7.14
          r/3.4.3-python2
          r/3.4.3-python3
          r/3.5.0-python-2.7.14
          r/3.5.0-python2
          r/3.5.3-python-2.7.14
          r/3.6.1-python3

Let's try loading the default version::

  $ module load r

You can list all the dependencies the R module requires and loads::

  $ module list
  Currently Loaded Modules:
    1) pcre/8.42        12) libpthread-stubs/0.4  23) libxml2/2.9.9        34) jdk/8u181-b13          45) libice/1.0.9
    2) ncurses/6.1      13) xproto/7.0.31         24) font-util/1.3.2      35) fontconfig/2.12.3      46) libx11/1.6.7
    3) zlib/1.2.11      14) libxau/1.0.8          25) libxft/2.3.2         36) pixman/0.34.0          47) libsm/1.2.2
    4) readline/7.0     15) libxcb/1.13           26) tk/8.6.8             37) cairo/1.14.12-python2  48) libxt/1.1.5
    5) sqlite/3.23.1    16) libxext/1.3.3         27) python/2.7.15        38) libjpeg-turbo/1.5.90   49) harfbuzz/1.4.6-python2
    6) openssl/1.0.2k   17) libxscrnsaver/1.2.2   28) tar/1.31             39) libtiff/4.0.9          50) gobject-introspection/1.49.2-python2
    7) tcl/8.6.8        18) libpng/1.6.34         29) gettext/0.19.8.1     40) bzip2/1.0.6            51) pango/1.41.0-python2
    8) kbproto/1.0.7    19) renderproto/0.11.1    30) gdbm/1.18.1          41) freetype/2.7.1         52) openblas/0.3.2
    9) xextproto/7.3.0  20) libxrender/0.9.10     31) perl/5.26.2          42) libssh2/1.8.0          53) r/3.4.3-python2
   10) libbsd/0.9.1     21) libiconv/1.15         32) libffi/3.2.1         43) curl/7.60.0
   11) libxdmcp/1.1.2   22) xz/5.2.4              33) glib/2.56.1-python2  44) icu4c/60.1

The last loaded module clearly shows that the version of the R loaded is ``r/3.4.3-python2``.
To load the latest version of R, use the *fullName* of the module::

  $ module load r/3.6.1-python3

.. note::

  We upgrade the modules from time to time and so the default version may change. 
  Thus, it is always a good idea to load a particular version of the modules 
  when compiling and subsequently for all your future runs.
  

What's going on under the hood here?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Linux systems, different environment variables like ``$PATH`` and
``$LD_LIBRARY_PATH`` help figure out how to run programs.  Modules just
cleverly manipulate these so that you can find the software you need,
even if there are multiple versions available.  You can see these variables
with the **echo** command, e.g. ``echo $PATH``.

When you load a module in a shell, the module command changes the current shell's environment variables,
and the environment variables are passed on to all the child processes. 

Making a module collection
--------------------------

There is a basic dependency/conflict system to handle module dependency.
Each time you load a module, it resolves all the dependencies.  This
can mean that loading module takes a long time, but there is a
solution: ``module save $collection_name`` and ``module restore
$collection_name``

Let's see how to do this in an example.

Try loading the ``graph-tool`` module. How long does it take?  Use ``module
list`` to see how many things were actually loaded::

  $ module load graph-tool             # 600 seconds!
  $ module list                        # 72 modules!

Then, do ``module save my-collection``.  Then ``module purge`` to
unload everything.  Now, do ``module restore my-collection``::

  $ module save my-gt
  $ module purge
  $ module restore my-gt               # only 3 seconds
  $ module list                        # same 72 modules

Was it much faster?

Generally, it is a good idea to save your modules 
as a collection to have your desired modules
all set up each time you want to re-compile/re-build::

  $ module anaconda/2020-02-tf2 gcc/9.2.0
  $ module save my-modules

So the subsequent times that you want to compile/build,
you simply ``module restore my-modules`` and this way
you can be sure you have the same previous environment.

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

If you are compiling things and want them to work in the future, load a
particular version of the module (``module load $name/$version``)
Then, things will keep working even if we upgrade in the meantime (in
fact, this is a primary advantage of modules)

We use the Lmod system and Lmod works by changing environment variables.  
Thus, they must be *sourced* by a shell and are only transferred to child processes.
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
   a  module such as ``py-gpaw``.  List what
   it loaded.  Check the value of ``PATH`` again.  Why is there so
   much stuff?

3. (Advanced) Same as number 2, but use ``env | sort >
   filename`` to store environment variables, then swap to
   ``py-gpaw/1.3.0-openmpi-scalapack-python3``.  Do the same, and compare the two outputs
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

The next tutorial covers :doc:`data storage <storage>`.
