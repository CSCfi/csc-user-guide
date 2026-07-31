---
tags:
  - Free
catalog:
  name: VCFtools
  description: Tools for working with VCF and BCF files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# VCFtools

VCFtools provides utilities for filtering, comparing and summarising genetic variation
stored in the Variant Call Format (VCF) and its binary counterpart, BCF.

[TOC]

## Available

* Roihu-CPU: 0.1.17
* Roihu-GPU: not available

Check the installed versions with `module avail vcftools` after loading `bio-apps`.

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only.

## License

Free to use and open source under
[LGPL-3.0 License](https://github.com/vcftools/vcftools/blob/master/LICENSE).

## Usage

On Roihu, VCFtools is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load vcftools
```

The basic syntax is:

```bash
vcftools --gzvcf input.vcf.gz --freq --out output
```

VCFtools is single-threaded, so a batch job needs only one CPU core. An example batch
job script:

```bash
#!/bin/bash
#SBATCH --job-name=vcftools
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load vcftools

srun vcftools --gzvcf input.vcf.gz --freq --out output
```

Submit the job with `sbatch vcftools_job.sh`.

## More information

* [VCFtools home page](https://vcftools.github.io/)
* [VCFtools manual](https://vcftools.github.io/man_latest.html)
* [CSC Service Desk](../support/contact.md)
