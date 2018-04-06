====================
Connecting to Triton
====================

All access to Triton is via Secure Shell (ssh).  Access to
``triton.aalto.fi`` is open from Aalto networks and CSC. For SSHing to
Triton from outside of your department or CSC, please login first to a
university server (like ``kosh.aalto.fi`` or  ``taltta.org.aalto.fi``)
and then open a session to ``triton.aalto.fi``.



Login shell: ssh
================


When you first log in, a set of in-cluster SSH keys is generated for
you. This is used to access all other Triton nodes. You shouldn't set
any password here (just push enter), because it is only used internally
in Triton.

Linux
-----

All Linux distributions come with an ssh client, so you don't need to do
anything.  To use graphical applications, use the standard "-X" option,
nothing extra needed.

::

    ssh triton.aalto.fi
    ssh username@triton.aalto.fi      # if your username is different

Mac
---

ssh is installed by default, same as Linux.  Run it from a terminal,
same command as Linux.  To run graphical applications, you need an to
install an X server (XQuartz).

Windows
-------

You need to install a ssh client yourself:  `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__ is
the standard one.  Use `WinSCP <https://winscp.net>`__ to transfer
files.  If you want to run graphical programs, you need an X server on
Windows: see this
`link <http://www.geo.mtu.edu/geoschem/docs/putty_install.html>`__ for
some instructions.

You can configure this with the hostname, username, and save the
settings so that you can connect quickly.



Set up key-based login
======================

Note: this section is only for connecting *to* Triton.  Once you are
connected the first time, a key for internal connections is
automatically made.

Linux
-----

We highly recommend you follow these steps on the first login to set up
passwordless SSH.  This will make your life much more pleasant, and can
be used when connecting to computers other than Triton. Using keys will
save you the trouble of entering passwords every time, since ssh stores
the key once and uses it for logging you in in the future.

**First, create the keypair on your own computer.** **Do not copy
private keys from other computers - one computer=one private key, and
copy only the public key (.pub) to any computer you want to log in to.**
Protect your SSH keyfiles with a *passphrase*. When asked to enter one,
use 3+ words, mixing languages, CAsE, or inflection, but make it
something you can remember without sticky notes.  `xkcd has some
opinions on this. <https://www.xkcd.com/936/>`__  A key without a
passphrase is like a password just sitting on disk - so be careful
here.  Passwordless keys are OK in certain cases, such as internal
triton connections.

::

    ssh-keygen -b 4096 -t rsa

**Then, copy the key to computers you want to log into:** Use the
``ssh-copy-id`` script to copy the public key file to Triton.  This will
put the key in ``~/.ssh/authorized_keys`` (you can check this file to see
everything that's there).   (To do this manually, put the contents of
``.ssh/id_rsa.pub`` file into ``~/.ssh/authorized_keys`` on Triton.  If
you do this yourself, you may set set the permissions on
``.authorized_keys`` file: ``chmod u=rwx .ssh/``, ``chmod u=rw``
``.ssh/authorized_keys``.)

Finally, you should be able to login automatically.  A program called
``ssh-agent`` (or ``gnome-keyring``) decrypts the key once and holds it and uses
it each time you need to connect.  If it doesn't work automatically, try
running ssh-add once.

Mac
---
You can follow same instructions from Linux.

Windows
-------
Realistically, on windows setting up keys takes some time.  You don't
need to worry about it (you will still have an ssh key on triton that
is used for internal connections).

You can make keys using ``puttygen``.  Here is `a tutorial`__.  You
should make a new key for each computer you have.

__ https://devops.profitbricks.com/tutorials/use-ssh-keys-with-putty-on-windows/



Advanced: set up ssh config file
================================

Linux/mac
---------

Openssh on linux can be made nicer if you set up a config file
(``.ssh/config``)::

    # Host alias triton: "ssh triton" instead of "ssh triton.aalto.fi".
    # You can set more options here.
    Host triton
        User YOUR_USERNAME
        Hostname triton.aalto.fi
        # Only if not on Aalto networks:
        # Next line *automatically* proxies you through kosh.aalto.fi.  You
        # probably want to set up a "kosh" host if username is different, and
        # set up public key authentication on kosh too.
        ProxyCommand ssh kosh.aalto.fi -W %h:%p
    # Defaults for all hosts.
    Host *
        # Following two lines allow SSH to reuse connections - second connections
        # open very fast.  If problems (channels exceeded), disable it.
        ControlMaster   auto
        ControlPath     /tmp/.ssh-USERNAME-mux-%r@%h:%p



File access
===========

You'll actually learn this in the next section, the `data storage
tutorial <storage>`.  It is easiest to mount them using SMB, and they
are also mounted on ``taltta.aalto.fi``, at
``/m/triton/{scratch,work}/``, which you can access over ssh or
``sftp``/``sshfs``.  See the next
tutorial (or :doc:`FAQ <../usage/faq>`).



What's next?
============

``ssh`` is one of the most fundamental Linux programs: by using it
well, you can really do almost anything from anywhere.  The
``.ssh/config`` file is valuable to set up.  If ssh is annoying to
use, ask for some help in getting it working well.

Next, move on to :doc:`the storage tutorial <storage>`
