# BayeScan

## Description

BayeScan aims at identifying candidate loci under natural selection from genetic data, using differences in allele frequencies 
between populations. The analysis is based on the multinomial-Dirichlet model. 

## Version

*   Bayescan 2.1 is available in Puhti

## Usage

To use BayeScan, first run command
```text
module load biokit
```
After that you can launch bayescan with a command like:
```text
bayescan_2.1 -threads 1 test_binary_AFLP.txt 
```

With bayescan_2.1 it is important to define the number of threads
always explisitely. This is because by default bayescan tries
to use all available cores. Further, these tasks should be executed as batch jobs
.
Below is a sample batch job file for bayescan:

```text
#!/bin/bash
#SBATCH --job-name=bayescan
#SBATCH --account=project_2001896
#SBATCH --time=08:00:00
#SBATCH --mem=8G
#SBATCH --partition=small
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load biokit

bayescan_2.1 -threads ${SLURM_CPUS_PER_TASK} test_binary_AFLP.txt > bayescan_omp.out
```


The above script can be submitted to the batch job system with command:
```text
sbatch script
```
Don't use Bayescan with more than 8 cpores (execpt if you have verifies that your task really 
benefits from larger core numbers).

More instructions for running batch jobs can be found form [CSC batch job instructions](https://docs.csc.fi/computing/running/getting-started/)

## More information

*   [BayeScan home page](http://cmpg.unibe.ch/software/BayeScan/index.html)
*   [BayScan manual](http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1_manual.pdf)
