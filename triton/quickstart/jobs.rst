=========================
Submitting jobs on Triton
=========================

.. admonition:: Prerequisites

    Optimally, before submitting a job: do enough tests and have a rough idea, how long your job takes, how much memory it needs and how much CPU(s)/GPU(s) it needs. Required Reading:

    - :doc:`Use Policy<../usagepolicy>`
    - :doc:`Acknowledging Triton<../acknowledgingtriton>`
    - :doc:`Loading Applications and libraries<../tut/applications>`

    Required Setup:

    - Setting up your System to connect to Triton according to the :doc:`connection guide <connecting>`
    - Your script and any data need to be on Triton (follow e.g. the :doc:`data transfer quick-start guide <data>`)

Types of jobs:
==============


Triton uses the Slurm scheduling system to allocate resources, like computer nodes, memory on the nodes, GPUs etc,
to the submitted jobs. For more details on Slurm, have a look `here <https://slurm.schedmd.com/>`_.
In this quickstart guide, we will only introduce the most important parameters, and skip over a lot of details.
There are multiple different types of jobs available on Triton. Here we focus on the most commonly used ones.

- Interactive jobs (commonly to test things or run graphical platforms with cluster resources)
- Batch jobs (normal jobs submitted to the cluster without direct user input)

to run an interactive connect to Triton and job simply run
::

    sinteractive

from the command line. You will then be connected to a free node, and can run your interactive session. More details can be found
in the tutorial :doc:`for interactive jobs<../tut/interactive>`.
If you have a specific command that you want to run you can also use:

::

    srun your_command

The most common job to run is a batch job, i.e. you submit a script that runs your code on the cluster.
To run this kind of job, you need a small script where you set parameters for the job and submit it to the cluster.
Using a script to set the parameters has the advantage that it is
easier to modify and reuse than passing the parameters on the command line.
A basic script (e.g. in the file ``BatchScript.slurm``) for a slurm batch job could look as follows:

.. code:: slurm

    #!/bin/bash
    #SBATCH --time=04:00:00
    #SBATCH --mem=2G
    #SBATCH --output=ScriptOutput.log

    module load scicomp-python-env
    srun python /path/to/script.py


To run this script use the command ``sbatch BatchScript.slurm``.

So, let us go through this script:

| ``#SBATCH --time=04:00:00`` asks for a 4 hour time slot, after which the job will be stopped.
| ``#SBATCH --mem=2G`` asks for 2Gb of memory for your job.
| ``#SBATCH --output=ScriptOutput.log`` sets the terminal output of the job to the specified file.
| ``module load scicomp-python-env`` tells the node you run on to load Python environment module.
| ``srun python /path/to/script`` tells the cluster to run the command ``python /path/to/script.py``

Most programming languages and tools have their own modules that need to be loaded before they can be run. You can get a list of available
modules by running ``module spider``. If you need a specific version of a module, you can check the available versions by running ``module spider MODULENAME``
(e.g. ``module spider r`` for ``R``). To load a specific version you have to specify this version during the load command (e.g. ``module load matlab/r2023b``
for the 2023b release of MATLAB). For further details please have a look at the :ref:`instructions for the specific application <application-list>`

There are plenty more parameters that you can set for the slurm scheduler as well (for a detailed list can be found `here <https://slurm.schedmd.com/pdfs/summary.pdf>`__),
but we are not going to discuss them in detail here, since they are likely not necessary for your first job.
