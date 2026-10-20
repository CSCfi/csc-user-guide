---
tags:
  - Free
catalog:
  name: MAGScoT
  description: Scoring and refinement of metagenomic bins from several binning tools
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MAGScoT

MAGScoT (MAG Scoring Tool) scores and refines metagenome-assembled genomes (MAGs)
from several binning tools. It estimates the completeness and contamination of
each bin from GTDB (release 207) single-copy marker genes, merges overlapping bins
from different tools, and selects the best set of non-overlapping bins.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/ikmb/MAGScoT/blob/main/LICENSE).

## Available

* Roihu-CPU: 1.1, via the `bio-apps` module.

## Usage

MAGScoT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MAGScoT module:

```bash
module load bio-apps/v202603
module load magscot/1.1
```

MAGScoT is an R script. The module sets `$MAGSCOT_INSTROOT` to the installation
directory, which contains the script and, under `hmm`, the GTDB marker gene
profiles. The module also loads Prodigal and HMMER.

Find the marker genes in the contigs: predict the genes with Prodigal, search them
for markers with HMMER and combine the hits into one table:

```bash
prodigal -p meta -i contigs.fa -a contigs.faa -o contigs.genes
hmmsearch -o tigr.out --tblout tigr.hits --noali --notextw --cut_nc --cpu 8 \
  $MAGSCOT_INSTROOT/hmm/gtdbtk_rel207_tigrfam.hmm contigs.faa
hmmsearch -o pfam.out --tblout pfam.hits --noali --notextw --cut_nc --cpu 8 \
  $MAGSCOT_INSTROOT/hmm/gtdbtk_rel207_Pfam-A.hmm contigs.faa
grep -v "^#" tigr.hits | awk '{print $1"\t"$3"\t"$5}' > contigs.hmm
grep -v "^#" pfam.hits | awk '{print $1"\t"$4"\t"$5}' >> contigs.hmm
```

MAGScoT reads the bins from a tab-separated file with three columns and no
header: bin, contig and binning tool. For example, to combine the bins from
[SemiBin2](semibin.md), [COMEBin](comebin.md) and [CONCOCT](concoct.md):

```bash
awk -F'\t' 'NR>1{print "semibin_"$2"\t"$1"\tsemibin2"}' semibin_out/contig_bins.tsv > contigs_to_bin.tsv
awk -F'\t' '{print "comebin_"$2"\t"$1"\tcomebin"}' comebin_out/comebin_res/comebin_res.tsv >> contigs_to_bin.tsv
awk -F',' 'NR>1{print "concoct_"$2"\t"$1"\tconcoct"}' concoct_output/clustering_merged.csv >> contigs_to_bin.tsv
```

Score and refine the bins:

```bash
Rscript $MAGSCOT_INSTROOT/MAGScoT.R -i contigs_to_bin.tsv --hmm contigs.hmm
```

MAGScoT writes the scores of the original bins to `MAGScoT.scores.out`, and the
refined bins and their contigs to `MAGScoT.refined.out` and
`MAGScoT.refined.contig_to_bin.out`. Change the `MAGScoT` prefix with `-o`. With
bins from only one binning tool, MAGScoT only scores them.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=magscot
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load magscot/1.1

prodigal -p meta -i contigs.fa -a contigs.faa -o contigs.genes
hmmsearch -o tigr.out --tblout tigr.hits --noali --notextw --cut_nc --cpu $SLURM_CPUS_PER_TASK \
  $MAGSCOT_INSTROOT/hmm/gtdbtk_rel207_tigrfam.hmm contigs.faa
hmmsearch -o pfam.out --tblout pfam.hits --noali --notextw --cut_nc --cpu $SLURM_CPUS_PER_TASK \
  $MAGSCOT_INSTROOT/hmm/gtdbtk_rel207_Pfam-A.hmm contigs.faa
grep -v "^#" tigr.hits | awk '{print $1"\t"$3"\t"$5}' > contigs.hmm
grep -v "^#" pfam.hits | awk '{print $1"\t"$4"\t"$5}' >> contigs.hmm

Rscript $MAGSCOT_INSTROOT/MAGScoT.R -i contigs_to_bin.tsv --hmm contigs.hmm
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MAGScoT GitHub repository](https://github.com/ikmb/MAGScoT)
