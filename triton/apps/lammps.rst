======
Lammps
======

:supportlevel: C
:pagelastupdated: 2014


`http://lammps.sandia.gov/ <http://lammps.sandia.gov/doc/Section_start.html#start_5>`__

Building LAMMPS as a library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    cd src
    # default g++ compilation with system g++
    module load openmpi/1.8.1-gcc
    make -f Makefile.lib serial
