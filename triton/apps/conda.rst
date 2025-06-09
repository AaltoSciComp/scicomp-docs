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
installation as well, for example cmake, Node.js, Java or Perl

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
