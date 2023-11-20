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

We have downloaded following models weights:

.. list-table::
  :header-rows: 1
  :widths: 1 1 3 2

  * * Model type
    * Model version
    * Module command to load
    * Description

  * * Llama 2
    * Raw data
    * `module load model-llama2/raw-data`
    * Raw weights of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b
    * `module load model-llama2/7b`
    * Raw weights of 7B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 7b-chat
    * `module load model-llama2/7b`
    * Raw weights of 7B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 13b
    * `module load model-llama2/13b`
    * Raw weights of 13B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 13b-chat
    * `module load model-llama2/13b-chat`
    * Raw weights of 13B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 70b
    * `module load model-llama2/13b`
    * Raw weights of 70B parameter version of `Llama 2 <https://ai.meta.com/llama/>`__.

  * * Llama 2
    * 70b-chat
    * `module load model-llama2/13b-chat`
    * Raw weights of 70B parameter chat optimized version of `Llama 2 <https://ai.meta.com/llama/>`__.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored.


Model weight conversions
************************

Usually models produced in research are stored as weights from PyTorch or other
frameworks. When doing inference,

We also have models that are already converted to different formats.


Huggingface
-----------

All Huggingface models can be loaded with:  ``module load model-huggingface/all``

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
    * `module load model-llama.cpp/f16-2023-08-28` (after loading a Llama 2 model for some weight)
    * Half precision version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q4_0-2023-08-28
    * `module load model-llama.cpp/q4_0-2023-08-28` (after loading a Llama 2 model for some weight)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q4_1-2023-08-28
    * `module load model-llama.cpp/q4_1-2023-08-28` (after loading a Llama 2 model for some weight)
    * 4-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

  * * Llama 2
    * q8_0-2023-08-28
    * `module load model-llama.cpp/q8_0-2023-08-28` (after loading a Llama 2 model for some weight)
    * 8-bit integer version of Llama 2 weights done with llama.cpp on 28th of Aug 2023.

Each module will set the following environment variables:

- ``MODEL_ROOT`` - Folder where model weights are stored.
- ``MODEL_WEIGHTS`` - Path to the model weights in GGUF format.


Ollama models
-------------


Doing inference with LLMs
*************************

Running an interactive chat with Ollama
---------------------------------------

Running inference with LangChain
--------------------------------

