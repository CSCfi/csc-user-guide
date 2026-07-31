---
tags:
  - Free
catalog:
  name: SRA Toolkit
  description: Tools for downloading and converting data from the NCBI Sequence Read Archive
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SRA Toolkit

The SRA Toolkit from NCBI provides `prefetch`, `fasterq-dump` and related commands for
retrieving and converting sequencing data stored in the INSDC Sequence Read Archive.

[TOC]

## Available

* Roihu-CPU: `sra-tools`
* Roihu-CPU: `sratoolkit`
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail sra-tools` or `module avail sratoolkit` after
loading `bio-apps`.

`sra-tools` and `sratoolkit` are two separate Spack builds of the same NCBI SRA Toolkit,
so either module gives you the same `prefetch`/`fasterq-dump` commands.

## License

Public domain, released by NCBI as a
[United States Government Work](https://github.com/ncbi/sra-tools/blob/master/LICENSE)
that is freely usable without restriction.

## Usage

On Roihu, the SRA Toolkit is part of the `bio-apps` collection, which has to be loaded
first, followed by either `sra-tools` or `sratoolkit`:

```bash
module load bio-apps
module load sra-tools
```

```bash
module load bio-apps
module load sratoolkit
```

The basic workflow is to fetch an accession, then convert it to FASTQ:

```bash
prefetch SRR12345678
fasterq-dump SRR12345678
```

`fasterq-dump` writes a full-size FASTQ output plus temporary files that can together be
several times larger than the downloaded `.sra` file, so run the job from the scratch
directory of your project rather than `$HOME`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=sra-download
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load sra-tools

cd /scratch/<project>
srun prefetch SRR12345678
srun fasterq-dump --threads $SLURM_CPUS_PER_TASK SRR12345678
```

Submit the job with `sbatch sra_job.sh`.

## More information

* [sra-tools home page](https://github.com/ncbi/sra-tools)
* [sra-tools wiki](https://github.com/ncbi/sra-tools/wiki)
* [SRA home page](https://trace.ncbi.nlm.nih.gov/Traces/sra)
* [CSC Service Desk](../support/contact.md)
