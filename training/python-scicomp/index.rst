===============================
Python for Scientific Computing
===============================

Abstract
========

Python is a modern, object-oriented programming language, which has
become popular in several areas of software development. This course
discusses how Python can be utilized in scientific computing. The
course starts by introducing the main Python package for numerical
computing, NumPy, and discusses then SciPy toolbox for various
scientific computing tasks as well as visualization with the
Matplotlib package.


Motivation
==========

Why Python
----------

Python has become popular, largely due to good reasons. It's very easy
to get started, there's lots of educational material, a huge amount of
libraries for doing everything imaginable.  Particularly in the
scientific computing space, there is the Numpy, Scipy, and matplotlib
libraries which form the basis of almost everything.  Numpy and Scipy
are excellent examples of using Python as a glue language, meaning to
glue together battle-tested and well performing code and present them
with an easy to use interface.  Also machine learning and deep
learning frameworks have embraced python as the glue language of
choice.  And finally, Python is open source, meaning that anybody can
download and install it on their computer, without having to bother
with acquiring a license or such.  This makes it easier to distribute
your code e.g. to collaborators in different universities.


Why not Python for Scientific Computing
---------------------------------------

While Python is extremely popular in scientific computing today, there
are certainly things better left to other tools.

- Implementing performance-critical kernels.  Python is a **very**
  slow language, which often doesn't matter if you can offload the
  heavy lifting to fast compiled code, e.g. by using Numpy array
  operations.  But if what you're trying to do isn't *vectorizable*
  then you're out of luck.  And alternative to Python, albeit much
  less mature and with a smaller ecosystem, but which provides a very
  fast generated code, is *Julia*.

- Creating libraries that can be called from other languages.  In this
  case you'll often want to create a library with a C interface, which
  can then be called from most languages.  Suitable languages for this
  sort of task, depending on what you are doing, could be Rust, C,
  C++, or Fortran.

- You really like static typing, or functional programming
  approaches. *Haskell* might be what you're looking for.


Python 2 vs Python 3
--------------------

There are two slightly incompatible versions of Python being used
today, 2 and 3.  Most large projects have supported 3 for a long time
already, and have announced dropping Python 2 support for future
versions (or have already done so), so at this point you should use
version 3 unless you're working on an existing project that for some
reason hasn't yet been ported to version 3.  Accordingly, in this
course we will use Python 3. For more info, see `Python 3
statement <https://python3statement.org/>`_ by many other the major
projects.


Practical details
=================

The instructor will use the ``anaconda3/latest`` module available on
triton.  However, if you have Python 3 with the usual scientific
libraries installed locally on your laptop, you should be able to use
that as well, if you prefer.

For interactively testing things in Python, you can use a Jupyter
notebook, or the ``ipython`` shell.  For writing Python code you will
need a text editor; Jupyter Lab does have one, if you prefer to work
in a browser based environment.

You're not expected to know much Python at the start of the course,
but a little bit of programming proficiency is needed as a
prerequisite.

The course focuses on hands-on exercises rather than lectures.


Introduction to Python
======================

If you are not familiar with Python, a short introduction to the most
common python builtin datatypes:

Scalars
-------

Scalar types, that is, single elements of various types:

::

   i = 42       # integer
   i = 2**77    # Integers are arbitrary precision
   g = 3.14     # floating point number
   c = 2 - 3j   # Complex number
   b = True     # boolean
   s = "Hello!" # String (Unicode)
   q = b'Hello' # bytes (8-bit values)


Collections
-----------

Collections are data structures capable of storing multiple values.

::

   l = [1, 2, 3]                      # list
   l[1]                               # lists are indexed by int
   d = {"Janne": 123, "Richard": 456} # dictionary
   d["Janne"]
   s = set()                          # Set of unique values


Python type system
------------------

Python is strongly and dynamically typed.

Strong here means, roughly, that it's not possible to circumvent the
type system (at least, not easily, and not without invoking undefined
behavior).

::

   x = 42
   type(x)
   x + "hello"

Dynamic typing means that types are determined at runtime, and a
variable can be redefined to refer to an instance of another type:

::

   x = 42
   x = "hello"


*Jargon*: Types are associated with rvalues, not lvalues. In
statically typed language, types are associated with lvalues, and are
(typically) reified during compilation.


Exercise 1
----------

Why needs numpy anyway? Implement matrix mult with nested lists as
your matrix representation.
