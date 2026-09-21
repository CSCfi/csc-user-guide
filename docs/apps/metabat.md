---
tags:
  - Free
catalog:
  name: MetaBAT
  description: Metagenome binning (MetaBAT2)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MetaBAT

MetaBAT is a tool for the accurate and efficient binning of metagenomic contigs into
genome bins (metagenome-assembled genomes) using tetranucleotide frequencies and contig
abundances. On Roihu it is provided as MetaBAT2.

[TOC]

## License

Free to use and open source. See the [MetaBAT license](https://bitbucket.org/berkeleylab/metabat/src/master/license.txt).

## Available

* Roihu: 2.15, via the `bio-apps` module.

## Usage

MetaBAT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MetaBAT module:

```bash
module load bio-apps/v202603
module load metabat/2.15
```

MetaBAT2 takes an assembly and a per-contig depth file (computed from BAM alignments
with `jgi_summarize_bam_contig_depths`):

```bash
jgi_summarize_bam_contig_depths --outputDepth depth.txt aln.sorted.bam
metabat2 -i assembly.fa -a depth.txt -o bins/bin -t 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=metabat2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load metabat/2.15

metabat2 -i assembly.fa -a depth.txt -o bins/bin -t $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MetaBAT repository](https://bitbucket.org/berkeleylab/metabat/)
