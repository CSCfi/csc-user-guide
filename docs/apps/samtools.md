---
tags:
  - Free
catalog:
  name: SAMtools
  description: Utilities for managing SAM/BAM formatted alignment files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SAMtools

SAMtools provides tools for using and manipulating SAM, BAM and CRAM formatted
alignments. You can use SAMtools for example for format conversion, sorting,
indexing and viewing alignments, and for basic variant-related processing.

[TOC]

## License

Free to use and open source under the
[MIT/Expat License](https://github.com/samtools/samtools/blob/develop/LICENSE).

## Available

* Roihu: 1.21, via the `bio-apps` module.

## Usage

SAMtools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SAMtools module:

```bash
module load bio-apps/v202603
module load samtools/1.21
```

Check the available versions with:

```bash
module spider samtools
```

After loading, you can run SAMtools:

```bash
samtools --version
```

Heavier SAMtools jobs should be run as batch jobs. Below is an example batch
script that converts a SAM file to BAM, then sorts and indexes it:

```bash
#!/bin/bash
#SBATCH --job-name=samtools
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000M

module load bio-apps/v202603
module load samtools/1.21

# Convert SAM to BAM
samtools view -bS aln.sam > aln.bam

# Sort the BAM file
samtools sort aln.bam -o aln-sorted.bam

# Index the sorted BAM file
samtools index aln-sorted.bam
```

Replace `<project>` with your CSC project (for example `project_2001234`). Submit
the job with:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md)
for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SAMtools home page](http://www.htslib.org/)
* [SAMtools documentation](http://www.htslib.org/doc/samtools.html)
