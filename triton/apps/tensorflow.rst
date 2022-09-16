Tensorflow
==========

:pagelastupdated: 2022-08-08

.. highlight:: bash

Tensorflow is a commonly used Python package for deep learning.

Basic usage
***********

First, check the tutorials up to and including :doc:`../tut/gpu`.

If you plan on using NVIDIA's containers to run your model, please check
the page about :doc:`nvidiacontainers`.

We provide a module for gpu enabled tensorflow 2.6  which can be loaded by 
``module load tensorflow``. If you need a newer tensorflow version, 
we suggest you install it via your own conda environment (see the instructions below).

Installing via conda
********************

Have a look :doc:`here </triton/apps/python-conda>` for details on how to install 
conda environments.

.. include:: /triton/examples/cuda/cuda_override_hint.rst

.. include:: /triton/examples/tensorflow/tensorflow_with_conda.rst

Examples:
*********

.. include:: ../examples/tensorflow/tensorflow_mnist.rst

.. include:: ../examples/tensorflow/tensorflow_singularity_mnist.rst


