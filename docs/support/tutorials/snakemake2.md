# Running Snakemake workflow on Puhti

[Snakemake workflow](../../apps/snakemake.md) is one of the popular scientific workflows in the bioinformatics community, although the workflow manager itself can be used in other scientific disciplines as well. Snakemake enables scalable and reproducible scientific pipelines by chaining a series of rules in a fully-specified software environment. 

## Installation
Snakemake is available as a module in Puhti supercomputer. This options suits well, if the workflow includes commandline-tools from other modules or Apptainer containers. 

```
module load snakemake
snakemake --help   #  to get information on more options.
```

To use commandline tools from other modules, load also these modules. 

To use tools installed as Apptainer containers:

* Add [`--use-apptainer`](https://snakemake.readthedocs.io/en/stable/executing/cli.html#apptainer/singularity) to your `snakemake` command
* [Specify the container](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#running-jobs-in-containers) path at the top level of the Snakefile or for each rule:

```
singularity: "image/tutorial.sif"
```

If the workflow includes Python scripts that require custom Python packages, make own Snakemake installation with Tykky. 

### Snakemake Tykky installation for Python
To install Snakemake with custom Python packages, use [Tykky container wrapper tool with conda](../../computing/containers/tykky.md#conda-based-installation). Follow the guidelines on Tykky page, the conda environment should include package `snakemake`. If you plan to use Snakemake with SLURM or HyperQueue integration (explained below), install also `snakemake-executor-plugin-slurm` for SLURM or `snakemake-executor-plugin-cluster-generic` for HyperQueue. 

If you use own Tykky installation, then in the examples below, replace `module load snakemake` with the export commant printed out by Tykky, something like: `export PATH="/projappl/project_xxxx/$USER/snakemake_tykky/bin:$PATH"`

Please note, create one Tykky installation for the whole workflow, not individual installations for each job step.


## Usage
Snakemake can be run in 4 different ways in supercomputers:

1) [In interactive mode](../../computing/running/interactive-usage.md) with local executor, with limited resources. Useful mainly for debugging or very small workflows.
2) With batch job and local executor. Resource usage limited to one full node. Useful for small and medium size workflows, simpler than next options, start with this if unsure.
3) With batch job and SLURM executor. Can use multiple nodes and different SLURM partitions (CPU and GPU), but may create significant overhead, if many small jobs. Could be used, if each job step for each file takes at least 30 min.
4) With batch job and HyperQueue as a sub-job scheduler. Can use multiple nodes, most complex set upt. Suits well for cases, when workflow includes a lot of small job steps.

!!! info "Note"
        Please do not launch heavy Snakemake workflows on **login nodes**.

The following toy example illustrates how a Snakemake workflow can be deployed at CSC. 

### Snakefile
Snakefile describes the contents of the workflow. Further information is available from [Snakemake Snakefile documentation](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html)

Let's use the following toy Snakemake script, `Snakefile` (with a capital S and no file extension), for the illustration:

```bash title="Snakefile"
rule all:
        input: "CAPITAL_CASE.txt"

rule say_hello:
        output: "smaller_case.txt"
        shell:
                """
                echo "hello-world greetings from csc to snakemake community !" > smaller_case.txt
                """
rule capitalise:
        input: "smaller_case.txt"
        output: "CAPITAL_CASE.txt"
        shell:
                """
                tr '[:lower:]' '[:upper:]' < {input} > {output}
                """
```

### Running Snakemake workflow with local executor interactively
The resources are reserved in advance, both for Snakemake and the workflow jobs as **one interactive session**. In interactive session, the workflow can be started for several times for debugging as long as the reserved resources are available. See resource limits for [interactive partition](../../computing/running/batch-job-partitions.md).

```
sinteractive --cores 2 --mem 10000 # start an interactive session with 2 CPU cores and 10 Gb of memory
module load snakemake
cd <to_folder_with_snakefile>
snakemake -s Snakefile --jobs 2
```

### Running Snakemake workflow with local executor and batch job
The resources are reserved in advance, both for Snakemake and the workflow as **one batch job**. The job will run as long as the snakemake command is running and stop automatically when it finishes. Local executor is limited to one node of supercomputer. The number cores can be extended depending on the system - 40 in Puhti and 128 in Mahti.

```bash title="tutorial-sbatch.sh"
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=small
#SBATCH --cpus-per-task=4

module load snakemake
snakemake -s Snakefile --jobs 2
```
Finally, you can submit the batch job from the login nodes as below:

```bash
sbatch tutorial-sbatch.sh
```

### Running Snakemake workflow with SLURM executor
The first batch job file reserves resources only for Snakemake itself. Snakemake then creates further SLURM jobs for workflow's job steps. This enables using several nodes on a supercomputer and also to use different partitions for different workflow steps, for example CPU and GPU. SLURM executor should be used only, if the job steps are at least 20-30 minutes long, otherwise the it could overload SLURM.

Here is a bash script for running the above toy example with SLURM executor:

```bash
#!/bin/bash
#SBATCH --job-name=snakemake_slurm
#SBATCH --account=project_2008498
#SBATCH --time=00:20:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --partition=small
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

module load snakemake
snakemake --jobs 2  -s Snakefile --executor slurm --default-resources slurm_account=project_xxxx slurm_partition=small
```
!!! info "Note"
        Make sure that the Snakemake own reservation is long enough to include also waiting time for other processes to get processed, including queueing time.

Default resources for each SLURM job are rather limited, to increase (or change) define the resource needs for each rule in the Snakefile:
```
rule say_hello:
        output: "smaller_case.txt"
            resources:
                runtime = 5, # minutes
                cpus_per_task = 1,
                mem_mb = 20000,
        shell:
                """
                echo "hello-world greetings from csc to snakemake community !" > smaller_case.txt
                """
```
Further information about [Snakemake SLURM executor](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/slurm.html)

!!! info "Note"
    Scaling up your jobs using Slurm should be done carefully to
    avoid unnecessarily overloading the Slurm accounting database with a large number of small jobs.
    Consider either configuring **localrules** cautiously with Slurm, or using Hyperqueue executor.


## Running Snakemake with HyperQueue executor
The resources are reserved in advance, both for Snakemake and the workflow as **one batch job**. It is possible to use several nodes on a supercomputer, but not to use different partitions for different workflow steps, for example CPU and GPU. HyperQueue executor fits well to workflows which have a lot of short job steps, because it "hides" them from SLURM. 

```bash
#!/bin/bash
#SBATCH --job-name=snakemake_hq
#SBATCH --account=project_2008498
#SBATCH --time=00:20:00
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu=40GB
#SBATCH --partition=small
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

module load hyperqueue
export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
mkdir -p "$HQ_SERVER_DIR"
hq server start & until hq job list &> /dev/null ; do sleep 1 ; done

srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" & hq worker wait 1

snakemake --keep-going -s Snakefile_SLURM --jobs 2 --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 1"

```
See [CSC HyperQueue page](https://docs.csc.fi/apps/hyperqueue/#using-hyperqueue-in-a-slurm-batch-job) for more options and details about HyperQueue.

!!! info "Note"
    HyperQueue creates task-specific folders (`job-<n>`) in the same directory
    from where you submitted the batch script. These are sometimes useful for
    debugging. However, if your code is working fine, the creation of many folders
    may be annoying besides causing some load on the Lustre parallel file system.
    You can prevent the creation of such task-specific folders by setting `stdout`
    and `stderr` HyperQueue flags to `none` ( i.e., `hq submit --stdout=none --stderr=none ...`)
