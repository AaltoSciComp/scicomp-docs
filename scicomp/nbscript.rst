nbscript: run notebooks as scripts
==================================

.. highlight:: python

.. warning:: This page and nbscript are under active development.



Notebooks as scripts?
---------------------

Jupyter is good for interactive work and exploration, but eventually
you need more resources than an interactive session can provide.
**nbscript** is a tool (written by us) that lets you run Jupyter
notebooks just like you would Python files. (`nbscript main site
<https://github.com/NordicHPC/nbscript>`__)

.. seealso::

   **Other tools:** There are other tools that run notebooks
   non-interactively, but (in my opinion) they treat command-line
   execution as an afterthought.  There is a long-standing standard for running
   scripts on UNIX-like systems, and if you don't use that, you are
   staying locked in to Jupyter stuff: the two worlds should be
   connected seamlessly.  `Links to more tools here
   <https://github.com/NordicHPC/nbscript#see-also>`__.

Once you start running notebooks as scripts, you really need to think
about how modular your whole workflow is.  Mainly, think about
dividing your work into separate preprocessing ("easy"), analysis
("takes lots of time and memory"), and visualization/post processing
("easy") stages.  Only the analysis phase needs to be run
non-interactively at first (to take advantage of more resources or
parallelize), but other parts can still be done interactively through
Jupyter.  You also need to design the analysis part so that it can run
on a small amount of data for development and debugging, and the whole
data for the actual processing.  You can read more general advice at
:doc:`Jupyter notebook pitfalls <jupyter-pitfalls>`.



nbscript basics
---------------

.. highlight:: console

The idea is ``nbscript input.ipynb`` has exactly the same kind of
interface you expect from ``bash input.sh`` or ``python input.py``:
command line arguments (including input files), printing to standard
output.  Since notebooks don't normally have any of these concepts and
you probably still want to run the notebook through the Jupyter
interface, there is a delicate balance.

Basic usage from command line.  To access these command line
arguments, see the next section::

   $ nbscript input.ipynb [argument1] [argument2]

If you want to save the output automatically, and not have it printed
to standard output::

  $ nbscript --save input.ipynb               # saves to input.out.ipynb
  $ nbscript --save --timestamp input.ipynb   # saves to input.out.TIMESTAMP.ipynb

If you want to submit to a cluster using Slurm, you can do that with
``snotebook``.  These all run automatically with ``--save
--timestamp`` to save the output::

   $ snotebook --mem=5G --time=1-12:00 input.ipynb



Setting up your notebook
------------------------

You need to carefully design your notebook if you want it to be
usable both as a script and as through Jupyter.  This section gives
some common patterns you may want to use.

.. highlight:: python

Detect if your notebook is running via nbscript, or not::

  import nbscript
  if nbscript.argv is not None:
      # We *are* running through nbscript

Get the command line arguments through nbscript.  This is ``None`` if
you are not running through nbscript::

  import nbscript
  nbscript.argv

You can use argparse like normal to parse arguments when
non-interactive (take ``argv`` from above)::

   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('input', help='Input file')
   args = parser.parse_args(args=argv)

Save some variables or save file if not running through nbscript::

  if nbscript.argv is not None:
      import cPickle as pickle
      state = dict(results=some_array,
                   other_results=other_array,
		   )
      pickle.dump(state, open('variables.pickle'), pickle.HIGHEST_PROTOCOL)

Don't run the main analysis when interactive::

  if nbscript.argv is None:
      # Don't do this stuff in Jupyter interface




Running with Slurm
------------------

Running as a script is great, but you need to submit to your cluster.
``nbscript`` comes with the command ``snotebook`` to make it easy to
submit to Slurm clusters.  It's designed to work just like ``sbatch``,
but directly submit notebook files without needing a wrapper script.

.. highlight:: console

``snotebook`` is just like ``nbscript``, but submits to slurm (via
``sbatch``) using any Slurm options::

  $ snotebook --mem=5G --time=1-12:00 input.ipynb
  $ snotebook --mem=5G --time=1-12:00 input.ipynb argument1.csv

By default, this automatically saves to ``input.out.TIMESTAMP.ipynb``,
but can be configured.

You can put normal ``#SBATCH`` comments in the notebook file, just
like you would when submitting with ``sbatch``.  But, it will only
detect it from the *very first cell* that has any of these arguments,
so don't split them over multiple cells.  Example:

.. code-block:: python

   #SBATCH --mem=5G
   #SBATCH --time=1-12:00

Just like with sbatch, you can combine command line options and
in-notebook options.



See also
--------

* `nbscript main page <https://github.com/NordicHPC/nbscript>`__, with
  more information.
