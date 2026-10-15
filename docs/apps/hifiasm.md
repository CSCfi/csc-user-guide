---
tags:
  - Free
catalog:
  name: hifiasm
  description: Haplotype-resolved de novo assembler for PacBio HiFi and ONT reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# hifiasm

Hifiasm is a fast haplotype-resolved de novo genome assembler for PacBio HiFi reads.
It can also assemble Oxford Nanopore (ONT) simplex R10 reads, and can use Hi-C reads,
parental data or ultra-long ONT reads to produce haplotype-resolved and
telomere-to-telomere assemblies.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/chhylp123/hifiasm/blob/master/LICENSE).

## Available

* Roihu-CPU: 0.25.0, via the `bio-apps` module.

## Usage

Hifiasm is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the hifiasm module:

```bash
module load bio-apps/v202603
module load hifiasm/0.25.0
```

Assemble HiFi reads, with `-o` giving the prefix of the output files and `-t` the
number of threads (the default is one thread):

```bash
hifiasm -o asm -t 32 reads.fq.gz 2> asm.log
```

The primary contigs are written to `asm.bp.p_ctg.gfa`, and two sets of partially
phased contigs to `asm.bp.hap1.p_ctg.gfa` and `asm.bp.hap2.p_ctg.gfa`. Convert the
primary contigs to FASTA with:

```bash
awk '/^S/{print ">"$2;print $3}' asm.bp.p_ctg.gfa > asm.p_ctg.fa
```

Useful options:

* `-l0`: disable duplication purging, for inbred or homozygous genomes.
* `-f0`: disable the initial bloom filter (16 GB of memory), for small genomes.
* `--ont`: assemble ONT simplex R10 reads (FASTQ) instead of HiFi reads.
* `--h1 read1.fq.gz --h2 read2.fq.gz`: phase the assembly with paired-end Hi-C reads.
* `--ul ul.fq.gz`: add ultra-long ONT reads.

Hifiasm saves the corrected reads and overlaps as `asm.*.bin` files and reuses them
if you run it again with the same prefix, which makes reruns with different
options much faster.

### Trio binning

When short reads from both parents are available, hifiasm can produce two
haplotype-resolved assemblies by trio binning. First count the parental k-mers
with [yak](yak.md), then give them to hifiasm with `-1` (paternal) and `-2`
(maternal):

```bash
module load bio-apps/v202603
module load yak/0.1
cat pat_1.fq.gz pat_2.fq.gz > pat.fq.gz
cat mat_1.fq.gz mat_2.fq.gz > mat.fq.gz
yak count -b37 -t 16 -o pat.yak pat.fq.gz
yak count -b37 -t 16 -o mat.yak mat.fq.gz
hifiasm -o asm -t 32 -1 pat.yak -2 mat.yak reads.fq.gz 2> asm.log
```

The two haplotype assemblies are written to `asm.dip.hap1.p_ctg.gfa` and
`asm.dip.hap2.p_ctg.gfa`. Hifiasm reuses the saved overlaps, so if you have already
run a standard assembly with the same prefix, you can give `/dev/null` instead of
the reads to skip read correction and overlapping.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=hifiasm
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=160G

module load bio-apps/v202603
module load hifiasm/0.25.0

hifiasm -o asm -t $SLURM_CPUS_PER_TASK reads.fq.gz 2> asm.log
```

The hifiasm documentation reports that a human genome (3.1 Gb, about 35x HiFi
coverage) takes around 8 hours and 140 GB of memory with 48 threads. Smaller
genomes need far less. Replace `<project>` with your CSC project (for example
`project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [hifiasm documentation](https://hifiasm.readthedocs.io/en/latest/)
* [hifiasm GitHub repository](https://github.com/chhylp123/hifiasm)
