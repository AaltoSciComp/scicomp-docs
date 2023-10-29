.. list-table::
   :header-rows: 1

   * * Method
     * Description
     * From where?

   * * ssh from Aalto networks
     * Standard way of connecting via command line.  Hostname is
       ``triton.aalto.fi``.  :doc:`More SSH info </scicomp/ssh>`.

       >Linux/Mac/Win from command line: ``ssh USERNAME@triton.aalto.fi``

       >Windows: same, see :ref:`triton-connecting-ssh` for details
       options.

     * VPN and Aalto networks (which is VPN, most wired,
       internal servers, ``eduroam``, ``aalto`` *only* if using an
       Aalto-managed laptop, but *not* ``aalto open``).  **Simplest
       SSH option if you can use VPN.**

   * * ssh (from rest of Internet)

     * Use `Aalto VPN
       <https://www.aalto.fi/en/services/remote-connection-to-aaltos-network-vpn>`__
       and row above.

       If needed: same as above, but must set up SSH key and then ``ssh -J
       USERNAME@kosh.aalto.fi USERNAME@triton.aalto.fi``.

     * Whole Internet, if you *first* set up `SSH key AND
       also use passwords (since 2023)
       <https://aaltoscicomp.github.io/blog/2023/ssh-keys-with-passwords/>`__

   * * VDI
     * "Virtual desktop interface", https://vdi.aalto.fi, from there you have to
       ``ssh`` to Triton (previous rows) and can run graphical
       programs via SSH.  `More info
       <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__.
     * Whole Internet

   * * Jupyter
     * https://jupyter.triton.aalto.fi provides the Jupyter interface
       directly on Triton (including command line).  Get a terminal
       with "New → Other → Terminal". :doc:`More info </triton/apps/jupyter>`.
     * Whole Internet

   * * Open OnDemand
     * https://ood.triton.aalto.fi, Web-based interface to the
       cluster.  Includes shell access and data transfer. "Triton
       Shell Access" for the terminal.  :doc:`More info </triton/usage/ood>`.
     * VPN and Aalto networks

   * * VSCode
     * Web-based available via OpenOnDemand (row above).

       Desktop-based "Remote
       SSH" allows running on Triton (which is OK, but don't use it
       for large computation).  :doc:`More info </triton/apps/vscode>`.
     * Same as Open OnDemand or SSH above
