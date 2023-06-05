=============
GPU computing
=============

.. admonition:: Video

   Watch this in our courses: `2022 February
   <https://www.youtube.com/watch?v=H1zEfxlU0M8&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=24>`__,
   `2021 January
   <https://www.youtube.com/watch?v=aoU1-5DjrGc&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=17>`__

.. admonition:: Abstract

   * Request a GPU with the Slurm option ``--gres=gpu:1`` or
     ``--gpus=1`` (some clusters need ``-p gpu`` or similar).
   * Select a certain type of GPU with e.g. ``--constraint='volta'``
     (see :doc:`the quick reference for names <../ref/index>`).
   * Monitor GPU performance with ``sacct -j JOBID -o comment -p``.
   * For development, run jobs of 4 hours or less, and they can run
     quickly in the ``gpushort`` queue.
   * If you aren't fully sure of how to scale up, contact us
     :doc:`Research Software Engineers </rse/index>` early.


.. figure:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/cluster-schematic/cluster-schematic-gpu.png
   :alt: Schematic of cluster with current discussion points highlighted; see caption or rest of lesson.

   GPU nodes allow specialized types of work to be done massively in parallel.


What are GPUs and how do they parallelise calculations?
-------------------------------------------------------

GPUs, short for graphical processing unit, are massively-parallel
processors that are optimized to perform numerical calculations in parallel.
Due to this specialisation GPUs can be substantially faster than CPUs when
solving suitable problems.

GPUs are especially handy when dealing with matrices and vectors.
This has allowed GPUs to become an indispensable tool in many research fields such
as deep learning, where most of the calculations involve matrices.

The programs we normally write in common programming languages, e.g. C++ are
executed by the CPU. To run a part of that program in a GPU the program must
do the following:

1. Specify a piece of code called a **kernel**, which contains the GPU part
   of the program and is compiled for the specific GPU architecture in use.
2. Transfer the data needed by the program from the RAM to GPU VRAM.
3. Execute the kernel on the GPU.
4. Transfer the results from GPU VRAM to RAM.

.. figure:: /images/parallel-gpu.svg
    :width: 80%
    :align: center


To help with this procedure special APIs (application programming interfaces)
have been created. An example of such an API is
`CUDA toolkit <https://en.wikipedia.org/wiki/CUDA>`__,
which is the native programming interface for NVIDIA GPUs.

On Triton, we have a large number of NVIDIA GPU cards from different
generations and a single machine with AMD GPU cards. Triton GPUs are not the
typical desktop GPUs, but specialized research-grade server GPUs with
large memory, high bandwidth and specialized instructions. For scientific purposes,
they generally outperform the best desktop GPUs.

.. seealso::

   Please ensure you have read :doc:`interactive` and :doc:`serial`
   before you proceed with this tutorial.

.. highlight:: console



Running a typical GPU program
-----------------------------

Reserving resources for GPU programs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To request GPUs on Slurm, you should use the ``--gres=gpu:1`` or ``--gpus=1``
-flags.

You can request more than one GPU with ``--gres=gpu:G``, where ``G`` is
the number of the requested GPUs.

See section
:ref:`on reserving specific GPU architectures <gpu-constraint>` and
:ref:`on reserving quick debugging resources <gpushort>` for more
advanced reservation options.

.. note::

   Most GPU programs cannot utilize more than one GPU at a time. Before
   trying to reserve multiple GPUs you should verify that your code
   can utilize them.



Running an example program that utilizes GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this example, let's consider
`pi-gpu.cu <https://github.com/AaltoSciComp/hpc-examples/blob/master/slurm/pi-gpu.cu>`__-example
from the
`hpc-examples <https://github.com/AaltoSciComp/hpc-examples>`__-repository.
It estimates pi with Monte Carlo methods and can utilize a GPU for calculating
the trials.

.. include:: ../ref/example-repo.rst

The script is in the ``slurm``-folder. This example is written in C++ and
thus it needs to be compiled before it can be run.

To compile CUDA-based code for GPUs, lets load a ``cuda``-module and
a newer compiler:

.. code-block:: bash

   module load gcc/8.4.0 cuda

Now we should have a compiler and a CUDA toolkit loaded. After this
we can compile the code with:

.. code-block:: bash

   nvcc -arch=sm_60 -gencode=arch=compute_60,code=sm_60 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_80,code=sm_80 -o pi-gpu pi-gpu.cu

This monstrosity of a command is written like this because we want our code
to be able run on multiple different GPU architectures. For more information,
see section on
:ref:`setting compilation flags for GPU architectures <cuda-arch-flags>`.

Now we can run the program using ``srun``:

.. code-block:: bash

   srun --time=00:10:00 --mem=500M --gres=gpu:1 ./pi-gpu 1000000

This worked because we had the correct modules already loaded.
Using a slurm script setting the requirements and loading the correct modules becomes easier:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:10:00
   #SBATCH --mem=500M
   #SBATCH --output=pi-gpu.out
   #SBATCH --gres=gpu:1

   module load gcc/8.4.0 cuda
   ./pi-gpu 1000000

.. note::

  If you encounter problems with CUDA libraries, see the
  :ref:`section on missing CUDA libraries <cuda-missing>`.


Special cases and common pitfalls
---------------------------------

Monitoring efficient use of GPUs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/monitoring/gpu.rst

.. _gpu-constraint:

