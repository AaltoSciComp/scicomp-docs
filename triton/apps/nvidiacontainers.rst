NVIDIA's singularity containers
===============================

:supportlevel: A
:pagelastupdated: 2020-05-15
:maintainer:

.. highlight:: bash

NVIDIA provides many different docker images containing scientific
software through their `NGC repository <https://ngc.nvidia.com>`_.
This software is available for free for NVIDIA's GPUs and one can
register for free to get access to the images.

You can use these images as a starting point for your own GPU images,
but do be mindful of NVIDIA's terms and conditions. If you want to
store your own images that are based on NGC images, either use
NGC itself or our own Docker registry that is documented on the
:doc:`singularity containers page <../usage/singularity>`.

We have converted some of these images with minimal changes into singularity
images that are available in Triton.

Currently updated images are:

  - ``nvidia-tensorflow``: Contains tensorflow. Due to major changes that
    happened between Tensorflow v1 and v2, image versions have either ``tf1``
    or ``tf2`` to designate the major version of Tensorflow.
  - ``nvidia-pytorch``: Contains PyTorch.

There are various other images available that can be installed very
quickly if required.

.. include:: ../examples/tensorflow/tensorflow_singularity_mnist.rst

.. include:: ../examples/pytorch/pytorch_singularity_mnist.rst
