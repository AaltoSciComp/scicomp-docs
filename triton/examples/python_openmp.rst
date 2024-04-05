Python OpenMP example
---------------------


``parallel_Python.sh``::

    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=2G
    #SBATCH -o parallel_Python.out

    module load scicomp-python-env

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun -c $SLURM_CPUS_PER_TASK python parallel_Python.py

``parallel\Python.py``::

    import numpy as np
    a = np.random.random([2000,2000])
    a = a + a.T
    b = np.linalg.pinv(a)
    print(np.amax(np.dot(a,b)))
