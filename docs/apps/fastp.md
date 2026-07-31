---
tags:
  - Free
catalog:
  name: fastp
  description: All-in-one preprocessing tool for FASTQ files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# fastp

fastp is an all-in-one preprocessing tool for FASTQ files, combining quality
filtering, adapter trimming and read filtering in a single fast pass. It also writes
an HTML and JSON quality report for each run.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail fastp` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/OpenGene/fastp/blob/master/LICENSE).

## Usage

On Roihu, fastp is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load fastp
```

The basic syntax for single-end reads is:

```bash
fastp -i in.fastq.gz -o out.fastq.gz
```

For paired-end reads:

```bash
fastp -i in.R1.fastq.gz -I in.R2.fastq.gz -o out.R1.fastq.gz -O out.R2.fastq.gz
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=fastp
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load fastp

srun fastp -i in.fastq.gz -o out.fastq.gz --thread $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch fastp_job.sh`.

## More information

* [fastp home page](https://github.com/OpenGene/fastp)
* [CSC Service Desk](../support/contact.md)
