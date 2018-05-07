=========
Aalto Mac
=========

This page describes the Aalto centrally-managed Mac computers, where
login is via Aalto accounts.  If you have a standalone laptop, some of
this may be relevant, but for the most part you will access your data
and Aalto resources via :doc:`remoteaccess`.

.. note::

   This page is still under development.


Basics
------

In the Aalto installations, login is via Aalto account only.

- accounts
- login/upgrades

Initial setup
~~~~~~~~~~~~~

Full disk encryption
~~~~~~~~~~~~~~~~~~~~

This must be enabled per-user, using FileVault.  On Aalto-managed
laptops, install "Enable FileVault disk encryption" (it's a custom
Aalto thing that does it for you)

Remote usage
~~~~~~~~~~~~


Laptop-specific
---------------

Data
----
This section details built-in ways of accessing data storage
locations.  For generic ways of accessing, see :doc:`remoteaccess`.
For Aalto data storage locations, see :doc:`aaltostorage` and :doc:`../data/outline`.

(project, archive, scratch, home mainly)



Software
--------

If you are the primary user, in the Software Center you can install
"Get temporary admin rights". This will allow you to become an
administrator for 30 minutes at a time. Then, you can install .dmg
files yourself.

Aalto software
~~~~~~~~~~~~~~

There is a tool called "Managed software center" (or "Managed software
update" in older versions) (`ITS instructions
<https://inside.aalto.fi/display/ITServices/Mac>`__).

Installing other software
~~~~~~~~~~~~~~~~~~~~~~~~~

Homebrew
########
`Homebrew <https://brew.sh>`_ is a handy package manager on Macs. On Aalto Macs, you have to install Brew in your home dir.

First install Xcode through Managed Software Centre (either search Xcode, or navigate through Categories -> Productivity -> Xcode).

.. code-block:: bash

	# Go to wherever you want to have your Brew (generally home directory) and run this
	mkdir Homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz -C Homebrew --strip 1

	# The next steps depends on the shell you're using, the default shell being zsh.
	# You can check which shell you're using with `echo $SHELL`.
	# For bash, replace .zshrc with .bashrc or .bash_profile or the like.
	echo "export PATH=\$PATH:$(pwd)/Homebrew/bin" >> ~/.zshrc


	# Reload the profile. Again, depends on your shell.
	source ~/.zshrc

	# Check if brew is correctly installed.
	which brew    # /Users/username/Homebrew/bin/brew

------------------------------------------------------------------------

Backup Service(Beta)
--------------------
We are providing a full clone-backup service for "Aalto Mac" users who work at the CS department. We use Time Machine. It is encrypted and automatic; hourly backup on charge mode in the background. It is "clone" because we can restore your environment in its entirity. You can think of it as a snapshot backup(though it isn't). It works under Aalto network i.e., it will work anywhere as long as you use Aalto vpn. We provide twice the space of your SSD; your Mac has 250GB of space, you get 500GB of backup space. If you would like to enroll in the program please pay a visit to our office, A243.

Restore
~~~~~~~
With Time Machine you have two options for restore.

1. Partial

	* You can restore file-by-file. Watch the video,

.. raw:: html

	<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
		<iframe src="https://www.youtube.com/embed/6bcf54aRBPk" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
	</div>



2. Complete restore

	* In case your Mac is broken, you can restore completely on a new Mac. For this, you must visit us.


Trouble-shooting
~~~~~~~~~~~~~~~~

Can't find the backup destination
#################################
This happens because either 1). you changed your password or the 2). server is down. Debug in the following manner,

.. code-block:: bash
	
	# Is the server alive?
	ping cs-239.org.aalto.fi

	# If alive, probably it's your keychain. 
	# Watch the video below.

	# If dead, something's wrong with the server.
	# Pease contact guru@cs.aalto.fi


.. raw:: html

	<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
		<iframe src="https://www.youtube.com/embed/jexhHxZ75w4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
	</div>


Corrupted backup
################

.. figure:: /images/time-machine-error.png
   :scale: 50%
   :align: center
   :alt: alternate text
   :figclass: align-center

This is an unfortunate situation with an unknown reason. If your backup data is unnecessary, start a new backup. If you want to fix the backup, please visit us. We can try to fix it but we cannot guarantee it.


-----------------------------------------------------

Common problems
---------------


















