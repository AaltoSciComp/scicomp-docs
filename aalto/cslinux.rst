========
CS Linux
========

CS Linux is an OS used for computers not supported by Aalto Linux. 
It is maintained by the CS Department IT and is currently only available for researchers in the CS department.
The OS is intended for setups which the :doc:`Aalto Linux <linux>` setup is not flexible enough (mainly custom built setups) for.
The Aalto Linux setup is recommended if it serves your needs.

Currently only desktop setups are available.

Basics
------

-  Home directory. CS Linux computers have a local home directory (instead of the Aalto home directory found in Aalto Linux).
-  Aalto credentials are used for login. Anyone in the CS department is able to login to any computer on-site. However, ssh login has to be enabled manually by CS-IT.
-  The systems are centrally managed with the help of Puppet.
-  CS Linux computers operate on a dedicated VLAN (different from Aalto Linux). The ethernet port used must be configured before using the computer. The login will not work if the computer is connected to the wrong VLAN. Changes to port configurations can be requested from CS-IT.
-  The default user interface for CS Linux is GNOME. If your computer doesn't have a graphical interface, but you would like it to have one, please contact CS-IT and it can be configured remotely with the help of Puppet.

**Requesting a new CS Linux computer**

- `Contact CS-IT <https://wiki.aalto.fi/display/CSdept/IT>`__.
-  Let CS-IT know who will be using the computer and if they need SSH and sudo access. The primary user receives sudo rights by default.
-  Let CS-IT know if you would like a graphical interface to be installed.

**When you are done with a computer**

-  Let CS-IT know that you are leaving and bring the computer to the CS-IT office or arrange for someone from the IT team to pick it up. CS-IT will perform a secure erase on the hard drive(s). This is important as most of the data is stored locally.

Software
--------

Ubuntu packages
~~~~~~~~~~~~~~~

If you are the primary user, you have sudo rights. You can then use ``apt`` to install packages.

The module system
~~~~~~~~~~~~~~~~~

The command ``module`` provides a way to manage various installed
versions of software across many computers. See :ref:`here<module-system>` for a detailed description on the module system.

Data
----

Everything is stored locally, meaning that there are no backups.
Anyone with physical access to the computer is able to access the data stored on it.

You are able to mount the Aalto home directory as well as the teamwork directories (requires sudo rights). This can be done by "connect to server"
in the file browser for easy graphical access, or via the command line
to choose the mounting location.

Samba share addresses:

-  ``smb://home.org.aalto.fi/$USER``
-  ``smb://tw-cs.org.aalto.fi/project/$projectname/`` - replace *$projectname*.
-  ``smb://tw-cs.org.aalto.fi/archive/$archivename/`` - replace *$archivename*.

.. rubric:: Mounting an smb share using terminal
.. code-block:: bash
  
  sudo mount -t cifs -o username=$USER,cruid=$USER,uid=$(id -u $USER),gid=$(id -g $USER),sec=krb5 //tw-cs.org.aalto.fi/project/ ~/mnt

.. note::

   Notice that Samba mounts don't include information about file and directory permissions.
   This means that all files and directories will have the default permissions. This also applies to anything that you create.

User accounts
-------------

User accounts on CS Linux are managed via the central configuration management. If you want to grant access to the system for other users, please contact CS-IT. Creating local users manually may cause unexpected issues.

Admin rights
------------

The primary user of the computer receives sudo rights by default.

Sudo rights can also be requested for other users (requires approval from primary user). These requests can be sent to CS-IT.

CS Linux computers are centrally managed, meaning that the centralized management should not be broken.
Our support is mostly limited to reinstalling the computer, in cases where sudo rights have been used to change settings.
