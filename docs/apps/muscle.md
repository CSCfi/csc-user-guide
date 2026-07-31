---
tags:
  - Free
catalog:
  name: MUSCLE
  description: Multiple sequence alignment of biological sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MUSCLE

MUSCLE aligns multiple nucleotide or protein sequences, offering accuracy and speed that
compare favourably with other widely used aligners such as ClustalW.

[TOC]

## Available

* Roihu-CPU: `muscle` 3.8.31
* Roihu-CPU: `muscle5` 5.1.0
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail muscle` / `module avail muscle5` after loading
`bio-apps`.

`muscle` is the classic MUSCLE 3 release, while `muscle5` is the current MUSCLE 5 line,
which replaced the `-in`/`-out` command-line syntax with `-align`/`-output` and added
multi-threaded alignment.

## License

MUSCLE 3 is dedicated to the public domain; see the
[public domain notice](https://drive5.com/muscle/manual/license.html). MUSCLE 5 is free
and open source under the
[GNU GPLv3](https://github.com/rcedgar/muscle/blob/main/LICENSE).

## Usage

On Roihu, MUSCLE is part of the `bio-apps` collection, which has to be loaded first,
followed by either `muscle` or `muscle5`:

```bash
module load bio-apps
module load muscle
```

```bash
module load bio-apps
module load muscle5
```

MUSCLE 3 uses the syntax:

```bash
muscle -in input.fasta -out aligned.fasta
```

MUSCLE 5 uses the newer syntax:

```bash
muscle -align input.fasta -output aligned.afa
```

Heavier jobs should be run as batch jobs. Only MUSCLE 5 is multi-threaded, scaling with
the number of threads given to `-threads`; MUSCLE 3 always runs on a single core. An
example batch job script for MUSCLE 5:

```bash
#!/bin/bash
#SBATCH --job-name=muscle5
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load muscle5

srun muscle -threads $SLURM_CPUS_PER_TASK -align input.fasta -output aligned.afa
```

Submit the job with `sbatch muscle5_job.sh`. For MUSCLE 3, use the same script with
`module load muscle`, `--cpus-per-task=1` and the `-in`/`-out` syntax instead.

## More information

* [MUSCLE 3 home page](https://drive5.com/muscle/)
* [MUSCLE 5 home page](https://drive5.com/muscle5/)
* [CSC Service Desk](../support/contact.md)
