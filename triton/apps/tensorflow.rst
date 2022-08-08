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

Have a look `here </triton/apps/pyhon-conda.rst`_ for details on how to install 
conda environments.
While tensorflow GPU versions are no longer incompatible with systems where no 
GPU is present they commonly come with a slightly slower performance on CPUs 
compared to versions that are CPU optimized. Tensorflow addressed this issue by 
being clever and installing a version optimized to the machine it is installed 
on. This leads to an issue on clusters, where commonly the login node does not 
have a CUDA enabled GPU installed. Therefore, is necessary to explicitly override 
this selection mechanism as detailed `here <https://conda-forge.org/blog/posts/2021-11-03-tensorflow-gpu/#installation>`_
, or to explicitly select a cuda enabled version of tensorflow in the environment
file as explained below.

.. include:: /triton/examples/tensorflow/tensorflow_with_conda.rst

Examples:
*********

.. include:: ../examples/tensorflow/tensorflow_mnist.rst

.. include:: ../examples/tensorflow/tensorflow_singularity_mnist.rst


