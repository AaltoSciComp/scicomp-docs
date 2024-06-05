About these tutorials
=====================

.. include:: /triton/ref/videos.rst

.. admonition:: Abstract

   * These tutorials are written for Aalto University's Triton
     cluster, but we have tried to make them useful far any
     Slurm-based cluster.

   * They are focused on basic usage, not the *high-performance* part:
     there is plenty else about that.

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

.. toctree::
   :hidden:

   required-cluster-setup

These tutorials use Aalto's cluster as an example, but they are
designed to be useful to a wide audience: most clusters operate on the
same principles with local configuration or practices needed.  This
course/these tutorials, along with a :doc:`quick reference similar to
ours <../ref/index>`, will be a great start to your career.  (People
running a cluster can check out our :doc:`hint sheet
<required-cluster-setup>` to see what differences you may need to explain.)

We will point out things that may be different, but you need to
consult your own reference to see how to do it:

- The way you connect to the cluster, including remote access methods.
- Exact names of batch partitions.
- The ``slurm`` utility probably isn't installed, ``seff`` may not be there.
- Module names for software.
- You probably don't have our Singularity container stuff installed.
- Parallel and GPU stuff is probably different.



What's next?
------------

Introduce yourself to :doc:`the cluster resources at Aalto <intro>`.
