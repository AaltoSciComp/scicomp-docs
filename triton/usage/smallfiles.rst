===========
Small files
===========

Millions of small files are a huge problem on any filesystem.  You may
think /scratch, being a fast filesystem, doesn't have this problem, but
it's actually worse here.  Lustre (scratch) as like an object store, and
stores files separately from medatata.  This means that each file access
requires multiple different network requests, and making a lot of files
brings your research (and managing the cluster) to a halt.  What counts
as a lot?  Your default quota is 1e6 files.  1e4 for a project is not a
lot.  1e6 for a single project is.

You may have been directed here because you have a lot of files.  In
that case, welcome to the world of big data, even if your total size
isn't that much!  (it's not just size, but difficulty of handling using
normal tools)  Please read this and see what you can learn, and ask us
if you need help.

This page is mostly done, but specific examples could be expanded.

See also:

-  `Data storage on the Lustre file
   system <lustre>`,
   especially the bottom.
-  `Compute node local drives <localstorage>`

Contents
--------

The problem with small files
----------------------------

You know Lustre is high performance and fast.  But, there is a
relatively high overhead for accessing each file.  Below, you can see
some sample transfer rates, and you can see that total performance drops
drastically when files get small.  (These numbers were for the pre-2016
Lustre system, it's better now but the same principle applies.)  This
isn't just a problem when you are trying to read files, it's also a
problem when managing, moving, migrating, etc.

+-------------+----------------------------------------------+
| File size   | Net transfer rate, many files of this size   |
+=============+==============================================+
| 10GB        | 1100 MB/s                                    |
+-------------+----------------------------------------------+
| 100MB       | 990 MB/s                                     |
+-------------+----------------------------------------------+
| 1MB         | 90MB/s                                       |
+-------------+----------------------------------------------+
| 10KB        | .9MB/s                                       |
+-------------+----------------------------------------------+
| 512B        | .04 MB/s                                     |
+-------------+----------------------------------------------+

Why do people make millions of small files?
-------------------------------------------

We understand there reasons people make lots of files: it's convenient. 
Here are some of the common problems (and alternative solutions) people
may be trying to solve with lots of files.

-  Flat files are universal format. If you have everything in its own
   file, then any other program can look at any data individually.  It's
   convenient.  This is a fast way to get started and use things.
-  Compatibility with other programs.  Same as above.
-  Ability to use standard unix shell tools.  Maybe your whole
   preprocessing pipeline is putting each piece of data in its own file
   and running different standard programs on it.  It's the Unix way,
   after all.
   Using filesystem as your index.  Let's say you have a program that
   reads/writes data which is selected by different keys.  It needs to
   locate the data for each key separately.  It's convenient to put all
   of these in their own files: this takes the role of a database index,
   and you simply open the file with the name of the key you need.  But
   the filesystem is *not* a good index.

   -  Once you get too many files, a database is the right tool for the
      job.  There are databases which operate as single files, so it's
      actually very easy.

-  Concurrency: you use filesystem as the concurrency layer.  You submit
   a bunch of jobs, each job writes data to its own file.  Thus, you
   don't have to worry about problems with appending to the same
   file/database synchronization/locking/etc.  This is actually a very
   common reason.

   -  This is a big one.  The filesystem is the most reliable way to
      join the output of different jobs (for example an array job), and
      it's hard to find a better strategy.  It's reasonable to keep
      doing this, and combine job outputs in a second stage to reduce
      the number of files

-  Safety/security: the filesystem isolates different files from each
   other, so if you modify one, there's less chance of corrupting any
   other ones.  This goes right along with the reason above.
-  You only access a few files at a time in your day to day work, so you
   never realize there's a problem.  However, when we try to manage data
   (migrate, move, etc), then a problem comes up.
-  Realize that forking processes has similar overhead. Small reads are
   also non-ideal, but less bad(?).

Strategies
----------

-  Realize you will have to have to change you workflow. You can't do
   everything with grep, sort, wc, etc. anymore. Congratulations, you
   have big data.
-  Consider right strategy for your program: a serious program should
   provide options for this.

   -  For example, I've seen some machine learning frameworks which
      provide an option to compress all the input data into a single
      file that is optimized for reading.  This is precisely designed
      for this type of case.  You *could* read all the files
      individually, but it'll be slower.  So in this case, one should
      first read the documentation and see there's a solution.  One
      would take all the original files and make the processed input
      files.  Then, take the original training data, package it together
      in one compressed archive for long-term storage.  If you need to
      look at individual input files, you can always decompress one by
      one.

-  Split - combine - analyze

   -  Continue like you have been doing: each (array?) job makes
      different output files.   Then, after running, combine the outputs
      into one file/database.  Clean up/archive the intermediate files. 
      Use this combined DB/file to analyze the data in the long term. 
      This is perhaps the easiest way to adapt your workflow.

-  HDF5: especially for numerical data, this is a good format for
   combining your results.  It is like a filesystem within a file, you
   can still name your data based on different keys for individual
   access.
-  Unpack to local disk, pack to scratch when done.

   -  Main article: :doc:`Compute node local
      drives <localstorage>`,
   -  This strategy can be combined with many of the other strategies
      below
   -  This strategy is especially good when your data is
      write-once-read-many.  You package all of your original data into
      one convenient archive, and unpack it to the local disk when you
      need it.  You delete it when you are done.

-  Use a proper database suitable for your domain (sqlite): Storing lots
   of small data where anything can be quickly findable and you can do
   computation efficiently is exactly what databases do.  It can be
   difficult to have a general purpose database work for you, but there
   are a wide variety of special-purposes databases these days.  Could
   one of them be suitable for storing the results of your computation
   for analysis?

   -  Note that if you are really doing high-performance random IO,
      putting a database on scratch is not a good idea, and you need to
      think more.
   -  Consider combining this with local disk: You can copy your
      pre-created database file to local disk and do all the random
      access you need.  Delete when done.  You can do
      modification/changes directly on scratch if you want.

-  key-value stores: A string key stores arbitrary data.

   -  This is a more general database, basically.  It stores arbitrary
      data for a certain key.

-  Read all data to memory.

   -  A strategy for using many files.  Combine all data into one file,
      read them all into memory, then do the random access in memory.

-  Compress them down when done.

   -  It's pretty obvious: when you are done with files, compress all of
      them into one.  You have the archive and can always unpack when
      needed.  You should especially at least do this when you are done
      with a project: if everyone did this, the biggest problems could
      be solved.

-  Make sure you have proper backups for large files, mutating files
   introduces risks!

   -  If you do go using these strategies, make sure you don't
      accidentally lose something you need.  Have backups (even if it's
      on scratch: backup your database files)

-  If you do have to keep many small flies, check the link above for
   lustre performance tuning.

   -  `Data storage on the Lustre file
      system <lustre>`

-  If you have other programs that can only operate on separate files

   -  This is a tough situation, investigate what you can do combining
      the strategies above.  At least you can pack up when done, and
      possibly copying to local disk while you are accessing is a good
      idea.

-  MPI-I/O: if you are writing your own MPI programs, this can
   parallelize output

Specific example: HDF5 for numerical data, or some database
-----------------------------------------------------------

HDF5 is essentially a database for numerical data.  You open a HDF5 file
and access different data by path - the path is like a filename.  There
are libraries for accessing this data from all relevant programming
languages.

If you have some other data that is structured, there are other
databases that will work.  For example, sqlite is a single-file,
serverless database for relational data, and there are other similar
things for time serieses or graphs.

Specific example: Unpacking to local disk
-----------------------------------------

You can see examples at `compute node local
drives <localstorage>`

Specific example: Key-value stores
----------------------------------

Let's say you have written all your own code and want an alternative to
files.  Instead, use a key-value database.  You open one file, and store
your file contents under different keys.  When you need the data out,
you request it by that key again.  The keys take the place of
filenames.  Anytime you would open files, you just access from these
key-value stores.  You also have ways of dumping and restoring the data
if you need to analyze it from different programs.

Performance tuning for small files
----------------------------------

See here: `Data storage on the Lustre file
system <lustre>`

