---
tags:
  - Free
catalog:
  name: HTSeq
  description: Count reads per gene from high-throughput sequencing alignments
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HTSeq

HTSeq is a Python package for processing high-throughput sequencing data. Its most
used part is `htseq-count`, which counts how many aligned reads overlap each gene in
a GTF or GFF annotation. The resulting count tables are used as input for
differential expression analysis, for example with DESeq2.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/htseq/htseq/blob/main/LICENSE).

## Available

* Roihu-CPU: 2.0.3 and 2.1.2 (module `py-htseq`), via the `bio-apps` module.

## Usage

HTSeq is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the HTSeq module:

```bash
module load bio-apps/v202603
module load py-htseq/2.1.2
```

The module provides the `htseq-count`, `htseq-count-barcodes` and `htseq-qa`
commands, and the `HTSeq` Python library.

For example, count the reads of a position-sorted BAM file from an unstranded
library per gene:

```bash
htseq-count -s no -r pos -c counts.tsv sample.bam genes.gtf
```

Check these options before you run `htseq-count`:

* `-s`: strandedness of the library. The default is `yes`. Use `no` for unstranded
  libraries and `reverse` for reverse-stranded ones, such as dUTP-based kits. A wrong
  setting silently leaves many reads uncounted.
* `-r`: sort order of paired-end data. The default is `name`. Use `pos` for BAM files
  sorted by position, which is the default of `samtools sort`.
* `-t` and `-i`: the feature type to count (default `exon`) and the attribute that
  groups features into genes (default `gene_id`). The defaults suit Ensembl GTF files.

The counts are written to the file given with `-c`, or to standard output if you
leave it out. The last rows (`__no_feature`, `__ambiguous` and so on) show how many
reads were not counted and why.

### Example batch script

`htseq-count` can process several BAM files at once, one core per file, and writes
one count column per file. Set the number of processes with `-n`:

```bash
#!/bin/bash
#SBATCH --job-name=htseq
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

module load bio-apps/v202603
module load py-htseq/2.1.2

htseq-count -s no -r pos -n $SLURM_CPUS_PER_TASK -c counts.tsv \
    sample1.bam sample2.bam sample3.bam sample4.bam genes.gtf
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [HTSeq documentation](https://htseq.readthedocs.io/)
* [htseq-count documentation](https://htseq.readthedocs.io/en/latest/htseqcount.html)
* [HTSeq GitHub repository](https://github.com/htseq/htseq)
* [Putri, G. et al. (2022). Analysing high-throughput sequencing data in Python with HTSeq 2.0. Bioinformatics 38, 2943–2945](https://doi.org/10.1093/bioinformatics/btac166)
