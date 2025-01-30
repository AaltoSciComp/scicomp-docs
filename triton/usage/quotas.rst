======
Quotas
======

Triton has quotas which limit both the space usage and number of files.
The quota for your home directory (``$HOME``) is 20GB, for $WRKDIR by default is
200GB, and project directories depending on request (as of 2021). These quotas exist
to avoid usage exploding without anyone noticing. If you ever need more
space, just ask. We'll either give you more or find a solution for you.

There is a inode (number of files) quota of 1 million, because scratch
is not that great for too many small files. If you have too many small
files, see :doc:`the page on small files <smallfiles>`.

.. admonition:: Quick reference

   .. include:: ../ref/quotas.rst



Lustre (scratch/work) quotas
----------------------------

.. note::

   Before 2021-09-15, quotas worked differently, and used group IDs
   rather than project IDs.  There were many things that could go
   wrong and give you "disk quota exceeded" even though there appeared
   to be enough space.

There are both quotas for users and projects
(``/m/$dept/scratch/$project``).  We use project IDs for this (see
detailed link in See Also), and our convention is that project IDs are
the same as numeric group IDs.  The ``quota`` command shows the correct
quotas (by project) by default, so there is nothing special you should
need to do.

If you want to look deeper, check the project ID with ``lfs
project -d {path}`` and quotas with ``lfs quota -hp {project_id}``.

Unlike the previous situation, there should be much fewer possible
quota problems.



Home directory quotas
---------------------

Home directories have a quota, and unlike scratch, space for home is
much more limited.  We generally don't increase home directory quotas,
but we can help you move stuff to scratch for the cases that fill up
your home directories (e.g. installing Python or R packages which go
to home by default)



Project/archive ("Aalto Teamwork")
----------------------------------

The project/scratch directories use a completely different system from
scratch (though quotas work similarly), even if they are visible on
Triton.  Quotas for these are managed through your departments or IT
Services.



See also
--------

* Linux project IDs: https://lwn.net/Articles/671627/ (note that this
  is not exactly the same implementation as Lustre but the general
  idea).
