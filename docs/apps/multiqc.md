---
tags:
  - Free
catalog:
  name: MultiQC
  description: Aggregate bioinformatics QC results from many samples into one report
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MultiQC

MultiQC scans a directory of log and report files from common bioinformatics tools, such
as FastQC, Cutadapt or STAR, and summarises them into a single interactive HTML report
covering all samples.

[TOC]

## Available

* Roihu-CPU: 1.28
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail py-multiqc` after loading `bio-apps`.

## License

Free to use and open source under
[GNU GPLv3](https://github.com/MultiQC/MultiQC/blob/main/LICENSE).

## Usage

On Roihu, MultiQC is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load py-multiqc
```

The basic syntax is:

```bash
multiqc results_directory -o multiqc_report
```

MultiQC recurses into `results_directory`, so it is enough to point it at the top-level
folder containing all your samples' tool outputs.

This is a lightweight, single-core job. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=multiqc
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load py-multiqc

srun multiqc results_directory -o multiqc_report
```

Submit the job with `sbatch multiqc_job.sh`.

## More information

* [MultiQC home page](https://multiqc.info)
* [MultiQC documentation](https://multiqc.info/docs/)
* [CSC Service Desk](../support/contact.md)
