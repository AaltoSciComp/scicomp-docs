New group leaders: what to know about computational research
============================================================

As a new group leader, how can you make the most of your future
group's computational work, so that it becomes an investment rather
than a liability?  This is currently focused on software.

If you are actively writing research software yourself, perhaps
directly check out :doc:`zen-of-scicomp` instead of this for the more
practical side.



About you
---------

* Are you planning a research group which partly uses computing
* Is your computing not your main thing (not what you want to focus
  on/not what you studied)?
* Do you want your new hires to use best practices, even if you can't
  mentor them yourself?
* Do you want your research to be reproducible and open?


Why plan in advance?
--------------------

* Your group's work is valuable.
* Over time, your work's value can grow...
* ... or it can be lost every 5 years as your group changes.



What usually goes wrong?
------------------------
At a group level, these often happen to semi-computational groups:

* Every researcher starts a project over from scratch
* Researchers leave, previous work becomes unusable (your group
  completely changes every ~5 years!)
* If you don't work at it, your group's software and data gets more
  and more disorganized, until it becomes unusable.  It limits what
  you can do in the future.

At an individual level:

* Time wasted with bugs
* Time wasted when one can't repeat analysis for reviews
* Desire to hide or not share code because it's "messy", which
  promotes the above cycle continuing.  And less Open Science.



Step 1: Define how you work together
------------------------------------
This is kind of meta, but: do you want to be a group of people
connected by supervisor, or a team that works together?

- Is co-working limited to coffee chats and presentations at group
  meetings?

  - Do these presentations comment only on the final results?
  - Or do you discuss and praise good practices for getting those
    results?
  - Are some meetings spent on skill development?

- Or on the other end, are you co-developing the same project?
- Are you a team, or a bunch of independent contractors?

.. admonition:: Suggestions

   * Don't be only  results oriented in your group activities.  Make
     sure you value the process with both your time and mental
     energy.



Planning vs writing a plan
--------------------------
     Plans are useless, planning is indispensable *- Dwight Eisenhower*

* Different grants request you make a **data management plan** and
  I've seen ideas of **software management plan** for the future.
* If you making a plan just for a grant, I think that's the wrong
  idea.  You want everything you do to *go beyond single projects.*

.. admonition:: Suggestions

   * Make a "practical plan" for important aspects, in your
     group's documentation area: "here is where you find our data",
     "here is where we share code", etc.  Keep it lightweight but
     useful.
   * Designate it as part of onboarding.
   * Update it as needed.



Group documentation, "group wiki"
---------------------------------
A single place for reference on groups practices helps with onboarding
and keeping things consistent and usable over time.

- A group wiki is a good place to start.
- Minimum documentation about how you want things done - or how they
  are *actually* being done.
- But not so strict that you can't make progress in the future.
- Index of important software, data, and other resources

  - But description of the software/data should be with the them, not
    in the group docs.

- Can you make everything open.  e.g. your group website contains this
  reference information, so it also serves as an advertisement?

.. admonition:: Suggestions

   * If in doubt, make a group wiki
   * Use it to keep your group's internal operating information
     organized - however makes sense for you.
   * When you hear of someone doing something new, ask: "did you
     update this in our wiki?"



Skill development
-----------------

Many people learn basic programming.  Far fewer people learn best
practices *beyond* programming:

- This, especially version control, is covered very well in the
  `CodeRefinery workshop <https://coderefinery.org>`__, twice a year.
- Consider attending a CodeRefinery as a team
- If you use lots of computing: :doc:`Aalto Introduction to Scientific
  Computing and HPC </training/scip/kickstart-2022-summer>`
- Train early, before getting started with bad practices that can't be
  changed.

But there is also informal learning, **mentoring**:

- You learn more from co-working than courses.
- You need good, active mentoring (not weekly status checks, but real
  co-working)
