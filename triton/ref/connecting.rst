.. list-table::
   :header-rows: 1

   * * Method
     * Description
     * From where?

   * * ssh
     * Standard way of connecting via command line.  Hostname is
       ``triton.aalto.fi``

       >Linux/Mac: ``ssh USERNAME@triton.aalto.fi``

       >Windows: WSL+Linux/mac command or use Powershell,
       which works very similar to linux shell.

     * Connections only from VPN and Aalto networks.
       ``kosh.aalto.fi`` is a good proxy host if you are not there:
       ``ssh -J USERNAME@kosh.aalto.fi USERNAME@triton.aalto.fi``

   * * VDI
     * "Virtual desktop interface", https://vdi.aalto.fi, from there you have to
       ``ssh`` to Triton (previous row) and can run graphical
       programs via SSH.
     * Whole internet

   * * Jupyter
     * https://jupyter.triton.aalto.fi provides the Jupyter interface
       directly on Triton (including command line).
     * Whole internet

   * * Open OnDemand
     * https://ood.triton.aalto.fi, Web-based interface to the
       cluster.  Includes shell access and data transfer.
     * VPN and Aalto networks
