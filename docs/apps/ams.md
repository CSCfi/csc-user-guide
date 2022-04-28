# AMS

The Amsterdam Modeling Suite offers DFT, semi-empirical, reactive force fields and fluid thermodynamics all with an integrated GUI, a powerful AMS driver and python scripting tool PLAMS. The main compute engines are ADF and BAND for electronic structure calculations (DFT), DFTB and MOPAC for more approximate methods to study larger systems.  

## Available

-   Puhti: AMS2022, ADF2022, BAND2022, DFTB2022, MOPAC2022, ReaxFF2022 , Version 2022.101
-   Mahti-rhel8: AMS2022, ADF2022, BAND2022, DFTB2022, MOPAC2022, ReaxFF2022 , Version 2022.101

## License
-  The license entitles software usage by any academic researcher or student of an academic institute where "Academic" means "belonging to a degree-granting institute". 
-  The license does not include the right for employees of government labs or other non-academic non-profit research institutes to use the software. 
-  The license only allows non-profit non-commercial use. 
-  The license excludes all forms of contract research, royalty-bearing activities and other activities leading to monetary benefits.

## Usage

Initialise AMS:

```bash
module load ams/2022.101
```


**Example batch script for Puhti **

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40      # MPI tasks per node
#SBATCH --account=yourproject     # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss
#SBATCH --mem-per-cpu=1500        # requested memory per process in MB
module purge
module load ams/2022.101
export SCM_USE_LOCAL_IMPI=yes
export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
mkdir -p $SCM_TMPDIR

# Copy an example input file
cp -f $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.inp .
"$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
```

!!! note
    Particularly some property calculations can be very disk I/O intensive. Such jobs benefit from using the [fast local storage (NVME)](../../computing/running/creating-job-scripts-puhti/#local-storage) on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Example batch script for Puhti using local disk**

```
#!/bin/bash
#SBATCH --partition=large
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40      # MPI tasks per node
#SBATCH --account=yourproject     # insert here the project to be billed
#SBATCH --time=00:10:00           # time as hh:mm:ss
#SBATCH --mem-per-cpu=1500        # requested memory per process in MB
#SBATCH --gres=nvme:100           # requested local disk space in GB
module load ams/2022.101
export SCM_USE_LOCAL_IMPI=yes
export SCM_TMPDIR=$LOCAL_SCRATCH

# Copy an example input file
cp -f $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.inp .
"$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
```

**Example batch script for Mahti-rhel8**

```
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128 # MPI tasks per node
#SBATCH --account=yourproject # insert here the project to be billed
#SBATCH --time=00:20:00       # time as hh:mm:ss
module purge
module load ams/2022.101
export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
mkdir -p $SCM_TMPDIR

# Copy an example input file
cp -f $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.inp .
"$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
```

### [The AMS-GUI](../apps/ams-gui.md)

AMS comes with an integrated GUI (Graphical User Interface) that makes it easy to set up, run and analyze modelling tasks.
You can test the GUI via the Puhti web interface, but for more extensive use we recommend to install
the GUI on your own laptop/workstation. For detailed instructions, see the [AMS-GUI documentation.](../apps/ams-gui.md)

## References

Depending on your usage, be careful to properly cite the AMS driver, used calculation engines as well as feature references. For details, see the [relevant AMS documentation](https://www.scm.com/doc/Documentation/ ) 

## More information
-   [AMS2022 Support pages](https://www.scm.com/support/)
-   [Tutorials](https://www.scm.com/doc/Tutorials/index.html)
-   [Teaching materials](https://www.scm.com/support/adf-teaching-materials/)
-   [FAQ](https://www.scm.com/faq/)
-   [Newsletter](https://www.scm.com/newsletters/)
