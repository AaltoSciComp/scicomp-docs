==============================================
Jupyterhub instructions for course instructors
==============================================

.. seealso::

   Main article with general usage instructions: :doc:`Jupyterhub for
   Teaching <jupyterhub>`.  For research purposes, see :doc:`Triton
   JupyterHub </triton/apps/jupyter>`.

   nbgrader documentation is at https://nbgrader.readthedocs.io/, and
   is necessary reading to understand how to use it.  It is not
   duplicated here.

Basics
======

The JupyterHub installation provides a way to provide a notebook-based
computational environment to students.  It is best to not think of
this service as a way to *do assignments*, but as a general *light
computing environment* that is designed to be easy enough to be used
for courses.  Thus,
students should feel empowered to do their own computing and this
should feel like a stepping stone to using their own systems set up
for scientific computing.  Students' own data is persistent as they go
through courses, and need to learn how to manage it themselves.  Jupyter
works best for project/report type workflows, not lesson/exercise
workflows but of course it can do that too.  In particular, there is
no real possibility for real-time grading and so on.

Optionally, you may use `nbgrader (notebook grader
<https://nbgrader.readthedocs.io/en/stable/>`__ to make assignments,
submit them to students, collect them, autograde them, manually grade,
and then export a csv/database of grades.  From that point, it is up
to you to manage everything.  There is currently no integration with
any other system, except that Aalto accounts are used to login.

You may find the book `Teaching and Learning with Jupyter
<https://jupyter4edu.github.io/jupyter-edu-book/>`__ helpful.

Currently we support Python the most, but there are `other language
kernels available for Jupyter
<https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`__.  For
research purposes, see the :doc:`Triton Jupyter page
<../triton/apps/jupyter>`.


Basic course environment
========================

The following are the properties of the course environment.  **To get
started with a course**, please read the below list and describe your
needs from the relevant items (contact address is at the bottom of
this page).  **Don't worry too much about understanding or answering
everything perfectly, there is a lot here - just let us know what you
have as concisely as possible and we will work together to answer the
rest.**

If all you need is a Python environment to do assignments and
projects, you don't need to request anything special - students can
just use the generic instance for their independent computational
needs.  If your course needs special packages which compatible with
existing packages, let us know and we will install them.  You *would*
want a course environment if you want to (distribute assignments to
students via the interface) and/or (collect assignments via the
interface).

A course environment consists of:

1. A course slug (of the form ``nameYEAR``, for example ``mlbp2018``)
   and full name.

2. Description of general computational load expected - number of
   students, expected processor and memory usage, expected data size
   both on disk and in memory, expected schedule (will everyone be
   doing an assignment right before the deadline?).  You should
   strongly discourage people from waiting until the last minute if
   you have hundreds of students in the course.  We'll provide
   feedback on how well we can handle the load.

3. Course schedule (lectures/exercise sessions/deadlines).  We add
   this to `our hub calendar
   <https://calendar.google.com/calendar/embed?src=d01se1d7m4gehcoruig0qkn5e4%40group.calendar.google.com>`__,
   which is used to avoid maintenance during important times.  You can
   check the calendar to avoid major deadlines at the same times as
   other courses.  Note: we've heard that late night deadlines are bad
   for students well-being, so don't make deadlines late at night just
   to reduce the peak load on our system.

4. (optional, recommended to use the default and add what you need)  A
   list of required software, or a docker container
   containing the Jupyter stack and additional
   software.  By default, we have an image based on the scipy stack
   and all the latest software that anyone else has requested, as long
   as it is mutually compatible.  You can request additional software,
   and this is shared among all courses.  If you need something
   special, you may be asked to take our image and extend it
   yourself.  Large version updates to the image are done twice a year
   during holidays.

   a. (optional) A sample python file or notebook to test that the
      environment
      works for your course (which will be made public and open
      source).  We also use use automated testing on our software
      images, so that we can be sure that our server images still work
      when they are updated.  If you send us a file, either ``.py`` or
      ``.ipynb``, we will add this to our automatic tests.  The
      minimum amount is something like ``import`` of the packages you
      need, a more advanced thing would test the libraries a little
      bit - do a minimal, quick calculation.

