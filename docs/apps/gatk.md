---
tags:
  - Free
catalog:
  name: GATK
  description: Genome Analysis Toolkit for variant discovery
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GATK

GATK (Genome Analysis Toolkit) is a collection of tools for variant discovery and
genotyping in high-throughput sequencing data, developed at the Broad Institute.

[TOC]

## License

GATK4 is open source and free to use. See the
[GATK licensing information](https://github.com/broadinstitute/gatk#license).

## Available

* Roihu: 4.5.0.0, via the `bio-apps` module.

## Usage

GATK is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the GATK module:

```bash
module load bio-apps/v202603
module load gatk/4.5.0.0
```

GATK tools are run through the `gatk` wrapper, followed by the tool name. Java options
such as the heap size can be passed with `--java-options`:

```bash
gatk --java-options "-Xmx8g" HaplotypeCaller -R reference.fa -I input.bam -O output.vcf.gz
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=gatk
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10G

module load bio-apps/v202603
module load gatk/4.5.0.0

gatk --java-options "-Xmx8g" HaplotypeCaller -R reference.fa -I input.bam -O output.vcf.gz
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [GATK home page](https://gatk.broadinstitute.org/)
* [GATK tool documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002302312)
