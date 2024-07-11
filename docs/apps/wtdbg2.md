---
tags:
  - Free
---

# wtdbg2

wtdbg2 is a fast _de novo_ assembly tool for long-read sequence data produced by PacBio or Oxford Nanopore Technologies sequencers.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Puhti: 2.5

## Usage

On Puhti, wtdbg2 is activated by loading the biokit module:

```bash
module load biokit
```

After that, you can use commands `wtdbg2` assembler and `wrpoa-cns` consenser commands. `wtdbg2` assembles raw reads and generates the contig layout and edge sequences in a file `prefix.ctg.lay.gz`. Executable `wtpoa-cns` takes this file as input and produces the final consensus in FASTA. 


A typical workflow looks like this:

```bash 
wtdbg2 -x rs -g 4.6m -t 16 -i reads.fa.gz -fo prefix
wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa
```

In the `wtdbg2` command, `-g` is the estimated genome size and `-x` specifies the sequencing technology, which could take value `rs` for PacBio RSII, `sq` for PacBio Sequel, `ccs` for PacBio CCS reads and `ont` for Oxford Nanopore. This option sets multiple parameters and should be applied before other parameters. When you are unable to get a good assembly, you may need to tune other parameters as described in the wtdbg2 manual.

In the case of any large (more than 10 Mb) genomes, wtdbg2 assembly process can take several hours or days. On Puhti, such large tasks should always be executed as batch jobs.

Below is a sample batch job file for assembling _C. elegans_ genome. 

The sample dataset was downloaded from ENA database with commands:

```bash
enaDataGet SRR5439404 -f fastq
mv SRR5439404/SRR5439404_subreads.fastq.gz ./
```

The actual assembly task was executed with the batch job below:

```bash
#!/bin/bash
#SBATCH --job-name=wtdbg2
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output==wtdbg2_out_32_%j
#SBATCH --error=wtdbg2_err_32_%j
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --partition=small

module load biokit

wtdbg2 -x rs -g100m -t $SLURM_CPUS_PER_TASK -i SRR5439404_subreads.fastq.gz -fo c_elegas_test
wtpoa-cns -t $SLURM_CPUS_PER_TASK -i c_elegas_test.ctg.lay.gz -fo c_elegabs.ctg.fa
```

In the example above `<project>` should be replaced with your project name. You can use `csc-projects` to check your CSC projects. Maximum running time is set to 12 hours (`--time=12:00:00`). As wtdbg2 uses thread-based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--ntasks=1`). The job reserves 32 cores `--cpus-per-task=32` that can use in total up to 64 GB of memory (`--mem=64G`). Note that the number of cores to be used needs to be defined in `wtdbg2` and `wtpoa-cns` commands too. This can be set with the option `-t`. In this case, we use `$SLURM_CPUS_PER_TASK` variable that contains the `--cpus-per-task` value (we could as well use `-t 32`, but then we have to remember to change the value if the number of the reserved CPUs is changed later.

The job is submitted to the batch job system with `sbatch` command. For example, if the batch job
file is named `wtdbg2_job.sh`, then the submission command is: 

```bash
sbatch wtdbg2_job.sh 
```

More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).

## More information

* [wtdbg2 home page](https://github.com/ruanjue/wtdbg2)
