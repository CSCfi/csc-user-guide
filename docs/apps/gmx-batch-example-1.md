
```
#!/bin/bash -l
#SBATCH -t 00:30:00
#SBATCH -p parallel
#SBATCH --ntasks-per-node=24
#SBATCH --nodes=8
#SBATCH -J GMX
#SBATCH --mem-per-cpu=512
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 192 core (8 full Haswell nodes) gromacs job, requesting 30 minutes time

export OMP_NUM_THREADS=1

# module load gromacs-env/2018.x # change x to the latest version
# un/comment to use non-default versions
module load gromacs-env # change x to the latest version

srun mdrun_mpi -s topol -maxh 0.5 
```
