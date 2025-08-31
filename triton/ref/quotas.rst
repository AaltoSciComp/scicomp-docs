* Read about :doc:`data storage at Aalto </data/index>` and
  :doc:`requesting storage space </data/requesting>`.  We strongly
  recommend project-based storage instead of increasing personal
  quotas.
* ``quota`` - print your quota and usage
* Finding what is using space

  * The ``dust`` tool prints a nice tree of largest directories.
    ``module load dust`` then ``dust $HOME`` on Triton.  ``$HOME`` can be
    replaced with any other directory (or left off for current directory)
  * ``du -h $HOME | sort -h``: Like above but works everywhere.  Use
    ``du -ah`` to list all files.

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
