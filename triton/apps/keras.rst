Keras
=====

:supportlevel:
:pagelastupdated: 2020-02-20
:maintainer:

Keras is a neural network library which runs on tensorflow (among
other things).

Basic usage
-----------

Keras is available in the ``scicomp-python-env`` module and some other 
modules.  Run ``module spider scicomp-python-env`` to list available modules.

You probably want to learn how to run in the :doc:`GPU queues
<../tut/gpu>`.  The other information in the :doc:`tensorflow
<tensorflow>` page also applies, especially the ``--constraint``
options to restrict to the GPUs that have new enough features.

Example
-------

::

   srun --gres=gpu:1 --pty bash
   module load scicomp-python-env
   python3
   >>> import keras
   Using TensorFlow backend.
   >>> keras.__version__
   '2.2.4'
