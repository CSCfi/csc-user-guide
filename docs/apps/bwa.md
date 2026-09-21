---
tags:
  - Free
catalog:
  name: BWA
  description: Short read aligner
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BWA

Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively short nucleotide sequences against a long reference sequence such as the human genome. It implements three algorithms, BWA-MEM (`mem`), BWA-Backtrack (`aln`) and BWA-SW (`bwasw`). BWA-Backtrack works for query sequences shorter than 200 bp. The other two algorithms are used for longer reads up to around 100 kbp. BWA-MEM is recommended for reads longer than 70 bp. All algorithms do gapped alignment.

BWA can be used to align both single-end and paired-end reads to a reference genome or sequence set.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 0.7.19, via the `bio-apps` module.

## Usage

BWA is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BWA module:

```bash
module load bio-apps/v202603
module load bwa/0.7.19
```

The basic syntax of BWA commands is:

```bash
bwa <command> [options]
```

### BWA indexes

The first step in aligning with BWA is downloading the reference genome and indexing it. Note that your `$HOME` directory is often too small for working with complete genomes; you should do the analysis in the scratch directory of your project instead.

Download a reference genome (for example with `wget`) to your scratch directory, then calculate the BWA indexes for it:

```bash
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa
```

Note that for small (less than 2 GB) reference genomes you could use the faster "is" indexing algorithm (`bwa index -a is`).

### Single-end alignment

Once the indexing is ready you can carry out the alignment for single-end reads with the command:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln.sam
```

If you wish to use the `aln` (BWA-Backtrack) algorithm, you need to do the alignment in two steps.

First calculate the actual alignment:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln_sa.sai
```

The result file is in BWA-specific `.sai` format that you can convert to SAM format with the `bwa samse` command:

```bash
bwa samse Homo_sapiens.GRCh38.dna.toplevel.fa aln_sa.sai reads.fastq > aln.sam
```

### Paired-end alignment

If you use the MEM algorithm, you can do the paired-end alignment with just one command:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa read1.fq read2.fq > aln.sam
```

In the case of the BWA-Backtrack algorithm, you should first do a separate alignment run for each read file:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq > aln1.sai
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads2.fq > aln2.sai
```

The two `.sai` alignment files are combined with the `bwa sampe` command:

```bash
bwa sampe Homo_sapiens.GRCh38.dna.toplevel.fa aln1.sai aln2.sai reads1.fq reads2.fq > aln.sam
```

### Example batch script

BWA jobs should be run as batch jobs. Below is a sample batch job script for running a BWA job on Roihu:

```bash
#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4000M

module load bio-apps/v202603
module load bwa/0.7.19

# Index the reference genome
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa

# Run the alignment
bwa mem -t $SLURM_CPUS_PER_TASK Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq reads2.fq > aln.sam
```

In the batch job example above, one BWA task (`--ntasks=1`) is executed. The BWA job uses 8 cores (`--cpus-per-task=8`) with a total of 32 GB of memory. The maximum duration of the job is twelve hours (`--time=12:00:00`). All the cores are assigned from one computing node (`--nodes=1`). Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

More information about BWA can be found from:

* [BWA home page](http://bio-bwa.sourceforge.net/index.shtml)
* [BWA manual](http://bio-bwa.sourceforge.net/bwa.shtml)
