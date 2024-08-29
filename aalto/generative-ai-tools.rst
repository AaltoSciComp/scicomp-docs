Generative AI services roadmap
==============================

If you need to use generative AI tools for, e.g. question and answering, speech to text, or text embedding, there are many tools and platforms available.
Roughly speaking, you could

* Use it via some web service.

  * Public services (eg. Chat GPT) *bad for data security*
  * Public services with contract to Aalto (e.g. `Aalto GPT
    <https://www.aalto.fi/en/services/aalto-gpt>`__)

* Use remote APIs to run models with your own code.

  * An OpenAI API
  * Models hosted locally at Aalto *good for data security*

* Running locally-installable models on your own
  computer/Triton. *best for data security*.

The first category is good for easy interactive or occasional use
(they can only be run manually), the second is good for scripted use
that isn't too intense (the network traffic slows things down and you
have to share resources), and the last category is good for
large-scale analysis.



Pre-build web services
----------------------

These are simple, directly usable web services.  These are good when
you need to try out models or do small tasks, but you are limited
because you have to type in and see the output by yourself - there is
no automation.

Examples:

* `Aalto AI Assistant
  <https://www.aalto.fi/en/services/aalto-ai-assistant-former-aalto-gpt>`__
  (Locally run but uses the same models as ChatGPT, paid by Aalto,
  good data security agreements).  Free for basic use within Aalto.
  It is possible for us to add features if requested.
* Public Chat GPT (not good for data security: there is no processing
  agreement with Aalto, things you submit may be used for other
  purposes)
* Many other services you can find online, many of which have
  questionable data security or ownership practices.
* The Aalto service `speech2text <speech2text.rst>`__ uses the Whisper
  model.  It is a multitasking model that can perform multilingual
  speech recognition, speech translation, and language
  identification.  speech2text runs on the Triton computer and thus is
  good for data security.





Web APIs to models
------------------

With APIs, you run your own code, but the model is running on someone
else's computer.  You access the model via the network, which can slows
things down a little bit.  The major advantage is that you only need
to focus on writing your own code, and it is easy to automate
large-scale usage.  You don't need to provide your own AI hardware,
only a place to run your general code.

From APIs, you can implement your own analysis, or even use locally
installed programs to chat, similar to the services described above.
It is possible to, for example, prompt a model with tens of thousands
of text inputs.


* `Aalto can provide Azure OpenAI API access
  <https://www.aalto.fi/en/services/aalto-ai-apis>`__,
  which gives you access to the same models as ChatGPT.  This comes
  with a good data security agreement, and small usage can be provided
  for free.

  * Allows access to the largest models and some of the most
    developed, but these large models have a significant cost.

* :doc:`Aalto-hosted open-source <llm-web-apis>` have good data security,
  since the data never leaves Aalto networks or Aalto computers.  It
  is possible to add models and cost-effectively scale as needed. (If
  these work, it is easy to use these models locally,
  allowing extreme scaling to large computer clusters)

  * We are currently limited in the number of models and hardware
    resources, but plan to scale in proportion to the need.
  * This is a very cost-efficient method to use these models.
  * These models will eventually be available in the Aalto AI
    Assistant as options you can test.

* OpenAI, and many other providers, also provide general API access
  for a price.  Without an Aalto contract, data security can not be
  guaranteed.



Locally installed models
------------------------

Open-source models can be downloaded and run on your own computers,
which can provide the ultimate performance for large analysis.  The
downside is that managing this software can be a significant
challenge.  However, once you do this, you will have access to almost
unlimited and "free for academic use" resources on High-performance
computing (HPC) clusters.

When running locally, you optimize for running very many queries very
fast, so it has the potential to have the highest performance for big
analysis (especially when combined with HPC clusters).

* In general, you would find the models yourself, see how it can be
  downloaded, and run it.
* :doc:`Aalto's Triton </triton/index>` cluster has many models
  pre-downloaded and software ready for your use.

  * See :doc:`/triton/apps/llms` for instructions (there are more
    model than listed on that page, and it is easy for us to
    download more as soon as they are released).
  * Installing the required software can sometimes be tricky, but
    Aalto SciComp has done this many times: come to our :ref:`garage
    help session <garage>` and ask us rather than waste your own time.
  * Triton provides a significant amount of GPU hardware, but it is
    limited.
  * We have many `code examples
    <https://github.com/AaltoSciComp/llm-examples>`__.

  * :doc:`Whisper </triton/apps/whisper>`, the speech transcription
    model and software, is installed on Triton in an easy to use
    package: simply copy your file and run.  (speech2text mentioned
    above is an even easier interface that uses similar principles).

* `CSC <https://research.csc.fi/csc-s-servers>`__ and `LUMI
  <https://research.csc.fi/-/lumi>`__ supercomputers have very many
  more GPUs than Triton, and is free for academic use.  It must be
  applied per-project, but this is routine.

  * These can sometimes be tricky to use.  Aalto SciComp supports
    these systems equally to our own.

* Models can of course be run on your own computer.  It is good to
  have GPU hardware.



Support
-------

For support in general AI tools, contact servicedesk@aalto.fi.  This
includes OpenAI/ChatGPT access and evaluating other tools for
taking them into use.

For computationally-oriented questions, Aalto SciComp offers a
:ref:`daily help session "garage" <garage>`, where you can ask any
question, including getting advice on recommended solutions *before*
you begin a project.
