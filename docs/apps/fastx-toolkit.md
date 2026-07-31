---
tags:
  - Free
catalog:
  name: FASTX-Toolkit
  description: Command line tools for FASTA/FASTQ short-read preprocessing
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# FASTX-Toolkit

The FASTX-Toolkit is a collection of command-line tools for preprocessing short-read
FASTA and FASTQ files, such as quality trimming, adapter clipping and format
conversion. Each task is a separate small program rather than one unified command.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail fastx-toolkit` after loading `bio-apps`.

## License

Free to use and open source under
[AGPL v3 License](https://github.com/agordon/fastx_toolkit/blob/master/LICENSE).

## Usage

On Roihu, FASTX-Toolkit is part of the `bio-apps` collection, which has to be loaded
first:

```bash
module load bio-apps
module load fastx-toolkit
```

Some of the tools it installs:

| Command                     | Function                                |
|------------------------------|------------------------------------------|
| `fastx_trimmer`             | Trim reads to a fixed length range      |
| `fastx_clipper`             | Remove adapter sequences from reads     |
| `fastq_quality_filter`      | Filter reads by quality score           |
| `fastq_quality_trimmer`     | Trim reads by quality score             |
| `fastx_quality_stats`       | Report per-base quality statistics      |
| `fastx_collapser`           | Collapse identical reads into one entry |
| `fastx_reverse_complement`  | Reverse-complement sequences            |

Each tool reads FASTA/FASTQ from `-i` (or standard input) and writes to `-o` (or
standard output). For example:

```bash
fastx_trimmer -f 1 -l 50 -i input.fastq -o trimmed.fastq
```

Heavier jobs should be run as batch jobs. The FASTX-Toolkit tools are single-threaded,
so a job only needs one CPU core. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=fastx-toolkit
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load fastx-toolkit

srun fastx_trimmer -f 1 -l 50 -i input.fastq -o trimmed.fastq
```

Submit the job with `sbatch fastx-toolkit_job.sh`.

## More information

* [FASTX-Toolkit home page](http://hannonlab.cshl.edu/fastx_toolkit/)
* [FASTX-Toolkit on GitHub](https://github.com/agordon/fastx_toolkit)
* [CSC Service Desk](../support/contact.md)
