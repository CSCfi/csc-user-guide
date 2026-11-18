---
tags:
  - Free
catalog:
  name: ClipKIT
  description: Trim multiple sequence alignments for phylogenetic analysis
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ClipKIT

ClipKIT trims multiple sequence alignments before phylogenetic analysis. Instead of
only removing poorly aligned sites, it keeps the sites that are informative for
building trees.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/JLSteenwyk/ClipKIT/blob/master/LICENSE.md).

## Available

* Roihu-CPU: 2.12.1 and 2.14.0 (module `py-clipkit`), via the `bio-apps` module.

## Usage

ClipKIT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the ClipKIT module:

```bash
module load bio-apps/v202603
module load py-clipkit/2.14.0
```

Trim an alignment with the default `smart-gap` mode:

```bash
clipkit alignment.fasta -o alignment.trimmed.fasta
```

Without `-o`, the output is written to the input file name with a `.clipkit` suffix.
Use `-m` to choose another trimming mode, for example `kpic-smart-gap`, which also
keeps only parsimony-informative and constant sites. Run `clipkit -h` to see all the
modes and options.

### Example batch script

Trimming one alignment takes only seconds. To trim many alignments, for example one
per gene, run them in a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=clipkit
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load py-clipkit/2.14.0

mkdir -p trimmed
for aln in alignments/*.fasta; do
    clipkit "$aln" -o trimmed/$(basename "$aln")
done
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ClipKIT documentation](https://jlsteenwyk.com/ClipKIT/)
* [ClipKIT GitHub repository](https://github.com/JLSteenwyk/ClipKIT)
* [Steenwyk, J.L. et al. (2020). ClipKIT: A multiple sequence alignment trimming software for accurate phylogenomic inference. PLOS Biology 18, e3001007](https://doi.org/10.1371/journal.pbio.3001007)
