# MrBayes

## Description

MrBayes is a program for the Bayesian inference on phylogenies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Version on CSC's Servers

-   Puhti: 3.2.7a

## Usage

To check available versions use:
```text
module spider mrbayes
```
To load a specific version:
```text
module load mrbayes/3.2.7a
```
After loading the module, the serial (i.e. single processor) version starts with command
```text
mb
```
Parallel version starts with command:
```text
mb-mpi 
```
When using the parallel version, you should note that MrBayes assigns one chain to one core, so for optimal performance you should use as many cores as the total number of chains in your job. If you for example have specified `nchains=4`, `nruns=2` you should use 8 cores (4*2).

## Batch jobs

Running MrBayes analysis might take considerable amount of CPU time and memory. It is recommended to run it through the batch job system in Puhti. Shorter test runs can be run in interactive mode using [sinteractive](../computing/running/interactive-usage.md). The serial version is recommended for interactive use.

To run a batch job you need to:

* Write a MrBayes command file (here "mb_com.nex") or include mrbayes command block in your .nex file. For details, see chapter 5.5.1 of the MrBayes manual.
* Write a batch job script (here "mb_batch")
* Make sure you have all your input files (here "primates.nex")
* Submit your job into the queue

MrBayes command file should include the commands you would type in MrBayes in interactive mode. This example 
runs the analysis in chapter 2 of the MrBayes 3.2 manual.

```text
begin mrbayes;
    set autoclose=yes nowarn=yes;
    execute primates.nex;
    lset nst=6 rates=invgamma;
    mcmc nchains=4 nruns=2 ngen=20000 samplefreq=100 printfreq=100 diagnfreq=1000;
    sump;
    sumt;
end;
```

Example batch job script for Puhti using 8 cores. (We are using 8 cores since our example uses nchains=4, nruns=2, so 4*2=8.)

```text
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=my_mrbjob
#SBATCH --error=my_mrbjob_err%j
#SBATCH --output=my_mrbjob_out%j
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=01:00:00
#SBATCH --partition=small

srun mb-mpi mb_com.nex >log.txt
```
To submit the job in Puhti:
```text
sbatch mb_batch 
```

## Manual

*   [MrBayes home page](https://nbisweden.github.io/MrBayes/index.html)
*   [Manual and other resources](https://nbisweden.github.io/MrBayes/manual.html)
