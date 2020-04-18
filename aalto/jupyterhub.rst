==========
JupyterHub
==========

.. note::

   This page is about the JupyterHub for light use and teaching,
   https://jupyter.cs.aalto.fi.  The :doc:`Triton <../triton/index>`
   JupyterHub for research is documented at
   :doc:`../triton/apps/jupyter`.


https://jupyter.cs.aalto.fi is a JupyterHub installation for teaching
and light usage.  Anyone at Aalto may use this for generic light
computing needs, teachers may create courses with assignments using
`nbgrader <https://nbgrader.readthedocs.io/en/stable/>`__.  Jupyter
has a `rich ecosystem <https://jupyter.org/>`__ of tools for modern
computing.


Basic usage
===========

Log in with any valid Aalto account.  Our environment may be used for light
computing and programming by anyone.

Your persistent storage has a quota of 1GB.  Your data belongs to you,
may be accessed from outside, and currently is planned to last no more
than one year from last login.  You are
limited to several CPUs and 1GB memory.

Your notebook server is stopped after 60 minutes of idle time, or 8 hours
max time.  Please close the Jupyter tab if you are not using it, or
else it may still appear as active.

There are some general use computing environments.  You will began with
Jupyter in the ``/notebooks`` directory, which is your persistent
storage.  Your server is completely re-created each time it restarts.
Everything in your home directory is re-created, only ``/notebooks``
is preserved.  (Certain files like ``.gitconfig`` are preserved by
linking into ``/notebooks/.home/...``.)

You begin with a computing server with the usual scipy
stack installed, plus a lot of other software used in courses here.

You may access your data as a network drive by SMB mounting it on your own
computer - see :doc:`jupyterhub-data`.  This allows you total control
over your data.

JupyterHub has no GPUs, but you can check out the :ref:`instructions
for using the Paniikki GPUs with the JupyterHub data
<jupyter-gpu-paniikki>`.  These instructions are still under
development.

Each notebook server is basically a Linux container primarily running a
Juptyer notebook server.  You may create Jupyter notebooks to interact
with code in notebooks.  To access a Linux bash shell, create a new
terminal - this is a great place to learn something new.

.. toctree::
   :hidden:

   jupyterhub-data


Terms of use
============

This service must be used according to the general IT usage policy of
Aalto university (including no unlawful purposes).  It should only be
used for academic purposes (but note that self-exploration and
programming for own interests is considered an academic purpose,
though commercial purposes is not allowed).  For more information, see
`the Aalto policies
<https://www.aalto.fi/en/services/it-policies-and-guidelines>`__.
Heavy non-interactive computational use is not allowed (basically,
don't script stuff to run in the background when you are not around.
If you are using this service is person, it is OK).  For research
computing, see :doc:`../triton/index`.



Courses and assignments
=======================

Some courses may use the `nbgrader
<https://nbgrader.readthedocs.io/en/stable/>`__ system to give and
grade assignments.  These courses have special entries in the list.
If you are a student in such a course, you will have a special
environment for that course.  Your instructor may customize the
environment, or it may one of our generic environments.

If your course is using **nbgrader**, there are some built-in features
for dealing with assignments.  Under the **Assignment list** tab, you
can see the assignments for your course (only the course you selected
when starting your notebook server).  You can fetch assignments to
work on them - they are then copied to your personal ``/notebooks``
directory.  You can edit the assignments there - fill out the
solutions and validate them.  Once you are done, you can submit them
from the same assignment list.

A course may give you access to a ``/coursedata`` folder with any
course-specific data.

By default, everyone may access every course's environment and fetch
their assignments.  We don't stop you from submitting assignments to
courses you are not enrolled in - but please don't submit assignments
unless you are registered, because the instructors must then deal with
it.  Some courses may restrict who can launch their notebook servers:
if you can not see or launch the notebook server for a course you are
registered for, please contact your instructor in this case.

Note that the ``/notebooks`` folder is shared across all of your
courses/servers, but the assignment list is specific to the course
you have started for your current session.  Thus, you should pay
attention to what you launch.  Remember to clean up your data
sometimes.


Instructors
===========

.. toctree::
   :hidden:

   jupyterhub-instructors/index

See the separate :doc:`instructors guide
<jupyterhub-instructors/index>`.
This service may be either used as general light computing for your
students, or using nbgrader to release and collect assignments.


Privacy policy
==============

This system is managed by Aalto CS-IT.  We do not store separate
accounts or user data beyond a minimal database of usernames and
technical logs of notebooks which are periodically removed (this is
separate from your data).  Your actual data is yours only and you are
responsible for it.  We do not access your data, but when necessary
for the operation of the system, but we use and may look at file
metadata such as permissions, timestamp, filename (``stat filename``).
Your ``/notebooks`` directory may be deleted once your have been
inactive for one year, and at the latest once your Aalto home
directory is removed (after your account expires).  Some courses will
use the ``feedback/`` directory to return assignments to you.

The use of your own data and submission of data to your course
instructors is the responsibility of you and the instructors.

See :doc:`the separate privacy policy document <jupyterhub-privacy>`
for longer, less useful information.



FAQ and bugs
============

