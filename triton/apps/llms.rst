LLMs
====


.. highlight:: bash

Large-language models are AI models that can understand and generate text
using transformer architectures.

Because the model weights are typically very large and the interest in the
models is high, we provide our users pre-downloaded model weights and
instructions on how to run inference and training on the models.


Pre-downloaded model weights
****************************

We have downloaded the following models weights (PyTorch model checkpoint directories):

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2
    * Raw data
    * ``module load model-llama2/raw-data``
    * Raw weights of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b
    * ``module load model-llama2/7b``
    * Raw weights of 7B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b-chat
    * `module load model-llama2/7b-chat`
    * Raw weights of 7B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 13b
    * ``module load model-llama2/13b``
    * Raw weights of 13B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 13b-chat
    * ``module load model-llama2/13b-chat``
    * Raw weights of 13B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 70b
    * `module load model-llama2/70b`
    * Raw weights of 70B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 70b-chat
    * `module load model-llama2/70b-chat`
    * Raw weights of 70B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored, i.e., PyTorch model checkpoint directory.
- ``TOKENIZER_PATH`` - File path to the tokenizer.model. 

Here is an example slurm script using the raw weights to do batch inference. For detailed environment setting up, example prompts and python code, please check out `this repo <>`__.

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=00:25:00
  #SBATCH --cpus_per_task=4
  #SBATCH --mem=20GB
  #SBATCH --gres=gpu:1
  #SBATCH --output=llama2inference-gpu.%J.out
  #SBATCH --error=llama2inference-gpu.%J.err

  # get the model weights
  module load model-llama2/7b
  echo $MODEL_ROOT
  # Expect output: /scratch/shareddata/dldata/llama-2/llama-2-7b
  echo $TOKENIZER_PATH
  # Expect output: /scratch/shareddata/dldata/llama-2/tokenizer.model
  
  # activate conda environment
  module load miniconda
  source activate llama2env

  # run batch inference
  torchrun --nproc_per_node 1 batch_inference.py \
    --prompts prompts.json \
    --ckpt_dir $MODEL_ROOT \
    --tokenizer_path $TOKENIZER_PATH \
    --max_seq_len 512 --max_batch_size 16
     
Model weight conversions
************************

Usually models produced in research are stored as weights from PyTorch or other
frameworks. When doing inference,

We also have models that are already converted to different formats.


Huggingface
-----------



We have the following Huggingface models stored:

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2
    * 
    * Module command to load
    * Description

All Huggingface models can be loaded with:  ``module load model-huggingface/all``,
Here is a python script using huggingface model.

.. code-block:: python

  #force transformer to use local hub instead of download from remote hub
  import os
  os.environ['TRANSFORMERS_OFFLINE'] = '1'

  from transformers import AutoModelForCausalLM, AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
  model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
  prompt = "How many stars in the space?"
  model_inputs = tokenizer([prompt], return_tensors="pt")
  input_length = model_inputs.input_ids.shape[1]
  generated_ids = model.generate(**model_inputs, max_new_tokens=20)
  print(tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0])

llama.cpp and GGUF
------------------

`llama.cpp <https://github.com/ggerganov/llama.cpp>`__ is a popular framework
for running inference on LLM models with CPUs or GPUs. llama.cpp uses a format
called GGUF as its storage format.

We have llama.cpp conversions of all models with multiple quantizations levels.

Before loading the modules load a module for the model weight you want to use.

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2
    * f16-2023-08-28
    * ``module load model-llama.cpp/f16-2023-08-28`` (after loading a Llama 2 model for some weight)
    * Half precision version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q4_0-2023-08-28
    * ``module load model-llama.cpp/q4_0-2023-08-28`` (after loading a Llama 2 model for some weight)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q4_1-2023-08-28
    * ``module load model-llama.cpp/q4_1-2023-08-28`` (after loading a Llama 2 model for some weight)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q8_0-2023-08-28
    * ``module load model-llama.cpp/q8_0-2023-08-28`` (after loading a Llama 2 model for some weight)
    * 8-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored.
- ``MODEL_WEIGHTS`` - Path to the model weights in GGUF format.

This Python code snippet is part of a 'Chat with Your PDF Documents' example, utilizing LangChain and leveraging model weights stored in a .gguf file. For detailed environment setting up and python code, please check out `this repo <>`__.

.. code-block:: python
  
  import os
  from langchain.llms import LlamaCpp

  model_path = os.environ.get('MODEL_WEIGHTS')
  llm = LlamaCpp(model_path=model_path, verbose=False)

Ollama models
-------------


Doing inference with LLMs
*************************

Running an interactive chat with Ollama
---------------------------------------

Running inference with LangChain
--------------------------------

