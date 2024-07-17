---
tags:
  - Free
---

# BayeScan

BayeScan aims at identifying candidate loci under natural selection from genetic data, using differences in allele frequencies 
between populations. The analysis is based on the multinomial-Dirichlet model. 

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)

## Available

* Puhti: 2.1 

## Usage

To use BayeScan, first run command

```bash
module load biokit
```

After that you can launch BayeScan with a command like:

```bash
bayescan_2.1 -threads 1 test_binary_AFLP.txt 
```

With bayescan_2.1, it is important to define the number of threads
always explicitly. This is because, by default, BayeScan tries
to use all available cores.

On Puhti, BayeScan tasks should be executed as batch jobs.
Below is a sample batch job file for BayeScan:

```bash
#!/bin/bash
#SBATCH --job-name=bayescan
#SBATCH --account=project_XXXXXX
#SBATCH --time=08:00:00
#SBATCH --mem=6G
#SBATCH --partition=small
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load biokit

bayescan_2.1 -threads ${SLURM_CPUS_PER_TASK} test_binary_AFLP.txt > bayescan_omp.out
```

The script above reserves 8 hours of computing time, 6 GB of memory and 4 computing cores. The `XXXXXX` in the `--account` definition
should be replaced with the ID number of your computing project. The job can be submitted to the batch job system with command:

```bash
sbatch script
```

Don't use BayeScan with more than 8 cores (except if you have verified that your task really benefits from larger core numbers).

More instructions for running batch jobs can be found form [CSC batch job instructions](../computing/running/getting-started.md)

## More information

* [BayeScan home page](http://cmpg.unibe.ch/software/BayeScan/index.html)
* [BayeScan manual](http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1_manual.pdf)
