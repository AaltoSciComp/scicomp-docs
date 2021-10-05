====================
Connecting to Triton
====================

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=i3m9uHDk9nE&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=7>`__

The traditional way of interacting with a cluster is via a terminal,
and Secure Shell (``ssh``) is the most common way of doing that, but
some clusters have other ways of getting a terminal (such as Jupyter
or virtual desktops).  Still, the command line is the most powerful
way of doing this.

.. admonition:: Prerequisites

      The :doc:`shell crash course </scicomp/shell>` is a prerequisite
      to this material (and the tutorial in general).


Summary:

You can connect to ``triton.aalto.fi`` via ssh from Aalto and CSC networks.
Aalto networks include: Wired workstation networks, ``eduroam``, and
the ``aalto`` wireless network *only if you are using an Aalto managed
laptop* (otherwise ``aalto`` is like ``aalto open``).  If you connect
to the Aalto VPN, you will be on the Aalto networks.

For SSHing to Triton from outside of your department or CSC, please
login first to a university server (like ``kosh.aalto.fi`` or
``taltta.org.aalto.fi``) and then open a session to
``triton.aalto.fi`` - or use the ``-J`` option in modern ssh.

.. important::

   Triton uses Aalto accounts, but your :doc:`account must be
   activated first <../accounts>`.

.. note::

   Are you here for a SciComp KickStart course?  You just need to :doc:`make
   sure you have an account <../accounts>` and then be able to connect
   via ssh (first section here), and you don't need to worry about the
   graphical application parts.  Everything else, we do tomorrow.

.. admonition:: Local differences

   The way you connect will be different in every site, but you should
   be able to get a terminal somehow.

There are different ways of connecting:

.. list-table::
    :header-rows: 1

    * * Method
      * About
      * From where?
    * * ssh
      * Works everywhere, from everywhere.  Firewalls may make things
	hard sometimes.
      * Aalto networks only, otherwise ssh to kosh and then Triton
    * * https://jupyter.triton.aalto.fi
      * Jupyter interface, but provides shell access via web browser.
      * Whole internet
    * * https://vdi.aalto.fi
      * Virtual desktop, from there you have to ``ssh`` to Triton
	anyway but gets you past firewalls and can run graphical
	programs via SSH.
      * Whole internet

.. highlight:: bash


Connecting via ssh
==================

Linux
-----

All Linux distributions come with an ``ssh`` client, so you don't need to do
anything.  To use graphical applications, use the standard ``-X`` option,
nothing extra needed.::

  ssh triton.aalto.fi
  # OR, if your username is different:
  ssh username@triton.aalto.fi


If you are from outside the Aalto networks, use the ProxyJump option
in modern OpenSSH::


    ssh -J kosh.aalto.fi triton.aalto.fi
    # OR, if your username is different:
    ssh -J username@kosh.aalto.fi username@triton.aalto.fi

    # If you do not have the -J option:
    ssh kosh.aalto.fi
    ssh triton.aalto.fi

Mac
---

``ssh`` is installed by default, same as Linux.  Run it from a terminal,
same command as Linux.  To run graphical applications, you need to
install an X server (XQuartz).

Windows
-------
If you are running Win10 with a recent update you should be able to follow
the same instructions as the linux/mac installation. The only difference is
that your config file and .ssh folder are in ``C:\Users\username\.ssh``, so 
anytime a tutorial refers to ``~/.ssh`` use ``C:\Users\username\.ssh`` instead.
to start the CLI on a windows machine run the cmd command (start -> run -> cmd).

If this doesn't work, you need to  install a ssh client yourself:  
`PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__ is the standard one.

In both instances, if you want to run graphical programs, you need an X server on
Windows: see this 
`link <http://www.geo.mtu.edu/geoschem/docs/putty_install.html>`__ for
some hints.  (Side note: putty dot org is an advertisement site trying to
get you to install something else.)


Advanced options
----------------

You can :doc:`verify the ssh key fingerprints <../usage/ssh-fingerprints>`.

See the :doc:`advanced ssh information </scicomp/ssh>` to learn how
to log in without a password, automatically save your username 
and more. It really will save you time.

``ssh`` is one of the most fundamental Linux programs: by using it
well, you can really do almost anything from anywhere.  The
``.ssh/config`` file is valuable to set up.  If ssh is annoying to
use, ask for some help in getting it working well.  



Exercise
--------

1. Connect to Triton.  List your home directory and work directory
   ``$WRKDIR``.

2. Check the uptime and load of the login node: ``uptime`` and
   ``htop`` (``q`` to quit - if ``htop`` is not available, then
   ``top`` works almost as well).  What else can you learn about the
   node?

3. Check what your default shell is: ``echo $SHELL``.  Go ahead and
   change your shell to bash if it's not yet (see below).



Change your shell to bash (Aalto)
---------------------------------

*Only needed if you shell isn't already* ``bash``.  *If* ``echo bash``
*reports* ``/bin/bash``\ *, then you are already using bash*.

The thing you are interacting with when you type is the **shell** -
the layer around the operating system.  ``bash`` is the most common
shell, but the Aalto default shell used to be ``zsh`` (which is more
powerful in some ways, but harder to teach with).  If you joined Aalto
after autumn 2018, you probably don't need to do anything.
We recommend that you check and change your shell to bash.

You can determine if your shell is bash by running ``echo $SHELL``.
Does it say ``/bin/bash``?

If not, ``ssh`` to ``kosh.aalto.fi`` and run ``chsh -s /bin/bash``.
It may take 15 minutes to update, and you will need to log in again.



Connecting via https://jupyter.triton.aalto.fi
==============================================

Jupyter is a web-based way of doing computing.  But what some people
forget is that it has a full-featured terminal and console included.

Go to https://jupyter.triton.aalto.fi (not **.cs.**\ aaalto) and log
in.  Select "Slurm 5 day, 2G" and start.

To start a terminal, click File→New→Terminal - you do anything you
need to do from here, same as ``ssh``.  If you need to edit text
files, you can also do that through JupyterLab (note: change to the
right directory *before* creating a new file!).

To learn more about Jupyterlab, you need to read up elsewhere, there
are plenty of tutorials.



Connecting via https://vdi.aalto.fi
===================================

If you go to https://vdi.aalto.fi, you can access a cloud-based Aalto
workstation.  HTML access works from everywhere, or download the
"VMWare Horizon Client" for a better connection.  Start a Ubuntu
desktop (you get Aalto Ubuntu).  From there, you **have to use the
normal ssh instructions** (via the Terminal application) using the
instructions you see above: ``ssh triton.aalto.fi``.

For more information, see `the IT help
<https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__.



What's next?
============

The next tutorial is about :doc:`software availability in general <applications>`.
