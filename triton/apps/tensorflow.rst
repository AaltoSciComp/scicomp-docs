Tensorflow
==========

:supportlevel: A
:pagelastupdated: 2020-02-20
:maintainer:

.. highlight:: bash

Tensorflow is a commonly used Python package for deep learning.

Basic usage
-----------

First, check the tutorials up to and including :doc:`../tut/gpu`.

The basic way to use is via the Python in the ``anaconda`` module.
The versions with ``-tf2`` (the default ones) have Tensorflow 2
installed.  If you use ``module spider anaconda``, you can see a
``-tf1`` version available.

.. warning:: Older versions of Tensorflow were CPU-only or GPU-only

   With older versions of tensorflow (<1.15.0), you have to decide at
   *install time* if you want a version that runs on CPUs or GPUs. This
   means that we can't install it for everyone and expect it to work
   everywhere - you have to load something different if you want it to
   run on login node/regular nodes (probably for testing) or GPU nodes.
   The old ``-cpu`` and ``-gpu`` versions in the ``anaconda2``- and
   ``anaconda3``-modules denoted this.

   From tensorflow versions >= 1.15.0, they solved this problem (thankfully)

Don't load any additional CUDA modules, anaconda includes everything.

If you use GPUs, you need ``--constraint='kepler|pascal|volta'`` in
order to select a GPU new enough to run tensorflow.  (Note that as we
get newer cards, this will need further updating).

.. include:: ../examples/tensorflow/tensorflow_mnist.rst


Common problems
---------------

* **ImportError: libcuda.so.1: cannot open shared object file: No such
  file or directory**. Older versions of GPU tensorflow can only be imported
  on GPU nodes (even though you'd think that you can import it and just not
  use the GPUs).  So you can only run this code in the GPU queue. Solution
  for this is to use the newer ``anaconda``-modules.

* Random CUDA errors: don't load any other CUDA modules, only
  ``anaconda``.  Anaconda includes the necessary libraries in compatible
  versions.
