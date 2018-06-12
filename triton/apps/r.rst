=
R
=


R is a language and environment for statistical computing and graphics
with wide userbase. There exists several packages that are easily
imported to R.

Getting started
~~~~~~~~~~~~~~~

Simply load the latest R.

::

    module load r
    R

It is best to pick a version of R and stick with it.  Do ``module
spider r`` and use the whole name::

  module load r/3.4.3-python-2.7.14


Installing packages
~~~~~~~~~~~~~~~~~~~

There are two ways to install packages.

#. You can usually install packages yourself, which allows you to keep
   up to date and reinstall as needed. Good instructions can be
   found
   `here <http://statistics.berkeley.edu/computing/R-packages>`__, for
   example::

     R
     > install.packages('L1pack')

   This should guide you to selecting a download mirror and offer you
   the option to install in your home directory.

   Before installing packages you should set a package location,
   because the default location of the home directory can quickly fill
   up and loading them from the home directory is very slow.
   Example of doing this is here:

   ::

       module load R
       export R_LIBS=$WRKDIR/R/$EBVERSIONR
       mkdir -p $R_LIBS

   Afterwards setting

   ::

       export R_LIBS=$WRKDIR/R/$EBVERSIONR

   after loading R module will point R to the correct library location
   (you can put this in your ``.bashrc`` file).
   More info on R library paths can be
   found `here <https://stat.ethz.ch/R-manual/R-devel/library/base/html/libPaths.html>`__.
   Looking at
   R `startup <https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html>`__
   can also be informative.

#. You can also put a request to the triton issue tracker and
   mention which R-version you are using.


Simple R serial job
~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r/r_serial.rst

Simple R job using OpenMP for parallelization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r/r_openmp.rst

Simple R parallel job using 'parallel'-package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r/r_parallel.rst
