Remote access to data
=====================

.. seealso::

   :doc:`/aalto/remoteaccess`


From Aalto networks (or VPN), you can mount many of the filesystems via
SMB. To use this well, you want to get the VPN set up first like
mentioned above. (You can also access these filesystems via ssh through
the shell servers):

.. tabs::

  .. group-tab:: Windows

    - In all cases, username=aalto username, domain=AALTO,
      password=Aalto password.
    - For NBE/PHYS, replace ``tw-cs`` with ``tw-nbe`` or ``tw-phys``.
    - **Home** directories: ``\\home.org.aalto.fi\``
    - **Project** directories: ``\\tw-cs.org.aalto.fi\project\$name\``
      (``$name``\ =project name)
    - **Archive** directories: ``\\tw-cs.org.aalto.fi\archive\$name\``
      (``$name``\ =project name)
    - **Scratch directories**, see :doc:`Triton storage
      <../triton/tut/remotedata>`.
    - ``\\work.org.aalto.fi\`` for **Aalto work** directories (different
      than Triton ``work``).

    To access these folders:  To do the mounting, Windows Explorer → Computer → Map network drive →
    select a free letter.

  .. group-tab:: Mac

    - In all cases, username=aalto username, domain=AALTO,
      password=Aalto password.
    - For NBE/PHYS, replace ``tw-cs`` with ``tw-nbe`` or ``tw-phys``.
    - **Home** directories: ``smb://home.org.aalto.fi/``
    - **Project** directories: ``smb://tw-cs.org.aalto.fi/project/$name/``
      (``$name``\ =project name)
    - **Archive** directories: ``smb://tw-cs.org.aalto.fi/archive/$name/``
      (``$name``\ =project name)
    - **Scratch directories**, see :doc:`Triton storage
      <../triton/tut/remotedata>`.
    - ``smb://work.org.aalto.fi`` for **Aalto work** directories (different
      than Triton ``work``).

    To access these folders: Finder → Go menu item → Connect to server → use the URLs
    above.

  .. group-tab:: Linux

    - In all cases, username=aalto username, domain=AALTO,
      password=Aalto password.
    - For NBE/PHYS, replace ``tw-cs`` with ``tw-nbe`` or ``tw-phys``.
    - **Home** directories: ``smb://home.org.aalto.fi/``
    - **Project** directories: ``smb://tw-cs.org.aalto.fi/project/$name/``
      (``$name``\ =project name)
    - **Archive** directories: ``smb://tw-cs.org.aalto.fi/archive/$name/``
      (``$name``\ =project name)
    - **Scratch directories**, see :doc:`Triton storage
      <../triton/tut/remotedata>`.
    - ``smb://work.org.aalto.fi`` for **Aalto work** directories (different
      than Triton ``work``).

    To access these folders: Files → Left sidebar → Connect to server → use the URLs above.
    For other Linuxes, you can probably figure it out.  (It varies
    depending on operating system, look around in the finder)

.. warning:: Must use VPN or Aalto network.

   Remember that you must connect to the Aalto VPN first, unless you are
   on an *Aalto laptop* on the ``aalto`` network.
