Local LLM web APIs
==================

As a pilot service, :doc:`Aalto RSE </rse/index>` has a service
running some common open-source LLMS (llama2, mistral, etc.) available
via the web.  This can be used for lightweight purposes via
programming, but shouldn't replace batch usage (use
:doc:`/triton/apps/llms`) or interactive chatting (use Aalto GPT).


Access
------

Currently this is not available publicly, but if you ask, we can
provide development access.  Chat with us in the #llms stream on
:ref:`chat`.  That's also the best way to contact the developers
(other contact methods are in :doc:`/help/index`.


Intended use and resource availability
--------------------------------------

This is ideal if you need to run things against LLMs which are only
running on Aalto servers, and without many requests per second (this
isn't for batch use).  This could, for example, be an alternative to
running your own LLM server for basic testing or small question
answering.

Right now, each models has limited resources (some running on CPUs and
some on GPUs).  They can serve a request every few seconds, but
resources could easily be overloaded.  We intend to add resources as
needed, depending on use.  For any serious use, please contact us so
that we can plan for the future.  Don't assume any stability or
performance right now.
