Nbgrader hints
==============

These are practical hints on using nbgrader for grades and
assignments.  You should also see the separate :doc:`autograding hints
<autograding>` page if you use that.



General
-------

To export grades, ``nbgrader export`` is your central point.  It will
generate a CSV file (using a custom MyCourses exporter), which you can
download, check, and upload to MyCourses.

For comprehensive details, see :doc:`exporting-grades`.



If students submit assignments/you use autograding
--------------------------------------------------

.. seealso::

   :doc:`autograding`

- In each notebook (or at least the assignment zero), in the top, have
  a ``STUDENT_NUMBER = xxx`` which they have to fill in.  Asking each
  student to include the student number in a notebook ensures that you
  can later write a script to capture it.



Late Submission
---------------

In this section, we will discuss how to handle late submissions and collection in nbgrader. You might need to customize some configurations, which you will write in the ``nbgrader_config.py`` file if you are using your own nbgrader configuration, or in the ``etc.jupyter.nbgrader_config.py.append`` file if you are using the default configuration (refer to the :doc:`./nbgrader` to learn more about the configuration). Either way, this file will be referred to as the **configuration file**.

Collection
~~~~~~~~~~
Before autograding, the submissions are collected from the students. The default behavior is to collect all submissions, regardless of the due date. This can become a problem if a student submits the assignment both before and after the due date. In this case, the student's grade will be based on the last submission.

You can change this behavior by setting the ``c.ExchangeCollect.before_duedate`` to ``True`` in the configuration file. This will collect the students' *last* submission before the due date, or their last late submission if there is no submission before due date.

.. code:: python

   c.ExchangeCollect.before_duedate = True

The late submission policies in the following section will affect the submissions collected after the due date regardless.

Policies and Plugins
~~~~~~~~~~~~~~~~~~~~

The default policy is ``none``, which does nothing (no penalty assigned).

Another policy provided by the default plugin is ``zero``, which assigns a zero grade to late submissions. You can change the policy by setting the ``c.LateSubmissionPlugin.policy`` in the configuration file:

.. code:: python

   c.LateSubmissionPlugin.policy = 'zero'
  

In addition, you can set your desired late submission policy for your course. There are some pre-defined policies that you can choose from, or send us a ticket describing the policy and we will try to create it for you.

.. seealso::

   :doc:`request-course`

The policies are defined in the ``aalto_nbgrader_late.py`` file (visible under the path ``/m/jhnas/jupyter/software/pymod/``). So far, the available policies are:

1. ``SubMarks``: The student's grade is reduced by a fixed number of marks for each hour the assignment is late (``penalty_unit=1`` would reduce 1 mark per hour from the submission score).

2. ``SubSteps``: The student's grade is reduced by a fixed number of marks every few hours the assignment is late.

3. ``SubRatio``: The student's grade is reduced by a fixed ratio for every day the assignment is late.

Moreover, you can provide a list of students to exempt from the late submission policy. You can set the list by adding a line to the nbgrader configuration file (see the example below).


.. admonition:: Example
   
   To adopt the ``SubRatio`` policy, you can use the following lines:

   .. code:: python
   
      c.AssignLatePenalties.plugin_class = 'aalto_nbgrader_late.SubRatio'
      c.SubRatio.penalty_unit = 0.2
      c.SubRatio.student_extensions = {"student1": 3600 * 24, "student2": 3600 * 12}

   In this example, the **SubRatio** policy is used with a penalty ratio of 20% per day. The students *student1* and *student2* are granted 24 hours and 12 hours extension respectively.

Another way to extend the deadline for some students is using the Formgrader interface, which is explained in the next section. We recommend using one approach or the other, as using both at the same time may cause issues.

Grant Extensions
~~~~~~~~~~~~~~~~

Another way to extend the deadline for some students is to use the "🗓️ Grant Extension" button on the "Manage Submissions" page for each individual.

.. note::
    
   - You can grant extensions to autograded submissions only.

   - The students cannot see the extension granted to them. You can inform them yourself.


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
exchange for your own testing  (Actually, this isn't even needed, you
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
  upstream limitation.  Contact us and we can run a script that will
  release the feedback to your students.



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
to link to email addresses, you can do the following.  (Note: the
format USERNAME@aalto.fi works for MyCourses upload, this process is
not usually needed these days anymore.)

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

__ https://github.com/AaltoSciComp/jupyterhub-aalto/blob/master/user-scripts/username-to-email.py




Our scripts and resources
-------------------------

Some scripts at https://github.com/AaltoSciComp/jupyter-wiki .

We are soon going to revise all of our instructor info which can be
useful to you later.
