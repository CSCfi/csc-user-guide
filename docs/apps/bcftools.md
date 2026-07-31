---
tags:
  - Free
catalog:
  name: BCFtools
  description: Utilities for variant calls in VCF and BCF format
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BCFtools

BCFtools is a set of command-line utilities for manipulating variant call data in the VCF
and BCF formats. It handles both compressed and uncompressed files transparently and
covers common tasks such as filtering, merging, indexing and computing summary
statistics on variant calls.

[TOC]

## Available

* Roihu-CPU: 1.23.1
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail bcftools` after loading `bio-apps`.

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Usage

On Roihu, BCFtools is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bcftools
```

The basic syntax is:

```bash
bcftools <command> [options] file.vcf.gz
```

Some commonly used commands:

* `view`      convert, subset and filter VCF/BCF files
* `call`      call variants from mpileup output
* `filter`    apply user-defined filters to a VCF/BCF
* `merge`     merge multiple VCF/BCF files
* `sort`      sort a VCF/BCF file
* `index`     index a VCF/BCF file
* `stats`     produce summary statistics

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bcftools
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bcftools

srun bcftools sort --threads $SLURM_CPUS_PER_TASK -Oz -o sorted.vcf.gz input.vcf.gz
```

Submit the job with `sbatch bcftools_job.sh`.

## More information

* [BCFtools home page](https://samtools.github.io/bcftools/)
* [BCFtools manual](https://samtools.github.io/bcftools/bcftools.html)
* [CSC Service Desk](../support/contact.md)
