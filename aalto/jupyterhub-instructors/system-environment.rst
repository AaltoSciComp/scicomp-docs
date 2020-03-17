System environment
==================

The following is the environment in each Jupyter notebook server
exists.  This is a normal Linux environment, and you are encouraged to
use the shell console to interact with it.  In fact, you will *need*
to use the console to do various things, and you will probably *need*
to do some scripting.

Why is everything not a push-button solution?  Everyone has such
unique needs, and we need to solve all of them.  We can only
accomplish our goals if people are able to - and do - do their own
scripting.



Linux container
---------------

Each time you launch your server, you get a personal Linux container.
Everything (except the data) gets reset each time it stops.  From the
user perspective, it looks like a normal Linux container.  Unlike some
setups, we allow students to acknowledge and browse the whole Linux
system.  (other systems try to hide it, but in reality they can't stop
students from accessing it).



Data
----

* ``/notebooks/`` is your per-user area.  It's what you see by
  default, and is shared among *all* your courses.

* ``/course/`` is the course directory (a `nbgrader concept
  <https://nbgrader.readthedocs.io/en/stable/user_guide/philosophy.html>`__).
  It is available only to instructors.  You need to read the nbgrader
  instructions to understand how this works.

* ``/coursedata/`` is an optional shared course data directory.
  Instructors can put files here so that students can access them
  without having to copy data over and over.  Instructors can write
  here, students can only read.  Remeber to make it readable to all
  students: ``chmod -R a+rX /coursedata``.

* ``/srv/nbgrader/exchange`` is the `exchange directory, a nbgrader
  concept
  <https://nbgrader.readthedocs.io/en/stable/user_guide/managing_assignment_files.html>`__
  but you generally don't have to worry about it yourself.


Data is available from outside JupyterHub: it is hosted on an
Aalto-wide server provided by Aalto.  Thus, you can access it on your
laptops, on Aalto public shell servers, and more.  A fast summary is
below, but see :doc:`../jupyterhub-data` for the main info.

* From your own laptop: The SMB server ``jhnas.org.aalto.fi`` path
  ``/vol/jupyter/{course,$username}``.

  * Linux: "Connect to server" from the file browser, URL
    ``smb://jhnas.org.aalto.fi/vol/jupyter``

  * Mac: same as Linux

  * Windows: ``\\jhnas.org.aalto.fi\vol\jupyter``.

* Data is available on public Aalto shell servers such as ``kosh`` and
  ``lyta``, at ``/m/jhnas/jupyter/``.



Software
--------

For Python, software is distributed through `conda
<https://anaconda.org/>`__.  You can install your own packages using
``pip`` or ``conda``, but *everything is reset when you restart the
server*.  This is sort of by design: a person can't permanently break
their own environment (restarting gets you to a good state), but you
have your own flexibility.

You *should* ask us to install common software which you are your
students need, instead of installing it yourself each time.  But you
should feel free to install it yourself to get your work done until
you do that.



Jupyter
-------

Both Jupyter Lab and classic notebooks are installed, along with a lot
of extensions.  If you need more extensions, let us know.  All courses
use only the classic notebook interface by default, because the
nbgrader web extensions do not work from Lab.
