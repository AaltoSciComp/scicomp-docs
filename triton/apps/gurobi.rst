Gurobi Optimizer
================


`Gurobi Optimizer <https://www.gurobi.com/>`_ is a commercial optimizing library.

License
-------

Aalto University has a site-wide floating license for Gurobi.

.. admonition:: Important notes
   
   As of writing of this Guide, Aalto only has a valid license for Gurobi 9.X and older.
   Therefore Gurobi 10 cannot be run on triton unless you bring
   your own license.

Gurobi with Python
------------------

.. admonition:: Package names
   
   Unfortunately the python gurobi packages installed via pip and via conda come with
   two distinct package names ``gurobi`` for the conda package and ``gurobipy`` for 
   the pip package. Normally, we install the guobi package in the scicomp python environment, 
   but there are some conda modules which have the gurobipy package. So you might need
   to select the correct package.

.. admonition:: License Files for older modules
   
   Older modules on Triton might not have the GRB_LICENSE_FILE environment variable set 
   properly, so you might need to point to it manually. To do so, you need to create a 
   ``gurobi.lic`` file in your home folder. The file should contain the following single line:
    
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

After setting the license, one can run, for example::

   module load scicomp-python-env
   python 

And then run the following script

.. code-block:: python

  import gurobipy as gp 
  # Depending on your conda version you 
  # might need gurobi instead of gurobipy

  # Create a new model
  m = gp.Model()

  # Create variables
  x = m.addVar(vtype='B', name="x")
  y = m.addVar(vtype='B', name="y")
  z = m.addVar(vtype='B', name="z")

  # Set objective function
  m.setObjective(x + y + 2 * z, gp.GRB.MAXIMIZE)

  # Add constraints
  m.addConstr(x + 2 * y + 3 * z <= 4)
  m.addConstr(x + y >= 1)

  # Solve it!
  m.optimize()

  print(f"Optimal objective value: {m.objVal}")
  print(f"Solution values: x={x.X}, y={y.X}, z={z.X}")




Gurobi with Julia
-----------------

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

For Julia there exists a package called
`Gurobi.jl <https://github.com/jump-dev/Gurobi.jl>`_ that provides an interface
to Gurobi. This package needs Gurobi C libraries so that it can run. The
easiest way of obtaining these libraries is to load the ``scicomp-python-env``-module and
use the same libraries that the Python API uses.

To install Gurobi.jl, one can use the following commands::

  module load gurobi/9.5.2
  module load julia
  julia

After this, in the ``julia``-shell, install ``Gurobi.jl`` with:

.. code-block:: julia

  using Pkg
  Pkg.add("Gurobi")
  Pkg.build("Gurobi")

  # Test installation
  using Gurobi
  Gurobi.Optimizer()

Before using the package do note the recommendations from
`Gurobi.jl' GitHub-page <https://github.com/jump-dev/Gurobi.jl>`_ regarding
the use of
`JuMP.jl <https://github.com/jump-dev/JuMP.jl>`_ and the reuse of environments.


Gurobi with any other language supported by gurobi
--------------------------------------------------

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

For other languages supported by gurobi (like MATLAB, R or C/C++) use

  module load gurobi/9.5.2
  
to load gurobi version 9.5.2 and then follow the instructions from the gurobi 
web-page. All global variables necessary for gurobi are already set, so you 
don't need any further configuration


