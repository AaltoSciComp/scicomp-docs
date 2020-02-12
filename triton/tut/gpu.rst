=============
GPU computing
=============

.. seealso::

   This tutorial assumes you have read :doc:`interactive`.

   Main article: :doc:`../usage/gpu`

.. highlight:: bash

GPUs and accelerators are basically very special parallel processors:
they can apply the same instructions to a big chunk of data at the
same time.  The speedup can be  100x or more... but only in the
specific cases where your code fits the model.  It happens that
machine learning/deep learning methods are able to use this type of
parallelism, so now these are the standard for this type of research.

On Triton, we have a large number of NVIDIA GPU cards from different
generations, and are constantly getting more.  Our GPUs are not your
typical desktop GPUs, but specialized research-grade server GPUs with
large memory, high bandwidth and specialized instructions. For
scientific purposes they generally exceed the best desktop GPUs.

Some nomenclature: a GPU is a graphical processing unit, CUDA is the
software interface for Nvidia GPUs. Currently we only support CUDA.


Getting started
---------------

GPUs are, just like anything, resources which are scheduled by slurm.
So in addition to time, memory, and CPUs, you have to specify how many
GPUs you want.  This is done with the ``--gres`` (generic resources)
option::

  srun --gres=gpu:1 $my_code

This means you request the ``gpu`` resources, and one of them
(``1``).  Combining this with the other required slurm options::

  srun --gres=gpu:1 -t 2:00:00 --mem=10G -c 3

... and you've got yourself the basics.  Of course, once you are ready
for serious runs, you should put your code into :doc:`slurm scripts <serial>`.

If you want to restrict yourself to a certain type of card, you should
use the ``--constraint`` option.  For example, to restrict to Kepler
generation (K80s), use ``--constraint=kepler`` or all new cards,
``--constraint='pascal|volta'`` (note the quotes - this is very
important, because ``|`` is a shell pipe symbol!).

Our available GPUs and architectures:

.. include:: ../ref/gpu.rst

Ready software
--------------

We support these machine learning packages out of the box:

* :doc:`Tensorflow <../apps/tensorflow>`:
  ``anaconda`` module.  Use ``--constraint='kepler|pascal|volta'``.
  See the Tensorflow page for info on older versions.
* Keras: same module as tensorflow
* PyTorch: same module as tensorflow
* :doc:`Detectron <../apps/detectron>`: via :doc:`singularity images <../usage/singularity>`
* CNTK: via :doc:`singularity images <../usage/singularity>`

Do note that most of the pre-installed software has CUDA already present.
Thus you **do not need to load CUDA** as a module when loading these.
See the :ref:`application list <application-list>` or :doc:`GPU
computing reference <../usage/gpu>` for more details.

Compiling code yourself
-----------------------

To compile things for GPUs, you need to load the relevant ``CUDA``
modules::

  module avail cuda
  module load gcc
  module load cuda

  nvcc cuda_code.cu -o cuda_code         # compile your CUDA code

More information is in the :doc:`reference <../usage/gpu>`, but most
people will use pre-built software through channels such as Anaconda
for Python.

Making efficient use of GPUs
----------------------------

When running a job, you want to check that the GPU is being fully
utilized.  To do this, ssh to your node (while the job is running),
and run ``nvidia-smi``, find your process (which might take some work)
and check the ``GPU-Util`` column.  It should be close to 100%,
otherwise see below.

After job has finished, you can use ``slurm history`` to obtain the
``JobID`` and run::

   sacct -j INSERT_JOBID_HERE -o comment -p

This will show the GPU utilization.  If this is low, then what?  Check
the normal ``seff`` command and see if the CPU utilization is 100%.
This could mean that the GPUs are not able to supply data fast enough,
see the section on CPUs below.  Similarly, your code may not be able
to load data fast enough, see the input/output section below.

Also, is your code itself efficient enough?  Are you using the
framework pipelines the way they should work?  Is it only using GPU
for a small portion of the entire task?  `Amdahl's law
<https://en.wikipedia.org/wiki/Amdahl's_law>`__ of parallelization
speedup is relevant here.

Enough CPUs
~~~~~~~~~~~

When using a GPU, you need to also request enough CPUs to supply the
data to the process.  So, increase the number of CPUs you request so
that you can provide the GPU with enough data.  However, don't request
too many: then, there aren't enough CPUs for everyone to use the GPUs,
and they go to waste!  (For the K80 nodes, we have only 1.5 CPUs per
GPU, but on all others we have 4-6 CPUs/GPU)

Input/output
~~~~~~~~~~~~

Deep learning work is intrinsically very data-hungry.  Remember what
we said about storage and input/output being important before
(:doc:`in the storage tutorial <storage>`)?  Now
it's really important.  In fact, faster memory bandwidth is the main
improvement of our server-grade GPUs compared to desktop models.

If you are loading lots of data, package the data into a container
format first: lots of small files are your worst enemy, and we have a
:doc:`dedicated page on small files <../usage/smallfiles>`.  Each
framework has a way to do this efficiently in a whole pipeline.

If your dataset consists of individual files and it is not too big,
it is a good idea to have the data stored in one file, which is then
copied to nodes ramdisk ``/dev/shm`` or temporary disk ``/tmp``.

If your data is too big to fit to the disk, we recommend that you
contact us for efficient data handling models.

Other
~~~~~

Most of the time, using more than one GPU isn't worth it, unless you
specially optimize, because communication takes too much time.  It's
better to parallelize by splitting tasks into different jobs.

FAQ
---

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

Exercises
---------

1. Run ``nvidia-smi`` on a GPU node with ``srun``. Use ``slurm history``
   to check which GPU node you ended up on. Try setting a constraint
   to force a different GPU architecture.

2. Copy ``/scratch/scip/examples/gpu/pi.cu`` to your work directory.
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

Next steps
----------

Check out or :doc:`reference information <../usage/gpu>` about GPU
computing, including examples of different machine learning languages.

If you came straight to this page, you should also read
:doc:`interactive` and :doc:`serial` (actually you should have read
them first, but don't worry).

This guide assumes you are using pre-existing GPU programs.  If you
need to write your own, that's a whole other story, and you can find
some hints on the reference page.
