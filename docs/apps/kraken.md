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

* Roihu-CPU: 2.17.1, 2.17.2 (module `kraken2`), via the `bio-apps` module.

## Usage

Kraken 2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Kraken 2 module:

```bash
module load bio-apps/v202603
module load kraken2/2.17.2
```

This loads the Kraken 2 package, which can be started with the command `kraken2`. For example:

```bash
kraken2 --help
```

### Databases

Kraken 2 needs a reference database (`--db`). CSC provides the following prebuilt
databases from the [Kraken 2 index collection](https://benlangmead.github.io/aws-indexes/k2)
in `/dataset/project_2020345/kraken2`:

| Database | Contents | Index size |
|----------|----------|------------|
| `k2_pluspf_20260226` | PlusPF (February 2026): RefSeq archaea, bacteria, viral, plasmid, protozoa and fungi, plus human and UniVec_Core | 103 GB |
| `k2_NCBI_reference_20251007` | One reference assembly per species for NCBI bacteria, archaea, protists and fungi (October 2025), plus human, RefSeq viral and UniVec_Core | 466 GiB |

The `kraken2` module sets `KRAKEN2_DB_PATH` to this directory, so you can give the
database by name:

```bash
kraken2 --db k2_pluspf_20260226 --threads $SLURM_CPUS_PER_TASK input.fasta --output results.txt
```

Kraken 2 loads the whole index into memory, so reserve at least the index size in memory for your job.
For example, a job using `k2_NCBI_reference_20251007` needs about `--mem=500G`. Jobs of this size
fit in the `small` partition, which allows up to 1500 GB of memory on its large-memory nodes.

To use another database, build your own with `kraken2-build` in a writable location (for example your project's `/scratch`). This downloads reference data and requires substantial disk space, memory and time:

```bash
kraken2-build --standard --db /scratch/<project>/kraken_db
```

Alternatively, you can download a prebuilt Kraken 2 index and give the full path of the directory where you unpacked it in `--db`.

### Example batch script

Both prebuilt databases need more memory than an interactive session allows, so run Kraken 2 with them as a batch job. Below is a sample job that classifies sequences against the PlusPF database using 8 cores, 120 GB of memory and 6 hours of runtime:

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
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=15G

module load bio-apps/v202603
module load kraken2/2.17.2

kraken2 --db k2_pluspf_20260226 --threads $SLURM_CPUS_PER_TASK --report sample.kreport --output results.txt input.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`). To use your own database, give its full path in `--db`.

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Kraken home page](https://ccb.jhu.edu/software/kraken2/)
