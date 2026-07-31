---
tags:
  - Free
catalog:
  name: Barrnap
  description: Prediction of ribosomal RNA gene locations in genomes
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Barrnap

Barrnap predicts the location of ribosomal RNA genes (5S, 16S, 23S for bacteria; 5S,
5.8S, 18S, 28S for eukaryotes) in genome assemblies.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail barrnap` after loading `bio-apps`.

## License

Free to use and open source under
[CC0 1.0 Universal](https://spdx.org/licenses/CC0-1.0.html).

## Usage

On Roihu, Barrnap is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load barrnap
```

The basic syntax is:

```bash
barrnap genome.fasta > rrna.gff
```

Barrnap parallelises its HMMER searches with `--threads`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=barrnap
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load barrnap

srun barrnap --threads $SLURM_CPUS_PER_TASK genome.fasta > rrna.gff
```

Submit the job with `sbatch barrnap_job.sh`.

## More information

* [Barrnap home page](https://github.com/tseemann/barrnap)
* [CSC Service Desk](../support/contact.md)
