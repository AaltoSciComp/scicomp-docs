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

	# Go to wherever you want to have your Brew and run this
	mkdir Homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz -C Homebrew --strip 1

	# This is a MUST!!!
	echo "export PATH=\$PATH:$(pwd)/Homebrew/bin" >> ~/.bash_profile

	# Reload the profile
	source ~/.bash_profile

	# Check if brew is correctly installed.
	which brew    # /Users/username/Homebrew/bin/brew

------------------------------------------------------------------------

Backup Service
--------------
We provide a full clone-backup service for Aalto-installation Macs. Aalto-installation means the OS is installed from Aalto repository. We use Apple `Time Machine <https://en.wikipedia.org/wiki/Time_Machine_(macOS)>`_. Backup is **wireless, encrypted, automatic, periodic and can be used even outside the campus** using :ref:`Aalto VPN <aalto_vpn>`. It is "clone" because we can restore your environment in its entirity. You can think of it as a snapshot backup(though it isn't). We provide twice the space of your SSD; your Mac has 250GB of space, you get 500GB of backup space. If you would like to enroll in the program please pay a visit to our office, T-talo A243.

Encryption
~~~~~~~~~~
We provide two options for encryption:

1. You set your own encryption key and only you know it. **The key is neither recoverable nor resettable**. You lose it, you lose your backup.
2. We set it on behalf of you and only we know it.

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
This happens because either 1). you changed your Aalto password or 2). the server is down. Debug in the following manner,

.. code-block:: bash
	
	# Is the server alive?
	ping timemachine.cs.aalto.fi

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

This is an unfortunate situation with an unknown reason. We take a snapshot of your backup. Please contact guru@cs.aalto.fi. 


-----------------------------------------------------

Common problems
---------------

Insane CPU rampage by ``UserEventAgent``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is a mysterious bug which Apple hasn't solved yet. We can reinstall your system for you.


















