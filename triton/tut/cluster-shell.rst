Using the cluster from a shell
==============================

A **shell** is the **command-line terminal interface** which is the
most common method of accessing remote computers.  If you are using a
cluster, you aren't just
computing things.  You are programming the computer to do things
for you over and over again.  *The shell is the only option to make
this work, so you have to learn a little bit*.

.. highlight:: console

Why a shell?
------------

The shell is the most powerful interface to computers: you can script
other programs to do things automatically.  It's much easier to script
things with text, than by clicking buttons.  It's also very easy to
add the **command line interfaces** to programs to make them
scriptable. Shells, such as **bash** or **zsh**, are basically
programming languages designed to connect programs together.


.. figure:: img/connecting--terminal.png
   :alt: Image of terminal with two commands ran: ``whoami`` and ``hostname``

   Image of a terminal - this is what you want does it all.


In the image above, we see a pretty typical example.  The **prompt**
is ``darstr1@login3:~$`` and gives a bit of info about what computer
you are running on.  The **commands** ``whoami`` tells who you are
(``darstr1``) and ``hostname`` tells what computer you are on
(``login3.triton.aalto.fi``).

You can also give **options** and **arguments** to programs, like
this::

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

You will learn all sorts of commands as you progress in your career.
:ref:`ref-command-line` gives the most important ones.



Basic usage: navigating around
------------------------------

On your phone and other "app"-like things, data just exists - you
don't really know where. *You* are the programmer when doing
scientific computing, so you have to make more meaningful decisions
about data.  This means knowing about **files** (a chuck of data) and
**directories** (hierarchical storage units, also known as folders).
*On a cluster, you can't throw everything into the same place. You
need to sort stuff and keep it organized.  File names are an essential
part of automating things.  Thus, you need knowledge of the storage
hierarchy*.

Everything on a Unix (Linux) system is organized in a hierarchy.
There aren't "drives" like "C-drive", different storage systems can be
available anywhere:

* ``/`` is the **root** of the filesystem
* ``/home/`` is a directory ("home directories")
* ``/home/darstr1/`` is the home directory of the user ``darstr1``
* ``/home/darstr1/git/`` is the directory darstr1 uses to store
  general git repositories.
* ... etc
* ``$HOME`` is an environment variable shortcut for your home directory.
* ``~`` is another shortcut for you home directory.
* On Triton, ``/scratch/`` is the basic place for storing research
  data.  Also on Triton, ``$WRKDIR`` is a shortcut for your personal
  space in scratch.

On a graphical computer, you open a windown to view files, but this is
disconnected from how you run programs.  In a shell, they are
intrinsically connected and that is *good*.

The most common commands related to directories:

* ``pwd`` shows the directory you are in.
* ``cd NAME`` changes to a directory.  All future commands are
  relative to the directory you change to.  This is the **(current)
  working directory**
* ``ls [NAME]`` lists the contents of a directory.  ``[NAME]`` is an
  optional directory name - by default, it lists the working directory.

Exercises, directories
~~~~~~~~~~~~~~~~~~~~~~

You have to be :doc:`connected to the custer and have a terminal
<connecting>` to do these exercises.

.. exercise:: Shell-1: Explore directories

  * Print your current directory with ``pwd``
  * List the contents with ``ls``
  * List the contents of ``/scratch/``, then the contents of another
    directory, and so on.
  * List your work directory ``$WRKDIR``.
  * Change to your work directory.  List it again, with a plan ``ls``
    (no full path needed).
  * List your home directory from your work directory (you need to
    give it a path)
  * Log out and in again.  List your current directory.  Note how it
    returns to your home directory - each time you log in, you need to
    navigate to where you need to be.

.. exercise:: Shell-2: Understand power of working directory

  * ``ls /scratch/cs/``
  * Change directory to ``/scratch``
  * Now list ``/scratch/cs``, but don't re-type ``/scratch``.



