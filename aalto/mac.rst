=========
Aalto Mac
=========

This page describes the Aalto centrally-managed Mac computers, where
login is via Aalto accounts.  If you have a standalone laptop, some of
this may be relevant, but for the most part you will access your data
and Aalto resources via :doc:`remoteaccess`.

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

.. code-block:: bash

	# Go to wherever you want to have your Brew and run this
	curl -L https://github.com/Homebrew/brew/tarball/master  | tar xz

	mv Homebrew-brew-43c658a Homebrew

	# This is a MUST!!!
	echo 'export PATH="path-where-you-installed/Homebrew/bin:$PATH"' >> ~/.bash_profile

	# Reload the profile
	source ~/.bash_profile

	# Check if brew is correctly installed.
	which brew    # /Users/username/Homebrew/bin/brew



Common problems
---------------
