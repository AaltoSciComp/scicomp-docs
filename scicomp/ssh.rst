===
SSH
===

This walk-through presumes that the user

- is working on a Linux machine or Mac
- has ``OpenSSH`` installed: ``ssh -V`` in the terminal to check
- has an account on the server of interest
- is connected to the Aalto network

We will be focusing on connecting to *Triton* but the methods described below are applicable to any of Aalto's other :doc:`remote servers </aalto/remoteaccess.html>`.


Basic use: connect to a server
==============================

The standard login command is ``ssh login_name@host_name``,  where ``login_name`` is your standard Aalto login and ``host_name`` is the address of the server you with to connect. In the case of Triton, the ``host_name`` is ``triton.aalto.fi``.

First time login
----------------

For Triton, you will be prompted to affirm that you wish to *ssh* into this server for the first time.
::
    The authenticity of host 'triton.aalto.fi (130.233.229.116)' can't be established.
    ECDSA key fingerprint is SHA256:04Wt813WFsYjZ7KiAyo3u6RiGBelq1R19oJd2GXIAho.
    Are you sure you want to continue connecting (yes/no)?

Compare the key fingerprint you get to the one for the machine at this **link**, and if they do not match, please contact SciComp IT **immediately**. If they do match, type ``yes`` and press enter. You will receive a notice
::
    Warning: Permanently added 'triton.aalto.fi,130.233.229.116' (ECDSA) to the list of known hosts.

The *public key* that identifies Triton will be stored in ``~/.ssh/known_hosts`` and you ought not get this prompt again. You will be also asked to input your Aalto password before you are fully logged in.

Known servers
-------------

You will not receive an authenticity prompt upon first login if the server's *public key* can be found in a list of known hosts. To check whether a server, *Kosh* for example, is known
::
    ssh-keygen -f /etc/ssh/ssh_known_hosts -F kosh.aalto.fi
    ssh-keygen -f ~/.ssh/known_hosts -F kosh.aalto.fi


Login without password: ssh keys
================================

You may get tired of typing a password all the time: and you should,
using a key is faster and more secure.  You make a *ssh key* on your
own computer, copy the *public* key to the other server, and then can
login without a password.

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

    ssh-keygen -o

**Then, copy the key to computers you want to log into:** Use the
``ssh-copy-id`` script to copy the public key file to Triton.  This will
put the key in ``~/.ssh/authorized_keys`` (you can check this file to see
everything that's there).   (To do this manually, put the contents of
``.ssh/id_rsa.pub`` file into ``~/.ssh/authorized_keys`` on Triton.  If
you do this yourself, you may set set the permissions on
``.authorized_keys`` file: ``chmod u=rwx .ssh/``, ``chmod u=rw``
``.ssh/authorized_keys``.)

Finally, you should be able to login automatically.  A program called
``ssh-agent`` (or ``gnome-keyring``) decrypts the key once and holds
it and uses it each time you need to connect.  If it doesn't work
automatically, try running ``ssh-add`` yourself once.

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

__ https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/



Config file: don't type so many options
=======================================

Openssh on Linux and Mac can be made nicer if you set up a config file
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



..
  The purpose of this document is to describe how to use ssh such that
  usage is reasonably convenient and secure. Key takeaways:

  - Creating ssh keys
      - Do not copy private keys around. Instead create a separate
        private/public key pair for each device, and copy the public
        keys to those hosts you need to connect to.
      - Always protect the private key by a passphrase.
  - Use a ssh agent (ssh-agent, GNOME keyring, macOS keyring, putty
    Pageant, etc.) in order to avoid having to type your key password
    all the time.
  - Prefer ProxyJump/ProxyCommand to agent forwarding.




References
==========

- https://infosec.mozilla.org/guidelines/openssh
- https://blog.0xbadc0de.be/archives/300
- https://nvlpubs.nist.gov/nistpubs/ir/2015/NIST.IR.7966.pdf
