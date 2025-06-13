.. _conda:

Software Environments with Conda
================================

**Conda** is a popular package manager that is especially
popular in data science and machine learning communities.  **mamba**
is a newer drop-in replacement with a much faster resolution
algorithm, you should use mamba for installing environments but most
commands work with either.

It is commonly used to handle complex requirements of Python
and R packages. Conda can handle many other library and software
installation as well, for example cmake, Node.js, Java or Perl.

.. seealso::

   Watch a `Research Software Hour episode on conda
   <https://www.youtube.com/watch?v=ddCde5Nu2qo&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__
   for an introduction + demo.


Doing everything faster with mamba
----------------------------------

For most purposes, `mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement
for conda that *is much faster*.  We recommend it everywhere it can be
used, and for most purposes mamba and conda are interchangeable.  They
manage the exact same environments.


Quick usage guide
-----------------

.. _conda-first-time-setup:


First time setup
~~~~~~~~~~~~~~~~

You can get conda and mamba by loading the ``mamba``-module.  **Mamba
is a faster drop-in replacement for conda and we recommend its use
where possible.**

.. code-block:: console

  $ module load mamba

By default Conda stores installed packages and environments in your home
directory. However, as your home directory has a lower quota, it is a good idea
to tell conda to install packages and environments into your work directory:

.. code-block:: console

  $ mkdir $WRKDIR/.conda_pkgs
  $ mkdir $WRKDIR/.conda_envs

  $ conda config --append pkgs_dirs ~/.conda/pkgs
  $ conda config --append envs_dirs ~/.conda/envs
  $ conda config --prepend pkgs_dirs $WRKDIR/.conda_pkgs
  $ conda config --prepend envs_dirs $WRKDIR/.conda_envs

Now you're all set up to create your first environment.


Creating a simple environment with conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One can install environments from the command line itself, but a better idea
is to write an ``environment.yml``-file that describes the environment.

Below we have a simple environment.yml

.. tabs::

   .. group-tab:: Python

        .. literalinclude:: /triton/examples/conda/python-environment.yml
           :language: yaml

    .. group-tab:: R

        .. literalinclude:: /triton/examples/conda/r-environment.yml
           :language: yaml

Now we can use the ``conda``-command to create the environment:

.. code-block:: console

  $ module load mamba
  $ mamba env create --file environment.yml

Once the environment is installed, you can activate it with:

.. code-block:: console

  $ source activate conda-example

.. include:: /triton/ref/condaactivate.rst

.. include:: /triton/apps/importantnotes/resetconda.rst 


Understanding the environment file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda environment files are written using YAML syntax.
In an environment file one usually defines the following:

- ``name``: Name of the desired environment.
- ``channels``: Which channels to use for packages.
- ``dependencies``: Which packages to install. This can
  include dependencies from PyPI using ``pip`` with
  :doc:`special syntax <python-conda>`.


Choosing conda channels
^^^^^^^^^^^^^^^^^^^^^^^

When an environment file is used to create an environment, conda
looks up the list of channels (in descending priority) and it will try to find
the needed packages.

Some of the most popular channels are:

- ``conda-forge``: An open-source channel with over 18k packages.
  Highly recommended for new environments.
- ``defaults``: A channel maintained by
  `Anaconda Inc. <https://www.anaconda.com>`_. You should exclude this
  due to licensing issues.  Default for anaconda distribution.
  in your own environments
- ``r`` : A subchannel of ``defaults``. The same licencing
  issues apply.
- ``bioconda``: A community maintained channel of
  `bioinformatics packages <https://bioconda.github.io>`_.
- ``nvidia`` : Maintained by NVIDIA. Contains packages for
  `CUDA <https://developer.nvidia.com/cuda-toolkit>`_ and other NVIDIA
  software.

One can have multiple channels defined like in the following example:

.. tabs::

  .. group-tab:: Python

      .. literalinclude:: /triton/examples/pytorch/pytorch-env.yml
         :language: yaml

  .. group-tab:: R

      .. literalinclude:: /triton/examples/r/bioconda-env.yml
         :language: yaml


Setting package dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Packages in ``environment.yml`` can have version constraints and version
wildcards.

.. tabs::

  .. group-tab:: Python

    One can also specify pip packages to install after conda-packages
    have been installed.

    .. literalinclude:: /triton/examples/conda/python-dependency-env.yml
      :language: yaml

  .. group-tab:: R

    .. literalinclude:: /triton/examples/conda/r-dependency-env.yml
      :language: yaml


Listing packages in an environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To list packages installed in an environment, one can use:

.. code-block:: console

  $ mamba list


Removing an environment
~~~~~~~~~~~~~~~~~~~~~~~

To remove an environment, one can use:

.. code-block:: console

  $ mamba env remove --name environment_name

Do remember to deactivate the environment before trying to remove it.


Cleaning up conda cache
~~~~~~~~~~~~~~~~~~~~~~~

Conda uses a cache for downloaded and installed packages. This cache can get
large or it can be corrupted by failed downloads.

In these situations one can use ``mamba clean`` to clean up the cache.

- ``mamba clean -i`` cleans up the index cache that conda uses to find the packages.
- ``mamba clean -t`` cleans up downloaded package installers.
- ``mamba clean -p`` cleans up unused packages.
- ``mamba clean -a`` cleans up all of the above.


Updating packages in an environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend updating the ``environment.yml`` file, and then:

.. code-block:: console

  $ mamba env update --file environment.yml

