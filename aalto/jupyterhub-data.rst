=========================
Accessing JupyterHub data
=========================

Unlike many JupyterHub deployments, your data is *yours* and have many
different ways to access it.  Most importantly, the data is a normal
Aalto network drive, and thus it can be accessed remotely, from your
own computers.

Remote access
-------------

Basic info
~~~~~~~~~~
You can do a SMB mount.  

* Linux: use "Connect to Server" from the file browser.  The path is
  ``smb://jhnas.org.aalto.fi/$username``.

* Mac: same path as Linux above, "Connect to Server"

* Windows: ``\\jhnas.org.aalto.fi\$username``.

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

Go to the directory with your username.

Now you have to start Jupyter there.  To do that, start a terminal in
the Jupyter directory.  You can do this by right clicking and
selecting "Open in Terminal":

.. figure:: /images/jupyterdata_03_startterminal.png
	    :scale: 75%
	    :align: center
	    :alt: Right click, and select Open in Terminal

Now that you have the terminal, you can load the Python modules with
``module load anaconda3`` and start jupyter with ``jupyter notebook``.
Note that the Paniikki anaconda3 modules may not have all the same
software as the JupyterHub does.  In this case, you will need to make
your own anaconda environment, or use one set up for your course
already:

.. figure:: /images/jupyterdata_04_startjupyter.png
	    :scale: 75%
	    :align: center
	    :alt: Start jupyter with the anaconda3 module.




