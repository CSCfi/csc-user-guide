---
tags:
  - Free
catalog:
  name: HTSlib
  description: C library for high-throughput sequencing data formats
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HTSlib

HTSlib is the C library that implements the core SAM/BAM/CRAM and VCF/BCF file
formats used across high-throughput sequencing, and is the engine behind SAMtools
and BCFtools.

[TOC]

## Available

* Roihu-CPU: 1.23.1
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail htslib` after loading `bio-apps`.

## License

Free to use and open source, mostly under the
[MIT/Expat License](https://github.com/samtools/htslib/blob/develop/LICENSE), with the CRAM
code under a modified BSD license.

## Usage

On Roihu, HTSlib is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load htslib
```

HTSlib is mainly a library that other tools such as SAMtools link against at build
time, but the module also provides its `bgzip` and `tabix` command-line utilities:

```bash
bgzip input.vcf
tabix -p vcf input.vcf.gz
```

Batch jobs should still go through Slurm. An example batch job script that
compresses a file with `bgzip`:

```bash
#!/bin/bash
#SBATCH --job-name=htslib
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load htslib

srun bgzip input.vcf
```

Submit the job with `sbatch htslib_job.sh`.

## More information

* [HTSlib home page](https://github.com/samtools/htslib)
* [HTSlib documentation](https://www.htslib.org/doc/)
* [CSC Service Desk](../support/contact.md)
