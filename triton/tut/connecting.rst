====================
Connecting to Triton
====================

.. include:: /triton/ref/videos.rst

The traditional way of interacting with a cluster is via the **command
line** in a **shell** in a **terminal**, and Secure Shell (``ssh``) is
the most common way of doing that.  To learn more command line basics,
see our :doc:`shell crash course </scicomp/shell>`.

.. admonition:: Abstract

   * When connecting to a cluster, our goal is to get a command-line
     terminal that provides a base for the rest of our work.
   * The standard way of connecting is via ssh, but Open OnDemand and
     Jupyter provide graphical environments that are useful for
     interactive work.
   * SSH host name is ``triton.aalto.fi``

   .. include:: ../ref/connecting.rst

.. admonition:: Kickstart course preparation

   Are you here for a SciComp KickStart course?  You just need to
   :doc:`make sure you have an account <../accounts>` and then be able
   to get to a terminal (as seen in the picture below) by any of the
   means here, and you don't need to worry about anything else.
   Everything else, we do tomorrow.

.. admonition:: Local differences

   The way you connect will be different in every site, but you should
   be able to get a terminal somehow.

.. figure:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/cluster-schematic/cluster-schematic-login.png
   :alt: Schematic of cluster with current discussion points highlighted; see caption or rest of lesson.

   We are working to get access to the login node.  This is the
   gateway to all the rest of the cluster.

.. highlight:: console



Getting an account
------------------

Triton uses Aalto accounts, but your :doc:`account must be
activated first <../accounts>`.


The terminal
------------

This is what you want by the end of this page: the command line
terminal.  Take the first option that works, or the one that's
comfortable to you.  However, it's good to get ``ssh`` working
someday, since it is very useful.  Later, in :doc:`cluster-shell`,
will explain more about how to actually use it.

.. figure:: img/connecting--terminal.png
   :alt: Image of terminal with two commands ran: ``whoami`` and ``hostname``

   Image of a terminal - this is what you want after this page.
   You'll see more about this means in :doc:`cluster-shell`.  Don't
   worry about what the commands mean, but you can probably figure
   out.


.. _triton-connecting-ssh:

Connecting via ssh
------------------

``ssh`` is one of the most fundamental programs of remote connections: by using it well, you
can really control almost anything from from anywhere.  It is not only
used for connecting to the cluster, but also for data transfer.  It's
worth making yourself comfortable with its use.

.. tabs::

   .. tab:: Linux

      All Linux distributions come with an ``ssh`` client, so you don't need to do
      anything.  To use graphical applications, use the standard ``-X`` option,
      nothing extra needed.::

        $ ssh triton.aalto.fi
        ## OR, if your username is different:
        $ ssh USERNAME@triton.aalto.fi

      If you are from outside the Aalto networks, use the ProxyJump
      option (``-J``) in modern OpenSSH::

          $ ssh -J kosh.aalto.fi triton.aalto.fi
          ## OR, if your username is different:
          $ ssh -J USERNAME@kosh.aalto.fi USERNAME@triton.aalto.fi

          ## If you do not have the -J option:
          $ ssh kosh.aalto.fi
          $ ssh triton.aalto.fi

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

   .. tab:: Windows with PowerShell

      If you can't use WSL, you can also use PowerShell.  Start
      the "Windows PowerShell" program.  Then, follow the Linux
      instructions.  If you want to set up ssh keys there are a few
      differences but overall it is the same procedure.

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
      instructions to connect to Triton (``ssh triton.aalto.fi``)

When connecting, you can :doc:`verify the ssh key fingerprints
<../usage/ssh-fingerprints>` which will ensure security.

See the :doc:`advanced ssh information </scicomp/ssh>` to learn how
to log in without a password, automatically save your username
and more. It really will save you time.

.. admonition:: SSH configuration file
   :class: dropdown

   This is described under the :doc:`advanced ssh information
   </scicomp/ssh>`, but here is a quick summary:

   If you use OpenSSH (Linux/MacOS/WSL or Windows Powershell instructions above), the
   ``.ssh/config`` file (on windows the ``.ssh`` folder is commonly under ``C:\Users\YourUsername``)
   is valuable to set up to make connecting more seamless, with this you can run
   ``ssh triton_via_kosh`` instead of using the ``-J`` option - and this same
   ``triton_via_kosh`` will work with what you learn on the :doc:`remotedata` page!::

      Host triton
      User USERNAME
      Hostname triton.aalto.fi

      Host triton_via_kosh
      User USERNAME
      Hostname triton
      ProxyJump USERNAME@kosh.aalto.fi


