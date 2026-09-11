---
tags:
  - Free
catalog:
  name: Structure
  description: Inference of population structure in genetics
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Structure

Structure is a software package for using multi-locus genotype data to investigate population structure. 
Its uses include inferring the presence of distinct populations, assigning individuals to populations, studying hybrid zones, 
identifying migrants and admixed individuals, and estimating population allele frequencies in situations where many 
individuals are migrants or admixed.

It can be applied to most of the commonly-used genetic markers, including SNPS, microsatellites, RFLPs and AFLPs. 

[TOC]

## License

Structure is free to use. Source code is available from the upstream website, but no explicit open-source license is specified.

## Available

* Roihu: 2.3.4, via the `bio-apps` module.

## Usage

Structure is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Structure module:

```bash
module load bio-apps/v202603
module load structure/2.3.4
```

Structure reads its run settings from `mainparams` and `extraparams` files in the
working directory. Prepare these files (along with your genotype data file), then
run Structure with:

```bash
structure
```

You can also point Structure at specific files and options on the command line, for example:

```bash
structure -m mainparams -e extraparams -K 3 -i infile -o outfile
```

Structure runs are single-core and can be long, so real analyses should be run as batch jobs. Below is a simple example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=structure
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load structure/2.3.4

structure
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

### Automating Structure and post-processing

Related tools for running and post-processing Structure analyses are available as
separate modules in bio-apps:

* [StrAuto](strauto.md) (`strauto`) — automate Structure across a range of *K* values and replicate runs, and chain the results into the Evanno ΔK analysis.
* `structureharvester` — StructureHarvester, for parsing Structure results and applying the Evanno ΔK method.
* `clumpp` — CLUMPP, for aligning replicate cluster assignments across runs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Structure home page](https://web.stanford.edu/group/pritchardlab/structure.html)
