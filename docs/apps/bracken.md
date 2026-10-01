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

* Roihu-CPU: 2.8, 2.9, via the `bio-apps` module.

## Usage

Bracken is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Bracken module:

```bash
module load bio-apps/v202603
module load bracken/2.9
```

### Databases

Bracken works with a [Kraken 2](kraken.md) database, which additionally needs Bracken
k-mer distribution files (`database<read length>mers.kmer_distrib`) built from it with
`bracken-build`. The [prebuilt Kraken 2 databases](kraken.md#databases) on Roihu include
these files for the following read lengths:

* `k2_pluspf_20260226`: 50, 75, 100, 150, 200, 250 and 300
* `k2_NCBI_reference_20251007`: 50, 150 and 200

The Bracken module also loads Kraken 2, which sets `KRAKEN2_DB_PATH` to the database
directory (`/dataset/project_2020345/kraken2`). Unlike `kraken2`, Bracken does not look
databases up by name, so give the path in `-d`, for example
`-d $KRAKEN2_DB_PATH/k2_pluspf_20260226`. Use the same database you used for the
Kraken 2 classification, and a read length (`-r`) that has a matching `kmer_distrib`
file. For your own Kraken 2 database, build the Bracken files with `bracken-build` in a
writable location (for example your project's `/scratch`).

### Running Bracken

After classifying reads with Kraken 2, estimate abundances at a given taxonomic level
(for example species, `-l S`) with:

```bash
bracken -d $KRAKEN2_DB_PATH/k2_pluspf_20260226 -i sample.kreport -o sample.bracken -r 150 -l S
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

bracken -d $KRAKEN2_DB_PATH/k2_pluspf_20260226 -i sample.kreport -o sample.bracken -r 150 -l S
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Bracken home page](https://ccb.jhu.edu/software/bracken/)
* [Bracken GitHub repository](https://github.com/jenniferlu717/Bracken)
