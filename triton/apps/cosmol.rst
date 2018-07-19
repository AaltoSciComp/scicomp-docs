COMSOL Multiphysics
~~~~~~~~~~~~~~~~~~~

-  Version 4.3 installed. Use module command to enable.

   -  Runing on the fat-nodes straight out of the box.
   -  Would be interesting to submit cluster jobs from the fat node.
   -  Pure MPI-parallel Tests have worked straight-forward. Something
      like the following was within the batch-job submit file::

          module  load mvapich2-x86_64
          BIN=/share/apps/comsol/comsol43/COMSOL43/bin/comsol
          INPUT_FILE=perX_inf.mph
          OUTPUT_FILE=perX_inf_$SLURM_JOB_ID.mph
          $BIN   batch \
              -clustersimple \
              -mpibootstrap slurm\
              -inputfile $INPUT_FILE \
              -outputfile $OUTPUT_FILE \
              -launcher slurm

-  Comsol uses a lot of temp file storage, which by default goes to
   $HOME. Fix a bit like the following::

       $ rm -rf ~/.comsol/v43a/recoveries 
       $ mkdir /triton/tfy/work/$USER/comsol_revoveries/ 
       $ ln -s /triton/tfy/work/$USER/comsol_revoveries/ ~/.comsol/ 
