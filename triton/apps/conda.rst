.. _conda:

Conda
=====

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

   $ source activate tidyverse

.. include:: /triton/ref/condaactivate.rst

.. include:: /triton/apps/importantnotes/resetconda.rst 


Understanding the environment file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda environment files are written using YAML syntax.
In an environment file one usually defines the following:

- ``name``: Name of the desired environment.
- ``channels``: Which channels to use for packages.
- ``dependencies``: Which packages to install. 


.. admonition:: Python-Specific: Using Pip in an environment file
   :class: dropdown

   Some packages or versions of packages may not be available in the
   Conda channels, but are available on the Python Package Index (PyPI).
   Conda provides a syntax for specifying these packages in the environment
   file, allowing you to track all dependencies in one place.

   .. code-block:: yaml

      name: conda-pip-env
      channels:
         - conda-forge
      dependencies:
         # Conda packages
         - python=3.9
         - pandas

         # Pip packages
         - pip:
            - some-pypi-only-package
            - git+https://github.com/user/repo.git@main


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

To list packages installed the in currently activated environment, one can use:

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
computing modules. For example, see the :ref:`Python page <scicomp-python-env>` or
the :doc:`R page <r>` for more information.

You should use conda when you need to create your own custom environment.


Why use conda? What are its advantages?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing package directly with a system package manager such as
``apt`` or a language specific package manager such as ``pip`` for Python or
``npm`` for JavaScript
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



Advanced usage
--------------


Finding available packages
~~~~~~~~~~~~~~~~~~~~~~~~~~

Because conda tries to make certain that all packages in an environment
are compatible with each other, there are usually tens of different versions
of a single package.

One can search for a package from a channel with the following command:

.. code-block:: console

   $ conda search --channel conda-forge libtorch

This will return a long list of packages where each line looks something like
this::

  libtorch                       2.6.0 cuda126_mkl_h76b5ff1_303  conda-forge

Here we have:

- The package name (``libtorch``).
- Version of the package (``2.6.0``).
- Package build version. This version often contains information on
  the libraries used by the package ( or CUDA 12.6).
  - ``cuda126`` indicates CUDA 12.6
  - ``mkl`` refers to the Intel MKL library

- Channel where the package comes from (``conda-forge``).


Checking package dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One can check package dependencies by adding the ``--info``-flag to the
search command. This can give a lot of output, so it is a good idea to
limit the search to one specific package:

.. code-block:: console

   $ conda search --info --channel conda-forge libtorch=2.6.0=cuda126_mkl_h76b5ff1_303

The output looks something like this::

  libtorch 2.6.0 cuda126_mkl_h76b5ff1_303
  ---------------------------------------
  file name   : libtorch-2.6.0-cuda126_mkl_h76b5ff1_303.conda
  name        : libtorch
  version     : 2.6.0
  build       : cuda126_mkl_h76b5ff1_303
  build number: 303
  size        : 498.4 MB
  license     : BSD-3-Clause
  subdir      : linux-64
  url         : https://conda.anaconda.org/conda-forge/linux-64/libtorch-2.6.0-cuda126_mkl_h76b5ff1_303.conda
  md5         : 9e678f51a95616bfb8435cce925d8866
  timestamp   : 2025-03-26 00:20:08 UTC
  constraints : 
    - pytorch-gpu ==2.6.0
    - pytorch-cpu ==99999999
    - pytorch 2.6.0 cuda126_mkl_*_303
  dependencies: 
    - __glibc >=2.17,<3.0.a0
    - _openmp_mutex * *_llvm
    - _openmp_mutex >=4.5
    - cuda-cudart >=12.6.77,<13.0a0
    - cuda-cupti >=12.6.80,<13.0a0
    - cuda-nvrtc >=12.6.85,<13.0a0
    - cuda-nvtx >=12.6.77,<13.0a0
    - cuda-version >=12.6,<13
    - cudnn >=9.8.0.87,<10.0a0
    - libabseil * cxx17*
    - libabseil >=20250127.1,<20250128.0a0
    - libblas * *mkl
    - libcblas >=3.9.0,<4.0a0
    - libcublas >=12.6.4.1,<13.0a0
    - libcudss >=0.5.0.16,<0.5.1.0a0
    - libcufft >=11.3.0.4,<12.0a0
    - libcufile >=1.11.1.6,<2.0a0
    - libcurand >=10.3.7.77,<11.0a0
    - libcusolver >=11.7.1.2,<12.0a0
    - libcusparse >=12.5.4.2,<13.0a0
    - libgcc >=13
    - libmagma >=2.9.0,<2.9.1.0a0
    - libprotobuf >=5.29.3,<5.29.4.0a0
    - libstdcxx >=13
    - libuv >=1.50.0,<2.0a0
    - libzlib >=1.3.1,<2.0a0
    - llvm-openmp >=20.1.1
    - mkl >=2024.2.2,<2025.0a0
    - nccl >=2.26.2.1,<3.0a0
    - sleef >=3.8,<4.0a0


