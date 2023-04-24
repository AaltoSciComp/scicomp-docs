========================
Linux shell crash course
========================

.. note::

   This is a kickstart for the Linux shell, to teach the minimum amount
   needed for any scientific computing course.  For more, see the
   `linux shell course <https://aaltoscicomp.github.io/linux-shell/>`__ or the
   references below.

   This is :doc:`basic B-level </training/index>`: no prerequisites.

.. admonition:: Watch this in video format

   There is a `companion video on YouTube
   <https://youtu.be/56p6xX0aToI>`__, if you would also like that
   format (and a `slightly longer one
   <https://youtu.be/ESXLbtaxpdI>`__ with more detail).


If you are reading this case, you probably need to do some sort of
scientific computing involving the **Linux shell**, or command line
interface.  You may wonder why we are still using a command line
today, but the answer is somewhat simple: once you are doing
*scientific computing*, you eventually need to script and automate
something.  The shell is the *only* method that gives you the power to
do *anything you may want*.

These days, you don't need to know as much about the shell as you used
to, but you *do* need to know a few important commands because the
command line works when nothing else does - and you can't do scripting
without it.



What's a shell?
---------------

It's the old-fashioned looking thing where you type commands with a
keyboard and get output to the screen.  It seems boring, but the real
power is that you can **script** (program) commands to run
automatically - which is the point of scientific computing.

You type a **command**, which may include **arguments**.  Output gets
shown to the screen.  Spaces separate commands and arguments.
Example: ``cp -i file1.txt file2.txt``.  ``cp`` is the command, ``-i`` is
an option, and ``file1.txt`` and ``file2.txt`` are arguments.  The
meaning of each option and argument is completely determined by the
program itself.

There are some conventions for options.  For example, ``--help`` or
``-h`` usually prints some help.

Files are represented by **filenames**, like ``file.txt``.
**Directories** are separated by ``/``, for example ``mydir/file.txt``
is **file.txt** inside of **mydir**.

**Exercise:** Start a shell.  On Linux or Mac, the "terminal"
application does this.



Editing and viewing files
-------------------------

``nano`` is an **editor** which allows you to **edit files** directly
from the shell.  This is a simple console editor which always gets the
job done.  Use *Control-x* (control and x at the same time), then
``y`` when requested and *enter*, to save and exit.

``less`` is a **pager** (file viewer) which lets you **view files**
without editing them.  (``q`` to quit, ``/`` to search, ``n`` / ``N``
to research forward and backwards, ``<`` for beginning of file, ``>``
for end of file)



Listing and moving files
------------------------

``ls`` **lists the current directory**.  ``ls -l`` shows more
information, and ``ls -a`` shows hidden files.  The options can be
combined, ``ls -la`` or ``ls -l -a``.  This pattern of options is
standard for most commands.

``mv`` will **move or rename files**.  For example, ``mv file.old
file.new``.

``cp`` will **make a copy of a file**, with the exact same syntax as
``mv``: ``cp file.old file.copy``.

``rm`` will **remove a file**: ``rm file.txt``.  To remove a directory,
use ``rm -r``.  Note that ``rm`` does not have backups and does not
ask for confirmation!

``mkdir`` **makes a directory**: ``mkdir dirname``.



Current directory
-----------------

Unlike with a graphical file browser, there is a concept of **current
working directory**: each shell is in a current directory.  If you
``ls``, it lists files in your current directory.  If a program tries
to open a file, it opens it *relative to that directory*.

``cd dirname`` will **change working directories** for your current
shell.  Normally, you will ``cd`` to a working directory, and use
relative paths from there. ``/`` alone refers to the **root
directory**, the parent of all files and directories.

``cd ..`` will change to the **parent directory** (dir containing this
dir).  By the same token, ``../..`` the parent of the parent, and so
on.

**Exercise:** Change to some directory and then another.  What do
(``cd -``) and (``cd`` with no arguments) do?  Try each a few times in
a row.


Online manuals for any command
------------------------------

``man`` is an **on-line manual**, type ``man ls`` to get help on the
``ls`` command.  The same works for almost any program.  In general you look for what you need,
not read everything.  The program that views the manual pages is (by
default) ``less`` which was described above: Use ``q`` to quit or
``/`` to search (``n`` and ``N`` to search again forward and
backwards).

``--help`` or ``-h`` is a standard argument that **prints a short
help** directly: for example ``cp --help``.

Manual pages can be long, some are easy
to read, some are impossible.  **tldr.sh** is a project that collects
simplified usage examples, see `the tldr.sh interactive web viewer
<https://tldr.inbrowser.app/>`__.



**Exercise:** briefly look at the manual pages and ``--help`` output
for the commands we have learned thus far.  How can you make ``rm``
ask before removing a file?


History and tab completion
--------------------------

Annoyed at typing so much?  We've got two ways to make work faster.

First, each shell keeps its **(shell) history**.  By pushing the up
arrow key, you can access previous lines.  Never type similar things
twice, go up in history and find the previous line, modify it, then
push enter to re-run.

Shells also have **tab
completion**.  Type the first few letters of any command or filename
and push tab once or twice... it will either complete it or show you
the options.  This is so important that it's used often, and many command
arguments can also be completed.

**Exercise:** Play around with tab completion.  Type ``pytho`` and
push ``TAB``. (erase that then start over) Then type ``p`` and push
``TAB`` twice.  (erase that and start over) Then ``ls``, space, and
the first few letters of a filename, then push ``TAB``.


Variables
---------

There are two kinds of variables in shell: **environment variables**
and **shell variables**.  You don't need to worry about the difference
now.  The ``$NAME`` or ``${NAME}`` syntax is used to is used to access
the value of a variable.

For example, the environment variable ``HOME`` holds your home
directory, for me ``/home/rkdarst``.    The command ``echo`` prints
whatever its arguments are, so ``echo $HOME`` prints my home
directory.  (Note that the variable is a property of the *shell*, not
of the *echo* command - this is sometimes important).

To set a variable, use ``NAME=value``.  ``export NAME=value`` sets it
as an *environment variable* which means that other processes you
start (from this shell) can use it.

The ``$VARIABLE`` syntax is also often used for examples: in this
case, it isn't an environment variable, but just something you need to
substitute yourself when running a command.



Quick reference
---------------

.. admonition:: Cheatsheet

   .. include:: /triton/ref/commandline.rst

See also
--------

* The `linux shell course <https://aaltoscicomp.github.io/linux-shell/>`__ has
  *much* more detail.
* Software Carpentry has a `basic shell course
  <http://swcarpentry.github.io/shell-novice/>`__.  Sections one to 3
  are details of what is above (the rest is about shell scripting).

.. exercise:: Explore manual pages

   For some fun, look at the manual pages for ``cat``,
   ``head``, ``tail``, ``grep``.

.. exercise:: Linux shell course (advanced)

   Read the `Linux shell course
   <https://aaltoscicomp.github.io/linux-shell/>`__ and understand
   what "pipes" and piping" are.
