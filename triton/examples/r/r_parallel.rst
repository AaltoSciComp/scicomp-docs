Parallel R example
------------------

:download:`r_parallel.slrm </triton/examples/r/r_parallel.slrm>`:

.. literalinclude:: /triton/examples/r/r_parallel.slrm

:download:`r_parallel.R </triton/examples/r/r_parallel.R>`:

.. literalinclude:: /triton/examples/r/r_parallel.R
  :language: r

When constrained to opt-architecture, run times for different core
numbers were

+-----------+-----------+-----------+-----------+----------+
| ncores    | 1         | 2         | 4         | 8        |
+===========+===========+===========+===========+==========+
| runtime   | 380.757   | 182.185   | 125.526   | 84.230   |
+-----------+-----------+-----------+-----------+----------+