Packages with underscores are meta-packages that should not be added to conda
environment specifications. They will be solved by conda automatically.

Here we can see more info on the package, including its dependencies.

When using mamba, one can also use ``mamba repoquery depends`` to
see the dependencies:

.. code-block:: console

   $ mamba repoquery depends --channel conda-forge tensorflow=2.8.1=cuda112py39h01bd6f0_0

Output looks something like this::

  Name                     Version Build                 Channel
  ─────────────────────────────────────────────────────────────────────────────
  __glibc >=2.17,<3.0.a0 >>> NOT FOUND <<<                                                           
  _openmp_mutex                            4.5        3_gnu                      conda-forge linux-64
  cuda-cudart                              12.9.79    h5888daf_0                 conda-forge linux-64
  cuda-cupti                               12.9.79    h9ab20c4_0                 conda-forge linux-64
  cuda-nvrtc                               12.9.86    h5888daf_0                 conda-forge linux-64
  cuda-nvtx                                12.9.79    h5888daf_0                 conda-forge linux-64
  cuda-version                             12.9       h4f385c5_3                 conda-forge noarch  
  cudnn                                    9.10.1.4   h7646684_0                 conda-forge linux-64
  libabseil                                20250512.0 cxx17_hba17884_0           conda-forge linux-64
  libabseil                                20250127.1 cxx17_hbbce691_0           conda-forge linux-64
  libblas                                  3.9.0      19_linux64_mkl             conda-forge linux-64
  libcblas                                 3.9.0      11_h71a1b9d_netlib         conda-forge linux-64
  libcublas                                12.9.1.4   h9ab20c4_0                 conda-forge linux-64
  libcudss                                 0.5.0.16   h14340ca_0                 conda-forge linux-64
  libcufft                                 11.4.1.4   h5888daf_0                 conda-forge linux-64
  libcufile                                1.14.1.1   ha8da6e3_0                 conda-forge linux-64
  libcurand                                10.3.10.19 h9ab20c4_0                 conda-forge linux-64
  libcusolver                              11.7.5.82  h9ab20c4_0                 conda-forge linux-64
  libcusparse                              12.5.10.65 h5888daf_0                 conda-forge linux-64
  libgcc                                   15.1.0     h767d61c_2                 conda-forge linux-64
  libmagma                                 2.9.0      h19665d7_1                 conda-forge linux-64
  libprotobuf                              5.29.3     h501fc15_0                 conda-forge linux-64
  libstdcxx                                15.1.0     h8f9b012_2                 conda-forge linux-64
  libtorch                                 2.6.0      cuda126_mkl_h76b5ff1_303   conda-forge linux-64
  libuv                                    1.51.0     hb9d3cd8_0                 conda-forge linux-64
  libzlib                                  1.3.1      h4ab18f5_1                 conda-forge linux-64
  llvm-openmp                              20.1.6     h024ca30_0                 conda-forge linux-64
  mkl                                      2024.2.2   ha957f24_15                conda-forge linux-64
  nccl                                     2.27.3.1   h03a54cd_0                 conda-forge linux-64
  sleef                                    3.8        h1b44611_0                 conda-forge linux-64

One can also print the full dependency list with
``mamba repoquery depends --tree``. This will produce a really long output.

.. code-block:: console

   $ mamba repoquery depends --tree --channel conda-forge tensorflow=2.8.1=cuda112py39h01bd6f0_0


Fixing conflicts between packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually first step of fixing conflicts between packages is to write a new
environment file and list all required packages in the file as dependencies.
A fresh solve of the environment can often result in a working environment.

Sometimes there is a case where a single package does not have support for a
specific version of Python or specific version of CUDA toolkit. In these cases
it is usually beneficial to give more flexibility to the solver by limiting
the number of specified versions.

One can also use the search commands provided by ``mamba`` to see what
dependencies individual packages have.

