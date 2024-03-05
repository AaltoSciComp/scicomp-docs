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

The API doesn't have it's own detailed documentation (ask us), but the
API should be OpenAI compatible (for chat models) so many existing
libraries work automatically.


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
plenty of opportunity for scaling, but this is not turned on until a
need is established.  CPU resources are significant, but there are
limited GPU resources (but that can change, depending on demand).
