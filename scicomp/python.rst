======
Python
======

*Note* For triton specific instructions see
`triton python page </triton/apps/python>`.  For Aalto Linux workstation
specific stuff, see `Aalto python page </aalto/python>`.

Python is widely used high level programming language that is widely
used in many branches of science.

Python distributions
--------------------

+--------------------------+--------------------------+--------------------------+
|                          | Python to use            | How to install own       |
|                          |                          | packages                 |
+==========================+==========================+==========================+
| Simple programs with     | Anaconda 2/3             | ``pip install --user``   |
| common packages, not     |                          |                          |
| switching between        |                          |                          |
| Pythons often            |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Most of the use cases,   | Anaconda 2/3             | conda environment +      |
| but sometimes different  |                          | conda                    |
| versions of modules      |                          |                          |
| needed                   |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Special advanced cases.  | Python from module       | virtualenv + pip install |
|                          | system                   |                          |
+--------------------------+--------------------------+--------------------------+

There are two main versions of python: 2 and 3. There are also
different distributions: The "regular" CPython that is usually
provided with the operating system, Anaconda (a package containing
cpython + a lot of other scientific software all bundled togeter),
PyPy (a just-in-time compiler, which can be much faster for some use
cases).

-  For general scientific/data science use, we suggest that you use
   Anaconda. It comes with the most common scientific software included,
   and is reasonably optimized.
-  PyPy is still mainly for advanced use (it can be faster under certain
   cases, but does not work everywhere). It is available in a module.

Installing your own packages with "pip install" won't work unless you
have administrator access, since it tries to install globally for all
users. Instead, you have these options:

-  ``pip install --user``: install a package in your home directory
   (``~/.local/lib/pythonN.N/``). This is quick and effective, but if
   you start using multiple versions of Python, you will start having
   problems and the only recommendation will be to delete all modules
   and reinstall.
-  Virtual environments: these are self-contained python environment
   with all of its own modules, separate from any other. Thus, you can
   install any combination of modules you want, and this is most
   recommended.

   -  Anaconda: use conda, see below
   -  Normal Python: virtualenv + pip install, see below

Installing own packages: Virtualenv, conda, and pip
---------------------------------------------------

You often need to install your own packages. Python has its own package
manager system that can do this for you. There are three important
related concepts:

-  pip: the Python package installer. Installs Python packages globally,
   in a user's directory (``--user``), or anywhere. Installs from the
   `Python Package Index <https://pypi.org/>`__.
-  virtualenv: Creates a directory that has all self-contained packages
   that is manageable by the user themself. When the virtualenv is
   activated, all the operating-system global packages are no longer
   used. Instead, you install only the packages you want. This is
   important if you need to install specific versions of software, and
   also provides isolation from the rest of the system (so that you work
   can be uninterrupted). It also allows different projects to have
   different versions of things installed. virtualenv isn't magic, it
   could *almost* be seen as just manipulating PYTHONPATH, PATH, and the
   like. Docs: https://docs.python-guide.org/dev/virtualenvs/
-  conda: Sort of a combination of package manager and virtual
   environment. However, it *only* installed packages into environments,
   and is *not* limited to Python packages. It can also install other
   libraries (c, fortran, etc) into the environment. This is extremely
   useful for scientific computing, and the reason it was created. Docs
   for envs: https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html.

So, to install packages, there is pip and conda. To make virtual
environments, there is venv and conda.

Advanced users can see this `rosetta
stone <https://conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands>`__
for reference.


Anaconda
--------

`Anaconda <https://www.anaconda.com>`__ is a Python distribution by
Continuum Analytics. It is nothing fancy, they just take a lot of useful
scientific packages and put them all together, make sure they work, and
do some sort of optimization. They also include all of the libraries
needed. It is also all open source, and is packaged nicely so that it
can easily be installed on any major OS. Thus, for basic use, it is a
good base to start with. **virtualenv** does not work with Anaconda, use
conda instead.


Conda environments
~~~~~~~~~~~~~~~~~~

A conda environment lets you install all your own packages. For
instructions how to create, activate and deactivate conda envrionments
see http://conda.pydata.org/docs/using/envs.html .

A few notes about conda environments:

-  Once you use a conda environment, everything goes into it. Don't mix
   versions with, for example, local packages in your home dir.
   Eventually you'll get dependency problems.
-  Often the same goes for other python based modules. We have setup
   many modules that do use anaconda as a backend. So, if you know what
   you are doing this might work.
-  The commands below will fail:

   -  ``conda create -n foo pip`` # tries to use the global dir, use the
      ``--user`` flag instead

   -  ``conda create --prefix $WRKDIR/foo --clone root`` # will fail as our
      anaconda module has additional packages (e.g. via pip) installed.

Basic pip usage
---------------

pip install by itself won't work, because it tries to install globally.
Instead, use this:

::

    pip install --user

**Warning!** If you do this, then the module will be shared among all
your projects. It is quite likely that eventually, you will get some
incompatibilities between the Python you are using and the modules
installed. In that case, you are on your own (simple recommendation is
to remove all modules from ``~/.local/lib/pythonN.N`` and reinstall). **If
you get incompatible module errors, our first recommendation will be to
remove everything installed this way and not do it anymore.**

Python: virtualenv
------------------

Virtualenv is default-Python way of making environments, but does
**not** work with Anaconda.

::

    # Create environment
    virtualenv DIR

    # activate it (in each shell that uses it)
    source DIR/bin/activate 

    # install more things (e.g. ipython, etc.)
    pip install PACKAGE_NAME

    # deactivate the virtualenv
    deactivate

