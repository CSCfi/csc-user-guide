---
tags:
  - Free
catalog:
  name: yak
  description: K-mer counting and k-mer based quality evaluation of reads and assemblies
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# yak

Yak is a k-mer counter and analysis tool. It estimates the base accuracy (QV) of
long reads and assembly contigs by comparing them with the k-mers of short reads,
without a reference genome. It also builds the parental k-mer tables used for trio
binning in [hifiasm](hifiasm.md), and evaluates the phasing of assemblies.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/lh3/yak/blob/master/LICENSE.txt).

## Available

* Roihu-CPU: 0.1, via the `bio-apps` module.

## Usage

Yak is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the yak module:

```bash
module load bio-apps/v202603
module load yak/0.1
```

Count the k-mers of paired-end short reads:

```bash
cat sr_1.fq.gz sr_2.fq.gz > sr.fq.gz
yak count -b37 -t 16 -o sr.yak sr.fq.gz
```

With the Bloom filter on (`-b`), yak reads the input twice: the first pass finds
the k-mers seen more than once and the second pass counts them, which discards
k-mers from sequencing errors. Concatenate paired-end reads into one file as
above: if you give two files, yak uses only the first for the first pass and only
the second for counting. `-b37` is recommended for human-sized data and uses
16 GB of memory for the Bloom filter.

Estimate the QV of an assembly from the short-read k-mers. `-p` also prints the
QV of each contig, and `-l100k` leaves out contigs shorter than 100 kb:

```bash
yak qv -t 16 -p -K3.2g -l100k sr.yak asm.fa > asm-sr.qv.txt
```

Evaluate the phasing of a haplotype assembly with k-mers counted from the
paternal and maternal short reads (see [trio binning in hifiasm](hifiasm.md#trio-binning)
for how to count them). Hifiasm writes its assemblies in GFA format, so convert
them to FASTA first:

```bash
awk '/^S/{print ">"$2;print $3}' asm.dip.hap1.p_ctg.gfa > asm.dip.hap1.p_ctg.fa
yak trioeval -t 16 pat.yak mat.yak asm.dip.hap1.p_ctg.fa > hap1.trioeval.txt
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=yak
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G

module load bio-apps/v202603
module load yak/0.1

cat sr_1.fq.gz sr_2.fq.gz > sr.fq.gz
yak count -b37 -t $SLURM_CPUS_PER_TASK -o sr.yak sr.fq.gz
yak qv -t $SLURM_CPUS_PER_TASK -p -K3.2g -l100k sr.yak asm.fa > asm-sr.qv.txt
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [yak GitHub repository](https://github.com/lh3/yak)
