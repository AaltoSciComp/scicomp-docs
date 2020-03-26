================
Cluster overview
================

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

Different types of nodes:

*  144 compute nodes `HP SL390s
   G7 <https://h10010.www1.hp.com/wwpc/us/en/sm/WF06a/15351-15351-3896136-3896139-4236125-4198401.html>`__,
   each equipped with 2x `Intel Xeon
   X5650 <https://ark.intel.com/products/47922/Intel-Xeon-Processor-X5650-%2812M-Cache-2_66-GHz-6_40-GTs-Intel-QPI%29>`__
   2.67GHz (Westmere six-core each). 118 compute nodes wsm[1-112,137-144],
   have 48 GB of DDR3-1066 memory, others wsm[113-136] have
   96GB, each node has 4xQDR Infiniband port,  wsm[1-112,137-144]
   have about 830 GB of local disk space (2 striped 7.2k SATA drives),
   while wsm[113-136] about 380GB on single drive. 16 nodes have by two
   additional SATA drives.

* 3 compute nodes ``gpu[20-22]`` are Dell PowerEdge C4130 for gpu computing. CPUs are 2x6 core Xeon E5 2620 v3 2.50GHz and memory configuration is 128GB DDR4-2133. There are 4x2 GPU K80 cards per node.

* 2 fat nodes HP DL580 G7 4U, 4x Xeon, 6x SATA drives, 1TB of DDR3-1066 memory each and 4xQDR Infiniband port.

* 48 compute nodes ``ivb[1-48]`` are HP SL230s G8 with 2x Xeon E5 2680 v2 10-core CPUs. First 24 nodes have 256 GB of DDR3-1667 memory and the other 24 are equipped with 64 GB.

* 67 compute nodes Dell PowerEdge C4130 servers with 2x Xeon E5 2680 v3 2.5GHz 12-core CPUs. 51 nodes ``pe[1-48,65-67]`` have 128 GB of DDR4-2133 memory while 15 nodes ``pe[49-64]`` have 256GB.

* 9 compute nodes ``pe[83-91]`` Dell PowerEdge C4130 with 2x Xeon X5 E5-2680 v4 2.4 GHz 14-core CPUs.

* 5 compute nodes ``gpu[23-27]`` for gpu computing.  CPUs are 2x12core Xeon
  E5-2680 v3 @ 2.50GHz and memory configuration 256GB DDR4-2400.
  There are 4x Tesla P100 16GB cards per node.

* 2 Nvidia DGX-1 compute nodes for gpu computing.  CPUs are 2x20 core
  Xeon E5-2698 v4 @ 2.2GHz and memory configuration 512GB DDR4-2133.
  There are 8x Tesla V100 16GB cards per node.  These nodes have a
  special operating system, unlike the rest of the cluster, and thus
  these nodes require special considerations.  See :doc:`the DGX page <usage/dgx>`.

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
on the CPU arch. The nodes within those islands connected with ratio 2:1,
thus for each 2
downlinks there is 1 uplink to spine switches. The islands are
``wsm[1-144]`` 1728 cores, ``ivb[1-45]`` 540 cores, ``pe[1-91]`` 2192 cores
(keep in mind that ``pe[83-91]`` have 28 cores per node). Uplinks from
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

