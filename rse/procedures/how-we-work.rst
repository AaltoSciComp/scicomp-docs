How we work
===========

.. warning::

   This page is still in draft form


This page is mostly focused on how long-term scheduled projects, which
are funded by the research groups themselves, work.
**Long-term tasks** are scheduled by FTE over weeks or months.

For short-term code review tasks, come to any of our :doc:`garage
sessions </help/garage>` and we will immediately take a look.

Types of service
----------------

* **Long-term** service deals with jobs that last months, and are
  scheduled in terms of FTE percentage over months.  This is often
  directly as salary from some grant, as a researcher.

* **Medium-term** service deal with jobs scheduled in days.  For
  simmplicity, these are often fee-for-service paid internally from
  basic funding.  Depending on your unit, they may also be free (paid
  by unit basic funding)

* **Short-term** could be a code review at one of our :doc:`garages
  </help/garage>` or a few hours of work.  This is generally free
  (paid by unit basic funding).


Beginning
---------

Check if it is a type of task that we can do: TODO

To actually make a request for support, see :doc:`request`.


Initial meeting
~~~~~~~~~~~~~~~

First, you can expect an quick initial meeting between the researchers
and RSEs.  Depending on the size and complexity of the project, there
may be several to find the right RSE and ensure that we can do a good
job helping you.

* What background knowledge is needed?  How long does it take to get
  started?
* What type of contribution will the RSE make?  For purposes of
  scientific integrity, consider if this reaches the point of
  scientific authorship.
* Researchers: provide access to code and documentation in advance, so
  that they can be browsed.  The more we know in advance, the better
  we can estimate the time required and how to best help you.



Scheduling and planning
~~~~~~~~~~~~~~~~~~~~~~~

RSEs will be assigned based on discussion between the researchers,
RSEs, Aalto Scientific Computing (the RSE group).  Your agreement is
with the RSE group, so your RSEs may change (even though we'll try to
avoid this).

We can never promise specific results in a specific time: we always
agree based on a certain amount of time.  As you can expect, projects
can sometimes take far longer than expected, so we try to budget
plenty of buffer into projects to accomplish the mandatory tasks.

Our exact scheduling system is not yet decided: if you start now, you
help design the system.

Costs and time tracking
~~~~~~~~~~~~~~~~~~~~~~~

TODO


Funding practicalities
~~~~~~~~~~~~~~~~~~~~~~

TODO


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
the future.  We'll teach you how to maintain this going forward.

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
finite resources and can't do everything for everyone.  You can expect
us to try to passively keep supporting you for about as long as your
project lasted.

If your department or unit provides basic funding (see implementation
plan), then long-term service is included, and this has no limits.
However, this is shared among everyone in your unit, and focused on
strategically support that helps many people.

Releasing the software
~~~~~~~~~~~~~~~~~~~~~~

A key goal of our support is releasing the software for broader use in
the community (open science).  Ideally, this will be a continual
process, but we can prepare you for release later on, too.

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



See also
--------

* `UCL RSE group processes
  <https://www.ucl.ac.uk/isd/services/research-it/research-software-development/what-to-expect-when-working-rsdg>`__:
  That page heavily inspired this page.  Broadly, most of what you
  read there also applies to us.
