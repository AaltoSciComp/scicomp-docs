=============
GPU computing
=============

.. include:: /triton/ref/videos.rst

.. admonition:: Abstract

   * Request a GPU with the Slurm option ``--gpus=1`` or
     ``--gres=gpu:0`` (some clusters need ``--partition=gpu`` or similar).
   * Select a certain type of GPU with e.g. ``--constraint='volta'``
     (see :doc:`the quick reference for names <../ref/index>`).
   * Monitor GPU performance with ``sacct -j JOBID -o comment -p``.
   * You can test out small jobs of 30 minutes or less in the
     ``gpu-debug``-partition (``--partition=gpu-debug``).
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

Slurm keeps track of the GPU resources as generic resources (GRES) or
trackable resources (TRES). They are basically limited resources that you
can request in addition to normal resources such as CPUs and RAM.

To request GPUs on Slurm, you should use the ``--gpus=1`` or ``--gres=gpu:1``
-flags.

You can also use syntax ``--gpus=GPU_TYPE:1`` (or ``--gres=gpu:GPU_TYPE:1``),
where ``GPU_TYPE`` is a name chosen by the admins for the GPU.
For example, ``--gpus=v100:1`` would give you a V100 card. See section on
:ref:`reserving specific GPU architectures <gpu-constraint>` for more information.

You can request more than one GPU with ``--gpus=G``, where ``G`` is
the number of the requested GPUs.

Some GPUs are placed in a quick debugging queue. See section on
:ref:`reserving quick debugging resources <gpu-debug>` for more
information.

.. note::

   Most GPU programs cannot utilize more than one GPU at a time. Before
   trying to reserve multiple GPUs you should verify that your code
   can utilize them.



Running an example program that utilizes GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../ref/examples-repo.rst

For this example, let's consider
`pi-gpu.cu <https://github.com/AaltoSciComp/hpc-examples/blob/master/slurm/pi-gpu.cu>`__
in the ``slurm``-folder. 
It estimates pi with Monte Carlo methods and can utilize a GPU for calculating
the trials.

The script is in the ``slurm``-folder. This example is written in C++ and CUDA.
Thus it needs to be compiled before it can be run.

To compile CUDA-based code for GPUs, lets load a ``cuda``-module and
a newer compiler:

.. code-block:: bash

   module load gcc/12.3.0 cuda/12.2.1

Now we should have a compiler and a CUDA toolkit loaded. After this
we can compile the code with:

.. code-block:: bash

   nvcc -arch=sm_60 -gencode=arch=compute_60,code=sm_60 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_90,code=sm_90 -o pi-gpu slurm/pi-gpu.cu

This monstrosity of a command is written like this because we want our code
to be able run on multiple different GPU architectures. For more information,
see section on
:ref:`setting compilation flags for GPU architectures <cuda-arch-flags>`.

Now we can run the program using ``srun``:

.. code-block:: bash

   srun --time=00:10:00 --mem=500M --gpus=1 ./pi-gpu 1000000

This worked because we had the correct modules already loaded.
Using a slurm script setting the requirements and loading the correct modules becomes easier:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:10:00
   #SBATCH --mem=500M
   #SBATCH --output=pi-gpu.out
   #SBATCH --gpus=1

   module load cuda/12.2.1
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
using the ``--constraint`` option.  For example, to restrict the submission to
Pascal generation GPUs only you can use ``--constraint='pascal'``.

For choosing between multiple generations, you can use the ``|``-character
between generations. For example, if you want to restrict the submission
Volta or Ampere generations you can use ``--constraint='volta|ampere'``.
Remember to use the quotes since ``|`` is the shell pipe.

To see what GPU resources are available, run ``slurm features`` or
``sinfo -o '%50N %18F %26f %30G'``.

Alternative way is to use syntax ``--gres=gpu:GPU_TYPE:1``, where ``GPU_TYPE``
is a name chosen by the admins for the GPU. For example, ``--gres=gpu:v100:1``
would give you a V100 card.

