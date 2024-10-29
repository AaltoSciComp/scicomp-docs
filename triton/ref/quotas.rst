* Read about :doc:`data storage at Aalto </data/index>` and
  :doc:`requesting storage space </data/requesting>`.  We strongly
  recommend project-based storage instead of increasing personal
  quotas.
* ``quota`` - print your quota and usage
* ``du -h $HOME | sort -h``: print all directories and
  subdirectories in your home directory, sorted by size.  This lets
  you find out where space is being used.  ``$HOME`` can be
  replaced with any other directory (or left off for the current
  directory).  Use ``du -a`` to list all files, not only directories.

  * ``du -h --max-depth=1 $HOME | sort -h``: Similar, but only list
    down to ``--max-depth`` levels.
  * ``du --inodes --max-depth=1 $HOME | sort -n``: Similar, but list
    the number of files in the directories.

* ``rm`` removes a single file, ``rm -r`` removes a whole directory
  tree.  **Warning: on scratch and Linux in general (unless backed
  up), there is no recovery from this!!** Think twice before you
  push enter.  If you have any questions, come to a garage and get
  help.
* ``conda clean`` cleans up downloaded conda files (but not
  environments).
