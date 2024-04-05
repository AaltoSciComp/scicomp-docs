=================
Jupyter on Triton
=================

.. note:: Quick link

   Triton's Jupyter is available via Open OnDemand,
   https://ondemand.triton.aalto.fi (Jupyter app).

.. note:: For new users

   Are you new to Triton and want to access Jupyter?  Triton is a
   high-performance computing cluster, and JupyterHub is just one of
   our services - one of the easiest ways to get started.  You still
   need a Triton account.  This site has many instructions, but you
   should read at least:

   * :doc:`About us <../tut/intro>`, :doc:`how to get help
     <../help>`, and :doc:`acknowledging Triton
     usage<../acknowledgingtriton>` (this JupyterHub is part of
     Triton, and thus Science-IT must be acknowledged in publications).
   * :doc:`The accounts page <../accounts>`, in order to request a
     Triton account.
   * Possibly the :doc:`storage page <../tut/storage>` and
     :doc:`remote data access page <../tut/remotedata>` to learn about
     the places to store data and how to transfer data.
   * The JupyterHub section of this page (below).

   If you want to use Triton more, you should finish the entire
   :ref:`tutorials section <tutorials>`.

..
  .. figure:: /images/jupyter_demo.gif
     :scale: 60%
     :align: center
     :alt: alternate text
     :figclass: align-center

     < Triton JupyterHub Demo >

Jupyter notebooks are a way of interactive, web-based computing:
instead of either scripts or interactive shells, the notebooks allow
you to see a whole script + output and experiment interactively and
visually.  They are good for developing and testing things, but once
things work and you need to scale up, it is best to put your code into
proper programs (:doc:`more info </scicomp/jupyter-pitfalls>`).  You
must do this if you are going to large parallel
computing.

Triton's standard Jupyter environment is available at
https://ondemand.triton.aalto.fi (the Jupyter app).

You can always run notebooks yourself on your own (or remote)
computers, but on Triton we have some facilities already set up to
make it easier.

.. highlight:: console


How Jupyter notebooks work
==========================
* Start a notebook
* Enter some code into a cell.
* Run it with the buttons or ``Control-enter`` or ``Shift-enter`` to
  run a cell.
* Edit/create new cells, run again.  Repeat indefinitely.
* You have a visual history of what you have run, with code and
  results nicely interspersed.  With certain languages such as Python,
  you can plots and other things embedded, so that it becomes a
  complete reproducible story.

JupyterLab is the next iteration of this and has many more features,
making it closer to an IDE or RStudio.

Notebooks are without a doubt a great tool.  However, they are only
one tool, and you need to know their limitations.  See our other page
on :doc:`limitations of notebooks </scicomp/jupyter-pitfalls>`.


.. _jupyterhub:

Jupyter via Open OnDemand
=========================

.. note::

   JupyterHub is replaced by Open OnDemand (OOD) since 2024 April.  The
   "Jupyter" app has been set up to reproduce the previous general-use
   Jupyter environment.


Connecting and starting
-----------------------
Log in to Open OnDemand:
https://ondemand.triton.aalto.fi.

Once you log in, select the Jupyter app.  Then, you must start your
single-user server.  Your server runs in the
Slurm queue, so the first start-up takes a few seconds but after that
it will stay running even if you log out.

The resources you request
are managed by slurm: if you go over the memory limit, your server
will be killed without warning or notification (but you can see it in
the output log, ``output.log`` in the session).  The Jupyter
server nodes are oversubscribed, which means that we can allocate more
memory and CPU than is actually available.  We will monitor the nodes
to try to ensure that there are enough resources available, so do
report problems to us.  **Please request the minimum amount of memory
you think you need** - you can always restart with more memory.  You
can go over your memory request a little bit before you get problems.
When you use Jupyter via this interface, the slurm billing weights are
lower, so that the rest of your Triton priority does not decrease by
as much.

