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


## Available

-   Puhti: 2.9.0
-   FGCI: 2.6.0
-   Chipster graphical user interface


## Usage
At CSC, BLAST searches can be executed in several ways:

-    using  the Chipster platform
-    interavtively with normal BLAST commans in Taito-shell
-    as batch jobs with pb command in Puhti
-    in FGCI grid with gb command in Taito

To use the latest BLAST in Taito first give set up command :
```text
module load biokit
```
After that you can start using the BLAST commands listed above. For example following command would search for sequence homologs form UniProt database for a protein sequence.
```text
blastp -query proteinseq.fasta -db uniprot -out result.txt
```
You can use -help option to see, what command line options are available for a certain BLAST command. For example 
```text
blastp -help
```
For example, command:  
```text
blastp -query proteinseq.fasta -evalue 0.001 -db uniprot -outfmt 7 -out result.table
```
Would run the same search as described above, except that the  e-value threshold would be set to 0.001(-evalue 0.001) and the out put is printed out a a table (-outfmt 7).

##Usage of pb (Parallel BLAST)  at CSC

If your query sequence set contains less than 20 sequences then Taito-shell is probable the most effective platforms for the search. However, if your query set contains hundreds or thousands of sequences then utilizing the taito.csc.fi cluster is more  effective. For this kind of massive blast searches you can utilize the `pb` command in Puhti. _pb_ (Parallel BLAST) is designed for situations, where the query file includes large amount of sequences. It splits the query task into several subjobs, that can be run simultaneously using the resources of the server very effectively. For large sets of query sequences, _pb: can speed up the search up to 50 fold. Two sample _pb_ commands for puhti.csc.fi:
```text
module load biokit

pb blastn -db nt -query 100_ests.fasta -out results.out

pb psiblast -db swiss -query protseqs.fasta -num_iterations 3 -out results.out
```
##Using own BLAST databases with pb

The pb program also allows users to do BLAST searches against their own fasta formatted sequence sets. This is done by replacing the `-db` option with option `-dbnuc` (for nucleotides) or `-dbprot` (for proteins). Example:
```text
pb blastn -dbnuc my_seq_set.fasta -query querys.fasta -out results.out
```
##Using genome data from ensembl with pb

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
ensemblfetch -names
```
<p>Below is a list of BLAST databases maintained at the servers of CSC.</p>

<table>
	<tbody>
		<tr>
			<td style="background-color: rgb(204, 204, 255);"><strong>Name</strong></td>
			<td style="background-color: rgb(204, 204, 255);"><strong>Database</strong></td>
			<td style="background-color: rgb(204, 204, 255);"><strong>Source file</strong></td>
		</tr>
		<tr>
			<td><strong>Nucleotides</strong></td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>nt</td>
			<td>NCBI non-redundant nucleotide database</td>
			<td>ftp://ftp.ncbi.nih.gov/blast/db/FASTA/</td>
		</tr>
		<tr>
			<td>refseq</td>
			<td>NCBI RefSeq RNA database</td>
			<td>ftp://ftp.ncbi.nih.gov/refseq/release/complete/</td>
		</tr>
		<tr>
			<td>refseq_con</td>
			<td>NCBI RefSeq human contigs</td>
			<td>ftp://ftp.ncbi.nih.gov/refseq/H_sapiens/H_sapiens/</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td><strong>Proteins</strong></td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>nr</td>
			<td>NCBI non-redundant protein database</td>
			<td>ftp://ftp.ncbi.nih.gov/blast/db/FASTA/</td>
		</tr>
		<tr>
			<td>pdb</td>
			<td>PDB protein structure database</td>
			<td>ftp://ftp.rcsb.org/pub/pdb/derived_data/</td>
		</tr>
		<tr>
			<td>swiss</td>
			<td>Uniprot/Swiss database</td>
			<td>ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/</td>
		</tr>
		<tr>
			<td>trembl</td>
			<td>Uniprot/TrEMBL database</td>
			<td>ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/</td>
		</tr>
		<tr>
			<td>uniref100</td>
			<td>Uniref100 database</td>
			<td>ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref100/</td>
		</tr>
		<tr>
			<td>uniref90</td>
			<td>UniRef90 database</td>
			<td>ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref90/</td>
		</tr>
		<tr>
			<td>uniref50</td>
			<td>UniRef50 database</td>
			<td>ftp://ftp.ebi.ac.uk/pub/databases/uniprot/uniref/uniref50/</td>
		</tr>
		<tr>
			<td><strong>Ensembl genomes</strong></td>
			<td>Select one of the species&nbsp; with pb options: -ensembl_dna, -ensembl_cdna or -ensembl_pep</td>
			<td>ftp://ftp.ensembl.org/</td>
		</tr>
	</tbody>
</table>

## Support

servicedesk@csc.fi

## Manual

More information about Blast can be found from the [BLAST page of NCBI](https://blast.ncbi.nlm.nih.gov/Blast.cgi)

