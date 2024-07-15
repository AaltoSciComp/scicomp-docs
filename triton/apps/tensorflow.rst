Tensorflow
==========

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

:pagelastupdated: 2022-01-09

.. highlight:: bash

Tensorflow is a commonly used Python package for deep learning.

Basic usage
-----------

First, check the tutorials up to and including :doc:`../tut/gpu`.

Installing via conda
--------------------

Have a look :doc:`here </triton/apps/python-conda>` for details on how to install
conda environments.

.. include:: /triton/examples/tensorflow/tensorflow_with_conda.rst

.. include:: /triton/examples/cuda/cuda_override_hint.rst


Examples
--------

.. include:: ../examples/tensorflow/tensorflow_mnist.rst

.. include:: ../examples/tensorflow/tensorflow_singularity_mnist.rst


