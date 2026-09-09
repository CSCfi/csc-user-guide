---
tags:
  - Free
catalog:
  name: antiSMASH
  description: Detection of secondary-metabolite biosynthesis gene clusters in microbial genomes
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# antiSMASH

antiSMASH (antibiotics and Secondary Metabolite Analysis Shell) performs genome-wide
identification, annotation and analysis of secondary-metabolite biosynthesis gene
clusters in bacterial and fungal genomes.

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html).

## Available

* Roihu: 8.0.4, via the `bio-apps` module.

## Usage

antiSMASH is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the antiSMASH module:

```bash
module load bio-apps/v202603
module load antismash/8.0.4
```

### Databases

antiSMASH requires reference databases that are **not** bundled with the module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download your own copy as
    shown below.

Download the databases to a writable location (for example your project's `/scratch`
directory) with `download-antismash-databases`, and point antiSMASH at them with the
`--databases` option:

```bash
download-antismash-databases --database-dir /scratch/<project>/antismash_db
```

### Running antiSMASH

antiSMASH takes an annotated genome (GenBank/EMBL) or a FASTA sequence as input.
It can use several CPU cores with the `--cpus` option. Runs should be submitted as
batch jobs:

```bash
#!/bin/bash
#SBATCH --job-name=antismash
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load antismash/8.0.4

antismash --cpus $SLURM_CPUS_PER_TASK \
    --databases /scratch/<project>/antismash_db \
    --output-dir results \
    genome.gbk
```

Replace `<project>` with your CSC project (for example `project_2001234`), and use the
same project in the database path.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [antiSMASH home page](https://antismash.secondarymetabolites.org/)
* [antiSMASH documentation](https://docs.antismash.secondarymetabolites.org/)
