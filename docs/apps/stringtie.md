---
tags:
  - Free
catalog:
  name: StringTie
  description: Transcript assembly and quantification for RNA-Seq alignments
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# StringTie

StringTie assembles aligned RNA-Seq reads into transcripts and estimates their
expression levels, working from a sorted BAM file of spliced read alignments.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail stringtie` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/gpertea/stringtie/blob/master/LICENSE).

## Usage

On Roihu, StringTie is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load stringtie
```

The basic syntax is:

```bash
stringtie aligned.sorted.bam -o transcripts.gtf
```

Assembling a large BAM file benefits from multiple threads via `-p`. An example batch
job script:

```bash
#!/bin/bash
#SBATCH --job-name=stringtie
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load stringtie

srun stringtie aligned.sorted.bam -p $SLURM_CPUS_PER_TASK -o transcripts.gtf
```

Submit the job with `sbatch stringtie_job.sh`.

## More information

* [StringTie home page and manual](https://ccb.jhu.edu/software/stringtie)
* [CSC Service Desk](../support/contact.md)
