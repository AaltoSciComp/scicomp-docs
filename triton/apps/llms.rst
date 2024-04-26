LLMs
====

Large-language models are AI models that can understand and generate
text, primarily using transformer architectures.  This page is about
running them on a local HPC cluster.  This requires extensive
programming experience and knowledge of using the cluster
(:ref:`tutorials`), but allows maximum computational power for the
least cost.  :doc:`Aalto RSE </rse/index>` maintains these models and
can provide help in using these, even to people who aren't
computational experts.

Because the models are typically very large and there are many people
interested in them, we provide our users with pre-downloaded model
weights and this page has instructions on how to load these weights
for inference purposes or for retraining and fine-tuning the models.


Pre-downloaded model weights
----------------------------
Raw model weights
~~~~~~~~~~~~~~~~~
We have downloaded the following raw model weights (PyTorch model checkpoints):

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2
    * Raw Data
    * ``module load model-llama2/raw-data``
    * Raw weights of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b
    * ``module load model-llama2/7b``
    * Raw weights of 7B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b-chat
    * ``module load model-llama2/7b-chat``
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
    * ``module load model-llama2/70b``
    * Raw weights of 70B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 70b-chat
    * ``module load model-llama2/70b-chat``
    * Raw weights of 70B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * CodeLlama
    * Raw Data
    * ``module load model-codellama/raw-data``
    * Raw weights of `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__.

  * * CodeLlama
    * 7b
    * ``module load model-codellama/7b``
    * Raw weights of 7B parameter version of `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__.

  * * CodeLlama
    * 7b-Python
    * ``module load model-codellama/7b-python``
    * Raw weights of 7B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, specifically designed for Python.
  * * CodeLlama
    * 7b-Instruct
    * ``module load model-codellama/7b-instruct``
    * Raw weights of 7B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, designed for instruction following.

  * * CodeLlama
    * 13b
    * ``module load model-codellama/13b``
    * Raw weights of 13B parameter version of `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__.

  * * CodeLlama
    * 13b-Python
    * ``module load model-codellama/13b-python``
    * Raw weights of 13B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, specifically designed for Python.
  * * CodeLlama
    * 13b-Instruct
    * ``module load model-codellama/13b-instruct``
    * Raw weights of 13B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, designed for instruction following.

  * * CodeLlama
    * 34b
    * ``module load model-codellama/34b``
    * Raw weights of 34B parameter version of `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__.

  * * CodeLlama
    * 34b-Python
    * ``module load model-codellama/34b-python``
    * Raw weights of 34B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, specifically designed for Python.
  * * CodeLlama
    * 34b-Instruct
    * ``module load model-codellama/34b-instruct``
    * Raw weights of 34B parameter version `CodeLlama <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`__, designed for instruction following.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored, i.e., PyTorch model checkpoint directory.
- ``TOKENIZER_PATH`` - File path to the tokenizer.model. 

Here is an example `slurm <https://scicomp.aalto.fi/triton/tut/slurm/>`__, script using the raw weights to do batch inference. For detailed environment setting up, example prompts and Python code, please check out `this repo <https://github.com/AaltoSciComp/llm-examples/tree/main/batch-inference-llama2>`__.

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
  
  # activate your conda environment
  module load mamba
  source activate llama2env

  # run batch inference
  torchrun --nproc_per_node 1 batch_inference.py \
    --prompts prompts.json \
    --ckpt_dir $MODEL_ROOT \
    --tokenizer_path $TOKENIZER_PATH \
    --max_seq_len 512 --max_batch_size 16
     
Model weight conversions
------------------------
Usually, models produced in research are stored as weights from PyTorch or other
frameworks. As for inference, we also have models that are already converted to different formats.


Huggingface Models
~~~~~~~~~~~~~~~~~~~


Following Huggingface models are stored on triton. Full list of all the available models are located at ``/scratch/shareddata/dldata/huggingface-hub-cache/models.txt``. Please contact us if you need any other models.