..
    Proxy for remote access
    ~~~~~~~~~~~~~~~~~~~~~~~

    When connecting to JupyterHub outside of Aalto networks, you need to
    connect somehow.  This describes how you can do it using SSH.  Using
    the Aalto VPN is easier (Aalto laptops have it set up by default).  In
    a few weeks, this should no longer be needed.

    If you use the proxy instead of the VPN:

    * Install the proxy extension

    * Install the extension FoxyProxy Standard (Firefox or Chrome).
      Some versions do not work properly: the 5.x series for Firefox may
      not work, but older and newer does.

      * Create a new proxy rule with the pattern ``*jupyter.triton.aalto.fi*``.

    * Proxy type: SOCKS5, Proxy URL: ``localhost``, port ``8123``.

      * SSH to kosh or some other Aalto computer and use the ``-D 8123``.
    This starts a proxy on your computer on port 8123.  This has to
      always be running whenever you connect to the notebook.

      * ``ssh -D 8123
	username@kosh.aalto.fi``.

    Now, when you go to ``jupyter.triton.aalto.fi``, you will
    *automatically* connect to the right place on Triton via FoxyProxy and
    the SSH proxy and can use Jupyter like normal.  But if the ssh
    connection goes down, then you can't connect and will get errors, and
    you will have to remember to restart it.  You should also remember
    that it will require SSH *inside* of Aalto too: it's simplest disable
    FoxyProxy inside of Aalto networks and enable only when you need.


Usage
-----
Once you get to your single-user server Jupyter running as your own
user on Triton.  You begin in a convenience directory which has links to
``home``, ``scratch``, etc.  You can not make files in this directory
(it is read-only), but you can navigate to the other folders to create
your notebooks.  You have access to all the Triton filesystems (not
project/archive) and all normal software.

The log files for your single-user servers can be found in the OOD
session directory, see
``output.log``.

For `reasons of web security
<https://jupyterhub.readthedocs.io/en/latest/reference/websecurity.html>`__,
you can't install your own extensions (but you can install your own
kernels).  Send your requests to us instead.



Software and kernels
====================
A **Jupyter Kernel** is the runtime which actually executes the code
in the notebook (and it is separate from Jupyter
itself). We have various kernels automatically installed:

* Python (module ``scicomp-python-env``)
* Matlab (latest module)
* Bash kernel
* R (a default R environment you can get by ``module load scicomp-r-env``.
  ("R (safe)" is similar but tries to block some local user configuration
  which sometimes breaks things, see FAQ for more hints.)
* Kernels (and software in kernels) may be updated over time - create
  your own environment for reproducibility.

Since these are the normal Triton modules, you can submit installation
requests for software in these so that it is automatically available.

.. admonition:: What's a kernel?  Where are they?
   :class: dropdown

   As stated at the start of this section, the kernel is what actually
   runs the code.  An example of a kernel command line is ``'python -m
   ipykernel_launcher -f{connection_file}``.  What ``python`` starts?:
   that depends on the environment or adding an absolute path.

   You can list your installed kernels with ``jupyter kernelspec
   list`` (to ensure the list is the same as jupyter.triton sees,
   ``module load jupyterhub/live first``).  Look in these directories,
   at ``kernel.json``, to see just what it does.

   You can remove kernels by removing their directory or ``jupyter
   kernelspec remove``.

   The program `envkernel <https://github.com/NordicHPC/envkernel>`__
   can serve as a wrapper to a) modify kernel.json files and b) adjust
   the environment (e.g. loading modules) at runtime, which can be
   hard to fully emulate by statically defining environment variables
   in kernel.json.


.. _triton-jupyter-virtualenv-conda-kernels:

Installing kernels from virtualenvs or Anaconda environments
------------------------------------------------------------

If you want to use Jupyter with your own packages, you can do that.
First, make a conda environment / virtual environment on Triton and
install the software you need in it (see :ref:`conda` or
:ref:`virtualenv`).  This environment can be used for other things,
such as your own development outside of Jupyter.

You have to have the package ``ipykernel`` installed in the
environment: Add it to your requirements/environment, or activate the
environment and do ``pip install ipykernel``.

Then, you need to make the environment visible inside of Jupyter.
**For conda environments**, you can do::

  $ module load jupyterhub/live
  $ envkernel conda --user --name INTERNAL_NAME --display-name="My conda" /path/to/conda_env

Or for **Python virtualenvs**::

  $ module load jupyterhub/live
  $ envkernel virtualenv --user --name INTERNAL_NAME --display-name="My virtualenv" /path/to/virtualenv

Installing a different R module as a kernel
-------------------------------------------

