---
tags:
  - Free
catalog:
  name: HTSeq
  description: Python package for processing high-throughput sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HTSeq

HTSeq is a Python package for processing data from high-throughput sequencing
experiments, most commonly used through its `htseq-count` script for counting
reads that overlap genomic features.

[TOC]

## Available

* Roihu-CPU: 2.0.3
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail py-htseq` after loading `bio-apps`.

## License

Free to use and open source under
[GNU General Public License v3.0](https://github.com/htseq/htseq/blob/main/LICENSE).

## Usage

On Roihu, HTSeq is part of the `bio-apps` collection, which has to be loaded first.
Note that the module name is `py-htseq`:

```bash
module load bio-apps
module load py-htseq
```

The main entry point is `htseq-count`:

```bash
htseq-count -f bam aligned.bam annotation.gtf > counts.txt
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=htseq-count
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load py-htseq

srun htseq-count -f bam aligned.bam annotation.gtf > counts.txt
```

Submit the job with `sbatch htseq_job.sh`.

## More information

* [HTSeq home page](https://htseq.readthedocs.io/en/master/index.html)
* [CSC Service Desk](../support/contact.md)
