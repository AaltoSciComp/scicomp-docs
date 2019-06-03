========================
Linux shell crass course
========================

If you are reading this case, you probably need to do some sort of
scientific computing involving the **Linux shell**, or command line
interface.  You may wonder why we are still using a command line
today, but the answer is somewhat simple: once you are doing
*scientific computing*, you eventually need to script and automate
something.  The shell is the *only* method that gives you the power to
do *anything you may want*.

These days, you don't need to know as much about the shell (we make
things easier), but there are at least a few important commands.
Still, the command line works when nothing else does, so you need to
learn a bit.



What's a shell?
---------------

It's the complicated looking thing where you type commands and get
output.

You type a **command**, which may include **arguments**.  Output gets
shown to the screen.  Spaces separate commands.

It seems boring, but the real power is that you can **script**
(program) commands to run automatically.



Editing and viewing files
-------------------------

You can use the command ``nano`` to edit files.  This is a simple
editor.

You can use the command ``less`` to view files without editing them.



Listing and moving files
------------------------

``ls`` lists the current directory.  ``ls -l`` shows more information,
and ``ls -a`` shows hidden files.  The options can be combined, ``ls
-la`` or ``ls -l -a``.  This pattern of options is standard for most
commands.

``mv`` will move or rename files.  For example, ``mv file.old
file.new``.

``cp`` will make a copy, with the exact same syntax as ``mv``: ``cp
file.old file.copy``.

``rm`` will remove a file: ``rm file.txt``.  To remove a directory,
use ``rm -r``.  Note that ``rm`` does not have backups and does not
ask for confirmation!

``mkdir`` makes a directory: ``mkdir dirname``.



Current directory
-----------------

Unlike with a graphical file browser, there is a concept of ``current
working directory``: each shell is in a current directory.  If you
``ls``, it lists files in your current directory.  If a program tries
to open a file, it opens it *relative to that directory*.

You can use ``cd`` to change working directories.



Online manuals for any command
------------------------------

``man`` is an on-line manual, type ``man ls`` to get help on the
``ls`` command.  The same works for almost any program.  They can be
easy to

Use ``q`` to quit or ``/`` to search (``n`` and ``N`` to search again
forward and backwards).



Tab completion
--------------

Annoyed at typing so much?  Everyone is, so shells have **tab
completion**.  Type the first few letters of any command and

**Exercise:** Type ``pytho`` and push ``TAB``. (erase that then start
over) Then type ``p`` and push ``TAB`` twice.  (erase that and start
over) Then ``ls``, space, and the first few letters of a filename,
then push ``TAB``.






See also
--------

* The :doc:`linux shell course <training/linux-shell-tutorial>` has
  *much* more details.
* Software Carpentry has a `basic shell course
  <http://swcarpentry.github.io/shell-novice/>`__.  Sections one to 3
  are details of what is above (the rest is about shell scripting).
