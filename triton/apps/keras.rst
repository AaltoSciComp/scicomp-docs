Keras
=====

:supportlevel:
:pagelastupdated: 2020-02-20
:maintainer:

Keras is a neural network library which runs on tensorflow (among
other things).

Basic usage
-----------

Keras is available in the ``anaconda`` module and some other anaconda
modules.  Run ``module spider anaconda`` to list available modules.

You probably want to learn how to run in the :doc:`GPU queues
<../tut/gpu>`.  The other information in the :doc:`tensorflow
<tensorflow>` page also applies, especially the ``--constraint``
options to restrict to the GPUs that have new enough features.

Example
-------

::

   srun -p gpu --pty bash
   module load anaconda
   python3
   >>> import keras
   Using TensorFlow backend.
   >>> keras.__version__
   '2.2.4'
