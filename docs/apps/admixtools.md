---
tags:
  - Free
catalog:
  name: AdmixTools
  description: Inference of population admixture from f-statistics
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# AdmixTools

AdmixTools is a package for inferring population history and admixture from
genome-wide allele-frequency data using f-statistics. It provides a set of
command-line programs, including `qpDstat` (D-statistics), `qp3Pop` (f3-statistics),
`qpAdm` and `qpGraph` (admixture modelling), `qpF4ratio` (admixture proportions) and
`convertf` (file-format conversion).

[TOC]

## License

AdmixTools may be freely copied for non-commercial purposes, provided the upstream copyright notice is retained. See the AdmixTools [README](https://github.com/DReichLab/AdmixTools/blob/master/README) for licensing terms.

## Available

* Roihu: 8.0.2, via the `bio-apps` module.

## Usage

AdmixTools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the AdmixTools module:

```bash
module load bio-apps/v202603
module load admixtools/8.0.2
```

The AdmixTools programs are driven by a parameter file that lists the input files
and options. For example, a D-statistics analysis is run with:

```bash
qpDstat -p parfile > qpDstat.log
```

See the [AdmixTools documentation](https://github.com/DReichLab/AdmixTools) for the
parameter-file format and options of each program.

Longer analyses should be run as batch jobs. Below is a simple example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=admixtools
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load admixtools/8.0.2

qpDstat -p parfile > qpDstat.log
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [AdmixTools GitHub repository](https://github.com/DReichLab/AdmixTools)
