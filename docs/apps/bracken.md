---
tags:
  - Free
catalog:
  name: Bracken
  description: Bayesian re-estimation of species abundance from Kraken output
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bracken

Bracken (Bayesian Reestimation of Abundance with KrakEN) re-estimates species- or
genus-level abundances from the taxonomic classifications produced by Kraken or
Kraken 2. It redistributes reads that were assigned to higher taxonomic levels down to
the most likely species or genus.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail bracken` after loading `bio-apps`.

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Usage

On Roihu, Bracken is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bracken
```

Bracken runs on a Kraken(2) report and a Bracken database built for the same Kraken
database and read length:

```bash
bracken -d kraken_db -i sample.kreport -o sample.bracken -r 150 -l S -t 10
```

Heavier jobs should be run as batch jobs. The re-estimation step is single-threaded. An
example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bracken
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bracken

srun bracken -d kraken_db -i sample.kreport -o sample.bracken -r 150 -l S -t 10
```

Submit the job with `sbatch bracken_job.sh`.

## More information

* [Bracken home page](https://ccb.jhu.edu/software/bracken)
* [Bracken source and documentation](https://github.com/jenniferlu717/Bracken)
* [CSC Service Desk](../support/contact.md)
