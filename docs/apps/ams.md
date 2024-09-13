---
tags:
  - Academic
---

# AMS

The Amsterdam Modeling Suite (AMS) is a comprehensive suite of computational chemistry software. It comes with a graphical user interface, [AMS-GUI](ams-gui.md) 
that provides an intuitive way for setting up, running, and analyzing simulations.

## Available

-   Puhti: ADF, Version 2024.102
-   Mahti: ADF, Version 2024.102

## License
-  The license entitles software usage by any academic researcher or student of an academic institute where "Academic" means "belonging to a degree-granting institute". 
-  The license does not include the right for employees of government labs or other non-academic non-profit research institutes to use the software. 
-  The license only allows non-profit non-commercial use. 
-  The license excludes all forms of contract research, royalty-bearing activities and other activities leading to monetary benefits.
-  Research groups which need other modules of the AMS suite can obtain a license for themselves to run the programs on the CSC computers. 

## Usage

Initialize AMS:

```bash
module load ams/2024.102
```

### Example batch scripts

!!! warning "Note"
    Particularly some property calculations can be very disk I/O intensive. Such jobs benefit from using the [fast local storage (NVMe)](../../computing/running/creating-job-scripts-puhti/#local-storage) on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

=== "Puhti"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed 
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500        # requested memory per process in MB
    module purge
    module load ams/2024.102
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    # Create an example input file from the examples 
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```
     
=== "Puhti, local disk"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500        # requested memory per process in MB
    #SBATCH --gres=nvme:100           # requested local disk space in GB
    module load ams/2024.102
    export SCM_TMPDIR=$LOCAL_SCRATCH
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

=== "Mahti"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=medium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128 # MPI tasks per node
    #SBATCH --account=yourproject # insert here the project to be billed
    #SBATCH --time=00:20:00       # time as `hh:mm:ss`
    module purge
    module load ams/2024.102
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

### [The AMS-GUI](../apps/ams-gui.md)

AMS comes with an integrated Graphical User Interface, [AMS-GUI](ams-gui.md) that makes it easy to set up, run and analyze modelling tasks.
You can test the GUI via the Puhti web interface, but for more extensive use we recommend installing
the GUI on your own laptop/workstation. For detailed instructions, see the [AMS-GUI documentation.](ams-gui.md)

## References

Depending on your usage, be careful to properly cite the AMS driver, used calculation engines as well as feature references. For details, see the [relevant AMS documentation](https://www.scm.com/doc/Documentation/ ) 

## More information

-   [AMS support pages](https://www.scm.com/contact-us/)
-   [Tutorials](https://www.scm.com/doc/Tutorials/index.html)
-   [Workshops](https://www.scm.com/workshops/)
-   [FAQ](https://www.scm.com/faq/)
-   [Knowledge bank](https://www.scm.com/knowledgebank/)
-   [The latest news](https://www.scm.com/news/)
