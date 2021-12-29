=============
GPU computing
=============

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=aoU1-5DjrGc&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=17>`__

.. admonition:: Generic instructions

   * Request a GPU with ``--gres=gpu:1``
   * Do not use ``srun`` in your batch script, there's a bug that
     prevents job step's access to the GPU.
   * If you use Python, generally don't load your own CUDA module
     unless you know you need this, install what you need through
     anaconda.
   * Monitor GPU performance with ``sacct -j <jobID> -o comment -p``.

Introduction
------------

GPUs, short for graphical processing unit, are massively-parallel
processors that are optimized to perform parallel operations.
Computations that might take days to run on CPUs, take substantially
less time on GPUs. This speed-up specially comes in handy when dealing
with large amounts of data, e.g. in machine learning/deep learning tasks,
which is why GPUs have become an indispensable tool in the research community.

The programs we normally write in common programming languages, e.g. C++ are
executed by the CPU. We need to explicitly communicate with the GPU if we want
GPU to execute the program. That is, upload the program and the input data to the GPU,
and transfer the result from the GPU to the main memory. What enable this procedure
are programming environments designed to communicate with GPUs in such a manner.
An example of such an API is `CUDA <https://en.wikipedia.org/wiki/CUDA>`_
which is the native programming interface for NVIDIA GPUs.

On Triton, we have a large number of NVIDIA GPU cards from different
generations and currently only support CUDA. Triton GPUs are not the
typical desktop GPUs, but specialized research-grade server GPUs with
large memory, high bandwidth and specialized instructions,
that are constantly increasing in number. For scientific purposes,
they generally outperform the best desktop GPUs.

.. seealso::

   Please ensure you have read :doc:`interactive` and :doc:`serial`
   before you proceed with this tutorial.

.. highlight:: console



GPU jobs
--------

To request GPUs on Slurm, you should use the ``--gres`` option either in
your batch script or as a command-line argument to your interactive job.
Used with a SBATCH directive in a batch script, exactly one  GPU is
requested as follows. :

.. code-block:: slurm

   #SBATCH --gres=gpu:1

You can request as many GPUs as you'd like using ``#SBATCH --gres=gpu:<n>``
wherein ``n`` denotes the number of the requested GPUs.

.. note::

   Most of the time, using more than one GPU isn't worth it, unless you
   specially optimize, because communication takes too much time.  It's
   better to parallelize by splitting tasks into different jobs.

You can restrict yourself to a certain type of GPU card by using
using the ``--constraint`` option.  For example, to restrict to Kepler
generation (K80s), use ``--constraint='kepler'`` or only Pascal or Volta
generations with ``--constraint='pascal|volta'`` (Remember to use the quotes
since ``|`` is the shell pipe)



Available machine learning frameworks
-------------------------------------

We support many common machine learning frameworks out of the box:

* :doc:`Tensorflow <../apps/tensorflow>`:
  ``module load anaconda``.
  See the Tensorflow page for info on older versions.
* Keras: ``module load anaconda``
* PyTorch:``module load anaconda``

Please note that most of the pre-installed softwares have CUDA already present.
Thus you **do not need to load CUDA** as a seperate module when loading these.
See the :ref:`application list <application-list>` for more details.



Compiling CUDA-based code
-------------------------

To compile CUDA-based code for GPUs, you need to load the relevant ``cuda``
module. You can see what versions of CUDA is available using ``module spider``::

   $ module spider cuda

When submitting a batch script, you need to load the ``cuda`` module,
compile your code, and subsequently run the executable.
An example of such a submission script is shown below wherein the
output of the code is written to a file named ``helloworld.out``
in the current directory:

.. code-block:: slurm

   #!/bin/bash
   #SBATCH --time=00:05:00
   #SBATCH --job-name=helloworld
   #SBATCH --mem-per-cpu=500M
   #SBATCH --cpus-per-task=1
   #SBATCH --gres=gpu:1
   #SBATCH --output=helloworld.out
   #SBATCH --partition=gpu

   module load cuda
   nvcc helloworld.cu -o helloworld
   ./helloworld

Using the :download:`helloworld.cu</triton/examples/gpu/helloworld.cu>`. 

.. code-block:: slurm

   #include "stdio.h"

   __global__ void cuda_hello(int* a){
           // blockIdx has values between 0 and 4
           printf("Hello World from GPU a[%d]=%d \n", blockIdx.x, a[blockIdx.x]);
   }

   int main(void) {
           int* d_a;

           // Allocates an array of 5 integers
           cudaMalloc(&d_a, 5*sizeof(int));

           // Runs 5 instances of kernel cuda_hello in parallel
           cuda_hello<<<5, 1>>>(d_a); 

           // This is needed for the printf in the kernel to display
           cudaDeviceSynchronize();

           printf("Hello from outside GPU\n");
           return 0;
   }


.. note::

   If you ever get ``libcuda.so.1: cannot open shared object file: No such
   file or directory``, this means you are attempting to use a CUDA
   program on a node without a GPU.  This especially happens if you try
   to test GPU code on the login node, and happens (for example) even if
   you try to import the GPU ``tensorflow`` module in Python on the login
   node. 

   You may also need to use ``module load CUDA``. The ``gpu`` partition will be cluster specific and can also be used as a command line argument. 



Examples
---------

.. include:: ../examples/tensorflow/tensorflow_mnist.rst

.. include:: ../examples/pytorch/pytorch_mnist.rst


Monitoring efficient use of GPUs
--------------------------------

.. include:: ../examples/monitoring/gpu.rst

Input/output
~~~~~~~~~~~~

Deep learning work is intrinsically very data-hungry.  Remember what
we said about storage and input/output being important before
(:doc:`Data storage <storage>`)? This matter becomes very important
when working with GPUs. In fact, faster memory bandwidth is the main
improvement of our server-grade GPUs compared to desktop models.

If you are loading big amounts of data, you should package
the data into a container format first; lots of small files
are your worst enemy.  Each framework has a way to do this
efficiently in a whole pipeline.

.. seealso::

   Please refer to the :doc:`small files <../usage/smallfiles>` page
   for more detailed information.

If your data consists of individual files that are not too big,
it is a good idea to have the data stored in one file, which is then
copied to nodes ramdisk ``/dev/shm`` or temporary disk ``/tmp``.

If your data is too big to fit in the disk, we recommend that you
contact us for efficient data handling models.

Available GPUs and architectures
--------------------------------

.. include:: ../ref/gpu.rst

Exercises
---------

.. include:: ../ref/examples-repo.rst

1. Run ``nvidia-smi`` on a GPU node with ``srun``. Use ``slurm history``
   to check which GPU node you ended up on. Try setting a constraint
   to force a different GPU architecture.

2. Load ``cuda`` and ``gcc`` (version less than 9) modules and
   compile the ``gpu/pi.cu`` example using ``nvcc``.
   Run it. Does it say zero? Try running it with a GPU and see what happens.

3. Run one of the samples given above. Try using ``sbatch`` as well.

4. (Advanced) The PyTorch example will try to load datasets from a folder
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
