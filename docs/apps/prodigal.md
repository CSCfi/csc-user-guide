---
tags:
  - Free
catalog:
  name: Prodigal
  description: Prokaryotic gene prediction
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Prodigal

Prodigal (Prokaryotic Dynamic Programming Genefinding Algorithm) is a fast, reliable
protein-coding gene prediction tool for prokaryotic (bacterial and archaeal) genomes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/hyattpd/Prodigal/blob/GoogleImport/LICENSE).

## Available

* Roihu: 2.6.3, via the `bio-apps` module.

## Usage

Prodigal is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Prodigal module:

```bash
module load bio-apps/v202603
module load prodigal/2.6.3
```

Predict genes from a genome, writing gene coordinates (GFF) and protein translations:

```bash
prodigal -i genome.fna -o genes.gff -f gff -a proteins.faa -d genes.fna
```

For metagenomic data, use the anonymous/meta procedure with `-p meta`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=prodigal
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load prodigal/2.6.3

prodigal -i genome.fna -o genes.gff -f gff -a proteins.faa -d genes.fna
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Prodigal GitHub repository](https://github.com/hyattpd/Prodigal)
* [Prodigal wiki](https://github.com/hyattpd/prodigal/wiki)
