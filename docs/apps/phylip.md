---
tags:
  - Free
catalog:
  name: PHYLIP
  description: Package of programs for inferring phylogenies
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PHYLIP

PHYLIP (the PHYLogeny Inference Package) is a collection of around 30 separate programs
for inferring evolutionary trees, covering parsimony, distance matrix and likelihood
methods for DNA, protein, and other kinds of data.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail phylip` after loading `bio-apps`.

## License

Free to use and open source under
[BSD 2-Clause License](https://github.com/phylipweb/phylip/blob/main/LICENSE).

## Usage

On Roihu, PHYLIP is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load phylip
```

PHYLIP has no single command; each program (`dnapars`, `neighbor`, `seqboot`,
`consense`, `drawtree`, and so on) implements one method. Every program is interactive:
it looks for an input file named `infile` in the current directory, then asks a series
of menu questions before writing `outfile` (and `outtree` for tree-building programs).

To run a PHYLIP program non-interactively in a batch job, put your data in `infile` and
redirect the menu answers from a text file. For example, to run `dnapars` and accept all
its default settings:

```bash
cp alignment.phy infile
echo "Y" > dnapars_answers.txt
dnapars < dnapars_answers.txt > screen.log
```

An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=phylip
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load phylip

cp alignment.phy infile
srun dnapars < dnapars_answers.txt > screen.log
```

Submit the job with `sbatch phylip_job.sh`.

## More information

* [PHYLIP home page](https://phylipweb.github.io/phylip/)
* [PHYLIP documentation](https://phylipweb.github.io/phylip/doc/main.html)
* [CSC Service Desk](../support/contact.md)
