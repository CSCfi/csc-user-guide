---
tags:
  - Academic
catalog:
  name: AMS
  description: Modelling suite providing the ADF engine
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# AMS

The Amsterdam Modeling Suite (AMS) is a comprehensive suite of computational chemistry software. It comes with a graphical user interface, [AMS-GUI](ams-gui.md) 
that provides an intuitive way for setting up, running, and analyzing simulations.

## Available

-   Puhti: AMS, Version 2024.102, 2025.105
-   Mahti: AMS, Version 2024.102, 2025.105
-   Roihu-CPU: AMS, Version 2026.104

## License
-  The license entitles software usage by any academic researcher or student of an academic institute where "Academic" means "belonging to a degree-granting institute". 
-  The license does not include the right for employees of government labs or other non-academic non-profit research institutes to use the software. 
-  The license only allows non-profit non-commercial use. 
-  The license excludes all forms of contract research, royalty-bearing activities and other activities leading to monetary benefits.
-  Research groups which need other modules of the AMS suite can obtain a license for themselves to run the programs on the CSC computers. 

## Usage

Initialize AMS on Puhti and Mahti:

```bash
module load ams/2025.105
```

Initialize AMS on Roihu-CPU:

```bash
module load ams/2026.104
```

### Example batch scripts

!!! warning "Note"
    Particularly some property calculations can be very disk I/O intensive. Such jobs benefit from using the fast local storage (NVMe) on [Puhti](../computing/running/creating-job-scripts-puhti.md#local-storage), [Mahti](../computing/running/example-job-scripts-mahti.md#local-disk-and-small-partition), or [Roihu](../computing/roihu-disk.md). Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

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
    module load ams/2025.105
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
    module load ams/2025.105
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
    module load ams/2025.105
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR

    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

=== "Mahti, local disk"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128 # MPI tasks per node
    #SBATCH --account=yourproject # insert here the project to be billed
    #SBATCH --time=00:20:00       # time as `hh:mm:ss`
    #SBATCH --gres=nvme:100
    module purge
    module load ams/2025.105
    export SCM_TMPDIR=$LOCAL_SCRATCH
    mkdir -p $SCM_TMPDIR
    
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

=== "Roihu-CPU"

    ```bash
    #!/bin/bash
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks=128              # MPI tasks
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:20:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500M       # requested memory per process
    module purge
    module load ams/2026.104
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

    !!! tip "Choosing core counts on Roihu-CPU"
        Roihu M-nodes have 384 cores, but ADF does not scale efficiently to a full
        node for typical jobs. The table below shows scaling for the Si35_TZ2P
        benchmark — note that scaling is strongly system- and model-dependent, so
        these numbers should be used as a guide rather than absolute values.
        **128–192 cores gives the best balance of efficiency and speed** for this
        case. Beyond that, wall time barely improves while memory usage and billing
        costs increase significantly. For full-node jobs, use local NVMe scratch
        (see the "Roihu-CPU, local disk" tabs) to avoid I/O contention from AMS's
        per-rank scratch files.

        | MPI ranks | CPU efficiency | Wall time |
        |-----------|----------------|-----------|
        | 48        | ~95%           | ~437 s    |
        | 96        | ~91%           | ~385 s    |
        | 128       | ~90%           | ~302 s    |
        | 192       | ~85%           | ~252 s    |
        | 384 (full node) | ~75%    | ~247 s    |

=== "Roihu-CPU, local disk"

    ```bash
    #!/bin/bash
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks=128              # MPI tasks
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:20:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500M       # requested memory per process
    module purge
    module load ams/2026.104
    # On Roihu, local NVMe scratch is available via $TMPDIR (no --gres flag needed)
    export SCM_TMPDIR=$TMPDIR/ams_$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

    !!! tip "See also"
        See the "Roihu-CPU" tab for core-count recommendations. For full-node
        jobs requiring maximum I/O performance, consider the disaggregated NVMe
        option in the "Roihu-CPU, disaggregated NVMe" tab.

        Maximum amount of local NVMe disk available in `$TMPDIR` depends on the Slurm partition and node type.
        On shared nodes (e.g. on the `small` and `longrun` partitions), you have access to 20 GiB of tmp storage.
        On full nodes (`medium` and `large` partitions), you have access to 600 GiB of local storage.
        See [Roihu storage documentation](../computing/roihu-disk.md#automatic-local-temporary-storage) for more details.

=== "Roihu-CPU, disaggregated NVMe"

    !!! info "Disaggregated NVMe on Roihu"
        Roihu provides a centralised pool of 307.2 TB fast NVMe storage served over
        InfiniBand NDR. For I/O-intensive full-node jobs this can outperform both
        Lustre scratch and node-local `$TMPDIR`. It requires a full-node partition
        (`medium` or `large`) and a `#BB_LUA` burst-buffer directive — shared-node
        support is not yet available. See
        [Roihu disk areas](../computing/roihu-disk.md#disaggregated-storage)
        for full details.

    ```bash
    #!/bin/bash
    #SBATCH --partition=medium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=384     # full node required for disaggregated NVMe
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:20:00           # time as `hh:mm:ss`
    #BB_LUA SBF storagesize=100GB path=/run/sbb/<user>
    module purge
    module load ams/2026.104
    # Disaggregated NVMe is mounted at the path specified in #BB_LUA above
    export SCM_TMPDIR=/run/sbb/<user>/ams_$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

    !!! tip "Benchmark results for Si35_TZ2P at 384 ranks"
        Benchmarking showed that disaggregated NVMe gives the best performance for
        full-node ADF jobs, outperforming both Lustre scratch and node-local `$TMPDIR`:

        | Scratch location | Wall time | CPU efficiency | Billing units |
        |------------------|-----------|----------------|---------------|
        | Lustre scratch   | ~247 s    | ~75%           | ~20 BU        |
        | `$TMPDIR` (node-local) | ~230 s | ~91%        | ~19 BU        |
        | Disaggregated NVMe | **~190 s** | ~89%       | **~15 BU**    |

        Note that scaling is strongly system- and model-dependent. See the
        "Roihu-CPU" tab for guidance on choosing core counts.

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
