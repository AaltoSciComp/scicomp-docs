========
CS Linux
========

CS Linux is an OS used for computers not supported by the Aalto Linux. It is maintained by the CS Department IT.

Currently only desktop setups are available.

Basics
------

- Home directory. CS Linux computers have a local home directory (instead of the Aalto home directory found in Aalto Linux).
- Login is done with Aalto credentials. Anyone in the CS department is able to login to any computer locally. However, ssh login has to be enabled manually by CS-IT.
- The systems are centrally managed with the help of Puppet.
- CS Linux computers operate on a dedicated VLAN (different from Aalto Linux). The ethernet port used must be configured before using the computer. The login will not work if the computer is connected to the wrong VLAN. Changes to port configurations can be requested from CS-IT.
- The default user interface for CS Linux is GNOME. If your computer doesn't have a graphical interface, but you would like it to have one, please contact CS-IT and it can be configured remotely with the help of Puppet.

**Requesting a new CS Linux computer**

- Contact CS-IT.
- Let us know who will be using the computer and if they need SSH and sudo access.
- Let us know if you would like a graphical interface to be installed.

**When you are done with a computer**

- Let CS-IT know that you are leaving and bring the computer to the CS-IT office or arrange for someone from the IT team to pick it up. CS-IT will perform a secure erase on the hard drive(s). This is important as most of the data is stored locally.
