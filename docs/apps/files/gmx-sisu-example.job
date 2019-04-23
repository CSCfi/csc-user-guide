#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=test
#SBATCH --job-name=GMX
#SBATCH --nodes=4
#SBATCH --no-requeue
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

(( ncores = SLURM_NNODES * 24 ))
# this script runs a 96 core (4 full nodes, capital N for SLURM) gromacs job
#requesting 30 minutes time

export OMP_NUM_THREADS=1

module load gromacs/2018 # change to the desired version

aprun -n $ncores gmx mdrun_mpi -s topol -dlb yes -maxh 0.5

