Testing a course
================

Often, people ask "how can I test the assignments if I use nbgrader"?
There are different options.



Test as an instructor
---------------------

The instructor functions don't overlap with the student functions: you
don't need some special way to test the student experience.

As an instructor, you can release assignments, then go to the student
view, fetch, do, submit, etc.  This is the same experience as students
would get, and really is the full experience (there is not much else
to test).  You and your TAs can test this way - and of course you can
add others just for the purpose of testing it this way.

Of course, you can add TAs just for the purpose of testing it like
this, and this would be recommended (as long as nothing is secret is
the course directory at the time you are doing these tests - remember
to remove them later).  You can do this yourself using the group
management service we send you (domesti.cs).

An instructor also has an option in the server list to spawn as a
student.  This hides the ``/course`` directory and makes the
environment identical to that of a student (but it shouldn't matter
much).



Send assignments to testers yourself
------------------------------------

Before all this fancy Jupyter interface, nbgrader was very simple:
send assignments around manually.  For example, they would post
assignments on the course website, people would submit via the course
site, and they would be downloaded and unpacked into the right places
in the course directory.  This is still probably the best way to test
things out.

Steps:

* To send an assignment to someone: download the generated release
  version from ``/course/release/$assignment_id/$name.ipynb`` .
* Send (e.g. email) to someone.  They send it back to you when done.
  They can do the assignment on their own computer, or upload to
  jupyter.cs to do it (the "general use" server works fine).
* To receive the assignment, put it back in the course dir as
  ``/course/submitted/$STUDENT_NAME/$assignment_id/$name.ipynb``.
  ``$STUDENT_NAME`` is invented by you, but the others should match.

That is all: now you can autograde and all, completely normally.
*This is all that the web interface does anyway*.

When you are done testing, you can delete these ``$STUDENT_NAME``
directories.  There is also some command to delete them from the
database if you want, or more likely you might remove the whole
``gradebook.db`` to make sure you start fresh.

The shell access (and other data access, see
:doc:`system-environment`) makes it easy to manage these files, copy
them in and out, and so on.



Add student testers while in private mode
-----------------------------------------

While your course is still in private mode, you can add dedicated
student testers.  This might be useful before the course becomes public.

- While this works, we don't recommend it unless you really need a lot
  of testers.  It is manual work to set up, and manual work to
  remove.  And likely we are going to forget to clean it up later.
- Just like above, you may need to clean up these test students.
- Send us a list of Aalto emails or usernames to add.



Request another course
----------------------

In principle, you could request a whole other jupyter.cs course, just
for testing, and we could add private students there.  But this would
be a lot of work for us (and some for you, when you need to transfer
files over - but if you use git that part won't be that bad).

In general, we don't do this - one of the above options should work
for you.  Even if you do this, you likely have to combine with some of
the above tasks (requesting us to add students while in private mode).



Nbgrader on your own computer
-----------------------------

You can always install nbgrader yourself, on your own computer, to
test out how it works.  Probably this is not for everyone, but is
effective to test things out.
