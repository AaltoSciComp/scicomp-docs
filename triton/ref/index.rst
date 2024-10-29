:gitstamp_ignore:

Triton quick reference
======================

In this page, you have all important reference information


..
   toctree::
   :maxdepth: 0

   modules.rst
   storage.rst
   partitions.rst
   slurm.rst
   slurm_status.rst
   toolchains.rst
   hardware.rst
   hardware_dist.rst

Quick reference guide for the Triton cluster at Aalto University, but
also useful for many other Slurm clusters.  See also this `printable
Triton cheatsheet
<https://aaltoscicomp.github.io/cheatsheets/triton-cheatsheet.pdf>`__,
as well as `other cheatsheets <https://aaltoscicomp.github.io/cheatsheets/>`__.



.. _ref-connecting:

Connecting
----------

See also: :doc:`../tut/connecting`.

.. include:: connecting.rst



.. _ref-modules:

Modules
-------

See also: :doc:`../tut/modules`.

.. include:: modules.rst



.. _ref-common-software:

Common software
---------------

See also: :doc:`../tut/applications`.

.. include:: software.rst



.. _ref-storage:

Storage
-------

See also: :doc:`../tut/storage`

.. include:: storage.rst



.. _ref-remote-data:

Remote data access
------------------

See also: :doc:`../tut/remotedata`.

.. include:: remotedata.rst



.. _ref-quotas:

Quotas
------

See also: :doc:`../usage/quotas`.

.. include:: quotas.rst



.. _ref-job-submission:

Job submission
--------------
See also: :doc:`../tut/serial`, :doc:`../tut/array`,
:doc:`../tut/parallel`, :doc:`../tut/serial`.

.. include:: slurm.rst

.. include:: slurm_status.rst



.. _ref-slurm-examples:

Slurm examples
--------------

See also: :doc:`../tut/serial`, :doc:`../tut/array`.

.. include:: slurm_examples.rst



.. _ref-partitions:

Slurm Partitions
----------------

.. include:: partitions.rst



.. _ref-toolchains:

..
  Toolchains
  ==========
  .. include:: toolchains.rst

.. _hardware-list:

.. _ref-hardware:

Hardware
--------

See also: :doc:`../overview`.

.. include:: hardware.rst

..
  .. include:: hardware_dist.rst



.. _ref-gpus:

GPUs
----

See also: :doc:`../tut/gpu`.

.. include:: gpu.rst



.. _ref-conda:


Conda Environments (Mamba)
--------------------------

See also: :doc:`../apps/python-conda`.  Note that ``mamba`` is a
drop-in replacement for ``conda``.

.. include:: conda.rst



.. _ref-command-line:

Command line
------------

See also: :doc:`/scicomp/shell`.

.. include:: commandline.rst
