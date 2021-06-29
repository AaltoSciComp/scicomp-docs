Gurobi Optimizer
================


`Gurobi Optimizer <https://www.gurobi.com/>`_ is a commercial optimizing library.

License
-------

Aalto University has a site-wide floating license for Gurobi.

You can create a ``gurobi.lic`` file in your home folder. The file should contain the following single line:

::
   
   TOKENSERVER=lic-gurobi.aalto.fi

You can create this license file with the following command on the login node::

  echo "TOKENSERVER=lic-gurobi.aalto.fi" > ~/gurobi.lic

The license is an Educational Institution Site License:

  Free Academic License Requirements, Gurobi Academic Licenses:
  Can only be used by faculty, students, or staff of a recognized
  degree-granting academic institution. Can be used for: Research or
  educational purposes. Consulting projects with industry – provided
  that approval from Gurobi has been granted.

Gurobi with Python
------------------

The default ``anaconda``-modules come with a pre-installed Gurobi installation.
By loading the module, ``$GUROBI_HOME``-variable is set to the installation
directory of the Anaconda-environment.

After setting the license, one can run, for example,
`mip1.py example <https://www.gurobi.com/documentation/9.1/quickstart_mac/cs_example_mip1_py.html>`_
from Gurobi's website::

  module load anaconda
  python $GUROBI_HOME/share/doc/gurobi/examples/python/mip1.py

Gurobi with Julia
-----------------

For Julia there exists a package called
`Gurobi.jl <https://github.com/jump-dev/Gurobi.jl>`_ that provides an interface
to Gurobi. This package needs Gurobi C libraries so that it can run. The
easiest way of obtaining these libraries is to load the ``anaconda``-module and
use the same libraries that the Python API uses.

To install Gurobi.jl, one can use the following commands::

  module load anaconda
  module load julia
  julia

After this, in the ``julia``-shell, install ``Gurobi.jl`` with:

.. code-block:: julia

  using Pkg
  Pkg.add("Gurobi")
  Pkg.build("Gurobi")a

  # Test installation
  using Gurobi
  Gurobi.Optimizer()

Before using the package do note the recommendations from
`Gurobi.jl' GitHub-page <https://github.com/jump-dev/Gurobi.jl>`_ regarding
the use of
`JuMP.jl <https://github.com/jump-dev/JuMP.jl>`_ and the reuse of environments.
