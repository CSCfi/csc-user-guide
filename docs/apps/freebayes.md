---
tags:
  - Free
catalog:
  name: Freebayes
  description: Genetic variant detector
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Freebayes

FreeBayes is a genetic variant detector designed to find small polymorphisms (SNPs, indels, MNPs and complex events).

FreeBayes is haplotype-based, in the sense that it calls variants based on the literal sequences of reads aligned to a particular target, not their precise alignment. This model is a straightforward generalization of previous ones (e.g. PolyBayes, samtools, GATK) which detect or report variants based on alignments. This method avoids one of the core problems with alignment-based variant detection, that identical sequences may have multiple possible alignments.

FreeBayes uses short-read alignments (BAM files) for any number of individuals from a population and a reference genome to determine the most-likely combination of genotypes for the population at each position in the reference. It reports positions which it finds putatively polymorphic in variant call file (VCF) format. It can also use an input set of variants (VCF) as a source of prior information, and a copy number variant map (BED) to define non-uniform ploidy variation across the samples under analysis.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/freebayes/freebayes/master/LICENSE).

## Available

* Roihu: 1.3.6, via the `bio-apps` module.

## Usage

FreeBayes is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the FreeBayes module:

```bash
module load bio-apps/v202603
module load freebayes/1.3.6
```

After this you can launch FreeBayes. For example:

```bash
freebayes -f reference.fa input.bam > results.vcf
```

Note that FreeBayes requires a BAM file that is indexed. A BAM file can be indexed with the `samtools index` command (load the `samtools` module first):

```bash
module load samtools/1.21
samtools index input.bam
```

FreeBayes analysis jobs can be computationally heavy and should be run as batch jobs on Roihu. Below is a sample batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=freebayes
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=24:00:00
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=16000M

module load bio-apps/v202603
module load freebayes/1.3.6

freebayes -f reference.fa input.bam > results.vcf
```

Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Freebayes home page](https://github.com/ekg/freebayes/blob/master/README.md)
* [Reference publication](https://arxiv.org/abs/1207.3907)
