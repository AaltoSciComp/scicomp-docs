Using Mathematica on Triton
---------------------------

Load Mathematica
~~~~~~~~~~~~~~~~

Mathematica is loaded through a module::

    module load mathematica

See available versions with ``module avail mathematica``.

You can test by running in text-based mode::

    $ wolfram



With graphical user interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch the graphical user interface (GUI), login to triton.aalto.fi
with ``-X``, i.e. X11 forwarding enabled.

::

    ssh -X triton.aalto.fi

If you need to run computationally-intensive things with the GUI, use
``sinteractive`` to get an :doc:`interactive shell on a
node<../tut/interactive>`::

  sinteractive --mem=10G --time=1:00

Either way, you start the GUI with mathematica::

    $ mathematica &



Running batch scripts
~~~~~~~~~~~~~~~~~~~~~

Create a script file, say ``script.m``.  You can run this script and
store the outputs in ``output.txt`` using::

  math -noprompt -run '<<script.m' > output.txt

To put this in a batch script, simply look at :doc:`the serial jobs
tutorial <../tut/serial>`.  Here is one such example::

  #!/bin/bash
  #SBATCH --mem=5G
  #SBATCH --time=2:00

  module load mathematica
  math -noprompt -run '<<script.m'



Common problems
~~~~~~~~~~~~~~~

**Activation** If you need to activate Mathematica when you first run
it, we recommend that you launch it in GUI mode first, choose 'Other
ways to activate'" then "Connect to a network license server", and
paste ``lic-mathematica.aalto.fi``.  It *should* be automatically
activated, though, if not file an issue and link this page.



See also
~~~~~~~~

Various other references also apply here once you load the module and
adapt them to Slurm:

* https://wiki.hpcc.msu.edu/display/hpccdocs/Using+Mathematica+in+Batch+Mode
* https://hpc.llnl.gov/software/mathematical-software/interactive-math-tools



Admin notes
~~~~~~~~~~~

When installing new versions, put ``!lic-mathematica.aalto.fi`` into
``Configuration/Licensing/mathpass`` in the base directory
