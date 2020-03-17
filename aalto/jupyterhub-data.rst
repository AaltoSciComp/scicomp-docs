=========================
Accessing JupyterHub data
=========================

Unlike many JupyterHub deployments, your data is *yours* and have many
different ways to access it.  Thus, we don't just have jupyter.cs, but
a whole constellation of ways to access and do *your work*, depending on what
suits you best for each part.

Your data (and as an instructor, your course's data) can be accessed
many ways:

* On jupyter.cs.
* Via network drive *on your own computer as local files*.
* On Aalto shell servers (such as kosh.aalto.fi).
* On other department/university workstations.

On Paniikki and Aalto computers
-------------------------------

On Paniikki, and the Aalto servers ``kosh.aalto.fi``,
``lyta.aalto.fi``, ``brute.aalto.fi``, and ``force.aalto.fi`` (and
possibly more), the JupyterHub is available automatically.  **You can,
for example, use the Paniikki GPUs.**

Data is available within the paths ``/m/jhnas/jupyter``.  The path on
Linux servers is also available on the hub, if you want to write
portable files.

.. csv-table::
   :delim: |
   :header-rows: 1

   Name                    | Path on hub     | Path on Linux servers
   personal notebooks      | ``/notebooks``  | ``/m/jhnas/jupyter/u/$nn/$username/``
   course data             | ``/coursedata`` | ``/m/jhnas/jupyter/course/$course_slug/data/``
   course instructor files | ``/course``     | ``/m/jhnas/jupyter/course/$course_slug/files/``
   shared data             | ``/m/jhnas/jupyter/shareddata/`` | ``/m/jhnas/jupyter/shareddata/``

.. csv-table::
   :delim: |
   :header-rows: 1

      Variable seen above | Meaning
      ``$username``       | Your Aalto username
      ``$nn``             | The two numbers you see in ``echo $HOME`` (the last two digits of your Aalto uid, ``id``)
      ``$course_slug``    | The short name of your course.

You can change directly to your notebook directory by using ``cd
/m/jhnas/jupyter/${HOME%/unix}``.

**You can link it to your home directory so that it's easily
available**.  In a terminal, run ``/m/jhnas/u/makedir.sh`` and you
will automatically get a link from ``~/jupyter`` in your home
directory to your user data.

**Permission denied?** Run ``kinit`` in the shell - this authenticates
yourself to the Aalto server and is required for secure access.  If
you log in with ssh keys, you may need to do this.

Remote access via network drive
-------------------------------

Basic info
~~~~~~~~~~

.. csv-table::
   :delim: |
   :header-rows: 1

   Name                    | Network drive path
   personal notebooks      | ``smb://jhnas.org.aalto.fi/$username/``
   course data             | ``smb://jhnas.org.aalto.fi/course/$course_slug/data/``
   course instructor files | ``smb://jhnas.org.aalto.fi/course/$course_slug/files/``
   shared data             | ``smb://jhnas.org.aalto.fi/shareddata/``

You can do a SMB mount, which makes the data available as a network
drive.  You will have the same copy of the data as on the hub -
actually, same data, so edits immediately take effect on both places,
just like your home directory.  *You must be on an Aalto network,
which for students practically means you must be connected to the*
**Aalto VPN** (see `vpn instructions
<https://it.aalto.fi/searchpage?search_api_fulltext=vpn>`__) or use an
Aalto computer.  The "aalto" wifi network does *not* work unless you
have an *Aalto* computer.

* Linux: use "Connect to Server" from the file browser.  The path is
  ``smb://jhnas.org.aalto.fi/$username``.  You may need to use
  ``AALTO\username`` as your username.  If there is separate "domain"
  option, use ``AALTO`` for domain and just your username for the username.

* Mac: same path as Linux above, "Connect to Server".  Use
  ``AALTO\your_username`` as the username.

* Windows: ``\\jhnas.org.aalto.fi\$username``, and use username
  ``AALTO\your_username``.  Windows sometimes caches the
  username/password for a long time, so if it does not work try
  rebooting.

You can also access course data and shared data by using
``jhnas.org.aalto.fi/course/`` or ``jhnas.org.aalto.fi/shareddata/``.

.. seealso::

   `Mounting network drives in Windows
   <https://www.aalto.fi/en/services/deployment-of-a-network-drive-in-windows>`__
   is the same instructions, but for Aalto home directories.  Anything
   there should apply here, too.


.. _jupyter-gpu-paniikki:

Using GPUs
----------

One problem with our JupyterHub so far is that we don't have GPUs
available.  But, because our data is available to other computers, you
can use the :doc:`paniikki` GPUs (quite good ones) to get all the
power you need.  To do this, you just need to access the Jupyter data
on these classroom computers.

**Terminal**: First, start a terminal.  You can navigate to your data
following the instructions above: ``cd
/m/jhnas/jupyter/${HOME%/unix}``.  From there, navigate to the right
directories and do what is needed.

**File browser**: Navigate to the path
``/m/jhnas/jupyter/u/$nn/$username``, where ``$nn`` is the two numbers
you see when you do ``echo $HOME`` in a terminal.  To open a terminal
from a location, right click and select "Open in Terminal".

Now that you have the terminal and the data, you can do whatever you
want with it.  Presumably, you will start Jupyter here - but first you
want to make the right software available.  If you course tells you
how to do that using an Anaconda environment, go ahead and do it.
(Please don't go installing large amounts of software like anaconda in
the Jupyter data directories - they are for notebooks and small-medium
data.)

Using the built-in anaconda, you can load the Python modules with
``module load anaconda`` and start Jupyter with ``jupyter notebook``:

.. figure:: /images/jupyterdata_04_startjupyter.png
	    :scale: 75%
	    :align: center
	    :alt: Start jupyter with the anaconda module.

	    Note that now, you need to ``module load anaconda``, not
	    anaconda\ **3** like the image shows.




