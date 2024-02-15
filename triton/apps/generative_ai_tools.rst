Generative AI Tools from Science-IT
=============================

If you need to use generative AI tools for, e.g. question and answering, speech to text, or text embedding, there are many tools and platforms available.
Roughly speaking, you could

* Use it via some web service.

  * Public services (eg. Chat GPT) *bad for data security*
  * Public services with contract to Aalto (e.g. `Aalto GPT
    <https://www.aalto.fi/en/services/aalto-gpt>`__)
  * Locally-hosted models via web APIs (we are working on this, see
    #llms on :ref:`our chat <chat>`) *good for data security*

* Running locally-installable models on your own
  computer/Triton. *best for data security*.

The first category is good for interactive or occasional use (the
network traffic slows things down and you have to share resources),
and the second category is good for large-scale analysis.



Speech to Text: Whisper
----------------------------
Whisper is a general-purpose speech recognition model. It is a
multitasking model that can perform multilingual speech recognition,
speech translation, and language identification. For the usage on
Triton, please check out the :doc:`whisper` page for running
it yourself, or :doc:`speech2text` for a system of using Whisper
designed for non-experts.



Locally installed LLMs
----------------------
We have many models already predownloaded and software installed for
using them.  See :doc:`llms`.  If you need more models, large datasets or code
examples, just ask us.  We also have tested and provide support for
(for example) running LLMs on CSC or LUMI supercomputers - which have
plenty more resources, but can be hard to use.



Open source models via APIs
---------------------------
We have open-source models coming via API.  This won't be running on
Triton, but will be running only on local hardware under our control.
The API will be the same as that of ChatGPT, so all ChatGPT tools (if
they can be directed to a different server) will be usable.

