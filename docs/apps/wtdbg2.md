---
tags:
  - Free
catalog:
  name: wtdbg2
  description: Fast assembler for long-read data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# wtdbg2

wtdbg2 is a fast _de novo_ assembly tool for long-read sequence data produced by PacBio or Oxford Nanopore Technologies sequencers.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Roihu-CPU: 2.5, via the `bio-apps` module.

## Usage

wtdbg2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the wtdbg2 module:

```bash
module load bio-apps/v202603
module load wtdbg2/2.5
```

After that, you can use the `wtdbg2` assembler and the `wtpoa-cns` consenser. `wtdbg2` assembles raw reads and generates the contig layout and edge sequences in a file `prefix.ctg.lay.gz`. Executable `wtpoa-cns` takes this file as input and produces the final consensus in FASTA.

A typical workflow looks like this:

```bash
wtdbg2 -x rs -g 4.6m -t 16 -i reads.fa.gz -fo prefix
wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa
```

In the `wtdbg2` command, `-g` is the estimated genome size and `-x` specifies the sequencing technology, which could take value `rs` for PacBio RSII, `sq` for PacBio Sequel, `ccs` for PacBio CCS reads and `ont` for Oxford Nanopore. This option sets multiple parameters and should be applied before other parameters. When you are unable to get a good assembly, you may need to tune other parameters as described in the wtdbg2 manual.

In the case of any large (more than 10 Mb) genomes, wtdbg2 assembly process can take several hours or days. On Roihu, such large tasks should always be executed as batch jobs.

Below is a sample batch job file for assembling _C. elegans_ genome.

The sample dataset (about 16 GB) was downloaded from the ENA database with the command:

```bash
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR543/004/SRR5439404/SRR5439404_subreads.fastq.gz
```

The actual assembly task was executed with the batch job below:

```bash
#!/bin/bash
#SBATCH --job-name=wtdbg2
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --partition=small

module load bio-apps/v202603
module load wtdbg2/2.5

wtdbg2 -x rs -g100m -t $SLURM_CPUS_PER_TASK -i SRR5439404_subreads.fastq.gz -fo c_elegans_test
wtpoa-cns -t $SLURM_CPUS_PER_TASK -i c_elegans_test.ctg.lay.gz -fo c_elegans.ctg.fa
```

In the example above `<project>` should be replaced with your project name. You can use `csc-projects` to check your CSC projects. Maximum running time is set to 12 hours (`--time=12:00:00`). As wtdbg2 uses thread-based parallelization, the process is considered as one job that should be executed within one node (`--nodes=1`, `--ntasks=1`). The job reserves 32 cores `--cpus-per-task=32` that can use in total up to 64 GB of memory (`--mem=64G`). Note that the number of cores to be used needs to be defined in `wtdbg2` and `wtpoa-cns` commands too. This can be set with the option `-t`. In this case, we use `$SLURM_CPUS_PER_TASK` variable that contains the `--cpus-per-task` value (we could as well use `-t 32`, but then we have to remember to change the value if the number of the reserved CPUs is changed later).

The job is submitted to the batch job system with `sbatch` command. For example, if the batch job
file is named `wtdbg2_job.sh`, then the submission command is:

```bash
sbatch wtdbg2_job.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [wtdbg2 home page](https://github.com/ruanjue/wtdbg2)
