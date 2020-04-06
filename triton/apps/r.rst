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

As any packages you install against R are specific to the version you
installed them with, it is best to pick a version of R and stick with it.
You can do this by checking the R version with ``module spider r`` and
using the whole name when loading the module::

  module load r/3.6.1-python3

If you want to detect the number of cores, you should use the proper
Slurm environment variables (defaulting to all cores)::

  library(parallel)
  as.integer(Sys.getenv('SLURM_CPUS_PER_TASK', parallel::detectCores()))


Installing packages
~~~~~~~~~~~~~~~~~~~

There are two ways to install packages.

#. You can usually install packages yourself, which allows you to keep
   up to date and reinstall as needed. Good instructions can be
   found
   `here <https://statistics.berkeley.edu/computing/R-packages>`__, for
   example::

     R
     > install.packages('L1pack')

   This should guide you to selecting a download mirror and offer you
   the option to install in your home directory.

   If you have a lot of packages, you can run out of home quota. In this
   case you should move your package directory to your work directory and
   replace it the ``~/R``-directory with a symlink that points to your
   ``$WRKDIR/R``.

   Example of doing this is here:

   ::

       mv ~/R $WRKDIR/R
       ln -s $WRKDIR/R ~/R

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
