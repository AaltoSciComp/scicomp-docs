=================
Data organization
=================


.. note::

   This is a work in progress.

Where should data be stored? How should it be handled so that it exists
and someone can make sense of it 5 years from now? These are important
questions but it's not always clear how to do things properly. It is not
obvious how to do this, and it is rarely taught. There is a long way
between processing your own data on your own computer for your own
courses to taking part in high-level research.

This page provides a summary of different types of data and the types of
storage locations available, so that they can be matched properly. It
also provides some practical advice for organizing data both for single
people and large, long-term projects.

How to arrange data?
====================

Data management isn't just picking a place to put data and keeping
everything there. You have to keep it organized so that you can archive
the long-term parts, back up the important parts parts, and eventually
get rid of the irrelevant parts at the end. If you don't think about
this in advance, you will end up losing *all* of your data once drives
fail, accounts expire, or someone stops copying it.

Traditional organization
~~~~~~~~~~~~~~~~~~~~~~~~

This is the traditional organization within a single person's project.
The key concept is separation of code, original data, scratch data, and
final outputs. Each is handled properly.

-  PROJECT/code/ - backed up and tracked in a version control system.
-  PROJECT/original/ - original and irreplaceable data. Backed up at the
   same time it is placed here.
-  PROJECT/scratch/ - bulk data, can be regenerated from code+original
-  PROJECT/doc/ - final outputs, which should be kept for a very long
   term.
-  PROJECT/doc/paper1/
-  PROJECT/doc/paper2/
-  PROJECT/doc/opendata/

When the project is over, code/ and doc/ can be backed up permanently
(original/ is already backed up) and the scratch directory can be kept
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

-  PROJECT/USER1/.... - each user directory has their own code/,
   scratch/, and doc/ directories. Code is synced via the version
   control system. People use the original data straight from the shared
   folder in the project.
-  PROJECT/USER2/....
-  PROJECT/original/ - this is the original data.
-  PROJECT/scratch/ - shared intermediate files, if they are stable
   enough to be shared.

For convenience, each user can create a symbolic link to the original/
data directory from their own directory.

Master project
~~~~~~~~~~~~~~

In this, you have one long-term master project that has many different
users and research themes with in. As time goes on, once users leave,
their directories can be cleaned up and removed. The same can happen for
the themes.

-  PROJECT/USER1/SUBPROJECT1/...
-  PROJECT/USER1/SUBPROJECT2/...
-  PROJECT/USER2/SUBPROJECT1/...
-  PROJECT/original/
-  PROJECT/THEME/USER1/...
-  PROJECT/THEME/USER2/...
-  PROJECT/archive/

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
========

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



