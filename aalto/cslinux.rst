========
CS Linux
========

CS Linux is an OS used for computers not supported by Aalto Linux. It is maintained by the CS Department IT.

Currently only desktop setups are available.

Basics
------

- Home directory. CS Linux computers have a local home directory (instead of the Aalto home directory found in Aalto Linux).
- Aalto credentials are used for login. Anyone in the CS department is able to login to any computer on-site. However, ssh login has to be enabled manually by CS-IT.
- The systems are centrally managed with the help of Puppet.
- CS Linux computers operate on a dedicated VLAN (different from Aalto Linux). The ethernet port used must be configured before using the computer. The login will not work if the computer is connected to the wrong VLAN. Changes to port configurations can be requested from CS-IT.
- The default user interface for CS Linux is GNOME. If your computer doesn't have a graphical interface, but you would like it to have one, please contact CS-IT and it can be configured remotely with the help of Puppet.

**Requesting a new CS Linux computer**

- Contact CS-IT.
- Let CS-IT know who will be using the computer and if they need SSH and sudo access. The primary user should receive sudo rights by default.
- Let CS-IT know if you would like a graphical interface to be installed.

**When you are done with a computer**

- Let CS-IT know that you are leaving and bring the computer to the CS-IT office or arrange for someone from the IT team to pick it up. CS-IT will perform a secure erase on the hard drive(s). This is important as most of the data is stored locally.

Software
--------
Ubuntu packages
~~~~~~~~~~~~~~~
If you are the primary user, you should have sudo rights. You can then use ``apt`` to install packages.

The module system
~~~~~~~~~~~~~~~~~
The command ``module`` provides a way to manage various installed
versions of software across many computers. This is the way that we
install custom software and newer versions of software, if it is not
available in Ubuntu. Note that these are shell functions that alter
environment variables, so this needs to be repeated in each new shell
(or automated in login).

-  See the :doc:`Triton module docs <../triton/tut/modules>` docs for
   details.
-  ``module load triton-modules`` will make most Triton software
   available on Aalto workstations (otherwise, most is hidden).
-  ``module avail`` to list all available package.
-  ``module spider $name`` to search for a particular name.
-  ``module load $name`` to load a module. This adjusts environment
   variables to bring various directories into ``PATH``, ``LD_LIBRARY_PATH``,
   etc.
-  We will try to keep important modules synced across the workstations
   and Triton, but let us know.

Useful modules:

-  ``anaconda`` and ``anaconda2`` will always be kept up to date with the latest Python
   Anaconda distribution, and we'll try to keep this in sync across
   Aalto Linux and Triton.
- ``triton-modules``: a metamodule that makes other Triton software available.

Admin rights
------------
The primary user of a computer should receive sudo rights by default. 

Sudo rights can also be requested for other users (requires approval from primary user). These requests can be sent to CS-IT.