* **I started the wrong environment and can't get back to the course
  selection list.**  In JupyterLab, use the menu bar, "Hub->Control
  Panel".  On the classic notebooks, use the "Control panel" button on
  the top right.  (Emergency backup: you can
  always change the URL path to ``/hub/home``).

* **Is JuptyerLab available?** Yes, and it's nice.  There are two
  general use instances that are actually the same, the only
  difference is one starts JupyterLab by default and one starts
  classic notebooks by default.  Course environments always use
  classic notebooks, because the nbgrader assignment list only works
  there.  To switch back and forth in any notebook server, change
  ``/tree`` in the URL to ``/lab/tree``.  If you want to use
  JupyterLab with a course's files, first start that course's server,
  get the assignments, then change to JupyterLab (change the URL, or
  stop and restart your server).

* **Can I login with a shell?**  Run a new terminal within the
  notebook interface.

* **Can I request more software be installed?**  Yes, let us know and
  we will include it if it is easy.  We aim to have featureful
  environments by default, but won't go so far as to install large
  specialist software.  It should be in standard repositories (conda
  or pip for Python stuff).

* **Can I do stuff with my class's assignments and not have it
  submitted?**  You have your personal storage space ``/notebooks/``,
  which you can use for whatever you want.  You can always make a copy
  of the assignment files there and play around with them as much as
  you want - even after the course is over, of course.

* **Are there other programming languages available?** Currently there
  is Python, R, and Julia.  More could be added if there is a good
  Jupyter kernel for it.

* **What can I use this for?** Intended uses include anything related
  to courses, own exploration of programming, own data analysis, and
  so on (see Terms of Service above).  Long-term background processing
  isn't good (but it's OK to leave small stuff running, close the tab,
  and come back).

* **When using nbgrader, how do I know what assignments I have already
  submitted?** Currently you can't beyond what is shown there.

* **Can I know right away what my score is after I submit an
  assignment with nbgrader?** nbgrader is not currently designed for
  this.

* **Are there backups of data?** Data storage is provided by the Aalto
  Teamwork system.  There are snapshots available in ``.snapshot`` in
  every directory (you have to ``ls`` this directory in a shell using
  its full name for it to appear the first time).  This service is not
  designed for long term data storage, and you should back up anything
  important because it will be lost after about one year or when your
  Aalto account expires.  You should use ``git`` as your primary
  backup mechanism, obviously.

* **Is git installed?** Yes, and you should use it.  Currently you
  have to configure your username and email each time you use it,
  because this isn't persistent (because home directories are not
  persistent).  Git will guide you through doing this.  In the future,
  your Aalto directory name/email will be automatically set.  As a
  workaround, run ``git config`` without the ``--global`` option in
  each repository.

* **I don't see "Assignment list".**  You are probably not in a
  general use server instead of a course server.  Stop your
  server and go spawn the notebook server of your course.

* **I'm getting an error code**  Here are the ones we know about:

  - 504 Gateway error: The hub isn't running in background.  This may
    be hub just restarting or us doing maintenance.  If it persists for
    more than 30 minutes, let someone know.

* **Stan/pystan/Rstan don't work.** Stan needs to do a
  memory-intensive compilation when your program is run.  We can't
  increase our memory limits too much, but we have a workaround: you
  need to tell your program to use the ``clang`` compiler instead of
  the ``gcc`` compiler by setting the environment variables
  ``CC=clang`` and ``CXX=clang++``.  For R notebooks, this should be
  done for you.  For RStudio, we don't know.  For Python, put the
  following in your notebook::

    import os
    os.environ['CC'] = "clang"
    os.environ['CXX'] = "clang++"

  We should set this the default, but want to be sure there are no
  problems first.

* **RStudio doesn't appear**.  It seems that it doesn't work from the
  Edge browser.  We don't know why, but try another browser.

* **I've exceeded my quota**.  You should reduce the space you use,
  the quota is 1GB.  If this isn't enough and you actually need more
  for your classes, tell your instructor to contact us.  To find large
  directories files: open a terminal and run ``du -h /notebooks/ |
  sort -h`` to find all large files.  Then clean up that stuff
  somehow, for example ``rm -r``.  Note that
  ``.home/.local/share/jupyter/nbgrader_cache`` will continue to grow
  and eventually needs to be cleaned up - after the respective course
  is done.


More info
=========

Students, your first point of contact for course-related matters and
bugs with JuptyerHub should be your instructors, not us.  They will
answer questions and send the relevant ones to us.  But, if you can
actively help with other things, feel free to comment via Github
repositories below.

The preferred way to send feedback and development requests is via
Github issues and pull requests.  However, we're not saying it's best
to give Github all our information, so you can also send tickets to
CS-IT.

Students and others who have difficulty in usage outside of a course
can contact CS-IT via the guru alias.

Notebooks are *not* an end-all solution: for an entertaining look at
some problems, see `"I don't like notebooks" by Joel Grus
<https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI>`__.
Most of these aren't actually specific to notebooks and JupyterLab
makes some better, but thinking hard about the downfalls of notebooks
makes your work better no matter what you do.

Our source is open and on Github:

- `single-user image
  <https://github.com/AaltoScienceIT/jupyter-aalto-singleuser>`__
  (everything about a user's environment)

- `server itself
  <https://github.com/AaltoScienceIT/jupyterhub-aalto>`__ (logging in,
  course profiles, etc).
