---
tags:
  - Free
catalog:
  name: Kraken
  description: Taxonomic sequence classification system
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Kraken

Kraken is a sequence classifier that assigns taxonomic labels to DNA sequences. 
Kraken examines the k-mers within a query sequence and uses the information within 
those k-mers to query a database. That database maps k-mers to the lowest common ancestor 
of all genomes known to contain a given k-mer.

On Roihu, Kraken is provided as **Kraken 2** (module `kraken2`, command `kraken2`).

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/DerrickWood/kraken2/master/LICENSE).

## Available

* Roihu: 2.17.1 (module `kraken2`), via the `bio-apps` module.

## Usage

Kraken 2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Kraken 2 module:

```bash
module load bio-apps/v202603
module load kraken2/2.17.1
```

This loads the Kraken 2 package, which can be started with the command `kraken2`. For example:

```bash
kraken2 --help
```

### Databases

Kraken 2 needs a reference database, which it queries by directory path (`--db`). Reference databases are not bundled with the module.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download or build your own
    database in a writable location (for example your project's `/scratch`).

You can build a standard database with `kraken2-build` (this downloads reference data and requires substantial disk space, memory and time):

```bash
kraken2-build --standard --db /scratch/<project>/kraken_db
```

Alternatively, you can download a prebuilt Kraken 2 index and point `--db` at the directory where you unpacked it.

### Example batch script

Using Kraken 2 with a large reference database requires plenty of memory. For example, the standard database requires around 40 GB of memory. Thus, Kraken should in practice always be executed as a batch job. Below is a sample Kraken job using 4 cores, 40 GB of memory and 6 hours of runtime:

```bash
#!/bin/bash
#SBATCH --job-name=kraken2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=06:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=10000M

module load bio-apps/v202603
module load kraken2/2.17.1

kraken2 --db /scratch/<project>/kraken_db --threads $SLURM_CPUS_PER_TASK input.fasta --output results.txt
```

Replace `<project>` with your CSC project (for example `project_2001234`), and point `--db` at your database directory.

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Kraken home page](https://ccb.jhu.edu/software/kraken2/)
