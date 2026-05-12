Local LLM web APIs
==================

As a pilot service, Aalto IT Services and :doc:`Aalto RSE </rse/index>` run an LLM gateway service at
`https://llm-gateway.k8s.aalto.fi/ <https://llm-gateway.k8s.aalto.fi/>`__
that is available to all Aalto employees for research and teaching purposes.  
It serves several open-source
models on Aalto hardware — your data never leaves Aalto premises.
This can be used for lightweight programmatic use, but shouldn't
replace batch usage (use :doc:`/triton/apps/llms`) or interactive
chatting (use Aalto AI assitant).

.. note::

   The service requires the **Aalto VPN**.  It is a shared resource
   with limited computing power, so please expect some waiting time
   between requests.


Who can use the endpoint and with what data?
--------------------------------------------

To use the local endpoint you need to have an active Aalto account and be part of Aalto staff. Students can get access via their course organiser (the organiser creates an API key for the students to use); teachers are responsible for revoking student keys once the course work is complete. The advantage of a fully local solution is that the endpoint can be use with data classified as confidential. Secret data should not be processed with these tools.


Access and API keys
-------------------

The gateway uses API key authentication with self-service key
management:

1. Connect to the Aalto VPN and open
   `https://llm-gateway.k8s.aalto.fi/ <https://llm-gateway.k8s.aalto.fi/>`__.
2. In the box labelled *Add a New key*, type a descriptive name for
   your key and submit.  You may create up to 10 keys.
3. Copy the generated key and store it somewhere safe — it will be used
   as ``api_key`` in your code.

For questions or feedback, join the ``#llms`` stream on :ref:`chat`.


Available models and limitations
--------------------------------

The following models are currently available (check
`the API docs <https://llm-gateway.k8s.aalto.fi/docs>`__ for an
always-up-to-date list):

.. list-table::
   :header-rows: 1
   :widths: 50 30 20

   * - Model
     - HuggingFace
     - Size (GB, estimated)
   * - ``Qwen/Qwen3-30B-A3B-Instruct-2507-FP8``
     - `Model card <https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8>`__
     - ~16
   * - ``RedHatAI/gemma-4-31B-it-FP8-Dynamic``
     - `Model card <https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-Dynamic>`__
     - ~17
   * - ``google/gemma-4-E4B-it``
     - `Model card <https://huggingface.co/google/gemma-4-E4B-it>`__
     - ~16
   * - ``Qwen/Qwen3-VL-30B-A3B-Instruct-FP8``
     - `Model card <https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct-FP8>`__
     - ~62
   * - ``Qwen/Qwen3-VL-30B-A3B-Thinking-FP8``
     - `Model card <https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Thinking-FP8>`__
     - ~16
   * - ``openai/gpt-oss-120b``
     - `Model card <https://huggingface.co/openai/gpt-oss-120b>`__
     - ~70

All models support the OpenAI-compatible chat/completions API, so most
existing OpenAI client libraries work without changes. If you want to request new models, please email ``rse@aalto.fi``; models must be available on HuggingFace and downloadable from within Europe. Please note that only models smaller than ~70GB can be used in the current hardware we have. Models of 40 GB or below are preferred as they fit on a single GPU; multi-GPU deployments are more fragile and may fail to start. Please note that the system does NOT provide ``responses`` background functionality (i.e. submit now, come back later). It does otherwise support ``responses``.

Only two models:

- ``Qwen/Qwen3-30B-A3B-Instruct-2507-FP8``
- ``RedHatAI/gemma-4-31B-it-FP8-Dynamic``

are permanently on, i.e. there is an instance of those running constantly. 

The other models are on demand, i.e. they will be spun up once a request comes in
(this can take up to several minutes depending on model size) and
will be turned off again if there are no requests for some time.
On-demand models are labelled as such in the model overview on the gateway frontend.
Given the limited resources (at time of writing the whole supporting infrastructure has 8 L40s cards)
not all models can run at the same time and it is entirely possible that a model
will not spin up after a request because resources are in use.
If you are unsure which one to pick as a start, pick "RedHatAI/gemma-4-31B-it-FP8-Dynamic".

Python quickstart
-----------------

**1. Set up an environment**

.. code-block:: bash

   mkdir my-llm-project && cd my-llm-project
   mamba create python=3.11 -p ./env
   mamba activate ./env
   pip install openai rich

**2. Run a test query**

Replace ``YOURKEYGOESHERE`` with the key you created above.

.. code-block:: python

   from openai import OpenAI
   from rich.console import Console
   from rich.markdown import Markdown

   client = OpenAI(
       api_key="YOURKEYGOESHERE",
       base_url="https://llm-gateway.k8s.aalto.fi/api/v1"
   )
   completion = client.chat.completions.create(
       model="RedHatAI/gemma-4-31B-it-FP8-Dynamic",
       messages=[
           {"role": "system", "content": "Helpful assistant that writes python for research."},
           {"role": "user", "content": "I need a python script to load a csv."}
       ]
   )

   console = Console()
   console.print(Markdown(completion.choices[0].message.content))

More examples are available at
`AaltoSciComp/llm-examples <https://github.com/AaltoSciComp/llm-examples/tree/main/aalto-llm-api>`__.


Intended use and resource availability
--------------------------------------

This is ideal if you need to run things through LLMs which are only
running on Aalto servers, and without many requests per second (this
isn't for batch use).  This could, for example, be an alternative to
running your own LLM server for basic testing or small question
answering.  It's also good if you need to test various open-source
LLMs out before beginning batch work.  It's perfectly suited for
intermittent daily use.

Right now, resources are limited and shared across all users.  Models
can serve a request every few seconds, but could easily be overloaded
under heavy demand.  We intend to add resources as needed, depending
on use.  For any serious use, please contact us so that we can plan
for the future.  Don't assume any stability or performance right now.


Technical implementation
------------------------

Models run on local hardware on the Aalto University premises.
Kubernetes is used to manage computing power, so in principle there is
plenty of opportunity for increasing resources if there is high demand, but this is not turned on until a
need is established.  CPU resources are significant, but there are
limited GPU resources (but that can change, depending on demand).
