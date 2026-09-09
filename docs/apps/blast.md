---
tags:
  - Free
catalog:
  name: BLAST
  description: Sequence similarity search tool for nucleotides and proteins
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BLAST

BLAST (Basic Local Alignment Search Tool) is the most frequently used sequence homology search tool. Given a query sequence (nucleotide or protein), BLAST compares it to a sequence database and picks out sequences with significant similarity to the probe sequence. BLAST uses a heuristic search protocol, which makes the search very fast compared to non-heuristic methods. The heuristics used may however cause BLAST to fail to find all significant hits.

The command line version of NCBI-BLAST (BLAST+) allows a user to modify all parameters of BLAST, to use special methods like PSI-BLAST and PHI-BLAST, and to analyze large data sets.

[TOC]

## License

Free to use and open source under [GNU LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

## Available

* Roihu-CPU: module `blast-plus`, via the `bio-apps` module (run `module avail` after loading `bio-apps` for the exact built version).

## Usage

BLAST+ is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BLAST module:

```bash
module load bio-apps/v202603
module load blast-plus
```

You can use the `-help` option to see the command line options for any BLAST
command, for example:

```bash
blastp -help
```

### BLAST commands

The most commonly used BLAST search commands are:

* `blastn` search hits for a nucleotide sequence from a nucleotide database
* `blastp` search hits for a protein sequence from a protein database
* `blastx` search hits for a nucleotide sequence from a protein database
* `psiblast` do iterative search for a protein sequence from a protein database
* `rpsblast` search hits for a protein sequence from a protein profile database
* `rpstblastn` search hits for a nucleotide sequence from a protein profile database
* `tblastn` search hits for a protein sequence from a nucleotide database
* `tblastx` search hits for a nucleotide sequence from a nucleotide database by using the protein translations of both query and database sequences.

Other useful commands:

* `blastdbcmd` retrieve a sequence or a set of sequences from BLAST databases
* `makeblastdb` create a new BLAST database
* `blast_formatter` reformat a BLAST archive formatted result file.

BLAST searches against the large shared databases are memory- and time-hungry, so
run them in an [interactive session](../computing/running/interactive-usage.md) or
a batch job rather than on a login node. For example, on the `interactive`
partition (each core gives 1.875 GB, up to 32 cores / 60 GB / 36 h):

```bash
sinteractive --account <project> --cores 8
module load bio-apps/v202603 blast-plus
blastp -query proteinseq.fasta -db nr -evalue 0.001 -outfmt 7 -out result.table
```

Large jobs that need more time or memory are better submitted to the `small`
partition as a batch job.

### Reference databases

CSC provides shared, ready-built BLAST databases on Roihu, and the `blast-plus`
module sets the environment variable `$BLASTDB` to their location
(`/dataset/project_2020345/blast`). You refer to a database by its **basename**
with `-db`, and BLAST resolves it under `$BLASTDB` automatically:

| Basename | Type | Database |
| --- | --- | --- |
| `core_nt` | nucleotide | NCBI Core nucleotide (the curated replacement for the old `nt`) |
| `nr` | protein | NCBI non-redundant protein |
| `uniref50.fasta` | protein | UniRef50 |

The taxonomy files (`taxdb.*`, `taxonomy4blast.sqlite3`) are staged alongside them,
so taxonomic names appear in the output and `-taxids` filtering works out of the box.

```bash
# nucleotide query vs. Core nucleotide
blastn -query nuc.fasta -db core_nt -out results.out

# protein query vs. nr
blastp -query proteinseq.fasta -db nr -out result.txt
```

### Using taxonomy to focus the search

The general-purpose databases like `core_nt` and `nr` are very large, so limiting a
search to a taxonomic subset makes it faster and keeps out irrelevant hits. BLAST+
accepts non-leaf taxIDs (i.e. above organism level, such as one for all primates).
For example, to focus a search on bird sequences (Taxonomy ID 8782) of `nr`:

```bash
blastp -query test.fasta -db nr -taxids 8782 -out test.res
```

If you will reuse a specific subset several times, it is more efficient to extract
it once and index your own database from it. Use `blastdbcmd` to pull a taxonomic
group out of `nr` or `core_nt`:

```bash
blastdbcmd -taxids 8782 -db nr -dbtype prot -out nrbirds.fasta -target_only
```

### Using your own database

Index your own FASTA sequence set with `makeblastdb`:

```bash
makeblastdb -in nrbirds.fasta -dbtype prot
```

To search against a database in your own directory, prepend it to `$BLASTDB` so
BLAST finds both your database and the shared ones:

```bash
export BLASTDB=/scratch/<project>/my_blastdb:$BLASTDB
blastp -query query.fasta -db nrbirds.fasta -out bird-only-hits.res
```

## Support

[Contact CSC Service Desk](../support/contact.md) for technical support.

## More information

More information on BLAST can be found on the [BLAST page of NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi).
