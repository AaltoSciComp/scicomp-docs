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

What does this mean?  Jupyter is not a learning management system
(even when coupled with nbgrader), it's "a way to make computational
narratives".  This means that this is not a point and click solution
to running courses, but a base to build computations on.  In order to
build a course, you need to be prepared to do your own scripting and
connections using the terminal.


You may find the book `Teaching and Learning with Jupyter
<https://jupyter4edu.github.io/jupyter-edu-book/>`__ helpful.

Currently we support Python the most, but there are `other language
kernels available for Jupyter
<https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`__.  For
research purposes, see the :doc:`Triton Jupyter page
</triton/apps/jupyter>`.


Limits
------

- This is not a captive environment: students may always trivially
  remove their files and data, and may share notebooks across
  different courses.  See above for the link to isolate-environment
  with instructions for fixing this.

- We don't have unlimited computational resources, but in practice we
  have quite a lot.  Try to avoid all students doing all the work
  right before a deadline and you should be fine, even with hundreds
  of students.

- There is no integration to any other learning management systems,
  such as the CS department A+ (yet).  The only unique identifier of
  students is the Aalto username.  ``nbgrader`` can get you a csv file
  with these usernames, what happens after that point is up to you.

- There is currently no plagiarism detection support.  You will have
  to handle this yourself somehow so far.
