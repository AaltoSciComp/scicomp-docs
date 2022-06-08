Hello world in C
~~~~~~~~~~~~~~~~

Let's consider the following Hello world-program 
(:download:`hello.c</triton/examples/c/hello-world/hello.c>`)
written in C.

.. literalinclude:: /triton/examples/c/hello-world/hello.c
	 :language: c


After downloading it to a folder, we can compile it with GCC.

First, let's load up a GCC module:

.. code-block:: bash

  module load gcc/8.4.0

Secondly, let's compile the code:

.. code-block:: bash

  gcc -o hello hello.c

Now we can run the program:

.. code-block:: bash

  ./hello

This outputs the expected **Hello world**-string.