Copy your code to the cluster
-----------------------------

Usually, you would start by copying some existing code and data into
the cluster (you can also develop the code straight on the cluster).
Let's talk about the code first.  You would ideally have code in a
**git repository** - this **version control system (VCS)** can tracks
files, synchronizes versions, and most importantly lets you copy them
to the cluster easily.  Git is outside the scope of this, but you
should see CodeRefinery's `git-intro course
<https://coderefinery.github.io/git-intro/>`__, and really all of
`CodeRefinery's courses <https://coderefinery.org>`__.  This isn't
covered any more here.

**We are going to pretend we are researchers working on a sample
project, named hpc-examples.  During the rest of the tutorials, we
will keep using this example repository.**

Let's clone the HPC-examples repository so that we can work on it.
First, we make sure we are in our home directory (we always want to
make sure we know where we are!  The home directory is the default
place, though)::

  $ cd $HOME

Then we clone our git repository::

  $ git clone https://github.com/AaltoSciComp/hpc-examples/

We can change into the directory::

  $ cd hpc-examples

Now we have our code in a place that can be used.

.. exercise:: Shell-3: clone the hpc-examples repository

  Do the steps above.

.. exercise:: Shell-4: log out and re-navigate to the hpc-examples reports

  Log out and log in again.  Navigate to the hpc-examples repository.
  Resuming work is an important but often forgotten part of work.



Running a basic program
-----------------------

But how would you actually run things?  Usually, you would:

* Decide where to store your code
* Copy your code to the cluster (like we did above with the
  hpc-examples repository)
* Each time you connect, change directory to the place with the code
  and run from there.

In our case, after changing to the hpc-examples directory, let's run
the program ``pi.py`` using Python (this will be our common example
for a while)::

  $ cd hpc-examples
  $ python3 slurm/pi.py 10000

The argument "10000" is the number of iterations of the `circle in
square <https://en.wikipedia.org/wiki/Pi#Monte_Carlo_methods>`__
method of calculating π.

.. exercise:: Shell-5: try calculating pi.

  Try doing what is above and running ``pi.py`` several times with
  different numbers of iterations.  Try passing the ``--seed`` command
  line option with the values ``13``, and ``19759``.

  .. solution::

    ::

      $ cd hpc-examples
      $ python3 slurm/pi.py 10000
      Calculating Pi via 10000 stochastic trials
      {"successes": 7815, "pi_estimate": 3.126, "iterations": 10000}
      $ python slurm/pi.py 100
      Calculating Pi via 100 stochastic trials
      {"successes": 78, "pi_estimate": 3.12, "iterations": 100}
      $ python slurm/pi.py 1000000
      Calculating Pi via 1000000 stochastic trials
      {"successes": 785148, "pi_estimate": 3.140592, "iterations": 1000000}

    ::

      $ python slurm/pi.py 10000 --seed=13
      Calculating Pi via 10000 stochastic trials
      {"successes": 7816, "pi_estimate": 3.1264, "iterations": 10000}
      $ python slurm/pi.py 10000 --seed=19759
      Calculating Pi via 10000 stochastic trials
      {"successes": 7817, "pi_estimate": 3.1268, "iterations": 10000}



Exercises
---------

.. exercise:: (advanced, to fill time) Shell-5: shell crash
              course

   Browse the :doc:`/scicomp/shell` and see what you do and don't know
   from there.  :doc:`A future lesson <cluster-shell>` goes into this
   a bit more, too.



See also
--------

This is only a short intro.  You really need to read
:doc:`/scicomp/shell` also for the full info.


* :doc:`/scicomp/shell`
* `Working directory <https://en.wikipedia.org/wiki/Working_directory>`__
* `git-intro course <https://coderefinery.github.io/git-intro/>`__,
  and really all of `CodeRefinery's courses
  <https://coderefinery.org>`__



What's next?
------------

The next step is looking at the :doc:`applications available
<applications>` on the cluster.
