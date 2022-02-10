.. _remote_access_to_data:

=====================
Remote access to data
=====================

.. admonition:: Video

   Watch this in our courses: `2022 February
   <https://www.youtube.com/watch?v=raRQvKLTHpg&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=18>`__,
   `2021 January
   <https://www.youtube.com/watch?v=guZYMgwdP4Q&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=10>`__

The cluster is just one part of your research: most people are
constantly transferring data back and forth.  Unfortunately, this can
be a frustrating experience if you haven't got everything running
smoothly.  In this tutorial, we'll explain some of the main methods.


.. admonition:: Cheatsheet

   * Data is also available from other places in Aalto, such as
     desktop workstations in some departments, shell servers, and
     https://vdi.aalto.fi.

   * Transferring data is available via ssh (the standard ``rsync``
     and ``sftp``)

   * Data can be mounted remotely using ssh (``sshfs``, from anywhere
     with ssh access) and SMB mounting on your own computer (within
     Aalto networks, Linux/mac: ``smb://data.triton.aalto.fi/PATH``,
     Windows: ``\\data.triton.aalto.fi\PATH`` and uses ``\``, ``PATH``
     could be ``work/USERNAME`` or ``scratch/DEPT/GROUPNAME``)



History and background
----------------------

Historically, ``ssh`` transfers have been the most common (which
includes ``rsync`` (recommended these days), ``scp``, ``sftp``, and
various other graphical programs that use these protocols) - and this
is still the most robust and reliable method.  There are
other modern methods, but they require other things.

There are two main styles of remote data access:

* **Transferring data** makes a new copy on the other computer.  This
  is generally efficient for large data.
* **Remote mounting** makes a view of the data on the other computer:
  when you access/modify the data on the other computer, it
  transparently accesses/modifies *in the original place without
  making a copy*.  This is very convenient, but generally slow.

  * We have this already set up for you from many computers at Aalto.



Data availability throughout Aalto
----------------------------------

Data is the basis of almost everything we do, and accessing it
seamlessly throughout Aalto is a great benefit.  Various other Aalto
systems have the data available.  However, this varies per department:
each department can manage its data as it likes.  So, we can't make
general promises about what is available where.


Linux shell server mounts require a valid Kerberos ticket (usually
generated when you log in). On long sessions these might expire, and
you have to renew them with ``kinit`` to keep going.  If you get a
permission denied, try ``kinit``.

Virtual desktop interface
~~~~~~~~~~~~~~~~~~~~~~~~~

VDI, `vdi.aalto.fi <https://vdi.aalto.fi>`__, is a Linux workstation
accessible via your web browser, and useful for a lot of work.  It is
not Triton, but has scratch mounted at ``/m/triton/scratch/``.
Your work folder can be access at ``/m/triton/scratch/work/USERNAME``. For SCI departments the
standard paths you have on your workstations are also working ``/m/{cs,nbe}/{scratch,work}/``.

Shell servers
~~~~~~~~~~~~~

Departments have various shell servers, see below.  There isn't a
generally available shell server anymore.

NBE
~~~

On workstations, work directories are available at ``/m/nbe/work`` and group scratch
directories at ``/m/nbe/scratch/$project/``, including the shell
server ``amor.org.aalto.fi``.

PHYS
~~~~

Directories available on demand through SSHFS. See the `Data
transferring <https://wiki.aalto.fi/display/TFYintra/Data+transferring>`__ page
at PHYS wiki.

CS
~~

On workstations, work directories are available at ``/m/cs/work/``, and group scratch
directories at ``/m/cs/scratch/$project/``.  The department shell
server is ``magi.cs.aalto.fi`` and has these available.



Remote mounting
---------------

There are many ways to access Triton data remotely.  These days, we
recommending figuring out how to **mount** the data remotely, so that
it appears as local data but is accessed over the network.  This saves
copying data back and forth and is better for data security, but is
slower and less reliable than local data.

Remote mounting using SMB
~~~~~~~~~~~~~~~~~~~~~~~~~

By far, remote mounting of files is the easiest method to transfer files.  If you are
not on the Aalto networks (wired, ``eduroam``, or ``aalto`` with
Aalto-managed laptop), connect to the :doc:`Aalto VPN
</aalto/remoteaccess>` first.  Note that
this is automatically done on some department workstations (see
above) - if not, request it!