.. _gpu-debug:

Reserving resources from the short job queue for quick debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a ``gpu-debug``-partition that you can use to run short jobs
(30 minutes or less) for quick tests and debugging. Use
``--partition=gpu-debug`` for this.

.. _cuda-missing:

CUDA libraries not found
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/cuda_drivers.png
   :width: 100%
   :align: center

   CUDA toolkit is usually installed separately to CUDA drivers

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many GPU codes come with precompiled kernels, but in some
cases you might need to compile your own kernels. When this is
the case you'll want to give the compiler flags that make it
possible to run the code on multiple different GPU architectures.

For GPUs in Triton these flags are:

.. code-block:: make

   -arch=sm_60 -gencode=arch=compute_60,code=sm_60 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_90,code=sm_90

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

For more information on suggested data loading procedures
for different frameworks, see
`Tensorflow's <https://www.tensorflow.org/guide/data_performance>`__
and
`PyTorch's <https://pytorch.org/docs/stable/data.html>`__ guides
on efficient data loading.

.. _cuda-nvprof:

Profiling GPU usage with nvprof
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: NVIDIA has a new profiling suite called Nsight Compute

   ``nvprof`` has been superceded by a tool called ``ncu``, which
   is a command line interface (CLI) for
   `NVIDIA Nsight Compute suite <https://docs.nvidia.com/nsight-compute/index.html>`__.
   We'll produce more up-to-date profiling examples in the future.

When using NVIDIA's GPUs you can try to use a profiling tool
called ``nvprof`` to monitor what took most of the GPU's
time during the code's execution.

Sample output might look something like this:

.. code-block:: bash

    ==30251== NVPROF is profiling process 30251, command: ./pi-gpu 1000000000
    ==30251== Profiling application: ./pi-gpu 1000000000
    ==30251== Profiling result:
                Type  Time(%)      Time     Calls       Avg       Min       Max  Name
     GPU activities:   84.82%  11.442ms         1  11.442ms  11.442ms  11.442ms  throw_dart(curandStateXORWOW*, int*, unsigned long*)
                       14.70%  1.9833ms         1  1.9833ms  1.9833ms  1.9833ms  setup_rng(curandStateXORWOW*, unsigned long)
                        0.30%  40.704us         1  40.704us  40.704us  40.704us  [CUDA memcpy DtoH]
                        0.17%  23.328us         1  23.328us  23.328us  23.328us  [CUDA memcpy HtoD]
          API calls:   89.52%  122.81ms         3  40.936ms  3.6360us  122.70ms  cudaMalloc
                       10.05%  13.794ms         2  6.8969ms  68.246us  13.726ms  cudaMemcpy
                        0.20%  269.55us         3  89.851us  11.283us  130.45us  cudaFree
                        0.14%  196.08us       101  1.9410us     122ns  83.854us  cuDeviceGetAttribute
                        0.04%  57.228us         2  28.614us  6.3760us  50.852us  cudaLaunchKernel
                        0.02%  32.426us         1  32.426us  32.426us  32.426us  cuDeviceGetName
                        0.01%  13.677us         1  13.677us  13.677us  13.677us  cuDeviceGetPCIBusId
                        0.01%  10.998us         1  10.998us  10.998us  10.998us  cudaGetDevice
                        0.00%  2.3540us         1  2.3540us  2.3540us  2.3540us  cudaGetDeviceCount
                        0.00%  1.2690us         3     423ns     207ns     850ns  cuDeviceGetCount
                        0.00%     663ns         2     331ns     170ns     493ns  cuDeviceGet
                        0.00%     656ns         1     656ns     656ns     656ns  cuDeviceTotalMem
                        0.00%     396ns         1     396ns     396ns     396ns  cuModuleGetLoadingMode
                        0.00%     234ns         1     234ns     234ns     234ns  cuDeviceGetUuid


