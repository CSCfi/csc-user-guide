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

* Roihu-CPU: 3.9 and 4.0.0a2 (a HUMAnN 4.0 alpha release), via the `bio-apps` module.

HUMAnN 3.9 is the current stable release. Use it unless you need HUMAnN 4.

## Usage

HUMAnN is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HUMAnN module:

```bash
module load bio-apps/v202603
module load humann/3.9
```

You can then run HUMAnN:

```bash
humann --help
```

### Databases

CSC provides the reference databases for both HUMAnN versions on Roihu, and the
module sets these environment variables to the databases of the loaded version:

| Variable | Database |
|----------|----------|
| `$HUMANN_NUC_DB` | ChocoPhlAn nucleotide database (`--nucleotide-database`) |
| `$HUMANN_PROT_DB` | UniRef protein database (`--protein-database`) |
| `$HUMANN_UTIL_DB` | Utility mapping files (`--utility-database` in HUMAnN 4, and `humann_regroup_table`) |

HUMAnN stores its database paths in a configuration file (`humann.cfg`) inside the
module's installation directory. On Roihu this installation is **read-only**, so
`humann_config` cannot change the paths. Instead, give the databases on the command
line for each run, as shown below.

HUMAnN also runs [MetaPhlAn](metaphlan.md) for taxonomic prescreening. The module
sets up the MetaPhlAn database that matches the HUMAnN version, so you do not need
to give it.

### Running HUMAnN

Download a small test file:

```bash
wget https://github.com/biobakery/humann/raw/master/examples/demo.fastq.gz
```

HUMAnN can use several CPU cores. Set `--cpus-per-task` to the number of cores and
pass `--threads $SLURM_CPUS_PER_TASK` to HUMAnN. Example batch job script:

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
module load humann/3.9

humann --threads $SLURM_CPUS_PER_TASK --input demo.fastq.gz \
    --nucleotide-database $HUMANN_NUC_DB \
    --protein-database $HUMANN_PROT_DB \
    --output demo_out
```

Replace `<project>` with your CSC project (for example `project_2001234`).

With HUMAnN 4.0.0a2, load `humann/4.0.0a2` and also add
`--utility-database $HUMANN_UTIL_DB`. HUMAnN 4 reads its pathway files from the
utility database.

The results are written to `demo_out`. HUMAnN 3.9 writes the gene family, pathway
abundance and pathway coverage tables to `demo_genefamilies.tsv`,
`demo_pathabundance.tsv` and `demo_pathcoverage.tsv`. HUMAnN 4 numbers its output
files, for example `demo_2_genefamilies.tsv` and `demo_4_pathabundance.tsv`.

To regroup the gene families, for example to KEGG orthologs, give the mapping file
from `$HUMANN_UTIL_DB` with `-c`. `humann_rename_table` adds the names of the groups:

```bash
humann_regroup_table -i demo_out/demo_genefamilies.tsv \
    -c $HUMANN_UTIL_DB/map_ko_uniref90.txt.gz -o demo_ko.tsv
humann_rename_table -i demo_ko.tsv -n kegg-orthology -o demo_ko_named.tsv
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [HUMAnN home page](https://huttenhower.sph.harvard.edu/humann)
*   [HUMAnN user guide](https://github.com/biobakery/humann)
*   [HUMAnN tutorial](https://github.com/biobakery/biobakery/wiki/humann3)
