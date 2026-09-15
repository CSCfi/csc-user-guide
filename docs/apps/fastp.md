---
tags:
  - Free
catalog:
  name: fastp
  description: Fast all-in-one FASTQ preprocessing and QC
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# fastp

fastp is a tool designed to provide fast all-in-one preprocessing for FASTQ files. It
performs adapter trimming, quality filtering, per-read quality pruning and generates
quality-control reports in HTML and JSON.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/OpenGene/fastp/blob/master/LICENSE).

## Available

* Roihu: 1.0.1, via the `bio-apps` module.

## Usage

fastp is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the fastp module:

```bash
module load bio-apps/v202603
module load fastp/1.0.1
```

For paired-end data:

```bash
fastp -i read1.fq.gz -I read2.fq.gz -o out1.fq.gz -O out2.fq.gz --thread 4
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=fastp
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load fastp/1.0.1

fastp -i read1.fq.gz -I read2.fq.gz -o out1.fq.gz -O out2.fq.gz --thread $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [fastp GitHub repository](https://github.com/OpenGene/fastp)
