Python MPI4py
=============


::

    #!/usr/bin/env python
    """
    Parallel Hello World
    """
    from mpi4py import MPI
    import sys
    size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()
    sys.stdout.write(
        "Hello, World! I am process %d of %d on %s.\n"
        % (rank, size, name))

Running helloworld.py using only srun::

    module load Python/2.7.11-goolf-triton-2016b
    srun --time=00:10:00 -n 4 -p debug python helloworld.py

Example sbatch script submit.sh when running helloworld.py through
sbatch::

    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH -n 4
    #SBATCH -p debug

    module load Python/2.7.11-goolf-triton-2016b
    mpiexec -n $SLURM_NTASKS python helloworld.py

