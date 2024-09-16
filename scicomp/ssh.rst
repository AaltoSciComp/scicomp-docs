SSH
===

Secure Shell (SSH) is the standard program for connecting to remote
servers and transferring data.  It is very secure and well-supported,
so it's worth learning to use it properly.  This page both gives a bit
of a crash course (top) and more details (bottom) for all common
connection methods.

.. highlight:: console



Setup
-----

Check the tabs below for your operating system and methods to see
which method you want to use.

.. tabs::

   .. group-tab:: Windows with PowerShell

      PowerShell is built in to Windows 10 and includes OpenSSH (the
      same as on Linux).  Start the "Windows PowerShell" program.
      **Then, follow the "Command line" instructions on most of this
      page if there isn't a separate PowerShell tab**.  If you want to
      set up SSH keys there are a few differences but overall it is
      the same procedure.

      This should work by default on recent Windows 10.

   .. group-tab:: Windows with WSL

      The Windows Subsystem for Linux lets you install a Linux
      operating system inside of Windows.  This is what we recommend
      with Windows, if it works.

      Install the `Windows Subsystem for Linux
      <https://docs.microsoft.com/en-us/windows/wsl/install>`__ **and
      then use the "Command line" instructions**.  This will give you a top-level
      interface to scientific work on your computer.

      This may not work if you do not have proper admin rights on your
      computer (e.g. if it is university managed).  Ask your IT
      support.

   .. group-tab:: Windows with PuTTY

      This should only be used if the other methods don't work.

      `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__
      is a separate application that includes a terminal and SSH
      together.  This used to be recommended before Windows 10.  There
      aren't detailed instructions below, but most of the ideas can be
      done with PuTTY somehow (except that SSH keys take more work).

   .. group-tab:: Windows with MobaXterm

      `MobaXterm <https://mobaxterm.mobatek.net/>`__ is a separate
      application that allow SSH and also graphical applications.
      It's liked by some people, but is freeware/commercial so isn't
      discussed much more here.  TODO: someone could describe it more
      if they wanted.

   .. group-tab:: Linux

      SSH is built-in to almost any distribution.  If it's not there,
      try installing the ``openssh-client`` package.

      Start the Terminal application to follow the rest of the
      instructions.  Then, follow the **"Command Line"** instructions
      on most of this page.

   .. group-tab:: Mac

      SSH should be built-in.  Start the Terminal application.  Then,
      follow the **"Command Line"** instructions on most of this page.

This guide uses Aalto University's HPC cluster as an example, but
should be applicable to other :doc:`remote servers at Aalto
</aalto/remoteaccess>` as well and many other outsiders as well.



Basic use: connect to a server
------------------------------

The standard login command with the command line is::

  $ ssh USER@triton.aalto.fi

where ``USER`` is your username (Aalto: standard Aalto login, not
email address) and ``triton.aalto.fi`` is the address of the server
you with to connect - replace this for your situation.

First time login: check host key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When connecting to a new computer, you will be prompted to affirm that
you wish to connect to this server for the first time.  This lets you
make sure you are connecting to the right computer (which is important
if you type a password!).  You'll get a message such as::

    The authenticity of host 'triton.aalto.fi (130.233.229.116)' can't be established.
    ECDSA key fingerprint is SHA256:04Wt813WFsYjZ7KiAyo3u6RiGBelq1R19oJd2GXIAho.
    Are you sure you want to continue connecting (yes/no)?

If possible, compare the key fingerprint you get to the one for the
machine which you can find online (Triton cluster:
:doc:`/triton/usage/ssh-fingerprints`, `Aalto servers
<https://www.aalto.fi/en/services/linux-shell-servers-at-aalto>`__),
and if they do not match, please contact the server administrator
**immediately**. If they do match, type ``yes`` and press enter. You
will receive a notice::

    Warning: Permanently added 'triton.aalto.fi,130.233.229.116' (ECDSA) to the list of known hosts.

The **public key** that identifies Triton will be stored in the file
``~/.ssh/known_hosts`` and you shouldn't get this prompt again. You
will be also asked to input your Aalto password before you are fully
logged in.  You want to say "yes, save the key for the future" - it's
more secure and you can always change it later if needed.

Checking known servers
~~~~~~~~~~~~~~~~~~~~~~

You will not receive an authenticity prompt upon first login if the
server's public key can be found in a list of known hosts. To check
whether a server, for example ``kosh.aalto.fi``, is known::

  $ ssh-keygen -F kosh.aalto.fi

Your computer might come with some keys pre-loaded for your
university's computers, for example::

  $ ssh-keygen -f /etc/ssh/ssh_known_hosts -F kosh.aalto.fi



