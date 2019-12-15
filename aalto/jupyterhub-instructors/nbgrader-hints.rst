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



Our scripts and resources
-------------------------

Some scripts at https://github.com/AaltoScienceIT/jupyter-wiki .

We are soon going to revise all of our instructor info which can be
useful to you later.
