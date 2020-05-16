PyTorch
=======

:supportlevel: A
:pagelastupdated: 2020-05-15
:maintainer:

.. highlight:: bash

PyTorch is a commonly used Python package for deep learning.

Basic usage
-----------

First, check the tutorials up to and including :doc:`../tut/gpu`.

If you plan on using NVIDIA's containers to run your model, please check
the page about :doc:`nvidiacontainers`.

The basic way to use is via the Python in the ``anaconda`` module.
If you're not using Tensorflow as well, you can pick either ``-tf1``-
or ``-tf2``-version. If you're using Tensorflow as well, please check our
:doc:`tensorflow` page.

Don't load any additional CUDA modules, ``anaconda`` includes everything.

If you use GPUs, you need ``--constraint='kepler|pascal|volta'`` in
order to select a GPU new enough to run tensorflow.  (Note that as we
get newer cards, this will need further updating).

.. include:: ../examples/pytorch/pytorch_mnist.rst

.. include:: ../examples/pytorch/pytorch_singularity_mnist.rst

Common problems
---------------

* Random CUDA errors: don't load any other CUDA modules, only
  ``anaconda``.  Anaconda includes the necessary libraries in compatible
  versions.
