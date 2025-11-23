Project management: RSE perspective
===================================


Summary
-------

.. list-table::
   :header-rows: 1

   * * Size
     * Priority
     * How to select
     * When starting
     * When finishing
   * * Garage
     * Top
     * Try to help everyone
     * Ask who you are, unit, background.  Ensure you help them at the
       level they need.  Shadow other help sessions to learn new things.
     * Record in garage diary with unit
   * * Small
     * Third
     * When you feel a garage project is helped by the extra time.
     * Record in garage diary for each visit.  Usually meetings are
       limited to garage times.
     * (none, already in garage)
   * * Medium
     * Lowest (filler)
     * When we have time, in proportion to :doc:`unit priorities <units-info>`.
     * Initial triage in garage.  At least two RSE staff, one experienced
       in the topic, arrange a planning meeting (either in garage or a
       separate time).  Invite the supervisor if needed.  Use the
       template doc.  Make an issue in rse-projects issue tracker, even
       if we can't necessarily do it.  Await a decision in weekly RSE
       meeting before promising anything.  In the meeting, the
       responsible RSE is decided and they contact the customer.
     * rse-projects issue tracker updated
       (:doc:`../checklists/project-done`).
   * * Large
     * Second (try to do all we can to get outside funding)
     * If there is not enough time for all requests, in proportion to :doc:`unit priorities <units-info>`.
     * Same ^
     * Same ^

**Project** is the term used for something large enough to use
tracking.  "Garage" and "Small" are not considered projects in this
sense.  (Sometimes we may say "small project" or "garage project" but
we should understand these don't have the whole tracking).

**Garage support** is the term used for Garage and Small projects
(even though "small" is split from garage when talking to management,
internally we would treat them pretty similar).


Why project management?
-----------------------

Our project management is designed to:

* Record where our time goes, so that we can get good reports to our
  funders, so that we will continue to be well-funded in the future.
* Prevent beginning projects which we may not be successful at due to
  {undefined goals, impossible goals, or generally not knowing}.
* Prevent over-committing ourselves, so that we run out of time and
  can't work well.
* Provide sound financial tracking


Definitions
-----------


Prioritization
--------------

See :doc:`prioritization`.  In short:

* Attend **garage** and support whatever you can there.  Record it in the
  garage diary.
* When you have time, upgrade garage projects to **small** projects.
  Meet in the garage and record.
* When you notice something larger, bring it to the weekly RSE meeting
  to see if we have time.
* Then we want to focus on **large** projects, since they provide our
  funding.
* Then **medium** projects fill the rest of the time.


Garage and small support
------------------------

Garage projects:

* Garage support unites us together and provides a way to learn from
  each other.
* It also has a very high impact with unsticking projects.
* **Record each help session** in the `garage diary git repository
  <https://version.aalto.fi/gitlab/AaltoScienceIT/garagediary>`__.
  You don't need any other major reporting.  (Don't make it obvious
  you are asking info for a diary.  Remember to ask at the start and
  try to make it a natural part of "getting to know you".)
* You can choose what projects to work on.  Usually you can figure out
  with others in the garage what's most important and what you need to
  do vs can let someone else do.
* If we seem to not have resources to handle all the garage projects,
  are there are some that no one wants to do, bring it up in the
  weekly RSE meeting.

Small projects:

* These are small extensions of garage projects, which you work on
  outside.
* You shouldn't promise anything you can't do within the few days or
  weeks (this shouldn't become a long-term mental burden for you).
* The customer should be the "prime mover", not you.  That means you
  do what you can, but it's on the customer to come back and make sure
  that things get managed over time.
* You can schedule more meetings if you want outside of garage time,
  if it makes sense.  Record meetings in the garage diary.
* Reporting: this is mixed in with the garage reporting.  It's assumed
  that small projects get more entries in the garage diary
  per-project, and this translates to the yearly report.


Typical project flow
--------------------

This is what should happen for anything bigger than a "small"
project. I apologize for calling these "gates".

G0: Potential project identified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the broad strokes of finding ideas.

* Anyone may hear of a potential project at any time.  You can
  introduce them to the idea that this may become a project and give
  them an idea of what may happen next.
* You don't have to commit to anything.
* You can discuss things at this stage in the weekly meeting if it
  would help you provide feedback to them.
* You can use the RSE weekly meeting to find someone else to help make
  the project plan (G1) if it's outside of your expertise (or a second
  person to provide more insight).
* You usually wouldn't make an issue in ``rse-projects`` yet.  (Info
  on how to do this is in below).  It would me made in cases such as:

  * You are very sure it will become a project (may as well get the
    project number to start tracking).
  * It's a serious request for a lot of resources.  It's useful to
    know what may be requested.
  * It's RSE services being written into a grant application.  It's
    good to know all of these cases for our reports.


G1: Project planning meeting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This phase makes a project somewhat more concrete, so that we can
decide if we want to do it or not.

* Two RSEs (one of which should be experienced in projects) meet with
  the customers.

  * The supervisor of the customers should be invited if it is
    relevant (it's funded, it needs their direction, etc.)

* Nothing is promised at this time, and planning doesn't have to be
  that deep.  The point is to get enough information (for the next
  step) to know if we should take on the project.
* Fill out the project starting template together with the customers.
  Make a copy in some shared space, give everyone edit access, and
  start filling out.
* The purpose of this meeting is to set expectations

  * What the actual need and outcome may be
  * What we actually can do and may have time to do
  * How hard the project will be
  * How much time it might take us
  * What the risks are (including risks that we just can't do what is
    needed, or it's not as useful as one would hope)
  * What each party needs to do
  * Who will manege it long-term
  * Funding

* At this point, there probably should be an issue made in
  rse-projects.

  * The readme in the `rse-timetracking repository
    <https://github.com/AaltoRSE/rse-timetracking>`__ describes how
    the rse-projects repository works
  * `rse-projects itself is private in Aalto GitLab
    <https://version.aalto.fi/gitlab/AaltoRSE/rse-projects/>`__.


G2: RSE team decision to begin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project plan as above is brought to the RSE meeting for a go/no-go
decision.

* It's presented at the meeting to decide if we can or can't do it.
* This isn't because RSEs need to ask permission, but to make sure we
  think of everything and provide a reasonable change to say "no"
  without it being someone's personal decision.

  * Key point: we don't want to over-commit

* We will consider things such as:

  * Who has time to do the implementation (it doesn't have to be the
    same person who attended the planning meeting, but it's good if we
    look ahead and likely candidates attend the planning meeting).
  * Does the team overall have time?
  * Are there any risks which weren't discussed in the planning
    meeting?  Do we think we can actually do it?
  * Funding (RSE leader may give advice on this)


Working on the project
~~~~~~~~~~~~~~~~~~~~~~

* If the project has funding, record time spent in Halli.
* TODO: add more here


Ending the project
~~~~~~~~~~~~~~~~~~

* See the :doc:`../checklists/project-done` checklist
* TODO: add more here



Finance time tracking
---------------------

For projects with their own funding (external or internal funding),
you should get instructions about how to record it.  For many
projects, this is marking them to Halli.  All other projects (funded
by the department's/school's basic funding) is marked in Halli to the
standard RSE salaries project (ask for it).



.. _rse-project-admin-types-of-projects:

Special project types
---------------------

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
