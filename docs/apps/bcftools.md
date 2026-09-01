---
tags:
  - Free
catalog:
  name: BCFtools
  description: Variant calling and VCF/BCF manipulation
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BCFtools

BCFtools is a set of utilities for variant calling and for manipulating variant call
format (VCF) and its binary counterpart (BCF) files. It is part of the same project as
[SAMtools](samtools.md) and HTSlib.

[TOC]

## License

Free to use and open source under the
[MIT/Expat License](https://github.com/samtools/bcftools/blob/develop/LICENSE).

## Available

* Roihu: 1.23.1, via the `bio-apps` module.

## Usage

BCFtools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BCFtools module:

```bash
module load bio-apps/v202603
module load bcftools/1.23.1
```

BCFtools provides many subcommands, for example `bcftools view`, `bcftools call`,
`bcftools mpileup`, `bcftools stats` and `bcftools filter`. For example, to call
variants from an alignment:

```bash
bcftools mpileup -f reference.fa aln.bam | bcftools call -mv -Oz -o calls.vcf.gz
```

Many subcommands can use several threads with the `--threads` option.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bcftools
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load bcftools/1.23.1

bcftools mpileup -f reference.fa aln.bam | bcftools call -mv -Oz -o calls.vcf.gz
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BCFtools home page](https://samtools.github.io/bcftools/)
* [BCFtools manual](https://samtools.github.io/bcftools/bcftools.html)
