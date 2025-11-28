---
tags:
  - Free
catalog:
  name: Trimmomatic
  description: Trim Illumina paired-end and single-read data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Trimmomatic

Trimmomatic performs a variety of useful trimming tasks for illumina paired-end and single ended data.

[TOC]

## License

- Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).
- The license does NOT apply to the sequence of the Illumina sequences contained in the software.
THE ILLUMINA sequences (adapters) etc REMAIN COPYRIGHTED and owned by Illumina and are used in Trimmomatic by permission.

## Available

- Puhti: 0.39
- [Chipster](https://chipster.csc.fi) graphical user interface

## Usage

Trimmomatic is included in the `biokit` module:

```bash
module load biokit
```

It can also be loaded separately:

```bash
module load trimmomatic
```

Trimmomatic can be launched with command:

```bash
trimmomatic
```

If you need to adjust Java settings you can use variable `$TMJAR`

```bash
java <java options> -jar $TMJAR <trimmomatic options>
```

Included adapter sequences for ILLUMINACLIP can be used by specifying `$ADAPTERS`, e.g:

```bash
ILLUMINACLIP:$ADAPTERS/TruSeq3-PE.fa:2:30:10
```

Trimmomatic jobs should be run either in an [interactive session](../computing/running/interactive-usage.md) or as batch job.

Example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=trimmomatic
#SBATCH --account=project_12345 # Substitute your project name
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8000

trimmomatic PE -threads $SLURM_CPUS_PER_TASK -phred64 \
forward.fq.gz reverse.fq.gz \
out_fw_paired.fq.gz out_fw_unpaired.fq.gz out_rev_paired.fq.gz out_rev_unpaired.fq.gz \
ILLUMINACLIP:$ADAPTERS/TruSeq3-PE.fa:2:30:10 \
LEADING:3 \
TRAILING:3 \
SLIDINGWINDOW:4:15 \
MINLEN:36
```

The batch job could be launched with command:

```bash
sbatch trimmomatic_script
```

## More information

* [Trimmomatic home page](http://www.usadellab.org/cms/?page=trimmomatic)
