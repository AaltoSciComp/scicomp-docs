COMSOL Multiphysics
~~~~~~~~~~~~~~~~~~~

To check which versions of Comsol are available, run::

          module spider comsol


Comsol in Triton is best run in `Batch-mode <https://www.comsol.com/blogs/how-to-run-simulations-in-batch-mode-from-the-command-line/>`_, i.e. without the graphical userinterface. Prepare your models on your workstation and bring the ready-to-run models to triton. However, various settings must be edited in the graphical user interface. For this, using `<vdi.aalto.fi>`_ to connect to triton is advicable. 

There is a largish but limited pool of floating COMSOL licenses in Aalto University, so please be careful not launch large numbers of comsol processess that each consume a separate license.
	  
-  Comsol uses a lot of temp file storage, which by default goes to
   ``$HOME``. Fix a bit like the following::

       $ rm -rf ~/.comsol/
       $ mkdir /scratch/work/$USER/comsol_revoveries/
       $ ln -sT /scratch/work/$USER/comsol_revoveries/ ~/.comsol

- You may need to allow access to all files in Comsol Preferences: File|Options --> Preferences --> Security --> Methods and Java libraries --> File system access: All files
       
Ways of running COMSOL in Triton
********************************

See for example the Comsol Knowledge base article `Running parametric sweeps, batch sweeps, and cluster sweeps from the command line <https://www.comsol.com/support/knowledgebase/1250>`_.


-  To run Comsol in a single node use ``-clustersimple`` and
   ``-launcher slurm``::

          #!/bin/bash

          # Ask for e.g. 20 compute cores
          #SBATCH --time=10:00:00
          #SBATCH --mem-per-cpu=2G
          #SBATCH --cpus-per-task=20

          cd $WRKDIR/my_comsol_directory
          module load Java
          module load comsol

          # Details of your input and output files
          INPUTFILE=input_model.mph
          OUTPUTFILE=output_model.mph

          comsol batch -clustersimple -launcher slurm -inputfile $INPUTFILE -outputfile $OUTPUTFILE -tmpdir $TMPDIR


-  Comsol can run even bigger jobs over multiple computing nodes with ``-clustersimple``. For this, please refer to Comsol online manual or ask for further help.



- If you have a parameter scan to perform, you can use the Cluster sweep node.


 You can test by loading from the Application Libraries the "cluster_setup_validation" model. The model comes with a documentation -pdf file, which you can open in the Application Libraries dialogue after selecting the model.

We start by loading the correct modules in triton (COMSOL requires MPICH2 compatible MPI libraries)::

  $ module purge
  $ module load module load comsol/5.6 intel-parallel-studio/cluster.2020.0-intelmpi
  

The cluster settings are saved in comsol settings, not in the model file. The correct settings are entered in *File|Options --> Preferences --> Multicore and Cluster Computing*. It is enough to choose **Scheduler type**: "*SLURM*" 

Also, enable access to the whole filesystem in *File|Options --> Preferences --> Security*: **File system access:* "*All files*"
 


How to `run a parametric sweep from command line <https://www.comsol.com/support/knowledgebase/1250>`_?


comsol batch -inputfile your_ready_to_run_model.mph -outputfile output_file.mph -study std1 -mode desktop


..
  /share/apps/spack/envs/fgci-centos7-generic/software/intel-parallel-studio/cluster.2020.0/ttn75qk/compilers_and_libraries_2020.0.166/linux/mpi/intel64/bin/mpirun
