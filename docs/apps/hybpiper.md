---
tags:
  - Free
catalog:
  name: HybPiper
  description: Target-capture (Hyb-Seq) locus recovery for phylogenomics
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HybPiper

HybPiper was designed for targeted sequence capture (Hyb-Seq), in which DNA sequences of
interest are enriched from genomic libraries. It recovers the target coding sequences
(and optionally flanking regions) from high-throughput sequencing reads, for use in
phylogenomics.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/mossmatters/HybPiper/blob/master/LICENSE.txt).

## Available

* Roihu: 2.3.4, via the `bio-apps` module.

## Usage

HybPiper is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HybPiper module:

```bash
module load bio-apps/v202603
module load hybpiper/2.3.4
```

For a single sample, assemble the target loci from paired-end reads:

```bash
hybpiper assemble -t_dna target_file.fasta -r sample_R1.fastq sample_R2.fastq --prefix sample --cpu 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=hybpiper
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
module load hybpiper/2.3.4

hybpiper assemble -t_dna target_file.fasta -r sample_R1.fastq sample_R2.fastq \
    --prefix sample --cpu $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [HybPiper GitHub repository](https://github.com/mossmatters/HybPiper)
* [HybPiper wiki](https://github.com/mossmatters/HybPiper/wiki)
