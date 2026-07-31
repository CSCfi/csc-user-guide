---
tags:
  - Free
catalog:
  name: Picard Tools
  description: Tools for working with SAM,BAM,CRAM and VCF files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
    - Roihu
---

# Picard Tools



Picard is a set of command line tools for manipulating high-throughput
sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.


[TOC]

## License

Free to use and open source under [MIT License](https://github.com/broadinstitute/picard/blob/master/LICENSE.txt).

## Available


- Puhti:  2.27.4, 2.27.5, 3.0.1,  3.1.1
- Roihu-CPU

Check the installed versions on Roihu with `module avail picard` after
loading `bio-apps`.

## Usage

### Puhti

To load Picard, load module:
```bash
module load picard
```

Note: The `biokit` module comes with Picard version 2.27.5 due to Java version compatibility
with other software. To use newer version of Picard, load the `picard` module.

To get a summary of available tools:
```bash
picard
```

Please note that in the Picard manual commands start with "java -jar
picard.jar". In Puhti it is easiest to run Picard through a wrapper script,
so substitute that with just `picard`.

Example:
```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

By default picard can use up to 8 GB  of memory. If your analysis task
requires more memory, you can launch picard with commands, `picard16`, `picard32`
and `picard64` that reserve 16, 32 or 64 GB of memory respectively.

Example:
```bash
picard16 SamToFASTQ I=input.bam FASTQ=output.fastq
```

If you need to specify Java options for Picard you can use `java -jar $PICARD`.

Example:
```bash
java -Xmx128g -jar $PICARD  SamToFASTQ I=input.bam FASTQ=output.fastq
```

### Roihu

On Roihu, Picard is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load picard
```

Picard is used the same way as on Puhti, for example:

```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=picard
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=8G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load picard

srun picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

Submit the job with `sbatch picard_roihu_job.sh`.

## More information

-   [Picard home page](http://broadinstitute.github.io/picard/)
-   [Detailed tool documentation](http://broadinstitute.github.io/picard/command-line-overview.html)
