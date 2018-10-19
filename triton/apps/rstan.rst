RStan
=====

:supportlevel: B
:pagelastupdated: 2018-07-26
:maintainer:

RStan is an R interface to Stan.  Stan is a platform for modeling.


Basic installation
------------------

RStan is installed as an R package and there is nothing too special
about it.

First, load the R module you need to use.  There are different
options, using different compilers.  If you get an Intel compiler
license error, try using one of the ``gcc``-based modules.

If you change R versions (from intel to gcc) or get errors about
loading libraries, removing your ``~/R`` directory and reinstalling
everything is the first place to start.

Notes
-----

You should detect the number of cores with::

  as.integer(Sys.getenv('SLURM_JOB_CPUS_PER_NODE', parallel::detectCores()))





Example
-------
