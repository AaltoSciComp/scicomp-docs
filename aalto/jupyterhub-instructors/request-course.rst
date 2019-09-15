Requesting a course
===================


To get started with a course, please read the below list and describe
your needs from the relevant items (contact address is at the bottom
of this page).  Don't worry too much about understanding or answering
everything perfectly, just let us know what you want to accomplish and
we will guide you to what you need.

Course or not?
--------------

If all you need is a Python environment to do assignments and
projects, you don't need to request anything special - students can
just use the generic servers for their independent computational
needs.  Students can upload and download any files they need.  You
could add data to the "shareddata" location, which is available to any
user.

You *would* want a course environment if you want to (distribute
assignments to students via the interface) and/or (collect assignments
via the interface).

Course environment options
--------------------------

When requesting a course, please read the following and tell us your
requirements in the course request email.

A course environment consists of:

1. A course slug (of the form ``nameYEAR``, for example ``mlbp2018``)
   and full name.  (required)

2. How many students, how computationally intensive the workload is,
   how much of peak load you expect during courses or right before
   deadlines.  Expected processor and memory usage, expected data size
   both on disk and in memory.  Expected schedule (will everyone be
   doing an assignment right before the deadline?).  You should
   strongly discourage people from waiting until the last minute if
   you have hundreds of students in the course.  We'll provide
   feedback on how well we can handle the load.  (required)

3. Course schedule (lectures/exercise sessions/deadlines).  We add
   this to `our hub calendar
   <https://calendar.google.com/calendar/embed?src=d01se1d7m4gehcoruig0qkn5e4%40group.calendar.google.com>`__,
   which is used to avoid maintenance during important times.  You can
   check the calendar to avoid major deadlines at the same times as
   other courses.  Note: we've heard that late night deadlines are bad
   for students well-being, so don't make deadlines late at night just
   to reduce the peak load on our system.

4. (optional, recommended to use the default and add what you need)  A
   list of required software, or a docker container
   containing the Jupyter stack and additional
   software.  By default, we have an image based on the scipy stack
   and all the latest software that anyone else has requested, as long
   as it is mutually compatible.  You can request additional software,
   and this is shared among all courses.  If you need something
   special, you may be asked to take our image and extend it
   yourself.  Large version updates to the image are done twice a year
   during holidays.

   a. (optional) A sample python file or notebook to test that the
      environment
      works for your course (which will be made public and open
      source).  We also use use automated testing on our software
      images, so that we can be sure that our server images still work
      when they are updated.  If you send us a file, either ``.py`` or
      ``.ipynb``, we will add this to our automatic tests.  The
      minimum amount is something like ``import`` of the packages you
      need, a more advanced thing would test the libraries a little
      bit - do a minimal, quick calculation.

5. A course directory ``/course``, available only to instructors.
   This comes by default, with a quota of a few gigabytes (combined with
   coursedata).  Note: instructors should manage assignments and so on
   using git or some other version control system, because the course
   directory lasts only one year, and is renewed for the next year.

6. A list of instructors (Aalto emails or usernames).  Instructors
   will be added to a Aalto unix group named ``jupyter-$courseslug``
   to provide access control.  To request new instructors, contact
   CS-IT and ask that people be added/removed from your group
   ``jupyter-$courseslug``.

   a. Primary group owner (e.g. main instructor).  Data is stored in a
      group according to :doc:`Science-IT data policy </aalot/datapolicy>`,
      and this person is in change of knowing what data exists,
      granting access and telling us what to do with the data
      long-term and they should be a long-term staff member.  There
      can be deputies (e.g. head TA) which can grant access.

   b. People who should be added to the announcement mailing list -
      these will get updates for updates and maintenance breaks.

   c. Lead contact person, if different from instructor.

7. (optional, not recommended)  A list of students (Aalto usernames).
   This can be null if anyone
   with an Aalto account should be able to access the environment
   (this is recommended to be as open as possible and to save manual
   effort).  If you provide a list of students, you will have to
   request manual effort every time it changes, so this is *not
   recommended*.

   a. Should non-students be allowed to spawn the environment?
      Default yes...

8. Should the image start in "private mode", where only instructors
   and students from the previous point can start the course
   environment?  From our side, there is no major disadvantage to
   going public from the start.

9. (optional, not recommended) A list of computational resources per
   image.  Default is currently 2GB and 4 processors (oversubscribed).
   Note that because this is a container, *only* the memory of the
   actual Python processes are needed, not the rest of the OS, and
   memory tends to be quite small.

10. Shared data directories.  If you have nontrivial data which needs
    distributing, consider one of these shared directories which saves
    it from being copied over and over.  The notebook directory itself
    can only support files of up to 2MB to prevent possible problems.
    If number of students times
    amount of data is more than a few hundred MB, strongly consider
    one of the data directories.  Read more about this :ref:`below
    <jupytercoursedata>`.

    a.  You can use the "shareddata" directory
	``/mnt/jupyter/shareddata``.  ``shareddata`` is available in
	all notebooks on jupyter.cs.aalto.fi (even outside of your
	course) and also (eventually) other Aalto servers.  This data
	should be considered public (and have a valid license), even
	though for now it's only accessible to Aalto accounts.

    b. ``/coursedata`` is only available within your course's
       environment (as chosen from the list).  ``coursedata`` is also
       assumed to be public to everyone at Aalto, though you have more
       control over it.

    c. If you use either of these, you can embed the paths directly in
       your notebooks.  This is easy for hub use, but makes it harder
       to copy the notebooks out of the hub to use on your own
       computers.  This is something we are working on.

12. Time period and expiry date - default is six months after the
    course is over, by which time data will be removed.  But if it will
    be used the next year, then we'll keep it up until then.  We
    intentionally replace the course directories every year both for
    security and to encourage you to use maintainable processes!

