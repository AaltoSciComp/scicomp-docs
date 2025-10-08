Hello world in C
~~~~~~~~~~~~~~~~

Let's consider the following Hello world-program 
(:download:`hello.c</triton/examples/c/hello-world/hello.c>`)
written in C.

.. literalinclude:: /triton/examples/c/hello-world/hello.c
	 :language: c


After downloading it to a folder, we can compile it with Intel C compiler (``icx``).

First, let's load up Intel compilers module that ``icx`` will use in the background:

.. code-block:: bash

  module load triton/2025.1-intel intel-oneapi-compilers/2025.0.0

Now let's compile the code:

.. code-block:: bash

  icx -o hello hello.c

Now we can run the program:

.. code-block:: bash

  ./hello

This outputs the expected **Hello world**-string.
