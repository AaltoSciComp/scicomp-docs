nbgrader hints
==============

These are practical hints on using nbgrader for grades and
assignments.  You should also see the separate :doc:`autograding hints
<autograding>` page if you use that.



General
-------

To export grades, ``nbgrader export`` is your central point.  It will
generate a CSV file (using a custom MyCourses exporter), which you can
download, check, and upload to MyCourses.



If students submit assignments/you use autograding
--------------------------------------------------

.. seealso::

   :doc:`autograding`

- In each notebook (or at least the assignment zero), in the top, have
  a ``STUDENT_NUMBER = xxx`` which they have to fill in.  Asking each
  student to include the student number in a notebook ensures that you
  can later write a script to capture it.



Testing releasing assignments, without students seeing
------------------------------------------------------

Sometimes instructors want to release and collect assignments as a
test, while the course is running.  To understand how the solution is
simpler than "make a new course", we need to understand what "release"
and "collect" do: they just move files around.  So, you can just move
them to a different place (called the **exchange**) instead of the one
that all students see.  Nbgrader docs sure doesn't do a good job of
explaining it, but behind the scenes it's quite simple, and that
simplicity means it's easy to control if you know what you are up
to...

You can equally move your test files around to a test, instructor-only
exchange for your own testing.  (Actually, this isn't even needed, you
can just copy them directly, test, and put back in the ``submitted/``
directory.  But some people want more.  So, from the jupyter terminal,
we have made these extra aliases::

   # Release to test exchange (as instructor):
   nbgrader-instructor-exchange release_assignment  $assignment_id
   # Fetch from test exchange (as instructor, pretending to be a student):
   nbgrader-instructor-exchange fetch_assignment  $assignment_id
   # Submit to test exchange (as instructor, pretending to be a student):
   nbgrader-instructor-exchange submit $assignment_id
   # Collect to test exchange (as instructor):
   nbgrader-instructor-exchange collect $assignment_id

This copies files to and from ``/course/test-instructor-exchange/``,
which you can examine and fully control.  If you are doing this, you
probably need that control anyway.  These terms match the normal
nbgrader terminology.

There's no easy way to make a switch between "live exchange" and
"instructor exchange" in the web interface, but because of the power
of the command line, we can easily do it anyway.

(use ``type -a nbgrader-instructor-exchange`` to see just what it does.)



Known problems
--------------

* The built-in feedback functionality doesn't work if you modify the
  submitted notebooks (for example, to make them run).  nbgrader
  upstream limitation.



Course data
-----------

If you use the ``/coursedata`` directory and want the notebook to be
usable outside of JupyterHub too, try this pattern:

.. code:: python

   import os
   if 'AALTO_JUPYTERHUB' in os.environ:
       DATA = '/coursedata'
   else:
       DATA = 'put_path_here'

   # when loading data, always os.path.join(DATA, 'the_file.py')

This way, the file can be easily modified to load data from somewhere
else.  Of course, many variations are possible.



Converting usernames to emails
------------------------------

JupyterHub has no access to emails or student numbers.  If you do need
to link to email addresses, you can do the following.

* ssh to kosh.aalto.fi

* cd to wherever you have exported a csv file with your grades (for
  example your course directory, ``cd
  /m/jhnas/jupyter/course/$course_slug/files/``).

* Run ``/m/jhnas/jupyter/software/bin/username-to-email.py
  exported_grades.csv`` - this will add an email column right after
  the username column.  If the username column is not the zeroth
  (counting from zero), use the ``-c $N`` option to tell it that the
  usernames are in the ``N``\ th column (zero indexed).

* Save the output somewhere, for example you could redirect it using
  ``>`` to a new filename.  A full example::

    /m/jhnas/jupyter/software/bin/username-to-email.py mycourses_export.csv > mycourses_usernames.csv

This script is also `available on github`__.

__ https://github.com/AaltoScienceIT/jupyterhub-aalto/blob/master/user-scripts/username-to-email.py




Our scripts and resources
-------------------------

Some scripts at https://github.com/AaltoScienceIT/jupyter-wiki .

We are soon going to revise all of our instructor info which can be
useful to you later.
