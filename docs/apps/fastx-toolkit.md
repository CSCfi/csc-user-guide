---
tags:
  - Free
catalog:
  name: FASTX-Toolkit
  description: FASTA/FASTQ short-read preprocessing tools
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# FASTX-Toolkit

The FASTX-Toolkit is a collection of command line tools for preprocessing short-read
FASTA/FASTQ files. It includes tools such as `fastx_trimmer`, `fastq_quality_filter`,
`fastx_clipper` and `fastx_collapser`.

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://github.com/agordon/fastx_toolkit/blob/master/COPYING).

## Available

* Roihu: 0.0.14, via the `bio-apps` module.

## Usage

FASTX-Toolkit is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the FASTX-Toolkit module:

```bash
module load bio-apps/v202603
module load fastx-toolkit/0.0.14
```

For example, to trim reads to a fixed length:

```bash
fastx_trimmer -l 50 -i input.fastq -o trimmed.fastq
```

or to filter by quality:

```bash
fastq_quality_filter -q 20 -p 80 -i input.fastq -o filtered.fastq
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=fastx
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

module load bio-apps/v202603
module load fastx-toolkit/0.0.14

fastx_trimmer -l 50 -i input.fastq -o trimmed.fastq
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [FASTX-Toolkit home page](http://hannonlab.cshl.edu/fastx_toolkit/)
