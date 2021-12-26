Tutorials required cluster setup
================================

This page describes the HPC/Slurm setup needed to follow along in our
HPC (=cluster computing) kickstart courses.  The target audience of
this page is HPC system staff who would like to direct their users to
follow along with this course.  If you don't match something here,
consider if that is desired and if so, it should be added to your
cheatsheet.

This course is designed to be a gentle introduction to scaling up from
a local workflow to running on a cluster.  It is not especially
focused on the *high performance* part but instead the basics and
running existing things on a cluster.

Our philosophy for clusters is:

* Make everything possible automatic (for example, partition
  selection, Slurm options).  A user should only need to specify what
  is needed - at least for tutorials.

* Standardization is good: don't break existing standard Slum things,
  it should be possible to learn "base Slurm" and use it across
  clusters (even if it's not the optimal form)

.. highlight:: bash


General
-------

These tutorials will be quite useful for clusters with:

- Slurm as the batch system
- You can get a shell (likely via ssh)
- ``git`` installed without needing to load a module
- Python 2 or 3 (any version) installed as ``python`` without needing
  to load a module


Quick reference
---------------

If you run your own cluster, create a quick reference such as
:doc:`/triton/ref/index` so that others following tutorials such as
ours can quickly translate to your own cluster's specifics.


Connecting
----------

Connection should be possible via ssh.  You probably want a
cheatsheet and installation help before our course.


Slurm
-----

Slurm is the workload manager.

Partitions are automatically detected in most cases.  We have a
``job_submit.lua`` script that detects these cases, so that for most
practical purposes ``--partition`` never needs to be specified:

* Partition based on run time
* GPU partition based on ``--gres``

There are no other mandatory Slurm arguments such as account or
cluster selection.

``seff`` is installed.

We use this ``slurm_tool`` wrapper, but we don't require it (but it
might be useful for your users): https://github.com/jabl/slurm_tool


Applications
------------

You use ``Lmod`` and it works across all nodes without further setup.

``git``: Git is used to clone our examples (and should have network
access).

``python``: We assume Python is available (version 2 or 3 - we make
our examples run on both) without loading a module.  Many of our basic
examples use this to run simple programs to demonstrate various
cluster features without getting deeper into software.


Data storage
------------

We expect this to be different for everyone.  We suggest that most
clusters have at least a home directory (small) and a work space
(large and high-performance).

``$HOME`` is the home directory, small and backed up, not for big
research, mounted on all nodes.

``$WRKDIR`` is an environment variable that points to a per-user
scratch directory (large, not backed up, suitable for fast I/O across
all nodes)
