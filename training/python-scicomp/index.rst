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
   l[1] = True                        # list elements can be any type
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


Organizing Python code
----------------------

Start Python scripts with

::

   #!/usr/bin/env python3

This ensures you get the correct python3 for the environment you are
using.

In general, don't put executable statements directly into the top
level scope in your files (modules), as this code is then run if you
try to import the module.

Instead, use this common idiom:

::

   if __name__ == '__main__':
       # your code goes here


Exercise 1.1
------------

Who needs numpy anyway? Implement matrix multiplication with nested
lists as your matrix representation. *Hint for beginners*: Create one
function

::

   def creatematrix(n, m):
       # ...

which creates an NxM matrix filled with random values
(e.g. random.random()). Then create another function

::

   def matrixmult(a, b):
       # ...

which multiplies together two matrices a and b.


Exercies 1.2
------------

Lets continue with the previous example, and add some object oriented
scaffolding around our matrix code.  Create a Matrix class with a
constructor to create the random matrix, and overload the '*' operator
to multiply two Matrix instances. Reuse the code from the previous
exercise.


Exercise 1.3
------------

The essence of science is experiment and measurement.  So lets measure
our matrix multiplication implementation, and calculate how fast it
can multiply matrices, in terms of "Gflops/s" (Giga floating point
operations per second). *Hint*: A "flop" is a floating point multiply
or addition/subtraction.  First figure out of many flops are needed to
multiply two matrices. Then you need to time it; for this you can use
the IPython magic %timeit command. And finally, equipped with this
information, you can calculate a Gflops/s score for you multiplication
method.


Enter NumPy
===========

Introduction
------------

The NumPy package provides a N-dimensional array type, and syntax and
utility functions for working with these arrays.

In contrast to a python list, a numpy array can only hold elements of
the same type. The element type can be seen via the 'dtype' attribute.

::

   import numpy as np
   a = np.array(((1,2,3),(4,5,6)))
   a.dtype
   a[0, 0] = "hello"  # error!
   a[0, 0] = 2**100    # error!

What these restrictions buy you is that the memory layout of a numpy
array is very efficient, similar to what you see in low level
languages like C or Fortran.  This means operating on these arrays is
very efficient; in fact, much of the speed advantage of numpy comes
from the fact that array syntax is implemented in fast C code.

Due to the memory layout of numpy being compatible with C and Fortran,
numpy arrays allows one to use functionality written in these other
languages.  Much of the SciPy ecosystem (NumPy, SciPy, etc.) consist
of python wrappers around widely used and battle-tested numerical
libraries written in C or Fortran such as LAPACK and BLAS.

The Python list

::

   a_list = [1, "hello", 1.2]

has roughly the following layout in memory:

.. image:: a_list.svg

In contrast, the NumPy array

::

   n = np.array((1,2,3))

has the memory layout like

.. image:: ndarray.svg

Exercise 2.1
------------

1. In the example above we saw that ``2**100`` was too large. What is
   the default datatype of a numpy integer array if we don't
   explicitly specify some type, and what is the largest possible
   integer we can store in such na element.

2. What is the smallest negative element (that is, the largest
   absolute value of a negative number)?  Is it different from the
   largest positive number, and if so, why?

3. What is the absolute value of the smallest negative element? Why?


Other ways of creating NumPy arrays
-----------------------------------

There are many different ways to create NumPy arrays, here's a few of
the most common ones:

::

   np.zeros((2, 3))      # 2x3 array with all elements 0
   np.ones((3, 2), bool) # 3x2 boolean array
   np.arange(3)          # Evenly spaced values in an interval
   np.linspace(..)       # similar to above

NumPy array slicing syntax
--------------------------

NumPy provides a convenient array syntax to reference subarrays,
similar to MATLAB for Fortran.

::

   a[low:high:step]

returns the array elements in the range ``[low, high)`` with a stride
of ``step``. Equivalently for multidimensional arrays.  For
multidimensional arrays NumPy by default stores arrays in row-major
order, like C. Note that this is in contrast to e.g. Fortran, MATLAB
or Julia that use a column-major layout.

Using array syntax efficiently is **key** to using NumPy in a fashion
that leads to short as well as efficient code.

