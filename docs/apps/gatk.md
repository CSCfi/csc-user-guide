---
tags:
  - Free
catalog:
  name: GATK
  description: Toolkit for variant discovery in high-throughput sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GATK

GATK (Genome Analysis Toolkit) is the Broad Institute's toolkit for variant discovery
in high-throughput sequencing data, covering germline and somatic short variant
calling as well as copy number and structural variant workflows. Most analyses are
built around individual tools such as HaplotypeCaller, run through the `gatk` wrapper.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail gatk` after loading `bio-apps`.

## License

GATK4, the current release series, is free to use and open source under the
[Apache License 2.0](https://github.com/broadinstitute/gatk/blob/master/LICENSE.TXT).
Older GATK 3.x releases were distributed under a separate, more restrictive licence.

## Usage

On Roihu, GATK is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load gatk
```

The basic syntax is:

```bash
gatk <ToolName> [arguments]
```

For example, to call germline variants with HaplotypeCaller:

```bash
gatk HaplotypeCaller --reference reference.fasta --input input.bam \
    --output output.g.vcf.gz
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=gatk
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load gatk

srun gatk --java-options "-Xmx12g" HaplotypeCaller \
    --reference reference.fasta \
    --input input.bam \
    --output output.g.vcf.gz \
    --native-pair-hmm-threads $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch gatk_job.sh`.

## More information

* [GATK home page](https://gatk.broadinstitute.org/hc/en-us)
* [GATK on GitHub](https://github.com/broadinstitute/gatk)
* [CSC Service Desk](../support/contact.md)
