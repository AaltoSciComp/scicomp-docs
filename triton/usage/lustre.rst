Storage: Lustre (scratch)
=========================

.. seealso::

   :doc:`the storage tutorial <../tut/storage>`.

Lustre is scalable high performance file system created for HPC. It
allows MPI-IO but mainly it provides large storage capacity and high
sequential throughput for cluster applications. Currently the total
capacity is 5PB.

As you might expect, making a storage system capable of storing
petabytes accessed at tens of gigabytes per second across hundreds of
nodes and users simultaneously is quite a challenge.  It works well,
but there are tradeoffs.  The basic idea in Lustre is to spread data
in large files over multiple storage servers.  Small files can be a
problem, but Triton's scratch is adjusted to mitigate it somewhat.
With large (larger than 1GB) files Lustre will significantly boost the
performance.

.. important::

   More often than not, when "Triton is down", it's Lustre (scratch)
   being down.  If you do normal-sized work this usually isn't a
   problem.  If you do big data-intensive work, please pay attention
   to storage and ask for help early.


Working with small files
------------------------

As Lustre is meant for large files, the performance with small (smaller
than 10MB) files will not be optimal. If possible, try to avoid working
with large numbers of small files.  Large numbers is greater than
thousands or tens of thousands.

.. seealso::

   * :doc:`smallfiles`, a dedicated page on handling small files.
   * :doc:`localstorage`, a page explaining how to use compute node
     local drives to unpack archives with many small files to get
     better performance.


Large datasets which consist mostly of small (<1MB) files can be slow to
process because of network overhead associated with individual files. If
it is your case, please consult `Compute node local
drives <localstorage>` page, see the ``tar`` example
over there or find some other way to compact your files together into
one.


Working with large files
------------------------

By default Lustre on Triton is configured so that as files grow
larger, they get `striped
<https://en.wikipedia.org/wiki/Data_striping>`__ (split) over more
storage servers.  This way, small files only require one server to
serve the file (reducing latency), while large files can be streamed
over multiple disks.

This page previously had instructions for how to adjust the striping
of files yourself, but it is now automatic.


Lustre: common recommendations
------------------------------

Triton's Lustre is much better than it was 10 years ago, but it's
still worth thinking about the following things:

Minimize use of ``ls -l`` and ``ls --color`` when possible.

Several excellent recommendations are at
https://www.nas.nasa.gov/hecc/support/kb/Lustre-Best-Practices_226.html
, they are fully applicable to our case.

Be aware, that being a high performance filesystem Lustre still has its
own bottlenecks, and even non-proper a usage by a single user can get
whole system in stuck. See the recommendations at the link above how to
avoid those potential situations. Common Lustre troublemakers are
``ls -lR``, creating many small files, ``rm -rf``, small random i/o,
heavy bulk i/o.

For advanced user, these slides (from 2012) can be interesting:
https://www.eofs.eu/wp-content/uploads/2024/02/06_daniel_kobras_s_c_lustre_fs_bottleneck.pdf
