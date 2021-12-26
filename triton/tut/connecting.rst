====================
Connecting to Triton
====================

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=i3m9uHDk9nE&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=7>`__

The traditional way of interacting with a cluster is via a terminal,
and Secure Shell (``ssh``) is the most common way of doing that.  The
terminal.  To learn more command line basics, see our :doc:`shell
crash course </scicomp/shell>` (which can be considered a prerequisite
for this series of tutorials).


.. admonition:: Cheatsheet

   * You can connect to Triton via ssh
   * Host name is ``triton.aalto.fi``
   * Connections available from the Aalto networks (VPN, most wired,
     internal servers, ``eduroam``, ``aalto`` *only* if using an
     Aalto-managed laptop, but *not* ``aalto open``),
   * VPN is best but ``kosh.aalto.fi`` is a good ssh jump host from
     outside (note the ``-J`` :doc:`ssh option </scicomp/ssh>`.

.. note::

   Are you here for a SciComp KickStart course?  You just need to :doc:`make
   sure you have an account <../accounts>` and then be able to connect
   via ssh (first section here), and you don't need to worry about the
   graphical application parts.  Everything else, we do tomorrow.

.. admonition:: Local differences

   The way you connect will be different in every site, but you should
   be able to get a terminal somehow.

There are different ways of connecting:

.. include:: ../ref/connecting.rst

.. highlight:: bash



Getting an account
------------------

Triton uses Aalto accounts, but your :doc:`account must be
activated first <../accounts>`.



Connecting via ssh
------------------

``ssh`` is one of the most fundamental programs: by using it
well, you can really do almost anything from anywhere.  It is not only
used for connecting to the cluster, but also for data transfer.  It's
worth making yourself comfortable with this.

.. tabs::

   .. tab:: Linux

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

   .. tab:: MacOS

      ``ssh`` is installed by default, usage is the same as in the
      Linux tab after starting the Terminal application.  To run
      graphical applications, you need to install an X server
      (XQuartz).

   .. tab:: Windows with WSL

      Install the `Windows Subsystem for Linux
      <https://docs.microsoft.com/en-us/windows/wsl/install>`__ and
      then use the Linux instructions.  This will give you a top-level
      interface to scientific work on your computer and is highly
      recommended.

      This may not work if you do not have proper admin rights on your
      computer (e.g. if it is university managed).  Ask your IT
      support well in advance for help!

   .. tab:: Windows with PuTTY

      If you can't use WSL, then you can install a separate terminal
      application.

      `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__ is
      the standard SSH client.  If you want to run graphical programs, you need an X server on
      Windows: see this
      `link <http://www.geo.mtu.edu/geoschem/docs/putty_install.html>`__ for
      some hints.  (Side note: putty dot org is an advertisement site trying to
      get you to install something else.)

      You should configure PuTTY with the hostname, username, and save the
      settings so that you can connect quickly.

      If you are outside the Aalto networks, you need to first connect to
      ``kosh.aalto.fi`` or some other server, and then use the Linux
      instructions to connect to Triton.

When connecting, you can :doc:`verify the ssh key fingerprints
<../usage/ssh-fingerprints>` which will ensure security.

See the :doc:`advanced ssh information </scicomp/ssh>` to learn how
to log in without a password, automatically save your username
and more. It really will save you time.

If you use OpenSSH (Linux/MacOS/WSL instructions above), the
``.ssh/config`` file is valuable to set up to make connecting more
seamless, with this you can run ``ssh triton_via_kosh`` instead of
using the ``-J`` option - and this same ``triton_via_kosh`` will work
with what you learn on the :doc:`remotedata` page!::

   Host triton
	User USERNAME
	Hostname triton.aalto.fi

   Host triton_via_kosh
	User USERNAME
	Hostname triton
	ProxyJump username@kosh.aalto.fi



.. admonition:: Change your shell to bash (old Aalto accounts)
   :class: toggle

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



Connecting via JupyterHub
-------------------------

Jupyter is a web-based way of doing computing.  But what some people
forget is that it has a full-featured terminal and console included.

Go to https://jupyter.triton.aalto.fi (not **.cs.**\ aalto.fi) and log
in.  Select "Slurm 5 day, 2G" and start.

To start a terminal, click File→New→Terminal - you do anything you
need to do from here, same as ``ssh``.  If you need to edit text
files, you can also do that through JupyterLab (note: change to the
right directory *before* creating a new file!).

To learn more about Jupyterlab, you need to read up elsewhere, there
are plenty of tutorials.



Connecting via the Virtual Desktop Interface
--------------------------------------------

If you go to https://vdi.aalto.fi, you can access a cloud-based Aalto
workstation.  HTML access works from everywhere, or download the
"VMWare Horizon Client" for a better connection.  Start a Ubuntu
desktop (you get Aalto Ubuntu).  From there, you **have to use the
normal Linux ssh instructions to connect to Triton** (via the Terminal
application) using the instructions you see above: ``ssh
triton.aalto.fi``.

For more information, see `the IT help
<https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__.


Exercises
---------

.. exercise:: Connecting-1: Connect to Triton

   Connect to Triton.  Use ``hostname`` to verify that you are on
   Triton.  List your home directory and work directory ``$WRKDIR``.

.. exercise:: Connecting-2: Test a few command line programs

   Check the uptime and load of the login node: ``uptime`` and
   ``htop`` (``q`` to quit - if ``htop`` is not available, then
   ``top`` works almost as well).  What else can you learn about the
   node?

.. exercise:: (optional, Aalto only) Connecting-3: check your default shell

   Check what your default shell is: ``echo $SHELL``.  Go ahead and
   change your shell to bash if it's not yet (see below).  This
   ``$SHELL`` syntax is an **environment variable** and a pattern you
   will see in the future.

   This is not needed for recent Aalto accounts but is a good exercise
   anyway.

.. exercise:: (advanced but recommended) Connecting-4: SSH configuration

   If you use Linux/MacOS/WSL, set up a ``.ssh/config`` file as shown
   above.  Customize it to suit your case.

.. exercise:: (advanced, to fill time) Connecting-5: shell crash
              course

   Browse the :doc:`/scicomp/shell` and see what you do and don't know
   from there.  Decide your future shell learning plan.



See also
--------

* :doc:`/scicomp/shell`



What's next?
------------

The next tutorial is about :doc:`software availability in general <applications>`.
