COMSOL Multiphysics
~~~~~~~~~~~~~~~~~~~

Comsol in Triton is best run in Batch-mode. To check which versions of Comsol are available, run::

          module spider comsol

-  To run Comsol in a single node use ``-clustersimple`` and
   ``-launcher slurm``::

          #!/bin/bash

          # Ask for e.g. 20 compute cores
          #SBATCH --time=0-10:00
          #SBATCH --mem-per-cpu=2G
          #SBATCH -N 1
          #SBATCH -c 20

          cd $WRKDIR/my_comsol_directory
          module load Java
          module load comsol

          # Details of your input and output files
          INPUTFILE=input_model.mph
          OUTPUTFILE=output_model.mph

          comsol batch -clustersimple -launcher slurm -inputfile $INPUTFILE -outputfile $OUTPUTFILE -tmpdir $TMPDIR


-  Comsol can run even bigger jobs over multiple computing nodes with ``-clustersimple``. For this, please refer to Comsol online manual or ask for further help.
-  Comsol uses a lot of temp file storage, which by default goes to
   ``$HOME``. Fix a bit like the following::

       $ rm -rf ~/.comsol/
       $ mkdir /scratch/work/$USER/comsol_revoveries/
       $ ln -sT /scratch/work/$USER/comsol_revoveries/ ~/.comsol