Load your R modules, install R kernel normally (to some ``NAME``),
use envkernel as a wrapper to re-write the kernel (reading the
``NAME`` and rewriting to the same ``NAME``), after it loads the
modules you need::

  ## Load jupyterhub/live, and R 3.6.1 with IRkernel.
  $ module load r-irkernel/1.1-python3
  $ module load jupyterhub/live

  ## Use Rscript to install jupyter kernel
  $ Rscript -e "library(IRkernel); IRkernel::installspec(name='NAME', displayname='R 3.6.1')"

  ## Use envkernel to re-write, loading the R modules.
  $ envkernel lmod --user --kernel-template=NAME --name=NAME $CONDA_PREFIX r-irkernel/1.1-python3


Installing a different R version as a kernel
--------------------------------------------

There are two ways to install a different R version kernel for jupyter. One relies on you building your own conda environment. 
The disadvantage is that you will need to create a kernel, the advantage is that you can add additional packages. The other option
is to use the existing R installations on Triton.

.. tabs::

  .. tab:: Using a conda environment
     
        You will need to create your own conda environment with all packages that are necessary
        to deploy the environment as a kernel.::

           ## Load mamba module before creating your environment - this provides mamba that is used to create your environment
           $ module load mamba

        Create your conda environment, selecting a ``NAME`` for the environment.::

           ## This will use the latest R version on conda-forge. If you need a specific version you can specify it
           ## as r-essentials=X.X.X, where X.X.X is your required R version number
           $ mamba create -n ENVNAME -c conda-forge r-essentials r-irkernel 
           ## If Mamba doesn't work you can also replace it with conda, but usually mamba is a lot faster

        The next steps are the same as building a Kernel, except for activating the environment instead of 
        loading the r-irkernel module, since this module depends on the R version.
        the ``displayname`` will be what will be displayed on jupyter ::
        
          ## Use Rscript to install jupyter kernel, you need the environment for this.
          ## You need the Python `jupyter` command so R can know the right place to
          ## install the kernel (provided by jupyterhub/live)
          $ module load jupyterhub/live
          $ source activate ENVNAME
          $ Rscript -e "library(IRkernel); IRkernel::installspec(name='ir-NAME', displayname='YOUR R Version')"
          $ conda deactivate ENVNAME

          ## For R versions before 4, you need to install the kernel. After version 4 IRkernel automatically installs it.
          $ envkernel conda --user --kernel-template=ir-NAME --name=ir-NAME ENVNAME    TODO: full path?
    
  .. tab:: Using existing Triton installations of R

       First, you need to load the R version you want to create 
       to deploy the environment as a kernel::

         $ module spider r
         ## Select one of the displayed R versions and load it with the following line
         $ module load r/THE_VERSION_YOU_WANT

       Start R and install the IRkernel package. ::

         ## start R
         $ R

       .. code-block:: rconsole

         ## In R install the IRkernel package (to your home directory)
         install.packages('IRkernel') 
         ## exit R again

       Create the installation specs using Rscript and IRKernel. Select a ``NAME`` for the environment specification
       that can be used to install it. The
       Next install the jupyter kernel. Here you need to select the ``NAME`` given before. 
       The NAME is what is will be referred to for installation, while ``DISPLAYNAME`` will be displayed in jupyter::

         ## Use Rscript to install the jupyter kernel. The jupyterhub/live module is required to point R at the right place for jupyter
         $ module load jupyterhub/live
         $ Rscript -e "library(IRkernel); IRkernel::installspec(name='NAME', displayname='DISPLAYNAME')"
         ## For R versions before 4, you need to install the kernel. After version 4 IRkernel automatically installs it.
         $ envkernel lmod --user --kernel-template=NAME --name=IMAGENAME YOURRMODULE
         ## YOURRMODULE should match the module you loaded above (THE_VERSION_YOU_WANT above)

.. note:: Installing R packages for jupyter

  Installing packages via jupyter can be problematic, as they require interactivity, which jupyter does not readily support.
  To install packages therefore go directly to triton. Load the environment or R module you use and install the packages
  ineractively. After that is done, restart your jupyter session and reload your kernel, all packages that you installed should
  then be available.

Install your own kernels from other Python modules
--------------------------------------------------

