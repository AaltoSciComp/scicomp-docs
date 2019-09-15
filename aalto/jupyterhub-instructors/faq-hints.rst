FAQ and hints
=============

Instructions/hints
------------------

- Request a course when you are sure you will use it.  You can use the
  general use containers for writing notebooks before that point.

- The course directory is stored according to the :doc:`Science-IT
  data policy </aalto/datapolicy>`.  In short, all data is stored in group
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
