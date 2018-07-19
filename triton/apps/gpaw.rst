GPAW
~~~~

There is GPAW version installed in
GPAW/1.0.0-goolf-triton-2016a-Python-2.7.11. It has been compiled with
GCC, OpenBLAS and OpenMPI and it uses Python/2.7.11-goolf-triton-2016a
as its base Python. You can load it with::

    $ module load GPAW/1.0.0-goolf-triton-2016a-Python-2.7.11

You can create a virtual environment against the Python environment with::

    $ export VENV=/path/to/env
    $ virtualenv --system-site-packages $VENV
    $ cd $VENV
    $ source bin/activate
    # test installation
    $ python -c 'import gpaw; print gpaw'

GPAW site: https://wiki.fysik.dtu.dk/gpaw/
