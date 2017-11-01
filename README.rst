================
About these docs
================

Requirements and building
~~~~~~~~~~~~~~~~~~~~~~~~~

The only software needed is Sphinx: Debian package
``python-sphinx``, : PyPI: ``python-sphinx``.  It is already installed
on Aalto workstations.

To build the docs, run ``make html``.

HTML output is in ``_build/html/index.html``, and other output formats
are available as well.


Editing
~~~~~~~

Look at examples and copy.  To add sections, add a new page in a
subfolder.  Link it from the main Table of Contents (``toctree``) in
``index.rst`` to have the document appear and be cross-referenced.

You can see a complete example from UiT: `source
<https://github.com/uit-no/hpc-doc>`_ and `compiled HTML
<http://hpc.uit.no/en/latest/>`_.



ReStructured text
~~~~~~~~~~~~~~~~~

ReStructured Text is similar to markdown in spirit, but has a more
strictly defined syntax, with more higher level structure.  This
allows more semantic markup, more power to compile into different
formats, and advanced things like indexing, permanent references, etc.

Restructured text `home <http://docutils.sourceforge.net/rst.html>`_
and `quick reference
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.

A very quick guide is below.

----

``Inline code/monospace``, *emphasis*, **strong emphasis**

::

   ``Inline code/monospace``, *emphasis*, **strong emphasis**

----

Inline `link <http://python.org>`_, or anonymous__, or separate_
`+different text <separate_>`_ links.  Trailing underscores indicate
links.

__ http://python.org

.. _separate: http://python.org

::

    Inline `link <http://python.org>`_, or anonymous__, or separate_
    (`or different text <separate_>`_ links).  Trailing underscores indicate
    links.

    __ http://python.org

    .. _separate: http://python.org

----

Linking to the web.  If possible use a permanent reference (next
section), but you can also refer to specific files by name.  Note,
that for internal links there are no trailing underscores::

  :doc:`../tut/interactive.rst`  (recommended)
  `../tut/interactive.rst`       (short, no warning if link breaks)

  With different text:
  :doc:`Text <../tut/interactive.rst>`  (recommended)
  `Text <../tut/interactive.rst>`       (short, no warning if link breaks)


----

Internal links.  `Permanent references across files <http://www.sphinx-doc.org/en/stable/markup/inline.html#role-ref>`_

Label things this way (note only one colon)::

  .. _label-name:

Reference them this way::

  :ref:`label-name`     (recommended)
  `label-name`          (short, no warning if link breaks)
  `Text <label-name>`   (short, no warning if link breaks)

----

::

   Block quote
   Block quote


::

   ::

     Block quote
     Block quote

----

Block quotes can also start with paragraph ending in double colon,
like this::

  Block quote

::

   Block quotes can also start with paragraph ending in double colon,
   like this::

       Block quote

----

Notes, warnings, etc.

.. note::

   This is a note

.. warning::

   This is a warning

::

  .. note::

    This is a note

  .. warning::

    This is a warning
