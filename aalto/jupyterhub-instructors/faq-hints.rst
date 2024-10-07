FAQ and hints
=============

.. _jupyterhub-courses-repo:

Shared course repository
------------------------

There's a lot to figure out and everyone has to learn by doing.  Why
not learn from each other?  We have a shared `jupyterhub-courses
<https://version.aalto.fi/gitlab/jupyterhub-courses>`__ repository on
version.aalto.fi with a repository for each course.  You can browse
and learn from how other courses make notebooks, thus saving you time.
It also makes it easier for us to help you.

- Decide who are the people to be added to the jupyterhub-courses
  Gitlab organization (usually those who have long term contracts with
  Aalto). You can add whoever you want to the your own courses's
  repository itself, but organization side should be kept in smaller
  group so that other TAs won't get access to courses which they might
  participate in.

- Setup git for your course. This is something that you might have
  already done, but :doc:`here are some general tips for nbgrader
  specifically <nbgrader>`.

- After you have gotten an access to the organization, you can create
  a course in version.aalto and then setup it as a new origin for your
  git repository: ``git remote add new_remote_name
  {address}``. (`Github help
  <https://help.github.com/en/github/using-git/adding-a-remote>`__)

- Now you can use to push to this new remote! For example, if your new
  origin were "gitlab" then ``git push gitlab master`` would push into
  version.aalto. Now you should be ready to go!

Instructions/hints
------------------

- Request a course when you are sure you will use it.  You can use the
  general use containers for writing notebooks before that point.

- Don't forget about the :doc:`flexible ways of accessing
  <course-data>` your :doc:`course data <../jupyterhub-data>`.

- The course directory is stored according to the :doc:`Science-IT
  data policy </data/science-it-data-policy>`.  In short, all data is stored in group
  directories (for these purposes, the course is a group).  The
  instructor in change is the owner of the group: this does not mean
  they own all files, but are responsible for granting access and
  answering questions about what to do with the data in the long
  term.  There can be a deputy who can also grant access.

- To add more instructors/TAs, go to `domesti.cs.aalto.fi
  <https://domesti.cs.aalto.fi>`_ and you can do it yourself.  You
  must be connected to an Aalto network.  See the `Aalto VPN guide
  <https://www.aalto.fi/en/services/establishing-a-remote-connection-vpn-to-an-aalto-network>`_
  for help with connecting to an Aalto network from outside.

- Store your course data in a git repository (or some other version
  control system) and push it to :doc:`version.aalto.fi </aalto/git>`
  or some such system.  ``git`` and relevant tools are all installed
  in the images.

- You know that you are linked as an instructor to a course if, when
  you spawn that course's environment, you get the ``/course``
  directory.

- You can now make a direct link that will spawn a notebook server,
  for example for a course with a slug of ``testcourse``:
  ```https://jupyter.cs.aalto.fi/hub/spawn?profile=testcourse``.  If
  the user is already running a server, it will **not switch to the
  new course**.  Expect some subtle confusion with this and plan for
  it.

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
    https://github.com/AaltoSciComp/isolate-namespace for
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

- A notebook can tell if it is being autograded by checking if
  ``NBGRADER_VALIDATING`` is set.

- You can install an identical version of nbgrader as we have using::

    pip install git+https://github.com/AaltoSciComp/nbgrader@live

  This may be useful if you get metadata mismatch errors between your
  system and ours.  There used to be more differences, these days the
  differences are minimal because most of our important changes have
  been accepted upstream.

- You can get an ``environment.yml`` file of currently installed
  packages using::

    conda env export -n base --no-builds

  But note this is everything installed: you should remove everything
  from this file except what your assignments actually depend on,
  since being less strict will increase the chances that it's
  reproduceable.  ``nbgrader`` should be removed (it pins to an
  unreleased development version which isn't available), and perhaps
  the ``prefix`` should too.  For actual versions installed, see
  ``base`` and ``standard`` dockerfiles in `the singleuser-image repo
  <https://github.com/AaltoSciComp/jupyter-aalto-singleuser>`_.



FAQ
---

- **Something with nbgrader is giving an error in the web browser**.
  Try running the equivalent command from the command line.  That will
  usually give you more debugging information, and may tell you what
  is going wrong.

- I see **Server not running ... Would you like to restart it?** This
  particular error also happens if there are temporary network
  problems (even a few seconds and it comes back).  It doesn't
  necessarily mean that your server isn't running, but there is no way
  to recover.  I always tell people: if you see this message, refresh
  the page.  If the server is still running, it recovers.  If it's
  actually not running, it will give you the option to restart it
  again.  If there are still network problems, you'll see an error
  message saying that.


- **Gurobi** Gurobi has license issues, and it's not clear if it can
  even be distributed by us.  So far, we only support open software.

  But, courses have used gurobi before.  They had students install
  themselves, in the Python environment, and somehow told it what
  the Aalto license server was.  For examaple, using the magic of "!"
  shell commands embedded in notebooks, it was something like this,
  which would automatically install gurobi for students and set the
  license file information.::

     !conda install -c gurobi gurobi
     !echo [license_file_information] > ~/.[license_file_path]

- **I have done a test release/fetch/autograde of an assignment, and I
  want to re-generate it.  It says I can't since there are already
  grades**.  You also need to remove it from the database with the
  following command.  Note that if students have already fetched, they
  will need to re-fetch it so *don't do this if it's already in the
  hands of the students* - you will only create chaos (see the point
  below).

  .. code-block:: console

     $ nbgrader db assignment remove ASSIGNMENT-ID

- **I have already released an assignment, and now I need to update it
  and release it again.  Some students have already fetched it.**
  This works easily if students haven't fetched it yet, if they have
  it requires some manual work from them.

  What you need to do: (make sure the old version is git-committed),
  edit the source/ directory version, un-release the assignment,
  generate it again, release the assignment again.  You might need to
  force it to fetch the assignment again, if it has already been
  fetched. (verify, TODO: let me know how you do this)

  On the student side: After an assignment is fetched, it won't present
  the option to fetch it again (that would lose their work).  Instead,
  they need to move the fetched version to somewhere else, then
  re-fetch.  You can send the following instructions to your students:

     I have updated an assignment, and you will need to re-fetch it.  You
     work won't be lost, but you will need to merge it into the new
     versions.

     * First, make sure you save everything and close the notebooks.
     * Open a terminal in Jupyter
     * Run the following commands to change to the course assignment
       directory and move the assignment to a new place (``-old``
       suffix on the directory name):

       .. code-block:: console

	  $ cd /notebooks/COURSE/
	  $ mv ASSIGMENT_ID ASSIGNMENT_ID-old

     * In the assignment list, it should now offer you to re-fetch the
       assignment.
     * You can now open both the new old old versions (but to open the
       old version, you need to navigate to
       ``/notebooks/COURSE/ASSIGNMENT_ID-old`` yourself to see it).
     * If you have already submitted the assignment, submit again.
       The old assignment is still submitted, but our fetching should
       get the new one.
