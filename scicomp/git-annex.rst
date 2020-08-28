``git-annex`` for data management
=================================


``git-annex`` is a extension to git which allows you to store large
files with git, but not in git.  This may seem contradictory, but what
it basically creates a key-value store to store large objects, where
the metadata (filenames, checksums, etc) is stored in the repository
and there is a way to distribute the files between repositories.

This page will describe only a very limited set of features of
git-annex.  In particular, it assumes and will let you:

- Store a number of files in git-annex, making them read-only (in a
  way that is much harder to accidentally break) and providing you
  checksumming for integrity checking.

- Do partial checkouts of data on other systems.

- Allow you to back up certain files to another system by ssh.  There
  will be support to ensure you have enough copies of the files on
  secure systems.

- Back up files to a third-party system, such as CSC's archival
  systems, using special protocols (like S3 or iRODS) with client-side
  encryption.  This allows secure storage of data anywhere.


**git-annex vs git LFS**  These two git extensions are often
compared.  git LFS is created by GitHub, and operates on a centralized
model: there is one server, all data goes there.  This introduces a
single point of failure, requires a special server capable of holding
all data, and loses distributed features.  git-annex is a true
distributed system, and thus better for large scale data management.


Background
==========

You probably know what git is - it tracks versions of files.  The full
history of every file is kept.  When something is recorded in
git-annex, the raw data is a separate storage area, and only links to
that and the metadata is distributed using regular git.  So, all
clones *know about* all files, but don't necessarily have all data.
Using ``git annex get``, one can get the raw data from another repo
and make it available locally.


For example, this is a ``ls -l`` of a real git repository which has a
``small-file.txt`` and a ``large-file.dat``.  You see that the small
file is just there, but the large file is a symlink to ``.git/annex/objects/XX/YY/...``::

   $ ls -l
   lrwxrwxrwx 1 darstr1 darstr1 200 Feb  4 11:08 large-file.dat -> .git/annex/objects/X4/xZ/SHA256E-s10485760--4c95ccee15c93531c1aa0527ad73bf1ed558f511306d848f34cb13017513ed34.dat/SHA256E-s10485760--4c95ccee15c93531c1aa0527ad73bf1ed558f511306d848f34cb13017513ed34.dat
   -rw-rw-r-- 1 darstr1 darstr1  21 Feb  4 11:06 small-file.txt

If the repository has the file, the symlink target exists.  If the
repository doesn't have the file, it's a dangling symlink.  ``git
add`` works like normal, ``git annex add`` makes the symlink.

Now let's ``git annex list`` here.  We see there are two repositories,
``here`` and ``demo2``.  ``large-file.dat`` is in both, as you can see
by the ``X``\ s.  ("web" and "bittorrent" are advanced features, not
used unless you request... but give you the idea of what you can do)::

  here
  |demo2
  ||web
  |||bittorrent
  ||||
  XX__ large-file.dat

The basic commands to distribute data are ``git annex get``, ``git
annex drop``, ``git annex sync``, and so on.





Basic setup
===========

In this section, you learn how to create a repository that tracks
large data files and makes them read-only.


::

   $ git init
   $ git annex init

   $ git add small-file.txt
   $ git annex add large-file.dat