SSH keys: better than just passwords
------------------------------------

By default, you will need to type your password each time you wish to
ssh into Triton, which can be tiresome, particularly if you regularly
have multiple sessions open simultaneously. A more secure (and faster)
way to authenticate yourself is to use a **SSH key pair** (this is
`public-key cryptography
<https://en.wikipedia.org/wiki/Public-key_cryptography>`__. The
private key should be encrypted with a strong password `xkcd
<https://www.xkcd.com/936/>`__ has good and amusing recommendations on
the subject of passwords. This authentication method will allow you to
log into multiple ssh sessions while only needing to enter your
password once, saving you time and keystrokes.

You make a key on your own computer/laptop, the copy the public
(``*.pub``) side to the cluster.  The private one (without ``.pub``)
stays on your computer.

Generate an SSH key
~~~~~~~~~~~~~~~~~~~

While there are many options for the key generation program ``ssh-keygen``, here are the four main ones.

- ``-t`` -> the cryptosystem used to make the unique key-pair and encrypt it.
- ``-f`` -> filename of key
- ``-C`` -> comment on what the key is for

Here are our recommended input options for key generation:

.. tabs::

   .. group-tab:: Command line

      ::

	 $ ssh-keygen -t ed25519

      This works on Linux, MacOS, Windows

   .. group-tab:: Windows with PuTTY

      The PuTTYgen program can generate keys.  We don't go into more
      details right now.  This provides a graphical application to
      generate keys and from here you would extract the OpenSSH format
      keys to copy to the servers.

Accept the default name of the key file by pushing enter with no extra
text(it will be automatically used later). Then, you will be prompted
to enter a password. **PLEASE** use a strong unique password. Upon
confirming the password, you will be presented with the key
fingerprint as both a SHA256 hex string as well as randomart
image. Your new key pair should be found in the hidden ``~/.ssh``
directory (A directory called ``.ssh`` in your user's home directory).

Key type ``ed25519`` makes a private key named ``~/.ssh/id_ed25519``
and public key named ``~/.ssh/id_ed25519.pub``.  The private key only
stays on your computer.  The public key goes to other comuters.
**Other key types were common in the past, and you may need to change
your filenames in some of the future commands** (for exmaple
``~/.ssh/id_rsa.pub``).


Copy public key to server
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use your key-pair to login to a server (for example: the
Triton cluster), you first need to securely copy the desired *public
key* to the machine with ``ssh-copy-id``. The script will also add the
key to the ``~/.ssh/authorized_keys`` file on the server. You will be
prompted to enter your Aalto password to initiate the secure copy of
the file to Triton.

.. tabs::

  .. group-tab:: Command line

     ::

	$ ssh-copy-id -i ~/.ssh/id_ed25519.pub USER@triton.aalto.fi

  .. group-tab:: Windows with PowerShell

     With this, we have to also make the directory and make sure the
     file has the right permissions.

     ::

	$ ssh USER@triton.aalto.fi "mkdir -p ~/.ssh ; chmod go-rwx ~/.ssh"
	$ cat ~/.ssh/id_ed25519.pub | ssh USER@triton.aalto.fi "cat >> ~/.ssh/authorized_keys"
	$ ssh USER@triton.aalto.fi "chmod go-rwx ~/.ssh/authorized_keys"

  .. group-tab:: Manual

     Connect to the system via some method and get a shell.  Copy the
     OpenSSH public key (it should be one line, though a quite long
     line).  You'll want to past the key as a new line in the file
     ``~/.ssh/authorized_keys`` file on the other server.  This is a
     file in your home directory (``~``), in the ``.ssh`` directory.

     From a terminal **on the remote computer**, you can run these
     commands to make a ``.ssh`` directory, edit the file, and set the
     permissions correctly.  ``nano`` is a common editor, if it's not
     available you need to use a different one::

	$ mkdir -p ~/.ssh
	$ nano ~/.ssh/authorized_keys
	## Paste the key into that file and save.
	$ chmod -R go-rwx ~/.ssh/

     You can also edit ``.ssh/authorized_keys`` to manage your keys
     later.

  .. group-tab:: Windows with PuTTY

      You'll need to grab the key from PUTTYgen and copy it to the
      remote server.  Copy the key from PuTTYgen and then us ethe
      "Manual" instructions.


.. admonition:: Connecting from outside of the Aalto network

   Sometimes, you can't connect directly to the computer you need to,
   since there is a **jump host** as some sort of a firewall.  You
   need to connect to that computer first.  This is described below in
   the section :ref:`proxyjump`, but we give first workaround here.
   but roughly.

   All this is easier if you set up a config file with ProxyJump
   (``-J``) first, and copy keys one at a time. (see :ref:`as
   described below <example_config_for_ssh>`).  Once this is done, you
   can copy your key to ``kosh`` first, then ``triton_via_kosh`` for
   example.

   Aalto University: If you can connect by VPN, or to Eduroam, then
   you can directly access the Triton cluster and copy your key like
   above.

   First copy the key to the jump host (like ``kosh.aalto.fi``), then
   copy to your final destination (like ``triton.aalto.fi``):

   .. tabs::

      .. group-tab:: Command line

	 ::

	    $ ssh-copy-id -i ~/.ssh/id_ed25519.pub USER@kosh.aalto.fi
	    $ ssh-copy-id -i ~/.ssh/id_ed25519.pub -o ProxyJump=USER@kosh.aalto.fi USER@triton.aalto.fi

      .. group-tab:: Windows with PowerShell

	 Like before, since ``ssh-copy-id`` isn't available, we have
	 to do extra steps to make sure the key is has the right
	 permissions - twice!  You may need to enter your password
	 many times here.

	 ::

	    ## Copy stuff to our jump host
	    $ ssh USER@kosh.aalto.fi "mkdir -p ~/.ssh ; chmod go-rwx ~/.ssh"
	    $ cat ~/.ssh/id_ed25519.pub | ssh USER@kosh.aalto.fi "cat >> ~/.ssh/authorized_keys"
	    $ ssh USER@kosh.aalto.fi "chmod go-rwx ~/.ssh/authorized_keys"

	    ## Copy stuff to the real destination
	    $ ssh -J USER@kosh.aalto.fi USER@triton.aalto.fi "mkdir -p ~/.ssh ; chmod go-rwx ~/.ssh"
	    $ cat ~/.ssh/id_ed25519.pub | ssh -J USER@kosh.aalto.fi USER@triton.aalto.fi "cat >> .ssh/authorized_keys"
	    $ ssh -J USER@kosh.aalto.fi USER@triton.aalto.fi "chmod go-rwx ~/.ssh/authorized_keys"



Login with SSH key
~~~~~~~~~~~~~~~~~~

If the key is in one of the standard filenames, it should work
directly.


.. _ssh-agent:

SSH key agent
~~~~~~~~~~~~~

To avoid having to type the decryption password, the *private key*
needs to be added to the ``ssh-agent`` with the command

.. tabs::

  .. group-tab:: Windows with PowerShell

     You will need administrative permissions to be able to start
     a ssh-agent on your machine that can store and handle
     passwords.

     1. Open *Services* from the start menu

     2. Scroll down to *OpenSSH Authentication Agent* > *double click*

     3. Change the *Startup type* to *Automatic (Delayed Start)*,
	or anything that is not *Disabled*, then *Apply*, and also
	start the service manually if it is not yet running.

     4. ``ssh-add`` to add the default key (to add a certain key,
        use ``ssh-add ~/.ssh/id_ed25519``, for example)

  .. group-tab:: Windows with PuTTY

     The program Pagent ("PuTTY Agent") can unlock your keys once and
     give them to PuTTY each time they are needed.  You can add keys
     and manage it from the small icon in the system tray.  TODO: more
     instructions on using Pagent.

  .. group-tab:: Linux

     SSH is likely to automatically save the key the first time you
     use it, so that you don't have enter your key's password multiple
     times.  If not, this will probably add it::

       $ ssh-add

     (You'll get a message if ``ssh-agent`` is not running.  In this
     case, to start a new agent, use ``eval $(ssh-agent)``.  It'll
     only work for this one shell, check the rest of the Internet for
     how to do more.)  TODO: is any more needed?

  .. group-tab:: Mac

     ::

	$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519


Once the password is added, you can ssh as normal but will immediately
be connected without any further prompts for passwords.



.. _proxyjump:

ProxyJump
---------

Often, you can't connect directly to your target computer: you need to
go through some other firewall host.  This is often done with two
separate ``ssh`` commands, but can be done with only one with the
``-J`` (ProxyJump) option::

  $ ssh -J FIREWALL.aalto.fi triton.aalto.fi

Both of these can take more options, for example if you need to
specify your username you might need to do it twice::

  $ ssh -J USER@FIREWALL.aalto.fi USER@triton.aalto.fi

Read more details at
https://www.redhat.com/sysadmin/ssh-proxy-bastion-proxyjump, including
putting this in your configuration file (or see below).

(Windows with PuTTY: Connection > Proxy > Proxy type="SSH to proxy and
use port forward.", then enter the firewall host as "Proxy hostname"
and port 22.



.. _ssh-multiplex:

Multiplexing
------------

Connections can be even faster: you can re-use existing connections to
start new connections, so that future ``ssh`` commands to the same
host are almost instant.  It **multiplexes** across the same
connection, and is controlled by ``ControlMaster``, ``ControlPath``,
and ``ControlPersist``.  With a proper SSH key setup, the gain is
minimal, but it can be useful sometimes.  **It is not recommend to use
this unless you really want this, since there are some gotchas::**

- Connections hanging (e.g. unstable network, changing network) will
  cause all multiplexed connections to hang.
- All multiplexed connections need to stop before the master process
  (first SSH connection) will stop.  So if you try to exit the first
  SSH but child processes are using it, it will appear to hang - this
  may not be obvious.
- If you are using with ProxyJump, there are two possible SSH
  processes which can hang and cause things to go wrong.
- Only use this on your own computers that you control, for security
  reasons.

This works with OpenSSH.  If you want to use this, to you ssh config
file (see below) add ``ControlMaster auto`` and ``ControlPath
/tmp/.ssh-USER-mux-ssh-%r@%h:%p`` (replacing USER with your username)
and test well.  You might want ``ServerAliveInterval 30`` to kill
stuff soon if network goes down.  We don't give a full example to
prevent unintended problems.  If you notice weird things happening
with your ssh, point your helpers to this section.



.. _ssh-config:

Config file: don't type so many options
---------------------------------------

Remembering the full settings list for the server you are working on
each time you log in can be tedious. A ssh ``config`` file allows you
to store your preferred settings and map them to much simpler login
commands. To create a new user-restricted ``config`` file

.. tabs::

  .. group-tab:: Command line

    ::

       $ touch ~/.ssh/config && chmod 600 ~/.ssh/config

  .. group-tab:: Windows PowerShell

     ::

	$ New-Item ~/.ssh/config


Open the created file to edit it as indicated below.

For a new configuration, you need specify in ``config`` at minimum the

- Host: the name of the settings list
- User: your login name when connecting to the server (if different
  from the username on your computer)
- Hostname: the address of the server

So for the simple Triton example, it would be:

.. code-block:: none

    # Configuration file for simplifying SSH logins
    #
    # HPC slurm cluster
    Host triton
	User LOGIN_NAME
	Hostname triton.aalto.fi

and you can use only this command to log in from now on::

  $ ssh triton

Any additional server configs can follow the first one and must start
with declaring the configuration ``Host``:

.. code-block:: none

    # general login server
    Host kosh
	User LOGIN_NAME
	Hostname kosh.aalto.fi
    # light-computing server
    Host brute
	User LOGIN_NAME
	Hostname brute.aalto.fi

There are optional ssh settings that may be useful for your work, such
as:

.. code-block:: none

   # Turn on X11 forwarding for Xterm graphics access
   ForwardX11 yes
   # Connect through another server (eg Kosh) if not connected directly to Aalto network
   ProxyJump USER@kosh.aalto.fi



.. _example_config_for_ssh:

Full sample config file
~~~~~~~~~~~~~~~~~~~~~~~

The following code is placed in the config file created above
(i.e. ``~/.ssh/config`` on Mac/Linux or ``%USERPROFILE%/.ssh/config``
on windows):

.. code-block:: none

    # general login server
    Host kosh
	User LOGIN_NAME
	Hostname kosh.aalto.fi

    # Triton, via kosh
    Host triton_via_kosh
	User LOGIN_NAME
	Hostname triton.aalto.fi
	ProxyJump kosh

Now, you can just do command such as::

  $ ssh triton
  $ rsync triton:/m/cs/scratch/some_file .
  ## And this works in any other tool that uses ssh.

directly, by using the ``triton`` alias.  Note that the Triton rule
uses the name ``kosh`` which is defined in the first part of the
file.



References
----------

- `man ssh
  <https://manpages.debian.org/stable/openssh-client/ssh.1.en.html>`__
  gives a detail of the SSH command line options
- `man ssh_config
  <https://manpages.debian.org/stable/openssh-client/ssh_config.5.en.html>`__
  gives a detail of all of the config file options
- https://www.mn.uio.no/geo/english/services/it/help/using-linux/ssh-tips-and-tricks.html -
  long-form guide
- https://blog.0xbadc0de.be/archives/300 - long-form guide
- https://www.phcomp.co.uk/Tutorials/Unix-And-Linux/ssh-passwordless-login.html
- https://en.wikibooks.org/wiki/OpenSSH/
- https://linuxize.com/post/ssh-command-in-linux/#how-to-use-the-ssh-command
- https://linuxize.com/post/how-to-setup-passwordless-ssh-login/
- https://hpc-uit.readthedocs.io/en/latest/account/login.html
- https://infosec.mozilla.org/guidelines/openssh
- https://www.ssh.com/ssh/ - commercial site