This output shows that most of the computing time was caused by calling the
``throw_dart``-kernel. It is important to note that in this example memory
allocation ``cudaMalloc`` and memory copying ``cudaMemcpy`` used more time than
the actual computation. Memory operations are time consuming operations and thus
best codes try to minimize the need for doing them.

To see a chronological order of different GPU operations one can also run
``nprof --print-gpu-trace``. The output will look something like this:

.. code-block:: bash

    ==31050== NVPROF is profiling process 31050, command: ./pi-gpu 1000000000
    ==31050== Profiling application: ./pi-gpu 1000000000
    ==31050== Profiling result:
       Start  Duration            Grid Size      Block Size     Regs*    SSMem*    DSMem*      Size  Throughput  SrcMemType  DstMemType           Device   Context    Stream  Name
    182.84ms  23.136us                    -               -         -         -         -  256.00KB  10.552GB/s    Pageable      Device  Tesla P100-PCIE         1         7  [CUDA memcpy HtoD]
    182.89ms  1.9769ms            (512 1 1)       (128 1 1)        31        0B        0B         -           -           -           -  Tesla P100-PCIE         1         7  setup_rng(curandStateXORWOW*, unsigned long) [118]
    184.87ms  11.450ms            (512 1 1)       (128 1 1)        19        0B        0B         -           -           -           -  Tesla P100-PCIE         1         7  throw_dart(curandStateXORWOW*, int*, unsigned long*) [119]
    196.33ms  40.704us                    -               -         -         -         -  512.00KB  11.996GB/s      Device    Pageable  Tesla P100-PCIE         1         7  [CUDA memcpy DtoH]
    
    Regs: Number of registers used per CUDA thread. This number includes registers used internally by the CUDA driver and/or tools and can be more than what the compiler shows.
    SSMem: Static shared memory allocated per CUDA block.
    DSMem: Dynamic shared memory allocated per CUDA block.
    SrcMemType: The type of source memory accessed by memory operation/copy
    DstMemType: The type of destination memory accessed by memory operation/copy

Here we see that the sample code did a memory copy to the device, ran kernel ``setup_rng``,
ran kernel ``throw_dart`` and did a memory copy back to the host memory.

For more information on ``nvprof``, see `NVIDIA's documentation on it <https://docs.nvidia.com/cuda/profiler-users-guide/index.html#nvprof>`__.

Available GPUs and architectures
--------------------------------

.. include:: ../ref/gpu.rst



Exercises
---------

.. include:: ../ref/examples-repo.rst

.. exercise:: GPU 1: Test nvidia-smi

   Run ``nvidia-smi`` on a GPU node with ``srun``. Use ``slurm history``
   to check which GPU node you ended up on.

.. exercise:: GPU 2: Running the example

   Run the example given above with larger number of trials
   (``10000000000`` or :math:`10^{10}`).

   Try using ``sbatch`` and Slurm script as well.

.. exercise:: GPU 3: Run the script and do basic profiling with nvprof

   ``nvprof`` is part of NVIDIA's profiling tools and it can be
   used to monitor which parts of the GPU code use up most time.

   Run the program as before, but add ``nvprof`` before it.

   Try running the program with chronological trace mode
   (``nvprof --print-gpu-trace``) as well.

   .. solution::

      With ``srun`` you can run the profiling as follows:

      .. code-block:: bash

         srun --time=00:10:00 --mem=500M --gres=gpu:1 nvprof ./pi-gpu 10000000000

      To get the trace output, you need to add the ``--print-gpu-trace``-flag:

      .. code-block:: bash

         srun --time=00:10:00 --mem=500M --gres=gpu:1 nvprof --print-gpu-trace ./pi-gpu 10000000000

      You should see output similar to ones shown in the section
      :ref:`profiling GPU usage with nvprof <cuda-nvprof>`.

.. exercise:: GPU 4: Your program

   Think of your program. Do you think it can utilize GPUs?

   If you do not know, you can check the program's documentation for words such as:

   - GPU
   - CUDA
   - ROCm
   - OpenMP offloading
   - OpenACC
   - OpenCL
   - ...


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
