# Turbomole

TURBOMOLE is a modular program suite for ab initio quantum-chemical and condensed-matter simulations 
It includes most standard and state of the art methods for ground state calculations. Properties both for ground and excited states can be obtained. TURBOMOLE has been designed for efficient study of large systems.

## Available

*   Puhti: 7.5
*   Mahti: 7.5

## License

-   You may use the Software exclusively for non-profit research
    purposes.
-   Only users from academic (i.e. degree-granting) institutes are
    allowed to use the Software

## Usage

Initialise Turbomole environment:

```bash
module load turbomole/7.5
```


**Batch script example for Puhti using MPI parallelization**

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss
export PARA_ARCH=MPI         # use MPI 
module load turbomole/7.5
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

**Batch script example for Puhti using SMP parallelization**

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1            # for SMP only 1 is possible
#SBATCH --cpus-per-task=40   # SMP threads
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss
export PARA_ARCH=SMP         # use SMP threads   
module load turbomole/7.5
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_CPUS_PER_TASK  # for SMP
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

!!! note
    Occasionally `mpshift` calculations are terminated due to the local `/tmp` becoming full. The problem can be circumvented by redefining `$TMPDIR`.
``` 
    export TMPDIR=$TURBOTMPDIR
```

!!! note
    Particularly some of the wavefunction-based electron correlation methods can be very disk I/O intensive. Such jobs benefit from using the fast local storage on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Batch script example for Puhti using MPI parallelization and local disk**

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss
#SBATCH --gres=nvme:100      # requested local disk in GB
export PARA_ARCH=MPI         # use MPI
module load turbomole/7.5
export SLURM_CPU_BIND=none
# define local disk as scratch
export TURBOTMPDIR=$LOCAL_SCRATCH/$SLURM_JOBID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
dscf > dscf.out
ccsdf12 > ccsdt.out
```

**Batch script example for Mahti using MPI parallelization**

```
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128 # MPI tasks per node
#SBATCH --account=<project>   # insert here the project to be billed
#SBATCH --time=00:60:00       # time as hh:mm:ss
export PARA_ARCH=MPI          # use MPI
module load turbomole/7.5
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```


## References
Please quote the usage of the program package under consideration of the version
number:

-   TURBOMOLE V7.5 2020, a development of University of Karlsruhe andForschungszentrum Karlsruhe GmbH, 1989-2007,TURBOMOLE GmbH, since 2007; available from https://www.turbomole.org.
-    Scientific publications require proper citation of methods and procedures employed.
The output headers of TURBOMOLE modules include the relevant papers. 

## More information
-   [TURBOMOLE GmbH](https://www.turbomole.org/turbomole/turbomole-documentation/) 
-   [Read About TURBOMOLE](https://aip.scitation.org/doi/10.1063/5.0004635 ) 

