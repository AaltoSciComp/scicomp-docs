Tensorflow
==========

:supportlevel: A
:lastupdated: 2018-07-21
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


Example
-------

Interactive::

  omes1@@login2:~$ module load anaconda3

  omes1@login2:~$ srun --pty --gres=gpu --constraint='kepler|pascal|volta' bash
  srun: job 33637511 queued and waiting for resources
  srun: job 33637511 has been allocated resources

  omes1@gpu27:~$ python
  Python 3.6.6 |Anaconda custom (64-bit)| (default, Jun 28 2018,
  17:14:51)
  [GCC 7.2.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import tensorflow
  >>>


As a batch script (submit with ``sbatch``)::

  #!/bin/bash -l
  #SBATCH --gres=gpu
  #SBATCH --constraint='kepler|pascal|volta'

  module load anaconda3
  python my_script.py
