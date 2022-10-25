==========================
Cluster technical overview
==========================

Shared resource
===============

Triton is a joint installation by a number of Aalto School of Science
faculties within `Science-IT
project <http://sci.aalto.fi/en/research/muu_tutkimustoiminta/science-it/>`__,
which was founded in 2009 to facilitate the HPC Infrastructure in all of
School of Science. It is now available to all Aalto researchers.

As of 2016, Triton is part of `FGCI - Finnish Grid and Cloud
Infrastructure <https://www.csc.fi/-/fgci>`__ (predecessor of `Finnish
Grid
Infrastructure <http://www.csc.fi/tutkimus/Laskentapalvelut/gridymparisto/fgi>`__).
Through the national grid and cloud infrastructure, Triton also becomes
part of the European Grid Infrastructure.

Hardware
========

.. include:: ref/hardware.rst


All Triton computing nodes are identical in respect to software and
access to common file system. Each node has its own unique host name and
ip-address.

Networking
==========

The cluster has two internal networks: Infiniband for MPI and Lustre
filesystem and Gigabit Ethernet for everything else like NFS ``/home``
directories and ssh.

The internal networks are unaccessible from outside. Only the login node
``triton.aalto.fi`` has an extra Ethernet connection to outside.

High performance InfiniBand has fat-tree configuration in general. Triton
has several InfiniBand segments (often called islands) distinguished based
on the CPU arch. The nodes within those islands connected with different
ratio like 2:1, 4:1 or 8:1, (i.e. in 4:1 case for each 4
downlinks there is 1 uplink to spine switches. The islands are
``ivb[1-45]`` 540 cores, ``pe[3-91]`` 2152 cores
(keep in mind that ``pe[83-91]`` have 28 cores per node), four ``c[xxx-xxx]`` segments
with 600 cores each, skl[1-48] and csl[1-48] with 1920 cores each [CHECKME]. Uplinks from
those islands are mainly used for Lustre communication.
Running MPI jobs possible on the entire island or its segment, but not
across the cluster.

Disk arrays
===========

All compute nodes and front-end are connected to `DDN SFA12k storage
system <usage/lustre>`:
large disk arrays with the Lustre filesystem on top of it cross-mounted
under ``/scratch`` directory. The system provides about 1.8PB of disk
space available to end-user.

Software
========

The cluster is running open source software infrastructure: CentOS 7,
with SLURM as the scheduler and batch system.

