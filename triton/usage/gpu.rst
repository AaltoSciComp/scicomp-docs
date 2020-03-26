=============
GPU Computing
=============

.. seealso::

   Introductory tutorial: :doc:`../tut/gpu` (read this first)

Overview
========

Triton has GPU cards from four different NVIDIA generations, as
described below.

Hardware breakdown
==================

.. include:: ../ref/gpu.rst


* Note: Tesla K80 cards are in essence two GK210 GPUs on a single chip
* Note: V100 cards are part of DGX machines, which were purchased by
  several groups and are currently special access only.  They are also a
  different operating system, please see :doc:`dgx`.

Detail info about cards available at
https://en.wikipedia.org/wiki/Nvidia_Tesla and for general info about
Nvidia GPUs
https://www.nvidia.com/object/tesla-supercomputing-solutions.html

Using GPU nodes
===============

GPU partitions
--------------

There are two queues governing these nodes: ``gpu`` and ``gpushort``, where the
latter is for jobs up to 4 hours.  Partitions are automatically selected.

The latest details can always be found with the following command::

    $ slurm p | grep gpu

GPU node allocation
-------------------

For gpu resource allocation one has to request a GPU resource, with
``--gres=gpu:N`` , where ``N``
stands for number of requested GPU cards.  To request a GPU with a
certain architecture, use ``--constraint=GENERATION``.   To request a specific card,
one must use syntax  ``--gres=gpu:CARD_TYPE:N``.  See the table below
for "slurm feature name" or "Slurm gres name".  For the full current
list of configured SLURM gpu cards names run ``slurm features``.


Example usages::

   --gres=gpu:2
   --gres=gpu:1 --constraint=pascal
   --gres=gpu:telsap100:1

When using multiple GPU's please verify that the code actually uses them with
instructions given in `Monitoring GPU usage`_.

GPU nodes environment and CUDA
------------------------------

User environment on ``gpu*`` nodes is the same as on other nodes, the
only difference is that they have nvidia kernel modules for Tesla cards.
`CUDA <https://www.nvidia.com/object/cuda_home_new.html>`__ comes through
``module``.

::

    $ module avail cuda    # list installed CUDA modules
    $ module load cuda/10.0.130   # load CUDA environment that you need
    $ nvcc --version   # see actual CUDA version that you got

Running a GPU job in serial
---------------------------

Quick interactive run::

    $ module load cuda
    $ srun -t 00:30:00 --gres=gpu:1 $WRKDIR/my_gpu_binary

Allocating a gpu node for longer interactive session, this will give you
a shell sessions::

    $ module load cuda
    $ sinteractive -t 4:00:00 --gres=gpu:1
    gpuXX$ .... run something
    gpuXX$ exit

Run a batch job

::

    $ sbatch gpu_job.sh

Where ``gpu_job.sh`` is

::

    #!/bin/bash

    #SBATCH --time=01:15:00          ## wallclock time hh:mm:ss
    #SBATCH --gres=gpu:teslak80:1    ## one K80 requested

    module load cuda

    ## run my GPU accelerated executable, note the --gres
    srun --gres=gpu:1  $WRKDIR/my_gpu_binary

Monitoring GPU usage
====================

Currently there isn't a good way of monitoring the gpu usage
non-interactively. Interactively one can (when the job is running) ssh to the
gpu node in question and run

::

    login2$ ssh gpuxx
    gpuxx$ watch -n 1 nvidia-smi

``CTRL + C`` quits the command.

This shows the gpu usage with 1 second interval. The GPU utilized by process
with PID X is shown in the first column of the second table. The first table
lists the GPUs by their ID Checking the ``Volatile GPU-Util`` column gives the
utilization of GPU. If your code uses less than 50% of the GPU you should
try to improve the data loading / CPU part of your code as the GPU is
underutilized.

If you run multi-GPU job you should verify that the all GPUs are properly
utilized. For many applications one needs to use multiple CPUs to fill the
GPUs with data. With badly implemented data handling multi-GPU setups can
be slower than single-GPU setups.


Development
===========

Compiling
---------

In case you either want to compile a CUDA code or a code with GPU
support, you must do it on one of the gpu nodes (because of nvidia libs
installed on those nodes only).

::

    $ sinteractive -t 1:00:00 --gres=gpu:1    # open a session on a gpu node
    $ module load cuda                        # set CUDA environment
    $ nvcc cuda_code.cu -o cuda_code          # compile your CUDA code
    .. or compile normally any other code with 'make'

Debugging
---------

CUDA SDK provides an extension to the well-known gnu debugger gdb. Using
cuda-gdb it is possible to debug the device code natively on the GPU. In
order to use the ``cuda-gdb``, one has to compile the program with option
pair ``-g -G``, like follows:

::

    $ nvcc -g -G cuda_code.cu -o cuda_code

See `CUDA-GDB User
Guide <https://developer.download.nvidia.com/compute/DevZone/docs/html/C/doc/cuda-gdb.pdf>`__
for a more information on cuda-gdb.

Applications and known issues
=============================

Check the :ref:`application-list` for most software.

nvidia-smi utility
------------------

Could be useful for debugging, in case one want to see the actual gpu
cards available on the node. If this command returns an error, you should
report that something is wrong on the node.

::

    gpuxx$ nvidia-smi -L   # gives a list of GPU cards on the node


cuDNN
-----

``cudnn`` is available as a module. The latest version can be found with
``module spider cudnn``. Note that (at least the later versions of)
cudnn require newer cards and cannot be used on the old fermi cards.
E.g. tensorflow does not run on the older fermi cards for this reason.


Nvidia MPS
----------

`Nvidia Multi-Process Service (MPS)
<https://docs.nvidia.com/deploy/mps/index.html>`__ provides a way to
share a single GPU among multiple processes. It can be used to
increase the GPU utilization by timesharing the GPU access, e.g. one
process can upload data to the GPU while another is running a
kernel. To use it one must first start the MPS server, and then CUDA
calls are automatically routed via the MPS server. At the end of the
job one must remember to shut it down. Example job script:

::

   #!/bin/bash -l

   #SBATCH --time=01:15:00          ## wallclock time hh:mm:ss
   #SBATCH --gres=gpu:teslak80:1    ## one K80 requested

   module load cuda

   ## Start the MPS server
   CUDA_MPS_LOG_DIRECTORY=nvidia-mps srun --gres=gpu:1 nvidia-cuda-mps-control -d&

   ## run my GPU accelerated executable
   srun --gres=gpu:1  $WRKDIR/my_gpu_binary

   ## Shut down the MPS server
   echo "quit" | nvidia-cuda-mps-control


CUDA samples
------------

There are CUDA code samples provided by Nvidia that can be useful for a
sake of testing or getting familiar with CUDA. Placed
at ``$CUDA_ROOT/samples``. To play with:

::

    $ sinteractive -t 1:00:00 --gres=gpu:1
    $ module load cuda
    $ cp -r $CUDA_ROOT/samples $WRKDIR
    $ cd $WRKDIR/samples
    $ make TARGET_ARCH=x86_64
    $ ./bin/x86_64/linux/release/deviceQuery
    ...
    $ ./bin/x86_64/linux/release/bandwidthTest
    ...

Attachments and useful links
============================

* `CUDA C Programming
  Guide <https://developer.download.nvidia.com/compute/DevZone/docs/html/C/doc/CUDA_C_Programming_Guide.pdf>`__
* `CUDA Zone on
  NVIDIA <https://developer.nvidia.com/category/zone/cuda-zone>`__
* `CUDA FAQ <https://developer.nvidia.com/cuda/cuda-faq>`__
