==============
Grid computing
==============

*Note: not directly related to local usage covered by other pages. The
whole thing is about an upper level cluster resources usage through Grid
interface.*

Grid computing on FGCI
~~~~~~~~~~~~~~~~~~~~~~

The `FGCI (Finnish Grid and Cloud Infrastructure) <https://www.csc.fi/-/fgci>`__ is a joint pool of
resources that consists of a number of Linux clusters placed all around
Finland. Triton is one of them. Being a part of FGCI Triton provides its
CPU and disk space resources to grid users. Having your local account on
Triton means having access to Triton local resources only, in order to
use whole grid one has to get grid certificate.

To get started with grid computing on FGCI, please consult the
https://research.csc.fi/fgci-user-guide pages.

Getting help
~~~~~~~~~~~~

CSC provides grid users with support at grid-support(at)csc.fi.

Triton local usage vs. Grid computing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In other words should I start thinking of running on Grid? Why yes.

FGCI is homogeneous with respect to hardware/software. You may expect
same Xeon CPUs connected through Infiniband and same Linux environment
on all the clusters. Thus tested binaries on Triton will work on any
other FGCI resource.

Grid is the best suited for from 30 minutes up to 24 hours long jobs. It
is for production runs mainly, you do the development/testing locally on
Triton and then send your jobs to the grid.

One can run MPI or large number of serial jobs, no CPU units/limits, no
overloaded queues, there always be a free slot for your job on one of
FGCI clusters.

Grid job management can be done from anywhere you prefer, including
Triton, CSC servers or your department workstation. Grid certificate is
independent on your Aalto / Triton / CSC account and valid for one year.
