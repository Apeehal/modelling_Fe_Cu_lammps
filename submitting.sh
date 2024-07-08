#!/bin/bash

#SBATCH --job-name=my_lammps_test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=00:01:00
#SBATCH --mem=190GB
#SBATCH --account=EEME030304

source ~/.bashrc

# Load necessary modules
module load lammps
module load openmpi

# Print SLURM and MPI environment variables for debugging
printenv | grep SLURM
printenv | grep MPI

# Check loaded modules
module list

# Check allocated nodes
srun hostname

# Run a simple MPI command
srun echo "Hello, World"

# Test MPI with a simple program
mpicc mpi_hello.c -o mpi_hello
srun -n 24 ./mpi_hello

# Run LAMMPS without CPU binding
srun -n 24 lmp_mpi -in in.tensile_strength_test.lmp

