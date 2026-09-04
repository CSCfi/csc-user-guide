---
tags:
  - Free
catalog:
  name: SRA Toolkit
  description: NCBI SRA Toolkit for accessing and converting SRA data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SRA Toolkit (sra-tools)

The SRA Toolkit and SDK from NCBI is a collection of tools and libraries for using data
in the INSDC Sequence Read Archives (SRA). It includes tools such as `prefetch` (for
downloading) and `fasterq-dump` (for converting SRA data to FASTQ).

[TOC]

## License

The SRA Toolkit is released into the public domain by the US National Library of
Medicine. See the [sra-tools repository](https://github.com/ncbi/sra-tools).

## Available

* Roihu: 3.3.0 (module `sra-tools`), via the `bio-apps` module.

## Usage

sra-tools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load sra-tools/3.3.0
```

!!! info "Configuration"
    On first use, configure the toolkit with `vdb-config` and point its cache to a
    location with space (for example your project's `/scratch`) so it does not fill your
    home directory.

Download an accession and convert it to FASTQ:

```bash
prefetch SRR000001
fasterq-dump SRR000001 --threads 8 --outdir fastq
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=fasterq-dump
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load sra-tools/3.3.0

fasterq-dump SRR000001 --threads $SLURM_CPUS_PER_TASK --outdir fastq
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [sra-tools GitHub repository](https://github.com/ncbi/sra-tools)
* [SRA Toolkit documentation](https://github.com/ncbi/sra-tools/wiki)
