---
tags:
  - Free
catalog:
  name: BayeScan
  description: Tool for identifying candidate loci under natural selection based on allele frequencies in populations
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BayeScan

BayeScan aims at identifying candidate loci under natural selection from genetic data, using differences in allele frequencies 
between populations. The analysis is based on the multinomial-Dirichlet model. 

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)

## Available

* Roihu-CPU: 2.1, via the `bio-apps` module.

## Usage

BayeScan is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BayeScan module:

```bash
module load bio-apps/v202603
module load bayescan/2.1
```

After that you can launch BayeScan with a command like:

```bash
bayescan_2.1 -threads 1 input.txt
```

With bayescan_2.1, it is important to define the number of threads
always explicitly. This is because, by default, BayeScan tries
to use all available cores.

The results are written to the current directory. To plot them in R, use the
`plot_bayescan` function from the `plot_R.r` file that comes with BayeScan:

```r
source(file.path(Sys.getenv("BAYESCAN_INSTROOT"), "share/bayescan/plot_R.r"))
plot_bayescan("input_fst.txt", FDR = 0.05)
```

On Roihu, BayeScan tasks should be executed as batch jobs.
Below is a sample batch job file for BayeScan:

```bash
#!/bin/bash
#SBATCH --job-name=bayescan
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=6G

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

module load bio-apps/v202603
module load bayescan/2.1

bayescan_2.1 -threads $SLURM_CPUS_PER_TASK input.txt
```

The script above reserves 8 hours of computing time, 6 GiB of memory and 4 computing cores. Replace `<project>` with your CSC project (for example `project_2001234`).

The job can be submitted to the batch job system with command:

```bash
sbatch script
```

In many cases BayeScan will not benefit from using more than 8 cores, so check performance if using more.

More instructions for running batch jobs can be found in [CSC batch job instructions](../computing/running/getting-started.md)

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BayeScan home page](https://cmpg.unibe.ch/software/BayeScan/index.html)
* [BayeScan manual](https://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1_manual.pdf)
