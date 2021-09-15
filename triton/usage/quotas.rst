======
Quotas
======

Triton has quotas which limit both the space usage and number of files.
The quota for your home directory is 10GB, for $WRKDIR by default is
200GB, and project directories depending on request. These quotas exist
to avoid usage exploding without anyone noticing. If you ever need more
space, just ask. We'll either give you more or find a solution for you.

There is a inode (number of files) quota of 1 million, because scratch
is not that great for too many small files. If you have too many small
files, see `the page on small files <smallfiles>`.


Lustre (scratch/work) quotas
----------------------------

.. note::

   Before 2021-09-15, quotas worked differently, and used group IDs
   rather than project IDs.  There were many things that could go
   wrong and give you "disk quota exceeded" even though there appeared
   to be enough space.

There are both quotas for users and projects
(/m/$dept/scratch/$project).  We use project IDs for this (see
detailed link in See Also).  The ``quota`` command shows the correct
quotas (by project) by default, so there is nothing special you should
need to do.

If you want to look deeper, check the project ID with ``lfs
project -d {path}` and quotas with ``lfs quota -hp {project_id}``.

Unlike the previous situation, there should be much fewer possible
quota problems.



See also
--------

* Linux project IDs: https://lwn.net/Articles/671627/ (note that this
  is not exactly the same implementation as Lustre but the general
  idea).

