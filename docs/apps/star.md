---
tags:
  - Free
---

# STAR


STAR (Spliced Transcripts Alignment to a Reference) is a fast NGS read aligner for  RNA-seq data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available



Puhti: 2.7.10a, 2.7.11a

## Usage

The `STAR` commands listed below are activated by loading `biokit` module.

```bash
module load biokit
```

Before you can run the actual alignment job, you must index your fasta formatted reference genome. In Puhti the working copies of reference genome indexes, as well as any large files, should be stored to the /scatch directory.

For ease of use, set an environment variable to point to your /scratch directory. (Substitute correct path for the one used in example).
```bash
export SCRATCH=/scratch/project_12345/$USER
```

Create a directory for the reference genome index:
```bash
mkdir $SCRATCH/star-genome
```

After that, the indexing can be done with command:
```bash
STAR --runMode genomeGenerate --genomeDir $SCRATCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN 2
```

Once the indexing is done, the actual mapping task can be launched. STAR will generate the mapping output using fixed file names. Because of that it is recommended that each STAR job is run in a new, empty directory. In Puhti you should create this new job directory to /scratch directory of your project. New directory called _starjob1_ can be created with command:
```bash
mkdir $SCRATCH/starjob1
```

after that the actual mapping job can be launched with commands:
```bash
cd $SCRATCH/starjob1
STAR --genomeDir $SCRATCH/star-genomes --readFilesIn my_reads.fastq
```

The default parameters STAR uses are typical for mapping 2x76 or 2x101 Illumina reads to the human genome.

In Puhti, all computing tasks should be executed as batch jobs. In batch jobs you can also utilize thread based parallelization. Below is a sample batch job file for STAR. The job uses six computing cores from a single computing node. The memory reservation is 24 GB. Note that you must change the `--account` setting to match you poject.
```bash
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

export SCRATCH=/scratch/project_12345/$USER

# calculate indexes. You don't need to recalculte the indexes if they already exist.
mkdir $SCRATCH/star-genome
STAR --runMode genomeGenerate --genomeDir $SCRATSCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN $SLURM_CPUS_PER_TASK

# Run the mapping task
STAR --genomeDir $SCRATCH/star-genome --readFilesIn my-reads.fastq --runThreadN $SLURM_CPUS_PER_TASK
```

The batch job script is launced with command sbatch. For example:
```bash
sbatch starjob1.sh
```


## More information

*   [STAR user manual](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf)
*   [STAR home page](https://github.com/alexdobin/STAR/)