.. admonition:: Aalto: Change your shell to bash
   :class: toggle

   *Only needed if you shell isn't already* ``bash``.  *If* ``echo $SHELL``
   *reports* ``/bin/bash``\ *, then you are already using bash*.

   The thing you are interacting with when you type is the **shell** -
   the layer around the operating system.  ``bash`` is the most common
   shell, but the Aalto default shell used to be ``zsh`` (which is more
   powerful in some ways, but harder to teach with).  Depending on
   when you joined Aalto, your default might already be ``bash``.
   We recommend that you check and change your shell to bash.

   You can determine if your shell is bash by running ``echo $SHELL``.
   Does it say ``/bin/bash``?

   If not, ``ssh`` to ``kosh.aalto.fi`` and run ``chsh -s /bin/bash``.
   It may take 15 minutes to update, and you will need to log in again.


Connecting via Open onDemand
----------------------------

.. seealso::

   :doc:`../usage/ood`

OOD (Open onDemand) is a web-based user interface to Triton, including
shell access, and data transfer, and a number of other applications
that utilize graphical user interfaces. Read more from :doc:`its guide
<../usage/ood>`.  The **Triton shell access app will get you the
terminal** that you need for basic work and the rest of these tutorials.

It is only available from Aalto networks and VPN.  Go to
https://ood.triton.aalto.fi and login with your Aalto account.


Connecting via JupyterHub
-------------------------

.. seealso::

   :doc:`../apps/jupyter`

Jupyter is a web-based way of doing computing.  But what some people
forget is that it has a full-featured terminal and console included.

Go to https://jupyter.triton.aalto.fi (not **.cs.**\ aalto.fi) and log
in.  Select "Slurm 5 day, 2G" and start.

**To start a terminal, click File→New→Terminal - this is the shell you
need.**  If you need to edit text
files, you can also do that through JupyterLab (note: change to the
right directory *before* creating a new file!).

Warning: the JupyterHub shell runs on a compute node, not a login
node.  Some software is missing so some things don't work.  Try ``ssh
triton.aalto.fi`` from the Jupyter shell to connect to the login node.
To learn more about Jupyterlab, you need to read up elsewhere, there
are plenty of tutorials.



Connecting via the Virtual Desktop Interface
--------------------------------------------

.. seealso::

   `VDI instructions on aalto.fi <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__

If you go to https://vdi.aalto.fi, you can access a cloud-based Aalto Linux
workstation.  HTML access works from everywhere, or download the
"VMWare Horizon Client" for a better connection.  Start a Ubuntu
desktop (you get Aalto Ubuntu).  From there, you **have to use the
normal Linux ssh instructions to connect to Triton** (via the Terminal
application) using the instructions you see above: ``ssh
triton.aalto.fi``.



Exercises
---------

If you are in the kickstart course, Connecting-1 is required for the
rest of the course.

.. exercise:: Connecting-1: Connect to Triton

   Connect to Triton, and get a terminal by one of the options above.
   Type the command ``hostname`` to verify that you are on Triton.
   Run ``whoami`` to verify your username.

   .. solution::

      ::

         $ hostname
         login3.triton.aalto.fi
         $ whoami
         darstr1


.. exercise:: Connecting-2: (optional) Test a few command line programs

   Check the uptime and load of the login node: ``uptime`` and
   ``htop`` (``q`` to quit - if ``htop`` is not available, then
   ``top`` works almost as well).  What else can you learn about the
   node?  (You'll learn more about these in :doc:`cluster-shell`, this
   is just a preview to fill some time.)

   .. solution::

      You should see something like this. From this example output we can tell that the node was last rebooted 18 days ago, and the load average
      seems pretty high (1 = "about one processor in use".  There are
      24 processors in 2023.  Load of 1-5 would be normal).  Someone
      is running things directly on the login node, which is not
      good::

         $ uptime
         17:32:25 up 18 days,  3:20, 128 users,  load average: 29.46, 32.78, 34.28

      More info::

         $ lscpu
         (long output not listed here)
         $ uname -a       # tells a bit about operating system info
         Linux login3.triton.aalto.fi 3.10.0-1160.83.1.el7.x86_64 #1 SMP Wed Jan 25 16:41:43 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

      We'll see more in :doc:`cluster-shell`.


.. exercise:: Connecting-3: (optional, Aalto only) Check your default shell

   Check what your default shell is: run ``echo $SHELL``.  If it doesn't
   say ``/bin/bash``, go ahead and change your shell to bash if it's
   not yet (see the expandable box above).

   This ``$SHELL`` syntax is an **environment variable** and a pattern
   you will see in the future.

   .. solution::

      ::

         $ echo $SHELL
         /bin/bash


.. exercise:: (advanced but recommended) Connecting-4: SSH configuration

   If you use Linux/MacOS/WSL, start setting up a ``.ssh/config`` file
   as shown above and in :doc:`/scicomp/ssh`.  You probably won't have
   time to finish this, but you can resume later.  Customize it to
   suit your case.

   The "solution" is listed in the linked documents.



See also
--------

* :doc:`/scicomp/ssh`



What's next?
------------

The next tutorial is about :doc:`using the terminal <cluster-shell>`.
