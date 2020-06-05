=============
GPU computing
=============

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

   You can see the main article: :doc:`../usage/gpu` for more
   detailed information.

GPU jobs
--------

To request GPUs on Slurm, you should use the ``--gres`` option either in
your batch script or as a command-line argument to your interactive job.
Used with a SBATCH directive in a batch script, exactly one  GPU is
requested as follows. ::

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

We support the following machine learning frameworks out of the box:

* :doc:`Tensorflow <../apps/tensorflow>`:
  ``module load anaconda/2020-02-tf2``.
  See the Tensorflow page for info on older versions.
* Keras: ``module load anaconda/2020-02-tf2``
* PyTorch:``module load anaconda/2020-02-tf2``
* :doc:`Detectron <../apps/detectron>`: via :doc:`singularity images <../usage/singularity>`
* CNTK: via :doc:`singularity images <../usage/singularity>`

Please note that most of the pre-installed softwares have CUDA already present.
Thus you **do not need to load CUDA** as a seperate module when loading these.
See the :ref:`application list <application-list>` or :doc:`GPU
computing reference <../usage/gpu>` for more details.

Compiling CUDA-based code
-------------------------

To compile CUDA-based code for GPUs, you need to load the relevant ``cuda``
module. You can see what versions of CUDA is available using ``module spider``::

   module spider cuda

When submitting a batch script, you need to load the ``cuda`` module,
compile your code, and subsequently run the executable.
An example of such a submission script is shown below wherein the
output of the code is written to a file named ``hello.out``
in the current directory::

   #!/bin/bash
   #SBATCH --time=00:35:00
   #SBATCH --job-name=gpuTest
   #SBATCH --mem-per-cpu=500M
   #SBATCH --cpus-per-task=2
   #SBATCH --gres=gpu:1
   #SBATCH --output=hello.out

   module load cuda
   nvcc helloworld.cu -o helloworld
   ./helloworld

.. note::

   If you ever get ``libcuda.so.1: cannot open shared object file: No such
   file or directory``, this means you are attempting to use a CUDA
   program on a node without a GPU.  This especially happens if you try
   to test GPU code on the login node, and happens (for example) even if
   you try to import the GPU ``tensorflow`` module in Python on the login
   node.

Examples
---------

.. include:: ../examples/tensorflow/tensorflow_mnist.rst

.. include:: ../examples/pytorch/pytorch_mnist.rst

.. include:: ../examples/cntk/cntk_mnist.rst

Monitoring efficient use of GPUs
--------------------------------

When running a GPU job, you should check that the GPU is being fully
utilized. Additionally, for the sake of troubleshooting and ensuring
that GPU is executing your code, not GPUs, you can run an interactive job::

   sinteractive --gres=gpu:1 --time=1:00:00 --mem=1G -c 3

When assigned a node in the GPU partition, you can ``ssh`` to the node
and run ``nvidia-smi``. You can find your process by e.g. using ``htop``
and inspect the ``GPU-Util`` column. It should be close to 100%.


Once the job has finished, you can use ``slurm history`` to obtain the
``jobID`` and run::

   sacct -j <jobID> -o comment -p

This also shows the GPU utilization.

.. note::

   There are factors to be considered regarding efficient use of GPUs.
   For instance, is your code itself efficient enough? Are you using the
   framework pipelines in the intended fashion? Is it only using GPU
   for a small portion of the entire task?  `Amdahl's law
   <https://en.wikipedia.org/wiki/Amdahl's_law>`__ of parallelization
   speedup is relevant here.

Monitoring CPUs
~~~~~~~~~~~~~~~

If the GPU utilization of your jobs are low, you can do
the ``seff <jobID>`` command and see if the CPU utilization is 100%.
This could mean that the GPUs are not able to supply data fast enough.

Please keep in mind that when using a GPU, you need to also
request enough CPUs to supply the data to the process.
So, you can increase the number of CPUs you request so that
enough data is provided for the GPU. However, you shouldn't request
too many: There wouldn't be enough CPUs for everyone to use the GPUs,
and they would go to waste (For the K80 nodes, we have only 1.5 CPUs per
GPU, but on all others we have 4-6 CPUs/GPU).

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

1. Run ``nvidia-smi`` on a GPU node with ``srun``. Use ``slurm history``
   to check which GPU node you ended up on. Try setting a constraint
   to force a different GPU architecture.

2. Copy ``/scratch/scip/hpc-examples/gpu/pi.cu`` to your work directory.
   Compile it using ``cuda`` module and ``nvcc``. Run it. Does it say zero?
   Try running it with a GPU and see what happens.

3. Run one of the samples given above. Try using ``sbatch`` as well.

4. Modify CTNK sample slurm script in a way that it copies datasets to
   an unique folder in ``/dev/shm`` or ``$TMPDIR`` before running the
   Python code. Modify CNTK sample so that it loads data from the new
   location.

   HINT: Check out ``mktemp --help``,
   :ref:`command output substitutions <linux-training-substitute-command-output>`-section
   from our Linux shell tutorial and the API page for Python's
   `os.environ <https://docs.python.org/3/library/os.html#os.environ>`_.

   Solution to ex. 4:
   :download:`cntk_mnist_ex4.py</triton/examples/cntk/cntk_mnist_ex4.py>`
   :download:`cntk_mnist_ex4.sh</triton/examples/cntk/cntk_mnist_ex4.sh>`.

What's next?
------------

Check out our :doc:`reference information <../usage/gpu>` about GPU
computing, including examples of different machine learning frameworks.

This guide assumes you are using pre-existing GPU programs.  If you
need to write your own, that's a whole other story, and you can find
some hints on the reference page.
