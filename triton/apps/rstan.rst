RStan
=====

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

:supportlevel: B
:pagelastupdated: 2018-07-26
:maintainer:

RStan is an R interface to Stan.  Stan is a platform for modeling.


Basic installation
------------------

RStan is installed as an R package and there is nothing too special
about it.

First, load the R module you need to use.  There are different
options, using different compilers.  Do **not** use an ``iomkl`` R
version, because it requires the intel compilers to work on the nodes
to compile every time you run, and they aren't available there.  If
you load a ``goolf`` R version, it will work (you could work around
this by pre-compiling models, if you wanted)::

  $ module spider R
  ...
  R/3.4.1-goolf-triton-2017a
  R/3.4.1-iomkl-triton-2017a

  $ module load R/3.4.1-goolf-triton-2017a

If you change R versions (from intel to gcc) or get errors about
loading libraries, you may have installed incompatible libraries.
Removing your ``~/R`` directory and reinstalling all of your libraries
is a good first place to start.

Notes
-----

You should detect the number of cores with::

  as.integer(Sys.getenv('SLURM_JOB_CPUS_PER_NODE', parallel::detectCores()))

Common Rstan problems
---------------------

* Models must be compiled on the machine that is running them, Triton
  or other workstations.  The compiled model files aren't necessarily
  portable, since they depend on the libraries available when build.
  One symptom of this problem is error messages which talk about
  loading libraries and ``GLIBC_2.23`` or some such.

* In order to compile models, you must have the compiler available on
  the nodes.  Thus, the Intel compilers (``iomkl``) won't work.  It
  also won't work if the Intel compiler license servers are down.
  Using the GNU compiler toolchains are more reliable.


Example
-------
