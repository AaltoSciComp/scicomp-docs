PyTorch
=======

:pagelastupdated: 2022-08-08

PyTorch is a commonly used Python package for deep learning.

Basic usage
***********

First, check the tutorials up to and including :doc:`../tut/gpu`.

If you plan on using NVIDIA's containers to run your model, please check
the page about :doc:`nvidiacontainers`.

The basic way to use PyTorch is via the Python in the ``anaconda`` module.
If you're not using Tensorflow as well, you can pick either ``-tf1``-
or ``-tf2``-version. If you're using Tensorflow as well, please check our
:doc:`tensorflow` page.

Don't load any additional CUDA modules, ``anaconda`` includes everything.

Building your own environment with PyTorch
******************************************

If you need a PyTorch version different to the one supplied with anaconda we
recommend installing your own anaconda environment as detailed `here </triton/apps/python-conda.rst>`_.
If you want to use the GPUs, you will need to install a GPU enabled pytorch version
in your environment. This can be done by explicitly requesting a GPU enabled 
pytorch version in your environment file as detailed below.
 
.. include:: /triton/examples/pytorch/pytorch_with_conda.rst


Examples:
*********

.. include:: ../examples/pytorch/pytorch_mnist.rst

.. include:: ../examples/pytorch/pytorch_singularity_mnist.rst


