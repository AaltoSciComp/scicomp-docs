=============
Aalto Windows
=============

This page describes the Aalto centrally-managed Mac computers, where
login is via Aalto accounts.  If you have a standalone laptop, some of
this may be relevant, but for the most part you will access your data
and Aalto resources via :doc:`remoteaccess`.

Basics
------

- accounts
- login/upgrades

Initial setup
~~~~~~~~~~~~~

Full disk encryption
~~~~~~~~~~~~~~~~~~~~

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

Aalto software
~~~~~~~~~~~~~~

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
