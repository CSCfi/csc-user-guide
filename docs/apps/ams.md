# AMS

The Amsterdam Modeling Suite offers DFT, semi-empirical, reactive force fields and fluid thermodynamics all with an integrated GUI, a powerful AMS driver and python scripting tool PLAMS. The main compute engines are ADF and BAND for electronic structure calculations (DFT), DFTB and MOPAC for more approximate methods to study larger systems.  

## Available

-   Puhti: AMS2019, ADF2019, BAND2019, DFTB2019, MOPAC2019, ReaxFF2019 

## License
-  The license entitles software usage by any academic researcher or student of an academic institute where "Academic" means "belonging to a degree-granting institute". 
-  The license does not include the right for employees of government labs or other non-academic non-profit research institutes to use the software. 
-  The license only allows non-profit non-commercial use. 
-  The license excludes all forms of contract research, royalty-bearing activities and other activities leading to monetary benefits.

## Usage

Initialise AMS on Puhti like this:

```bash
module load adf/2019.104
```


**Example batch script for Puhti **

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss

ulimit -s unlimited
export SCM_TMPDIR=$PWD/SCM_TMP_$SLURM_JOB_ID
mkdir -p $SCM_TMPDIR
export SCM_USE_LOCAL_IMPI=yes
module purge
module load intel/19.0.4 intel-mpi/18.0.5 
module load adf/2019.104

$ADFBIN/adf < methane_dimer_dispersion.inp > methane_dimer_dispersion.log
seff $SLURM_JOBID
```
!!! note
    Particularly some property calculations can be very disk I/O intensive. Such jobs benefit from using the fast local storage on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Example batch script for Puhti using local disk**

```
#!/bin/bash
#SBATCH --partition=large
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss
#SBATCH --gres=nvme:100      # requested local disk space in GB 
ulimit -s unlimited
export SCM_TMPDIR=$LOCAL_SCRATCH/$SLURM_JOB_ID
mkdir -p $SCM_TMPDIR
export SCM_USE_LOCAL_IMPI=yes
module purge
module load intel/19.0.4 intel-mpi/18.0.5
module load adf/2019.104

$ADFBIN/adf < methane_dimer_dispersion.inp > methane_dimer_dispersion.log
seff $SLURM_JOBID
```
### The AMS-GUIs

The present CSC license also allows CSC users to install the Graphical User Interfaces on their local workstations. For details contact CSC Service Desk , servicedesk@csc.fi .

## References

Depending on your usage, be careful to properly cite the AMS driver, used calculation engines as well as feature references. For details, see the [relevant documentation](https://www.scm.com/support/ ) 

## More information
-   [AMS2019 Support pages](https://www.scm.com/support/)
-   [Tutorials](https://www.scm.com/doc/Tutorials/index.html)
-   [Teaching materials](https://www.scm.com/support/adf-teaching-materials/)
-   [FAQ](https://www.scm.com/faq/)
