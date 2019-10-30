# Turbomole

TURBOMOLE is a program package for electronic structure calculations.
It includes most standard and state of the art methods for ground state calculations. Properties both for ground and excited states can be obtained. TURBOMOLE has been designed for efficient study of large systems.

## Available

-   Puhti: 7.4.1

## License

-   You may use the Software exclusively for non-profit research
    purposes.
-   Only users from academic (i.e. degree-granting) institutes are
    allowed to use the Software

## Usage

Initialise Turbomole on Puhti like this:

```bash
$ module load turbomole/7.4.1 
```


**Example batch script for Puhti using MPI parallelization**

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss

ulimit -s unlimited
export PARA_ARCH=MPI         # use MPI 
export MPI_USESRUN=1
export SLURM_MPI_TYPE=pmi2
export SLURM_CPU_BIND=none
export I_MPI_PIN_DOMAIN=auto,compact
module load turbomole/7.4.1
export PARNODES=$SLURM_NTASKS # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
seff $SLURM_JOBID
```
**Example batch script for Puhti using SMP parallelization**


```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1            # for SMP only 1 is possible
#SBATCH --cpus-per-task=40   # SMP threads
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss

ulimit -s unlimited
export PARA_ARCH=SMP         # use SMP threads   
export MPI_USESRUN=1
export SLURM_MPI_TYPE=pmi2
export SLURM_CPU_BIND=none
export I_MPI_PIN_DOMAIN=auto,compact
module load turbomole/7.4.1
export PARNODES=$SLURM_CPUS_PER_TASK  # for SMP
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
seff $SLURM_JOBID
```

!!! note
    Particularly some of the wavefunction-based electron correlation methods can be very disk I/O intensive. Such jobs benefit from using the fast local storage on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Example batch script for Puhti using MPI parallelization and local disk**

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss
#SBATCH --gres=nvme:100      # requested local disk in GB

ulimit -s unlimited
export PARA_ARCH=MPI         # use MPI
export MPI_USESRUN=1
export SLURM_MPI_TYPE=pmi2
export SLURM_CPU_BIND=none
export I_MPI_PIN_DOMAIN=auto,compact
module load turbomole/7.4.1
# define local disk as scratch
export TURBOTMPDIR=$LOCAL_SCRATCH/$SLURM_JOBID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
dscf > dscf.out
ccsdf12 > ccsdt.out
seff $SLURM_JOBID
```
## References
Please quote the usage of the program package under consideration of the version
number:

-   TURBOMOLE V7.4 2019, a development of University of Karlsruhe and
Forschungszentrum Karlsruhe GmbH, 1989-2007,
TURBOMOLE GmbH, since 2007; available from
http://www.turbomole.com.
-    Scientific publications require proper citation of methods and procedures employed.
The output headers of TURBOMOLE modules include the relevant papers. 

## More information
-   [TURBOMOLE GmbH](https://www.turbomole.org/turbomole/turbomole-documentation/) 
