Keras
=====

:supportlevel:
:pagelastupdated: 2018
:maintainer:

Keras is a neural network library which runs on tensorflow (among
other things).

Basic usage
-----------

Keras is available in the ``anaconda2/3`` modules (GPU version) and
some other anaconda modules.  Run ``module spider anaconda3`` to list
available modules.  The ``-cpu`` modules have a tensorflow that will
run on CPUs.  The others have GPU-only versions, so you *have* to run
in the :doc:`GPU queues <../tut/gpu>`.  The other information in the
:doc:`tensorflow <tensorflow>` page also applies, especially the
``--constraint`` options to restrict to the GPUs that have new enough
features.

Example
-------

::

   srun -p gpu --pty bash
   module load anaconda3
   python3
   >>> import keras
   Using TensorFlow backend.
   >>> keras.__version__
   '2.2.4'
