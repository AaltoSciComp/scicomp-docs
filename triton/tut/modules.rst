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
paths, so that when you run "python" it runs the program from
"/cvmfs/fgi.csc.fi/apps/el7/Python/3.5.2-foss-2016b/bin".

Loading modules
---------------

Normally, you run ``module load MODULE_NAME``. Do it in your open shell,
your program scripts, or whatever.  You could put it in your
~.bash\_profile, but then realize that it will always be there, even if
you don't expect it.  Watch out for this if unexpected things start
happening.  You can load any number of modules, and there is a basic
dependency/conflict system, but you can still probably make problems if
you do something really convoluted.

Listing and getting info
------------------------

.. include:: ../ref/modules.rst

Final notes
-----------

The modules used to compile and run a program become part of its
environment and must always be specified.

environment-modules use environment variables.  Thus, they must be
**sourced** by a shell and are are only transferred to child processes.
Anything that clears the environment clears loaded modules.  Module
loading is done by special functions (not scripts) that are
shell-specific and set environment variables.

Some modules are provided by Aalto Science-IT, some by CSC.  You could
even make your own user modules if needed...


