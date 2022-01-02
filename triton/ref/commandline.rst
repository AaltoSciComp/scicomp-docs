``ls [DIR]``
   List current directory (or DIR)

``pwd``
   Print current directory

``cd DIR``
   Change directory.  ``..`` is parent directory, ``/`` is root, ``/``
   is also chaining directories, e.g. ``dir1/dir2`` or ``../../``

``nano FILE``
   Edit a file (there are many other editors, but ``nano`` is common,
   nice, and simple).

``mkdir DIR-NAME``
   Make a new directory.

``cat FILE``
   Print entire contents of file to standard output (the terminal)

``less FILE``
   Less is a "pager", and lets you scroll through a file.  ``q`` to
   quit.

``mv SOURCE DEST``
   Move (=rename) a file.  ``mv SOURCE1 SOURCE2 DEST-DIRECTORY/``
   copies to directory.

``cp SOURCE DEST``
   Copy a file.  The ``DEST-DIRECTORY/`` syntax of ``mv`` works as
   well.

``rm FILE ...``
   Remove a file.  Note, from the command line there is no recovery!
   Always pause and check before running this command.  Add ``-r`` to
   remove whole directories recursively.

``head [FILE]``
   Print the first 10 (or N lines with ``-n N``) of a file.  Can take
   input from standard input instead of ``FILE``.  ``tail`` is similar
   but the end of the file.

``grep PATTERN [FILE]``
   Print lines matching a pattern in a file, suitable as a primitive
   find feature, or quickly searching for output.  Can also use
   standard input instead of ``FILE``.

``du [-ash] [DIR]``
   Print disk usage of a directory. ``-h`` means "human readable" (MB,
   GB, etc), ``-s`` means "only of DIR, not all subdirectories also".
   ``-a`` means "all files, not only directories".
   A common pattern is ``du -h DIR | sort -h`` to print all
   directories and their sizes, sorted by size.

``stat``
   Show detailed information on a file's properties.

``find [DIR]``
   find can do almost anything, but that means it's really hard to use
   it well.  Let's be practical: with only a directory argument, it
   prints all files and directories recursively, which might be useful
   itself.  Many of us do ``find DIR | grep NAME`` to grep for the
   name we want (even though this isn't the "right way", there are
   find options which do this same thing more efficiently).

``|`` (pipe): ``COMMAND1 | COMMAND2``
   The output of ``COMMAND1`` is sent to the input of ``COMMAND2``.
   Useful for combining simple commands together into complex
   operations - a core part of the `unix philosophy
   <https://en.wikipedia.org/wiki/Unix_philosophy>`__.

``>`` (output redirection): ``COMMAND > FILE``
   Write standard output of ``COMMAND`` to ``FILE``.  ``<`` does the
   opposite, read input from a file.

``type COMMAND`` or ``which COMMAND``
   Show exactly what will be run, for a given command (e.g. ``type
   python3``).

``man COMMAND-NAME``
   Browse on-line help for a command.  ``q`` will exit, ``/`` will
   search (it uses ``less`` as its pager by default).

``-h`` and ``--help``
   Common command line options to print help on a command.  But, it
   has to be implemented by each command.
