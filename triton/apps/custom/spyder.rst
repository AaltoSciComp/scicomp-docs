======
Spyder
======

Spyder is the Scientific PYthon Development
EnviRonment:\ https://pythonhosted.org/spyder/

This guide shows you how to set this up with different version of Qt4
and python compared to the default version provided by operating system.
Virtual environment makes this encapsulated from the rest of the
environment and thus you can install different versions of python
packages and also make the environment more portable.

Load pre-set environment modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    module load triton/python/2.7.6
    module load qt/4.8.6

Setup you virtualenv
~~~~~~~~~~~~~~~~~~~~

::

    mkdir -p /local/mhhakala/virtualenv && cd /local/mhhakala/virtualenv
    virtualenv spyder_env
    source spyder_env/bin/activate

Install SIP + PyQt to the virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # note, that we now have the virtualenv spyder_env activated
    # SIP/PyQt4 do not install with pip, so download first to some location
    tar zxf sip-4.16.7.tar.gz
    cd sip-4.16.7
    python configure.py
    make && make install

    tar zxf PyQt-x11-gpl-4.10.4.tar.gz
    cd PyQt-x11-gpl-4.10.4
    python configure.py
    make
    make install

Install spyder to the virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # still under activated spyder_env
    pip install spyder
