Tensorflow
==========

:supportlevel: A
:pagelastupdated: 2019-06-03
:maintainer:

.. highlight:: bash

Tensorflow is a commonly used Python package for deep learning.

Basic usage
-----------

First, check the tutorials up to and including :doc:`../tut/gpu`.

With tensorflow, you have to decide at *install time* if you want a
version that runs on CPUs or GPUs.  This means that we can't install
it for everyone and expect it to work everywhere - you have to load
something different if you want it to run on login node/regular nodes
(probably for testing) or GPU nodes.  You probably want to use GPUs.

The basic way to use is via the Python in the ``anaconda3`` module (or
``anaconda2``) - but these modules have the GPU version installed, so
you can't run or test on the login node.

If you ``module spider anaconda3`` (or 2), you can see several
versions ending in ``-cpu`` or ``-gpu``.  These have respectively the
CPU and GPU versions of tensorflow installed.

If you use GPUs, you need ``--constraint='kepler|pascal|volta'`` in
order to select a GPU new enough to run tensorflow.  (Note that as we
get never cards, this will need further updating).

.. include:: ../examples/tensorflow/tensorflow_mnist.rst
