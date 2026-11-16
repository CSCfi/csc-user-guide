---
tags:
  - Free
catalog:
  name: GenomeScope 2.0
  description: Estimate genome size, heterozygosity and ploidy from k-mer counts
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GenomeScope 2.0

GenomeScope 2.0 estimates the genome size, heterozygosity and repeat content of a
genome from the k-mer counts of unassembled sequencing reads. It works for genomes up
to hexaploid.

[TOC]

## License

Free to use and open source under the [Apache 2.0 license](https://github.com/tbenavi1/genomescope2.0/blob/master/LICENSE).

## Available

* Roihu-CPU: 2.1.0, via the `bio-apps` module.

## Usage

GenomeScope is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the GenomeScope module:

```bash
module load bio-apps/v202603
module load genomescope2/2.1.0
```

GenomeScope needs a histogram of k-mer counts as input. You can make one with
[Jellyfish](jellyfish.md), which is also in bio-apps. Count the canonical k-mers
(`-C`) of your reads and export the histogram:

```bash
module load jellyfish/2.2.7
jellyfish count -C -m 21 -s 1000000000 -t 8 reads_1.fastq reads_2.fastq -o reads.jf
jellyfish histo -t 8 reads.jf > reads.histo
```

Then run GenomeScope on the histogram, giving the k-mer length used for counting:

```bash
genomescope.R -i reads.histo -o genomescope_out -k 21
```

The plots and a summary of the estimated genome properties are written to
`genomescope_out`. Use `-p` to set the ploidy if it is not 2.

### Example batch script

Counting the k-mers takes the most time and memory, so run the whole analysis as a
batch job:

```bash
#!/bin/bash
#SBATCH --job-name=genomescope
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load jellyfish/2.2.7
module load genomescope2/2.1.0

jellyfish count -C -m 21 -s 1000000000 -t $SLURM_CPUS_PER_TASK reads_1.fastq reads_2.fastq -o reads.jf
jellyfish histo -t $SLURM_CPUS_PER_TASK reads.jf > reads.histo
genomescope.R -i reads.histo -o genomescope_out -k 21
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [GenomeScope 2.0 GitHub repository](https://github.com/tbenavi1/genomescope2.0)
* [Ranallo-Benavidez, T.R., Jaron, K.S. & Schatz, M.C. (2020). GenomeScope 2.0 and Smudgeplot for reference-free profiling of polyploid genomes. Nature Communications 11, 1432](https://doi.org/10.1038/s41467-020-14998-3)
