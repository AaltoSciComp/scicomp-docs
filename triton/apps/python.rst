======
Python
======

Python is widely used programming language where we have installed all
basic packages on every node. Yet, python develops quite fast and the
system provided packages are ofter not complete or getting old.

Python distributions
--------------------

+----------------------+-------------------------------+------------------------+
|                      | Python to use                 | How to install own     |
|                      |                               | packages               |
+======================+===============================+========================+
| I don't really care, | Anaconda                      |                        |
| I just want recent   | ``module load anaconda``      |                        |
| stuff and to not     |                               |                        |
| worry.               |                               |                        |
+----------------------+-------------------------------+------------------------+
| Simple programs with | Anaconda                      | ``pip install --user`` |
| common packages, not | ``module load anaconda``      |                        |
| switching between    |                               |                        |
| Pythons often        |                               |                        |
+----------------------+-------------------------------+------------------------+
| Your own conda       | Miniconda                     | conda environment +    |
| environment          | ``module load miniconda``     | conda                  |
|                      |                               |                        |
|                      |                               |                        |
+----------------------+-------------------------------+------------------------+
| Your own virtual     | Module virtualenv             | virtualenv + pip +     |
| environment          | ``module load py-virtualenv`` | setuptools             |
|                      |                               |                        |
|                      |                               |                        |
+----------------------+-------------------------------+------------------------+

The main version of modern Python is 3. Support for old Python 2 ended at the
end of 2019. There are also different distributions: The "regular" CPython,
Anaconda (a package containing CPython + a lot of other scientific software all
bundled togeter), PyPy (a just-in-time compiler,  which can be much faster for
some use cases). Triton supports all of these.

-  For general scientific/data science use, we suggest that you use
   Anaconda. It comes with the most common scientific software included,
   and is reasonably optimized.
-  There are many other "regular" CPython versions in the module system.
   These are compiled and optimized for Triton, and are highly
   recommended.  The default system Python is old and won't be updated.

Make sure your environments are **reproducible** - you can recreate
them from scratch.  History shows you will probably have to do this
eventually, and it also ensures that others can always use your code.
We recommend a minimal ``requirements.txt`` (pip) or
``environment.yml`` (conda), hand-created with the minimal
dependencies in there.

Quickstart
----------

Use ``module load anaconda`` (or ``module load anaconda2`` for Python 2) to get a
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
(add ``--user``) to install the package in your home directory
(``~/.local/lib/pythonN.N/``)::

  pip install --user $package_name

This is quick and effective best used for leaf packages without many
dependencies and if you don't switch Python modules often.

.. warning:: ``pip install --user`` can result in incompatibilities

   If you do this, then the module will be shared among all
   your projects. It is quite likely that eventually, you will get some
   incompatibilities between the Python you are using and the modules
   installed. In that case, you are on your own (simple recommendation is
   to remove all modules from ``~/.local/lib/pythonN.N`` and reinstall). **If
   you get incompatible module errors, our first recommendation will be to
   remove everything installed this way and use conda/virtual
   environments instead.**  It's not a bad idea to do this when you
   switch to environments anyway.

   If you encounter problems, remove all your user packages::

      rm -r ~/.local/lib/python*.*/

   and reinstall everything *after* loading the environment you want.

.. note:: Example of dangers of ``pip install --user``

   Someone did ``pip install --user tensorflow``.  Some time later,
   they noticed that they couldn't use Tensorflow + GPUs.  We couldn't
   reproduce the problem, but in the end found they had this local
   install that was hiding any Tensorflow in any module (forcing a CPU
   version on them).

Note: ``pip`` installs from the `Python Package Index
<https://pypi.org/>`__.

.. _conda:

Anaconda and conda environments
-------------------------------

`Anaconda <https://www.anaconda.com>`__ is a Python distribution by
Continuum Analytics (open source, of course). It is nothing fancy,
they just take a lot of useful scientific packages and their dependencies
and put them all together, make sure they work, and do some optimization.
They also include most of the most common computing and data science packages
and non-Python compiled software and libraries. It is also all open
source, and is packaged nicely so that it can easily be installed on
any major OS.

To load anaconda, use the module system (you can also load specific
versions):

::

    module load anaconda     # python3
    module load anaconda2    # python2

.. note::

   Before 2020, Python3 was via the ``anaconda3`` module (note the
   ``3`` on the end).  That's still there, but in 2020 we completely
   revised our Anaconda installation system, and dropped active
   maintenance of Python 2.  All updates are in ``anaconda`` only in
   the future.

