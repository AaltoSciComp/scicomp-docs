===================
Nvidia DGX machines
===================

Triton currently has two `Nvidia DGX-1 machines <dgx_>`_ machines
which contain 8 V100 GPUs and are optimized for deep learning.

.. _dgx: https://en.wikipedia.org/wiki/Nvidia_DGX-1


Access and prerequisites
========================

The DGX machines have been specifically bought by several groups, and
thus general access is not available.  If you should have access but
don't, :doc:`email our support alias <../help>` with a CC to your
group leader, and we will fix this.  You can check the access list by
running ``getent group dgx``.


Basics
======

The DGX machines have a special operating system from Nvidia based on
Ubuntu 16.04, and thus form a very special of a Triton node because
the rest of Triton is CentOS.  We have done work to make them work
together, but it will require special effort to make code run on both
halves.  You may find some problems, so please be aggressive about
filing issues (but also aggressive about checking the background
yourself and giving us good information).

Basic reading: :doc:`../tut/connecting`.

Unlike before, direct access is not available: you should connect to
the login node and submit jobs via Slurm, not running directly
interactively.

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

Unlike the rest of Triton, you can't see which modules are available
on the login node: currently see above (which might go out of date)
or get an interactive shell on the DGX node (see below) and run
``module avail`` yourself.

Running jobs
------------

Basic reading: tutorials on :doc:`interactive jobs
<../tut/interactive>`, :doc:`serial jobs <../tut/serial>`

All runs on the DGX machines go via Slurm.  For an introduction to
slurm, see the tutorials linked above, and in general all the rest of
the Triton user guide.  Slurm is a cluster scheduling system, which
takes job requests (code, CPU/memory/time/hardware requirements) and
distributes it to nodes.  You basically need to declare what your jobs
require, and tell it to run on DGX nodes.

Basic required slurm options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The necessary Slurm parameters are:

* ``-p dgx`` to indicate that we want to run in the DGX partitions.
* ``--gres=gpu:v100:1`` to request GPUs (Slurm also manages GPUs and
  limits you to the proper devices).

  * To request more than one graphics card, ``--gres=gpu:2:v100:1``

* ``--export=HOME,USER,TERM`` to limit the environment exported.
  Because these are a different operating system, you need to clear
  most environment variables.  If there are extra environment
  variables you need, add them here.

* ``/bin/bash -l``: you need to give the full path to ``bash`` and
  request a login shell, or else the environment won't be properly
  set by Slurm.


* To set the run time, ``--time=HH:MM:SS``.  If you want more CPUs,
add ``-c N``.  If you want more (system) memory, use ``--mem=5GB`` and
so on.  (These are completely generic slurm options.)

To check running and jobs: ``squeue -p dgx`` (whole cluster) or
``slurm q`` (for your own jobs).


Getting an interactive shell for own work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, to get an interactive shell, run::

  srun -p dgx --gres=gpu:v100:1 --export=HOME,USER,TERM --pty /bin/bash -l

From here, you can do whatever you want interactively with your
dedicated resources almost as if you logged in directly.  Remember to
log out when done, otherwise your resources stay dedicated to you and
no one else can use them!


Batch scripts
~~~~~~~~~~~~~

Similarly to the rest of Triton, you can make batch scripts::

  #!/bin/bash -l
  #SBATCH -p dgx
  #SBATCH --gres=gpu:1
  #SBATCH --mem=5G --time=5:00
  #SBATCH --export=HOME,USER,TERM

  your shell commands here


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

