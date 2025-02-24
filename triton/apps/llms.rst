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

The simplest way to use pre-trained open-source LLMs is to access them through HuggingFace and to leverage their `🤗 Transformers Python library <https://huggingface.co/docs/transformers/en/index>`__. 

HuggingFace provides a wide range of tools and pre-trained models, making it easy to integrate and utilize these models in your projects.

You can explore their offerings at `🤗 HuggingFace <https://huggingface.co/>`__.

.. note::

  We are keeping an eye on the latest models and have pre-downloaded some of them for you. If you need any other models, please contact :doc:`the Aalto RSEs </rse/index>`.

  Run command ``ls /scratch/shareddata/dldata/huggingface-hub-cache/hub`` to see the full list of all the available models.

Below is an example of how to use the 🤗 Transformers `pipeline() <https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/pipelines#transformers.pipeline>`__ to load a pre-trained model and use it for text generation.

.. tabs::

  .. group-tab:: Slurm script

    Request computational resources and load the necessary modules.

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

      # Load Python environment to use HuggingFace Transformers
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


Below is a Python script using a HuggingFace model (``meta-llama/Llama-3.1-8B``) for text generation. 

Use it as the content of ``your_script.py`` in the Slurm script example above or a Jupyter notebook cell.

.. code-block:: python

  from transformers import AutoModelForCausalLM, AutoTokenizer
  import torch

  model_name = "meta-llama/Llama-3.1-8B"

  # Load tokenizer
  tokenizer = AutoTokenizer.from_pretrained(model_name)

  # Load model with bfloat16 on GPU
  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      torch_dtype=torch.bfloat16,  # Use bfloat16
      device_map="auto"            # Automatically maps to GPU if available
  )

  # Prepare input
  prompt = "How many stars in the space?"
  model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")  # Send inputs to GPU
  input_length = model_inputs.input_ids.shape[1]

  # Generate response
  generated_ids = model.generate(**model_inputs, max_new_tokens=20)

  # Decode and print result
  print(tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0])


Other Frameworks
~~~~~~~~~~~~~~~~

While HuggingFace provides a convenient way to access and use LLMs, there are other frameworks available for running LLMs, such as

- `LangChain <https://langchain.github.io/>`__
- `TensorFlow <https://www.tensorflow.org/>`__
- `PyTorch <https://pytorch.org/>`__
- `DeepSpeed <https://www.deepspeed.ai/>`__

If you need assistance running LLMs in these or other frameworks, please contact :doc:`the Aalto RSEs </rse/index>`.


More examples
~~~~~~~~~~~~~

AaltoRSE has prepared a repository with examples of using LLMs on Triton. You can find it `here <https://github.com/AaltoSciComp/llm-examples/tree/main/>`__.


