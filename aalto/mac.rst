=========
Aalto Mac
=========

This page describes the Aalto centrally-managed Mac computers, where
login is via Aalto accounts.  If you have a standalone laptop (one
which does not use your Aalto account), some of this may be relevant,
but for the most part you are on your own and you will access your
data and Aalto resources via :doc:`remoteaccess`.

More instructions: https://inside.aalto.fi/display/ITServices/Mac


Basics
------

In the Aalto installations, login is via Aalto account only.

- When you get a computer, ask to be made primary user (this should be
  default, but it's always good to confirm).  This will allow you to
  manage the computer and install software.

- The first time you login, you must be on an Aalto network (wired or
  ``aalto`` wifi) so that the laptop can communicate with Aalto
  servers and get your login information.  After this point, you don't
  need to be on the Aalto network anymore.

- Login is via your Aalto account.  The password stays synced when you
  connect from an Aalto netowrk.



Full disk encryption
--------------------

This must be enabled per-user, using FileVault.  **You should always
do this, there is no downside.**  On Aalto-managed
laptops, install "Enable FileVault disk encryption" (it's a custom
Aalto thing that does it for you).  To do this manually, "Settings →
Privacy → enable File Vault."



Data
----
You can mount Aalto filesystems by using SMB.  Go to Finder → File or
Go (depending on OS) → Connect
to Server → enter the ``smb://`` URL from the data storage pages.

You can find more information at For generic ways of accessing, see
:doc:`remoteaccess`.  For Aalto data storage locations see
:doc:`aaltostorage`, and for the big picture of where and how to store
data see :doc:`aaltodata`.

The program ``AaltoFileSync`` is pre-installed and can be used to
synchronize files.  But you basically have to set it up yourself.


Software
--------

.dmg files
~~~~~~~~~~
If you are the primary user, in the Software Center you can install
the program "Get temporary admin rights". This will allow you to become an
administrator for 30 minutes at a time. Then, you can install ``.dmg``
files yourself.  This is the recommended way of installing ``.dmg``
files.

Aalto software
~~~~~~~~~~~~~~
There is an application called "Managed software center"
pre-installed (or "Managed software update" in older versions).  You
can use this to install a wide variety of ready-packaged software.  (`ITS
instructions <https://inside.aalto.fi/display/ITServices/Mac>`__).

Homebrew
~~~~~~~~
`Homebrew <https://brew.sh>`_ is a handy package manager on Macs. On
Aalto Macs, you have to install Brew in your home dir.  Once you
install brew, you can easily instnall whatever you may need.

First install Xcode through Managed Software Centre (either search Xcode, or navigate through Categories -> Productivity -> Xcode).

.. code-block:: bash

	# Go to wherever you want to have your Brew and run this
	mkdir Homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz -C Homebrew --strip 1

	# This is a MUST!!!
	echo "export PATH=\$PATH:$(pwd)/Homebrew/bin" >> ~/.zprofile

	# Reload the profile
	source ~/.zprofile

	# Check if brew is correctly installed.
	which brew    # /Users/username/Homebrew/bin/brew

Older versions of MacOS (pre Mojave) use bash as the default shell, therefore you need to setup the environment differently:

.. code-block:: bash

	echo "export PATH=\$PATH:$(pwd)/Homebrew/bin" >> ~/.bash_profile

	# Reload the profile
	source ~/.bash_profile


Admin rights
------------

The "Get temporary admin rights" program described under .dmg file
installation above lets you get *some* admin rights - but not full
sudo and all.

You don't need full admin rights to install brew.

If you need sudo rights, you need a workstation admin (wa) account.
Contact your department admin for details.



CS Mac backup service
---------------------
The CS department provides a full clone-backup service for
Aalto-installation mac computers.  Aalto-installation means the OS is
installed from Aalto repository.

We use Apple `Time Machine
<https://en.wikipedia.org/wiki/Time_Machine_(macOS)>`_. Backup is
**wireless, encrypted, automatic, periodic and can be used even
outside the campus** using the :ref:`Aalto VPN <aalto_vpn>`. It is "clone"
because we can restore your environment in its entirety. You can think
of it as a snapshot backup(though it isn't). We provide twice the
space of your SSD; your Mac has 250GB of space, you get 500GB of
backup space. If you would like to enroll in the program please pay a
visit to our office, T-talo A243.

Encryption
~~~~~~~~~~
We provide two options for encryption:

1. You set your own encryption key and only you know it. **The key is
   neither recoverable nor resettable**. You lose it, you lose your
   backup.

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

   * In case your Mac is broken, you can restore completely on a new
     Mac. For this, you must visit us.

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
	# Pease contact CS-IT.


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

This is an unfortunate situation with an unknown reason. We take a
snapshot of your backup. Please contact CS-IT.


Common problems
---------------

Insane CPU rampage by ``UserEventAgent``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is a mysterious bug which Apple hasn't solved yet. We can reinstall your system for you.
