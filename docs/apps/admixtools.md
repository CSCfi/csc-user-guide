---
tags:
  - Non-commercial
catalog:
  name: ADMIXTOOLS
  description: Statistical tools for detecting and dating population admixture
  license_type: Non-commercial
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ADMIXTOOLS

ADMIXTOOLS implements the population genetics methods from Patterson et al. (2012),
"Ancient Admixture in Human History", such as D-statistics, f-statistics and admixture
graph fitting from SNP genotype data.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail admixtools` after loading `bio-apps`.

## License

ADMIXTOOLS is copyrighted by Harvard University and the Broad Institute, and may be
freely copied and used for non-commercial purposes. See the
[license notice](https://github.com/DReichLab/AdmixTools/blob/master/README) at the top
of the repository README for the full terms.

## Usage

On Roihu, ADMIXTOOLS is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load admixtools
```

ADMIXTOOLS provides several programs, each driven by a parameter file, for example
`qpDstat` for D-statistics:

```bash
qpDstat -p parfile.txt > qpDstat.out
```

These are single-threaded, lightweight statistical tests. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=admixtools
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load admixtools

srun qpDstat -p parfile.txt > qpDstat.out
```

Submit the job with `sbatch admixtools_job.sh`.

## More information

* [ADMIXTOOLS home page](https://github.com/DReichLab/AdmixTools)
* [CSC Service Desk](../support/contact.md)
