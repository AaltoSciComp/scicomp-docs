Storage
=======

.. seealso::

   These pages have details that go beyond this page:

   * :doc:`../tut/storage` - basic prerequisite tutorial
   * :doc:`../tut/remotedata` - basic prerequisite tutorial
   * :doc:`../usage/lustre`
   * :doc:`../usage/localstorage`
   * :doc:`../usage/quotas`
   * :doc:`../usage/smallfiles`


This pages gives an overview of more advanced storage topics.  You
should read the :doc:`storage <../tut/storage>` and :doc:`remote data
<../tut/storage>` tutorials first.



Checklist
---------

Do any of these apply to you?  If so, consider your situation and ask
us for help!

If you have been sent this checklist because your jobs may be having
a lot of IO, don't worry.  It's not *necessarily* a problem but please
go through this checklist and let us know what applies to you so we
can give some recommendations.

- Many small files being accessed in jobs (hundred or more).

- Files with extremely random access, in particular databases or
  database-like things (hdf5).

- Files being read over and over again.  Alternatives: copy to local
  disks, or read once and store in memory.

- Number of files growing, for example all your runs have separate
  input files, output files, Slurm output files, and you have many runs.

- Constantly logging to certain files, writing to files from many
  parallel jobs at the same time.

- Reading from single files from many parallel jobs or threads at the
  same time.

- Is all your IO concentrated at one point, or spread out over the
  whole job?

( and if we've asked you specifically about your jobs, could you also
describe what kind of job it is, the type of disk read and write
happens, and in what kinds of pattern?  Many small files, a few large
ones, reading same files over and over, etc.  How's it spread out
across jobs? )

If you think your IO may have bad patterns or even you just want to
talk to make sure, let one of the Triton staff know or submit an issue
in the issue tracker.



Checking your jobs' IO usage
----------------------------

You can check the total disk read and write of your past jobs using::

  # All your recent jobs:
  sacct -o jobid%10,user%8,jobname%10,NodeList,MaxDiskRead,MaxDiskWrite -u $USER
  # A single jobid
  sacct -o jobid%10,user%8,jobname%10,NodeList,MaxDiskRead,MaxDiskWrite -j $jobid

These statistics are calculated on the whole node and thus include
IO caused by other jobs on the same server while your job is running.

More advanced tool are being tested and will be available once they
are finished.



Loading data for machine learning
---------------------------------

As we've said before, modern GPUs are super data-hungry when used for
machine learning.  If you try to open many files to feed it the data,
"you're going to have a bad time".  Luckily, different packages have
different solutions to the problem.

In general, at least try to combine all of your input data into some
sort of single file that can be read in sequence.

Try to do the least amount of work possible in the core training
loops: any CPU usage, print, logging, preprocessing, postprocessing,
etc. reduces the amount of time the GPU is working unless you
do it properly (Amdhal's law).

* Tensorflow: `data input pipelines <https://www.tensorflow.org/guide/data_performance>`__
* PyTorch: `data loaders <https://pytorch.org/tutorials/beginner/basics/data_tutorial.html>`__

(more coming later)
