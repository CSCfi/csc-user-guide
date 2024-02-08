---
tags:
  - Academic
---

# TURBOMOLE

[TURBOMOLE](https://www.turbomole.org/turbomole/turbomole-features/) is a fast
and robust quantum chemistry program package with very efficient
implementations of various computational methods (HF/DFT/MP2/CC). Properties
both for ground and excited states can be obtained. TURBOMOLE has been designed
for efficient study of large systems. 

## Available

- Puhti: 7.5.1, 7.6, 7.7, 7.8
- Mahti: 7.5.1, 7.6, 7.7, 7.8

## License

- You may use the Software exclusively for non-profit research
  purposes.
- Only users from academic (i.e. degree-granting) institutes are
  allowed to use the Software

## Usage

Initialise TURBOMOLE environment:

```bash
module load turbomole/7.8
```

### Batch script example for Puhti using MPI parallelization

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as `hh:mm:ss`
export PARA_ARCH=MPI         # use MPI 
module load turbomole/7.8
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### Batch script example for Puhti using SMP parallelization

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1            # for SMP only 1 is possible
#SBATCH --cpus-per-task=40   # SMP threads
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
export PARA_ARCH=SMP         # use SMP threads   
module load turbomole/7.8
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_CPUS_PER_TASK  # for SMP
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

!!! info "Note"
    Occasionally `mpshift` calculations are terminated due to the local `/tmp`
    becoming full. The problem can be circumvented by redefining `$TMPDIR`:
    ```bash
    export TMPDIR=$TURBOTMPDIR
    ```

!!! info "Note"
    Particularly some of the wavefunction-based electron correlation methods
    can be very disk I/O intensive. Such jobs benefit from using the fast local
    storage on Puhti. Using local disk for such jobs will also reduce the load
    on the Lustre parallel file system.
 
### Batch script example for Puhti using MPI parallelization and local disk

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
#SBATCH --gres=nvme:100      # requested local disk in GB
export PARA_ARCH=MPI         # use MPI
module load turbomole/7.8
export SLURM_CPU_BIND=none
# define local disk as scratch
export TURBOTMPDIR=$LOCAL_SCRATCH/$SLURM_JOBID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
dscf > dscf.out
ccsdf12 > ccsdt.out
```

### Batch script example for Mahti using MPI parallelization

```bash
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128 # MPI tasks per node
#SBATCH --account=<project>   # insert here the project to be billed
#SBATCH --time=00:60:00       # time as `hh:mm:ss`
export PARA_ARCH=MPI          # use MPI
module load turbomole/7.8
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### NumForce calculations

NumForce is a tool that can be used to calculate second derivatives (molecular
Hessian) for all methods for which analytic gradients are available in
`TURBOMOLE`. A NumForce job spawns `3*N*2` (`N` = number of atoms) independent
gradient calculations.  Usually it is most efficient that the single gradient
calculations are run as serial (`unset PARA_ARCH`). Each serial calculation is
expected to take roughly the same time, hence optimally the total number of
gradient calculations should be an integer multiple of the allocated cores.

A NumForce step in a job file:

```bash
unset PARA_ARCH
export HOSTS_FILE=$PWD/turbomole.machines
rm -f $HOSTS_FILE
srun hostname > $HOSTS_FILE
ulimit -s unlimited
kdg tmpdir
NumForce -ri -central -mfile $HOSTS_FILE > NumForce.out
```

## References

Please quote the usage of the program package under consideration of the
version number:

- TURBOMOLE V7.8, a development of University of Karlsruhe and
  Forschungszentrum Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, since 2007;
  available from https://www.turbomole.org
- A review article should be mentioned, as well:
  https://doi.org/10.1063/5.0004635
- Scientific publications require proper citation of methods and procedures
  employed. The output headers of TURBOMOLE modules include the relevant
  papers. 

## More information

- [TURBOMOLE GmbH](https://www.turbomole.org/turbomole/turbomole-documentation/) 
- [TURBOMOLE: Today and Tomorrow](https://pubs.acs.org/doi/10.1021/acs.jctc.3c00347)
- [TURBOMOLE review](https://aip.scitation.org/doi/10.1063/5.0004635) 
- [TURBOMOLE tutorial](https://www.turbomole.org/wp-content/uploads/Tutorial_7-7.pdf)
- [TURBOMOLE Users Forum](https://forum.turbomole.org/index.php)
