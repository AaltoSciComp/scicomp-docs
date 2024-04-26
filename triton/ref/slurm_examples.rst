Simple batch script, submit with ``sbatch the_script.sh``:

.. code-block:: slurm

   #!/bin/bash -l
   #SBATCH --time=01:00:00
   #SBATCH --mem-per-cpu=1G

   module load scicomp-python-env
   python my_script.py


Simple batch script with array (can also submit with
``sbatch --array=1-10 the_script.sh``):

.. code-block:: slurm

   #!/bin/bash -l
   #SBATCH --array=1-10

   python my_script.py --seed=$SLURM_ARRAY_TASK_ID
