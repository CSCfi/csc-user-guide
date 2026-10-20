---
tags:
  - Free
catalog:
  name: CONCOCT
  description: Metagenomic binning using sequence composition and coverage
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# CONCOCT

CONCOCT bins metagenomic contigs into genomes using their sequence composition and
their coverage across several samples.

[TOC]

## License

Free to use and open source under the [BSD 2-Clause License](https://github.com/BinPro/CONCOCT/blob/develop/LICENSE.txt).

## Available

* Roihu-CPU: 1.1.0 (module `py-concoct`), via the `bio-apps` module.

## Usage

CONCOCT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the CONCOCT module:

```bash
module load bio-apps/v202603
module load py-concoct/1.1.0
```

CONCOCT needs the contigs, and sorted and indexed BAM files from mapping the reads
of each sample to the contigs. First cut the contigs into 10 kb pieces and compute
the coverage of each piece in each sample:

```bash
cut_up_fasta.py contigs.fa -c 10000 -o 0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed mapping/*.sorted.bam > coverage_table.tsv
```

Run CONCOCT, with `-t` giving the number of threads (the default is one thread):

```bash
concoct --composition_file contigs_10K.fa --coverage_file coverage_table.tsv \
  -b concoct_output/ -t 16
```

Merge the clustering of the pieces back to the original contigs, and write each
bin to a FASTA file:

```bash
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
mkdir concoct_output/fasta_bins
extract_fasta_bins.py contigs.fa concoct_output/clustering_merged.csv \
  --output_path concoct_output/fasta_bins
```

To combine the bins of CONCOCT with those of other binning tools, use
[MAGScoT](magscot.md).

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=concoct
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G

module load bio-apps/v202603
module load py-concoct/1.1.0

cut_up_fasta.py contigs.fa -c 10000 -o 0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed mapping/*.sorted.bam > coverage_table.tsv
concoct --composition_file contigs_10K.fa --coverage_file coverage_table.tsv \
  -b concoct_output/ -t $SLURM_CPUS_PER_TASK
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
mkdir concoct_output/fasta_bins
extract_fasta_bins.py contigs.fa concoct_output/clustering_merged.csv \
  --output_path concoct_output/fasta_bins
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [CONCOCT documentation](https://concoct.readthedocs.io/)
* [CONCOCT GitHub repository](https://github.com/BinPro/CONCOCT)
