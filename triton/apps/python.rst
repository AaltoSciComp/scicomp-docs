======
Python
======

Python is widely used programming language where we have installed all
basic packages on every node. Yet, python develops quite fast and the
system provided packages are ofter not complete or getting old.

Python distributions
--------------------

+--------------------------+--------------------------+--------------------------+
|                          | Python to use            | How to install own       |
|                          |                          | packages                 |
+==========================+==========================+==========================+
| Most of the use cases,   | Anaconda 2/3             | conda environment +      |
| but sometimes different  |                          | conda                    |
| versions of modules      |                          |                          |
| needed                   |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Simple programs with     | Anaconda 2/3             | ``pip install --user``   |
| common packages, not     |                          |                          |
| switching between        |                          |                          |
| Pythons often            |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Special advanced cases.  | Python from module       | virtualenv + pip install |
|                          | system                   |                          |
+--------------------------+--------------------------+--------------------------+

There are two main versions of Python: 2 and 3. There are also different
distributions: The "regular" CPython, Anaconda (a package containing
CPython + a lot of other scientific software all bundled togeter), PyPy
(a just-in-time compiler, which can be much faster for some use cases).
Triton supports all of these.

-  For general scientific/data science use, we suggest that you use
   Anaconda. It comes with the most common scientific software included,
   and is reasonably optimized.
-  There are many other "regular" CPython versions in the module system.
   These are compiled and optimized for Triton, and are highly
   recommended.  The default system Python is old and won't be updated.
-  PyPy is still mainly for advanced use (it can be faster under certain
   cases, but does not work everywhere). It is available in a module.

Quickstart
----------

Use ``module load anaconda2`` or ``module load anaconda3`` to get a
modern Python.

If you have simple needs, use :ref:`pip install --user
<pip-install-user>` to install packages.  For complex needs, use
:ref:`anaconda + conda environments <conda>` to isolate your
projects.



.. _pip-install-user:

Install your own packages easily
--------------------------------

Installing your own packages with ``pip install`` won't work, since it
tries to install globally for all users. Instead, you should do this
(add ``-user``) to install the package in your home directory
(``~/.local/lib/pythonN.N/``)::

  pip install --user $package_name

This is quick and effective best used for leaf packages without many
dependencies and if you don't switch Python modules often.

**Warning!** If you do this, then the module will be shared among all
your projects. It is quite likely that eventually, you will get some
incompatibilities between the Python you are using and the modules
installed. In that case, you are on your own (simple recommendation is
to remove all modules from ``~/.local/lib/pythonN.N`` and reinstall). **If
you get incompatible module errors, our first recommendation will be to
remove everything installed this way and use conda/virtual
environments instead.**  It's not a bad idea to do this when you
switch to environments anyway.

Note: ``pip`` installs from the `Python Package Index
<https://pypi.python.org/pypi>`__.



.. _conda:

Anaconda and conda environments
-------------------------------

`Anaconda <https://www.continuum.io>`__ is a Python distribution by
Continuum Analytics. It is nothing fancy, they just take a lot of
useful scientific packages and put them all together, make sure they
work, and do some sort of optimization. They also include most of the
most common computing and data science packages. It is also all open
source, and is packaged nicely so that it can easily be installed on
any major OS.

To load anaconda, use the module system (you can also load specific
versions):

::

    module load anaconda2    # python2
    module load anaconda3    # python3

Conda environments
~~~~~~~~~~~~~~~~~~

**virtualenv** does not work with Anaconda, use ``conda`` instead.

A conda environment lets you install all your own packages. Your home
directories are very small, so it requires some initial steps. You see
``module load teflon`` here a lot: conda does bad things with permissions,
thus messing up quota accounting. This prevents that.

