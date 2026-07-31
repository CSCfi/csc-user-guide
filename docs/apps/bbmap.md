---
tags:
  - Free
catalog:
  name: BBMap
  description: Short read aligner for DNA and RNA-seq data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BBMap

BBMap is a splice-aware short-read aligner for DNA and RNA-seq data, part of the
BBTools suite of sequence analysis utilities.

[TOC]

## Available

* Roihu-CPU: 39.59
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail bbmap` after loading `bio-apps`.

## License

Free to use and open source under
[BSD 3-Clause LBNL License](https://github.com/bbushnell/BBTools/blob/master/license.txt).

## Usage

On Roihu, BBMap is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bbmap
```

The basic syntax is:

```bash
bbmap.sh in=reads.fastq out=mapped.sam ref=genome.fasta
```

BBMap parallelises with `threads=`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bbmap
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=8G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bbmap

srun bbmap.sh in=reads.fastq out=mapped.sam ref=genome.fasta \
    threads=$SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch bbmap_job.sh`.

## More information

* [BBMap home page](https://bbmap.org/tools/bbmap)
* [CSC Service Desk](../support/contact.md)
