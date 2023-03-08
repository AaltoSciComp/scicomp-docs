Git-annex for data management
=============================

.. seealso::

   `Video intro to git-annex, from Research Software Hour <https://www.youtube.com/watch?v=NKCBXOfyoyM&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__.


`git-annex <https://git-annex.branchable.com/>`__ is a extension to git
which allows you to manage large files with git, without checking
their contents in git.  This may seem contradictory, but it
basically creates a key-value store for large files, whose metadata is
stored in git and contents distributed using other management commands.

This page describes only a very limited set of features of git-annex
and how to use them.  In particular, it tries to break git-annex into
three "simple" types of tasks.  Git-annex can do almost anything
related to data management, but that is also its weakness (it doesn't
"do one thing and do it simply").  By breaking the possibilities down,
we can hopefully make it manageable.  The three layers are:

- **Level 1: Track metadata in git and lock file contents local-only:**
  Even on a single computer, one can rigorously track data files to
  record who produced the data, the history, and the hash of the
  content, even without recording the contents into git.  On top of
  this, files can be very safely **locked** to prevent accidental
  modification of primary copies of the data.  (commands such as ``git
  annex add``)

- **Level 2: Transfer and synchronize file content between
  repositories:** Once the metadata is tracked and the git repository
  is shared, you might want to move the content between repositories.
  You can easily do this ``git annex get``, ``git annenx copy
  [--to|--from]``.  You can put any file anywhere and metadata is
  always synced.

- **Level 3: Manage synchronization across many repositories:** Once
  you have more than two (or even more than one) repository, keeping
  track of locations of all files is hard.  Git-annex solves this as
  well: you can define what content should be in each location and
  data is automatically distributed.  So, for example, you can insist
  on all data is always stored in your object storage, all active data
  is also on the cluster, and user environments have whatever is
  requested.  Git-annex is very focused on never losing data, it can
  ensure that one locked copy is always present in some repository.
  (commands such as ``git annex wanted``, ``git annex numcopies``,
  ``git annex sync --content``)

The biggest problems are that it can do everything, which makes
documentation quite dense, and the documentation is not that great.

.. highlight:: shell-session



Background
----------

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
annex drop``, ``git annex sync``, and so on.  The basic principles of
git-annex are data integrity and security: it will try very hard to
prevent you from using git/git-annex commands to lose the only copy of
any data.



Basic setup
-----------

After you have a git repository, you run ``git annex init`` to set up
the git-annex metadata.  This is run once in each repository in the
git-annex network::

   $ git init
   $ git annex init 'triton cluster'   # give a name to the current repo



Level 1: locally locking and tracking data
------------------------------------------

You can add small files like normal using git (full content in git),
and large files with ``git annex add``, which replaces the file with a
symlink to its *locked* content::

   $ git add small-file.txt
   $ git annex add large-file.dat
   $ git commit           # metadata: commit message, author, etc.

Now, your content is safe: it is a symlink to somewhere in
``.git/annex/objects`` and it is almost impossible for you to
accidentally lose the data.  If you do want to modify a file, first
run ``git annex unlock``, and then commit it again when done.  The
original content is saved until you clean it up (unless you configure
otherwise).  The **largefiles** settings will determine the behavior
of ``git add``, you can set which files should always be committed to
the annex (instead of git).

At this point, ``git push|pull`` will only move metadata around (the
commit message and link to ``.git/objects/AA/BB/HHHHHHHH``, with the
hash ``HHHHH`` a unique hash of the file contents).  This is what is
stored in the primary git history itself.

Structured metadata (arbitrary key/value pairs) can be assigned to any
files with ``git annex metadata`` (and can be automatically generated
when files are first added, such as the date of addition).  Files can
be filtered and transferred based on this metadata.  Structured
metadata helps us manage data much better once we get to level 3.

So now, with little work, we have a normal git repository that
provides a history (metadata) to other data files, keeps them safe,
and can be used like a normal repository.

Relevant commands:

* ``git annex init``
* ``git annex add``
* ``git annex unannex``
* ``git annex unlock``
* ``git annex lock``
* ``git annex metadata``
* ``git annex info``
* Configuration ``annex.largefiles``



Level 2: moving data
--------------------

Data in one place isn't enough, so let's do more.  Just like git
remotes, **git-annex remotes** allow moving data around in a
*decentralized* manner.