This works if the module provides the command ``python`` and
``ipykernel`` is installed.  This has
to be done once in any Triton shell::

  $ module load jupyterhub/live
  $ envkernel lmod --user --name INTERNAL_NAME --display-name="Python from my module" MODULE_NAME
  $ module purge

Install your own kernels from Singularity image
-----------------------------------------------
First, find the ``.simg`` file name.  If you are using this from one
of the Triton modules, you can use ``module show MODULE_NAME`` and
look for ``SING_IMAGE`` in the output.

Then, install a kernel for your own user using envkernel.  This has to
be done once in any Triton shell::

  $ module load jupyterhub/live
  $ envkernel singularity --user --name KERNEL_NAME --display-name="Singularity my kernel" SIMG_IMAGE
  $ module purge

As with the above, the image has to provide a ``python`` command and
have ``ipykernel`` installed (assuming you want to use Python, other
kernels have different requirements).

Julia
-----

Julia: currently doesn't seem to play nicely with global
installations (so we can't install it for you, if anyone knows
something otherwise, let us know).
Roughly, these steps should work to install the kernel yourself::

  $ module load julia
  $ module load jupyterhub/live
  $ julia

.. code-block:: julia-repl

  julia> Pkg.add("IJulia")

If this doesn't work, it may think it is already installed.  Force
it with this:

.. code-block:: julia-repl

  julia> using IJulia
  julia> installkernel("julia")



Install your own non-Python kernels
-----------------------------------
* First, ``module load jupyterhub/live``.  This loads
  the conda environment which contains all the server code and
  configuration.  (This step may not be needed for all kernels)
* Follow the instructions you find for your kernel.  You may need to
  specify ``--user`` or some such to have it install in your user
  directory.
* You can check your own kernels in
  ``~/.local/share/jupyter/kernels/``.

If your kernel involves loading a :doc:`module </triton/tut/modules>`,
you can either a) load the modules within the notebook server
("softwares" tab in the menu), or b) update your ``kernel.json`` to
include the required environment variables (see `kernelspec
<https://jupyter-client.readthedocs.io/en/stable/kernels.html>`__).
(We need to do some work to figure out just how this works).  Check
``/appl/manual_installations/software/jupyterhub/live/miniconda/share/jupyter/kernels/ir/kernel.json``
for an example of a kernel that loads a module first.

..
  This one-liner might help: ``( echo "  \"env\": {" ; for x in LD_LIBRARY_PATH LIBRARY_PATH MANPATH PATH PKG_CONFIG_PATH ; do echo "    \"$x\": \"${!x}\"", ; done ; echo "  }" ) >> ~/.local/share/jupyter/kernels/ir/kernel.json`` + then edit the JSON to make it valid.

From Jupyter notebooks to running on the queue
==============================================

While jupyter is great to interactively run code, it can become 
a problem if you need to run multiple parameter sets through a jupyter
notebook or you need a specific resource which is not available
for jupyter. The latter might be because the resource is sparse enough
that having an open jupyter session that finished a part and is waiting
for the user to start the next is idly blocking the resource. 
At this point you will likely want to move your code to pure python and 
run it via the queue.

Here are the steps necessary to do so:

1. Log into Triton via ssh ( Tutorials can be found :doc:`here </triton/quickstart/connecting/>` and :doc:`here </triton/tut/connecting/>` ).
2. In the resulting terminal session, load the jupyterhub module to have jupyter available ( ``module load jupyterhub`` )
3. Navigate to the folder where your jupyter notebooks are located. You can see the path by moving your mouse over the files tab on jupyterlab.
4. Convert the notebook(s) you want to run on the cluster ( ``jupyter nbconvert yourScriptName.ipynb --to python``). 

   * If you need to run your code for multiple different parameters, modify the python code to allow input parameter parsing 
     (e.g. using `argparse <https://docs.python.org/3/howto/argparse.html>`__, or `docopt <https://github.com/docopt/>`__ )
     You should include both input and output arguments as you want to save files to different result folders or have them have indicative filenames. 
     There are two main reasons for this approach: A) it makes your code more maintainable, since you don't need to modify 
     the code when changing parameters and B) you are less likely to use the wrong version of your code (and thus getting the wrong results).
