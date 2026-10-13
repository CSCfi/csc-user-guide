---
tags:
  - Free
catalog:
  name: run_dbcan
  description: Automated carbohydrate-active enzyme (CAZyme) annotation
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# run_dbcan (dbCAN)

run_dbcan (dbCAN) is a standalone tool for automated annotation of carbohydrate-active
enzymes (CAZymes) in genomes and metagenomes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/bcb-unl/run_dbcan/blob/master/LICENSE).

## Available

* Roihu: 5.2.9 (module `py-dbcan`), via the `bio-apps` module.

## Usage

run_dbcan is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load py-dbcan/5.2.9
```

### Databases

CSC provides the dbCAN reference databases for run_dbcan 5.2.9, including the CGC
and PUL databases, on Roihu. The `py-dbcan` module sets the `DBCAN_DB` environment
variable to their location. Give it to run_dbcan with `--db_dir $DBCAN_DB`, as in the
example below.

### Running run_dbcan

```bash
#!/bin/bash
#SBATCH --job-name=run_dbcan
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
module load py-dbcan/5.2.9

run_dbcan CAZyme_annotation --input_raw_data proteins.faa --mode protein \
    --db_dir $DBCAN_DB --output_dir dbcan_out --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [run_dbcan GitHub repository](https://github.com/bcb-unl/run_dbcan)
* [run_dbcan documentation](https://dbcan.readthedocs.io/)
