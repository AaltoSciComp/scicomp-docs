Cluster technical overview
==========================

Shared resource
---------------

Triton is a joint installation by a number of Aalto School of Science
faculties within `Science-IT
project <http://sci.aalto.fi/en/research/muu_tutkimustoiminta/science-it/>`__,
which was founded in 2009 to facilitate the HPC Infrastructure in all of
School of Science. It is now available to all Aalto researchers.

Hardware
--------

.. include:: ref/hardware.rst


All Triton computing nodes are identical in respect to software and
access to common file system. Each node has its own unique host name and
ip-address.

Networking
----------

Internally the cluster uses Infiniband for MPI and Lustre and NFS.

The internal networks are unaccessible from outside. Only the login node
``triton.aalto.fi`` has an extra Ethernet connection to outside.

High performance InfiniBand has fat-tree configuration in general. Triton
has several InfiniBand segments (often called islands) distinguished based
on the CPU arch. Uplinks from
those islands are mainly used for Lustre communication.
Running MPI jobs possible on the entire island or its segment, but not
across the cluster.

Storgage
--------

All compute nodes and front-end are connected to a `ClusterStor storage
system <usage/lustre>`:
large disk arrays with the Lustre filesystem on top of it cross-mounted
under ``/scratch`` directory. The system provides about 5PB of disk
space available to end-user.

System software
---------------

The cluster is running open source software infrastructure: Red Hat Enterprise Linux
with SLURM as the scheduler and batch system.

