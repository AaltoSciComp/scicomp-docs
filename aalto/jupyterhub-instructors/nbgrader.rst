Nbgrader basics
===============

"nbgrader is a tool that facilitates creating and grading assignments
in the Jupyter notebook. It allows instructors to easily create
notebook-based assignments that include both coding exercises and
written free-responses. nbgrader then also provides a streamlined
interface for quickly grading completed assignments."  *- nbgrader
upstream documentation*

Currently you should read the upstream `nbgrader documentation
<https://nbgrader.readthedocs.io/en/stable/>`__, which we don't
repeat.  We have some custom Aalto modifications (also submitted
upstream) which are:

How to use nbgrader
-------------------

Read the nbgrader docs!  We can't explain everything again here.

The course directory is ``/course/``.  Within this are ``source/``,
``release/``, ``submitted/``, ``autograded/``, and ``feedback/``.



Things which don't (necessarily) work in nbgrader
-------------------------------------------------

* **Autograde**: if you click the thing, it will work, but is the same
  as running all your students code *on your own computer* with no
  security whatsoever.  A slightly clever student is able to see other
  students work (a privacy breach), alter their grades.

* **Feedback**: While it appears to work, it is designed to operate by
  hashing the contents of the notebook.  Thus, if you have to edit the
  notebook to make it execute, the hash will be different and the
  built-in feedback distribution will not work.

* Furthermore, don't expect hidden tests to stay hidden, grading to
  happen actually automatically, things to be fully automatic, and so
  on.  Do expect a computing environment optimized for learning.

These are just intrinsic to how nbgrader works.  We'd hope to fix
these sometime, but it will require a more coordinated development
effort.


Aalto specifics
---------------

- Instructors can share responsibilities, multiple instructors can use
  the exchange to release/collect files, autograde, etc.  Note that
  with this power comes responsibility - try hard to keep things
  organized.

- We can have the assignments in ``/notebooks`` while providing
  whole-filesystem access (so that students can also access
  ``/coursedata``).

- We've added some extra security and sharing measures (most of these
  are contributed straight to nbgrader).

To use nbgrader:

- Request a course as above.

- Read the `nbgrader user instructions
  <https://nbgrader.readthedocs.io/>`__.

- You can use the ``Formgrader`` tab at the top to manage the whole
  nbgrader process (this automatically appears for instructors).  This
  is the easiest way, because it will automatically set up the course
  directory, create assignment directories, etc.  But, you can use the
  ``nbgrader`` command line, too.  It is especially useful for
  autograding.

- It's good to know how we arrange the course directory anyway,
  especially if you want to manage things yourself without Formgrader.
  The "course directory" (nbgrader term) is ``/course``.  The original
  assignments go in ``/course/source``.  The other directories are
  ``/course/{nbgrader_step}`` and, for the most part, are
  automatically managed.

- New assignments should be in ``/course/source``.  Also don't use
  ``+`` in the assignment filename (nbgrader #928).

- Manage your assignments with ``git``.  See below for some hints
  about how to do this.

- If you ever get permission denied errors, let us know.  nbgrader
  does not support multiple instructors editing the same files that
  well, but we have tried to patch it in order to do this.  We may
  still have missed some things here.



Version control of course assignments
-------------------------------------

`git <https://git-scm.com/>`__ is a version control system which lets
you track file versions, examine history, and share.  We assume you
have basic knowledge of git, and here we will give practical tips to
use git to manage a course's files.  Our vision is that you should use
nbgrader to manage the normal course files, not the students
submissions.  Thus, to set up the next year's course, you just clone
the existing git repository to the new ``/course`` directory.  You
backup the entire old course directory to maintain the old students
work.  Of course, there are other options, too.

Create a new git repository in your ``/course/`` directory and do some
basic setup::

  cd /course/
  git init
  git config core.sharedRepository group

You should make a ``.gitignore`` file excluding some common things
(TODO: maybe more is needed)::

  gradebook.db
  release/
  submitted/
  autograded/
  feedback/
  .nbgrader.log
  .ipynb-checkpoints

The git repository is in ``/course``, but the main subdirectory of
interest is the ``source/`` directory, which has the original files,
along with whatever other course notes/management files you may have
which are under ``/course``.  Everything else is auto-generated.


Autograding
-----------

.. seealso:

   :doc:`autograding`

.. warning::

   ``nbgrader autograde`` is not secure, because arbitrary student
   code is run with instructor permissions.  Read more from the
   instructor page.

