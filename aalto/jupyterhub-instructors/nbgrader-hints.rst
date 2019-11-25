nbgrader hints
==============

These are practical hints on using nbgrader for grades and
assignments.  You should also see the separate :doc:`autograding hints
<autograding>` page if you use that.

General
-------

To export grades, ``nbgrader export`` is your central point.  It will
generate a CSV file (using a custom MyCourses exporter), which you can
download and upload to MyCourses.



If students submit assignments/you use autograding
--------------------------------------------------

.. seealso::

   :doc:`autograding`

- In each notebook (or at least the assignment zero), in the top, have
  a ``STUDENT_NUMBER = xxx`` which they have to fill in.  Asking each
  student to include the student number in a notebook ensures that you
  can later write a script to capture it.


Our scripts and resources
-------------------------

Some scripts at https://github.com/AaltoScienceIT/jupyter-wiki .

We are soon going to revise all of our instructor info which can be
useful to you later.
