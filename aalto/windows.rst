=============
Aalto Windows
=============

This page describes the Aalto centrally-managed Windows computers,
where login is via Aalto accounts.  If you have a standalone laptop
(login not using Aalto account), some of this may be relevant, but for
the most part you will access your data and Aalto resources via
:doc:`remoteaccess`.

More instructions: https://inside.aalto.fi/display/ITServices/Windows



Basics
------

In the Aalto installations, login is via Aalto account only.

- You must be on the Aalto network the first time you connect.

Full disk encryption
~~~~~~~~~~~~~~~~~~~~

Aalto Windows laptops come with this by default, tied to your login
password.  To verify encryption, find "BitLocker" from the start menu
and check that it is on.

Note, that on standalone installations, you can do encryption by
searching "TrueCrypt" in programs - it is already included.


Data
----

This section details built-in ways of accessing data storage
locations.  For generic ways of accessing remotely, see
:doc:`remoteaccess`.  For Aalto data storage locations, see
:doc:`/data/aalto-details` and :doc:`/data/principles`.

Your home directory is automatically synced to some degree.

You can store local data at
``C:\LocalUserData\User-data\<yourusername>``.  Note that this is not
backed up or supported.  For data you want to exist in a few years,
use a network drive.  It can be worth making a working copy here,
since it can be faster.



Software
--------

Aalto software
~~~~~~~~~~~~~~

There is a `Windows software self-service portal
<https://www.aalto.fi/en/services/self-service-portal-for-requesting-windows-software-installations>`__
which can be used to install some software automatically.

Installing other software
~~~~~~~~~~~~~~~~~~~~~~~~~

To install most other software, you need administrator rights. These are granted through an application called BeyondTrust.
If BeyondTrust is not already installed, open "Start Software Installation - Aalto IT" from the Start Menu. Install BeyondTrust from the Installation status tab. The computer might require a restart after this.

To enable admin rights go back to "Start Software Installation - Aalto IT" and from the application tab install "Enable Admin Rights for Primary User". Read and accept the agreement and restart the computer after the installation has been completed.

Common problems
---------------
