About these tutorials
=====================

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=etYG9YhsXKI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=5>`__

   Or see the `full playlist <https://www.youtube.com/playlist?list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc>`__.

Welcome to the Aalto Scientific Computing High-performance computing
(HPC) tutorials.  These tutorials will get you started with the Triton
cluster.

Despite the HPC in the name, most of these tutorials are not about the
*high-performance* part: instead, we get you started using and
submitting jobs to the cluster.  These days, many people use a cluster
for simple jobs: getting more stuff done at once, not a few very big
tasks.  Doing the big tasks are a more specialized topic, which this
will introduce you to and you will be able to use other software for
that.  Programming your own HPC software is out of our scope.



Not at Aalto?
-------------

These tutorials use Aalto's cluster as an example, but they are
designed to be as general as possible.  You can probably follow along
and learn useful topics here anyway, but you will have.  We recommend
you review the basics of your cluster's documentation first, then read
this.  You will have to translate somethings to your own specifics,
but hopefully our examples can inspire you to understand your own docs
better.

These tutorials will be quite useful if you have:

- A cluster using Slurm as the batch system
- You can get a shell on that server
- The ``git`` installed
- Python 2 or 3 installed as ``python``

Unfortunately, not all clusters are standardized (though probably they
should be slightly more than they are).  Things that may be different
(we'll try to point these out where relevant):

- The way you connect to the cluster, including remote access methods.
- Exact names of batch partitions.
- The ``slurm`` utility probably isn't installed, ``seff`` may not be there.
- Module names for software.
- You probably don't have our singularity stuff installed.
- Parallel and GPU stuff is probably different.



Runing another cluster?
-----------------------

If you run your own cluster, create a quick reference such as
:doc:`/triton/ref/index` so that others following tutorials such as
this can quickly translate to your own cluster's specifics.

Don't you think clusters should be more interoperable?  It's something
we are thinking about.


What's next?
------------

Introduce yourself to :doc:`the cluster resources at Aalto <intro>`.
