#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=2G
#SBATCH --output=orca_example.out

# remove any existing modules
module purge
# load the open-mpi library
module load openmpi/4.1.2
# load orca module
module load orca/5.0.3

# remove old outputs
rm -f water*

# create an example input
cat > water.inp << EOF
!HF
!DEF2-SVP
!PAL4
* xyz 0 1
O   0.0000   0.0000   0.0626
H  -0.7920   0.0000  -0.4973
H   0.7920   0.0000  -0.4973
*
EOF

# Parallel runs need the full path to orca executable
# Do not use srun as orca will call mpi independently: https://www.orcasoftware.de/tutorials_orca/first_steps/trouble_install.html#using-openmpi
$(command -v orca) water.inp