Reserving specific GPU types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can restrict yourself to a certain type of GPU card by using
using the ``--constraint`` option.  For example, to restrict to Pascal,
use ``--constraint='pascal'`` or only Volta or Ampere
generations with ``--constraint='volta|ampere'``. Remember to use the quotes
since ``|`` is the shell pipe.

.. _gpushort:

Reserving resources from the short job queue for quick debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a ``gpushort`` partition with a time limit of 4 hours that
often has space (like with other partitions, this is automatically
selected for short jobs).  As of early 2022, it has four Tesla P100
cards in it (view with ``slurm partitions | grep gpushort``).  If you
are doing testing and development and these GPUs meet your needs, you
may be able to test much faster here. Use ``-p gpushort`` for this.

.. _cuda-missing:

CUDA libraries not found
~~~~~~~~~~~~~~~~~~~~~~~~

If you ever get ``libcuda.so.1: cannot open shared object file: No such
file or directory``, this means you are attempting to use a CUDA
program on a node without a GPU. This especially happens if you try
to test a GPU code on the login node.

Another problem that might occur is when a program will try to use
pre-compiled kernels, but the corresponding CUDA toolkit is not
available.

This might happen in you have used a ``cuda``-module to compile
the code and it is not loaded when you try to run the code.

If you're using Python, see the section on :ref:`CUDA libraries and Python <cuda-python-dl>`.

.. _cuda-python-dl:

CUDA libraries and Python deep learning frameworks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using a Python deep learning frameworks such as Tensorflow
or PyTorch you usually need to create a conda environment that
contains both the framework and CUDA framework that the framework
needs.

We recommend that you either use our centrally installed
module that contains both frameworks (more info 
:ref:`here <conda>`)
or install your own using environment using instructions
presented
:doc:`here </triton/apps/python-conda>`. These instructions
make certain that the installed framework has a corresponding
CUDA toolkit available. See the :ref:`application list <application-list>`
for more details on specific frameworks.

Please note that pre-installed software either has CUDA already
present or it loads the needed modules. Thus you
**do not need to explicitly load CUDA** from the module system when
loading these.

.. _cuda-arch-flags:

Setting CUDA architecture flags when compiling GPU codes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many GPU codes come with precompiled kernels, but in some
cases you might need to compile your own kernels. When this is
the case you'll want to give the compiler flags that make it
possible to run the code on multiple different GPU architectures.

For GPUs in Triton these flags are:

.. code-block:: make

   -arch=sm_60 -gencode=arch=compute_60,code=sm_60 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_80,code=sm_80

Here architectures (``compute_XX``/``sm_XX``) number 60, 70 and 80
correspond to GPU cards P100, V100 and A100 respectively.

For more information, you can check this
`excellent article <https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/>`__
or `CUDA documentation on the subject <https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#options-for-steering-gpu-code-generation>`__.

Keeping GPUs occupied when doing deep learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many problems such as deep learning training are data-hungry.
If you are loading large amounts of data you should make certain
that the data loading is done in an efficient manner or the GPU
will not be fully utilized.

All deep learning frameworks have their own guides on how to optimize
the data loading, but they all are some variation of:

1. Store your data in multiple big files.
2. Create code that loads data from these big files.
3. Run optional pre-processing functions on the data.
4. Create a batch of data out of individual data samples.

Tasks 2 and 3 are usually parallelized across multiple CPUs. Using
pipelines such as these can dramatically speed up the training procedure.

If your data consists of individual files that are not too big,
it is a good idea to have the data stored in one file, which is then
copied to nodes ramdisk ``/dev/shm`` or temporary disk ``/tmp``.

Avoiding small files is in general a good rule to follow. Please refer
to the :doc:`small files <../usage/smallfiles>` page for more detailed
information.

If your data is too big to fit in the disk, we recommend that you
contact us for efficient data handling models.



Available GPUs and architectures
--------------------------------

.. include:: ../ref/gpu.rst



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: GPU-1: Test nvidia-smi

   Run ``nvidia-smi`` on a GPU node with ``srun``. Use ``slurm history``
   to check which GPU node you ended up on. Try setting a constraint
   to force a different GPU architecture.

.. exercise:: GPU-2: Running a script

   Run one of the samples given above. Try using ``sbatch`` as well.

.. exercise:: (advanced) GPU-3: Local job files

   (Advanced) The PyTorch example will try to load datasets from a folder
   called ``data`` in a local folder. Modify the Slurm script so that
   the script:

   a. Creates an unique folder in ``/dev/shm`` or ``$TMPDIR`` before running the
      Python code.
   b. Moves to this folder when job is running.
   c. Runs the PyTorch-example from this location. Verify that the
      datasets are stored in the local disk.

   HINT: Check out ``mktemp --help``,
   `command output substitutions
   <https://aaltoscicomp.github.io/linux-shell/quoting-substitution-aliases/#substitute-a-command-output>`__ section
   from our Linux shell tutorial and the API page for Python's
   `os.environ <https://docs.python.org/3/library/os.html#os.environ>`_.



See also
--------

* If you aren't fully sure of how to scale up, contact us
  :doc:`Research Software Engineers </rse/index>` early.


What's next?
------------

You have now seen the basics - but applying these in practice is still
a difficult challenge!  There is plenty to figure out while combining
your own software, the Linux environment, and Slurm.

Your time is the most valuable thing you have.  If you aren't fully
sure of how to use the tools, it is much better to ask that struggle
forever.  Contact us the :doc:`Research Software Engineers
</rse/index>` early - for example in our :doc:`daily garage
</help/garage>`, and we can help you get set up well.  Then, you can
continue your learning while your projects are progressing.
