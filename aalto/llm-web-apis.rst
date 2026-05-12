Local LLM web APIs
==================

:doc:`Aalto RSE </rse/index>` runs an LLM gateway service at
`https://llm-gateway.k8s.aalto.fi/ <https://llm-gateway.k8s.aalto.fi/>`__
that is available to all Aalto users.  It serves several open-source
models on Aalto hardware — your data never leaves Aalto premises.
This can be used for lightweight programmatic use, but shouldn't
replace batch usage (use :doc:`/triton/apps/llms`) or interactive
chatting (use Aalto GPT).

.. note::

   The service requires the **Aalto VPN**.  It is a shared resource
   with limited computing power, so please expect some waiting time
   between requests.


Who can use the endpoint and with what data?
--------------------------------------------

To use the local endpoint you need to have an active Aalto account. The advantage of a fully local solution is that the endpoint can be use with data classified as confidential. Secret data should not be processed with these tools.


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


Available models
----------------

The following models are currently available (check
`the API docs <https://llm-gateway.k8s.aalto.fi/docs>`__ for an
always-up-to-date list):

- ``Qwen/Qwen3-30B-A3B-Instruct-2507-FP8``
- ``RedHatAI/gemma-4-31B-it-FP8-Dynamic``
- ``google/gemma-4-31B-it``
- ``google/gemma-4-E4B-it``
- ``Qwen/Qwen3-VL-30B-A3B-Instruct-FP8``
- ``Qwen/Qwen3-VL-30B-A3B-Thinking-FP8``
- ``openai/gpt-oss-120b``

All models support the OpenAI-compatible chat/completions API, so most
existing OpenAI client libraries work without changes.


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
plenty of opportunity for scaling, but this is not turned on until a
need is established.  CPU resources are significant, but there are
limited GPU resources (but that can change, depending on demand).