If you make major changes, or *anything* goes wrong, we recommend
removing the environment and re-creating it.  (This is a big benefit
of environment files).


Installing single new packages into an environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend the previous section instead, so that the
``environment.yml`` file stays consistent, and you can always re-create
or move the environment if needed


If needed, ``mamba-install`` can be used (in this case, install
``matplotlib`` from ``conda-forge`` into an environment.

.. code-block:: console

  $ mamba install --freeze-installed --channel conda-forge matplotlib

Installing packages into an existing environment can be risky: conda uses
channels given from the command line when it determines which channels it
should use for the new packages.

This can cause a situation where installing a new package results in the
removal and reinstallation of multiple packages. Adding the
``--freeze-installed``-flags makes already installed packages safe and by
giving explicitly the channels to use, one can make certain that the new
packages come from the same source.

It is usually a better option to create a new environment with the new
package set as an additional dependency in the ``environment.yml``.
This keeps the environment reproducible.

If you intend on installing packages to existing environment, adding
default channels for the environment can also make installing packages
easier.


Setting default channels for an environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is a good idea to store channels used when creating the environment
into a configuration file that is stored within the environment. This makes
it easier to install any missing packages.

For example, one could add ``conda-forge`` into the list of default channels
with:

.. code-block:: console

  $ conda config --env --add channels conda-forge

We can check the contents of the configuration file with:

.. code-block:: console

  $ cat $CONDA_PREFIX/.condarc

  
Motivation for using conda
--------------------------


When should you use conda?
~~~~~~~~~~~~~~~~~~~~~~~~~~

For many common use cases, you can use the pre-installed scientific
computing modules. For example, see the :doc:`Python-page <python>` or
the :doc:`R-page <r>` for more information.

You should use conda when you need to create your own custom environment.


Why use conda? What are its advantages?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing package directly with a system package manager such as
`apt` or a language specific package manager such as `pip` for Python or
`npm` for JavaScript
is usually enough if you are the only user and working on one project.
However, conda solces several problems that often arise in scientific
computing. If these are familiar, using Conda is a good idea:

1. How do you install multiple separate suites of packages for different use cases?
2. How do you handle packages that depend on some external libraries?
3. How do you make sure that all of the packages have are compatible with each other?
4. How do you install and use multiple different versions of the same package?

Conda tries to solve these problems with the following ways:

1. Conda creates **environments** where packages are installed. Each
   environment can be activated separately.
2. Conda installs library **dependencies** to the environment.
3. Conda uses a **solver engine** to figure out whether packages are compatible
   with each other.

Conda also caches installed packages so doing copies of similar environments
does not use additional space.

One can also use the environment files to make the installation procedure more
reproducible.


Creating an environment with CUDA toolkit
-----------------------------------------

NVIDIA's `CUDA-toolkit <https://developer.nvidia.com/cuda-toolkit>`_ is
needed for working with NVIDIA's GPUs. Many frameworks that work on
GPUs need to have a supported CUDA toolkit installed.

Conda is often used to provide the CUDA toolkit and additional libraries such
as cuDNN. However, one should choose the version of the CUDA toolkit based on
what the software requires.

If the package is installed from a conda channel such as ``conda-forge``,
conda will **automatically retreive the correct version of CUDA toolkit**.


In other cases one can use an environment file like this:

.. literalinclude:: /triton/examples/cuda/cuda-env.yml
   :language: yaml
  
.. _cuda_hint:

.. include:: /triton/examples/cuda/cuda_override_hint.rst



Creating an environment with GPU enabled Tensorflow
---------------------------------------------------


.. tabs::

  .. group-tab:: Python

    .. include:: /triton/examples/tensorflow/tensorflow_with_conda.rst

  .. group-tab:: R

    To create an environment with GPU enabled Tensorflow you can use an
    environment file like this:

    .. literalinclude:: /triton/examples/conda/r-tensorflow-cuda.yml

    Here we install the latest tensorflow from ``conda-forge``-channel with an additional
    requirement that the build version of the ``tensorflow``-package must contain
    a reference to a CUDA toolkit. For a specific version replace the ``=*=*cuda*`` with e.g. ``=2.8.1=*cuda*`` for version ``2.8.1``.



Creating an environment with GPU enabled Torch
----------------------------------------------

.. tabs::

  .. group-tab:: Python

    .. include:: /triton/examples/pytorch/pytorch_with_conda.rst

  .. group-tab:: R

    .. include:: /triton/examples/conda/r-torch-cuda.rst



If you encounter errors related to CUDA while creating the
environment, do note :ref:`this hint <cuda_hint>` on overriding
CUDA during installation.


Using an optimized Intel MKL enabled BLAS library
-------------------------------------------------

BLAS (Basic Linear Algebra Subprograms) is a linear algebra library used
be R and Julia, the `Numpy <https://numpy.org/>`_ library for Python, and
many other libraries.
Intel provides their own fast BLAS implementation in
Intel MKL (Math Kernel Library). When using Intel CPUs, this library
can give a significant performance boost to mathematical calculations.

One can install this library as the default BLAS by specifying
``blas * mkl`` as a requirement in the dependencies like in this:


.. tabs::

  .. group-tab:: Python

    .. literalinclude:: /triton/examples/conda/numpy-mkl-env.yml
      :language: yaml
  .. group-tab:: R

    .. literalinclude:: /triton/examples/conda/r-mkl-env.yml
      :language: yaml



