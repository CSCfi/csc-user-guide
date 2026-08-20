---
tags:
  - Free
catalog:
  name: BRAKER
  description: Automatic genome annotation pipeline for eukaryotes
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BRAKER

BRAKER is a pipeline for eukaryotic genome annotation. It combines GeneMark and
AUGUSTUS, optionally guided by RNA-Seq and/or protein evidence, to generate full
gene-structure annotations for novel genomes.

On Roihu, BRAKER is provided as **BRAKER4** (`braker4`, version 0.5.0-beta): a
complete re-implementation of the pipeline as a [Snakemake](https://snakemake.github.io/)
workflow that runs every underlying tool (GeneMark, AUGUSTUS, DIAMOND,
BUSCO/compleasm, RepeatMasker, …) inside Apptainer/Singularity **containers**.

## License

BRAKER is free and open source (MIT). Tools bundled in the BRAKER4 containers
carry their own licenses, including GeneMark, which is free for academic use.

## Available

* Roihu: `braker4` 0.5.0-beta, via the `bio-apps/v202603` module.

## How it works on Roihu

BRAKER4 runs as a Snakemake workflow that submits each step of the pipeline as its
own Slurm job and executes it inside a container. You control the workflow with the
`braker4` command; it pulls the container images on first use and orchestrates the
whole annotation.

* The `braker4` module provides Snakemake, the Slurm executor plugin, pandas, the
  BRAKER4 workflow, and a ready-made **Roihu Snakemake profile** at
  `$BRAKER4_HOME/profiles/roihu`.
* You run everything from a directory on **`/scratch`** (the workflow writes there;
  the module installation directory is read-only to jobs).
* Container images are downloaded once into a shared `/scratch` cache and reused.

## Before your first run

You need:

1. A **working directory on `/scratch`** for inputs, outputs, and the image cache.
2. A **`config.ini`** and a **`samples.csv`** in that working directory.

### config.ini

Copy the Roihu template and edit it:

```bash
module load bio-apps/v202603 braker4
cp $BRAKER4_HOME/config.ini.roihu config.ini
```

The template redirects the pipeline's download directories to `/scratch`
(required — their defaults point inside the read-only installation directory). At
minimum set, under `[paths]`:

```ini
[paths]
busco_download_path = /scratch/project_2012345/braker4_busco_downloads
```

`[SLURM_ARGS]` controls the per-rule Slurm resources (`cpus_per_task`,
`mem_of_node`, `max_runtime`); `[containers]` lists the container images
(left at their defaults, they are pulled automatically).

### samples.csv

One row per genome. The header (14 columns) and a minimal ab-initio (ES-mode)
example:

```csv
sample_name,genome,genome_masked,protein_fasta,bam_files,fastq_r1,fastq_r2,sra_ids,varus_genus,varus_species,isoseq_bam,isoseq_fastq,busco_lineage,reference_gtf
my_species,/scratch/project_2012345/genome.fa,/scratch/project_2012345/genome_masked.fa,,,,,,,,,,eukaryota_odb12,
```

`busco_lineage` is required. Add evidence by filling the relevant columns, e.g.
`protein_fasta` for protein evidence, `bam_files` (colon-separated) for RNA-Seq
alignments, or `isoseq_bam` for IsoSeq — BRAKER4 selects ES/EP/ET/ETP mode
automatically from the evidence you provide.

## Running BRAKER4

Run `braker4` pipeline from your `/scratch` working directory. It is
lightweight (it submits and waits); the actual computation runs in Slurm jobs it
launches through the Roihu profile.

```bash
module load bio-apps/v202603 braker4

cd /scratch/project_2012345/braker_run     # your working directory
cp $BRAKER4_HOME/config.ini.roihu config.ini      # edit busco_download_path etc.
# ... create samples.csv ...

# Fast, node-local cache for container image conversion:
export APPTAINER_CACHEDIR=$TMPDIR/apptainer

braker4 \
    --workflow-profile $BRAKER4_HOME/profiles/roihu \
    --default-resources slurm_account=project_2012345 slurm_partition=small \
    --singularity-prefix /scratch/project_2012345/braker4_sif
```

* Replace `project_2012345` with your own project.
* `--default-resources slurm_account=… slurm_partition=…` must list **both**
  values together (specifying `--default-resources` on the command line replaces
  the whole block from the profile).
* `--singularity-prefix` is the shared, persistent image store; it **must be on
  `/scratch`** so the compute nodes can read the images.
* Add `-n` for a dry run (builds the job plan without submitting anything) and
  `--rerun-incomplete` to resume an interrupted run.

For long or heavy annotations, run the main Snakemake process inside an
[interactive session](../computing/running/interactive-usage.md) instead of on a
login node.

## Resources and partitions

BRAKER4's rules are single-node jobs that request specific cores and memory, which
fits the Roihu **`small`** partition. The per-rule sizing comes from `config.ini [SLURM_ARGS]`
(defaults: 48 cores, 120 GB, 72 h); the profile supplies only the account and
partition. If the pipeline fails because a step needs more than 72 h, move that
run to `longrun` (10-day limit); if a step needs more than 1500 GiB, move it to
`hugemem` (up to 6037 GiB, but a 36 h limit — use `hugemem_longrun` if it needs both).

## More information

* [BRAKER4 home page](https://github.com/Gaius-Augustus/BRAKER4)
