Theano
------

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

:supportlevel:
:pagelastupdated:
:maintainer:

If you're using the theano library, you need to tell theano to store
compiled code on the local disk on the compute node. Create a file
``~/.theanorc`` with the contents

::

    [global]
    base_compiledir=/tmp/%(user)s/theano

Also make sure that in your batch job script you create this directory
before you launch theano. E.g.

::

    mkdir -p /tmp/${USER}/theano

The problem is that by default the ``base_compiledir`` is in your home
directory (``~/.theano/``), and then if you first happen to run a job on a
newer processor, a later job that happens to run on an older processor
will crash with an "Illegal instruction" error.
