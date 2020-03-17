.. _jupytercoursedata:

Course data
===========

.. seealso::

   One of the best features of jupyter.cs is powerful data access.
   See :doc:`../jupyterhub-data`

If your course uses data, request a ``coursedata`` or ``shareddata``
directory as mentioned above.  You need to add the data there
yourself, either through the Jupyter interface or SMB mounting of
data.

If you use ``coursedata``, just start the course environment and
instructors should have permissions to put files in there.  Please try
to keep things organized!

If you use ``shareddata``, ask for permission to put data there - we
need to make the directory for you.  When asking, tell us the
(computer readable short)name of the dataset.  In the shareddata
directory, you find a README file with some more instructions.  All
datasets should have a minimum README (copy the template) which makes
it minimally usable for others.

In both cases, you need to ``chmod -R a+rX`` the data directory so
that the data becomes readable to students.

Note: after you are added to relevant group to access the data, it
make take up to 12 hours for your account information to be updated
so that it can be accessed via remote mounting.


Don't include large amount of data in the assignment directories -
there will be at least four, if not more, copies of data made for
every student.



Data from other courses
-----------------------

Sometimes, when you are in course A's environment, you want to access
the data from course B.  For example, A is the next year's edition of
the course B, and it could be useful to check the old files.

You can access the files for every course which you are an instructor
of at the path ``/m/jhnas/jupyter/course/``.  The ``files/``
sub-directory is the entire course directory for that course, the same
as ``/course/`` in each course image.  You can also access the course
data directory at ``data/`` there.

All old courses (for which you are listed as an instructor) are
available, but if the course is in the "achived" state, you can't
modify the files.
