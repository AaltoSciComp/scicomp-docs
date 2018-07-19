=============
GPU computing
=============

.. note::

   This page is still under development.

.. highlight:: bash

GPUs and accelerators are basically very special parallel processors:
they can apply the same instructions to lots of different data at the
same time.  You can get a speedup of 100x or more... but only in the
specific cases where your code fits the model.  It happens that
machine learning/deep learning methods are able to use this type of
parallelism, so now these are the standard for this type of research.

On Triton, we have a large number of Nvidia GPU cards of different
generations, and are constantly getting more.  Our GPUs are not for
desktops, but specialized research-grade server GPUs with large
memory, high bandwidth, and for scientific purposes generally
exceed the best desktop GPUs.

Some nomenclature: a GPU is a graphical processing unit, CUDA is the
software interface for Nvidia GPUs.  (we only support CUDA)



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
``--constraint='kepler|pascal'`` (note the quotes - this is very
important, because ``|`` is a shell pipe symbol!).

Note: before summer 2016, you also had to specify a GPU partition
(``-p gpu`` or ``-p gpushort``).  Now, this is automatically detected,
and the recommendation is to leave this off.

Our available GPUs and architectures:

.. include:: ../ref/gpu.rst



Ready software
--------------

We support these machine learning packages out of the box:

* tensorflow: ``anaconda2`` / ``anaconda3`` modules.  Use ``--constraint='kepler|pascal|volta'``
* keras: same as tensorflow
* pytorch: same module as tensorflow
* Detectron: via :doc:`singularity images <../apps/singularity>`
* CNTK:
* Torch: currently possibly but not easy, in the future through singularity

See the :doc:`GPU computing reference <../usage/gpu>` page for more
details.




Compiling code yourself
-----------------------

To compile things for GPUs, you need to load the relevant ``CUDA``
modules::

  module avail CUDA
  module load CUDA

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

Input/output
~~~~~~~~~~~~

Deep learning work is intrinsically very data-hungry.  Remember what
we said about storage and input/output being important before
(:doc:`in the storage tutorial <storage>`)?  Now
it's really important.  In fact, faster memory bandwidth is the main
improvement of our server-grade GPUs compared to desktop models.

If you are loading lots of data, package the data into a container
format first: lots of small files are your worst enemy, and we have a
:doc:`dedicated page on small files <../usage/smallfiles>`.

Enough CPUs
~~~~~~~~~~~

When using a GPU, you need to also request enough CPUs to supply the
data to the process.  So, increase the number of CPUs you request so
that you can provide the GPU with enough data.  However, don't request
too many: then, there aren't enough CPUs for everyone to use the GPUs,
and they go to waste!  (For the K80 nodes, we have only 1.5 CPUs per
GPU, but on all others we have 6 CPUs/GPU)

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



Exercises
---------

In ``triton-examples`` (at ``/scratch/scip/examples`` and also on
github), you find some examples:

1. Compile and run using ``srun`` the ``gpu/pi.cu`` example.


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
