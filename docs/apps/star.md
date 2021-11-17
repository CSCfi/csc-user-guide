# STAR

## Description
STAR (Spliced Transcripts Alignment to a Reference) is a fast NGS read aligner for  RNA-seq data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Version on CSC's Servers

Puhti: 2.7.2

## Usage

The _STAR_ commands listed abowe are activated by loading _biokit_ module.

```text
module load biokit
```

Before you can run the actual alignment job, you must index your fasta formatted reference genome. In Puhti the working copies of
 reference genome indexes, as well as any large files, should be stored to the scatch directory ($SCRATCH). In this example we store the indexes to the directory $SCRATCH/star-genomes.

First the reference genome index directory is generated with command:
```text
mkdir $SCRATCH/star-genome
```
After that, the indexing can be done with command:
```text
STAR --runMode genomeGenerate --genomeDir $SCRATCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN 2
```
Once the indexing is done the actual mapping task can be launched. STAR will generate the mapping output using fixed file names.
Because of that it is recommended that each STAR job is run in a new, empty directory. In Puhti you should create this new job directory 
to scratch directory ($SCRATCH) of your project. New directory called _starjob1_ can be created with command:
```text
mkdir $SCRATCH/starjob1
```
after that the actual mapping job can be launched with commands:
```text
cd $SCRATCH/starjob1
STAR --genomeDir $SCRATCH/star-genomes --readFilesIn my_reads.fastq
```
The default parameters, that STAR uses, are typical for mapping 2x76 or 2x101 Illumina reads to the human genome. In Puhti the default parameter settings are available in file:
```text
/appl/soft/bio/star/STAR-2.7.2a/source/parametersDefault
```
In Puhti, all heavier computing tasks should be executed as batch jobs. In batch jobs you can also utilize thread based 
parallelization. Bellow is a sample batch job file for STAR. The job uses six computing cores from a single computing node. 
The memory reservation is 24 GB (4GB/core * 6 cores). Note that you must change the _--account_ setting to match you poject.
```text
#!/bin/bash -l
#SBATCH --job-name=STAR
#SBATCH --output=STAR.stdout
#SBATCH --error=STAR.stderr
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=6
#SBATCH --account=project_1234567
#SBATCH --mem=24000

# calculate indexes. You don't need to recalculte the indexes if they already exist.
mkdir $SCRATCH/star-genome
STAR --runMode genomeGenerate --genomeDir $SCRATSCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN $SLURM_CPUS_PER_TASK

# Run the mapping task
STAR --genomeDir $SCRATCH/star-genome --readFilesIn my-reads.fastq --runThreadN $SLURM_CPUS_PER_TASK
```

The batch job script is launced with command sbatch. For example:
```
sbatch starjob1.sh
```


## Manual

*   [STAR user manual](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf)
*   [STAR home page](https://github.com/alexdobin/STAR/)




