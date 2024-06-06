PyTorch
=======

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

:pagelastupdated: 2022-08-08

PyTorch is a commonly used Python package for deep learning.

Basic usage
***********

First, check the tutorials up to and including :doc:`../tut/gpu`.

If you plan on using NVIDIA's containers to run your model, please check
the page about :doc:`nvidiacontainers`.

The basic way to use PyTorch is via the Python in the ``scicomp-python-env`` module.
Don't load any additional CUDA modules, ``scicomp-python-env`` includes everything.


Building your own environment with PyTorch
******************************************

If you need a PyTorch version different to the one supplied with the scicomp python environment we
recommend installing your own conda environment as detailed `here </triton/apps/python-conda.rst>`_.

.. include:: /triton/examples/pytorch/pytorch_with_conda.rst

.. include:: /triton/examples/cuda/cuda_override_hint.rst


Examples:
*********

.. include:: ../examples/pytorch/pytorch_mnist.rst

.. include:: ../examples/pytorch/pytorch_singularity_mnist.rst


