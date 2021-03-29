# Megahit

## Description

Megahit is an ultra fast assembly tool for metagenomics data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Version on CSC's Servers

-   Puhti: 1.2.8

## Usage

In Puhti, Megahit is activated by loading the _biokit_ environment.

```text
module load biokit
```
For usage help use command:
```text
megahit -h
```
Assembling metagenomic data can be very resource demanding. Note that you should not run Megahit in the login nodes of Puhti.
For any real analysis task we recommend running Megahit as a batch job.


Sample Megahit batch job:
```text
#!/bin/bash
#SBATCH --job-name=Megahit
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=megahit_out_8
#SBATCH --error=megahit_err_8
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --partition=small


module load biokit
srun megahit -1 reads_1.fastq -2 reads_2.fastq -t $SLURM_CPUS_PER_TASK --m 32000000000 -o result_directory
```
In the example above _<project>_ could be replaced with your project name. You can use `csc-workspaces` to check your Puhti projects. Maximum running time is 
set to 12 hours (`--time=12:00:00`). As Megahit uses threads based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--nodes=1`). The job reserves eight cores `--cpus-per-task=8` that can use in total up to 32 GB of memory  (` --mem=32G`). Note that the number of cores to be used needs to be defined in actual Megahit command
too. That is done with Megahit option `-t`. In this case we use $SLURM_CPUS_PER_TASK variable that contains the _cpus-pre-task_ 
value ( we could as well use `-t 8` but then we have to remember to change the value if number of the reserved CPU:s is changed).

The job is submitted to the to the batch job system with `sbatch` command. For example, if the batch job
file is named as _megahit_job.sh_ then the submission command is: 
```text
sbatch megahit_job.sh 
```
More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).



## Manual

*   [Megahit home page](https://github.com/voutcn/megahit)





