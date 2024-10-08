=======================
AI and Machine Learning 
=======================
This page is for users interested in performing machine learning or other AI-related tasks on Triton.

Working interactively with Jupyter on Triton
---------------------------------------------
Triton provides a Jupyter interface in Open OnDemand: https://ondemand.triton.aalto.fi. This service runs on CPU computing nodes and allows you to run Python code interactively. You can use it to run small-scale machine learning and other AI-related tasks.


Python environment for machine learning
----------------------------------------
Via ``module load scicomp-python-env``, you can load an Aalto Scientific Computing(ASC) managed Python environment with commonly used packages, such as PyTorch, TensorFlow, jax, etc. This is also the default kernel for Jupyter on Triton. More info on :ref:`scicomp-python-env`.
Another ASC managed Python environment is ``scicomp-llm-env`` which is meant for large language models (LLMs) tasks and includes packages like Huggingface Transformers, llama_cpp_python, vllm, langchain, fastapi,etc. 
You can also create customized :ref:`conda` for your jobs. 


Data storage and I/O for machine learning
-----------------------------------------
:doc:`Data storage and I/O <../tut/storage>` play a critical role in the performance of machine learning tasks on HPCs. Properly handling data can significantly speed up training and inference.

:doc:`Local storage <../usage/localstorage>` on computing nodes are the recommended places for I/O operations, especially for tasks that involve large datasets and require repeated data loading. Also read the section :doc:`smallfiles <../usage/smallfiles>` and :doc:`lustre <../usage/lustre>` for more information on how to handle millions of small files efficiently on Triton.

Modern machine learning frameworks such as PyTorch and TensorFlow have been implemented to take advantage of multiple CPU cores for I/O operations such as data loading. For example, try different values for --cpus-per-task in combination with using a `DataLoader <https://pytorch.org/docs/stable/data.html>`__  to see if you get a speed-up:

::

    #!/bin/bash

    #SBATCH --gpus=1                 # gpu count
    #SBATCH --ntasks=1               # total number of tasks
    #SBATCH --cpus-per-task=8        # cpu-cores per task

For more information regarding data loading, see
`Tensorflow's <https://www.tensorflow.org/guide/data_performance>`__
and
`PyTorch's <https://pytorch.org/docs/stable/data.html>`__ guides.

To save your quota, we have downloaded some datasets and large language models to the shared folder ``/scratch/shareddata/dldata``. For detailed instructions/examples, please refer to the :doc:`../apps/llms` section or our example repositories: https://github.com/AaltoRSE/ImageNetTools, https://github.com/AaltoRSE/pytorch-ddp-imagenet.


GPU-accelerated model training
-------------------------------

A typical slurm script for GPU-accelerated model training looks like this:

::

    #!/bin/bash

    #SBATCH --job-name=torch-test    # job name
    #SBATCH --ntasks=1               # total number of tasks 
    #SBATCH --cpus-per-task=8        # cpu-cores per task 
    #SBATCH --mem=40G                # total memory
    #SBATCH --gpus=1                 # number of gpus 
    #SBATCH --time=00:05:00          # time limit
    #SBATCH --mail-type=end          # send mail when job ends
    #SBATCH --mail-user=<your-email>

    module purge
    module load scicomp-python-env
    python mnist_classify.py --epochs=5


Maximizing GPU utilization is a key factor in achieving high performance on GPUs. Please read the section :ref:`gpu-occupancy` for detailed information and try out the strategies discussed there to see how GPU utilization changes.

To see how efficiently your job is using the GPU when it has started, run the command ``slurm q`` to check out the node name. SSH to that node via ``ssh <nodename>`` and then run the command ``watch -n 1 nvidia-smi`` to monitor the GPU utilization and allocated memory to the GPU. Type ``Ctrl+C`` to exit the watch command. Use the exit command ``exit`` to leave the compute node and return to the login node.

To monitor resource usage of completed/failed jobs, one can use `sacct <https://slurm.schedmd.com/sacct.html>`__.

For example, with the following command, you can see the resource usage of a job with jobid <jobid>: 
::

    sacct -j <jobid> -o TRESUsageInAve,TRESUsageInMax,MaxRSS,MaxVMSize,Elapsed,State -p

Profiling 
---------
If you want to do a more thorough analysis of your code's execution and identify performance bottlenecks to optimize resource usage, there are several tools such as ``nsys``, ``ncu`` available on triton for profiling your code, see the :ref:`gpu-profiling` section for more information regarding profiling tools and report visualization approaches.

Distributed model training
---------------------------
When you want to handle larger datasets or more complex models that can't fit into the memory of a single GPU, you can use distributed model training. In general, this will help speed up model training and scale your machine learning tasks in HPC environments. However, because more resources are required, the queue time will increase. For the time being, Triton only supports single-node, multi-GPU jobs.

A proper distributed learning run requires setting some environment variables. The official documents of most deep learning frameworks may not aim at slurm-managed cluster environments, so we have created some examples to make it easier for you to do distributed model training on Triton, such as a DDP example: https://github.com/AaltoRSE/pytorch-ddp-imagenet. The work is in progress and we will add more examples in the future. You are welcome to share your examples.


Hyperparameter searching
------------------------
A straightforward way for hyperparameter searching is using a job array. This will allow you to run multiple jobs with one sbatch command. Each job within the array trains the network using a different set of parameters. A simple example looks like this:
::

    #!/bin/bash

    #SBATCH --job-name=array_job_name
    #SBATCH --output=torch_%A_%a.out
    #SBATCH --array=0-14

    # Parameter arrays
    parameterA=(0.1 0.01 0.001)
    parameterB=(2 4 6 8 10)

    # Calculate index 
    index_A=$((SLURM_ARRAY_TASK_ID / 5))
    index_B=$((SLURM_ARRAY_TASK_ID % 5))

    # Extract the actual value based on the index
    valueA=${parameterA[$index_A]}
    valueB=${parameterB[$index_B]}

    python script.py --parameterA $valueA --parameterB $valueB


Working with large language models
----------------------------------

As mentioned above, you can find more instructions on how to use open source LLMs on its :doc:`dedicated documentation page <../apps/llms>` . For more generative AI services in Aalto, see :doc:`Generative-ai-tools </aalto/generative-ai-tools>`.


Deep learning softwares
-----------------------
If you need to use other software that can not be easily installed via conda, for example, some software that requires a specific dependency or a specific version of a dependency that is not available on triton or needs to run in a container, :ref:`open an issue <issuetracker>` to tell us so we can help you.


More resources
--------------

If you are working on CSC's platforms, it is worth referring to `CSC's example repo <https://github.com/CSCfi/pytorch-ddp-examples>`__.
