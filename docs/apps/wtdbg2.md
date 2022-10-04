# wtdbg2

## Description

wtdbg2 is a fast _de novo_ assembly tool for long-read sequece data produced by PacBio or Oxford Nanopore Technologies sequencers.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Version on CSC's Servers

-   Puhti: 2.5

## Usage

In Puhti, the wtdbg2 is activated by loading the biokit environment.

```text
module load biokit
```

After that you can use commands `wtdbg2` asembler and `wrpoa-cns` consenser commands. _wtdbg2_ assembles raw reads and generates the contig layout and edge sequences in a file _prefix_.ctg.lay.gz. Executable _wtpoa-cns_ takes this file as input and produces the final consensus in FASTA. 


A typical workflow looks like this:

```text 
wtdbg2 -x rs -g 4.6m -t 16 -i reads.fa.gz -fo prefix
wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa
```

In the wtdbg2 command `-g` is the estimated genome size and `-x` specifies the sequencing technology, which could take value _rs_ for PacBio RSII, _sq_ for PacBio Sequel, _ccs_ for PacBio CCS reads and _ont_ for Oxford Nanopore. This option sets multiple parameters and should be applied before other parameters. When you are unable to get a good assembly, you may need to tune other parameters as described in the wtdbg2 manual.

In the case of any large ( more than 10 Mb) genomes,  wtdbg2 assembly process can take several hours or days. In Puhti, this large tasks shoud always be executed as batch jobs.

Below is a sample batch job file for assembling C. elegans genome. 

The sample dataset was downloaded from ENA database with commands:

```text
enaDataGet SRR5439404 -f fastq
mv SRR5439404/SRR5439404_subreads.fastq.gz ./
```

The actutal assembly task was executed with the batch job below:

```text
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
In the example above _<project>_ could be replaced with your project name. You can use `csc-workspaces` to check your Puhti projects. Maximum running time is set to 12 hours (`--time=12:00:00`). As wtdbg2 uses threads based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--ntasks=1`). The job reserves 32 cores `--cpus-per-task=32` that can use in total up to 64 GB of memory  (` --mem=64G`). Note that the number of cores to be used needs to be defined in wtdbg2 and wtpoa-cns commands too. That is done with option `-t`. In this case we use `$SLURM_CPUS_PER_TASK` variable that contains the _cpus-pre-task_  value ( we could as well use `-t 32` but then we have to remember to change the value if number of the reserved CPU:s is changed).

The job is submitted to the to the batch job system with `sbatch` command. For example, if the batch job
file is named as _wtdbg2_job.sh_ then the submission command is: 
```text
sbatch wtdbg2_job.sh 
```
More information about runnig batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).



## Manual

*   [wtdbg2 home page](https://github.com/ruanjue/wtdbg2)





