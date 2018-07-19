Paraview
========

As a module
------------

A serial version is available on login2. You will need to use the
"forward connection" strategy by using ssh port forwarding. For example,
run ``ssh -L BBBB:nnnNNN:AAAA username@triton``\ , where BBBB is the
server you connect to locally and nnnNNN is the node name and AAAA is
the port on that node. See `this FAQ question <faq-connecttoserveronnode>`.

See issue #13:
https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues/13 for some
user experiences. (Note: the author of this entry is not a paraview
expert, suggestions welcome.)

As a container
--------------

You can also use paraview via :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.  It is part of the
:doc:`openfoam` container.
