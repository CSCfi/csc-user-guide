---
tags:
  - Free
catalog:
  name: BUSCO
  description: Genome/transcriptome completeness assessment via orthologs
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BUSCO

BUSCO (Benchmarking Universal Single-Copy Orthologs) assesses the completeness of
genome assemblies, gene sets and transcriptomes by searching for a set of orthologs
that are expected to be present as single-copy genes in a given lineage.

[TOC]

## License

Free to use and open source under the [MIT License](https://gitlab.com/ezlab/busco/-/blob/master/LICENSE).

## Available

* Roihu: 5.4.3, 6.1.0, via the `bio-apps` module.

## Usage

BUSCO is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BUSCO module:

```bash
module load bio-apps/v202603
module load busco/6.1.0
```

BUSCO is run with the `busco` command, specifying the input, the mode
(`genome`, `proteins` or `transcriptome`) and a lineage dataset:

```bash
busco -i genome.fa -m genome -l eukaryota_odb12 -o result -c 8
```

### Lineage datasets

BUSCO downloads the required lineage datasets automatically into a `busco_downloads`
directory in your working directory. Run BUSCO from your project's `/scratch` directory
so there is space for these datasets.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, let BUSCO download the lineage
    datasets to a writable location, or download them yourself with
    `busco --download <lineage>`.

### Augustus gene predictor

If you run BUSCO with the Augustus gene predictor (`--augustus`), Augustus needs a
**writable** configuration directory, because it writes trained species parameters
there. The module provides a snapshot of this configuration via the `$CONFIG_TEMPLATE`
environment variable. Unpack it to a writable location and point
`AUGUSTUS_CONFIG_PATH` at it before running BUSCO:

```bash
tar -xzf $CONFIG_TEMPLATE -C /scratch/<project>/
export AUGUSTUS_CONFIG_PATH=/scratch/<project>/config
```

The default gene predictor (Metaeuk/Miniprot) does not require this step.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=busco
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load busco/6.1.0

busco -i genome.fa -m genome -l eukaryota_odb12 -o result -c $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BUSCO home page](https://busco.ezlab.org/)
* [BUSCO user guide](https://busco.ezlab.org/busco_userguide.html)
