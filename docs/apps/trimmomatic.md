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
    - Roihu
---

# Trimmomatic

Trimmomatic performs a variety of useful trimming tasks for illumina paired-end and single ended data.

[TOC]

## License

- Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).
- The license does NOT apply to the sequence of the Illumina sequences contained in the software.
THE ILLUMINA sequences (adapters) etc REMAIN COPYRIGHTED and owned by Illumina and are used in Trimmomatic by permission.

## Available

* Roihu: 0.39, via the `bio-apps` module.

## Usage

Trimmomatic is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Trimmomatic module:

```bash
module load bio-apps/v202603
module load trimmomatic/0.39
```

Trimmomatic can be launched with the command:

```bash
trimmomatic
```

If you need to adjust Java settings, such as the maximum heap size, set the
`_JAVA_OPTIONS` environment variable, which the Java runtime picks up automatically:

```bash
export _JAVA_OPTIONS="-Xmx8g"
```

Trimmomatic ships a set of standard Illumina adapter files. The module sets the
`$TRIMMOMATIC_INSTROOT` environment variable, which points to the installation, and
the bundled adapter files are located under `$TRIMMOMATIC_INSTROOT/share/adapters`.
Give the path to the adapter file you need in the `ILLUMINACLIP` step, for example:

```bash
ILLUMINACLIP:$TRIMMOMATIC_INSTROOT/share/adapters/TruSeq3-PE.fa:2:30:10
```

Trimmomatic jobs should be run either in an [interactive session](../computing/running/interactive-usage.md) or as a batch job.

Example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=trimmomatic
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8000

module load bio-apps/v202603
module load trimmomatic/0.39

trimmomatic PE -threads $SLURM_CPUS_PER_TASK -phred33 \
forward.fq.gz reverse.fq.gz \
out_fw_paired.fq.gz out_fw_unpaired.fq.gz out_rev_paired.fq.gz out_rev_unpaired.fq.gz \
ILLUMINACLIP:$TRIMMOMATIC_INSTROOT/share/adapters/TruSeq3-PE.fa:2:30:10 \
LEADING:3 \
TRAILING:3 \
SLIDINGWINDOW:4:15 \
MINLEN:36
```

The batch job could be launched with command:

```bash
sbatch trimmomatic_script
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Trimmomatic home page](http://www.usadellab.org/cms/?page=trimmomatic)
