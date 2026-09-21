---
tags:
  - Free
catalog:
  name: Bracken
  description: Species abundance estimation from Kraken2 output
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bracken

Bracken (Bayesian Reestimation of Abundance with KrakEN) is a statistical method that
computes the abundance of species in DNA sequences from a metagenomics sample. It uses
the taxonomic assignments made by [Kraken 2](kraken.md) to estimate species- (or
other level) abundances.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/jenniferlu717/Bracken/blob/master/LICENSE).

## Available

* Roihu: 2.9, via the `bio-apps` module.

## Usage

Bracken is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Bracken module:

```bash
module load bio-apps/v202603
module load bracken/2.9
```

### Databases

Bracken works with a [Kraken 2](kraken.md) database, which additionally needs a Bracken
database built from it (with `bracken-build`). These reference databases are not bundled
with the module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, build or download your own in a
    writable location (for example your project's `/scratch`).

### Running Bracken

After classifying reads with Kraken 2, estimate abundances at a given taxonomic level
(for example species, `-l S`) with:

```bash
bracken -d /scratch/<project>/kraken_db -i sample.kreport -o sample.bracken -r 150 -l S
```

where `-r` is the read length and `-d` points to the Kraken 2 / Bracken database.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bracken
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load bracken/2.9

bracken -d /scratch/<project>/kraken_db -i sample.kreport -o sample.bracken -r 150 -l S
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Bracken home page](https://ccb.jhu.edu/software/bracken/)
* [Bracken GitHub repository](https://github.com/jenniferlu717/Bracken)
