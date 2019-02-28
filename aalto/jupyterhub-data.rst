=========================
Accessing JupyterHub data
=========================

Unlike many JupyterHub deployments, your data is *yours* and have many
different ways to access it.  Most importantly, the data is a normal
Aalto network drive, and thus it can be accessed remotely, from your
own computers.

On Paniikki and Aalto computers
-------------------------------

TODO: eventually, on Paniikki, and the Aalto servers kosh, lyta,
brute, and force, the JupyterHub data will be available
automatically.

..
  on Paniikki and the Aalto servers kosh, lyta, brute, and force,
  you can simply access all Jupyter data at the path ``/m/jhnas/``.  In
  a terminal, run ``/m/jhnas/u/makedir.sh`` and you will automatically
  get a link from your home directory ``~/jupyter`` to your user data.

Remote access via network drive
-------------------------------

Basic info
~~~~~~~~~~

.. note::

   These instructions are still being tested and updated, because
   people have many different computers and we don't fully control the
   data storage ourselves.  Please check back for updates.

You can do a SMB mount, which makes the data available as a network
drive.  You will have the same copy of the data as on the hub -
actually, same data, so edits immediately take effect on both places,
just like your home directory.  *You must be on an Aalto network,
which for students practically means you must be connected to the*
**Aalto VPN** or use an Aalto computer.  The "aalto" wifi network does *not*
work unless you have an *Aalto* computer.

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
   <https://it.aalto.fi/instructions/deployment-network-drive-windows>`__
   is the same instructions, but for Aalto home directories.  Anything
   there should apply here, too.


.. _jupyter-gpu-paniikki:

Using GPUs
----------

One problem with our JupyterHub so far is that we don't have GPUs
available.  But, because our data is available to other computers, you
can use the :doc:`paniikki` GPUs (quite good ones) to get all the
power you need.  To do this, you just need to make the data available
on these classroom computers, and then start Jupyter or whatever you
need.

First, log in to a Paniikki computer and open the file browser.
Depending on your desktop, you can use "Places --> Connect to server",
or "Connect to Server from the file browser.

.. figure:: /images/jupyterdata_01_connect_menu.png
	    :scale: 75%
	    :align: center
	    :alt: Connect to Server

Then, enter the server address ``smb://jhnas.org.aalto.fi``

.. figure:: /images/jupyterdata_02_servername.png
	    :scale: 75%
	    :align: center
	    :alt: Server URL

Go to the directory with your username.  At this point, you can set a
bookmark that saves this for the future.

Now you have to start Jupyter there.  To do that, start a terminal in
the Jupyter directory.  You can do this by right clicking and
selecting "Open in Terminal":

.. figure:: /images/jupyterdata_03_startterminal.png
	    :scale: 75%
	    :align: center
	    :alt: Right click, and select Open in Terminal

Now that you have the terminal and the data, you can do whatever you
want with it.  Presumably, you will start Jupyter here - but first you
want to make the right software available.  If you course tells you
how to do that using an Anaconda environment, go ahead and do it.
(Please don't go installing large amounts of software like anaconda in
the Jupyter data directories - they are for notebooks and small-medium
data.)

Using the built-in anaconda, you can load the Python modules with
``module load anaconda3`` and start Jupyter with ``jupyter notebook``:

.. figure:: /images/jupyterdata_04_startjupyter.png
	    :scale: 75%
	    :align: center
	    :alt: Start jupyter with the anaconda3 module.




