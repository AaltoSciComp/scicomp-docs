=============
Remote Access
=============

This page describes remote access solutions. Most of them are provided
by Aalto, but there are also instruction for accessing your workstations
here. See Aalto Inside for more details.

.. highlight:: console

Linux shell servers
~~~~~~~~~~~~~~~~~~~

-  Department servers have **project**, **archive**, **scratch**, etc
   mounted, so are good to use for research purposes.

   -  CS: ``magi.cs.aalto.fi``: Department staff server (no heavy computing,
      access to workstations and has file systems mounted, use the ``kinit``
      command first if project directories are not accessible)

   - NBE: ``amor.org.aalto.fi``, same as above.

   - Math: ``elliptic.aalto.fi``, ``illposed.aalto.fi``,
     same as above (but no project, archive and scratch directories)

-  `Aalto servers <https://www.aalto.fi/en/services/linux-shell-servers-at-aalto>`__

   -  ``kosh.aalto.fi``, ``lyta.aalto.fi``: Aalto, for general login use
      (no heavy compting)
   -  ``brute.aalto.fi``, ``force.aalto.fi``: Aalto, for "light computing"
      (expect them to be overloaded and not that useful). If you are
      trying to use these for research, you really want to be using
      Triton instead.
   -  ``viila.aalto.fi``: Staff server (access to workstations and has
      filesystems mounted, but you need to kinit to access them.) that
      is kind of outdated and different.

-  Your **home** directory is shared on all Aalto shell servers, and
   that means ``.ssh/authorized_keys`` as well.

-  You can use any of these to mount things remotely via sshfs. This is
   easy on Linux, harder but possible on other OSs. You are on your own
   here.  You still need ``kinit`` at the same time.

   -  The CS filesystems **project** and **archive** and Triton
      filesystems **scratch** and **work** are mounted on
      ``magi`` (and ``viila.aalto.fi``) (see
      :doc:`storage </data/aalto-details>`).

For any of these, if you can't access something, run ``kinit``!

.. _aalto_vpn:

VPN
~~~

To access certain things, you need to be able to connect to the Aalto
networks.  VPN is one way of doing that. This is easy and
automatically set up on Aalto computers.

`Main Aalto instructions
<https://www.aalto.fi/en/services/establishing-a-remote-connection-vpn-to-an-aalto-network>`__.
Below is some quick reference info.

-  Generic: OpenConnect/Cisco AnyConnect protocols. ``vpn.aalto.fi``, ``vpn1.aalto.fi`` or ``vpn2.aalto.fi``
-  Aalto Linux: Status bar → Network → VPN Connections → Aalto TLS
   VPN.
-  Aalto mac: Dock → Launchpad → Cisco AnyConnect Secure Mobility
   Client
-  Aalto windows: Start → Search → AnyConnect
-  Personal Linux laptops: Use OpenConnect. Configuration on Ubuntu:
   Networks → Add Connection → Cisco AnyConnect compatible VPN. →
   Set Gateway to ``vpn.aalto.fi`` and User Agent to ``AnyConnect''.
   Then connect and use Aalto username/password. Or from the command
   line: ``openconnect https://vpn.aalto.fi --useragent=AnyConnect``.  This requires a new enough OpenConnect, at least Ubuntu 23.10 has it.
-  Personal mac: `use Cisco AnyConnect VPN
   Client <https://download.aalto.fi/staff/>`__
-  personal windows: `use Cisco AnyConnect VPN
   Client <https://download.aalto.fi/staff/>`__

SSH SOCKS proxy
~~~~~~~~~~~~~~~

If you need to access the Aalto networks, but can't send all of your
traffic through the Aalto network, you can use SSH + the SSH built in
SOCKS proxy.  **Only use this on computers that only you control,
since the proxy itself doesn't have authentication.**

Connect to an Aalto server using SSH with the ``-D`` option::

  $ ssh -D 8080 USERNAME@kosh.aalto.fi

Configure your web browser or other applications to use a SOCKS5 proxy
on ``localhost:8080`` for connections. Remember to revert when done or
else you can't connect to anything once the SSH tunnel stops ("proxy
refusing connections").

The web browser extension FoxyProxy Standard (available on many web
browsers despite the name) may be useful here, because you can
direct *only the domains you want through the proxy*.

- Go to the FoxyProxy options
- Configure a proxy with some title ("Aalto 8080" for example), Proxy
  type SOCKS5, Proxy IP 127.0.0.1 (localhost), port 8080 (or whatever
  you used in the ssh command, no username or password.
- Save and edit patterns
- Add a new pattern ("New White") and use a pattern you would like,
  for example ``*.aalto.fi``, and make sure it's enabled.
- Save

Now, in this browser, when you try to access anything at
``*.aalto.fi``, it will go through the SOCKS proxy and appear to come
from the computer to which you connected.  By digging around in
options or using the extension button, you can direct everything
through a proxy and so on.

This can actually also be used for SSH on linux at least (install the
program ``netcat-openbsd``)::

  ssh -o 'ProxyCommand=nc -X 5 -x 127.0.0.1:8123 %h %p' HOSTNAME



Remote mounting of network filesystems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::

   :doc:`/data/remote-access`


Accessing your Linux workstation / Triton remotely
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Remote access to desktop workstations is available via the university
   staff shell servers ``viila.aalto.fi`` or department-specific
   servers ``magi.cs.aalto.fi`` (CS), ``amor.org.aalto.fi`` (NBE),
   ``elliptic.aalto.fi``/``illposed.aalto.fi`` (Math).
-  You need to be the **PrimaryUser** of the desktop in order to ssh to
   it.
-  Remote access to Triton is available from any Aalto shell server:
   ``viila``, ``kosh.aalto.fi``, etc.
-  When connecting from outside Aalto, you `have to
   use <https://aaltoscicomp.github.io/blog/2023/ssh-keys-with-passwords/>`__
   both SSH keys and a password, or use the VPN.
-  See :doc:`/scicomp/ssh` for generic SSH instructions.
-  SSHing directly to computers using openssh ProxyJump:

   -  Put this in your .ssh/config file under the proper Host line:
      ``ProxyJump viila.aalto.fi`` (or for older SSH clients,
      ``ProxyCommand ssh viila.aalto.fi -W %h:%p``).
   -  Note that unless your local username matches your Aalto username, or
      unless you have defined the username for ``viila.org.aalto.fi`` elsewhere
      in the SSH config, you will have to use the format
      ``aaltousername@viila.org.aalto.fi`` instead.

Remote desktop
~~~~~~~~~~~~~~

Aalto has remote desktops available at https://vdi.aalto.fi and http://mfavdi.aalto.fi/.  This
works from any network.

There are both Windows and Linux desktops available.  They are
arranged as virtual machines with the normal desktop installations, so
have access to all the important filesystems and all ``/m/{dept}/...``.
