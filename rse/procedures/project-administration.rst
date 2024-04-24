Project administration
======================

.. note::

   This page is still a working document, discuss anything that
   appears like it should be improved.

Unfortunately (fortunately, since it means our work has value?), we
need to track where our time goes in order
to justify the benefits of what we do.  There are two main uses of the
data:

1) General reporting: being able to say how our time is distributed
   among departments and projects.  This doesn't have to be perfectly
   accurate (and since we have so many small projects, it would be a
   big waste of time to try to be perfect) - but it should be
   roughly proportional to actual time spent.  This is tracked in
   Gitlab.

2) Financial reporting and project payments.  This needs to be
   accurate, but only for the few projects which have special funding.
   The master data is in financial systems, but Gitlab can sometimes
   be used to make this reporting a bit easier.



Typical project flow
--------------------

* Someone will contact us somehow.  We try to get them to the garage
  or a some talk as soon as possible.

* Initial discussion.  If it seems this should be a tracked project,
  then make the issue

* Be aware that it takes some time to get up to speed with a project.
  This should be considered when making the initial estimate, during
  the first consultation.  When recording time spent, include the time
  it takes to get up to speed and learn whatever else is needed for
  the project.



Finance time tracking
---------------------

For projects with their own funding (external or internal funding),
you should get instructions about how to record it.  For many
projects, this is marking them to Halli.  All other projects (funded
by the department's/school's basic funding) is marked in Halli to the
standard RSE salaries project (ask for it).



.. _rse-project-admin-types-of-projects:

Types of projects
-----------------

Special projects
~~~~~~~~~~~~~~~~

Examples: EU-funded projects

Special projects are their own distinct entity and are not mixed with
other work of our team.  They receive dedicated days for their work,
and are not given attention on other days.  Because these get
exclusive days, the master data of these projects is in Halli, and
because Halli can be used for records later, they are not recorded in
Gitlab. (Note: "special" does not mean better, it's usually more
productive to be available for researchers whenever they need us).

Special projects get one Gitlab issue to track the overall contact,
but it isn't updated on a day-to-day basis.

Daily procedures: At the end of every day, record the working time in
Halli.  As much as possible, these project days should not be mixed
with other work, but internal team meetings, etc. are allowed if
necessary.  In Halli, record each day's worktime (scaled to the
standard 7.25h/day) in proportion to the time spent on the special
project (allocated to that project)/internal work (allocated to
RSE-salaries).


Normal funded projects
~~~~~~~~~~~~~~~~~~~~~~

For projects providing their own funding, but aren't special, GitLab
is used to track the time we spend on them.  The
main purpose of Gitlab is to record the department distribution of all
of our basic funding, for which Halli can't hold all the needed information.
Other funded projects which can be intermixed with our normal work can
fit into this category.

Daily procedures: A Gitlab issue is created for every
project and used for each day's work, with funding source
``Funding::Project``.  Time is recorded in Gitlab and may be mixed
with other projects however the customer sees appropriate.  Halli is
marked to the respective project and at least is correct by-month.


Internal charging projects
~~~~~~~~~~~~~~~~~~~~~~~~~~

"Internal changing" projects are funded, but are paid in one sum for a
certain amount of work, and there is no place to mark hours into
Halli.  These are mostly certain types of basic funding.  Gitlab is
used to track time spent on these projects.

Daily procedures: Like above for Gitlab.  Halli is marked to the
standard RSE-salaries project.  ``Funding::Project``


Basic funding projects
~~~~~~~~~~~~~~~~~~~~~~

These projects are paid by our basic funding, provided by our
sponsoring units.  This also includes all of our internal work,
meetings, development, and teaching.

Daily procedures: Same as above.  Gitlab funding marked as
``Funding::Unit``




Gitlab day-to-day procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `the rse-timetracking repository
<https://github.com/AaltoRSE/rse-timetracking>`__ for info on how to use
Gitlab.  But the actual data is in **rse-projects**, a separate
private repository.
