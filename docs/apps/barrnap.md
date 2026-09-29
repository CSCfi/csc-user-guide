---
tags:
  - Free
catalog:
  name: Barrnap
  description: Rapid ribosomal RNA (rRNA) prediction
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Barrnap

Barrnap (BAsic Rapid Ribosomal RNA Predictor) predicts the location of ribosomal RNA
genes in genomes. It supports bacterial, archaeal, mitochondrial and eukaryotic rRNA.

[TOC]

## License

Free to use and open source. See the [Barrnap license](https://github.com/tseemann/barrnap/blob/master/LICENSE).

## Available

* Roihu: 0.9, via the `bio-apps` module.

## Usage

Barrnap is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Barrnap module:

```bash
module load bio-apps/v202603
module load barrnap/0.9
```

Barrnap takes a FASTA genome as input and writes rRNA feature predictions in GFF3
format. Select the kingdom with `--kingdom` (`bac`, `arc`, `euk` or `mito`) and the
number of threads with `--threads`:

```bash
barrnap --kingdom bac --threads 4 genome.fna > rrna.gff
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=barrnap
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
module load barrnap/0.9

barrnap --kingdom bac --threads $SLURM_CPUS_PER_TASK genome.fna > rrna.gff
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Barrnap GitHub repository](https://github.com/tseemann/barrnap)