NumPy also provides so-called *advanced indexing*, where you can
select elements with a list of indices.

::

   a = np.zeros((3, 3))
   b = a[(0, 1), (1, 1)]
   b[0] = 1    # Will this modify a?


Views vs. copies
----------------

When slicing an array, you **DO NOT** get a copy of those elements,
but rather a *view*.  That is, the data elements are the same as in
the original array

::

   a = np.ones((2, 2))
   b = a[1, 1:2]
   b[0] = 2

Views rather than copies is more efficient, particularly for large
arrays, but they can sometimes be confusing. Be careful!

If you do need a copy, NumPy arrays have a ``copy`` method to create a
copy rather than getting a view.

**NOTE** With advanced indexing, you always get a copy!


Array shape and size
--------------------

NumPy arrays have a shape and size attribute.

::

   a = np.zeros((2,3))
   a.size               # Number of elements
   a.shape              # shape tuple

We can modify the shape of an array with the ``reshape`` or ``resize``
methods. Or for the special case of flattening an array to a 1D array,
``ravel``.

Combining, splitting and rolling arrays
---------------------------------------

For combining multiple arrays into a larger array, see the
``concatenate``, ``stack``, ``block``, and the more specialized
variants ``hstack``, ``vstack``, ``dstack``.

Similarly, for splitting an array into multiple parts, there's
``split``, ``hsplit``, ``vsplit``.

To roll an array, that is shift the elements along a give axis, use
``roll``.


Exercise 2.2
------------

Create an array ``x`` of 100 evenly spaced numbers in the range
[-2*pi, 2*pi].

Next, create an array ``y``, where each element is the ``sin`` of each
element in the previously created array.

Then, figure out the indices where the array ``y`` changes sign. What
are the ``x`` values for these indices?


NumPy I/O
---------

NumPy has functionality for saving and loading NumPy arrays from
files.  For reading/writing textfiles there is ``loadtxt`` and
``savetxt``. See also ``genfromtxt`` with more sophisticated handling
of missing values etc.

For large arrays, it's faster to use a binary format. For these NumPy
defines a ``.npy`` format. Loading and saving these files can be done
with the ``load`` and ``save`` methods.  There's also the ``.npz``
format, which is a zip archive containing several numpy ndarrays in
one file. ``.npz`` format files can be read/written with ``load``,
``savez`` and ``savez_compressed`` methods. This is a good choice for
temporary or intermediate files such as checkpoints etc. Note that the
format is Numpy-specific, and other languages might not easily be able
to read it. Similarly, for long-term archiving other formats might be
a better choice.


Random Numbers in NumPy
-----------------------

The ``numpy.random`` module contains functionality to create
pseudorandom numbers following different distributions.

Linear algebra in Numpy
-----------------------

The ``dot`` method provides a generalized dot product. It can compute
dot products of 1D vectors, matrix-vector products as well as
matrix-matrix products.  It is an interface to the famous BLAS
library, of which multiple highly optimized versions exist.  The
``numpy.linalg`` module contains interfaces to the most common linear
algebra operations, such as calculating eigenvalues, Cholesky and
singular value decompositions, solving linear systems, least squares,
(pseudo)inverse. This module is an interface to the LAPACK library
(which in turn builds on top of BLAS).

Exercise 2.3
------------

Remember our first exercise, implementing matrix multiplication? Now
do the same, but use NumPy arrays and the ``dot`` method. Compare
performance to the code you wrote yourself earlier, using the IPython
%timeit macro.


SciPy
=====

SciPy is a library that builds on top of NumPy. It contains a lot of
interfaces to battle-tested numerical routines written in Fortran or
C, as well as python implementations of many common
algorithms. Briefly, it contains functionality for

- Special functions (Bessel, Gamma, etc.)
- Numerical integration
- Optimization
- Interpolation
- Fast Fourier Transform (FFT)
- Linear algebra (more complete than in NumPy)
- Sparse matrices
- Statistics
- More I/O routine, e.g. Matrix Market format for sparse matrices,
  MATLAB files (.mat), etc.


Matplotlib
==========


Homework
========

XY model?
