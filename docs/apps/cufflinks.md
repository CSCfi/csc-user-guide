---
tags:
  - Free
catalog:
  name: Cufflinks
  description: Transcript assembly and differential expression for RNA-Seq
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Cufflinks

Cufflinks assembles transcripts, estimates their abundances, and tests for differential
expression and regulation in RNA-Seq samples. The package includes tools such as
`cufflinks`, `cuffmerge`, `cuffdiff` and `cuffcompare`.

[TOC]

## License

Free to use and open source under the [Boost Software License 1.0](https://cole-trapnell-lab.github.io/cufflinks/).

## Available

* Roihu: 2.2.1, via the `bio-apps` module.

## Usage

Cufflinks is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Cufflinks module:

```bash
module load bio-apps/v202603
module load cufflinks/2.2.1
```

To assemble transcripts from an aligned, sorted BAM file:

```bash
cufflinks -p 4 -o cufflinks_out aligned.sorted.bam
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=cufflinks
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load cufflinks/2.2.1

cufflinks -p $SLURM_CPUS_PER_TASK -o cufflinks_out aligned.sorted.bam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Cufflinks home page](https://cole-trapnell-lab.github.io/cufflinks/)