5. A course directory ``/course``, available only to instructors.
   This comes by default, with a quota of a few gigabytes (combined with
   coursedata).  Note: instructors should manage assignments and so on
   using git or some other version control system, because the course
   directory lasts only one year, and is renewed for the next year.

6. A list of instructors (Aalto emails or usernames).  Instructors
   will be added to a Aalto unix group named ``jupyter-$courseslug``
   to provide access control.  To request new instructors, contact
   CS-IT and ask that people be added/removed from your group
   ``jupyter-$courseslug``.

   a. Primary group owner (e.g. main instructor).  Data is stored in a
      group according to :doc:`Science-IT data policy <datapolicy>`,
      and this person is in change of knowing what data exists,
      granting access and telling us what to do with the data
      long-term and they should be a long-term staff member.  There
      can be deputies (e.g. head TA) which can grant access.

   b. People who should be added to the announcement mailing list -
      these will get updates for updates and maintenance breaks.

   c. Lead contact person, if different from instructor.

7. (optional, not recommended)  A list of students (Aalto usernames).
   This can be null if anyone
   with an Aalto account should be able to access the environment
   (this is recommended to be as open as possible and to save manual
   effort).  If you provide a list of students, you will have to
   request manual effort every time it changes, so this is *not
   recommended*.

   a. Should non-students be allowed to spawn the environment?
      Default yes...

8. Should the image start in "private mode", where only instructors
   and students from the previous point can start the course
   environment?  From our side, there is no major disadvantage to
   going public from the start.

9. (optional, not recommended) A list of computational resources per
   image.  Default is currently 2GB and 4 processors (oversubscribed).
   Note that because this is a container, *only* the memory of the
   actual Python processes are needed, not the rest of the OS, and
   memory tends to be quite small.

10. Shared data directories.  If you have nontrivial data which needs
    distributing, consider one of these shared directories which saves
    it from being copied over and over.  The notebook directory itself
    can only support files of up to 2MB to prevent possible problems.
    If number of students times
    amount of data is more than a few hundred MB, strongly consider
    one of the data directories.  Read more about this :ref:`below
    <jupytercoursedata>`.

    a.  You can use the "shareddata" directory
	``/mnt/jupyter/shareddata``.  ``shareddata`` is available in
	all notebooks on jupyter.cs.aalto.fi (even outside of your
	course) and also (eventually) other Aalto servers.  This data
	should be considered public (and have a valid license), even
	though for now it's only accessible to Aalto accounts.

    b. ``/coursedata`` is only available within your course's
       environment (as chosen from the list).  ``coursedata`` is also
       assumed to be public to everyone at Aalto, though you have more
       control over it.

    c. If you use either of these, you can embed the paths directly in
       your notebooks.  This is easy for hub use, but makes it harder
       to copy the notebooks out of the hub to use on your own
       computers.  This is something we are working on.

12. Time period and expiry date - default is six months after the
    course is over, by which time data will be removed.  But if it will
    be used the next year, then we'll keep it up until then.  We
    intentionally replace the course directories every year both for
    security and to encourage you to use maintainable processes!



nbgrader
========

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

- Instructors can share responsibilities, multiple instructors can use
  the exchange to release/collect files, autograde, etc.  Note that
  with this power comes responsibility - try hard to keep things
  organized.

- We can have the assignments in ``/notebooks`` while providing
  whole-filesystem access (so that students can also access
  ``/coursedata``).

- Submissions are hidden from other students better.

- While not part of nbgrader, we have a way to isolate the grading
  process so that students can't access other instructor files.

To use nbgrader:

- Request a course as above.

- Once you log in to your course's environment, the per-course
  ``/course`` (instructors only) and ``/srv/nbgrader/exchange``
  (instructors and students, if requested) are mounted.

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

