---
tags:
  - Free
catalog:
  name: STAR
  description: Short read aligner
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# STAR

STAR (Spliced Transcripts Alignment to a Reference) is a fast NGS read aligner for RNA-seq data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 2.7.11b, via the `bio-apps` module.

## Usage

STAR is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the STAR module:

```bash
module load bio-apps/v202603
module load star/2.7.11b
```

Before you can run the actual alignment job, you must index your fasta formatted reference genome. On Roihu the working copies of reference genome indexes, as well as any large files, should be stored to the /scratch directory.

For ease of use, set an environment variable to point to your /scratch directory. (Substitute the correct path for the one used in the example.)

```bash
export SCRATCH=/scratch/<project>/$USER
```

Create a directory for the reference genome index:

```bash
mkdir $SCRATCH/star-genome
```

After that, the indexing can be done with command:

```bash
STAR --runMode genomeGenerate --genomeDir $SCRATCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN 2
```

Once the indexing is done, the actual mapping task can be launched. STAR will generate the mapping output using fixed file names. Because of that it is recommended that each STAR job is run in a new, empty directory. On Roihu you should create this new job directory to the /scratch directory of your project. A new directory called _starjob1_ can be created with command:

```bash
mkdir $SCRATCH/starjob1
```

after that the actual mapping job can be launched with commands:

```bash
cd $SCRATCH/starjob1
STAR --genomeDir $SCRATCH/star-genome --readFilesIn my_reads.fastq
```

The default parameters STAR uses are typical for mapping 2x76 or 2x101 Illumina reads to the human genome.

On Roihu, all computing tasks should be executed as batch jobs. In batch jobs you can also utilize thread based parallelization. Below is a sample batch job file for STAR. The job uses six computing cores from a single computing node. The memory reservation is 24 GB. Note that you must change the `--account` setting to match your project.

```bash
#!/bin/bash
#SBATCH --job-name=STAR
#SBATCH --account=<project>
#SBATCH --output=STAR.stdout
#SBATCH --error=STAR.stderr
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=24000

module load bio-apps/v202603
module load star/2.7.11b

export SCRATCH=/scratch/<project>/$USER

# calculate indexes. You don't need to recalculate the indexes if they already exist.
mkdir $SCRATCH/star-genome
STAR --runMode genomeGenerate --genomeDir $SCRATCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN $SLURM_CPUS_PER_TASK

# Run the mapping task
STAR --genomeDir $SCRATCH/star-genome --readFilesIn my-reads.fastq --runThreadN $SLURM_CPUS_PER_TASK
```

The batch job script is launched with command `sbatch`. For example:

```bash
sbatch starjob1.sh
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [STAR user manual](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf)
*   [STAR home page](https://github.com/alexdobin/STAR/)
