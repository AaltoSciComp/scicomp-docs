==============================================
Jupyterhub instructions for course instructors
==============================================

.. seealso::

   Main article with general usage instructions: :doc:`Jupyterhub for
   Teaching <jupyterhub>`.  For research purposes, see :doc:`Triton
   JupyterHub </triton/apps/jupyter>`.

Basics
======

The JupyterHub installation provides a way to provide a notebook-based
computational environment to students.  It is best to not think of
this service as a way to *do assignments* in a restricted fashion, but as a general *light
computing environment* that can also be used for courses.  Thus,
students should feel empowered to do their own computing.  Jupyter
works best for project/report type workflows, not lesson/exercise
workflows but of course it can do that too.

Optionally, you may use `nbgrader (notebook grader
<https://nbgrader.readthedocs.io/en/stable/>`__ to make assignments,
submit them to students, collect them, autograde them, manually grade,
and then export a csv/database of grades.  From that point, it is up
to you to manage everything.  There is currently no integration with
any other system, except that Aalto accounts are used to login.

Currently we support Python the most, but there are `other language
kernels available for Jupyter
<https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`__.  For
research purposes, see the :doc:`Triton Jupyter page
<../triton/apps/jupyter>`.


Basic course environment
========================

The following are the properties of the course environment.  To
request a course, please describe what you want from the items below.
Note that if all you need is the normal Python environment and are not
using nbgrader, you don't need to request a special course - students
can just use the generic instance for their personal/studies
computational needs.  We may update software in the generic instance
to keep things up to date and add additional features people request,
as long as it doesn't break backwards compatibility too badly.

A course environment is basically some definitions in a config file
consisting of:

1. A course slug, of the form ``nameYEAR`` (for example ``mlbp2018``)
   and full name.

2. A docker container containing the Jupyter stack and additional
   software.  By default, this is the `jupyter scipy stack
   <https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook>`__
   (with our custom modifications, of course - github repo coming).
   You can take and extend this image for your own course if you would
   like, but it would be best to stay as generic as possible.

3. A course directory ``/course``, available only to instructors.
   This comes default, with a quota of 1GB (combined with
   coursedata).  Note: instructors should manage assignments and so on
   using git or some other version control system.

4. A list of instructors (Aalto usernames).  This can be null if not
   using nbgrader or ``/coursedata``.  Instructors will be added to a
   Aalto unix group named ``jupyter-$coursename`` to limit data
   access.  To request new instructors, contact CS-IT and ask that
   people be added/removed from your group ``jupyter-$coursename``.

   a. Primary group owner (e.g. main instructor or professor).  Data
   is stored in a group according to :doc:`Science-IT data policy
   <datapolicy>`, and this person is in change of knowing what data
   exists, granting access and telling us what to do with the data
   long-term and they should be a long-term staff member.  There can
   be deputies (e.g. head TA) which can grant access.

5. A list of students (Aalto usernames).  This can be null if anyone
   with an Aalto account should be able to access the environment
   (this is recommended to be as open as possible and to save manual
   effort).

   a. Should non-students be allowed to spawn the environment?
      Default yes...

   b. Should non-students be allowed to submit assignments?  Default
      yes.

   c. There is a "private" mode where only instructors and test
      students can see the image.  If you want, we can create your
      course in this mode.

6. A list of computational resources per image.  Default is currently
   512MB and 3 processors (oversubscribed).  Note that because this is
   a container, *only* the memory of the actual Python processes are
   needed, not the rest of the OS.

7. Do you want a ``/mnt/jupyter/shareddata`` or ``/coursedata``
   directory for shared data?  ``coursedata`` is only available when
   your course's notebook.  ``shareddata`` is available in all
   notebooks on jupyter.cs.aalto.fi and also other Aalto servers.
   ``coursedata`` is also assumed to be public to everyone at Aalto,
   though not as easy to access.
   If so, tell us its quota.  Note: quota is shared with
   the course directory.  If number of students times amount of data
   is more than a few hundred MB, strongly consider one of the data
   directories.

8. Lead contact person.

9. Time period and expiry date - default is six months after the
   course is over, by which time data will be removed.  But if it will
   be used the next year, then we'll keep it up until then.  You must
   agree to manage data well.


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

- Submissions are hidden by more than just timestamps.

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

- New assignments should be in ``/course/source``.  Remember to name
  your assignments like ``$courseslug-*``.  Also don't use ``+`` in
  the assignment filename (nbgrader #928).

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
  the student's code as the instructor.  Students can do all
  sorts of bad things with this, and the only way to stop them is to
  check notebooks yourself before autograding.  We have a custom-build
  solution at https://github.com/AaltoScienceIT/isolate-namespace, but
  it will require manual work.  This requires a Linux computer.



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
Remember to name the assignments like ``$courseslug-NN-name`` as
described above.

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

- When using ``nbgrader``, name all of your assignments like
  ``$courseslug-NN-$assignmentname``, for example ``mlbp2018-01-regression``.
  The ``NN`` is some assignment number, so that things are sorted properly.
  Assignment names are an accidental global namespace in nbgrader once
  they are copied to a user's notebook directory, so you should use
  names which won't clash with anyone else's.

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
  mess up group-writeability permissions.

- You are the data controller of any assignments which students
  submit.  We do not access these assignments on your behalf, and a
  submission of an assignment is an agreement between you and the
  student.

- You should always do random checks of a fair fraction of notebooks,
  to avoid unexpected problems.

- You can tell what image you have using ``echo $JUPYTER_IMAGE_SPEC``.

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
