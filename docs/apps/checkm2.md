---
tags:
  - Free
catalog:
  name: CheckM2
  description: Genome quality assessment via machine learning
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# CheckM2

CheckM2 provides rapid assessment of genome bin quality using machine learning,
predicting the completeness and contamination of metagenome-assembled genomes (MAGs)
and other genomes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/chklovski/CheckM2/blob/main/LICENSE).

## Available

* Roihu: 1.1.0, via the `bio-apps` module.

## Usage

CheckM2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the CheckM2 module:

```bash
module load bio-apps/v202603
module load checkm2/1.1.0
```

### Database

CheckM2 needs a DIAMOND reference database (~3 GB), which is **not** bundled with the
module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download your own copy to a
    writable location (for example your project's `/scratch`).

Download the database with:

```bash
checkm2 database --download --path /scratch/<project>/checkm2_db
```

You can then point CheckM2 at it with `--database_path`, or set the `CHECKM2DB`
environment variable to the downloaded `.dmnd` file.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=checkm2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load checkm2/1.1.0

checkm2 predict --threads $SLURM_CPUS_PER_TASK \
    --database_path /scratch/<project>/checkm2_db/CheckM2_database/*.dmnd \
    --input bins/ --output-directory checkm2_out -x fa
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [CheckM2 GitHub repository](https://github.com/chklovski/CheckM2)