- To autograde from the command line, add the option
  ``--Autograde.create_student=True`` so that it will automatically
  add students to the grader database.  This happens automatically if
  you click the lightning bolt to autograde from the Formgrader UI.

- nbgrader is `not secure
  <https://github.com/jupyter/nbgrader/issues/483>`__, because it runs
  the student's code as the instructor.  We have a custom-build
  solution at https://github.com/AaltoScienceIT/isolate-namespace, but
  it will require manual work.  This requires a Linux computer.

  **Autograding is not secure right now.  If you use autograding,
  contact us first well in advance so we can improve the
  documentation.**  Autograding is equivalent to accepting arbitrary
  code from all students and running it *on your own computer*
  automatically without checking input or outputs.  Do this at your
  own risk, but we do *not* offer this as a secure service without our
  custom add-ons.


Using git
=========

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


.. _jupytercoursedata:

Course data
===========

If your course uses data, request a ``coursedata`` or ``shareddata``
directory as mentioned above.  You need to add the data there
yourself, either through the Jupyter interface or SMB mounting of
data.

If you use ``coursedata``, just start the course environment and
instructors should have permissions to put files in there.  Please try
to keep things organized!

If you use ``shareddata``, ask for permission to put data there - we
need to make the directory for you.  When asking, tell us the
(computer readable short)name of the dataset.  In the shareddata
directory, you find a README file with some more instructions.  All
datasets should have a minimum README (copy the template) which makes
it minimally usable for others.

In both cases, you need to ``chmod -R a+rX`` the data directory so
that the data becomes readable to students.

Note: after you are added to relevant group to access the data, it
make take up to 12 hours for your account information to be updated
so that it can be accessed via remote mounting.



Public copy of assignments
==========================

Let's say you want to make your assignments publicly
available so that anyone can access them to follow along without being
an Aalto student or being registered.  This is
also important because your course environment will go away after a
few months - do you want students to be able to refer to it later?  If
so, do the below.

- change to the ``release/`` directory and ``git init``.  Create a new
  repo here.
- Manually ``git add`` the necessary assignment files after they are
  generated from the ``source`` directory.  Why do we need a new repo?
  Because you can't have the instructor solutions/answers made public.

- Update files (``git commit -a`` or some such) occasionally when new
  versions come out.

- Add a ``requirements.txt`` file listing the different packages you
  need installed for a student to use the notebooks.  See the
  `MyBinder instructions
  <https://mybinder.readthedocs.io/en/latest/using.html#preparing-a-repository-for-binder>`__
  for different ways to do this, but a normal Python
  ``requirements.txt`` file is easiest for most cases.  On each line,
  put in a name of a package from the Python Package Index.  There are
  other formats for ``R``, ``conda``, etc, see the page.

- Then, push this ``release/`` repo to a public repository (check
  mybinder for supported locations).  Make sure you don't ever
  accidentally push the course repository!

- Then, go to https://mybinder.org/ and use the UI to create a URL for
  the resources.  You can paste this URL into your course info, but
  recommend people use our resources first if they can (see below for
  the reason).

- Note that mybinder has a limit of 100 simultaneous users for a
  repository, to prevent too much use for single organization's
  projects.  It's possible that limits will change or decrease later.
  Either way, for Aalto primary academic purposes we should use our
  resources first to avoid over-burdening free resources, and students
  should be advised as such.

- If you have a ``/coursedata`` directory, you will have to provide
  these files some other way.  You could put them in the assignment
  directory and the ``release/`` git repository, but then you'll need
  to have notebooks able to load them from two places: ``/coursedata``
  or ``.``.  I'd recommend do this: ``import os``, ``if
  os.path.exists('/coursedata'): DATADIR='/coursedata'``,  ``else:
  DATADIR='.'`` and then access all data files by
  ``os.path.join('DATADIR', 'filename.dat')``.  This has the added
  advantage that it's easy to swap out ``DATADIR`` later, too.

