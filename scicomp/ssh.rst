===
SSH
===

This walk-through presumes that the user

- is working on a Linux machine or Mac
- has ``OpenSSH`` installed: ``ssh -V`` in the terminal to check
- has an account on the server of interest
- is connected to the Aalto network

We will be focusing on connecting to *Triton* but the methods described below are applicable to any of Aalto's other :doc:`remote servers </aalto/remoteaccess>`.


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


SSH keys: better than just passwords
====================================

By default, you will need to type your password each time you wish to ssh into Triton, which can be tiresome, particularly if you regularly have multiple sessions open simultaneously. A more secure (and faster) way to authenticate yourself is to use a *shh key pair* and encrypt the this with a strong password. `xkcd <https://www.xkcd.com/936/>`__ has good and amusing recommendations on the subject of passwords. This authentication method will allow you to log into multiple ssh sessions while only needing to enter your password once, saving you time and keystrokes.

Generate an SSH key
-------------------

While there are many options for the key generation program ``ssh-keygen``, here are the four main ones.

- *-t* -> the cryptosystem used to make the unique key-pair and encrypt it.
- *-b* -> the number of key bits
- *-f* -> filename of key
- *-C* -> comment on what the key is for

Here are our recommended input options for key generation.

::
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_triton -C "triton key for ${USER}"

After running this command in the terminal, you will be prompted to enter a password. **PLEASE** use a strong unique password. Upon confirming the password, you will be presented with the key fingerprint as both a SHA256 hex string as well as randomart image. Your new key pair should be found in the hidden ``~/.ssh`` directory. If you wish to use keys for other servers, you should generate **new** key pairs and use **different** passwords.

Copy public key to server
-------------------------

In order to use your key-pair to login to Triton, you first need to securely copy the desired *public key* to the machine with ``ssh-copy-id``. The script will also add the key to the ``~/.ssh/authorized_keys`` file on the server. You will be prompted to enter your Aalto password to initiate the secure copy of the file to Triton.

::
    ssh-copy-id -i ~/.ssh/id_rsa_triton.pub login_name@triton.aalto.fi


Login with SSH key
-------------------

To avoid having to type the decryption password, the *private key* it needs to be added to the ``ssh-agent`` with the command

::
    ssh-add ~/.ssh/id_rsa_triton

Once the password is added, you can ssh into Triton as normal but will immediately be connected without any further prompts. If you are unsure whether a ``ssh-agent`` process is running on your machine, ``ps -C ssh-agent`` will tell you if there is. To start a new agent, use ``eval $(ssh-agent)``.


Config file: don't type so many options
=======================================

Remembering the full settings list for the server you are working on each time you log in can be tedious. A ssh ``config`` file allows you to store your preferred settings and map them to much simpler login commands. To create a new user-restricted ``config`` file

::
    touch ~/.ssh/config && chmod 600 ~/.ssh/config


For a new configuration, you need specify in ``config`` at minimum the

- Host: the name of the settings list
- User: your login name when connecting to the server
- Hostname: the address of the server

So for the simple Triton example, it would be

::
    # Configuration file for simplifying SSH logins
    #
    # HPC slurm cluster
    Host triton
        User LOGIN_NAME
        Hostname triton.aalto.fi

and you would use ``ssh triton`` to log in. Any additional server configs can follow the first one and must start with declaring the configuration ``Host``.

::
    # general login server
    Host kosh
        User LOGIN_NAME
        Hostname kosh.aalto.fi
    # light-computing server
    Host brute
        User LOGIN_NAME
        Hostname brute.aalto.fi

There are optional ssh settings that may be useful for your work, such as

::
        # Turn on X11 forwarding for Xterm graphics access
        ForwardX11 yes
        # Connect through another server (eg Kosh) if not connected directly to Aalto network
        ProxyCommand ssh kosh.aalto.fi -W %r@%h:%p
        # Specify which ssh private key is used for login identification
        IdentityFile ~/.ssh/id_rsa_triton


..
  The purpose of this document is to describe how to use ssh such that
  usage is reasonably convenient and secure. Key takeaways:

  - Logging into server with ssh and verify the server authenticity
  - Creating ssh keys
      - Generate complex key with strong password
      - One key for each server
  - Login with ssh key
      - ssh-agent holds password for session
      - save password
  - Setting up an ssh-config file to save & map your preferred login settings


References
==========

- https://www.ssh.com/ssh/
- https://blog.0xbadc0de.be/archives/300
- https://www.phcomp.co.uk/Tutorials/Unix-And-Linux/ssh-passwordless-login.html
- https://en.wikibooks.org/wiki/OpenSSH/
- https://linuxize.com/post/ssh-command-in-linux/#how-to-use-the-ssh-command
- https://linuxize.com/post/how-to-setup-passwordless-ssh-login/
- https://hpc-uit.readthedocs.io/en/latest/account/login.html
- https://www.mn.uio.no/geo/english/services/it/help/using-linux/ssh-tips-and-tricks.html
- https://infosec.mozilla.org/guidelines/openssh
