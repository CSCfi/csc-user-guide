---
tags:
  - Free
---

# Minimap2

Minimap2 is a fast general-purpose alignment program to map DNA or long mRNA sequences against a large reference database.
It can be used for:

* mapping of accurate short reads (preferably longer than 100 bases)
* mapping 1kb genomic reads at error rate 15% (e.g. PacBio or Oxford Nanopore genomic reads)
* mapping full-length noisy Direct RNA or cDNA reads
* mapping and comparing assembly contigs or closely related full chromosomes of hundreds of megabases in length

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/lh3/minimap2/master/LICENSE.txt).

## Available

* Puhti: 2.24
* Chipster graphical user interface

## Usage

On Puhti, Minimap2 can be used as part of the `biokit` module collection:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including Minimap2. Note however that there are other bioinformatics tools on Puhti that have separate setup commands.
Once biokit module is loaded, Minimap2 starts with the command:

```bash
minimap2
```

Without any options, `minimap2` takes a reference database and a query sequence file as input and produce approximate mapping, without base-level alignment (i.e. no CIGAR), in the PAF format:

```bash
minimap2 ref.fa query.fq > approx-mapping.paf
```

If you wish to get the output in SAM format, you can use option `-a`.

For different data types, Minimap2 needs to be tuned for optimal performance and accuracy.
With option `-x` you can use case specific parameter sets, pre-defined and recommended by the Minimap2 developers.
 
### Map long noisy genomic reads (_map-pb_ and _map-ont_)

* PacBio subreads (_map-db_):

```bash
minimap2 -ax map-pb ref.fa pacbio-reads.fq > aln.sam
```

* Oxford Nanopore reads (_map-ont_):

```bash
minimap2 -ax map-ont ref.fa ont-reads.fq > aln.sam 
```

### Map long mRNA/cDNA reads (splice)

* PacBio Iso-seq/traditional cDNA

```bash
minimap2 -ax splice -uf ref.fa iso-seq.fq > aln.sam
``` 

* Nanopore 2D cDNA-seq

```bash
minimap2 -ax splice ref.fa nanopore-cdna.fa > aln.sam
```

* Nanopore Direct RNA-seq

```bash
minimap2 -ax splice -uf -k14 ref.fa direct-rna.fq > aln.sam
```
 
* mapping against SIRV control

```bash
minimap2 -ax splice --splice-flank=no SIRV.fa SIRV-seq.fa
```

### Find overlaps between long reads (_ava-pb_ and _aca-ont_)

* PacBio read overlap

```bash
minimap2 -x ava-pb reads.fq reads.fq > ovlp.paf
```

* Oxford Nanopore read overlap

```bash
minimap2 -x ava-ont reads.fq reads.fq > ovlp.paf
```

### Map short accurate genomic reads (sr)

Note, Minimap2 does not work well with short spliced reads.

* single-end alignment

```bash
minimap2 -ax sr ref.fa reads-se.fq > aln.sam
```

* paired-end alignment

```bash
minimap2 -ax sr ref.fa read1.fq read2.fq > aln.sam
```

* paired-end alignment

```bash
minimap2 -ax sr ref.fa reads-interleaved.fq > aln.sam 
```

### Full genome/assembly alignment (_asm5_)

* assembly to assembly

```bash
minimap2 -ax asm5 ref.fa asm.fa > aln.sam
```

## Example batch script for Puhti

On Puhti, Minimap2 jobs should be run as batch jobs. Below is a sample batch job file
for running a Minimap2 paired-end alignment on Puhti.

```bash
#!/bin/bash -l
#SBATCH --job-name=minimap2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --account=<project>
#SBATCH --mem=16000

module load biokit
minimap2 -t $SLURM_CPUS_PER_TASK -ax splice -uf ref.fa iso-seq.fq > aln.sam
```

In the batch job example above, one task (`--ntasks=1`) is executed. The Minimap2 job
uses 8 cores (`--cpus-per-task=8`) with a total of 16 GB of memory (`--mem=16000`).
The maximum duration of the job is four hours (`--time=04:00:00`). All the cores
are assigned from one computing node (`--nodes=1`). In addition to the resource
reservations, you have to define the billing project for your batch job. This
is done by replacing the `<project>` with the name of your project. You can
use command `csc-projects` to see what projects you have on Puhti.

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.bash
```

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* More information about Minimap2 can be found from the [Minimap2 home page](https://lh3.github.io/minimap2/).
