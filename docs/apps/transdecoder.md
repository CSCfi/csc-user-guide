---
tags:
  - Free
catalog:
  name: TransDecoder
  description: Identification of candidate coding regions in transcript sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# TransDecoder

TransDecoder finds candidate coding regions in transcript sequences, such as
transcripts assembled de novo with [Trinity](trinity.md) or from RNA-seq alignments
to a genome. It predicts the protein sequences of the transcripts, which you can then
annotate with [Trinotate](trinotate.md).

[TOC]

## License

Free to use and open source under the [BSD 3-Clause License](https://github.com/TransDecoder/TransDecoder/blob/master/LICENSE.txt).

## Available

* Roihu-CPU: 5.7.1, via the `bio-apps` module.

## Usage

TransDecoder is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the TransDecoder module:

```bash
module load bio-apps/v202603
module load transdecoder/5.7.1
```

TransDecoder runs in two steps. First, find the long open reading frames (ORFs) in
the transcripts. Then, predict which of them are likely coding regions:

```bash
TransDecoder.LongOrfs -t transcripts.fasta
TransDecoder.Predict -t transcripts.fasta
```

The predicted proteins are written to `transcripts.fasta.transdecoder.pep`, their
coding sequences to `transcripts.fasta.transdecoder.cds`, and their locations to
`transcripts.fasta.transdecoder.gff3` and `.bed`. By default, ORFs must be at least
100 amino acids long (`-m`). For strand-specific data, add `-S` to
`TransDecoder.LongOrfs` to search only the top strand of the transcripts.

To keep ORFs that have Pfam domain or BLAST hits even if they would otherwise be
left out, give the search results to `TransDecoder.Predict` with `--retain_pfam_hits`
and `--retain_blastp_hits`. See the
[TransDecoder documentation](https://github.com/TransDecoder/TransDecoder/wiki) for
details.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=transdecoder
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load transdecoder/5.7.1

TransDecoder.LongOrfs -t transcripts.fasta
TransDecoder.Predict -t transcripts.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [TransDecoder documentation](https://github.com/TransDecoder/TransDecoder/wiki)
* [TransDecoder GitHub repository](https://github.com/TransDecoder/TransDecoder)