- Desks next to each other where you can see each others screens
- Pair programming
- But, as an academic supervisor, you probably don't have time to
  mentor.  How do you get mentoring?

  - Set up group to work together
  - Time and motivation for self-learning
  - Encourage a internal specialist who can mentor for you ("Research
    software engineer").

.. admonition:: Suggestions

   * Everyone in your group attends a `CodeRefinery workshop
     <https://coderefinery.org>`__
   * At least one group member is developed into a computational
     specialist and supports others.



Why talk so much about teaching and mentoring, rather than practices?
---------------------------------------------------------------------

* Unlike many topics, we can't rely on academic courses to prepare
  your group members.
* In all my experience, good software and data practices comes from
  sharing good internal practices.
* I know supervisors can't do everything, but hopefully they can
  promote what they need internally.



Software in research
--------------------

* Software allows you to do far more than one can alone and transform research.
* ... but can also be one of the most complex tasks you do.

* What kind do you use?

  * You can and will use software developed by others
  * Many groups develop their own internally.
  * If you make something good, you may want to release it so that
    others can use it - and cite you.



Software: tools
---------------

We give a lightning overview.  Come to `CodeRefinery
<https://coderefinery.org>`__ for the full story.

Version control
~~~~~~~~~~~~~~~
* Tracks changes

  * solves: Everything just broke but I don't know what I changed.
  * solves: I'm getting different results than when we submitted the
    paper.

* Allows collaboration

  * solves: "can you send me the latest version of the code"
  * solves: "we're using two different versions, too bad"

* Creates a single source of truth for the code

  * Not different scattered around on everyone's computers

* Most common these days: :doc:`git </scicomp/git>`

.. admonition:: Suggestions

   * Everyone must learn the basics of a version control system
     (CodeRefinery week 1 does this).
   * Find a source of advanced support (your specialist group member
     or some other university service)

Github, Gitlab, etc.
~~~~~~~~~~~~~~~~~~~~
* **Version control platforms**
* Online hosting platforms for git (others available)
* Very useful to keep stuff organized
* Makes a lot of stuff below possible.
* Individual projects and **organizations** with members - for your
  group.

.. admonition:: Suggestions

   * Make one public Github/Gitlab organization for your group
   * Make one internal Gitlab organization hosted at your university.
   * Strongly discourage personal repositories for common code.

Issue tracking
~~~~~~~~~~~~~~
* Version control platforms provide **issue trackers**
* Important bugs, improvements, etc. can be closely tracked.

.. admonition:: Suggestions

   * Use issues for your most important common projects

Change proposals (aka "pull requests")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Feature of version control platforms like Github or Gitlab
* People should work together, but maybe not everyone should be able to
  modify everything, right?
* Contributors (your group or outside) can contribute without risk
  of messing things up.
* For this to work you *need to actually review, improve, and accept them*

.. admonition:: Suggestions

   * Decide which projects are important enough for a more formal
     change process.
   * Use pull requests for these projects which should not be broken.

Testing
~~~~~~~
* How do you know your code is correct?  Try running it, right?
* But what happens if you change it later?
* **Software testing** is a concept of writing tests, which can
  automatically verify functionality.
* You write tests, and then anytime you make a change later, the tests
  verify it still works.

.. admonition:: Suggestions

   * Each moderately important project has some test data and can
     automatically run something
   * More important projects: add in as many tests as practical

Documentation
~~~~~~~~~~~~~
* Documentation makes reusability.
* Minimum is Readme files in each repository.
* Big projects can have dedicated documentation.

.. admonition:: Suggestions

   * Every projects gets a README file.  As supervisor, read these
     README files and confirm what it contains.
   * Dedicated, in-repository documentation for large projects (for
     example `Sphinx <https://www.sphinx-doc.org/en/master/>`__)

Licensing
~~~~~~~~~
* Reuse gets you citations
* Reuse requires a license - or else significant reuse will be minimal.
* You will often need to check your local policies on making something
  open source.

.. admonition:: Suggestions

   * Decide (with stakeholders) on a license as early as possible -
     use only open-source licenses unless there is special reason.
     You don't have to actually open right away.
   * Try to focus on using similarly licensed things.

Publication and release
~~~~~~~~~~~~~~~~~~~~~~~
* If you invest in your software, you probably want to share it

  * "If we release a paper on some method, and we don't include *easy
    to use* software to run it, our impact will be tiny compared to
    what it could be." - CS Professor

* Good starting point: make the repository open on Github/Gitlab
* Can also be archived on Zenodo (or other places) to make it
  citeable.
* Do all work expecting that it might be made open someday.  Separate
  public and secret information into different repositories.

.. admonition:: Suggestions

   * Public on GitHub/GitLab as soon as possible
   * Next level is releases on package indexes
   * You can make software papers later (when relevant)


Working together on code
------------------------

Group discussion: What can go wrong when people work together?



Other computational topics
--------------------------

... not exactly software, but still relevant to this discussion.

Data storage
~~~~~~~~~~~~

- Discourage single-user storage spaces (laptop, home directories)
- Use common shared spaces instead
- Network drives

  - Usually used via a remote system
  - Some can be locally mounted on your own laptop for ease of use
  - Not the best for people who want to work on their own computer,
    but works.  Data can be synced.

Aalto Scientific Computing strategy:

- All mass storage provided in shared group directories.
- Request as many as your want - each one has a unique access control.
- Access and data can be passed on as the group evolves.

.. admonition:: Suggestions

   * Have a plan.  People know where central storage is and at least
     one copy must be there.
   * Request central network drive storage if possible.
   * Ask your group members: "Where is your data?  Is the data
     documented?"


Data storage locations at Aalto University
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Own devices

  * Danger, no backups!  Personal devices are considered insecure.

* Aalto home directories

* Aalto network drives

  * Large, secure, backed-up.  Request from your department or from
    Aalto IT Services.
  * 10-100 GB range is easy.

* Triton HPC Cluster

  * Very large, fast, direct cluster access, but not backed up.
  * 10s-100s of TB.

* CSC data storage resources

* Public data repositories

  * For open data



Computing
~~~~~~~~~

There are a range of computing options: (easy to use, small) ⋄ (harder
to use, large)

- Own devices

- Remote servers

- Remote computer clusters

  - Aalto
  - CSC



Support
-------

It's dangerous to go alone.  Take us!

* There were many things above.
* Hopefully you got some ideas, but I don't think that anyone can do
  this alone (I learned everything by working with others)
* Rely on support and mentoring.

Some possibilities, if you are at Aalto:

* At Aalto: :doc:`Daily Scientific Computing garage </help/garage>`
* At Aalto: :doc:`Research Software Engineer consulting service </rse/index>`
* At Aalto: `Data Agents <https://www.aalto.fi/en/services/data-agents>`__


.. admonition:: Suggestions

   * Ensure your group members come to garage if they have questions
     you can't answer.
   * Come to a RSE consultation and chat at least once when getting
     your group started.



Summary: dos and don'ts
-----------------------

.. admonition:: You are not allowed to

   - Not use version control
   - Not push to online repository
   - Have critical data or material only on an own computer.
   - Make something so chaotic that you can't organize it later
   - Go alone

.. admonition:: ... but you don't have to

   - Start every code perfectly
   - Do everything perfectly
   - ... as long as you can improve it later, if needed.
   - Know everything yourself.



Checklist
---------
- Set up group reference information (for example, wiki).
- Work with your supporters to create a basic outline of plan.
- Set up Github organization for group code
- Set up Gitlab organization for internal work (university Gitlab)
- Create your internal data/software management plan.
- (Think what code/data will be most reused, put it in one place, and
  make it reusable.)
- Send group members to CodeRefinery as they join.



See also
--------

* :doc:`zen-of-scicomp` - different levels of different aspects you
  can slowly improve.  Emphasizes that you don't have to be perfect
  when you first start.
