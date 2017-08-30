========
Python 2
========

Scientific Python
=================

The full `SciPy Stack <https://www.scipy.org/stackspec.html>`__
containing the base scientific python packages are available via the
'anaconda' modules. If you want to use Python 2.7, please load the
anaconda2 module

::

    module load anaconda2

And if you wish to use Python 3.x (currently 3.5) use the anaconda3
module

::

    module load anaconda3

The numpy provided by anaconda uses OpenBLAS so it's fast.

Note that the Anaconda distribution comes with its own python
interpreter, so instead of starting your scripts with

::

    #!/usr/bin/python

(or python3 for Python 3.x) you should instead use

::

    #!/usr/bin/env python

for Python 2.7 and

::

    #!/usr/bin/env python3

for Python 3.x

Conda Forge
-----------

There exists a project `Conda-Forge <https://conda-forge.github.io/>`__
providing extra packages not included in the standard conda repository.
A list of current packages can be seen here: `Conda-Forge
feedstocks <https://conda-forge.github.io/feedstocks.html>`__ . If you
need any of these packages, let the admin know and we'll install them.

Extra packages
--------------

Extra packages installed via conda (if available), conda-forge or with
"pip install". If you want some package that is currently not installed,
you can search with 'conda search NAME' or 'pip search NAME', or look at
the list of package in conda-forge at the link above. If you find what
you want, just file an issue at the issue tracker asking for it to be
installed.

**Admins ohoi:** The script at
/share/apps/anaconda/install-extra-packages.sh installs the extra
packages. Whenever somebody asks for a new package to be added to
anaconda, please add it there. And also, after installing a new anaconda
version, run the script so that all the extra packages are installed.


