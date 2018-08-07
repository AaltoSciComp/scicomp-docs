================================================
Teaching Jupyterhub instructions for instructors
================================================

.. seealso::

   Main article: :doc:`Jupyterhub for Teaching <jupyterhub>`.

Basics
======

The JupyterHub installation provides a way to provide a notebook-based
computational environment to students.  Optionally, you may use
`nbgrader (notebook grader
<https://nbgrader.readthedocs.io/en/stable/>`__ to make assignments,
submit them to students, collect them, autograde them, manually grade,
and then export a csv/database of grades.  From that point, it is up
to you to manage.  There is currently no integration with any other
system, except that Aalto accounts are used to login.

Currently we support Python the best, but there are `other language
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

3. A list of instructors (Aalto usernames).  This can be null if not
   using nbgrader or ``/coursedata``.  Instructors will be added to a
   Aalto unix group named ``jupyter-$coursename`` to limit data
   access.

4. A list of students (Aalto usernames).  This can be null if anyone
   with an Aalto account should be able to access the environment
   (this is recommended to be as open as possible and to save manual
   effort).

   a. Should non-students be allowed to spawn the environment?
      Default yes...

   b. Should non-students be allowed to submit assignments?  Default
      yes.

4. A list of computational resources per image.  Default is currently
   512MB and 1 processor (oversubscribed).  Note that because this is
   a container, *only* the memory of the actual Python processes are
   needed, not the rest of the OS.

5. Do you want a ``/coursedata`` directory for shared data?  If so,
   tell us its quota.

6. Lead contact person.

7. Time period and expiry date - default is six months after the
   course is over, by which time data will be removed.  But if it will
   be used the next year, then we'll keep it up until then.


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

To use nbgrader:

- Request a course as above.

- Name all of your assignments like ``$courseslug-$assignmentname``,
  for example ``mlbp2018-week1``.  Assignment names are an accidental
  global namespace in nbgrader once they are copied to a user's
  notebook directory.

- Once you log in to your course's environment, a per-course
  ``/course`` (instructors only) and ``/srv/nbgrader/exchange``
  (instructors and students) are mounted.

- You can use the ``Formgrader`` tab at the top to manage the process
  (this automatically appears for instructors).


**WARNING:** nbgrader is `not secure
<https://github.com/jupyter/nbgrader/issues/483>`__, because it runs
the student's code as the instructor.  In fact, students can do all
sorts of bad things with this, and the only way to stop them is to
check notebooks yourself.  In fact, we can't recommend bulk usage of
nbgrader because of this.  (We are working on a local solution.)


Limits
======

- This is not a captive environment: students may always trivially
  remove their files and data, and may share notebooks across
  different courses.

- We don't have unlimited computational resources, but we can try to
  procure what is necessary.  Work as hard as you can to spread the
  load and de-peak deadlines.

- There is no integration to any other learning management systems,
  such as the CS department A+ (yet).  The only unique identifier of
  students is the Aalto username.

- Currently there is nothing in place to return marked-up assignments
  to students.  We can possibly make a root script to do this.


More info
=========

Contact: CS-IT.
