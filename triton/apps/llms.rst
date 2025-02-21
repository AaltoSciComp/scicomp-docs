LLMs
====

Large-language models (LLMs) are AI models that can understand and generate
text, primarily using transformer architectures. They are extensively used for tools and 
tasks such as chatbots, translation, summarization, sentiment analysis, and question answering.

This page is about running LLMs on Aalto Triton. As a prerequisite, it is recommended to
get familiar with the basics of using the cluster, including running jobs and using Python (:ref:`tutorials`).

.. note::

    If at any point something doesn't work, you are unsure how to get started or proceed, do not hesitate to contact :doc:`the Aalto RSEs </rse/index>`. 

    You can visit us at :ref:`the daily Zoom help session at 13.00-14.00 <garage>`.
 

HuggingFace Models
~~~~~~~~~~~~~~~~~~~

The simplest way to use open-source LLMs is through the tools and pre-trained models hub provided by the `HuggingFace <https://huggingface.co/>`__ platform.

Most open-source models from HuggingFace are widely supported and integrated with the transformers Python library.

.. note::

  We are keeping our eyes on the latest models and have pre-downloaded some of them for you. If you need any other models, please contact :doc:`the Aalto RSEs </rse/index>`.

  Run command ``ls /scratch/shareddata/dldata/huggingface-hub-cache/hub`` to see the full list of all the available models.

An example how to run a HuggingFace model on Triton using a Slurm script or Jupyter notebook is shown below.

.. tabs::

  .. group-tab:: Slurm script

    Request computational resources and load the module for huggingface models:

    .. code-block:: bash
    
      #!/bin/bash
      #SBATCH --time=00:30:00
      #SBATCH --cpus-per-task=4
      #SBATCH --mem=40GB
      #SBATCH --gpus=1
      #SBATCH --output huggingface.%J.out
      #SBATCH --error huggingface.%J.err

      # Set HF_HOME to /scratch/shareddata/dldata/huggingface-hub-cache
      module load model-huggingface

      # Load environment
      module load scicomp-llm-env

      # Force transformer to load model(s) from local hub instead of download and load model(s) from remote hub. 
      export TRANSFORMERS_OFFLINE=1
      export HF_HUB_OFFLINE=1

      python your_script.py

  .. group-tab:: Jupyter notebook

    TODO: How to get Jupyter session with GPU on Triton?

    In jupyter notebook, one can set up all necessary environment variables directly:

    .. code-block:: python

      ## Force transformer to load model(s) from local hub instead of download and load model(s) from remote hub. 
      ## IMPORTANT: This must be executed before importing the transformers library
      import os
      os.environ['TRANSFORMERS_OFFLINE'] = '1'
      os.environ['HF_HUB_OFFLINE'] = '1'
      os.environ['HF_HOME']='/scratch/shareddata/dldata/huggingface-hub-cache'


Below is a Python script using a HuggingFace model (``mistralai/Mistral-7B-v0.1``) for text generation. 

Use it as the content of ``your_script.py`` in the Slurm script example above or a Jupyter notebook cell.

.. code-block:: python

  from transformers import pipeline

  pipe = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")

  prompts = ["How many stars in a galaxy?", "How many planets in a solar system?"]

  results = pipe(prompts)

  print(results)


More examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AaltoRSE has prepared a repository with examples of using LLMs on Triton. You can find it `here <https://github.com/AaltoSciComp/llm-examples/tree/main/>`__.


