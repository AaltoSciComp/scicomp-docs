Project lifecycle
=================

This page describes what you can expect during a project.


Background
----------

Remember that we don't do projects in isolation - our help is part of
a complete support package.  Even before you have a "project", you can
come to a :doc:`garage office hour </help/garage>` for help (and in
fact, this is the recommended way to start a project).

.. figure:: https://github.com/AaltoSciComp/aaltoscicomp-graphics/blob/master/figures/project-steps.png?raw=true
   :alt: A flowchart diagram, of which me main point is that you can
	 request short-term "garage" support as much as you want, and
	 it can get upgraded to a "project" if it's a big enough
	 task.  The project should have a clear planning meeting in it
	 and we'll verify that we have enough time before accepting.

   Project management diagram.  The main point is short stuff is free
   and easy in garage, and from garage we can upgrade to longer projects.


Requesting
----------

Come to the `SciComp garage </help/garage>` or see :doc:`contact`.
You can always chat with us for initial brainstorming.


Every project is unique
-----------------------

The below has the most important steps, but they are often combined or
skipped when the answers are clear.


Idea meeting
------------

We discuss the needs broadly and possibly non-technically, to help our
customers understand what is possible and how projects might look.  We
will try to gather all the relevant people, including PIs if relevant,
to make sure that everyone has the same idea of the project and its
goals.

We will often start brainstorming in our `project plan template
<https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk/>`__
(which can also serve as running notes, if there isn't a better
place).

.. admonition:: Topics
   :class: dropdown

   * What is the actual need and ultimate goal, and what is the best way
     to get there?  (We can often find easier paths than you might think)
   * What is feasible to accomplish?
   * Is Aalto RSE the right team to do this?
   * Setting up communication channels: who is involved, shared drive
     place for notes and documents.
   * Risks and risk management.
   * Time frame, deadlines, and long-term maintenance.
   * How will data be managed?  To map things out, consider `this
     one-page data management plan table
     <https://drive.google.com/drive/folders/0BzlGN0F6ew2hc0hGVXVTaGZwQjQ>`__.
   * What access or permissions ares needed?
   * Any relevant ethical or security issues?
   * Acknowledgments and authorships. (Actually decided later, but
     discussing basic principles.  We are not mainly looking for
     authorships but sometimes our work might reach that level.)
   * Funding if needed (at least initial discussion to be followed up later).


Technical planning meeting
--------------------------

A possibly smaller set of people get together and discuss the actual
implementation steps.  The goal is to get a shared understanding of
what actual steps will be taken and by who and set the overall
timeline and phases of the project.  Of course, sometimes such advance
planning is not possible, then we plan how the uncertainty is handled.

After this, we should be able to determine if we can commit resources
and on what timeframe.

