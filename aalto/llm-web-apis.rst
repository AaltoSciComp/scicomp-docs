Local LLM web APIs
==================

As a pilot service, Aalto IT Services and :doc:`Aalto RSE </rse/index>` have a service
running some common open-source LLMS (Qwen3, gemma4, ...) available
via the OpenAI-compatible APIs.  This can be used for lightweight purposes via
programming, but shouldn't replace batch usage (use
:doc:`/triton/apps/llms`) or interactive chatting (use the Aalto AI assistant).


Access
------

The service is currently hosted on https://llm-gateway.k8s.aalto.fi and 
the API will remain there, while the front end will move in the near 
future. Access is currently limited to staff, and teachers can create
keys they can provide to students for teaching purposes. It is up 
to the teacher to recall those keys again after the work is done.

The API provided is basically a responses and chat/completions API 
and mostly OpenAI compatible. The service is based on vllm and the 
api specification can be found `here <https://llm-gateway.k8s.aalto.fi/docs>`__.
Here are some simple `examples <https://github.com/AaltoSciComp/llm-examples/tree/main/aalto-llm-api>`__.

Models
------

The cluster this service runs on has a limited amount of resources 
(there are only 8 GPUs in total in this cluster), and we hope that those we will
get more in the future. This means that most models are not running
constantly but scale down to 0 when not in use, and it can, depending on
model size, take a substantial time (up to several minutes) for them to spin up (get the model loaded into memory).
On demand models are marked in the Model overview on the frontend. 

Request Additional Models
~~~~~~~~~~~~~~~~~~~~~~~~~
We can add additional models to the system if they are available on
huggingface and downloadable from europe. If you have a request for a model
please send an email to rse@aalto.fi with the name of the model and
we will try to set it up. 
Due to the resource limitations, the maximum model size we currently can
support is 60GB (which just about makes oss-gpt-120b possible). 
Optimal model sizes are 40G or below, as those fit onto a single GPU 
on the cluster, and multi-GPU models often cause problems during
deployment. 


Intended use and resource availability
--------------------------------------

This is ideal if you need to run things through LLMs which are only
running on Aalto servers, and without many requests per second (this
isn't for batch use).  This could, for example, be an alternative to
running your own LLM server for basic testing or small question
answering.  It's also good if you need to test various open-source
LLMs out before beginning batch work.  It's perfectly suited for
intermittent daily use. 

Right now, each models has limited resources (some running on CPUs and
some on GPUs).  They can serve a request every few seconds, but
resources could easily be overloaded.  We intend to add resources as
needed, depending on use.  For any serious use, please contact us so
that we can plan for the future.  Don't assume any stability or
performance right now.


Technical implementation
------------------------

Models run on local hardware on the Aalto University premises.
Kubernetes is used to manage computing power, so in principle there is
plenty of opportunity for increasing resources if there is high demand and the models do scale to some extent.

