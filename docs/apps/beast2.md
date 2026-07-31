---
tags:
  - Free
catalog:
  name: BEAST 2
  description: Bayesian evolutionary analysis by MCMC sampling
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BEAST 2

BEAST 2 is a cross-platform program for Bayesian phylogenetic inference using Markov
chain Monte Carlo (MCMC). It infers rooted, time-measured phylogenies from molecular
sequence data under strict or relaxed molecular clock models, and can also be used to
test evolutionary hypotheses without conditioning on a single tree topology.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail beast2` after loading `bio-apps`.

## License

Free to use and open source under
[GNU LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

## Usage

On Roihu, BEAST 2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load beast2
```

The basic syntax is:

```bash
beast [options] input.xml
```

MCMC chains are long-running and should always be submitted as batch jobs. An example
batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=beast2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load beast2

srun beast -threads $SLURM_CPUS_PER_TASK input.xml
```

Submit the job with `sbatch beast2_job.sh`. Since MCMC chains may need more time than the
requested walltime allows, check convergence with a tool such as Tracer before extending
a run.

## More information

* [BEAST 2 home page](http://beast2.org/)
* [Taming the BEAST tutorials](https://taming-the-beast.org/)
* [CSC Service Desk](../support/contact.md)
