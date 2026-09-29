---
tags:
  - Free
catalog:
  name: SortMeRNA
  description: Filtering and sorting of rRNA reads from (meta)transcriptomic data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SortMeRNA

SortMeRNA is a local sequence alignment tool for filtering, mapping and clustering
ribosomal RNA (rRNA) from metatranscriptomic and metagenomic data. It is commonly used
to separate rRNA reads from the rest of an RNA-seq dataset.

[TOC]

## License

Free to use and open source under [GNU LGPLv3](https://github.com/sortmerna/sortmerna/blob/master/LICENSE.txt).

## Available

* Roihu: 7.0.0, via the `bio-apps` module.

## Usage

SortMeRNA is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SortMeRNA module:

```bash
module load bio-apps/v202603
module load sortmerna/7.0.0
```

### Databases

SortMeRNA needs one or more rRNA reference databases (FASTA files, such as the SILVA or
Rfam rRNA sets), which are **not** bundled with the module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download the rRNA reference
    databases you need to a writable location (for example your project's `/scratch`).

### Running SortMeRNA

```bash
#!/bin/bash
#SBATCH --job-name=sortmerna
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load sortmerna/7.0.0

sortmerna --ref rRNA_db.fasta --reads reads.fq.gz \
    --workdir sortmerna_run --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SortMeRNA documentation](https://sortmerna.readthedocs.io/)
* [SortMeRNA GitHub repository](https://github.com/sortmerna/sortmerna)
