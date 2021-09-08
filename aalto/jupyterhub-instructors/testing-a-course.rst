Testing a course
================

Often, people ask "how can I test the assignments if I use nbgrader"?
There are different options.



Test as an instructor
---------------------

As an instructor, you can release assignments, then go to the student
view, fetch, do, submit, etc.  This is the same experience as students
would get, and there is not really much more to test other than this.
You can and TAs (or TAs you add just for this purpose) can test this
way.

An instructor also has an option in the server list to spawn as a
student.  This hides the ``/course`` directory and makes the
environment identical to that of a student (but it shouldn't matter
much).



Send assignments yourself
-------------------------

Before all this fancy Jupyter interface, nbgrader was very simple:
send assignments around manually.  For example, they would post
assignments on the course webpage, people would submit, and they would
be unpacked to the right format.  This is still probably the best way
to test things out.

* To send an assignment to someone: download and send from
  ``/course/release/$assignment_id/$name.ipynb``.
* Send (e.g. email, posting somewhere) to someone.  They send it back
  to you when done.  They can do it on their own computer, or upload
  to jupyter.cs to do it.
* To receive the assignment, put it back in the course dir as
  ``/course/submitted/$STUDENT_NAME/$assignment_id/$name.ipynb``.
  ``$STUDENT_NAME`` is invented by you, but the others should match.

That is all: now you can autograde and all, completely normally.
*This is all that the web interface does anyway*.

When you are done testing, you can delete these ``$STUDENT_NAME``\ s.
There is also some command to delete them from the database, or more
likely you might remove the whole ``gradebook.db`` to make sure you
start fresh.



Add student testers while in private mode
-----------------------------------------

Your course can be private, and we can add students who can launch it
(as students, not as instructors).

- Send us a list of Aalto emails or usernames to add.
- This is manual work, we don't recommend doing this.  Plus, we are
  eventually going to forget that we added these special students,
  they will maintain access even after the course, and whe knows what
  else.



Nbgrader on your own computer
-----------------------------

You can always install nbgrader yourself, on your own computer, to
test out how it works.  Probably this is not for everyone, but is
effective to test things out.



Request another course
----------------------

In principle, you could request a whole other jupyter.cs course, just
for testing, and we could add private students there.  But this would
be a lot of work for us (and some for you, when you need to transfer
files over - but if you use git that part won't be that bad).

In general, we don't do this - one of the above options should work
for you.
