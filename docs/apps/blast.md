# BLAST

BLAST (Basic Local Alignment Search Tool) is the most frequently used sequence homology search tool. Given a query sequence (nucleotide or protein), BLAST compares it to a sequence database and picks out sequences with significant similarity to the probe sequence. BLAST uses a heuristic search protocol, which makes search very fast compared to non-heuristic methods. The heuristics used may however cause BLAST to fail to find all significant hits.

The command line version of NCBI-BLAST allows a user to modify all parameters of BLAST, to use special methods like PSI-BLAST and PHI-BLAST, and to analyze large data sets.

In Puhti you can use `pb`(Parallel Blast) command for large sets of query sequences. The pb program splits a large search jobs into several subjobs, that are executed simultaneously (more below).


The most commonly used BLAST commands are:

*   **blastn** search hits for a nucleotide sequence from nucleotide database
*   **blastp** search hits for a protein sequence from protein database
*   **blastx** search hits for a nucleotide sequence from protein database
*   **psiblast** do iterative search for a protein sequence from protein database
*   **rpsblast** search hits for a protein sequence from protein profile database
*   **rpstblastn** search hits for a nucleotide sequence from protein profile database
*   **tblastn** search hits for a protein sequence from nucleotide database
*   **tblastx** search hits for a nucleotide sequence from nucleotide database by using the protein translations of both query and database sequences.

Other blast commands

*    **blastdbcmd** retrieve a sequence or a set of sequences form BLAST databases
*    **makeblastdb** create a new BLAST database
*    **blast_formatter** reformat a BLAST archive formatted BLAST result file.
[TOC]

## License

Free to use and open source under [GNU LGPLv2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

## Available

-   Puhti: 2.10.0
-   FGCI: 2.6.0
-   Chipster graphical user interface


## Usage
At CSC, BLAST searches can be executed in several ways:

-    using the Chipster platform
-    with normal BLAST commands in interctive batch jobs (`sinteractive -i`)
-    as batch jobs with `pb` command in Puhti

## Interactive usage in Puhti

To use the latest BLAST version in Puhti first give set up command :
```text
module load biokit
```
Then launch an interactive bactch job session with command:
```text
sinteractive -i
```
Reserve 8 GiB of memory, for your interactive session.

After that you can start using the BLAST commands listed above. For example following command would search for sequence homologs form UniProt database for a protein sequence.
```text
blastp -query proteinseq.fasta -db uniprot -out result.txt
```
You can use `-help` option to see, what command line options are available for a certain BLAST command. For example 
```text
blastp -help
```
For example, command:  
```text
blastp -query proteinseq.fasta -evalue 0.001 -db uniprot -outfmt 7 -out result.table
```
Would run the same search as described above, except that the  e-value threshold would be set to 0.001(-evalue 0.001) and the out put is printed out to a table (-outfmt 7).


## Usage of pb (Parallel BLAST) at CSC

If your query sequence set contains less than 20 sequences then interactive batch job is probably the most effective way top do the search. However, if your query set contains hundreds or thousands of sequences then utilizing the parallel computing capacity of Puhti is more effective. For this kind of massive blast searches you can utilize the `pb` command.

_pb_ (Parallel BLAST) is designed for situations, where the query file includes large amount of sequences. It splits the query task into several subjobs, that can be run simultaneously using the resources of the server very effectively. For large sets of query sequences, _pb_ can speed up the search up to 50 fold. Two sample _pb_ commands for puhti.csc.fi:
```text
module load biokit

pb blastn -db nt -query 100_ests.fasta -out results.out

pb psiblast -db swiss -query protseqs.fasta -num_iterations 3 -out results.out
```


_pb blast_ commands can be executed interactively in the login nodes of Puhti. You don't need to create  any batch job file yourself. In stead _pb_ command creates and submits a batch job automatically. Once BLAST job is started _pb_ starts a process that monitor the progress of the blast job. As running a large BLAST jobs may take a long time you may need close the monitoring. You can do that by pressing: _Ctrl-c_. After that you can start other tasks or log out from Puhti. The BLAST jobs will still continue running in the batch job system. 

To reconnect to your pb blast job, go to your scratch directory and run command:

```text
blast_clusterrun
```
This lists the temporary directories of your unfinished pb blast jobs. You can check the job number of your blast job from the directory name. Use this number with _-jobid_ option to define the pb blast job you wish to reconnect to.

```text
blast_clusterrun -jobid some-number
```

## Using own BLAST databases with pb

The pb program also allows users to do BLAST searches against their own fasta formatted sequence sets. This is done by replacing the `-db` option with option `-dbnuc` (for nucleotides) or `-dbprot` (for proteins). Example:
```text
pb blastn -dbnuc my_seq_set.fasta -query querys.fasta -out results.out
```
## Using taxonomy lists to focus the search

Since BLAST version 2.10.0, the BLAST database format has changed to version 5. This version supports using a single taxonomy ID number or list of taxonomies, to focus the search only to an organism based subset from the search database.

The BLAST tools include a command `get_species_taxids.sh` that can be used to generate taxidlists.
First you have to find the the higher lever TaxID number your wish to use. For example, the TaxID of _Betacoronavirus_ genius can be found with command:

```text
get_species_taxids.sh -n Betacoronavirus 
```
Then the TaxIDs of the spcies that belong to this genius (TaxID: 694002) can be retrieved with command:
```text
get_species_taxids.sh -t 694002 > b-coronaviruses.txt
```
The command above produces a file containing TaxID numbers of Betacoronaviruses. This file can the be used with the `-taxidlist` to define BLAST to do the search only against the sequences originating form the defined species. For example:

```text
pb blastp -db nr -query queryset.fasta -taxidlist b-coronaviruses.txt -out corona_results 
``` 

Note that `-taxidlist` can be used only with databases that include species information.


## Using genome data from ensembl with pb

_pb_ command can also automatically retrieve a species specific dataset from the Ensembl or Ensembl genomes servers and use the dataset as the search database. This is done by replacing the `-db` option with option `-ensembl_dna` (retrieves the genomic DNA),  `-ensenmbl_cdna` (retrieves the cDNA sequences)  or `-ensembl_prot` (retrieves the protein sequences). The latin name of a species or taxonomy index number is given as an argument for the ensembl options. You should use underscore (_) in stead of space in the species name.

For example to compare a set of nucleotide sequences against the human genome, you could use a command like:
```text
pb blastn -query dna_fargments.fasta -ensembl_dna homo_sapiens -out  human_hits.txt
```

To compare the same dna fragments against the protein sequences, predicted from the chicken genome, you could use command:
```text
pb tblastn -query dna_fargments.fasta -ensembl_prot gallus_gallus -out  chicken_hits.txt
```

You can see the list of species, available at Ensembl and Ensembl genomes databases with command:
```text
ensemblfetch.sh -names
```
## Running BLAST in FGCI grid with gb

**gb** (grid blast) will soon be available in Puhti.
<!-- *  [gb instructions](./grid_blast.md) -->

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
| **Ensembl genomes** | Select one of the species  with pb options: -ensembl_dna, -ensembl_cdna or -ensembl_pep | ftp://ftp.ensembl.org/   |

## Support

servicedesk@csc.fi

## Manual

More information on Blast can be found from the [BLAST page of NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
