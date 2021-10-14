==============
Data on Triton
==============

This section gives an best practices data usage, access and transfer to and from Triton.

.. admonition:: Prerequisites

      For data transfer, we assume that you have set up your system according to the 
      instructions in the :doc:`Quick guide<quickconnecting>`

Locations and quotas
--------------------

.. include:: ../ref/storage.rst

Access to data and data transfer
--------------------------------

.. admonition:: Prerequisites

      On Windows systems, this guide assumes that you use `GIT-bash <https://gitforwindows.org/>`__,
      and have ``rsync`` installed according to :doc:`this guide<tut/rsynconwindows>` 

Download data to Triton
~~~~~~~~~~~~~~~~~~~~~~~

To download a dataset directly to Triton you can use ``wget``

::
	
	wget https://url.to.som/file/on/a/server


If the data requires a login you can use:

::
	
	wget --user username --ask-password https://url.to.som/file/on/a/server
	
	
Downloading directly to Triton allows you to avoid the unnecessary network traffic and time required to first download it to your machine
and then transferring it over to Triton.

If you need to download a larger (>10GB) dataset to Triton from the internet please veryfy that the download acctually succeeded properly.

This can be done by comparing the md5 checksum, commonly provided by hosts along with the downloadable data. After downloadingsimply run:

::

	md5sum downloadedFileName

The resulting checksum has to be identical to the one listed online. If it is not, your data is most likely corrupted and should not be used.

For very large datasets (>100GB) you should check, whether they are already on Triton. The folder for these kinds of datasets is located at:
``/scratch/shareddata/dldata``, and if not, please contact the admins to have it added there. This avoids the same dataset being downloaded multiple 
times.


Copy data to and from Triton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The folders available on Triton are listed above. To copy small amounts of data to and from Triton from outside the Aalto network,
you can either use scp or on linux/mac mount the file-system using sftp (e.g. ``sftp://triton_via_kosh``).

From inside the Aalto network, you can also mount the Triton file system via smb:

  * scratch: ``smb://data.triton.aalto.fi/scratch/``.
  * work: ``smb://data.triton.aalto.fi/work/$username/``.

More details can be found :ref:`here<_remote_access_to_data>`
	
For larger files, or folders with multiple files and if the data is already on your machine, we suggest using rsync, 

::

	# Copy PATHTOLOCALFOLDER to your Triton home folder
	rsync -avzc -e "ssh" PATHTOLOCALFOLDER triton_via_kosh:/home/USERNAME/
	# Copy PATHTOTRITONFOLDER from your Triton home folder to LOCALFOLDER
	rsync -avzc -e "ssh" triton_via_kosh:/home/USERNAME/PATHTOTRITONFOLDER LOCALFOLDER triton_via_kosh:/home/USERNAME/

For more details on rsync have a look :ref:`here <rsync_data_transfer>`.



Best practices with data
------------------------

I/O can be a limiting factor when using the cluster. The probably most important factor 
limiting I/O speed on Triton is file-sizes. The smaller the files the more inefficient their transfer.
When you run a job on Triton and need to access many small files, we recommend to first pack them into
a large tarball:

::

     # To tar, and compress a folder use the following command
     tar -zcvf mytarball.tar.gz folder
     # To only bundle the data (e.g. if you want to avoid overhead by decompressing)
     # a folder use the following command
     tar -cvf mytarball.tar folder

copy them over to the node where your code is executed and extract them there within the slurm script or your code. 
::

   # copy it over
   cp mytarball.tar /tmp
   # and extract it locally
   tar -xf /tmp/mytarball.tar


If each input file is only used once, it's more efficient to load the tarball directly from the network drive
IF it fits into memory, load it into memory, if not, try to use a streaming input and have the required files 
in the tar-ball in the required order. 
For more information on storage and data usage on Triton have a look at these documents:

   * :doc:`Small files<../usage/smallfiles>`
   * :doc:`Storage: Local Drives<../usage/localstorage>`
   * :doc:`Storage: Lustre<../usage/lustre>`
   * :doc:`Data Storage<../tut/storage/>`


