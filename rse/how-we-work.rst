Starting a project with us
==========================

This page is mostly focused on how long-term scheduled projects, which
are funded by the research groups themselves, work.
**Long-term projects** are scheduled by fraction of full-time-equivalent
(FTE) over weeks or months.

For short-term code review tasks, come to any of our :doc:`garage
sessions </help/garage>` and we will immediately take a look.



Types of service
----------------

* **Long-term** service deals with jobs that last months, and are
  scheduled in terms of FTE percentage over months.  This is often
  directly as salary from some grant, as a researcher would be.

* **Medium-term** service deal with jobs scheduled in days.  This is
  mostly funded by basic funding from the member units.

* **Short-term** usually consists of support at one of our
  :doc:`garages </help/garage>` or a few hours of work.  This is
  generally free (paid by unit basic funding).



Beginning
---------

To actually make a request for support, see :doc:`request`.


Initial meeting
~~~~~~~~~~~~~~~

First, you can expect an quick initial meeting between the researchers
and RSEs.  Depending on the size and complexity of the project, there
may be several to find the right RSE and ensure that we can do a good
job helping you.

* What scientific background knowledge is needed?  How long does it take to get
  started?
* What type of contribution will the RSE make (see next section)?  For
  purposes of
  scientific integrity, consider if this reaches the point of
  scientific authorship (see bottom).
* Researchers: provide access to code, documentation, and relevant
  scientific background in advance, so
  that they can be browsed.  The more we know in advance, the better
  we can estimate the time required and how to best help you.
* How do you manage your data?  To map things out, consider `this
  one-page data management plan table
  <https://drive.google.com/drive/folders/0BzlGN0F6ew2hc0hGVXVTaGZwQjQ>`__.
* Final outputs, location, publication.
* Time frame and schedule flexibility.


What we can accomplish
~~~~~~~~~~~~~~~~~~~~~~

It is very important to consider what the practical outcome of the
project will be, because different researchers have very different
needs.  Together, we will think about these questions:

- What's the object of focus

  - Software

  - Data

  - Workflows

- What is accomplished?

  - Create a brand-new product based on scientific specification.  Is
    this done in an agile way (continuous feedback) or is the exact
    result known?

  - Improve some existing workflow or software, possibly drastically.

  - Improve some other project, primarily maintained by someone else.

  - Prepare a project for publication, release, or being used by more
    people.

- Future plan

  - Primarily teach via example, so that the researcher can fully
    continue developing the project themselves.

  - Provide a finished product, which won't need updates later

  - Provide a product that will be continually maintained by
    specialists (RSEs or similar - us?).


Scheduling and planning
~~~~~~~~~~~~~~~~~~~~~~~

RSEs will be assigned based on discussion between the researchers,
RSEs, and Aalto Scientific Computing (the RSE group).  Your agreement is
with the RSE group, so your RSEs may change if there is a need (even
though we'll try to avoid this).

We will work with you to give a good view of how long we take
something will take and any risks (as in, what if it turns out to not
be possible?)  We can't promise specific results in a specific time
(no one can), but we do try to give the best estimates we can.  This
planning includes any buffer and backup plans.

It may take some time to fit your project into our schedule (of course
this also depends on the urgency.)  We realizes that your schedule is
also uncertain, but we hope that you can find time to work with us
once we start, since otherwise we may move on and requeue your
project.

If we schedule a project but lose contact with you (no responses to
our messages), we'll assume you are busy with other things and may
re-add the project to the queue, and we'll need to find a new time in
the schedule.  Please let us know if you don't have time, we
understand the busyness of research.

A project doesn't have to be done "all at once" but can be interleaved
with your own work schedule.



Costs and time tracking
~~~~~~~~~~~~~~~~~~~~~~~

We track the time we spend and record it to your project.



Getting started
---------------

Version control
~~~~~~~~~~~~~~~

One can hardly do development work without using a good version
control system.  Our first step will be help you start using a version
control system, if you are not yet using one, or if you are ensure you
are using it optimally.  If you don't have a preference, we'll
recommend git and GitHub / Aalto Gitlab.

Research background
~~~~~~~~~~~~~~~~~~~

If some understanding of the scientific background wasn't important,
you might be hiring a software developer instead.  Expect us to take
some time to understand the science.

Understanding existing code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Also expect that, if there is any existing code, it will take some
time to understand for a new person.  Also, there is likely to be a
period of refactoring to improve the existing code, where it seems
like not much is getting done.  This is a necessary step in investing
for the future.



During the project
------------------

Our RSE will most likely want to go work with you, in your physical
location (well, after corona-time), a lot of the time.  It would be
good to arrange a desk area as close as possible to existing
researchers.  "Mobile-space" but close is better than fixed but
further.

Our goal isn't just to provide a service, but to teach your group how
to work better yourselves after the project.

Software quality and testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software which is untested can hardly be considered scientific.  We
will work with you to set up a automatic testing framework and other
good practices so that you can ensure software quality, even after the
project.  This also ensures faster and more accurate development in
the future.  We'll teach you how to maintain this going forward.  This
is in proportion to the complexity of the project and need.

We also pay particular attention to the maintenance burden of
software: you'll be using software much longer than you write it.  We
aim for simple, reliable strategies rather than the fanciest things
*right now*.

..
  Overheads
  ~~~~~~~~~

  No person can work 100% of the time on a project, some time is needed
  for management and overheads.  Our RSEs as researchers focused on
  software quality, who have other responsibilities to deal with.  On
  the other hand, it is exactly these overheads that allow us to
  continue supporting you after the project is over.  These overheads
  also connect you to the broader Aalto Scientific Computing community.

  For long-term projects (percent of FTE over months) and medium-term
  projects (days), assume the time includes all of these overheads and
  efficiency is ~75%.

  For short-term projects scheduled by hours, overhead isn't expected.



After the project
-----------------

We don't want to drop support right after the project (that's why you
work with us, not an external software developer).  Still, we have
finite resources and can't fund work on one project from another, so
can't do everything for everyone.  You can expect
us to try to passively keep supporting you for during the "daily
garage" time as best we can.

If your department or unit provides basic funding (see the
:doc:`implementation plan <procedures/implementation>`), then long-term service
is included, and this has no limits.  However, this is shared among
everyone in your unit, and focused on strategically support that helps
many people.

.. _rse-how-we-work-kpis:

Tracking scientific benefits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We need to record the benefits of this service:

* Researcher time saved
* Computer time saved
* Number of papers supported
* Software released or contributed to
* Open science outcomes (e.g. open software, data management)
* New work made possible (e.g. grant or project wouldn't have been
  possible)
* Qualitative experience: increased satisfaction, educational
  outcomes, etc.


Releasing the software
~~~~~~~~~~~~~~~~~~~~~~

A key goal of our support is releasing the software for broader use in
the community (open science).  Ideally, this will be a continual
process (continue releasing as development goes forward), but we can
prepare you for a first release later on, too.

We recognize the need to maintain a competitive advantage for your own
work, but at the same time, if your work is not reproducible, it's not
science.  We'll work with you to find the right balance, but a common
strategy is some core is open, while your actual analysis scripts
which make use of that core are released with your articles.



Academic credit
~~~~~~~~~~~~~~~

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



Acknowledging us
----------------

You can acknowledge us as "Aalto Research Software Engineering
service" or "Aalto RSE".  In papers/presentations, please acknowledge
us if we significantly contribute to your work.

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
