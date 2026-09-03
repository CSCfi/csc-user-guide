---
tags:
  - Free
catalog:
  name: Megahit
  description: Metagenomics assembly
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Megahit

Megahit is an ultra-fast assembly tool for metagenomics data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 1.2.9, via the `bio-apps` module.

## Usage

Megahit is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Megahit module:

```bash
module load bio-apps/v202603
module load megahit/1.2.9
```

For usage help, use command:

```bash
megahit -h
```

Assembling metagenomic data can be very resource demanding. Note that you should not run Megahit on the login nodes.
For any real analysis task, we recommend running Megahit as a batch job.

Sample Megahit batch job:

```bash
#!/bin/bash
#SBATCH --job-name=Megahit
#SBATCH --account=<project>
#SBATCH --output=megahit_out_%j
#SBATCH --error=megahit_err_%j
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module load bio-apps/v202603
module load megahit/1.2.9

srun megahit -1 reads_1.fastq -2 reads_2.fastq -t $SLURM_CPUS_PER_TASK --m 32000000000 -o result_directory
```

In the example above `<project>` should be replaced with your project name. You can use `csc-projects` to check your CSC projects. Maximum running time is 
set to 12 hours (`--time=12:00:00`). As Megahit uses thread-based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--nodes=1`). The job reserves eight cores (`--cpus-per-task=8`) that can use in total up to 32 GB of memory (` --mem=32G`). Note that the number of cores to be used needs to be defined in actual Megahit command
too. That is done with Megahit option `-t`. In this case we use `$SLURM_CPUS_PER_TASK` variable that contains the `--cpus-per-task` 
value (we could as well use `-t 8`, but then we have to remember to change the value if the number of the reserved CPUs is changed).

The job is submitted to the batch job system with `sbatch` command. For example, if the batch job
file is named as `megahit_job.sh`, then the submission command is:

```bash
sbatch megahit_job.sh 
```

More information about running batch jobs can be found from [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Megahit home page](https://github.com/voutcn/megahit)
