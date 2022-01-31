.. list-table::
   :header-rows: 1

   * * Method
     * Description

   * * rsync transfers
     * Transfer back and forth via command line.  Set up ssh first.

       ``rsync triton.aalto.fi:/path/to/file.txt file.txt``

       ``rsync file.txt triton.aalto.fi:/path/to/file.txt``

   * * SFTP transfers
     * Operates over SSH.  sftp://triton.aalto.fi in file browsers
       (Linux at least), FileZilla (to ``triton.aalto.fi``).

   * * SMB mounting

     * Mount (make remote viewable locally) to your own computer.

       Linux: File browser, ``smb://data.triton.aalto.fi/scratch/``

       MacOS: File browser, same URL as Linux

       Windows: ``\\data.triton.aalto.fi\scratch\``
