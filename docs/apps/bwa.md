---
tags:
  - Free
---

# BWA

Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively short nucleotide sequences against a long reference sequence such as the human genome. It implements three algorithms, BWA-MEM (`mem`), BWA-Backtrack (`aln`) and BWA-SW (`bwasw`). BWA-Backtrack works for query sequences shorter than 200bp. The other two algorithms are used longer reads up to around 100kbp. BWA-MEM is recommended for reads longer than 70gb. All algorithms do gapped alignment.

BWA can be used to align both single-end and paired-end reads to a reference genome or sequence set.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Puhti: 0.7.17
- [Chipster](https://chipster.csc.fi) graphical user interface

## Usage

On Puhti, BWA can be taken in use as part of the `biokit` module collection:

```bash
module load biokit
```

The biokit modules set up a set of commonly used bioinformatics tools, including BWA. Note however that there are other bioinformatics tools on Puhti that have separate setup commands.

The basic syntax of BWA commands is:

```bash
bwa <command> [options]
```

### BWA indexes

CSC does not maintain pre-compiled BWA indexes for reference genomes on Puhti, but you can check if genomes used in Chipster can provide you a ready-made index for a genome you want use. This can be done with the command:

```
chipster_genomes bwa
``` 

If a suitable genome index is not found, the fist step in creating alignment with BWA is downloading the reference genome and indexing it. Please note that your `$HOME` directory is often too small for working with complete genomes. Instead, you should do the analysis in the scratch directory of your Puhti project.

You can use for example command `ensemblfetch` or `wget` to download a reference genome to Puhti. For example:

```bash
ensemblfetch homo_sapiens
```

The command above retrieves the human genome sequence to a file called `Homo_sapiens.GRCh38.dna.toplevel.fa`. You can calculate the BWA indexes for this file with the command:

```bash
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa
```

Note that for small less than 2 GB reference genomes you could use a faster "is" indexing algorithm (`bwa index -a is`)

### Single-end alignment

Once the indexing is ready you can carry out the alignment for singe-end reads with the command:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln.sam
```

If you wish to use the `aln` (BWA-Backtrack) algorithm, you need to do the alignment in two steps.

First calculate the actual alignment:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln_sa.sai
```

The result file is in BWA-specific `.sai` format that you can convert to SAM format with `bwa samse` command:

```bash
bwa samse Homo_sapiens.GRCh38.dna.toplevel.fa aln_sa.sai reads.fastq > aln.sam
```

### Paired-end alignment

If you use the MEM algorithm, you can do the paired-end alignment with just one command:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa read1.fq read2.fq > aln.sam
```

In the case of BWA-Backtrack algorithm, you should first do a separate alignment run for each read file:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq > aln1.sai
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads2.fq > aln2.sai
```

The two `.sai` alignment files are combined with command `bwa sampe`:

```bash
bwa sampe Homo_sapiens.GRCh38.dna.toplevel.fa aln1.sai aln2.sai reads1.fq reads2.fq > aln.sam
```

### Running BWA batch jobs on Puhti

In Puhti, BWA jobs should be run as batch jobs. Below is a sample batch job file for running a BWA job on Puhti:

```bash
#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=32000
#SBATCH --account=your_project_name

#load the bio tools
module load biokit

# Index the reference genome
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa

# Run the alignnments
bwa mem -t $SLURM_CPUS_PER_TASK Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq reads2.fq > aln.sam
```

In the batch job example above, one BWA task (`--ntasks=1`) is executed. The BWA job uses 8 cores (`--cpus-per-task=8`) with a total of 32 GB of memory (`--mem=32000`). The maximum duration of the job is twelve hours (`--time 12:00:00`). All the cores are assigned from one computing node (`--nodes=1`). In addition to the resource reservations, you have to define the billing project for your batch job. This is done by replacing `your_project_name` with the name of your project. You can use command `csc-projects` to see what projects you have on Puhti.

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.bash
```

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## More information

More information about BWA can be found from:

* [BWA home page](http://bio-bwa.sourceforge.net/index.shtml)
* [BWA manual](http://bio-bwa.sourceforge.net/bwa.shtml)
