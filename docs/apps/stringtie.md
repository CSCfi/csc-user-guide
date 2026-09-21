---
tags:
  - Free
catalog:
  name: StringTie
  description: Transcript assembly and quantification for RNA-Seq
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# StringTie

StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential
transcripts. It can be used for transcript assembly and quantification, either de novo
or guided by a reference annotation.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/gpertea/stringtie/blob/master/LICENSE).

## Available

* Roihu: 3.0.3, via the `bio-apps` module.

## Usage

StringTie is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the StringTie module:

```bash
module load bio-apps/v202603
module load stringtie/3.0.3
```

Assemble transcripts from a sorted BAM file, optionally guided by a reference
annotation:

```bash
stringtie aligned.sorted.bam -G annotation.gtf -o assembled.gtf -p 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=stringtie
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
module load stringtie/3.0.3

stringtie aligned.sorted.bam -G annotation.gtf -o assembled.gtf -p $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [StringTie home page](https://ccb.jhu.edu/software/stringtie/)