.. list-table::
  :header-rows: 1
  :widths: 1 1

  * * Model type
    * Huggingface model identifier

  * * Text Generation
    * mistralai/Mistral-7B-v0.1

  * * Text Generation
    * mistralai/Mistral-7B-Instruct-v0.1

  * * Text Generation
    * tiiuae/falcon-7b

  * * Text Generation
    * tiiuae/falcon-7b-instruct

  * * Text Generation
    * tiiuae/falcon-40b

  * * Text Generation
    * tiiuae/falcon-40b-instruct

  * * Text Generation
    * google/gemma-2b-it

  * * Text Generation
    * google/gemma-7b

  * * Text Generation
    * google/gemma-7b-it

  * * Text Generation
    * google/gemma-7b

  * * Text Generation
    * LumiOpen/Poro-34B


  * * Text Generation
    * meta-llama/Llama-2-7b-hf

  * * Text Generation
    * meta-llama/Llama-2-13b-hf

  * * Text Generation
    * meta-llama/Llama-2-70b-hf

  * * Text Generation
    * codellama/CodeLlama-7b-hf

  * * Text Generation
    * codellama/CodeLlama-13b-hf

  * * Text Generation
    * codellama/CodeLlama-34b-hf

  * * Translation
    * Helsinki-NLP/opus-mt-en-fi

  * * Translation
    * Helsinki-NLP/opus-mt-fi-en

  * * Translation
    * t5-base
  
  * * Fill Mask
    * bert-base-uncased

  * * Fill Mask
    * bert-base-cased

  * * Fill Mask
    * distilbert-base-uncased

  * * Text to Speech
    * microsoft/speecht5_hifigan
  
  * * Text to Speech
    * facebook/hf-seamless-m4t-large

  * * Automatic Speech Recognition
    * openai/whisper-large-v3

  * * Token Classification
    * dslim/bert-base-NER-uncased



All Huggingface models can be loaded with  ``module load model-huggingface/all``.
Here is a Python script using huggingface model.

.. code-block:: python

  ## Force transformer to load model(s) from local hub instead of download and load model(s) from remote hub. NOTE: this must be run before importing transformers.
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
~~~~~~~~~~~~~~~~~~~

`llama.cpp <https://github.com/ggerganov/llama.cpp>`__ is a popular framework
for running inference on LLM models with CPUs or GPUs. llama.cpp uses a format
called GGUF as its storage format.

We have llama.cpp conversions of all Llama 2 and CodeLlama models with multiple quantization levels.

NOTE: Before loading the following modules, one must first load a module for the raw model weights. For example, run ``module load model-codellama/34b`` first, and then run ``module load codellama.cpp/q8_0-2023-12-04`` to get the 8-bit integer version of CodeLlama weights in a .gguf file.

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2 
    * f16-2023-08-28
    * ``module load model-llama.cpp/f16-2023-12-04`` (after loading a Llama 2 model for some raw weights)
    * Half precision version of Llama 2 weights done with llama.cpp on 4th of Dec 2023.

  * * Llama 2 
    * q4_0-2023-08-28
    * ``module load model-llama.cpp/q4_0-2023-12-04`` (after loading a Llama 2 model for some raw weights)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 4th of Dec 2023.

  * * Llama 2
    * q4_1-2023-08-28
    * ``module load model-llama.cpp/q4_1-2023-12-04`` (after loading a Llama2 model for some raw weights)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 4th of Dec 2023.

  * * Llama 2 
    * q8_0-2023-08-28
    * ``module load model-llama.cpp/q8_0-2023-12-04`` (after loading a Llama 2 model for some raw weights)
    * 8-bit integer version of Llama 2 weights done with llama.cpp on 4th of Dec 2023.

  * * CodeLlama
    * f16-2023-08-28
    * ``module load codellama.cpp/f16-2023-12-04`` (after loading a CodeLlama model for some raw weights)
    * Half precision version of CodeLlama weights done with llama.cpp on 4th of Dec 2023.

  * * CodeLlama
    * q4_0-2023-08-28
    * ``module load codellama.cpp/q4_0-2023-12-04`` (after loading a CodeLlama model for some raw weights)
    * 4-bit integer version of CodeLlama weights done with llama.cpp on 4th of Dec 2023.

  * * CodeLlama
    * q8_0-2023-08-28
    * ``module load codellama.cpp/q8_0-2023-12-04`` (after loading a CodeLlama model for some raw weights)
    * 8-bit integer version of CodeLlama weights done with llama.cpp on 4th of Dec 2023.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored.
- ``MODEL_WEIGHTS`` - Path to the model weights in GGUF file format.

This Python code snippet is part of a 'Chat with Your PDF Documents' example, utilizing LangChain and leveraging model weights stored in a .gguf file. For detailed environment setting up and Python code, please check out `this repo <https://github.com/AaltoSciComp/llm-examples/tree/main/chat-with-pdf>`__.

.. code-block:: python
  
  import os
  from langchain.llms import LlamaCpp

  model_path = os.environ.get('MODEL_WEIGHTS')
  llm = LlamaCpp(model_path=model_path, verbose=False)


More examples
------------------------------------------------------------

Starting a local API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
With the pre-downloaded model weights, you are also able create an API endpoint locally. For detailed examples, you can checkout `this repo <https://github.com/AaltoSciComp/llm-examples/tree/main/>`__.

