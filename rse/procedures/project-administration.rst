Project management: RSE perspective
===================================


Summary
-------

**Project** is the term used for something large enough to use
tracking.  (Thus "Garage" and "Small" are not considered projects in
this sense, even though we may say "garage projets" and "small
projects" - you can figure it out).

**Garage support** is the term used for Garage and Small projects
(even though "small" is split from garage when talking to management,
internally we would treat them pretty similar).

Procedures by project size
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * * Size
     * Priority
     * How to select
     * When starting
     * When finishing
   * * Garage
     * Top
     * Try to help everyone: help, redirect, or give advice to do themselves.
     * Ask who you are, unit, background.  Ensure you help them at the
       level they need.  Shadow other help sessions to learn new things.
     * Record in `garage diary <https://version.aalto.fi/gitlab/AaltoScienceIT/garagediary>`__ (with unit)
   * * Small
     * Third
     * When garage project needs extra time and you {have time & want} to
       do it.
     * Discuss expectations with customer.  Usually meetings are in
       garage times; record in garage diary for each visit.
     * (none, already in diary)
   * * Medium
     * Lowest (filler)
     * When we have time, in proportion to :doc:`unit priorities
       <units-info>`.

       Confirm in weekly meeting before accepting.
     * Initial triage in garage.  Arrange a detailed planning meeting.
       Usually at least two RSE staff, at one experienced in the topic
       attend.  Invite the customer's supervisor if needed.  Use the
       `template doc
       <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__.
       Make an issue in rse-projects issue tracker if it seems like a
       good project, even if we can't do it.  Await a decision in weekly
       RSE meeting before promising anything.  In the meeting, the
       responsible RSE is decided and they contact the customer.
     * rse-projects issue tracker updated
       (:doc:`../checklists/project-done`).
   * * Large
     * Second (try to do all we can to get outside funding)
     * If there is not enough time for all requests, in proportion to :doc:`unit priorities <units-info>`.
     * Same ^
     * Same ^

Procedures for M/L projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * * Stage
     * What it means
     * How to get here
     * Info stored in
   * * S0 Lead
     * You've learned someone has a vague idea
     * Whoever knows them best talks and explains the ideas of RSE
       stuff.  Give basic expectations.  Ask them if they want to
       proceed.
     * - If vague: nowhere, tell them to contact us again when ready.

       - If they want to proceed: (a) set up the next stage yourself
         or (b) add to weekly meeting agenda to find someone who will
         do the pre-planning meeting.
   * * Pre-planning meeting
     * Discussed enough to work out details before acceptance.
     * Pre-planning meeting with at least two RSEs (doesn't have to be
       those who got the lead, but it's good if someone who might do
       it is there + someone who can mentor that person).  Use the `template doc
       <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__
       or similar.
     * Template doc + `rse-projects
       <https://version.aalto.fi/gitlab/AaltoRSE/rse-projects/>`__
       issue created
   * * S1/S2 Accepted (Waiting / Queued)
     * We've decided we can do the project.
     * Decision in weekly meeting based on pre-planning meeting info.
       Ensure we have time, ensure we have funding.  See if anyone
       else can find new risks.  Final check for who has time to
       actually do the project.  Checklist:

       * Project can be defined
       * A RSE has skills, interest, and *time*
       * Team as whole has time and skills to support

     * Person(s) doing it contact the customer.
   * * S3 In progress
     * It's being worked on.
     * (someone starts working on it)
     * Halli if needed.  Update rse-projects issue periodically.  Keep
       good communication with the customer, for example in the same
       planning doc.
   * * S5 Reporting
     * Project is basically done but we are waiting for stats to add
       to rse-projects before forgetting about it.
     * (finish project)
     * rse-projects issue label
   * * S6 Done
     * Done, don't have to think about it anymore
     * Discuss with customer: what do they need to know from here?
       Add to weekly meeting agenda to discuss lessons leaned.
     * rse-projects issue fully updated with label, summary, time
       spent/saved, and other stats.
   * * S7 Maintenance
     * Project is done but it still occupies our minds since we may be
       asked to do maintenance in the future.
       Add to weekly meeting agenda to discuss lessons leaned.
     * (finish project)
     * rse-projects issue label
   * * S8 Cancelled
     * It was a good project, but we decided not to do it
     * Either we decide we don't have time, or customer decides it is
       no longer needed.
     * rse-projects issue label.


Why project management?
-----------------------

Our project management is designed to:

* Record where our time goes, so that we can get good reports for our
  funders, so that we will continue to be well-funded in the future.
* Show that our output work roughly corresponds to input funding (by
  unit, and goals of those units).
* Avoid projects which we may not be successful at due to {undefined
  goals, impossible goals, or generally not knowing}.
* Prevent over-committing ourselves, so that we start hurting
  ourselves or failing at everything we do.
* Provide sound financial tracking for projects that need it.



Prioritization
--------------

See the summary at the top (G/S/M/L projects)   In short,

* **garage** projects get top priority since they connect us together
  and serve to share skills.
* Then we would do projects preferred by funders (projects with their
  own funding, those from units providing funding).
* Then fill with other things.

Formal criteria can be found in :doc:`prioritization` and
:doc:`units-info`, but you don't need to know these: let the RSE
leader help figure out in the weekly meeting.


Garage and small support
------------------------

Garage projects:


* General guidelines and user support hints:
  :doc:`/tech/online-work-and-support`, :doc:`/tech/user-support`
* Garage support unites us together and provides a way to learn from
  each other.
* It also has a very high impact with un-blocking researchers.
* **Record each help session** in the `garage diary git repository
  <https://version.aalto.fi/gitlab/AaltoScienceIT/garagediary>`__.
  You don't need any other major reporting.  (Try not to make it
  obvious you are asking info for a diary.  Remember to ask at the
  start and try to make it a natural part of "getting to know you".)
