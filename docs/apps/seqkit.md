---
tags:
  - Free
catalog:
  name: SeqKit
  description: Cross-platform FASTA/FASTQ toolkit
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SeqKit

SeqKit is a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. It
provides a wide range of subcommands for common sequence operations such as statistics,
searching, filtering, subsampling and format conversion.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/shenwei356/seqkit/blob/master/LICENSE).

## Available

* Roihu: 2.10.0, via the `bio-apps` module.

## Usage

SeqKit is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SeqKit module:

```bash
module load bio-apps/v202603
module load seqkit/2.10.0
```

SeqKit is run through the `seqkit` command followed by a subcommand. For example, to
print summary statistics for a set of FASTA files:

```bash
seqkit stats *.fasta
```

or to filter sequences by minimum length:

```bash
seqkit seq -m 1000 input.fasta > long_sequences.fasta
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=seqkit
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load seqkit/2.10.0

seqkit stats -j $SLURM_CPUS_PER_TASK *.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SeqKit documentation](https://bioinf.shenwei.me/seqkit/)
* [SeqKit GitHub repository](https://github.com/shenwei356/seqkit)
