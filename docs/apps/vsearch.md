---
tags:
  - Free
catalog:
  name: VSEARCH
  description: Versatile sequence search and clustering
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# VSEARCH

VSEARCH is a versatile open-source tool for metagenomics. It offers fast searching,
clustering, chimera detection, dereplication, subsampling and other operations on
nucleotide sequences, and is a common open-source alternative to USEARCH.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/torognes/vsearch/blob/master/LICENSE.txt).

## Available

* Roihu: 2.22.1, via the `bio-apps` module.

## Usage

VSEARCH is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the VSEARCH module:

```bash
module load bio-apps/v202603
module load vsearch/2.22.1
```

For example, to cluster sequences at 97% identity:

```bash
vsearch --cluster_fast input.fasta --id 0.97 --centroids centroids.fasta --threads 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=vsearch
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load vsearch/2.22.1

vsearch --cluster_fast input.fasta --id 0.97 --centroids centroids.fasta --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [VSEARCH GitHub repository](https://github.com/torognes/vsearch)
