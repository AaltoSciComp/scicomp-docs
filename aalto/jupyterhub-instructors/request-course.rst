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
requirements in the course request email.  If you are using the hub
without a specific course item in the selection list, please let us
know at least 3a, 6, 7, and 8 below.

Required metadata is:

.. list-table::

   * * 1. Course slug
     * Permanent identifier of course, of the form ``nameYEAR``, for
       example ``mlbp2018``) and full name.

   * * 2. Course display name
     * What students see in the interface

   * * 3. Contact
     * Who to ask about day-to-day matters, could be multiple.  Aalto
       emails or usernames.

   * *
     * 3a. Who should be added to the "announcement" issue and gets
       announcements about updates during the periods.

   * * 4. Supervisor
     * Long-term staff who can answer questions about old data even if
       the course TAs move on.  Might be same as contact.  This is the
       "primary owner" of all data according to the :doc:`Science-IT
       data policy </aalto/datapolicy>`.

   * * 5. Instructors
     * Who will have access to the instructor data?  Instructors will
       be added to a Aalto unix group named ``jupyter-$courseslug`` to
       provide access control.  To request new instructors, you do
       this yourself (:doc:`see the relevant FAQ <faq-hints>`).  Or, email
       CS-IT and ask that people be added/removed from your group
       ``jupyter-$courseslug``.

   * * 6. Number of students
     * Just to keep track of expected load and so on.

   * * 7. Course schedule
     * Sessions when all students will be using it (e.g. lectures,
       tutorials).  Deadlines when you expect many students will be
       working. Will be added to `our hub calendar
       <https://calendar.google.com/calendar/embed?src=d01se1d7m4gehcoruig0qkn5e4%40group.calendar.google.com>`__,
       to avoid doing maintenance when at critical moments.  Please do
       whatever you can to de-peak loads, but in reality we can
       probably handle whatever you throw at as.  Very late night
       deadlines are usually not good since we often do maintenance
       then (and are bad for students...).

   * * 8. Expected load
     * What kind of assignments?  Lots of CPU, memory intensive?
       Knowing how people use the resources helps us to make things
       work well.

   * * 9. Course time frame
     * What periods is the course?  Note: these aren't automatically
       used yet, you may still have to mail us to make it private or
       not.

   * *
     * 9a. Public date - course automatically becomes public on this
       date (until then, students can't see it).

   * *
     * 9b. Hide date - course automatically goes back to private mode
       on this date. (it's fine and recommended to give a long buffer
       here).

   * *
     * 9c. Archive date - course goes into "archive" mode after this
       time, gets hidden from instructors, too.

   * *
     * 9a. Delete date - data removed.  Not automatic, contacts will
       get an email to confirm (we aren't crazy).


A course environment consists of (comment on any specifics here):

1. A course directory ``/course``, available only to instructors.
   This comes by default, with a quota of a few gigabytes (combined with
   coursedata).  Note: instructors should manage assignments and so on
   using git or some other version control system, because the course
   directory lasts only one year, and is renewed for the next year.

2. **Software** (optional, recommended to use the default and add what you need)  A
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

3. **Computational resources** (optional, not recommended) A list of computational resources per
   image.  Default is currently 2GB and 4 processors (oversubscribed).
   Note that because this is a container, *only* the memory of the
   actual Python processes are needed, not the rest of the OS, and
   memory tends to be quite small.

4.  **Shared data directories.**  If you have nontrivial data which needs
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