.. admonition:: Scheduling and planning
   :class: dropdown

   RSEs will be assigned based on discussion between the researchers,
   RSEs, and Aalto Scientific Computing (the RSE group).  Your agreement is
   with the RSE group, so your RSEs may change if there is a need (even
   though we'll try to avoid this).

   We will work with you to give a good view of how long we take
   something will take and any risks (as in, what if it turns out to not
   be possible?)  We can't promise specific results in a specific time
   (no one can), but we do try to give the best estimates we can -
   however, estimating within research projects can be extremely
   difficult, because the development is so closely tied to research and
   most projects have unique challenges.  This planning includes any
   buffer and backup plans.

   It may take some time to fit your project into our schedule (of course
   this also depends on the urgency.)  We realizes that your schedule is
   also uncertain, but we hope that you can find time to work with us
   once we start, since otherwise we may move on and requeue your
   project.

   If we schedule a project but lose contact with you (no responses to
   our messages), we'll assume you are busy with other things and may
   re-add the project to the queue, and we'll need to find a new time in
   the schedule.  In other words, we don't change for no-shows, but you
   may lose your place in the queue.  Please let us know if you don't
   have time, we understand the busyness of research.

   A project doesn't have to be done "all at once" but can be interleaved
   with your own work schedule.  In other words, we can work 25-50% for
   multiple months, as you may need.

.. admonition:: Typical concerns when getting started
   :class: dropdown

   **Version control.**
   One can hardly do development work without using a good version
   control system.  Our first step will be help you start using a version
   control system, if you are not yet using one, or if you are ensure you
   are using it optimally.  If you don't have a preference, we'll
   recommend git and GitHub / Aalto Gitlab.

   **Research background.**
   If some understanding of the scientific background wasn't important,
   you might be hiring a software developer instead.  Expect us to take
   some time to understand the science.

   **Understanding existing code.**
   Also expect that, if there is any existing code, it will take some
   time to understand for a new person.  Also, there is likely to be a
   period of refactoring to improve the existing code, where it seems
   like not much is getting done.  This is a necessary step in investing
   for the future.

   **Software quality and testing.**
   Software which is untested can hardly be considered scientific.  We
   will work with you to set up a automatic testing framework and other
   good practices so that you can ensure software quality, even after the
   project.  This also ensures faster and more accurate development in
   the future.  We'll teach you how to maintain this going forward.  This
   is in proportion to the complexity of the project and need.

   **Maintenance.**
   We also pay particular attention to the maintenance burden of
   software: you'll be using software much longer than you write it.  We
   aim for simple, reliable strategies rather than the fanciest things
   *right now*.





Implementation
--------------

The researchers and research engineers work together to accomplish the
project.  You can expect active communication, but at the same time we
need you to be involved and responsive, otherwise we may have to
re-allocate our time.  We all know research is iterative and
exploratory, and we would rather meet with you frequently to work with
you rather than work to a specification.

.. admonition:: Workspaces
   :class: dropdown

   We can work online or visit/join your own group work spaces.  We
   should be as close to you as possible, whether that is online or
   in-person.  Our goal isn't just to provide a service, but to teach
   your group how to work better yourselves after the project.

*Proof of concept: Sometimes, it's unknown if an idea will even work
(we are researchers, after all).  Thus, it may be wise to have a
minimal proof of concept to check if the basic idea is functional
before going too deep.  It may be possible to accomplish this even
before funding is decided or without funding.*


.. _rse-how-we-work-kpis:

Project finishing and maintenance
---------------------------------

We should ensure that at some point a project is closed, so that our
resources are freed up.  As shown in the first figure on the page, we
do not disappear: we attempt to continue with minor help as our time
allows (that's why you work with us, not consultants).

We will want to get some basic stats once the project has finished,
and for this we need to define some "end point".

.. admonition:: Tracking outcome and benefits
   :class: dropdown

   We need to record the benefits of this service for our university
   sponsors.  Typical things include:

   * Researcher time saved
   * Computer time saved
   * Number of papers supported
   * Software released or contributed to
   * Open science outcomes (e.g. open software, data management)
   * New work made possible (e.g. grant or project wouldn't have been
     possible)
   * Qualitative experience: increased satisfaction, educational
     outcomes, etc.

   Some of these may not be immediately known, so we may follow up and
   ask later on.  Please answer any surveys or messages.

.. admonition:: Open science and societal benefit
   :class: dropdown

   A key goal of our support is releasing things for broader use in
   the community (open science), **but of course the choice is up to
   you**.  Ideally, open science is a continual process (continue
   releasing as development goes forward), but we can prepare you for
   a first release later on, too.

   We recognize the need to maintain a competitive advantage for your
   own work, but at the same time, if your work is not reproducible,
   it's not science.  We'll work with you to find the right balance,
   but a common strategy is some core is open, while your actual
   analysis scripts which make use of that core are released with your
   articles.

.. admonition:: Academic credit
   :class: dropdown

   Our RSEs do creative scientific work on your projects, which
   (depending on scope) can rise to the level of scientific authorship.
   This should be discussed early in the project.

   * The software-based
     scientific creativity can be different than what is published in your
     articles: in this case, it can make sense to release the software
     separately.

   * This is not to say that RSEs who work on a project should always
     be authors, but it should be considered at the start.  See `TENK
     guidelines on research integrity (authorship section)
     <https://tenk.fi/en/advice-and-materials>`__.

   * A contributing that is significant enough to become scientific
     novelty and such that the programmer must take responsibility for
     the outcome of the work usually rises to the level of
     co-authorship.

   * It is OK to consider the code authorship as a separate output from
     the scientific ideas, and the RSE can help properly publish the
     code so that it is citeable separately from the paper.


.. admonition:: Acknowledgements
   :class: dropdown

   You can acknowledge us as "Aalto Research Software Engineering
   service" or "Aalto RSE".  In papers/presentations, please acknowledge
   us if we significantly contribute to your work.

   For research outputs which appear in ACRIS (paper, data), you can
   :ref:`tag them with the Science-IT infrastructure <acris-link>`.

   When talking with/presenting to your colleagues, please do talk about
   our services and its benefits.  Our link is
   https://scicomp.aalto.fi/rse/ .  Word of mouth is the best way to
   ensure our funding to continue to serve you.



See also
--------

* `UCL RSE group processes
  <https://www.ucl.ac.uk/isd/services/research-it/research-software-development/what-to-expect-when-working-rsdg>`__:
  That page heavily inspired this page.  Broadly, most of what you
  read there also applies to us.
