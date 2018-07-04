=============
GPU Computing
=============

This is the reference page.  There is also the :doc:`basic GPU
tutorial <../tut/gpu>` which you should read first.

Overview
========

Triton has GPU cards from four different Nvidia generations, as
described below.

Hardware breakdown
==================

.. csv-table::
   :delim: |

   Card          | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability   | Slurm gres name  | Slurm feature name
   Tesla M2090   | 22             | gpu[1-11]    | Fermi          | 512                       | 6G                | 2.0                       | ``m2090``        | ``fermi``
   Tesla M2070   | 6              | gpu[17-19]   | Fermi          | 448                       | 6G                | 2.0                       | ``m2070``        | ``fermi``
   Tesla M2050   | 10             | gpu[12-16]   | Fermi          | 448                       | 3G                | 2.0                       | ``m2050``        | ``fermi``
   Tesla K80\*   | 12             | gpu[20-22]   | Kepler         | 2x2496                    | 2x12GB            | 3.7                       | ``teslak80``     | ``kepler``
   Tesla P100    | 20             | gpu[23-27]   | Pascal         | 3854                      | 16GB              | 6.0                       | ``teslap100``    | ``pascal``
   Tesla V100    | 16             | dgx[01-02]   | Volta          | 5120                      | 16GB              | 7.0                       | ``v100``         | ``volta``

* Note: Tesla K80 cards are in essence two GK210 GPUs on a single chip
* Note: V100 cards are part of DGX machines, which were purchased by
  several groups and are currently special access only.  They are also a
  different operating system, please see :doc:`dgx`.

Detail info about cards available at
http://en.wikipedia.org/wiki/Nvidia_Tesla and for general info about
Nvidia GPUs
http://www.nvidia.com/object/tesla-supercomputing-solutions.html

Using GPU nodes
===============

GPU partitions
--------------

There are two queues governing these nodes: ``gpu`` and ``gpushort``, where the
latter is for jobs up to 4 hours.

The latest details can always be found with the following command::

    $ slurm p | grep gpu

GPU node allocation
-------------------

For gpu resource allocation one has to request a GPU resource, with
``--gres=gpu:N`` , where ``N``
stands for number of requested GPU cards. To request a specific card,
one must use syntax  ``--gres=gpu:CARD_TYPE:N`` ,  see 'Slurm feature
name' in the table above.

::

    --gres=gpu:2
    --gres=gpu:teslak80:1

For the full current list of configured SLURM gpu cards names run
``slurm features``.

Note: Before summer 2016, you also had to specify a GPU partition with
``-p gpu`` or ``-p gpushort``.  Now, this is automatically detected
and the recommendation is to leave it off.

When using multiple GPU's please verify that the code actually uses them with
instructions given in `Monitoring GPU usage`_.

GPU nodes environment and CUDA
------------------------------

User environment on ``gpu*`` nodes is the same as on other nodes, the
only difference is that they have nvidia kernel modules for Tesla cards.
`CUDA <http://www.nvidia.com/object/cuda_home_new.html>`__ comes through
``module``.

::

    $ module avail CUDA    # list installed CUDA modules
    $ module load CUDA/7.5.18   # load CUDA environment that you need
    $ nvcc --version   # see actual CUDA version that you got

Running a GPU job in serial
---------------------------

Quick interactive run

::

    $ module load CUDA
    $ srun -t 00:30:00 --gres=gpu:1 $WRKDIR/my_gpu_binary

Allocating a gpu node for longer interactive session, this will give you
a shell sessions

::

    $ module load CUDA
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

    module load CUDA

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
    $ module load CUDA                        # set CUDA environment
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
Guide <http://developer.download.nvidia.com/compute/DevZone/docs/html/C/doc/cuda-gdb.pdf>`__
for a more information on cuda-gdb.

Applications and known issues
=============================

nvidia-smi utility
------------------

Could be useful for debugging, in case one want to see the actual gpu
cards available on the node. If this command returns an error, it is
time to report that something is wrong on the node.

::

    gpuxx$ nvidia-smi -L   # gives a list of GPU cards on the node

cuDNN
-----

``cudnn`` is available as a module. The latest version can be found with
``module spider cudnn``. Note that (at least the later versions of)
cudnn require newer cards and cannot be used on the old fermi cards.
E.g. tensorflow does not run on the older fermi cards for this reason.

Tensorflow example
------------------

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
    #SBATCH --gres=gpu:teslak80:4
    #SBATCH --mem-per-cpu 10G
    #SBATCH -t 4:00:00

    module load anaconda2 CUDA/7.5.18 cudnn/4
    source activate tensorflow

    python -m tensorflow.models.image.cifar10.cifar10_multi_gpu_train --num-gpus 4

You can submit this job with

::

    $ sbatch submit_cifar.sh

and you'll be able to find the results in the slurm log file.

Theano configuration
--------------------

If you're using the theano library, you need to tell theano to store
compiled code on the local disk on the compute node. Create a file
``~/.theanorc`` with the contents

::

    [global]
    base_compiledir=/tmp/%(user)s/theano

Also make sure that in your batch job script you create this directory
before you launch theano. E.g.

::

    mkdir -p /tmp/${USER}/theano

The problem is that by default the ``base_compiledir`` is in your home
directory (``~/.theano/``), and then if you first happen to run a job on a
newer processor, a later job that happens to run on an older processor
will crash with an "Illegal instruction" error.


Nvidia MPS
----------

`Nvidia Multi-Process Service (MPS)
<http://docs.nvidia.com/deploy/mps/index.html>`__ provides a way to
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

   module load CUDA

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
at ``$CUDA_HOME/samples``. To play with:

::

    $ sinteractive -t 1:00:00 --gres=gpu:1
    $ module load CUDA
    $ cp -r $CUDA_HOME/samples $WRKDIR
    $ cd $WRKDIR/samples
    $ make TARGET_ARCH=x86_64
    $ ./bin/x86_64/linux/release/deviceQuery
    ...
    $ ./bin/x86_64/linux/release/bandwidthTest
    ...

Attachments and useful links
============================

* `CUDA C Programming
  Guide <http://developer.download.nvidia.com/compute/DevZone/docs/html/C/doc/CUDA_C_Programming_Guide.pdf>`__
* `CUDA Zone on
  NVIDIA <http://developer.nvidia.com/category/zone/cuda-zone>`__
* `CUDA FAQ <http://developer.nvidia.com/cuda/cuda-faq>`__