-  Initial setup: link the conda cache to your work directory (an
   rsync error because ``~/.conda`` doesn't exist is OK)::

       # Move your package cache to your work directory.  The following does it automatically.
       rsync -lrt ~/.conda/ $WRKDIR/conda/ && rm -r ~/.conda
       ln -sT $WRKDIR/conda ~/.conda
       quotafix -gs --fix $WRKDIR/conda

-  Load the anaconda version you want to use. You will need to always
   load same version each time you source the environment::

       # Load anaconda first.  This must always be done before activating the env!
       module load anaconda2     # or anaconda3

-  Create an environment::

       # create environment with package pip in it
       module load teflon
       conda create --prefix PATH/TO/DIR python pip ipython ...
       module unload teflon

-  Activating and using the environment, installing more packages,
   etc. can be done either using ``conda install`` or ``pip install``::

       # This must be run in each shell to set up the environment variables properly.
       # make sure module is loaded first.
       source activate PATH/TO/DIR

       # Install more packages, either conda or pip
       module load teflon
       conda search PACKAGE_NAME
       conda install PACKAGE_NAME
       pip install PACKAGE_NAME
       module unload teflon

-  Leaving the environment when done (optional)::

       # Deactivate the environment
       source deactivate

-  If you run into "quota exceeded" problems, you need to do the first
   steps above which move the .conda directory to another folder. The
   quotafix command may be useful to try to reset things (see above),
   but if that doesn't work: in the worst case, remove everything and
   recreate it.::

       # remove all conda things
       rm -r ~/.conda $WRKDIR/conda
       # Remove anything installed with pip install --user.
       rm -r ~/.local/lib/python*.*/

-  Worst case, you have incompatibility problems. Remove everything,
   including the stuff installed with ``pip install --user``. If you've
   mixed your personal stuff in with this, then you will have to
   separate it out.::

       # Remove anything installed with pip install --user.
       rm -r ~/.local/lib/python*.*/

A few notes about conda environments:

-  Once you use a conda environment, everything goes into it. Don't mix
   versions with, for example, local packages in your home dir and
   ``--pip install --user``.  Things installed (even previously) with
   ``pip install --user`` will be visible in the conda environment and
   can make your life hard!
   Eventually you'll get dependency problems.
-  Often the same goes for other python based modules. We have setup
   many modules that do use anaconda as a backend. So, if you know what
   you are doing this might work.
-  The commands below will fail:

   -  ``conda create -n foo pip`` # tries to use the global dir, use the
      ``--prefix`` instead

   -  ``conda create --prefix $WRKDIR/foo --clone root`` # will fail as our
      anaconda module has additional packages (e.g. via pip) installed.



.. _virtualenv:

Python: virtualenv
------------------

Virtualenv is default-Python way of making environments, but does
**not** work with Anaconda.  We generally recommend using anaconda,
since it includes a lot more stuff by default, but ``virtualenv``
works on other systems easily so it's good to know about.

::

    # Create environment
    virtualenv DIR

    # activate it (in each shell that uses it)
    source DIR/bin/activate

    # install more things (e.g. ipython, etc.)
    pip install PACKAGE_NAME

    # deactivate the virtualenv
    deactivate



Python optimized for Triton
---------------------------

There are Python modules installed with the typical software setup
against :doc:`EasyBuild toolchains <../apps/index>`. While some of the
more general packages available with anaconda installation might be
missing, the Numpy and Scipy installations on these modules are highly
optimized against the installed linear algebra libraries. A typical
module loading using these toolchains could be

::

    module load Python/2.7.11-goolf-triton-2016a
    module load numpy/1.11.1-goolf-triton-2016a-Python-2.7.11
    module load scipy/0.18.0-goolf-triton-2016a-Python-2.7.11

Use ``module spider Python`` to see available modules. More specialized
modules like Tensorflow, Theano etc. will be installed against these
modules so that they can be in optimal settings. Submit your issue in
tracker if you wish some other Python modules to be included in these
installations.



Background: ``pip`` vs ``python`` vs ``anaconda`` vs ``conda`` vs ``virtualenv``
--------------------------------------------------------------------------------

Virtual environments are self-contained python environments with
all of their own modules, separate from the system packages.  They are
great for research where you need to be agile and install whatever
versions and packages you need.  **We highly recommend virtual
environments or conda environments (below)**

   -  Anaconda: use conda, see below
   -  Normal Python: virtualenv + pip install, see below

You often need to install your own packages. Python has its own package
manager system that can do this for you. There are three important
related concepts:

-  pip: the Python package installer. Installs Python packages globally,
   in a user's directory (``--user``), or anywhere. Installs from the
   `Python Package Index <https://pypi.python.org/pypi>`__.
-  virtualenv: Creates a directory that has all self-contained packages
   that is manageable by the user themself. When the virtualenv is
   activated, all the operating-system global packages are no longer
   used. Instead, you install only the packages you want. This is
   important if you need to install specific versions of software, and
   also provides isolation from the rest of the system (so that you work
   can be uninterrupted). It also allows different projects to have
   different versions of things installed. virtualenv isn't magic, it
   could *almost* be seen as just manipulating ``PYTHONPATH``, ``PATH``, and the
   like. Docs: http://docs.python-guide.org/en/latest/dev/virtualenvs/
-  conda: Sort of a combination of package manager and virtual
   environment. However, it *only* installed packages into environments,
   and is *not* limited to Python packages. It can also install other
   libraries (c, fortran, etc) into the environment. This is extremely
   useful for scientific computing, and the reason it was created. Docs
   for envs: http://conda.pydata.org/docs/using/envs.html.

So, to install packages, there is ``pip`` and ``conda``. To make virtual
environments, there is ``venv`` and ``conda``.

Advanced users can see this `rosetta
stone <http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html>`__
for reference.

On Triton we have added some packages on top of the Anaconda
installation, so cloning the entire Anaconda environment to local conda
environment will not work (not a good idea in the first place but some
users try this every now and then).



Examples
--------

Running Python with internal parallelization (OpenMP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A simple parallel Python script using OpenMP. Both anaconda modules and
optimized Python modules support OpenMP, but optimized versions are
faster.

.. include:: ../examples/python_openmp.rst


Running MPI parallelized Python with mpi4py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MPI parallelized Python requires a valid MPI installation that support
our SLURM scheduler. Thus anaconda is not the best option. We have
installed MPI-supporting Python versions to different toolchains.

Using mpi4py is quite easy. Example is provided below.

.. include:: ../examples/python/mpi4py/mpi4py.rst
