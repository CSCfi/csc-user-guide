---
tags:
  - Free
catalog:
  name: eggNOG-mapper
  description: Functional annotation of sequences via orthology (eggNOG)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# eggNOG-mapper

eggNOG-mapper is a tool for fast functional annotation of novel sequences. It uses
precomputed orthologous groups and phylogenies from the eggNOG database to transfer
functional information from fine-grained orthologs.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/eggnogdb/eggnog-mapper/blob/master/LICENSE.txt).

## Available

* Roihu: 2.1.15, via the `bio-apps` module.

## Usage

eggNOG-mapper is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the eggNOG-mapper module:

```bash
module load bio-apps/v202603
module load eggnog-mapper/2.1.15
```

### Databases

eggNOG-mapper requires the eggNOG reference databases, which are **not** bundled with
the module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download your own copy to a
    writable location (for example your project's `/scratch`).

Download the databases with `download_eggnog_data.py` and point eggNOG-mapper at them
with `--data_dir` (or the `EGGNOG_DATA_DIR` environment variable):

```bash
download_eggnog_data.py -y --data_dir /scratch/<project>/eggnog_db
```

The `-y` flag in the above command can be included e.g. in scripts and batch jobs to skip a confirmation prompt before the download proceeds.

### Running eggNOG-mapper

eggNOG-mapper is run with the `emapper.py` command:

```bash
#!/bin/bash
#SBATCH --job-name=emapper
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
module load eggnog-mapper/2.1.15

emapper.py --cpu $SLURM_CPUS_PER_TASK \
    --data_dir /scratch/<project>/eggnog_db \
    -i proteins.fasta -o annotation
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [eggNOG-mapper GitHub repository](https://github.com/eggnogdb/eggnog-mapper)
* [eggNOG-mapper wiki](https://github.com/eggnogdb/eggnog-mapper/wiki)
