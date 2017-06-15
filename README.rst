About Triton docs
=================

Requirements and building
~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx: Debian package ``python-sphinx``, : PyPI: ``python-sphinx``

Run ``make html``.


Editing
~~~~~~~

Example from UiT: `source <https://github.com/uit-no/hpc-doc>`_ and
`compiled HTML <http://hpc.uit.no/en/latest/>`_.

To add sections, add a new page in a subfolder.  Link it from the main
Table of Contents.


ReStructured text
~~~~~~~~~~~~~~~~~

ReStructured Text is similar to markdown in spirit, but has a more
strictly defined syntax, with more higher level structure.  This
allows more semantic markup.

Restructured text `home <http://docutils.sourceforge.net/rst.html>`_
and `quick reference
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.



``Inline code/monospace``, *emphasis*, **strong emphasis**

::

   ``Inline code/monospace``, *emphasis*, **strong emphasis**



Inline `link <http://python.org>`_, or anonymous__, or separate_
link.  Trailing underscores indicate links.

__ http://python.org

.. _separate: http://python.org

::

   Inline `link <http://python.org>`_, or anonymous__, or separate_
   link.  Trailing underscores indicate links.

    __ http://python.org

    .. _separate: http://python.org



::

   Block quote
   Block quote


::

   ::

     Block quote
     Block quote



Block quotes can also start with paragraph ending in double colon,
like this::

  Block quote

::

   Block quotes can also start with paragraph ending in double colon,
   like this::

       Block quote



`Permanent references across files <http://www.sphinx-doc.org/en/stable/markup/inline.html#role-ref>`_
