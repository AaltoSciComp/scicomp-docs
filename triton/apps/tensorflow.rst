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


Example 2 (older)
-----------------

.. warning::

   You no longer need to manually install tensorflow, so the first
   part of this example is not relevant anymore.

This chapter gives a step-by-step guide how to run the tensorflow
cifar10 example on 4 gpu's. All commands below are typed on the login
node, it is not necessary to ssh to a gpu node first.

First load anaconda (python), CUDA and cudnn

::

    $ module load anaconda2 CUDA/7.5.18 cudnn/4

After that create a conda environment to install tensorflow in:

::

    $ conda create -n tensorflow python=2.7

    $ source activate tensorflow
    $ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl
    $ pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl

For some (unclear) reason you have to run the pip command twice, first
with ``--ignore-installed`` and second time without to make the conda
environment work.

Now we can create a batch script (``submit_cifar.sh``) that runs this
code on 4 gpus

::

    #!/bin/bash

    #Request 4 gpus
    #SBATCH --gres=gpu:4 --constraint='kepler|pascal|volta'
    #SBATCH --mem-per-cpu 10G
    #SBATCH -t 4:00:00

    module load anaconda2 CUDA/7.5.18 cudnn/4
    source activate tensorflow

    python -m tensorflow.models.image.cifar10.cifar10_multi_gpu_train --num-gpus 4

You can submit this job with

::

    $ sbatch submit_cifar.sh

and you'll be able to find the results in the slurm log file.

