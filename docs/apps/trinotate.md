---
tags:
  - Free
catalog:
  name: Trinotate
  description: Functional annotation of transcriptomes
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Trinotate

Trinotate is a suite for the functional annotation of transcriptomes, particularly
de novo assembled transcriptomes from [Trinity](trinity.md). It searches the
transcripts and their predicted proteins against SwissProt, Pfam and Rfam, and
collects the results into an SQLite database, from which it writes an annotation
report.

[TOC]

## License

Free to use and open source under the [BSD 3-Clause License](https://github.com/Trinotate/Trinotate/blob/master/LICENSE.txt).

## Available

* Roihu-CPU: 4.0.2, via the `bio-apps` module.

## Usage

Trinotate is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Trinotate module:

```bash
module load bio-apps/v202603
module load trinotate/4.0.2
```

The Trinotate module also loads [TransDecoder](transdecoder.md), which predicts the
proteins that Trinotate annotates.

### Databases

CSC provides the Trinotate reference data (SwissProt, Pfam and Rfam) on Roihu, and
the module sets `$TRINOTATE_DATA_DIR` to their location. Trinotate finds the data
through this variable, so you do not need to run `Trinotate --create` to download
them. Instead, start each annotation project from a copy of the empty Trinotate
database:

```bash
cp $TRINOTATE_DATA_DIR/TrinotateBoilerplate.sqlite myTrinotate.sqlite
```

### Annotating a Trinity assembly

Run the annotation in a directory of your own, for example in your project's
`/scratch`. First predict the proteins with TransDecoder:

```bash
TransDecoder.LongOrfs -t Trinity.fasta
TransDecoder.Predict -t Trinity.fasta
```

Load the transcripts and proteins into the database. The gene-to-transcript map
(`Trinity.fasta.gene_trans_map`) is written by Trinity next to the assembly:

```bash
Trinotate --db myTrinotate.sqlite --init \
    --gene_trans_map Trinity.fasta.gene_trans_map \
    --transcript_fasta Trinity.fasta \
    --transdecoder_pep Trinity.fasta.transdecoder.pep
```

Run the searches and load their results into the database:

```bash
Trinotate --db myTrinotate.sqlite --run ALL --CPU 16 \
    --transcript_fasta Trinity.fasta \
    --transdecoder_pep Trinity.fasta.transdecoder.pep
```

`--run ALL` runs the SwissProt BLAST searches of the transcripts and proteins, the
Pfam domain search and the Rfam search. SignalP and TMHMM are not available on
Roihu, so Trinotate skips them. If the job stops, run the same command again:
Trinotate skips the searches that have already finished.

Finally, write the annotation report:

```bash
Trinotate --db myTrinotate.sqlite --report > Trinotate_report.tsv
```

### Example batch script

The searches, especially the BLAST search of the transcripts, can take a long time
for a large transcriptome, so run them in a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=trinotate
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G

module load bio-apps/v202603
module load trinotate/4.0.2

Trinotate --db myTrinotate.sqlite --run ALL --CPU $SLURM_CPUS_PER_TASK \
    --transcript_fasta Trinity.fasta \
    --transdecoder_pep Trinity.fasta.transdecoder.pep
Trinotate --db myTrinotate.sqlite --report > Trinotate_report.tsv
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Trinotate documentation](https://github.com/Trinotate/Trinotate/wiki)
* [Trinotate GitHub repository](https://github.com/Trinotate/Trinotate)
