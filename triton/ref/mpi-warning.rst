Some libraries/programs might have already existing requirement for a certain
MPI version. If so, use that version or ask for administrators to create
a version of the library with dependency on the MPI version you require.

.. warning::

   Different versions of MPI are not compatible with each other. Each
   version of MPI will create code that will run correctly with only
   that version of MPI. Thus if you create code with a certain version,
   you will need to load the same version of the library when you are
   running the code.

   Also, the MPI libraries are usually linked to slurm and network
   drivers. Thus, when slurm or driver versions are updated, some
   older versions of MPI might break. If you're still using said
   versions, let us know. If you're just starting a new project, it
   is recommended to use our recommended MPI libraries.
