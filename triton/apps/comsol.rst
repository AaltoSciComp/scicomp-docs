COMSOL Multiphysics
~~~~~~~~~~~~~~~~~~~

.. hint:: Join the other COMSOL users in our Zulip :ref:`chat`: Stream "#triton", topic "Comsol user group".


To check which versions of Comsol are available, run::

          module spider comsol


Comsol in Triton is best run in `Batch-mode <https://www.comsol.com/blogs/how-to-run-simulations-in-batch-mode-from-the-command-line/>`_, i.e. without the graphical userinterface. Prepare your models on your workstation and bring the ready-to-run models to triton. However, various settings must be edited in the graphical user interface. For this, using `<vdi.aalto.fi>`_ to connect to triton is advisable. 

For detailed tutorials from COMSOL, see for example the Comsol Knowledge base articles `Running COMSOL® in parallel on clusters <https://www.comsol.com/support/knowledgebase/1001>`_ and `Running parametric sweeps, batch sweeps, and cluster sweeps from the command line <https://www.comsol.com/support/knowledgebase/1250>`_.

Prerequsities of running COMSOL in Triton
-----------------------------------------

There is a largish but limited pool of floating COMSOL licenses in Aalto University, so please be careful not launch large numbers of comsol processess that each consume a separate license.
	  
-  Comsol uses a lot of temp file storage, which by default goes to
   ``$HOME``. Fix a bit like the following::

       $ rm -rf ~/.comsol/
       $ mkdir /scratch/work/$USER/comsol_revoveries/
       $ ln -sT /scratch/work/$USER/comsol_revoveries/ ~/.comsol


- You may need to  enable access to the whole filesystem in *File|Options --> Preferences --> Security*: **File system access:** "*All files*"
 
  .. image:: comsol_preferences_security.jpg
	     :width: 50%
	     :alt: Figure showing the comsol security preferences dialog box: File system access: All files is highlighted.

- Enable the "Study -> Batch and Cluster" as well as "Study -> Solver and Job Configurations" nodes in the "Show More Options dialog box you can open by right-clicking the study in the Model Builder Tree.
		   
  



The cluster settings can be saved in comsol settings, not in the model file. The correct settings are entered in *File|Options --> Preferences --> Multicore and Cluster Computing*. It is enough to choose **Scheduler type**: "*SLURM*" 

.. image:: comsol_preferences_cluster.jpg
	   :width: 50%
	   :alt: Figure showing the cluster preferences dialog box: Scheduler type: Slurm is highlighted.
	   
You can test by loading from the Application Libraries the "cluster_setup_validation" model. The model comes with a documentation -pdf file, which you can open in the Application Libraries dialogue after selecting the model.

COMSOL requires MPICH2 compatible MPI libraries::

  $ module purge
  $ module load comsol/5.6 intel-parallel-studio/cluster.2020.0-intelmpi


An example run in a single node
-------------------------------

Use the parameters ``-clustersimple`` and ``-launcher slurm``. Here is a sample batch-job::

          #!/bin/bash

          # Ask for e.g. 20 compute cores
          #SBATCH --time=10:00:00
          #SBATCH --mem-per-cpu=2G
          #SBATCH --cpus-per-task=20

          cd $WRKDIR/my_comsol_directory
          module load Java
          module load comsol/5.6
	  module load intel-parallel-studio/cluster.2020.0-intelmpi

          # Details of your input and output files
          INPUTFILE=input_model.mph
          OUTPUTFILE=output_model.mph

          comsol batch -clustersimple -launcher slurm -inputfile $INPUTFILE -outputfile $OUTPUTFILE -tmpdir $TMPDIR

	  


Cluster sweep
-------------

If you have a parameter scan to perform, you can use the Cluster sweep node. The whole sweep only needs one license even if comsol launches multiple instances of itself.

First set up the cluster preferences, as described above.


Start by loading the correct modules in triton (COMSOL requires MPICH2 compatible MPI libraries). Then open the graphical user interface to comsol on the login node and open your model. ::

  $ module purge
  $ module load module load comsol/5.6 intel-parallel-studio/cluster.2020.0-intelmpi
  $ comsol

