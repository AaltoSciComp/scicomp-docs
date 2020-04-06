=========================
Storage: Lustre (scratch)
=========================

.. seealso::

   :doc:`the storage tutorial <../tut/storage>`.

Lustre is scalable high performance file system created for HPC. It
allows MPI-IO but mainly it provides large storage capacity and high
sequential throughput for cluster applications. Currently the total
capacity is 2PB. The basic idea in Lustre is to spread data in each file
over multiple storage servers. With large (larger than 1GB) files Lustre
will significantly boost the performance.

Working with small files
~~~~~~~~~~~~~~~~~~~~~~~~

As Lustre is meant for large files, the performance with small (smaller
than 10MB) files will not be optimal. If possible, try to avoid working
with multiple small files.

**Note: Triton has a default stripe of 1 already, so it is by default
optimized for small files (but it's still not that great).  If you use
large files, see below.**

If small files are needed (i.e. source codes) you can tell Lustre not to
spread data over all the nodes. This will help in performance.

To see the striping for any given file or directory you can use
following command to check status

::

    lfs getstripe -d /scratch/path/to/dir

You can not change the striping of an existing file, but you can change
the striping of new files created in a directory, then copy the file to
a new name in that directory.

::

    lfs setstripe -c 1 /scratch/path/to/dir
    cp somefile /scratch/path/to/dir/newfile

Working with lots of small files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Large datasets which consist mostly of small (<1MB) files can be slow to
process because of network overhead associated with individual files. If
it is your case, please consult `Compute node local
drives <localstorage>` page, see the ``tar`` example
over there or find some other way to compact your files together into
one.

Working with large files
~~~~~~~~~~~~~~~~~~~~~~~~

By default Lustre on Triton is configured to stripe a single file over a
single OST. This provides the best performance for small files, serial
programs, parallel programs where only one process is doing I/O, and
parallel programs using a file-per-process file I/O pattern. However,
when working with large files (>> 10 GB), particularly if they are
accessed in parallel from multiple processes in a parallel application,
it can be advantageous to stripe over several OST's.  In this case the
easiest way is to create a directory for the large file(s), and set the
striping parameters for any files subsequently created in that
directory:

::

    cd $WRKDIR
    mkdir large_file
    lfs setstripe -c 4 large_file

The above creates a directory ``large_file`` and specifies that files
created inside that directory will be striped over 4 OST's. For really
really large files (hundreds of GB's) accessed in parallel from very
large MPI runs, set the stripe count to "-1" which tells the system to
stripe over all the available OST's.

To reset back to the default settings, run

::

    lfs setstripe -d path/to/directory

Lustre: common recommendations
------------------------------

- Minimize use of ``ls -l`` and ``ls --color`` when possible

Several excellent recommendations are at

-  https://www.nas.nasa.gov/hecc/support/kb/Lustre-Best-Practices_226.html
-  http://www.nics.tennessee.edu/computing-resources/file-systems/io-lustre-tips.

They are fully applicable to our case.

Be aware, that being a high performance filesystem Lustre still has its
own bottlenecks, and even non-proper a usage by a single user can get
whole system in stuck. See the recommendations at the link above how to
avoid those potential situations. Common Lustre troublemakers are
``ls -lR``, creating many small files, ``rm -rf``, small random i/o,
heavy bulk i/o.

For advanced user, these slides can be interesting:
https://www.eofs.eu/fileadmin/lad2012/06_Daniel_Kobras_S_C_Lustre_FS_Bottleneck.pdf
