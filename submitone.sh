#!/bin/bash

#SBATCH --job-name=my_lammps_tensile_simulation
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=00:01:00
#SBATCH --mem=190GB
#SBATCH --account=EEME030304

source .bashrc

# cd your directory

srun -n 24 --cpu-bind=cores --mpi=pmix_v3 lmp_mpi -in in.tensile_strength_test.lmp > log_output.txt 

# lmp -in in.tensile_strength_test.lmp

