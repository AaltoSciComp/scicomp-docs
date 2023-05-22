Using the cluster from a shell
==============================

A **shell** is the **command-line terminal interface** which is most often
used in remote computers.  If you are using a cluster, you aren't just
computing things.  You are programming the computer to do things
for you over and over again.  *The shell is the only option to make
this work, so you have to learn a little bit*.

.. highlight:: console

Why a shell?
------------

The shell is the most powerful interface to computers: you can script
other programs to do things automatically.  When you are using a
cluster, you aren't just *doing the same thing on a bigger system* but
you program the computer to do things over and over and over again.
Shells, such as **bash** or **zsh**, are programming languages
designed for this.


.. figure:: img/connecting--terminal.png
   :alt: Image of terminal with two commands ran: ``whoami`` and ``hostname``

   Image of a terminal - this is what you want does it all.  The prompt
   ``darstr1@login3:~$`` gives a bit of info about who you are and
   where you are.  The commands ``whoami`` tells who you are
   (``darstr1``) and ``hostname`` tells what computer you are on
   (``login3.triton.aalto.fi``).

The shell uses **command line interfaces**, like this::

  $ python pi.py --seed=50

The parts are like this:

* ``python`` is the program that is run.
* ``pi.py`` and ``--seed=50`` are **arguments**.  It tells
  the program what to do, and the program can interpert them however
  it wants.  For Python, ``your-program.py`` is the Python file and
  that Python file itself knows how to handle ``--seed=50``.

These arguments let you control the program without modifying the
source code (or clicking buttons with yoru mouse!).  this lets us, for
example, make a shell script that runs with many different ``--seed``
values.

.. seealso::

  This is only a short intro.  You really need to read
  :doc:`/scicomp/shell` also for the full info.



Basic usage: navigating around
------------------------------

The first thing you need is to be able to go to files and directories.
Why?  *On a cluster, you can't throw everything into the same place.
You need to sort stuff and keep it organized.  Thus, you need files
and directories*.

**Directories** are often called folders.  Like "folders" implies,
they organize things.  Folders can also contain other folders, and so
on.

* ``pwd`` shows the directory you are in
* ``cd NAME`` changes to a directory
* ``cd`` changes back to your home directory
* ``/`` is the "root directory", everything is found under here.
* ``~`` is a shortcut for your home directory. 
* ``/home`` is a directory ``/home`` under ``/``


Copy your code to the cluster
-----------------------------

Usually, you would start by copying some existing code and data into
the cluster.  Let's talk about the code first.  You would ideally have
code in a **git repository** - this **version control system (VCS)**
can tracks files, synchronizes versions, and most importantly lets you
copy them to the cluster easily.  Git is outside the scope of this,
but you should see CodeRefinery's `git-intro course
<https://coderefinery.github.io/git-intro/>`__, and really all of
`CodeRefinery's courses <https://coderefinery.org>`__.  This isn't
covered any more here.

Let's clone the HPC-examples rpository.  This is something we'll use
in future examples.  First, we make sure we are in our home directory
(we always want to make sure we know where we are!  The home directory
is the default place, though)::

  $ cd $HOME

Then we clone our git repository::

  $ git clone https://github.com/AaltoSciComp/hpc-examples/

We can change into the directory::

  $ cd hpc-examples

Now we have our code

* Understand files and directories
* Navigate to a working directory
* "git clone" your project


Running a basic program
-----------------------

But how would you actually run things?  Usually, you would:

* Decide where to store your code
* Copy your code to the cluster (like we did above with the
  hpc-examples repository)
* Each time you connect, change directory to the place with the code
  and run from there.


What's next?
------------

The next step is looking at the :doc:`applications available
<applications>` on the cluster.
