Public copy of assignments
==========================

One disadvantage of a powerful system is that we have to limit access
to authorized users.  But you shouldn't let this limit access to your
course: there is nothing special about our system, and if you allow
others to see your assignments, they can run them themselves.  For
example, the service https://mybinder.org allows anyone to run
arbitrary notebooks from git repositories.



This is also important because your course environment will go away
after a few months - do you want students to be able to refer to it
later?  If so, do the below.

- change to the ``release/`` directory and ``git init``.  Create a new
  repo here.
- Manually ``git add`` the necessary assignment files after they are
  generated from the ``source`` directory.  Why do we need a new repo?
  Because you can't have the instructor solutions/answers made public.

- Update files (``git commit -a`` or some such) occasionally when new
  versions come out.

- Add a ``requirements.txt`` file listing the different packages you
  need installed for a student to use the notebooks.  See the
  `MyBinder instructions
  <https://mybinder.readthedocs.io/en/latest/introduction.html#preparing-a-repository-for-binder>`__
  for different ways to do this, but a normal Python
  ``requirements.txt`` file is easiest for most cases.  On each line,
  put in a name of a package from the Python Package Index.  There are
  other formats for ``R``, ``conda``, etc, see the page.

- Then, push this ``release/`` repo to a public repository (check
  mybinder for supported locations).  Make sure you don't ever
  accidentally push the course repository!

- Then, go to https://mybinder.org/ and use the UI to create a URL for
  the resources.  You can paste this button into your course
  materials, so that it's a one-click process to run your assignments.

- Note that mybinder has a limit of 100 simultaneous users for a
  repository, to prevent too much use for single organization's
  projects.  This shouldn't be the first place you direct students for
  day-to-day work.

- If you have a ``/coursedata`` directory, you will have to provide
  these files some other way.  You could put them in the assignment
  directory and the ``release/`` git repository, but then you'll need
  to have notebooks able to load them from two places: ``/coursedata``
  or ``.``.  I'd recommend do this: ``import os``, ``if
  os.path.exists('/coursedata'): DATADIR='/coursedata'``,  ``else:
  DATADIR='.'`` and then access all data files by
  ``os.path.join('DATADIR', 'filename.dat')``.  This has the added
  advantage that it's easy to swap out ``DATADIR`` later, too.
