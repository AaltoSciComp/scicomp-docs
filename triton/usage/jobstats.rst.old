
Monitoring jobs' usage of the filesytem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our Lustre servers collect so-called jobstats - statistics of Lustre
usage by individual Slurm jobs. These statistics can be viewed by a
tool called jobstats. To view jobstats for your job, you need to do
the following::

  module load jobstats
  jobstats <jobid> <jobid> ...

Do note that the job statistics are collected from our storage servers
every 10 seconds, but are only transferred to our statistics servers every
5 minutes. Thus smalls that take less than 5 minutes might show incorrect
statistics.

Please do not run too many queries too often, as we're still testing
the capabilities of our statistics server.

Output of the tool looks something like this::

                                                         54324759
  Bytes read (% of load on a single server)                    -1
  Bytes read (Max)                                              0
  Bytes read (Total)                                            0
  Bytes written (% of load on a single server)  88.88888888888889
  Bytes written (Max)                                  6442450944
  Bytes written (Total)                                7247757312
  Files closed (Total)                                         -1
  Files opened (Total)                                         -1
  Getattr calls made (Total)                                    0
  Read calls made (Total)                                       0
  Setattr calls made (Total)                                    0
  Write calls made (Total)                                   1728

Currently the jobstats history only goes back in time for couple of weeks.
This is due to the amount of statistics that our monitoring records.

How to read jobstats
####################

Any values with ``-1`` mean that either that there wasn't any calls that
were captured or that the percentage ratio could not be calculated.

The different lines of the jobstats output are explained below:

- ``Bytes read (% of load on a single server)``: This statistic shows the
  percentage of bytes that were read from a single Lustre server. If this is
  close to a 100%, see the recommendations below for avoiding hotspots.
- ``Bytes read (Max)``: This statistic shows the number of bytes that
  were read from the a single Lustre server. This number divided by the total
  bytes read will produce the percentage of load on a single Lustre server.
- ``Bytes read (Total)``: This statistic shows the total number of bytes
  read by your job. If the number is very high, see the recommendations
  below for minimizing your data loading.
- ``Bytes written (% of load on a single server)``: Similar to bytes read
  percentage, but for bytes written.
- ``Bytes written (Max)``: Similar to bytes read maximum, but for bytes
  written.
- ``Bytes written (Total)``: Similar to bytes read total, but for bytes
  written.
- ``Files closed (Total)``: Total number of files closed during the job
  runtime. If this is very high, please check below for recommendations on
  minimizing the number of files opened/closed.
- ``Files opened (Total)``: Similar to files closed, but for files opened.
- ``Getattr calls made (Total)``: Total number of getattr metadata calls
  made during job runtime. If this is high, please check below for
  recommendations on minimizing the number of metadata calls.
- ``Read calls made (Total)``: Number of file read calls made during the
  job runtime (byte reads). If high, please check below for
  recommendations on how to minimize the number of read calls.
- ``Setattr calls made (Total)``: Similar to getattr calls, but this
  time for setattr calls.
- ``Write calls made (Total):``: Similar to read calls, but this time for
  write calls.

My job shows a close to 100% bytes read/write load on a single server
#####################################################################

If your job has a high percentage of load on a single server **AND**
the number of bytes read/written is high, you might cause **hotspots** on our
storage servers.

As each file is by default striped on a single server, having a large
file read/written by your code will put the load of reading/writing the file
on a single server.

Of course, if you read/write a large amount of data you should first
look at the instructions on that as well so that the overall amount of
data that's being read/written will be minimized.

Besides that, you might want to split your data to smaller pieces
(1-10GB, depending on the size of the original data) or to look at our
:doc:`Lustre-page </triton/usage/lustre>` for instructions on how to
stripe your large files to multiple storage servers. Both methods
distribute the load of reading/writing to multiple servers.

However, you should **not** stripe small files as that will increase the
filesystem load. If uncertain, please ask us admins about helping you
with a good IO workflow.

My job shows a very high read/write byte count
##############################################

If your job reads/writes a lot of data the main question you should ask is
whether all of the reads/writes are necessary. For example, you might ask:

1. Do I use/need all of the output my code is generating?
2. If I create checkpoints of the state of my program execution,
   is the rate of checkpointing set to be too fast?
3. Could I do my IO against the
   :doc:`local disks or ramdisk </triton/usage/localstorage>` and only
   once copy my input there/copy my output out?
4. Is some of this load created by temporary files?
   Could I divert some of this load to local disks?
5. Am I constantly reading the same files again and again? Could I place the
   files to the local disks/ramdisk during the job runtime?
6. Do I use efficient binary output format or do I save data in an ASCII
   textfile which requires more space?
7. Am I loading a dataset, but only using a piece of it during job execution?
   Could I split the dataset to pieces before I run my code?

If you have any questions or do not know the answer how your program does
its IO, do not hesitate to ask us admins on helping you figure out a good
IO workflow.

My job opens/closes a high number of files
##########################################

If your job opens/closes a large number of files it might either:

1. Constantly open/close the input/output files. This is usually unnecessary
   and can be fixed by keeping the input/output files open during job runtime
   or by reducing the rate of output.
2. Open a large number of input/output files. If you're working with a large
   number of small files you might want to look at our pages on how to use
   :doc:`local disks </triton/usage/localstorage>` and ``tar`` to group up
   your small files into larger collections.
3. Your code might open a lot of libraries stored in the Lustre filesystem.
   Are you compiling code? Use
   :doc:`local disks or ramdisk </triton/usage/localstorage>` for that. Are
   you loading an anaconda environment or R libraries from the Lustre
   filesystem? Move them to your ``$HOME``-directory.

My job makes a high number of getattr/setattr-calls
###################################################

Do you run something like ``find ...``, ``ls -l ...`` or ``chmod ...`` in
your scripts? Commands like these do getattr/setattr queries towards our
metadata servers. Are these commands necessary for running your program?

These kinds of calls also happen if you untar/unzip files to the Lustre
filesystem.

My job makes a high number of read/write-calls
##############################################

A high number of read/write calls can happen for multitude of reasons.

Firstly, as
**number of bytes read/written = size of a block read/written* number of read/write calls**,
a large number of read/write calls might indicate that your code is read/write
its input/output in small chunks. Using ASCII data, small files or read/print
statements in your code can easily create a huge number of read/write calls.
For example, a print statement is typically written into a buffer of size 4-64KB.
Thus writing a 10MB file using print statements can create up to thousands of
write calls. Using binary formats will usually solve this problem as they
usually write in much larger chunks (typically 1-4MB).

Secondly, a large number of read/write operations might occur if you're doing
lots of random read operations. This happens easily when using database formats
such as lmdb or sqlite. Lustre is not the best format for random reads or
for database interaction. You might want to look into using
:doc:`local disks or ramdisk </triton/usage/localstorage>` for storing your
database during the job runtime.

If you're reading/writing a lot of data or opening/closing a lot files, this
number is usually very high as well. Thus it is usually good to look at the
instructions for those cases as well.
