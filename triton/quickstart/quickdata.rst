==============
Data on Triton
==============

This section gives an best practices data usage, access and transfer to and from triton.

.. admonition:: Prerequisites

      For data transfer, we assume that you have set up your system according to the 
      instructions above

Locations and Quotas
--------------------

.. include:: ../ref/storage.rst

Access to data and data transfer
--------------------------------

.. admonition:: Prerequisites

      On Windows systems, this guide assumes that you use `GIT-bash <https://gitforwindows.org/>`__,
      and have ``rsync`` installed according to :doc:`this guide<tut/rsynconwindows>` 

The folders available on triton are listed above. To copy small amounts of data to and from triton from outside the Aalto network,
you can either use scp or on linux/mac mount the file-system using sftp (e.g. ``sftp://triton_via_kosh``).

From inside the Aalto network, you can also mount the triton file system via smb:

  * scratch: ``smb://data.triton.aalto.fi/scratch/``.
  * work: ``smb://data.triton.aalto.fi/work/$username/``.

More details can be found :ref:`here<_remote_access_to_data>`

	
For larger files, or folders with multiple files, we suggest using rsync 

::
	# Copy PATHTOLOCALFOLDER to your triton home folder
	rsync -avzc -e "ssh" PATHTOLOCALFOLDER triton_via_kosh:/home/USERNAME/
	# Copy PATHTOTRITONFOLDER from your triton home folder to LOCALFOLDER
	rsync -avzc -e "ssh" triton_via_kosh:/home/USERNAME/PATHTOTRITONFOLDER LOCALFOLDER triton_via_kosh:/home/USERNAME/

For more details on rsync have a look :ref:`here <rsync_data_transfer>`.

Best Practices with data
------------------------

I/O can be a limiting factor when using the cluster. The probably most important factor 
limiting I/O speed on triton is file-sizes. The smaller the files the more inefficient their transfer.
When you run a job on triton and need to access many small files, we recommend to first pack them into
a large tarball:

::
     #To tar, and compress a folder use the following command
     tar -zcvf mytarball.tar.gz folder
     #To only bundle the data (e.g. if you want to avoid overhead by decompressing) a folder use the following command
     tar -cvf mytarball.tar folder

copy them over to the node where your code is executed and extract them there within the slurm script. 
If each input file is only used once, it's more efficient to load the tarball directly from the network drive
IF it fits into memory, load it into memory, if not, try to use a streaming input and have the required files 
in the tar-ball in the required order. 
For more information on storage and data usage on triton have a look at these documents:

   * :doc:`Small files<../usage/smallfiles>`
   * :doc:`Storage: Local Drives<../usage/localstorage>`
   * :doc:`Storage: Lustre<../usage/lustre>`
   * :doc:`Data Storage<../tut/storage/>`


