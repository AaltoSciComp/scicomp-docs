Project management
==================

.. note::

   This page is still a working document, discuss anything that
   appears like it should be improved.



Unfortunately (fortunately?), we need to track where our time goes in order
to justify the benefits of what we do.  There are two main uses of the
data:

1) General reporting: being able to say how our time is distributed
   among departments and projects.  This doesn't have to be perfectly
   accurate (and since we have so many small projects, it would be a
   big waste of time to try to be perfect) - but it should be
   asymptotically correct.  This is tracked in Gitlab.

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



Gitlab commands and project metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The full documentation of the GitLab commands is in the
rse-timetracking project readme:
https://github.com/AaltoRSE/rse-timetracking .