The scratch filesystem can be remote mounted using SMB inside secure
Aalto networks at the URLs

* scratch: ``smb://data.triton.aalto.fi/scratch/``.
* work: ``smb://data.triton.aalto.fi/work/$username/``.

On different operating systems:

* Linux (Ubuntu for example): File manager (Nautilus) → File →
  Connect to server.  Use the ``smb://`` URLs above.
* Windows 10: In the "File Explorer", go to "This PC" → "Computer"
  menu at the top → "Map Network Drive".  Use the URLs above but
  replace ``smb://`` with ``\\`` and ``/`` with ``\``.  For example,
  ``\\data.triton.aalto.fi\scratch\``.
* Mac: Finder → Go → Connect to Server.  Use the ``smb://`` URLs above.
* From Aalto managed computers, you can use ``lgw01.triton.aalto.fi``
  instead of ``data.triton.aalto.fi`` and it might auto-login.

Depending on your OS, you may need to use either your username
directly or ``AALTO\username``.

.. warning::

   In the future, you will only be able to do this from Aalto managed
   computers.  This remote mounting will really help your work, so we
   recommend you to request an Aalto managed computer (citing this
   section) to make your work as smooth as possible (or use
   vdi.aalto.fi, see below.

Remote mounting using SFTP (Linux and Mac)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use sftp and one of the shell servers to mount triton directly to your machine.
Easiest is to set up your ssh config (``.ssh/config``) on your machine as follows (replace ``USERNAME`` by your username):

::

    Host kosh
        User USERNAME
        Hostname kosh.aalto.fi
    	
    Host triton_via_kosh	
        User USERNAME
        Hostname triton.aalto.fi
        ProxyJump kosh    


Instead of ``kosh``, you can also use ``taltta`` or any other shell server (see :doc:`Remote Access <../../aalto/remoteaccess>`) as a proxy to jump the firewall.
You can now open a graphic file manager that supports the sftp protocol (e.g. Files on Aalto Linux), and open:

``sftp://triton_via_kosh``


which will direct you to the root folder of triton. To access scratch use:


``sftp://triton_via_kosh/scratch``


And to access your home folder use:

``sftp://triton_via_kosh/home/USERNAME``

Remote mounting using sshfs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sshfs`` is a neat program that lets you mount remote filesystems via
ssh only.  It is well-supported in Linux, and somewhat on other
operating systems.  Its true advantage is that you can mount any
remote ssh server - it doesn't have to be set up specially for SMB or
any other type of mounting.  On Ubuntu, you can mount by "File → Connect to
server" and using ``sftp://triton.aalto.fi/scratch/work/USERNAME``.
This also works from any shell server with data (see previous section).

The below uses command line programs to do the same, and makes the
``triton_work`` on your local computer access all files in
``/scratch/work/USERNAME``.  Can be done with other folders.::

    mkdir triton_work
    sshfs USERNAME@triton.aalto.fi:/scratch/work/USERNAME triton_work

Note that ``ssh`` binds together many ways of accessing Triton (and
other servers), with a
similar syntax and options.  Learning to use it well is a great
investment in your future.  Learn more about ssh on :doc:`the ssh
page </scicomp/ssh>`.

For Aalto Linux workstation users: it is recommended that you mount ``/scratch/``
under the local disk ``/l/``. You should be able to create the subfolder folder under ``/l/`` 
and point sshfs to that subfolder as in the example here above.



Transferring data
-----------------

This section tells ways you can copy data back-and-forth between
Triton and your own computers.  This may be more annoying for
day-to-day work but is better for transferring large data.

Using sftp
~~~~~~~~~~

The *SFTP* protocol uses ssh to transfer files.  On Linux and Mac, the
``sftp`` command line program are the must fundamental way to do this,
and are available everywhere.

A more user-friendly way of doing this (with a nice GUI) is the
`Filezilla program <https://filezilla-project.org/>`__. Make sure you are using
`Aalto VPN <https://www.aalto.fi/en/services/establishing-a-remote-connection-vpn-to-an-aalto-network>`__, then
you can put triton.aalto.fi as SFTP server with port 22.

Below is an example of the "raw" SFTP usage::

    # Copying from HOME to local PC
    user@pc123 $ sftp user12@triton.aalto.fi:filename
    Connected to triton.aalto.fi.
    Fetching /home/user12/filename to filename
    # copying to HOME
    user@pc123 $ sftp -b - user12@triton <<< 'put testCluster.m'
    sftp> put foo
    # copying to WRKDIR
    user@pc123 $ sftp -b - user12@triton:/scratch/work/USERNAME/ <<< 'put testCluster.m'
    ...

With all modern OS it is also possible to just open your OS file manager (e.g. Nautilus on Linux) and just put as address in the bar::

    sftp://triton.aalto.fi

If you are connecting from remote and cannot use the VPN, you can connect instead to department machines like kosh.aalto.fi, amor.org.aalto.fi (for NBE). The port is 22. *Note:* If you do not see your shared folder, you need to manually specify the full path (i.e. the folder is there, just not yet visible).

.. _rsync_data_transfer:

Using rsync
~~~~~~~~~~~

.. admonition:: Prerequisites

   To install rsync on windos please refer to :doc:`this guide </scicomp/rsynconwindows>`

Rsync is similar to sftp, but is smarter at restarting files.  Use rsync
for large file transfers.  ``rsync`` actually uses the ssh protocol so
you can ``rsync`` from anywhere you can ``ssh`` from. ``rsync`` is installed
by default on Linux and Mac terminals. On Windows machines we recommend using `GIT-bash <https://gitforwindows.org/>`__.

While there are better places on the internet to read about rsync, it is good
to try it out to sychronise a local folder on your triton's scratch. Sometimes
the issue with copying files is related to group permissions. This command takes
care of permissions and makes sure that all your local files are identical (= same
MD5 fingerprint) to your remote files::

    rsync -avzc -e "ssh" --chmod=g+s,g+rw --group=GROUPNAME PATHTOLOCALFOLDER USERNAME@triton.aalto.fi:/scratch/DEPT/PROJECTNAME/REMOTEFOLDER/

Replace the bits in CAPS with your own case. Briefly, ``-a`` tries to preserve all attributes of the file, ``-v`` increases verbosity to see what rsync is doing, ``-z`` uses compression, ``-c`` skips files that have identical MD5 checksum, ``-e`` specifies to use ssh (not necessary but needed for the commands coming after), ``--chmod`` sets the group permissions to shared (as common practice on scratch project folders), and ``--group`` sets the groupname to the group you belong to (note that GROUPNAME == PROJECTNAME on our scratch filesystem).

If you want to just check that your local files are different from the remote ones, you can run rsync in "dry run" so that you only see what the command would do, without actually doing anything.::

    rsync --dry-run -avzc ...

Sometimes you want to copy only certain files. E.g. go through all folders, consider only files ending with ``py``::

    rsync -avzc --include '*/' --include '*.py' --exclude '*' ...

Sometimes you want to copy only files under a certain size (e.g. 100MB)::

   rsync -avzc --max-size=100m ...

Rsync does NOT delete files by default, i.e. if you delete a file from the local folder, the remote file will not be deleted automatically, unless you specify the ``--delete`` option.

Please note that when working with files containing code or simple text, git is a better option to synchronise your local folder with your remote one, because not only it will keep the two folders in sycn, but you will also gain version controlling so that you can revert to previous version of your code, or txt/csv files.

Version control
~~~~~~~~~~~~~~~

Don't forget that you can use version control (git, etc.) for your
code and other small files.  This way, you transfer to/from Triton via
a version control server (Aalto Gitlab, Github, etc).  Often, one
would develop locally (committing often of course), pull on Triton, do
whatever some minor development directly on Triton to make it work
there, then push back to the server.



Exercises
---------

.. exercise:: RemoteData-1: Mounting your work directory

   Mount your work directory by SMB - and alternatively sftp or sshfs - and transfer a file to Triton.
   Note that you must be connected to the Aalto VPN (from outside campus), or on ``eduroam``, the ``aalto`` *with Aalto
   laptop* (from campus).

.. exercise:: (advanced) RemoteData-2: rsync

   If you have a Linux or Mac computer, study the ``rsync``
   manual page and try to transfer a file.



What's next?
------------

The next tutorial is about :doc:`interactive jobs <interactive>`.
