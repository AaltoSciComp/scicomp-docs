.. list-table::
   :header-rows: 1

   * * Method
     * Description
     * From where?

   * * ssh from Aalto networks
     * Standard way of connecting via command line.  Hostname is
       ``triton.aalto.fi``.  :doc:`More info </scicomp/ssh>`, both
       `SSH keys and passwords are required since 2023 <https://aaltoscicomp.github.io/blog/2023/ssh-keys-with-passwords/>`__.

       >Linux/Mac/Win from command line: ``ssh USERNAME@triton.aalto.fi``

       >Windows: same, see :ref:`triton-connecting-ssh` for details
       options.

     * Connections from Aalto networks (VPN, most wired,
       internal servers, ``eduroam``, ``aalto`` *only* if using an
       Aalto-managed laptop, but *not* ``aalto open``).  **Simplest
       SSH option if you can use VPNVPN.**

   * * ssh (from rest of Internet)

     * Same as above, but must set up SSH key and then ``ssh -J
       USERNAME@kosh.aalto.fi USERNAME@triton.aalto.fi``

     * From the rest of the Internet: must have *both* `SSH key AND
       password set up
       <https://aaltoscicomp.github.io/blog/2023/ssh-keys-with-passwords/>`__

   * * VDI
     * "Virtual desktop interface", https://vdi.aalto.fi, from there you have to
       ``ssh`` to Triton (previous row) and can run graphical
       programs via SSH.  `More info
       <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__.
     * Whole internet

   * * Jupyter
     * https://jupyter.triton.aalto.fi provides the Jupyter interface
       directly on Triton (including command line).  Get a terminal
       with "New → Other → Terminal". :doc:`More info </triton/apps/jupyter>`.
     * Whole internet

   * * Open OnDemand
     * https://ood.triton.aalto.fi, Web-based interface to the
       cluster.  Includes shell access and data transfer. "Triton
       Shell Access" for the terminal.  :doc:`More info </triton/usage/ood>`.
     * VPN and Aalto networks

   * * VSCode
     * Available via OpenOnDemand (row above).  Desktop-based "Remote
       SSH" allows running on Triton (which is OK, but don't use it
       for large computation).  :doc:`More info </triton/apps/vscode>`.
     * Same as SSH above
