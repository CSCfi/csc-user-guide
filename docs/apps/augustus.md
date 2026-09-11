---
tags:
  - Free
catalog:
  name: AUGUSTUS
  description: Gene prediction in eukaryotic genomic sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# AUGUSTUS

AUGUSTUS is a program that predicts genes in eukaryotic genomic sequences. It can be
used as an ab initio predictor and can also incorporate external evidence such as
RNA-Seq alignments and protein homology.

[TOC]

## License

Free to use and open source under the [Artistic License 1.0](https://opensource.org/license/artistic-1-0).

## Available

* Roihu: 3.5.0, via the `bio-apps` module.

## Usage

AUGUSTUS is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the AUGUSTUS module:

```bash
module load bio-apps/v202603
module load augustus/3.5.0
```

To predict genes using an existing species model:

```bash
augustus --species=human genome.fa > predictions.gff
```

### Configuration directory

The module sets the `AUGUSTUS_CONFIG_PATH` environment variable, pointing to the
configuration directory (species models, parameters) in the module installation. This
installation is **read-only**, which is fine for running predictions with existing
species models.

If you need to **train a new species** (or otherwise write to the configuration
directory, for example with `etraining` or the `autoAug` scripts), copy the
configuration to a writable location and point `AUGUSTUS_CONFIG_PATH` there:

```bash
cp -r $AUGUSTUS_CONFIG_PATH /scratch/<project>/augustus_config
export AUGUSTUS_CONFIG_PATH=/scratch/<project>/augustus_config
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=augustus
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load augustus/3.5.0

augustus --species=human genome.fa > predictions.gff
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [AUGUSTUS home page](https://bioinf.uni-greifswald.de/augustus/)
* [AUGUSTUS GitHub repository](https://github.com/Gaius-Augustus/Augustus)
