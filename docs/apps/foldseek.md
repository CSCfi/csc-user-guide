---
tags:
  - Free
catalog:
  name: Foldseek
  description: Fast protein structure search and clustering
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Foldseek

Foldseek enables fast and sensitive comparisons of large sets of protein structures.
It describes structures with a structural alphabet (3Di) and searches and clusters
them with MMseqs2-based algorithms. On Roihu it is provided as a GPU-accelerated
build for the GH200 GPU nodes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/steineggerlab/foldseek/blob/master/LICENSE.md).

## Available

* Roihu-GPU: 10-941cd33, via the `bio-apps` module.

Foldseek runs on the Roihu GPU (GH200) nodes. Log in to `roihu-gpu.csc.fi` and load the
modules there so you get the GPU build.

## Usage

Foldseek is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Foldseek module:

```bash
module load bio-apps/v202603
module load foldseek/10-941cd33
```

Search a set of query structures (PDB or mmCIF files) against a set of target
structures:

```bash
foldseek easy-search queries/ targets/ results.m8 tmp
```

Cluster a set of structures:

```bash
foldseek easy-cluster structures/ clusters tmp -c 0.9
```

### Databases

CSC provides shared, prebuilt Foldseek databases on Roihu, and the `foldseek`
module sets the environment variable `$FOLDSEEK_DB` to their location (under
`/dataset/project_2020345/foldseek`). Give the path to a database as the search
target:

| Database | Source (`foldseek databases` name) | Padded copy for GPU search |
|----------|------------------------------------|----------------------------|
| `afdb` | Alphafold/UniProt | `afdb_pad` |
| `afdb50` | Alphafold/UniProt50 | `afdb50_pad` |
| `afdb_proteome` | Alphafold/Proteome | `afdb_proteome_pad` |
| `afdb_swissprot` | Alphafold/Swiss-Prot | `afdb_swissprot_pad` |
| `esmatlas30` | ESMAtlas30 | `esmatlas30_pad` |
| `pdb` | PDB | `pdb_pad` |
| `cath50` | CATH50 | `cath50_pad` |
| `bfmd` | BFMD | `bfmd_pad` |
| `bfvd` | BFVD | `bfvd_pad` |

```bash
foldseek easy-search queries/ $FOLDSEEK_DB/pdb results.m8 tmp
```

The [ProstT5](https://github.com/mheinzinger/ProstT5) model is also provided, so you
can search with amino acid sequences (FASTA) instead of structures:

```bash
foldseek easy-search queries.fasta $FOLDSEEK_DB/pdb results.m8 tmp --prostt5-model $FOLDSEEK_DB/prostt5
```

To use another database, `foldseek databases` downloads prebuilt databases. Run it
without arguments to list all available databases. Download large databases to
your project's `/scratch`:

```bash
foldseek databases <name> /scratch/<project>/<database> tmp
```

### GPU-accelerated search

Add `--gpu 1` to run a search on the GPU. A GPU search needs a padded target
database. Use the padded copies of the shared databases (names ending in `_pad`):

```bash
foldseek easy-search queries/ $FOLDSEEK_DB/afdb_swissprot_pad results.m8 tmp --gpu 1 --prefilter-mode 1
```

For your own databases, make a padded copy with `makepaddedseqdb`:

```bash
foldseek makepaddedseqdb mydb mydb_pad
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=foldseek
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=gpumedium
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=72
#SBATCH --gres=gpu:gh200:1

module load bio-apps/v202603
module load foldseek/10-941cd33

foldseek easy-search queries/ $FOLDSEEK_DB/afdb_swissprot_pad results.m8 tmp --gpu 1 --prefilter-mode 1 \
  --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`). See
[creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md)
for more about batch jobs, and the
[GPU partitions](../computing/running/batch-job-partitions.md) for the available GPU
resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Foldseek GitHub repository](https://github.com/steineggerlab/foldseek)
* [Foldseek web server](https://search.foldseek.com)