Conda environments
~~~~~~~~~~~~~~~~~~

If you encounter a situation where you need to create your own environment,
we recommend that you use conda environments. When you create your own
environment the packages from the base environment (default environment
installed by us) will not be used, but you can choose which packages you want
to install.

We nowadays recommend that you use the ``miniconda``-module for installing these
environments. Miniconda is basically a minimal Anaconda installation that can be used to
create your own environments.

Do note that these environments can be quite big and if you have multiple
environments installed you can run into quota issues in your ``/home``. If
you encounter such issues do contact us. In the past we recommended installing
conda environments under ``$WRKDIR``, but this can cause file system problems
when launching array jobs and is thus no longer recommended.

**virtualenv** does not work with Anaconda, use ``conda`` instead.

-  Load the miniconda module. You should look up the version and use
   load same version each time you source the environment::

       # Load miniconda first.  This must always be done before activating the env!
       module load miniconda

-  Create an environment. This needs to be done once::

       # create environment with the packages you require
       conda create -n ENV_NAME python pip ipython tensorflow-gpu pandas ...

-  Activate the environment. This needs to be done every time you load
   the environment::

       # This must be run in each shell to set up the environment variables properly.
       # make sure module is loaded first.
       source activate ENV_NAME

-  Activating and using the environment, installing more packages,
   etc. can be done either using ``conda install`` or ``pip install``::

       # Install more packages, either conda or pip
       conda search PACKAGE_NAME
       conda install PACKAGE_NAME
       pip install PACKAGE_NAME

-  Leaving the environment when done (optional)::

       # Deactivate the environment
       source deactivate

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

.. _virtualenv:

Python: virtualenv
------------------

Virtualenv is default-Python way of making environments, but does
**not** work with Anaconda.  We generally recommend using anaconda,
since it includes a lot more stuff by default, but ``virtualenv``
works on other systems easily so it's good to know about.

::

    # Load module python
    module load py-virtualenv

    # Create environment
    virtualenv DIR

    # activate it (in each shell that uses it)
    source DIR/bin/activate

    # install more things (e.g. ipython, etc.)
    pip install PACKAGE_NAME

    # deactivate the virtualenv
    deactivate

.. _python-ipyparallel:

IPython Parallel
----------------

`ipyparallel <https://ipyparallel.readthedocs.io/en/latest/>`__ is a
tool for running embarrassingly parallel code using Python.   The
basic idea is that you have a *controller* and *engines*.  You have a
*client* process which is actually running your own code.

Preliminary notes: ipyparallel is installed in the
anaconda{2,3}/latest modules.

Let's say that you are doing some basic interactive work:

* Controller: this can run on the frontend node, or you can put it on
  a script.  To start: ``ipcontroller --ip="*"``
* Engines: ``srun -N4 ipengine``: This runs the four engines in slurm
  interactively.  You don't need to interact with this once it is
  running, but remember to stop the process once it is done because it
  is using resources.  You can start/stop this as needed.
* Start your Python process and use things like normal::

    import os
    import ipyparallel
    client = ipyparallel.Client()
    result = client[:].apply_async(os.getpid)
    pid_map = result.get_dict()
    print(pid_map)

This method lets you turn on/off the engines as needed.  This isn't the
most advanced way to use ipyparallel, but works for interactive use.

See also: :doc:`../examples/python/ipyparallel/ipyparallel` for a version
which goes in a slurm script.

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
   `Python Package Index <https://pypi.org/>`__.
-  virtualenv: Creates a directory that has all self-contained packages
   that is manageable by the user themself. When the virtualenv is
   activated, all the operating-system global packages are no longer
   used. Instead, you install only the packages you want. This is
   important if you need to install specific versions of software, and
   also provides isolation from the rest of the system (so that you work
   can be uninterrupted). It also allows different projects to have
   different versions of things installed. virtualenv isn't magic, it
   could *almost* be seen as just manipulating ``PYTHONPATH``, ``PATH``, and the
   like. Docs: https://docs.python-guide.org/dev/virtualenvs/
-  conda: Sort of a combination of package manager and virtual
   environment. However, it *only* installed packages into environments,
   and is *not* limited to Python packages. It can also install other
   libraries (c, fortran, etc) into the environment. This is extremely
   useful for scientific computing, and the reason it was created. Docs
   for envs: https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html.

So, to install packages, there is ``pip`` and ``conda``. To make virtual
environments, there is ``venv`` and ``conda``.

Advanced users can see this `rosetta
stone <https://conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands>`__
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
