=============
Remote Access
=============

This page describes remote access solutions. Most of them are provided
by Aalto, but there are also instruction for accessing your workstations
here. See Aalto Inside for more details.

Linux shell servers
~~~~~~~~~~~~~~~~~~~

-  CS department servers:

   -  ``magi``: Department staff server (no heavy computing,
      access to workstations and has file systems mounted, use kinit
      command first if project directories are not visible)

-  `Aalto servers <https://inside.aalto.fi/display/ITServices/Linux+shell+servers>`__

   -  ``kosh.aalto.fi``, ``lyta.aalto.fi``: Aalto, for general login use
      (no heavy compting)
   -  ``brute.aalto.fi``, ``force.aalto.fi``: Aalto, for "light computing"
      (expect them to be overloaded and not that useful). If you are
      trying to use these for research, you really want to be using
      Triton instead.
   -  ``taltta.aalto.fi``: Staff server (access to workstations and has
      filesystems mounted, but you need to kinit to access them.) that
      is kind of outdated and different.

-  Your **home** directory is shared on all Aalto shell servers, and
   that means .ssh/authorized\_keys as well.
-  You can use any of these to mount things remotely via sshfs. This is
   easy on Linux, harder but possible on other OSs. You are on your own
   here. magi is recommended since kerberos is not needed.

   -  The CS filesystems **project** and **archive** and Triton
      filesystems **scratch** and **work** are mounted on
      ``magi`` (and ``taltta.aalto.fi``) (see
      `storage <aaltostorage>`__).

.. _aalto_vpn:

VPN / web proxy
~~~~~~~~~~~~~~~

To access certain things, you need to be able to connect to the Aalto
networks via VPN. This is easy and automatically set up on Aalto
computers.

For the main Aalto instructions,
`see it.aalto.fi and search for "VPN"
<https://it.aalto.fi/searchpage?search_api_fulltext=vpn>`__.  This
section has some quick reference info.

-  Generic: OpenConnect/Cisco AnyConnect protocols. ``vpn.aalto.fi``
-  Aalto Linux: Status bar → Network → VPN Connections → Aalto TLS
   VPN.
-  Aalto mac: Dock → Launchpad → Cisco AnyConnect Secure Mobility
   Client
-  Aalto windows: Start → Search → AnyConnect
-  Personal Linux laptops: Use OpenConnect. Configuration on Ubuntu:
   Networks → Add Connection → Cisco AnyConnect compatible VPN. →
   ``vpn.aalto.fi``. Then connect and use Aalto username/password. Or from
   command line: ``openconnect https://vpn.aalto.fi``
-  Personal mac: `use Cisco AnyConnect VPN
   Client <https://download.aalto.fi/staff/>`__
-  personal windows: `use Cisco AnyConnect VPN
   Client <https://download.aalto.fi/staff/>`__

For more lightweight things (though not actually easier!), you can use
ssh proxy. You are on your own
here. ``ssh -D 8080 $username@kosh.aalto.fi``. Configure your web
browser or other applications to use a SOCKS5 proxy on ``localhost:8080``
for connections. Remember to revert when done or else you can't connect
to anything. The extension FoxyProxy Standard may be useful here.

Remote mounting of network filesystems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Aalto networks (or VPN), you can mount many of the filesystems via
SMB. To use this well, you want to get the VPN set up first like
mentioned above. (You can also access these filesystems via ssh through
the shell servers):

- In all cases, username=aalto username, domain=AALTO,
  password=Aalto password.
- ``smb://home.org.aalto.fi/`` for your home directory
- ``smb://tw-cs.org.aalto.fi/project/$name/`` for project
  directories (``$name``\ =project name)
- ``smb://tw-cs.org.aalto.fi/archive/$name/`` for archive
  directories (``$name``\ =project name)
- For scratch directories, see :doc:`Triton storage
  <../triton/tut/storage>`.
- ``smb://work.org.aalto.fi`` for "Aalto work" directories (different
  than Triton ``work``).

Depending on your OS, you may need to use either your username
directly or ``AALTO\username``

On Ubuntu: Files → Left sidebar → Connect to server → use the URLs above.
For other Linuxes, you can probably figure it out.

On mac laptops: Finder → Go menu item → Connect to server → use the URLs
above.

On windows laptops:  To do the mounting, Windows Explorer → Computer → Map network drive →
select a free letter.  ``smb://`` becomes ``\\`` (without the ``smb:``), and ``/`` becomes
``\``.  For example, a full URL could be
``\\tw-cs.org.aalto.fi\project\mygroup``.  You can also just enter
it into the file manager bar.

Remember that you must connect to the Aalto VPN first!

Accessing you Linux workstation / Triton remotely
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Remote access to desktop workstations is available via the university
   staff shell servers ``taltta.aalto.fi`` or department-specific
   servers ``magi.cs.aalto.fi`` (CS), ``amor.org.aalto.fi`` (NBE).
-  You need to be the **PrimaryUser** of the desktop in order to ssh to
   it.
-  Remote access to Triton is available from any Aalto shell server:
   ``taltta``, ``kosh.aalto.fi``, etc.
-  SSHing directly to computers using openssh ProxyCommand:

   -  Put this in your .ssh/config file under the proper Host line:
      ``ProxyCommand ssh taltta.aalto.fi -W %h:%p``
   -  For this to be most useful, you probably want to set up ssh keys,
      otherwise you will have to enter your password twice.
   -  This starts getting beyond the basic level of ssh use, so you may
      want to read up on ssh keys, ProxyCommand, ControlMaster. It can
      make your experience much better.

Remote Windows desktop
~~~~~~~~~~~~~~~~~~~~~~

Aalto has a windows remote desktop available. As usual, you must be on
the Aalto VPN or Aalto networks.

-  Server name ``rds01.org.aalto.fi`` (or ``rds02``).
-  login with Aalto credentials, username: ``AALTO\$username``
-  From Linux: the GUI program ``remmina`` lets you connect.  Follow
   the instructions to add a server connection.
   Username is Aalto username and password is Aalto password.  If you are on the
   Aalto network, you can turn the quality settings quite high (True
   color, Quality=best).  Security=negotiate.
-  From Linux: the command line program ``rdesktop`` can connect:
   ``rdesktop -u 'AALTO\$username' -g 1360x760 rds01.org.aalto.fi``

As usual (on Linux), you can also access this directly through SSH
forwarding instead of the VPN (``remmina`` seems to be able to do this
automatically):

-  ``ssh -L 3389:rds01.org.aalto.fi:3389 kosh.aalto.fi``
-  ``rdesktop -u 'AALTO\$username' -g 1360x760 localhost``


