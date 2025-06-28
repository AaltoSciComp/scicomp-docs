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

The most common way to use pre-trained open-source LLMs is to access them through HuggingFace 
and to leverage their `🤗 Transformers Python library <https://huggingface.co/docs/transformers/en/index>`__. 

HuggingFace provides a wide range of tools and pre-trained models, making it easy to integrate and utilize these models in your projects.

You can explore their offerings at `🤗 HuggingFace <https://huggingface.co/>`__.

.. note::

  We are keeping an eye on the latest models and have pre-downloaded some of them for you. If you need any other models, please contact :doc:`the Aalto RSEs </rse/index>`.

  Run command ``ls /scratch/shareddata/dldata/huggingface-hub-cache/hub`` to see the full list of all the available models.

Below is an example of how to use the 🤗 Transformers `pipeline() <https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/pipelines#transformers.pipeline>`__ to load a pre-trained model and use it for question answering.


Example: Question Answering
---------------------------

In the following sbatch script, we request computational resources, load the necessary modules, and run a Python script that uses a HuggingFace model for question answering.

  .. code-block:: bash
  
    #!/bin/bash
    #SBATCH --time=00:30:00
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=80GB #This is system memory, not GPU memory.
    #SBATCH --gpus=1
    #SBATCH --partition=gpu-v100-32g # modify according to your needs
    #SBATCH --output huggingface.%J.out
    #SBATCH --error huggingface.%J.err

    #By loading the model-huggingface module, we set HF_HOME to /scratch/shareddata/dldata/huggingface-hub-cache which is a shared scratch space.
    #By default, HF_HOME is set to $HOME/.cache/huggingface, which is under your own home directory where you have limited quota.
    module load model-huggingface

    # Load a ready to use conda environment to use HuggingFace Transformers
    module load scicomp-llm-env/2025.2

    # Force transformer to load model(s) from local hub instead of download and load model(s) from remote hub. 
    export TRANSFORMERS_OFFLINE=1
    export HF_HUB_OFFLINE=1

    python your_script.py

The ``your_script.py`` Python script uses a HuggingFace model ``mistralai/Mistral-7B-Instruct-v0.1`` for conversations and instructions.

.. code-block:: python

  from transformers import pipeline
  import torch

  # Initialize pipeline
  pipe = pipeline( 
    "text-generation", # Task type 
    model="mistralai/Mistral-7B-Instruct-v0.1", # Model name 
    device="cuda", # Specify to use CUDA as device
    max_new_tokens=1000 
  ) 

  # Prepare prompts
  messages = [
    {"role": "user", "content": "Continue the following sequence: 1, 2, 3, 5, 8"}    
    ]

  # Generate and print responses
  responses = pipe(messages) 
  print(responses)

For reference, here is a table of model size and memory requirements for different model sizes and data types:

+---------------+------------+---------------+---------------+------------+
| Model Size    | Parameters | float32 (4B)  | float16 (2B)  | int8 (1B)  |
+===============+============+===============+===============+============+
| 1B parameters | 1e9        | 4 GB          | 2 GB          | 1 GB       |
+---------------+------------+---------------+---------------+------------+
| 7B parameters | 7e9        | 28 GB         | 14 GB         | 7 GB       |
+---------------+------------+---------------+---------------+------------+
|13B parameters | 13e9       | 52 GB         | 26 GB         | 13 GB      |
+---------------+------------+---------------+---------------+------------+

In addition to the model size, you should also consider additional memory overhead for intermediate activations and input token embeddings.

Note: this is the scenario where you are using the model for inference. For training, memory requirements are significantly higher due to gradients, optimizer states (e.g., Adam maintains momentum and variance estimates), gradient accumulation buffers, and larger activation caches. Training can require 3-4x more memory than the model size alone.

You can look at the `model card <https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1>`__ for more information about the model.


Other Frameworks
~~~~~~~~~~~~~~~~

While HuggingFace provides a convenient way to access and use LLMs, there are other popular frameworks 
available for running LLMs, such as `vLLM <https://docs.vllm.ai/en/latest/>`__ for high-performance inference,
`Ollama <https://ollama.com/>`__ for local deployment, `DeepSpeed <https://www.deepspeed.ai/tutorials/inference-tutorial/>`__, 
and `LangChain <https://python.langchain.com/docs/how_to/local_llms/>`__ for building LLM applications.

If you need assistance running LLMs in these or other frameworks, please contact :doc:`the Aalto RSEs </rse/index>`.


More examples
~~~~~~~~~~~~~

AaltoRSE has prepared a repository with miscellaneous examples of using LLMs on Triton. You can find it `here <https://github.com/AaltoSciComp/llm-examples/tree/main/>`__.


