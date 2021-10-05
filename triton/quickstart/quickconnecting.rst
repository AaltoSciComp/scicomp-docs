Most of the information on this page is also available on other tutorial sites. 
This page is essentially a condensed version of those sites, that will only give you a recipe 
how to quickly set up your machine and the most important details. For more in-depth information
please have a look at the linked pages for each section


Connecting to Triton
====================

There are three suggested ways to connect to triton, as detailed in the table below.
With more info found at :doc:` the connecting Tutorial<tut/connecting>`

.. list-table::
    :header-rows: 1

    * * Method
      * About
      * From where?
    * * ssh
      * Works everywhere, from everywhere.  Firewalls may make things
	hard sometimes.
      * Aalto networks only, otherwise ssh to kosh and then Triton
    * * https://jupyter.triton.aalto.fi
      * Jupyter interface, but provides shell access via web browser.
      * Whole internet
    * * https://vdi.aalto.fi
      * Virtual desktop, from there you have to ``ssh`` to Triton
	anyway but gets you past firewalls and can run graphical
	programs via SSH.
      * Whole internet


Connecting via ssh
==================

.. admonition:: Prerequisites

      This section assumes that you have a basic understanding of the linux shell, 
      you know know, what an ``ssh`` key is, that you have an ``ssh`` public/private
      key pair stored in the default location and that  you have some basic 
      understanding of the ssh config. If you lack either of these,
      have a look at the following pages:  
      
      * :doc:`Shell crash course </scicomp/shell>`  
      * :doc:`Configuration and use of ``ssh``<../scicomp/ssh>`  
      * :doc:`SSH fingerprints <usage/ssh-fingerprints>` 

Setting up ssh for passwordfree access
--------------------------------------

The following guide shows you how to set up the ssh system to allow you to connect to triton from either outside of 
the aalto network or from within using an ssh key instead of your password. In the following 
guide ``USERNAME`` refers to your Aalto user name and ``~/.ssh`` refers to your ssh config folder. 
(On Windows, you can use `GIT-bash <https://gitforwindows.org/>`__, which will allow
you to use linux style abbreviations. The actual folder is normally located under 
``C:\Users\currentuser\.ssh``, where currentuser is the name of the user).
First, create the file ``config`` in the ``~/.ssh`` folder with the following content, or add 
the following lines to it if it already exists. Instead of ``kosh`` you can also use any other 
remote access server (see :doc:`Remote Access <../aalto/remoteaccess>`)

::

    Host triton
        User USERNAME
        Hostname triton.aalto.fi
        
    Host kosh
        User USERNAME
        Hostname kosh.aalto.fi

    	
    Host triton_via_kosh	
        User USERNAME
        Hostname triton
        ProxyJump kosh    

Next, you have to add your public key to the authorized keys of both kosh and triton. 
For this purpose you have to connect to the respective servers and add your public key to 
the ``authorized_keys`` file in the servers ``.ssh/`` folder.

::
# Connect and log in to kosh
ssh kosh
# Open the authorized_keys file and copy your public key.
nano .ssh/authorized_keys
# Copy your public key into this file
# to save the file press ctrl + x and the confirm with y
# afterwards exit from kosh
exit

Now you do the same for triton by using our defined proxy jump over kosh.

::
# Connect and log in to kosh
ssh triton_via_kosh
# Open the authorized_keys file and copy your public key.
nano .ssh/authorized_keys
# Copy your public key into this file
# to save the file press ctrl + x and the confirm with y
# afterwards exit from triton
exit


Now, to connect to triton you can simply type:

::

    ssh triton
    # Or, if you are not on the aalto network:
    ssh triton_via_kosh


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

Linux / Mac:

For small individual files, you can simply use ``scp`` to copy them over to triton, 
or copy things from triton to your machine. For the following commands, replace ``triton_via_kosh``
by ``triton`` if you are within the aalto network.

::
	# To copy to your home folder:
	scp fileName.ext triton_via_kosh:/home/USERNAME/
	# To copy to your work folder:
	scp fileName.ext triton_via_kosh:/scratch/work/USERNAME/
	# To copy from your work folder:
	scp triton_via_kosh:/scratch/work/USERNAME/fileName.ext localFolder

Alternatively, you can also use e.g. files on ubuntu and simply mount tryton by typing in:
::
	sftp://triton_via_kosh
	
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


