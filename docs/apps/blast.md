---
tags:
  - Free
---

# BLAST

BLAST (Basic Local Alignment Search Tool) is the most frequently used sequence homology search tool. Given a query sequence (nucleotide or protein), BLAST compares it to a sequence database and picks out sequences with significant similarity to the probe sequence. BLAST uses a heuristic search protocol, which makes search very fast compared to non-heuristic methods. The heuristics used may however cause BLAST to fail to find all significant hits.

The command line version of NCBI-BLAST allows a user to modify all parameters of BLAST, to use special methods like PSI-BLAST and PHI-BLAST, and to analyze large data sets.

In Puhti you can use `pb` (Parallel Blast) command for large sets of query sequences. The `pb` program splits a large search jobs into several subjobs that are executed simultaneously (more below).

The most commonly used BLAST commands are:

* `blastn` search hits for a nucleotide sequence from nucleotide database
* `blastp` search hits for a protein sequence from protein database
* `blastx` search hits for a nucleotide sequence from protein database
* `psiblast` do iterative search for a protein sequence from protein database
* `rpsblast` search hits for a protein sequence from protein profile database
* `rpstblastn` search hits for a nucleotide sequence from protein profile database
* `tblastn` search hits for a protein sequence from nucleotide database
* `tblastx` search hits for a nucleotide sequence from nucleotide database by using the protein translations of both query and database sequences.

Other blast commands

* `blastdbcmd` retrieve a sequence or a set of sequences form BLAST databases
* `makeblastdb` create a new BLAST database
* `blast_formatter` reformat a BLAST archive formatted BLAST result file.

[TOC]

## License

