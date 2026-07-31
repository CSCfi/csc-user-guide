---
tags:
  - Free
catalog:
  name: Jellyfish
  description: Tool for fast, memory-efficient counting of k-mers in DNA
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Jellyfish

Jellyfish is a command-line tool for fast, memory-efficient counting of k-mers,
substrings of a fixed length, in DNA sequences.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail jellyfish` after loading `bio-apps`.

## License

Free to use and open source under [GNU General Public License v3.0][jellyfish-license].

[jellyfish-license]: https://github.com/gmarcais/Jellyfish/blob/master/LICENSE-GPL-3.0

## Usage

On Roihu, Jellyfish is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load jellyfish
```

Count 21-mers in a FASTQ file, then summarise the resulting histogram:

```bash
jellyfish count -m 21 -s 100M -t 8 -C reads.fastq -o reads.jf
jellyfish histo reads.jf > reads.histo
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=jellyfish
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load jellyfish

srun jellyfish count -m 21 -s 100M -t $SLURM_CPUS_PER_TASK -C reads.fastq -o reads.jf
```

Submit the job with `sbatch jellyfish_job.sh`.

## More information

* [Jellyfish home page](https://www.cbcb.umd.edu/software/jellyfish/)
* [CSC Service Desk](../support/contact.md)
