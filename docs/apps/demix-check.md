---
tags:
  - Free
catalog:
  name: demix_check
  description: Check mSWEEP/mGEMS cluster assignments of demixed reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# demix_check

demix_check assesses the binned reads from an mSWEEP/mGEMS analysis, to help judge
whether reads assigned to a cluster really come from that cluster or from an
unrepresented one missing from the reference set. It compares Mash distances between
the binned reads and the reference isolates against the within- and between-cluster
distances of the references, and gives each cluster a confidence score from 1
(highest) to 4 (lowest).

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/harry-thorpe/demix_check/blob/main/LICENSE).

## Available

* Roihu-CPU: 1.0.20250120, via the `bio-apps` module.

## Usage

demix_check is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the demix_check module:

```bash
module load bio-apps/v202603
module load demix-check/1.0.20250120
```

The module also loads the tools the pipeline calls (themisto, mSWEEP, mGEMS, Mash
and seqtk). Run the pipeline with the `demix_check` command (`demix_check.py` also
works):

```bash
demix_check --help
```

demix_check has three modes: `--mode_setup` prepares a reference set, `--mode_check`
checks the results of an existing mGEMS analysis, and `--mode_run` runs
themisto, mSWEEP and mGEMS on a set of reads and then checks the results.

### Setting up a reference set

A reference set is a directory, named after the set, that contains a tab-separated
`ref_info.tsv` file with the columns `id`, `cluster` and `assembly` (path to the
isolate's assembly):

```text
id          cluster  assembly
isolate_1   SC1      path/to/isolate_1.fasta
isolate_2   SC1      path/to/isolate_2.fasta
isolate_3   SC2      path/to/isolate_3.fasta
```

Setup mode writes the themisto index, Mash sketches and cluster thresholds into the
reference directory, so it must be writable (for example under your project's
`/scratch`):

```bash
demix_check --mode_setup --ref ref_dir/Kpne --threads 8
```

### Checking or running mGEMS

To check an existing mGEMS analysis against the same reference set:

```bash
demix_check --mode_check --binned_reads_dir mGEMS_analysis/binned_reads \
  --msweep_abun mGEMS_analysis/msweep_abundances.txt \
  --out_dir output_dir --ref ref_dir/Kpne --threads 8
```

To run the whole mSWEEP/mGEMS pipeline on paired-end reads and then check the
results:

```bash
demix_check --mode_run --r1 reads_1.fastq.gz --r2 reads_2.fastq.gz \
  --out_dir output_dir --ref ref_dir/Kpne --threads 8
```

The cluster scores are written to `clu_score.tsv`. Add `--plots` to also produce
distance plots (`sample_plot.pdf`). See the
[demix_check README](https://github.com/harry-thorpe/demix_check#readme) for
hierarchical runs with several reference sets and for the score definitions.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=demix_check
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
module load demix-check/1.0.20250120

demix_check --mode_run --r1 reads_1.fastq.gz --r2 reads_2.fastq.gz \
  --out_dir output_dir --ref ref_dir/Kpne --threads $SLURM_CPUS_PER_TASK --plots
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [demix_check GitHub repository](https://github.com/harry-thorpe/demix_check)
* [mGEMS GitHub repository](https://github.com/PROBIC/mGEMS)
* [mSWEEP GitHub repository](https://github.com/PROBIC/mSWEEP)
