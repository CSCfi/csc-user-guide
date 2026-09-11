---
tags:
  - Free
catalog:
  name: HUMAnN
  description: Profiling microbial pathways with metagenomic data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HUMAnN

HUMAnN is a pipeline for efficiently and accurately profiling the presence/absence and abundance of 
microbial pathways in a community from metagenomic or metatranscriptomic sequencing data. 
This process (functional profiling) aims to describe the metabolic potential of a microbial community and its members. 

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/biobakery/humann/master/LICENSE).

## Available

* Roihu: 4.0.0a2 (a HUMAnN 4.0 alpha release), via the `bio-apps` module.

## Usage

HUMAnN is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HUMAnN module:

```bash
module load bio-apps/v202603
module load humann/4.0.0a2
```

You can then run HUMAnN:

```bash
humann --help
```

### Databases

HUMAnN's reference databases (ChocoPhlAn and UniRef) are several gigabytes and are
**not** bundled with the module. HUMAnN also uses [MetaPhlAn](metaphlan.md) for
taxonomic prescreening, which needs its own database.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download and use your own
    copies as shown below.

HUMAnN stores its database paths in a configuration file (`humann.cfg`) inside the
module's installation directory. On Roihu this installation is **read-only**, so
`humann_config` and the default config update of `humann_databases` cannot save
paths there. Instead, download the databases to a writable location (for example
your project's `/scratch` directory) with `--update-config no`, and point HUMAnN at
them on the command line for each run.

```bash
humann_databases --download chocophlan full /scratch/<project>/humann_db --update-config no
humann_databases --download uniref uniref90_diamond /scratch/<project>/humann_db --update-config no
```

### Running HUMAnN

HUMAnN can utilize several CPU cores. Set `--cpus-per-task` to the desired number
and pass `--threads $SLURM_CPUS_PER_TASK` to HUMAnN so it matches the requested
number of cores. Point HUMAnN at your downloaded databases with `--nucleotide-database`
and `--protein-database` (and MetaPhlAn's database via `--metaphlan-options`).

Example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=humann
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=2000M

module load bio-apps/v202603
module load humann/4.0.0a2

DB=/scratch/<project>/humann_db

# Download a test file
wget https://github.com/biobakery/humann/raw/master/examples/demo.fastq.gz

# Run HUMAnN, specifying the database locations on the command line
humann --threads $SLURM_CPUS_PER_TASK --input demo.fastq.gz \
    --nucleotide-database $DB/chocophlan \
    --protein-database $DB/uniref \
    --output demo_out
```

Replace `<project>` with your CSC project (for example `project_2001234`), and use
the same project in the database paths above.

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [HUMAnN home page](https://huttenhower.sph.harvard.edu/humann)
*   [HUMAnN user guide](https://github.com/biobakery/humann)
*   [HUMAnN tutorial](https://github.com/biobakery/biobakery/wiki/humann3)
