===================
Nvidia DGX machines
===================

Triton currently has two `Nvidia DGX-1 machines <dgx_>`_ machines
which contain 8 V100 GPUs and are optimized for deep learning.

.. _dgx: https://en.wikipedia.org/wiki/Nvidia_DGX-1


Access and prerequisites
========================

The DGX machines have been specifically bought by several groups, and
thus public access is not available.  You can check the access list by
running ``getent group dgx``.  If you should have access but don't,
:doc:`email our support alias <../help>` with a CC to your group
leader, and we will fix this.


Basics
======

The DGX machines have a special operating system from Nvidia, and
thus form a very special case.  Their OS is based on Ubuntu 16.04,
while the rest of Triton is CentOS, so we have had to some work to
integrate them.  You may find some problems, please be aggressive
about filing issues (but also aggressive about checking yourself if
you can solve them).

Software and modules
--------------------

Basic reading: :doc:`../tut/modules`.

You should load software using the ``module`` command, just like the
rest of Triton.  However, since the base operating system is
different, modules are not automatically compatible.  So, you can't
automatically reuse the modules you use on the rest of Triton.

The current available modules are::

  ----------------------- /share/apps/anaconda-ci/modules ------------------------
  anaconda2/5.1.0-cpu        modules/anaconda2/5.1.0-cpu
  anaconda2/5.1.0-gpu (D)    modules/anaconda2/5.1.0-gpu (D)
  anaconda3/5.1.0-cpu        modules/anaconda3/5.1.0-cpu
  anaconda3/5.1.0-gpu (D)    modules/anaconda3/5.1.0-gpu (D)

  -------------------- /share/apps/singularity-ci/dgx/modules --------------------
  nvidia-caffe/18.02-py2          nvidia-tensorflow/18.02-py2
  nvidia-cntk/18.02-py3           nvidia-tensorflow/18.02-py3 (D)
  nvidia-mxnet/18.02-py2          nvidia-theano/18.02
  nvidia-mxnet/18.02-py3   (D)    nvidia-torch/18.02-py2
  nvidia-pytorch/18.02-py3

  ------------------------- /share/apps/modulefiles/dgx --------------------------
  matlab/r2012a    matlab/r2015b    matlab/r2016b
  matlab/r2014a    matlab/r2016a    matlab/r2017b (D)

  -------------------- /usr/share/lmod/lmod/modulefiles/Core ---------------------
  lmod/5.8    settarg/5.8

Unlike the rest of Triton, you can't see which modules are avali

Running jobs
------------

All runs on the DGX machines go via Slurm.  For an introduction to
slurm, see the tutorials on :doc:`interactive jobs
<../tut/interactive>`, :doc:`serial jobs <../tut/serial>`, and those
after.

The necessary slurm parameters to run on the DGX nodes are ``-p
dgx --gres=gpu:v100``  (the second one obviously requesting the
graphics card - to just test a shell, you could leave it off to get
resources sooner).  If you want more CPUs, add ``-c N``.  If you want
more (system) memory, use ``--mem=5GB`` and so on.

Because of environment mismatch, you need ot clear most environment
variables using ``export`` as you see below.  If there are extra
environment variables you need, add them here.

For example, to get an interactive shell, run (special to DGX nodes,
you should use the full path of bash)::

  srun -p dgx --gres=gpu:v100 --export=HOME,USER,TERM --pty /bin/bash -l

From here, you can do whatever you want interactively with your
dedicated resources.  Remember to log out when done, otherwise your
resources stay dedicated to you!

Nvidia containers
=================

Some of the Nvidia containers designed for the DGX machines are
available as modules - see above.  They are integrated with our Triton
:doc:`singularity <../singularity>` setup, so you can use those same
procedures::

  module load nvidia-tensorflow

  # Get a shell within the image:
  singularity_wrapper shell


  # Execute Python within the image
  singularity_wrapper exec python3 code.py

``singularity_wrapper`` sets the image file (from the module you
loaded), important options (to bind-mount things), and starts it.

This is a minimum slurm script (submit with ``sbatch``, see the slurm
info above and tutorials for more info)::

  #!/bin/bash -l
  #SBATCH -p dgx
  #SBATCH --gres=gpu:1
  #SBATCH --mem=5G --time=5:00
  #SBATCH --export=HOME,USER,TERM

  module load nvidia-tensorflow
  singularity_wrapper exec python -V


Other notes
===========

Forwarding ports is no different than the rest of Triton - you just
need to go through the login node: ``ssh -L
local_port:dgxNN.int.triton.aalto.fi:remote_port``.


Known bugs
==========

* You have to give the full path to ``/bin/bash`` and give the ``-l``
  option to make a login shell.
* You have to limit the environment variables you export, because they
  are different.  But you have to export at least ``HOME`` and possibly more.
* The ``/m/`` tree is not there (but ``/scratch`` is).
* You can't figure out modules are available without getting an interactive shell there.