Instructions and hints to instructors
=====================================

Instructions/hints
------------------

- Request a course when you are sure you will use it.  You can use the
  general use containers for writing notebooks before that point.

- The course directory is stored according to the :doc:`Science-IT
  data policy <datapolicy>`.  In short, all data is stored in group
  directories (for these purposes, the course is a group).  The
  instructor in change is the owner of the group: this does not mean
  they own all files, but are responsible for granting access and
  answering questions about what to do with the data in the long
  term.  There can be a deputy who can also grant access.

- Store your course data in a git repository (or some other version
  control system) and push it to :doc:`version.aalto.fi </aalto/git>`
  or some such system.  ``git`` and relevant tools are all installed
  in the images.

- You know that you are linked as an instructor to a course if, when
  you spawn that course's environment, you get the ``/course``
  directory.

- We have a test course which you can use as a sandbox for testing
  nbgrader and courses.  No data here is private even after deleted,
  and data is not guaranteed to be persistent.  Use only for testing.
  Use the general use notebook for writing and sharing your files
  (using git).

- The course environments are not captive: students can install
  whatever they want.  Even if we try to stop them, they can use the
  general use images (which may get more software at any time) or
  download and re-upload the notebook files.  Either way, autograding
  is done in the instructors environment, so if you want to limit the
  software that students can use, this must be done at the autograding
  stage or via other hacks.

  - 1) If you want to check that students have *not* used some particular
    Python modules, have an hidden test that they haven't used the
    module, like: ``'tensorflow' not in sys.modules``.

  - 2) autograde in an environment which does not have these extra
    packages.  Really, #2 is the only true solution.  See the
    information under
    https://github.com/AaltoScienceIT/isolate-namespace for
    information on doing this.

  - In all cases, it is good practice to pre-import all modules the
    students are expected to be able to use and tell students that
    other modules should not be imported.

- Students should use you, not us, as the first point of contact for
  problems in the system.  Please announce this to students.  Forward
  relevant problems to us.

- You can access your course data via SMB mounting at the URLs
  ``smb://jhnas.org.aalto.fi/course/$courseslug/files/`` and the course data
  using ``smb://jhnas.org.aalto.fi/course/$courseslug/data/``
  (with Windows, use ``\\`` instead of ``/`` and don't include
  ``smb://``).  This can be very nice for managing files.  This may
  mess up group-writeability permissions.  It will take up to half a
  day to be able to access the course files after your request your
  course.

- You are the data controller of any assignments which students
  submit.  We do not access these assignments on your behalf, and a
  submission of an assignment is an agreement between you and the
  student.

- You should always do random checks of a fair fraction of notebooks,
  to avoid unexpected problems.

- You can tell what image you have using ``echo $JUPYTER_IMAGE_SPEC``.

- A notebook can tell if it is in the hub environment if the
  ``AALTO_JUPYTERHUB`` environment variable is set.

Limits
------

- This is not a captive environment: students may always trivially
  remove their files and data, and may share notebooks across
  different courses.  See above for the link to isolate-environment
  with instructions for fixing this.

- We don't have unlimited computational resources, but we can try to
  procure what is necessary.  Work as hard as you can to spread the
  load and de-peak deadlines.  You should discuss estimated number of
  students and estimated deadlines (days of the week) before courses
  start so that we can spread the load some.

- There is no integration to any other learning management systems,
  such as the CS department A+ (yet).  The only unique identifier of
  students is the Aalto username.  ``nbgrader`` can get you a csv file
  with these usernames, what happens after that point is up to you.

- Currently there is nothing in place to return marked-up assignments
  to students.  We can possibly make a root script to do this.
  Organize assignments by username and we can do the rest.

- There is currently no plagiarism detection support.  You will have
  to handle this yourself somehow so far.


More info
=========

Contact: CS-IT via the guru alias guru @ cs dot aalto.fi (students,
contact your course instructors first).

For source code and reporting issues, see the main jupyterhub page.
