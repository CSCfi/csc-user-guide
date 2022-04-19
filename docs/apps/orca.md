# ORCA

[ORCA](https://orcaforum.kofo.mpg.de/app.php/portal ) is an ab initio quantum chemistry program package that contains modern electronic structure methods including density functional theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical quantum chemistry methods. Its main field of application is larger molecules, transition metal complexes, and their spectroscopic properties. ORCA is developed in the research group of [Frank Neese](https://en.wikipedia.org/wiki/Frank_Neese). The free version is available only for academic use at academic institutions. 

[TOC]

## Available

-   Puhti: 5.0.3
-   Mahti-rhel8: 5.0.3

Note that due to licensing issues every user has to install their own copy of the program 

## License
 
ORCA users should register, agree to the EULA , download and install a private copy of the program (via [https://orcaforum.kofo.mpg.de/app.php/portal](https://orcaforum.kofo.mpg.de/app.php/portal))
The free version is available only for academic use at academic institutions.

## Usage

- Download the ORCA 5.0.3, Linux, x86-64, shared-version, ` orca_5_0_3_linux_x86-64_shared_openmpi411.tar.xz`
- Move the downloaded file to your computing project's application area (/projappl/<proj\>) on Puhti
- Unpack the package, `tar xf orca_5_0_3_linux_x86-64_shared_openmpi411.tar.xz`
- Example batch script for Puhti

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --account=<your billing project>
#SBATCH --time=0:30:00 # time as hh:mm:ss
module purge
module load gcc/9.1.0 openmpi/4.1.1-cuda intel-mkl/2019.0.4
export ORCADIR=<path to your ORCA directory>/orca_5_0_3_linux_x86-64_shared_openmpi411
export LD_LIBRARY_PATH=$ORCADIR:$LD_LIBRARY_PATH

ORTERUN=`which orterun`
ln -sf ${ORTERUN}  ${SLURM_SUBMIT_DIR}/mpirun
export PATH=${SLURM_SUBMIT_DIR}:${PATH}

$ORCADIR/orca orca_5.0.3.inp > orca_5.0.3.out
rm -f  ${SLURM_SUBMIT_DIR}/mpirun
```

- Example batch script for Puhti using local disk

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --account=<your billing project>
#SBATCH --time=0:30:00 # time as hh:mm:ss
#SBATCH --gres=nvme:100  # requested local disk space in GB
module purge
module load gcc/9.1.0 openmpi/4.1.1-cuda intel-mkl/2019.0.4
export ORCADIR=<path to your ORCA directory>/orca_5_0_3_linux_x86-64_shared_openmpi411
export LD_LIBRARY_PATH=$ORCADIR:$LD_LIBRARY_PATH

ORTERUN=`which orterun`
ln -sf ${ORTERUN}  ${SLURM_SUBMIT_DIR}/mpirun
export PATH=${SLURM_SUBMIT_DIR}:${PATH}

#Set $ORCA_TMPDIR to point to the local disk
export ORCA_TMPDIR=$LOCAL_SCRATCH
# Copy only the necessary files to $ORCA_TMPDIR
# Add more here if needed.
cp $SLURM_SUBMIT_DIR/*.inp $ORCA_TMPDIR/
# Move to $ORCA_TMPDIR
cd $ORCA_TMPDIR

$ORCADIR/orca orca_5.0.3.inp > orca_5.0.3.out
rm -f  ${SLURM_SUBMIT_DIR}/mpirun

# Copy all output to submit directory
cp -r $ORCA_TMPDIR $SLURM_SUBMIT_DIR
```

- Example batch script for Mahti-rhel8


```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --account=<your billing project>
#SBATCH --time=0:30:00 # time as hh:mm:ss
#SBATCH --job-name=orca-5.0.3
#SBATCH --error=jobfile.err%J
#SBATCH --output=jobfile.out%J
module purge
module load gcc/11.2.0 openmpi/4.1.2 openblas/0.3.18-omp
export ORCADIR=<path to your ORCA directory>/orca_5_0_3_linux_x86-64_shared_openmpi411
export LD_LIBRARY_PATH=$ORCADIR:$LD_LIBRARY_PATH

ORTERUN=`which orterun`
ln -sf ${ORTERUN}  ${SLURM_SUBMIT_DIR}/mpirun
export PATH=${SLURM_SUBMIT_DIR}:${PATH}

$ORCADIR/orca orca_5.0.3.inp > orca_5.0.3.out
rm -f  ${SLURM_SUBMIT_DIR}/mpirun
```

!!! note
    Please remember to adjust %pal nproc in your input file according to the total number of requested MPI tasks (nodes * ntasks-per-node) 


- You can find a few additional example jobs in the directory:

``` 
/appl/soft/chem/orca
```

## References

Cite your work with the following references:

The generic reference for ORCA is:
- Neese, F. (2012) The ORCA program system, Wiley Interdiscip. Rev.: Comput. Mol. Sci., 2, 73-78.

Please do not only cite the above generic reference, but also cite in addition the original
papers that report the development and ORCA implementation of the methods you have used in
your studies! The publications that describe the functionality implemented in ORCA are
given in the manual.

## More information
-   [ORCA Forum (login with the same credentials as you used for downloading)](https://orcaforum.kofo.mpg.de/app.php/portal)
-   [ORCA Tutorials](https://www.orcasoftware.de/tutorials_orca/)
-   [ORCA Input Library, containing example inputs](https://sites.google.com/site/orcainputlibrary/home) 
-   [Release notes](https://orcaforum.kofo.mpg.de/viewforum.php?f=56)


