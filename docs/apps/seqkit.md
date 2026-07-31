---
tags:
  - Free
catalog:
  name: seqkit
  description: Toolkit for FASTA/Q file manipulation
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# seqkit

seqkit is a cross-platform, ultrafast toolkit for manipulating and searching FASTA and
FASTQ files, covering common tasks like format conversion, subsetting and statistics.

[TOC]

## Available

* Roihu-CPU: 2.10.0
* Roihu-GPU: not available

Check the installed versions with `module avail seqkit` after loading `bio-apps`.

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only.

## License

Free to use and open source under
[MIT License](https://github.com/shenwei356/seqkit/blob/master/LICENSE).

## Usage

On Roihu, seqkit is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load seqkit
```

The basic syntax is:

```bash
seqkit <command> [options] input.fasta
```

For example, to get basic statistics on a FASTQ file:

```bash
seqkit stats input.fastq.gz
```

Most seqkit commands parallelize over records with the `-j`/`--threads` option (default
4). An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=seqkit
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load seqkit

srun seqkit stats --threads $SLURM_CPUS_PER_TASK input.fastq.gz
```

Submit the job with `sbatch seqkit_job.sh`.

## More information

* [seqkit home page and documentation](https://bioinf.shenwei.me/seqkit/)
* [CSC Service Desk](../support/contact.md)
