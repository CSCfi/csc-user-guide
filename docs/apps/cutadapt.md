---
tags:
  - Free
catalog:
  name: Cutadapt
  description: Trimming high-throughput sequencing reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Cutadapt

Cutadapt finds and removes adapter sequences, primers, poly-A tails and other types of 
unwanted sequence from your high-throughput sequencing reads.

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/marcelm/cutadapt/blob/main/LICENSE).

## Available

* Roihu-CPU: 4.7, 5.1 and 5.2 (module `py-cutadapt`), via the `bio-apps` module.

## Usage

Cutadapt is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Cutadapt module:

```bash
module load bio-apps/v202603
module load py-cutadapt/5.2
```

Remove an adapter from the 3' end of single-end reads:

```bash
cutadapt -a AGATCGGAAGAGC -o trimmed.fastq.gz reads.fastq.gz
```

For paired-end reads, give the adapter of the second read with `-A` and the second
output file with `-p`:

```bash
cutadapt -a AGATCGGAAGAGC -A AGATCGGAAGAGC -o trimmed_1.fastq.gz -p trimmed_2.fastq.gz \
  reads_1.fastq.gz reads_2.fastq.gz
```

Cutadapt uses one core by default. Use `-j` to set the number of cores.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=cutadapt
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8G

module load bio-apps/v202603
module load py-cutadapt/5.2

cutadapt -j $SLURM_CPUS_PER_TASK -a AGATCGGAAGAGC -A AGATCGGAAGAGC \
  -o trimmed_1.fastq.gz -p trimmed_2.fastq.gz reads_1.fastq.gz reads_2.fastq.gz
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Cutadapt documentation](https://cutadapt.readthedocs.io/en/stable/)
