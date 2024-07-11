---
tags:
  - Free
---

# iPyrad

iPyrad is an interactive toolkit for assembly and analysis of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS) for population genetic and phylogenetic studies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Puhti: 0.9.84, 0.9.85, 0.9.92

## Usage

On Puhti, iPyrad can be used by loading the `ipyrad` module:

```bash
module load ipyrad
```

!!! info "Note"
    The actual `ipyrad` command should always be executed in a batch job environment.

For iPyrad tasks that are not computationally heavy, an
[interactive batch job](../computing/running/interactive-usage.md) provides 
a good environment without queuing in between tasks.

You can open an interactive batch job session with the command:

```bash
sinteractive -m 16G
```

iPyrad processing can now be started with the command:

```bash
ipyrad -n taskname
```

This creates a new parameter file (`params-taskname.txt`) that should be edited according to your analysis case.

For example, in the case of job called `run1`:

```bash
ipyrad -n run1
module load nano
nano params-run1.txt
```

Once the parameter file is ready, you can start the actual iPyrad analysis. In interactive batch
jobs you can run small tasks that use just one computing core. Thus, you should add
definition `-c 1` to the `ipyrad` command:

```bash
ipyrad -p params-run1.txt -s 1234567 -c 1
```

## Running heavy iPyrad jobs in Puhti

If you are analyzing large datasets, it is recommended that you run the iPyrad process is several phases. Some steps of the iPyrad analysis can utilize parallel computing. To speed up the processing, you could run these analysis steps as normal batch jobs.

The first two steps are typically executed rather quickly, and you can run them in an interactive batch job environment (see above). 
For example, in the case of job `run1`:

```bash
ipyrad -p params-run1.txt -s 12 -c 1
```

The third step of the iPyrad analysis runs a clustering for each sample set. Before starting this step, study first the content of the `jobname_edits` directory created by step 2. To check how many samples will be analyzed, you can, for example, count the rows in the file `s2_rawedit_stats.txt`.

For example:

```bash
cd run1_edits
ls -l
wc -l s2_rawedit_stats.txt
```

The number of samples is the maximum number of parallel processes you should use in the parallel batch jobs. In practice, you should use a value that is about half of the number of samples. For example, if you have 24 samples in the `*_edits` directory, then you could consider using 12-16 cores.

The parallelization implementation of iPyrad requires that you always have only one iPyrad "task" running in one node. This means that you should always have the batch job parameter `--ntasks-per-node=1`. However, you can define that this task uses several cores with `--cpus-per-task`. For example, if you would assign the number of batch job tasks to 2 (`--ntasks=2`) and number of cores used by one task to 8 (`--cpus-per-task=8`), your job would use 2 * 8 = 16 cores. 

This number of cores (`--ntasks` * `--cpus-per-task`) is then given to the iPyrad command with option `-c`. This is critical, as otherwise iPyrad will only use one core, even if it is requested from Slurm with `--cpus-per-task=8`. Further, if you are using more than one node you should define that MPI is in use (`--MPI`) and that the commands of the pipeline are executed using only one computing core (`-t`).

In the sample case here, we will use 20 cores in one node. If the run time is expected to be more than 3 days, the job should be submitted to longrun partition (`#SBATCH --partition=longrun`). In this case, we reserve 72 hours (3 days). Further, in step 3, the clustering commands are executed using 20 cores (`-c 20`), each running one thread (`-t 1`).

```bash
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s3
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --partition=small

module load ipyrad
ipyrad -p params-run1.txt -s 3 -c 20 -t 1 
```

The batch job is launched with command:

```bash
sbatch ipyrad_batch_job_file.sh
```

Once the job has finished, you could run the next step by replacing `-s 3` with `-s 4` etc.

For the setups 4-7, a maximum of 8 cores is recommended. Thread assigning option should always be set, as the default settings of iPyrad are not suitable for batch jobs.

```bash
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s4567
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small

module load ipyrad
ipyrad -p ipyrad-run1.txt -s 4567 -c 8 -t 1 
```

More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).

## Using cPouta for very long iPyrad jobs

The maximum run time on Puhti is 14 days. In some cases, running the iPyrad analysis step 3 may take even longer time. In those cases, you can use the
[cPouta cloud service](../cloud/pouta/index.md) to set up your own virtual machine.

## More information

* [ipyrad home page](https://ipyrad.readthedocs.io/)
