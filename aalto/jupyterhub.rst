=======================
JupyterHub for Teaching
=======================

.. note::

   This page is about the JupyterHub for teaching,
   https://jupyter.cs.aalto.fi.  The Triton JupyterHub for research is
   documented at :doc:`../triton/apps/jupyter`.


https://jupyter.cs.aalto.fi is a JupyterHub installation for teaching.
Anyone at Aalto may use this for generic light computing needs,
teachers may create courses with assignments using `nbgrader
<https://nbgrader.readthedocs.io/en/stable/>`__.


Basic usage
===========

Log in with any valid Aalto account.  Our environment may be used for light
computing and programming by anyone.

Your persistent storage has a quota of 1GB.  Your data belongs to you,
may be accessed from outside, and currently is planned to last no more
than one year from last login.  (TODO: in the future, the user
directories will be mounted on other Aalto computers).  You are
limited to one CPU and XXX MB of memory.

There are some general use computing containers.  You will began with
Jupyter in the ``/notebooks`` directory, which is your persistent
storage.

You begin with a computing container with the usual scipy
stack installed.

You may access your data remotely by SMB mounting it on your own
computer from inside the Aalto network or via Aalto VPN.  The SMB url
is ``smb://jhnas.org.aalto.fi/u/USERNAME``, or on Windows
``\\jhnas.org.aalto.fi\u\username``. (note: does not work yet)

Each container is basically a Linux container primarily running a
Juptyer notebook server.  You may create Jupyter notebooks to interact
with code in notebooks.  To access a Linux shell, create a new
terminal.


Courses and assignments
=======================

Some courses may use the `nbgrader
<https://nbgrader.readthedocs.io/en/stable/>`__ system to give and
grade assignments.  These courses have special entries in the list.

If you are a student in a course, you will have a special environment
for that course.  Your instructor may customize the environment, or it
may one of our generic environments.

If your course is using **nbgrader**, there are some built-in features
for dealing with assignments.  Under the **Assignment list** tab, you
can see the assignments for your course (only the course you currently
have running).  You can fetch assignments to work on them - they are
then copied to your personal ``/notebooks`` directory.  You can edit
the assignments there - fill out the solutions and validate them.
Once you are done, you can submit them.

A course may give you access to a ``/coursedata`` folder with any
course-specific data.

By default, everyone may access every course's environment and fetch
their assignments.  We don't stop you from submitting them - but
please don't submit assignments unless you are registered.  You are
giving your work to the course, which must be dealt with and then it
will be ignored.  Some courses may restrict the users which can launch
their notebooks or who can submit assignments and for these the
submission will mysteriously fail - please contact your course
instructor in this case.

Note that the ``/notebooks`` folder is shared across all of your
courses/containers, but the assignment for each course is specific to
the course/container you start when you begin your session.  Thus, you
should pay attention to these things.  Remember to clean up your data
sometimes.


Instructors
===========

See the separate :doc:`instructors guide <jupyterhub-instructors>`.


Privacy policy
==============

This system is managed by Aalto CS-IT.  We do not store separate
accounts or user data beyond a minimal database of usernames and
running notebooks which is periodically cleaned up (this is separate
from your data).  Your actual data is yours only and you are
responsible for it.  We do not access your data, but when necessary
for the operation of the system, may look at the metadata such as
permissions, timestamp, filename (``stat filename``).

The use of your own data and submission of data to your course
instructors is the responsibility of you and the instructors.

See :doc:`the separate document <jupyterhub-privacy>` for uselessly
legal information. (note: not written yet)



FAQ and bugs
============

* **Is JuptyerLab available?** Yes, and it's nice.  There are two
  general use instances that are actually the same, the only
  difference is one starts JupyterLab by default and one starts
  classic notebooks by default.  Course environments always use
  classic notebooks, because the nbgrader assignment list only works
  there.  To switch back and forth in any container, change ``/tree``
  in the URL to ``/lab/tree``.

* **How do I know what assignments I have already submitted?**
  Currently you can't.

* **Are there backups?**  Data storage is provided by the Aalto
  Teamwork system.  There are snapshots available in ``.snapshot`` in
  every directory, but this directory does not appear until you try to
  list it by the full name.