Free to use and open source under [GNU LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

## Available

* Puhti: 2.15.0
* Chipster graphical user interface


## Usage

At CSC, BLAST searches can be executed in several ways:

* using the Chipster platform
* with normal BLAST commands in interactive batch jobs (`sinteractive -i`)
* as batch jobs with `pb` command in Puhti

## Interactive usage in Puhti

To use the latest BLAST version in Puhti first give command:

```bash
module load biokit
```

Then launch an interactive batch job session with command:

```bash
sinteractive -i
```

Reserve 8 GiB of memory for your interactive session.

After that you can start using the BLAST commands listed above. For example following command would search for sequence homologs from UniProt database for a protein sequence.

```bash
blastp -query proteinseq.fasta -db uniprot -out result.txt
```

You can use `-help` option to see what command line options are available for a certain BLAST command. For example 

```bash
blastp -help
```

For example, command:  

```bash
blastp -query proteinseq.fasta -evalue 0.001 -db uniprot -outfmt 7 -out result.table
```

Would run the same search as described above, except that the e-value threshold would be set to 0.001 (`-evalue 0.001`) and the output is printed out to a table (`-outfmt 7`).

## Usage of pb (Parallel BLAST) at CSC

If your query sequence set contains less than 20 sequences then interactive batch job is probably the most effective way top do the search. However, if your query set contains hundreds or thousands of sequences, then utilizing the parallel computing capacity of Puhti is more effective. For this kind of massive blast searches you can utilize the `pb` command.

`pb` (Parallel BLAST) is designed for situations where the query file includes large amount of sequences. It splits the query task into several subjobs that can be run simultaneously using the resources of the server very effectively. For large sets of query sequences, `pb` can speed up the search up to 50-fold. Two sample `pb` commands for Puhti:

```bash
module load biokit
pb blastn -db nt -query 100_ests.fasta -out results.out
pb psiblast -db swiss -query protseqs.fasta -num_iterations 3 -out results.out
```

`pb blast` commands can be executed interactively in the login nodes of Puhti. You don't need to create any batch job file yourself. Instead, `pb` command creates and submits a batch job automatically. Once BLAST job is started, `pb` starts a process that monitors the progress of the blast job. As running a large BLAST job may take a long time, you may need to close the monitoring. You can do that by pressing `Ctrl-c`. After that you can start other tasks or log out from Puhti. The BLAST jobs will still continue running in the batch job system. 

To reconnect to your `pb blast` job, go to your scratch directory and run command:

```bash
blast_clusterrun
```

This lists the temporary directories of your unfinished `pb blast` jobs. You can check the job number of your blast job from the directory name. Use this number with `-jobid` option to define the `pb blast` job you wish to reconnect to.

```bash
blast_clusterrun -jobid some-number
```

## Using own BLAST databases with pb

The `pb` program also allows users to do BLAST searches against their own fasta formatted sequence sets. This is done by replacing the `-db` option with option `-dbnuc` (for nucleotides) or `-dbprot` (for proteins). Example:

```bash
pb blastn -dbnuc my_seq_set.fasta -query querys.fasta -out results.out
```

If your database is big, building the BLAST indexes may require more than 1 GB of memory (that is the job specific memory limit in Puhti login nodes). In those cases you can submit the job from an interactive batch job (with e.g. 8 GB of memory).

## Using taxonomy to focus the search

The general purpose NCBI BLAST databases like _NT_ or _NE_ have grown very large, which slows the searches in Puhti. Thus, if you can focus your search to only a subset of these databases it makes the search faster and prevents non-important hits to be reported.

Starting with BLAST+ 2.15.0, the BLAST+ command line applications support
a new feature: they accept non-leaf taxIDs (i.e., those above an organism level,
such as the one for primates). For example to focus the search to only bird sequences 
(Taxonomy ID: 8782) of NR database you could use command

```bash
pb blastp -db nr - query test.fasta -taxids 8782 -out test.res
```

If you know that you will use a specific subset of _NR_ or _NT_ databases several times, it is more effective
to filter this part of sequences out once and then index your own database form the filtered sequences. You can use command `blastdbcmd` to filter out a specific taxonomic group from _NR_ or _NT_ databases.

For example all bird sequences can be retrieved from _NR_ database with command:

```bash
blastdbcmd -taxids 8782 -db nr -dbtype prot -out nrbirds.fasta -target_only
```

The resulting fasta file can be indexed for BLAST searches with `makeblastdb` command.

```bash
makeblastdb -in nrbirds.fasta -dbtype prot
```

To use your own database, you must redefine environment variable `BLASTDB` so that it points to the directory where you have the index. For example if the indexes locate in directory `my_blastdb` in the scratch directory of project `project_20012345`, the variable would be set with command:

```bash
export BLASTDB=/scrartch/project_20012345/my_blastdb
```

Now you can use your own database in the BLAST search:

```bash
pb blastp -db nrbirds.fasta - queryquery.fasta -out bird-only-hits.res
```

## Using genome data from Ensembl with pb

`pb` command can also automatically retrieve a species specific dataset from the Ensembl or Ensembl genomes servers and use the dataset as the search database. This is done by replacing the `-db` option with option `-ensembl_dna` (retrieves the genomic DNA), `-ensembl_cdna` (retrieves the cDNA sequences) or `-ensembl_prot` (retrieves the protein sequences). The latin name of a species or taxonomy index number is given as an argument for the Ensembl options. You should use underscore (`_`) instead of space in the species name.

For example to compare a set of nucleotide sequences against the human genome, you could use a command like:

```bash
pb blastn -query dna_fargments.fasta -ensembl_dna homo_sapiens -out human_hits.txt
```

To compare the same DNA fragments against the protein sequences, predicted from the chicken genome, you could use command:

```bash
pb tblastn -query dna_fargments.fasta -ensembl_prot gallus_gallus -out chicken_hits.txt
```

You can see the list of species, available at Ensembl and Ensembl genomes databases with command:

```bash
ensemblfetch.sh -names
```

Below is a list of BLAST databases maintained at the servers of CSC.

| **Name          | Database                                             | Source file**                                               |
|-----------------|------------------------------------------------------|-------------------------------------------------------------|
| **Nucleotides** |                                                                                               |
| nt              | NCBI non-redundant nucleotide database               | ftp://ftp.ncbi.nih.gov/blast/db/FASTA/                      |
| refseq          | NCBI RefSeq RNA database                             | ftp://ftp.ncbi.nih.gov/refseq/release/complete/             |
| refseq_con      | NCBI RefSeq human contigs                            | ftp://ftp.ncbi.nih.gov/refseq/H_sapiens/H_sapiens/          |
|                 |                                                      |                                                             |
| **Proteins**    |                                                      |                                                             |
| nr              | NCBI non-redundant protein database                  | ftp://ftp.ncbi.nih.gov/blast/db/FASTA/                      |
| pdb_v5          | PDB protein structure database                       | ftp://ftp.rcsb.org/pub/pdb/derived_data/                    |
| swiss           | Uniprot/Swiss database                               | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/    |
| trembl          | Uniprot/TrEMBL database                              | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/    |
| uniprot         | Uniprot Swiss and TrEMBL                             |   |
| uniref100       | Uniref100 database                                   | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref100/ |
| uniref90        | UniRef90 database                                    | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref90/  |
| uniref50        | UniRef50 database                                    | ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref50/  |
| **Ensembl genomes** | Select one of the species with `pb` options: `-ensembl_dna`, `-ensembl_cdna` or `-ensembl_pep` | ftp://ftp.ensembl.org/   |

## Support

[Contact CSC Service Desk](../support/contact.md) for technical support.

## More information

More information on Blast can be found from the [BLAST page of NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi).