Add a "Cluster Sweep" node to your study and a "Cluster Computing" node into your "Job Configurations" (You may need to first enable them in the "Show more options". Check the various options. You can try solving a small test case from the graphical user interface. You should see COMSOL submitting jobs to the SLURM queue. 

For a larger run, COMSOL can then submit the jobs with comsol but without the GUI::

  $ comsol batch -inputfile your_ready_to_run_model.mph -outputfile output_file.mph -study std1 -mode desktop

See also how to `run a parametric sweep from command line? <https://www.comsol.com/support/knowledgebase/1250>`_

  
Since the sweep may take some time to finnish, please consider using `tmux <https://github.com/tmux/tmux/wiki/Getting-Started>`_ or `screen <https://www.gnu.org/software/screen/manual/screen.html#Getting-Started>`_ to keep your session open.




MATLAB + COMSOL --  livelink
----------------------------

It is possible to control COMSOL with MATLAB. The `blog post <https://knifelees3.github.io/2019/07/06/A_En_How_To_Use_COMSOL_LiveLink_With_MATLAB/#Run-COMSOL-live-link-with-MATLAB-on-server>`_ by KnifeLee was useful in preparation of this example.

Save a username and password for COMSOL mph server
**************************************************

Before your first use, you need to save the username and password for COMSOL mph server. On the login node, run::

  $ module load comsol/5.6
  $ comsol mphserver
  
And COMSOL will ask for you to choose a username and password. You can close the comsol server with "close".

Please note, that each instance of the below process uses a COMSOL licence, so this method is not useful for parameter scans.

Example files for batch job workflow
************************************

Here is an example batch submit script ``comsol_matlab_livelink.sh``::

  #!/bin/bash

  #SBATCH --time=10:00:00

  # Ask for a single node, since the port for connections between COMSOL and MATLAB is by default using port 2036,
  # and this is an easy way to avoid clashes between multiple jobs.
  #SBATCH --nodes=1
  #SBATCH --exclusive
  
  
  module load matlab
  module load comsol/5.6
 

  echo starting comsol server in the background
  comsol mphserver &
  echo comsol is now running
  
  matlab -nodesktop -nosplash -r "runner;exit(0)"
  echo matlab closed


The MATLAB process is running the ``runner.m`` script::

  disp('Including comsol routines into the path.')
  addpath /share/apps/comsol/5.6/mli/

  disp('Connecting to COMSOL from MATLAB')
  mphstart(2036)
  disp('Connection established')
  
  disp('Starting Model Control Script')

  script;
  
  disp('Exiting Matlab')
  exit(0);


The Model Control Script ``script.m`` could be e.g. the following::

  import com.comsol.model.*;
  import com.comsol.model.util.*;
  model = ModelUtil.create('Model1');  
  model.component.create('comp1', true);
  %...


The job is submitted with::

  $ sbatch comsol_matlab_livelink.sh

Cluster computing controlled from your windows workstation
----------------------------------------------------------

The following example shows a working set of settings to `use triton as a remote computation cluster for COMSOL <https://www.comsol.com/blogs/how-to-run-on-clusters-from-the-comsol-desktop-environment/>`_.

Prerequisities:

 * Store ssh-keys in pagent so that you can connect to triton with putty without entering the password.

 * Save / install `putty executables <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ locally, e.g. in Z:\\putty:

   * plink.exe

   * pscp.exe

   * putty.exe

  .. image:: comsol_cluster_computing.jpg
	     :width: 50%
	     :alt: Figure showing the comsol settings for Cluster Computing.

  .. image:: comsol_cluster_computing_1.jpg
	     :width: 50%
	     :alt: Figure showing the comsol settings for Cluster Computing within the Job Configurations.

  
..
  /share/apps/spack/envs/fgci-centos7-generic/software/intel-parallel-studio/cluster.2020.0/ttn75qk/compilers_and_libraries_2020.0.166/linux/mpi/intel64/bin/mpirun
