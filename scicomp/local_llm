==================
Running Local LLMs
==================

This page describes options for running large language models (LLMs) locally.
Most users should use already available services :doc:`local-llm-web-apis`
or run on Triton :doc:`python-environment-for-machine-learning`.

Llama.cpp
---------

Llama.cpp is a simple and secure way of running LLMs locally. To install it,
 - find the latest release from ``GitHub <https://github.com/ggml-org/llama.cpp/releases>`__`
 - download the appropriate binary version for your operating system and architecture
 - extract the archive

You should be able to run the server directly from the extracted folder. Locate the executable
called `llama-server`. You will need a model file, for example
``https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf <https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf>`__`.

``Huggingface <https://huggingface.co>`__` is a cood place to look for model files. Look for
a gguf file, that is the binary version of the model.

To run llama.cpp, run the command `llama-server -m qwen2.5-1.5b-instruct-q4_k_m.gguf --jinja`.
See ``llama.cpp documentation <https://github.com/ggml-org/llama.cpp#llama-server>`__` for details.

Llama.cpp has a default browser interface, which will open at 127.0.0.1:8080 by default.