5. (Optional) Set up a conda environment. This is mainly necessary if you have multiple conda or pip installable packages that are 
   required for your job and which are not part of the normal Sc module. Try it via ``module load scicomp-python-env``. 
   You can't install into the scicomp environment provided by the scicomp-python-env module and you should NOT use  ``pip install --user`` as it will bite you later (and can cause difficult to debug problems).
   If you need to set up your own environment follow :doc:`this guide </triton/apps/python-conda/>`
6. Set up a slurm batch script in a file e.g. ``simple_python_gpu.sh``. You can do this either with ``nano simple_python_gpu.sh`` 
   (to save the file press ``ctrl+x``, type ``y`` to save the file and press ``Enter`` to accept the file name), or you can mount
   the triton file system and use your favorite editor, for guides on how to mount the file system have a look 
   `here </triton/quickstart/data/>` and `here </triton/tut/remotedata/>`).
   Depending on your OS, it might be difficult to mount home and it is 
   anyways best practice to use ``/scratch/work/USERNAME`` for your code.
   :download:`Here </triton/examples/python/simple_python_gpu.sh>` is an example:
   
   .. literalinclude:: /triton/examples/python/simple_python_gpu.sh
      :language: slurm

   This is a minimalistic example. If you have parameter sets that you want to use have a look at :doc:`array jobs here </triton/tut/array/>`)

7. Submit your batch script to the queue : ``sbatch simple_python_gpu.sh``
   This call will print a message like: ``Submitted batch job <jobid>``
   You can use e.g. ``slurm q`` to see your current jobs and their status in the queue, or monitor your jobs as described :doc:`here </triton/tut/monitoring/>`.


Git integration
===============

You can enable git integration on Triton by using the following
lines from inside a git repository.  (This is normal nbdime, but uses
the centrally installed one so that you don't have to load a
particular conda environment first.  The ``sed`` command fixes
relative paths to absolute paths, so that you use the tools no matter
what modules you have loaded)::

  $ /appl/manual_installations/software/jupyterhub/live/miniconda/bin/nbdime config-git --enable
  $ sed --in-place -r 's@(= )[ a-z/-]*(git-nb)@\1/appl/manual_installations/software/jupyterhub/live/miniconda/bin/\2@' .git/config



FAQ/common problems
===================
* **My server has died mysteriously.**  This may happen if resource
  usage becomes too much and exceed the limits - Slurm will kill your
  notebook.  You can check the ``output.log`` file in the OOD session
  directory.

* **My R kernel keeps dying**.  Some people seem to have global R
  configuration, either in ``.bashrc`` or ``.Renviron`` or some such
  which globally, which even affects the R kernel here.  Things we
  have seen: pre-loading modules in ``.bashrc`` which conflict with
  the kernel R module; changing ``RLIBS`` in ``.Renviron``.  You can
  either (temporarily or permanently) remove these changes, or you
  could `install your own R kernel <https://irkernel.github.io/>`__.
  If you install your own, it is up to you to maintain it (and
  remember that you installed it).



See also
========
* https://jupyter.org

  * Online demos and live tutorial: https://jupyter.org/try (use the
    Python one)

* Jupyter basic tutorial: https://www.youtube.com/watch?v=HW29067qVWk
  (this is just the first link on youtube - there are many more too)

* More advanced tutorial: `Data Science is Software
  <https://www.youtube.com/watch?v=EKUy0TSLg04>`__ (this is not just a
  Jupyter tutorial, but about the whole data science workflow using
  Jupyter.  It is annoying long (2 hours), but *very* complete and
  could be considered good "required watching")

* :doc:`/scicomp/jupyter-pitfalls`

* CSC has this service, too, however there is no long term storage yet
  so there is limited usefulness for research: https://notebooks.csc.fi/

Our configuration is available on Github.  Theoretically, all the
pieces are here but it is not yet documented well and not yet
generalizable.  The Ansible role is a good start but the jupyterhub
config and setup is hackish.

* Ansible config role:
  https://github.com/AaltoSciComp/ansible-role-fgci-jupyterhub
* Configuration and automated conda environment setup:
  https://github.com/AaltoSciComp/triton-jupyterhub

..
  Matlab support:
    pip install matlab_kernel
    cd $MATLABROOT/extern/engines/python/
    python setup.py
