======
Octave
======

From Octave's `web page <https://www.gnu.org/software/octave/about.html>`_:
    GNU Octave is a high-level language, primarily intended for numerical computations. It provides a convenient command line interface for solving linear and nonlinear problems numerically, and for performing other numerical experiments using a language that is mostly compatible with Matlab. It may also be used as a batch-oriented language.

    Octave has extensive tools for solving common numerical linear algebra problems, finding the roots of nonlinear equations, integrating ordinary functions, manipulating polynomials, and integrating ordinary differential and differential-algebraic equations. It is easily extensible and customizable via user-defined functions written in Octave’s own language, or using dynamically loaded modules written in C++, C, Fortran, or other languages.

Getting started
~~~~~~~~~~~~~~~

Simply load the latest version of Octave.

::

    module load octave
    octave

It is best to pick a version of octave and stick with it.  Do ``module
spider octave`` and use the whole name::

    module load octave/4.4.1-qt-python2

To run octave with the GUI, run it with::

    octave --force-gui

Installing packages
~~~~~~~~~~~~~~~~~~~

Before installing packages you should create a file ``~/.octaverc`` with the 
following content::

    package_dir = ['/scratch/work/',getenv('USER'),'/octave'];
    eval (["pkg prefix ",package_dir, ";"]);
    setenv("CXX","g++ -std=gnu++11")
    setenv("DL_LD","g++ -std=gnu++11")
    setenv("LD_CXX","g++ -std=gnu++11")
    setenv("CC","gcc")
    setenv("F77","gfortran")

This sets up ``/scratch/work/$USER/octave`` to be your Octave package directory
and sets ``gcc`` to be your compiler. By setting Octave package directory to
your work directory you won't run into any quota issues.

After this you should load ``gcc``\ - and ``texinfo``\ -modules. This gives you an 
up-to-date compiler and tools that Octave uses for its documentation::

    module load gcc
    module load texinfo

Now you can install packages in octave with e.g.::

    pkg install -forge -local io

After this you can unload the ``gcc``\ - and ``texinfo``\ -modules::

    module unload gcc
    module unload texinfo