- Regular git remotes work, if the git-annex shell tools are
  installed.
- Git-annex **special remotes**, which essentially serve as key-value
  stores.  Options include `S3, cloud drives, rsync, and many, many
  more <https://git-annex.branchable.com/special_remotes/>`__.

Regular git remotes are set up with ``git annex init`` on the remote
side.  Special remotes are created with ``git annex initremote``.
Every remote has a unique name and UUID to manage data locations.

Once the remotes are set up, you can move data around::

  $ git annex get data/input1.dat                # get data from any available source
  $ git annex copy --to=archive data/input2.dat

You can remove data from a repo, but git-annex will actively connect
to other remotes to verify that other copies of the file exist before
dropping it::

  $ git annex drop data/scratch1.txt

These commands more around data in ``.git/annex/objects/`` and update
tracking information on the special ``git-annex`` branch so that
git-annex knows which remotes have which files - very important to
avoid a giant mess!

Special remotes can be created like such::

  $ git annex initremote NAME type=S3 encryption=shared host=a3s.fi

And enabled in other git repositories to make more links within the
repository network::

  $ git annex enableremote NAME

Note that special remotes are client-side encrypted unless you set
``encryption=none``, and also chunked to deal with huge files even on
remotes which do not support them.

Relevant commands:

* ``git annex get``
* ``git annex drop``
* ``git annex move``
* ``git annex copy``
* ``git annex list``
* ``git annex find``
* ``git annex initremote``
* ``git annex enableremote``



Level 3: synchronizing data
---------------------------

Moving data is great, but when data becomes Big, manually managing it
doesn't work.  Git-annex *really* shines here.  The most basic command
is ``sync --content``, which will automatically commit anything new
(to git or the annex depending on the largefiles rules) and distribute
all data everywhere reachable (including regular git-tracked files).
Without ``--content``, it syncs only metadata and regular commits::

  $ git annex sync --content

But, all data everywhere doesn't scale to complex situations: we need
to somehow define what goes where.  And this should be done
declaratively.  One of the most basic declarations in the minimum
number of copies allowed **numcopies**.  Git-annex won't let you drop
a file from a repository without being very sure that this many copies
exist in other repositories.  This setting is synced through the
entire repository network::

  $ git annex numcopies N

The next level is `preferred content
<https://git-annex.branchable.com/preferred_content/>`__, which
specifies what files a given repository wants.  ``git annex sync
--content`` will use these expressions to determine what to send
where::

   $ git annex wanted . 'include=*.mp3 and (not largerthan=100mb) and exclude=old/*'
   $ git annex wanted archive 'anything'
   $ git annex wanted cluster 'present or copies=1'

Repository groups and `standard groups
<https://git-annex.branchable.com/preferred_content/standard_groups/>`__
allow you to more easily define rules (the standard groups list lets
you see the power of these expressions).  Various built-in background
processes can automatically watch for new files and run ``git annex
sync --content`` automatically for you, which can make your data
management a fully automatic process.  Repository transfer costs can
allow git-annex to fetch data from a nearby source, rather than a
further one.  Client-side encryption can allow you to use any
available storage with confidence.

Relevant commands:

* ``git annex sync [--content]``
* ``git annex numcopies``
* ``git annex trust``
* ``git annex untrust``
* ``git annex group``
* ``git annex wanted``
* ``git annex groupwanted``
* ``git annex required``
* ``git annex unused``
* ``git annex schedule``
* ``git annex watch``




..
   assumes and will let you:

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



See also
--------

- `Video intro to git-annex, from Research Software Hour <https://www.youtube.com/watch?v=NKCBXOfyoyM&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__.

- **git LFS**  These two git extensions are often
  compared.  git LFS is created by GitHub, and operates on a centralized
  model: there is one server, all data goes there.  This introduces a
  single point of failure, requires a special server capable of holding
  all data, and loses distributed features.  git-annex is a true
  distributed system, and thus better for large scale data management.

- **dvc**: The level 1/2 use case is practically copied from
  git-annex.  It seems to have a lot less flexibility on high-level
  data management, client-side encryption. The main point of dvc seems
  to be track commands that have been run and their inputs/output to
  make those commands reproducible, which is completely different from
  git-annex.  Most importantly (to the author of this page) it has
  default-on analytics sent to remote servers, which makes its ethics
  questionable.
