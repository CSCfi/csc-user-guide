---
tags:
  - Free
catalog:
  name: GTDB-Tk
  description: Taxonomic classification of bacterial and archaeal genomes using the GTDB
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GTDB-Tk

GTDB-Tk is a software toolkit for assigning objective taxonomic classifications to
bacterial and archaeal genomes, including metagenome-assembled genomes (MAGs) and
single-amplified genomes (SAGs). Classifications are based on the
[Genome Taxonomy Database (GTDB)](https://gtdb.ecogenomic.org/), and the
`classify_wf` workflow places query genomes into the GTDB reference tree using a
combination of gene calling (Prodigal), marker identification (HMMER, pplacer),
tree placement (FastTree) and average nucleotide identity screening (skani).

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/Ecogenomics/GTDBTk/blob/master/LICENSE).

## Available

* Roihu: 2.7.2, via the `bio-apps` module.

## Usage

GTDB-Tk is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the GTDB-Tk module:

```bash
module load bio-apps/v202603
module load py-gtdbtk/2.7.2
```

The classification commands are run through the `gtdbtk` command, for example
`gtdbtk classify_wf`.

### Reference data

GTDB-Tk needs the GTDB reference data package (~100 GiB), matched to the tool
version. On Roihu this data is **already provided** by CSC and the module sets the
`GTDBTK_DATA_PATH` environment variable for you — you do **not** need to download
or configure anything. GTDB-Tk 2.7.2 uses GTDB release **R232**.

You can check the path after loading the module with:

```bash
echo $GTDBTK_DATA_PATH
```

### Example batch script

`classify_wf` takes a directory of genome FASTA files as input. The default
divide-and-conquer classification needs roughly **140 GiB of memory** and benefits
from many cores (see the GTDB-Tk
[hardware requirements](https://ecogenomics.github.io/GTDBTk/installing/index.html#hardware-requirements)).

```bash
#!/bin/bash
#SBATCH --job-name=gtdbtk
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=160G

module load bio-apps/v202603
module load py-gtdbtk/2.7.2

gtdbtk classify_wf \
    --genome_dir genomes/ \
    --extension fa \
    --out_dir gtdbtk_out \
    --cpus $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

* `--extension` is the file extension of your input genomes (`fa`, `fasta`, `fna`, …).
* GTDB-Tk 2.7 screens query genomes against the GTDB representatives with skani
  automatically; there is no separate reference database to download or configure
  for this step.
* The `pplacer` step is the most memory-intensive. If a run runs out of memory, first
  add `--pplacer_cpus 1` (lower peak memory, slower), then try increasing your `--mem` request
  — the `small` partition can provide up to 1500 GiB. GTDB-Tk's `--scratch_dir` option, which spills
  pplacer's allocation to disk, is best avoided on Roihu: its backing file is roughly
  as large as the memory it saves (likely making it too big for `$TMPDIR`), and its random, 
  memory-mapped access pattern performs poorly on the Lustre `/scratch` filesystem.

Running `--full_tree` (placement into the complete, undecorated reference tree)
requires around **950 GiB of memory** and must be run on the
[`hugemem` partition](../computing/running/creating-job-scripts-roihu.md); the
default divide-and-conquer approach is recommended for almost all use.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md)
for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [GTDB-Tk GitHub repository](https://github.com/Ecogenomics/GTDBTk)
* [GTDB-Tk documentation](https://ecogenomics.github.io/GTDBTk/)
* [Genome Taxonomy Database (GTDB)](https://gtdb.ecogenomics.org/)
