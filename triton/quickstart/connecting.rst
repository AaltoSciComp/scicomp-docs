====================
Connecting to Triton
====================

Most of the information on this page is also available on other tutorial sites.
This page is essentially a condensed version of those sites, that will only give you a recipe
how to quickly set up your machine and the most important details. For more in-depth information,
please have a look at the linked pages for each section.

There are three suggested ways to connect to Triton, as detailed in the table below,
with more info found at :doc:`the connecting tutorial <../tut/connecting>`.

.. include:: ../ref/connecting.rst


Get an account
==============

First, you need to :doc:`get an account <../accounts>`.



Connecting via ssh
==================

.. admonition:: Prerequisites

      This section assumes that you have a basic understanding of the linux shell,
      you know know, what an ``ssh`` key is, that you have an ``ssh`` public/private
      key pair stored in the default location and that  you have some basic
      understanding of the ssh config. If you lack either of these,
      have a look at the following pages:

      * :doc:`Shell crash course </scicomp/shell>`
      * :doc:`Configuration and use of ssh </scicomp/ssh>`
      * :doc:`SSH fingerprints <../usage/ssh-fingerprints>`

Setting up ssh for passwordless access
--------------------------------------

The following guide shows you how to set up the ssh system to allow you to connect to Triton from either outside of
the Aalto network or from within using an ssh key instead of your password. In the following
guide ``USERNAME`` refers to your Aalto user name and ``~/.ssh`` refers to your ssh config folder.
(On Windows, you can use `GIT-bash <https://gitforwindows.org/>`__, which will allow
you to use linux style abbreviations. The actual folder is normally located under
``C:\Users\currentuser\.ssh``, where currentuser is the name of the user).
First, create the file ``config`` in the ``~/.ssh`` folder with the following content, or add
the following lines to it if it already exists. Instead of ``kosh`` you can also use any other
remote access server (see :doc:`Remote Access </aalto/remoteaccess>`)

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

Next, you have to add your public key to the authorized keys of both kosh and Triton.
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

Now you do the same for Triton by using our defined proxy jump over kosh.

::

    # Connect and log in to kosh
    ssh triton_via_kosh
    # Open the authorized_keys file and copy your public key.
    nano .ssh/authorized_keys
    # Copy your public key into this file
    # to save the file press ctrl + x and the confirm with y
    # afterwards exit from Triton
    exit


Now, to connect to Triton you can simply type:

::

    ssh triton
    # Or, if you are not on the aalto network:
    ssh triton_via_kosh
