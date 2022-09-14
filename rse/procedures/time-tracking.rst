Time tracking
=============

.. warning::

   This page is still in draft form and being discussed and
   developed - it is *only a proposal*.  See the note on the parent
   page.

   This proposal may turn out to be especially bad... please comment.

Unfortunately (fortunately?), we need to track where our time goes in order
to justify the benefits of what we do.  There are two main uses of the
data:

1) General reporting: being able to say how our time is distributed
   among departments and projects.  This doesn't have to be perfectly
   accurate (and since we have so many small projects, it would be a
   big waste of time to try to be perfect) - but it should be
   asyptotically correct.  This is tracked in Gitlab.

2) Financial reporting and project payments.  This needs to be
   accurate, but only for the few projects which have special
   funding.  The master data is in financial systems, but Gitlab can
   be used to make this reporting a bit easier.



Finance time tracking
---------------------

For projects with their own funding (external or internal funding), they
should be marked in Halli.  All other projects (funded by the
department's/school's basic funding) is marked to the standard RSE
project (ask for it), and this time is accounted for at the end of
each year (using internal corrections).



Internal time tracking
----------------------

(This section is for our RSEs)

GitLab is used to track all projects and time we spend on them.
Projects have labels that describe them, and GitLab ``/estimate`` and
``/spend`` commands are used to record time spent.

* Be aware that it takes some time to get up to speed with a project.
  This should be considered when making the initial estimate, during
  the first consultation.  When recording time spent, include the time
  it takes to get up to speed and learn whatever else is needed for
  the project.
* Include typical daily overheads into project time (imagine you are a
  researcher - how much time do you spend doing other support
  activities?  Use that model).
* When being paid by projects (in the Finance systems), we need to
  *only* record time actually
  spent on that project.  Thus, the rest of your time should still be
  recorded to the common RSE project in the finance system.

Day-to-day procedure
~~~~~~~~~~~~~~~~~~~~

* Record new projects in GitLab.  Most short garage consultations are
  not recorded in GitLab, unless there is some sort of extra
  communication about it.

  * Look through the list of labels and set any relevant labels onto
    the project.  Use ``/estimate`` to make some time estimate (wild
    guess - hour? day?  week?  month?)

  * There is an issue template that can be used for basic starting
    info (and also it is also in :doc:`templates`).

* We discuss the next steps in a weekly meeting, if it's not obvious.

* Each time you spend time on a project, use ``/spend`` to record
  time.  (for example, ``/spend 4h`` or ``/spend 2d``).



Gitlab commands:
~~~~~~~~~~~~~~~~

* Use these within the issue as a comment, to control the time
  allocation.
* ``TIME-RECORD`` has the form ``XXmoYYwZZdUUhVVm`` for ``XX`` month, ``YY``
  weeks ``ZZ`` days ``UU`` hours and ``VV`` minutes.
* Time units: Months (``mo``), Weeks (``w``), Days (``d``), Hours (``h``),
  Minutes (``m``). Default conversion rates are 1mo = 4w, 1w = 5d, and 1d = 8h.
* ``/estimate TIME-RECORD`` - estimate total time a project make take.
  Used as
  soon as possible at beginning of a project, can always be updated
* ``/spend TIME-RECORD [YYYY-MM-DD]`` - announce that you have spent a
  certain amount of time
  on the project, you can give an optional date for the spent time.
* ``/timesaved TIME-RECORD [YYYY-MM-DD]`` - estimate total researcher time
  saved, this is important for us to see how efficient we are.

Project management and results:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most projects should have a few details associated with them, like contact
details of the requesting researcher and potentially also their supervisor.

Gitlab commands for project details:

* ``/contacts EMAIL[, EMAIL [...]]`` - who we usually communicate with,
  note that these people will get update emails, when the project is updated.
* ``/supervisor EMAIL[, EMAIL [...]]`` - PI(s) responsible for research (not
  usually contacted)
* ``/summary TEXT`` - text to be added to the summary bullet points of this
  project. Takes the whole note as text, but should be a single sentence.


For an overview of our work we try to keep track on what kind of results are
supported by it. For this we keep a record of associated publications either
in the form of papers, software or datasets. It is also interesting to see
how many researchers benefited from any given project, so we keep track of
those, this number can easily increase at a later point if software we
produced or systems we set in place are used by more people.

Gitlab commands for project outcomes:

* ``/projects INT`` - number of researcher projects supported by this RSE project
* ``/publications INT`` - number of publications supported by this RSE project
* ``/software INT`` - number of software packages supported by this RSE project
* ``/datasets INT`` - datasets supported by this RSE project
* ``/outputs INT`` - number of open science outputs produced other than the categories above





