---
tags:
  - Free
catalog:
  name: VSEARCH
  description: Toolkit for metagenomic sequence clustering, search and chimera detection
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# VSEARCH

VSEARCH is an open-source alternative to USEARCH, supporting sequence clustering,
chimera detection, dereplication and searching for metagenomic and amplicon data.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail vsearch` after loading `bio-apps`.

## License

Free to use and open source under
[GPL-3.0 License](https://github.com/torognes/vsearch/blob/master/LICENSE.txt) (VSEARCH
can also be used under the BSD 2-Clause License, at your choice).

## Usage

On Roihu, VSEARCH is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load vsearch
```

The basic syntax is:

```bash
vsearch --cluster_fast sequences.fasta --id 0.97 --centroids centroids.fasta
```

Clustering or searching large sequence sets benefits from multiple threads. An example
batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=vsearch
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load vsearch

srun vsearch --cluster_fast sequences.fasta --id 0.97 \
    --threads $SLURM_CPUS_PER_TASK --centroids centroids.fasta
```

Submit the job with `sbatch vsearch_job.sh`.

## More information

* [VSEARCH home page](https://github.com/torognes/vsearch)
* [CSC Service Desk](../support/contact.md)