* You can choose what projects to work on.  Work with others in the
  garage to figure out who does what (sometimes you may need to "take
  one for the team").
* It's OK to say if we really can't do something, or redirect them to
  better support, or give them homework reading to do before coming
  back to do more.
* If you ever see customers that need interventions (completely not
  prepared to do their work, lack of supervision, mental health
  crisis, coming back too often, etc.)
* If garage starts to get overloaded, bring it up it the weekly RSE
  meeting.

Small projects:

* These are small extensions of garage projects, which you work on
  outside the garage time.
* You shouldn't promise anything you can't do within the few days or
  weeks (this shouldn't become a long-term mental burden for you).
* The customer should be the "prime mover", not you.  That means you
  do what you can, but it's on the customer to come back and make sure
  that things get managed over time.
* You usually meet in garage but can schedule meetings outside of that
  time, too.  Record each garage visit in the garage diary.
* Reporting: this is mixed in with the garage reporting.  It's assumed
  that small projects get more entries in the garage diary
  per-project, and this translates to the yearly report.


Typical project flow
--------------------

This is what should happen for anything bigger than a "small"
project.

Potential project identified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the broad strokes of finding potential projects.

* Anyone may hear of a potential project at any time.  You can tell
  them about the RSE service, what will happen next, and see if they
  are interested.
* You don't have to commit to anything.
* You can discuss the lead at the weekly meeting if you would like
  feedback or someone else to take it over.
* You can use the RSE weekly meeting to find someone else to help make
  the project plan if it's outside of your expertise.
* You usually wouldn't make an issue in ``rse-projects`` yet.  (Info
  on how to do this is in below).  It would me made in cases such as:

  * You are very sure it will become a project (may as well get the
    project number to start tracking).
  * It's a serious request for a lot of resources.  It's useful to
    know what may be requested.
  * It's RSE services being written into a grant application.  It's
    good to know all of these cases for our reports.  RSE leader
    should usually be contacted for grant application stuff.


Project pre-planning meeting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This meetings gets enough details so that we can make a decision.  It
may happen right away (lead comes up in garage) or after some delay
(need to find the people to do the meetings).

* `Pre-planning meeting template doc
  <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__
* The point is to get enough information (for the next step) to know
  if we should take on the project.
* Two RSEs (one of which should be experienced in projects) meet with
  the customers.  This is a good chance for an experienced person to
  mentor someone learning the topic.

  * The supervisor of the customers should be invited if it is
    relevant (it's funded, it needs their direction, etc.)

* Nothing is promised at this time, and planning doesn't have to go
  into technical details.  But it should be deep enough to know if
  there's a technical reason we can't take it on.
* Fill out the project together with the customers.
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


RSE team decision to begin
~~~~~~~~~~~~~~~~~~~~~~~~~~

The project plan as above is brought to the RSE meeting for a go/no-go
decision.

* The project is presented at the meeting to decide if we can or can't
  do it.

  * Project has been defined
  * A RSE has skills, interest, and *time*
  * Team as whole has time and skills to support
  * What is the goal?
  * How do you plan on approaching it?
  * What help do you need?
  * What risks have you discussed?

* This isn't because RSEs need to ask permission, but to make sure we
  think of everything and provide a reasonable change to say "no"
  without it being someone's personal decision.

  * Key point: we don't want to over-commit
  * Others may have experience in the topic and have valuable advice
  * Others may know of other risks

* We will consider things such as:

  * Who has time to do the implementation (it doesn't have to be the
    same person who attended the planning meeting, but it's good if we
    look ahead and likely candidates attend the planning meeting).
  * Does the team overall have time?
  * Are there any risks which weren't discussed in the planning
    meeting?  How to handle them with the customer?
  * Do we think we can actually do it?
  * Funding (RSE leader may give advice on this)


Working on the project
~~~~~~~~~~~~~~~~~~~~~~

* This is mostly independent work.
* RSEs are expected to ask for help if it is needed.  Add an agenda
  item in the RSE weekly meeting if you can't get help in garage or
  you need a wider audience.
* If the project has funding, record time spent in Halli.
* TODO: add more here


Ending the project
~~~~~~~~~~~~~~~~~~

* Update the issue tracker.
* See the :doc:`../checklists/project-done` checklist.
* TODO: add more here



Finance time tracking
---------------------

Halli serves as our source of truth about funded projects.  For
projects with their own funding (external or internal funding), you
should get instructions about how to record it.  All other projects
(funded by the department's/school's basic funding) is marked in Halli
to the standard RSE salaries project (ask for it).



.. _rse-project-admin-types-of-projects:

Notes on special types of projects
----------------------------------

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

Daily procedures: A Gitlab issue is created for every project, with
funding source ``Funding::Project``.  At the end of every day, record
the working time in Halli.  As much as possible, these project days
should not be mixed with other work, but internal team meetings,
etc. are allowed if necessary.  In Halli, record each day's worktime
(scaled to the standard 7.25h/day) in proportion to the time spent on
the special project (allocated to that project)/internal work
(allocated to RSE-salaries).


Normal funded projects
~~~~~~~~~~~~~~~~~~~~~~

For projects providing their own funding, Halli is also used to track
the time spent on them, but you can work on them whenever the
customers request.

Daily procedures: A Gitlab issue is created for every project, with
funding source ``Funding::Project``.  Halli is marked to the
respective project and at least is correct by-month.


Internal charging projects
~~~~~~~~~~~~~~~~~~~~~~~~~~

"Internal changing" projects are funded, but are paid as a lump-sum
internal invoice and Halli is not used.  These projects are not very
common.  Gitlab is used to track time spent on these projects.

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
