=================
Data organization
=================

How should data be stored?  On the simplest level, this asks "on what
physical disks", but this page is concerned about something more
high-level: how you organize data on those disks.

Data organization is very important, because if you don't do it early,
you end up with a *epic* mess which you will never have time to clean
up.  If you organize data well, then everything after becomes much
easier: you can archive what you need.  Others can find what they
need.  You can open what you need easily.

**Everything here applies equally if you are working alone or if you
are part of a team.**


Organize your projects into directories
---------------------------------------

Names
~~~~~

As simple as it seems, choosing a good name for each distinct
workspace is an important first step.  This serves as an identifier to you
and others, and by having a name you are able to refer to, find, and
organize your data now and in the future.

A name should be unique among all of your work over all your career,
and also unique among all of your colleagues, too (and any major
public projects, too).  Don't reuse the same names for related things.
For example, let's say I have a project called ``xproject``.  If I
track the code separately from the data, I'd have a different
directory called ``xproject-data`` and the main projects refers to
the data directory, instead of coping the data.

How many named workspaces should you have for each project?  It
depends on how large they are and how diverse the types of data are.
If the data is small and not very demanding, it doesn't matter much.
If you have large data vs small other files, it may be good to
separate out the data.  If you have some data/code/files which will be
reused in different projects, it makes sense to split them.  If you
have confidential data that can't be shared, it's good to separate
them from the rest of the data.

Names should be usable and directory names and identifiers.  Try to
stick to letters, numbers, ``-``, and ``_`` - no spaces, punctuation,
or symbols.  Then, the name is usable on repositories and other
services, too.

Good names include ``MobilityAnalysis``, ``transit``, ``transit-hsl``,
and ``lgm-paper``.  Bad names are too general given their purpose or
what else you might do.

Each directory's contents moves together as a unit, as much as
possible.

Organizing these directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should have a flat organization in as few places as
possible.  For example, on your laptop you may have ``~/project`` for
things for the stuff you mainly work on and ``~/git`` for other minor
version controlled things.  On your workstations or servers, you may
also have ``/scratch/work/$username`` which is your personal stuff
that is not backed up, ``/m/cs/project/$groupname/$username/`` which
is backed up, ``/local`` which is temporary stuff on your own
computer, and so on.  The server-based locations can be easily shared
among multiple people.

Your structure should be as **flat** as possible, without many layers
in each directory.  Thus, to find a given project, you only need to
look inside each of the main locations above, not inside every other
project.  This allows you to get the gist of your data for future
archival or clean-up.  When two directories need to refer to each
other, you have them directly refer to each other where they are, for
example use ``../xproject-data`` from inside the ``xproject``
directory.  (You can have subdirectories inside the projects).

Different types of projects go in different places.  For example,
``xproject`` can be on the backed up location because it's your
daily work, while ``xproject-data`` is on some non-backed up place
because you can always recover the data.


Synchronizing
~~~~~~~~~~~~~

If you work on different systems, each directory of the same name
*should* have roughly the same contents - as if you could synchronize
it with version control.

For small stuff, you might synchronize with version control.  You may
use some other program, like Dropbox or the like.  Or in the case of
data which has a master copy somewhere else, you just download what
you need.



Organize files within directories
---------------------------------

Traditional organization
~~~~~~~~~~~~~~~~~~~~~~~~

This is the traditional organization within a single person's project.
The key concept is separation of code, original data, scratch data, and
final outputs. Each is handled properly.

-  ``PROJECT/code/`` - backed up and tracked in a version control system.
-  ``PROJECT/original/`` - original and irreplaceable data. Backed up at the
   same time it is placed here.
-  ``PROJECT/scratch/`` - bulk data, can be regenerated from code+original
-  ``PROJECT/doc/`` - final outputs, which should be kept for a very long
   term.
-  ``PROJECT/doc/paper1/`` - different papers/reports, if not stored
   in a different project directory.
-  ``PROJECT/doc/paper2/``
-  ``PROJECT/doc/opendata/``

When the project is over, ``code/`` and ``doc/`` can be backed up permanently
(``original/`` is already backed up) and the scratch directory can be kept
for a reasonable time before it is removed (or put into cold storage).

The most important thing is that code is kept separate from the data.
This means no copying files over and over to minor variations. Could
should be adjustable for different purposes (and you can always get the
old versions from version control). Code is run from the code directory,
no need to copy to each folder individually.

Multi-user
~~~~~~~~~~

The system above can be trivially adapted to suit a project with
multiple users:

-  ``PROJECT/USER1/....`` - each user directory has their own ``code/``,
   ``scratch/``, and ``doc/`` directories. Code is synced via the version
   control system. People use the original data straight from the shared
   folder in the project.
-  ``PROJECT/USER2/....``
-  ``PROJECT/original/`` - this is the original data.
-  ``PROJECT/scratch/`` - shared intermediate files, if they are stable
   enough to be shared.

For convenience, each user can create a symbolic link to the original/
data directory from their own directory.

Master project
~~~~~~~~~~~~~~

In this, you have one long-term master directory for a whole research
group, and members project that has many different
users and research themes with in. As time goes on, once users leave,
their directories can be cleaned up and removed. The same can happen for
the themes.

-  ``PROJECT/USER1/SUBPROJECT1/...``
-  ``PROJECT/USER1/SUBPROJECT2/...``
-  ``PROJECT/USER2/SUBPROJECT1/...``
-  ``PROJECT/original/``
-  ``PROJECT/THEME/USER1/...``
-  ``PROJECT/THEME/USER2/...``
-  ``PROJECT/archive/``

Common variants
~~~~~~~~~~~~~~~

-  Simulations with different parameters: all parameters are stored in
   the code directory, within version control. The code knows what
   parameters to use when making a new run. This makes it easy to see
   the entire history of your simulations.
-  Downloading data: this can be put into either original or scratch,
   depending on how much you trust the original source to stay
   available.
-  Multiple sub-projects: this can be
-  Multiple types of code: separate long-term code from scratch research
   code. You can separate parameters from code. And so on...

Projects
--------

In Aalto, data is organized into project groups. Each project has
members who can access the data, and different shared storage spaces
(project, archive, scratch (see below)). You can apply for these
whenever you need.

What should a project contain? How much should go into the same project?

-  **One project that lasts forever per research group:** This is
   traditional. A professor will get a project allocated, and then
   people put data in here. There may be subdirectories for each
   researcher or topic, and some shared folders for common data. The
   problem here is that the size will grow without bound. Who will ever
   clean up all the old stuff? These have a way of growing forever so
   that the data becomes no longer manageable, but they are convenient
   because it keeps the organization flat.

   -  If data size is small and growing slower than storage, this works
      for long-term.
   -  It can also work if particular temporary files are managed well
      and eventually removed.

-  **One project for each distinct theme:** A research group may become
   interested in some topic (for example, a distinct funded project),
   and they get storage space just for this. The project goes on and is
   eventually closed.

   -  You can be more fine-grained in access, if data is confidential
   -  You can ensure that the data stays together
   -  You can ensure that data end-of-life happens properly. This is
      especially useful for showing you are managing data properly as
      part of grant applications.
   -  You can have a master group as a member of the specific project.
      This allows a flat organization, where all of your members can
      access all data in different projects.



