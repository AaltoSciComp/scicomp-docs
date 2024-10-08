======
Python
======
.. _Python Help:

.. admonition:: Video

   `See an example in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=Pd1LUyDIOfg&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=20>`__


Python is widely used programming language where we have installed all
basic packages on every node. Yet, python develops quite fast and the
system provided packages are ofter not complete or getting old.

.. highlight:: console

Python distributions
--------------------

.. list-table::
   :header-rows: 1

   * *
     * What to use
     * How

   * * I use some common libraries
     * The pre-built python environment by ASC
     * ``module load scicomp-python-env``

   * * I need to select my own packages
     * Mamba/conda environments
     * ``module load mamba`` and :doc:`python-conda`

   * * Own small pure Python packages
     * Virtual environment (for most purposes we recommend Conda though)
     * Normal virtualenv tools


The main version of modern Python is 3. Support for old Python 2 ended at the
end of 2019. There are also different distributions: The "regular" CPython,
Anaconda (using the conda package manager and containing CPython + a lot of other scientific software all
bundled together, but not licensed for use in large organizations),
miniforge/micromamba (installers focusing on the conda-forge channel
from the conda package manager),
PyPy (a just-in-time compiler,  which can be much faster for
some use cases).

Make sure your environments are **reproducible** - you can recreate
them from scratch.  History shows it's easier to re-create when you
have a problem (compared to solving dependency problems), and your
code will also be installable on other systems.
We recommend a minimal ``environment.yml`` (conda) or
``requirements.txt`` (pip), hand-created with exactly what you need in
there.


.. _scicomp-python-env:

Triton pre-built ``scicomp-python-env``
---------------------------------------

This module contains a pre-built Conda environment with many common
packages people request.  It might serve your needs, and we can
install other packages into it if you need it (but it might be faster
to make your own env).  Note that the versions in this might get updated
at any time, so it's not a stable solution.

It is loaded through the module system::

  $ module load scicomp-python-env



Conda environments
------------------

.. seealso::

   :doc:`python-conda`



.. _virtualenv:

Virtual environments
--------------------

Python's normal virtual environment tools work on Triton.  We normally
recommend Conda environments instead, since they handle all the extra
compiled libraries needed for scientific software.  Virtual
environments probably work fine for pure-Python code.

We don't include more instructions on virtual environments here.



Conda/virtualenvironments in Jupyter
------------------------------------

If you make a conda environment / virtual environment, you can use it
from Triton's JupyterHub (or your own Jupyter).  See
:ref:`triton-jupyter-virtualenv-conda-kernels`.



Warning: ``pip install --user``
-------------------------------

.. warning:: ``pip install --user`` can result in incompatibilities

   We stringly recommend not to instal packages using ``pip install --user``.
   If you do this, the package will be shared among all
   your projects, and will even overwrite any package installed in an environment.
   It is quite likely that eventually, you will get some
   incompatibilities between the Python you are using and the packages
   installed. In that case, you are on your own (simple recommendation is
   to remove all packages from ``~/.local/lib/pythonN.N`` and reinstall). **If
   you get incompatible module errors, our first recommendation will be to
   remove everything installed this way and use conda/virtual
   environments instead.**  It's not a bad idea to do this when you
   switch to environments anyway.

   If you encounter problems, remove all your user packages::

      $ rm -r ~/.local/lib/python*.*/

   and reinstall everything *after* loading the environment you want.

.. note:: Example of dangers of ``pip install --user``

   Someone did ``pip install --user tensorflow``.  Some time later,
   they noticed that they couldn't use Tensorflow + GPUs.  We couldn't
   reproduce the problem, but in the end found they had this local
   install that was hiding any Tensorflow in any module (forcing a CPU
   version on them).



Background: ``pip`` vs ``python`` vs ``anaconda`` vs ``conda`` vs ``virtualenv``
--------------------------------------------------------------------------------

Virtual environments are self-contained python environments with
all of their own modules, separate from the system packages.  They are
great for research where you need to be agile and install whatever
versions and packages you need.  **We highly recommend virtual
environments or conda environments (below)**

   -  Conda: use conda, see below
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

.. include:: ../examples/python/python_openmp/python_openmp.rst


Running MPI parallelized Python with mpi4py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MPI parallelized Python requires a valid MPI installation that support
our SLURM scheduler. We have installed MPI-supporting Python versions to different toolchains.

Using mpi4py is quite easy. Example is provided below.

.. include:: ../examples/python/mpi4py/mpi4py.rst
