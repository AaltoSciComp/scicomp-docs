.. list-table::
   :header-rows: 1

   * * Method
     * Description
     * From where?

   * * :ref:`ssh from Aalto networks <triton-connecting-ssh>`
     * Standard way of connecting via command line.  Hostname is
       ``triton.aalto.fi``.  :doc:`More SSH info </scicomp/ssh>`.

       >Linux/Mac/Win from command line: ``ssh USERNAME@triton.aalto.fi``

       >Windows: same, see :ref:`triton-connecting-ssh` for details
       options.

     * VPN and Aalto networks (which is VPN, most wired,
       internal servers, ``eduroam``, ``aalto`` *only* if using an
       Aalto-managed laptop, but *not* ``aalto open``).  **Simplest
       SSH option if you can use VPN.**

   * * :ref:`ssh (from rest of Internet) <triton-connecting-ssh>`

     * Use `Aalto VPN
       <https://www.aalto.fi/en/services/remote-connection-to-aaltos-network-vpn>`__
       and row above.

       If needed: same as above, but must set up SSH key and then ``ssh -J
       USERNAME@kosh.aalto.fi USERNAME@triton.aalto.fi``.

     * Whole Internet, if you *first* set up `SSH key AND
       also use passwords (since 2023)
       <https://aaltoscicomp.github.io/blog/2023/ssh-keys-with-passwords/>`__

   * * `VDI <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__
     * "Virtual desktop interface", https://vdi.aalto.fi, from there you can ``ssh``
       to Triton or access OOD.  `More info
       <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__.
     * Whole Internet

   * * :doc:`Open OnDemand </triton/usage/ood>`
     * https://ondemand.triton.aalto.fi, Web-based interface to the
       cluster. Also known as OOD. Includes shell access, GUI, data transfer, Jupyter and a number of GUI applications
       like Matlab etc.  :doc:`More info </triton/usage/ood>`.
     * Whole internet

   * * :doc:`Jupyter </triton/apps/jupyter>`
     * Since April 2024 Jupyter is part of Open OnDemand, see
       above. Use the "Jupyter" app to get same environment as
       before.  :doc:`More info </triton/apps/jupyter>`.
     * See Open OnDemand above

   * * :doc:`VS Code / Codium desktop </triton/apps/vscode>`
     * With the "Remote-SSH" extension it can provide shell access and
       file transfer.  Warnings: open only project directories (or it
       uses excessive CPU), and don't use large CPU/mem tasks with it
       (see warnings on the page).

     * Same as SSH options above above.
