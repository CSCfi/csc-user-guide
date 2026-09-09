---
tags:
  - Free
catalog:
  name: Mash
  description: Fast genome/metagenome distance estimation (MinHash)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Mash

Mash is a fast tool for estimating the distance between genomes and metagenomes using
the MinHash dimensionality-reduction technique. It reduces large sequences to compact
sketches, enabling rapid distance and containment estimates.

[TOC]

## License

Free to use and open source. See the [Mash license](https://github.com/marbl/Mash/blob/master/LICENSE.txt).

## Available

* Roihu: 2.3, via the `bio-apps` module.

## Usage

Mash is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Mash module:

```bash
module load bio-apps/v202603
module load mash/2.3
```

Create sketches and estimate the distance between two genomes:

```bash
mash sketch -o reference genome1.fa
mash dist reference.msh genome2.fa
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=mash
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load mash/2.3

mash sketch -p $SLURM_CPUS_PER_TASK -o reference *.fa
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Mash documentation](https://mash.readthedocs.io/)
* [Mash GitHub repository](https://github.com/marbl/Mash)
