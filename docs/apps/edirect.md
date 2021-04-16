# Entrez Direct

## Description

Edirect, or Entrez Direct,  is a tooltkit to retrieve sequences and other data from the NCBI sequence databases based on given query terms. 
The pacage consists of several commands:

Navigation functions support exploration within the Entrez databases:

*    **esearch** performs a new Entrez search using terms in indexed fields.
*    **elink** looks up neighbors (within a database) or links (between databases).
*    **efilter** filters or restricts the results of a previous query.

Records can be retrieved in specified formats or as document summaries:

*    **efetch** downloads records or reports in a designated format.

Desired fields from XML results can be extracted without writing a program:

*    **xtract** converts EDirect XML output into a table of data values.

Several additional functions are also provided:

*    **einfo** obtains information on indexed fields in an Entrez database.
*    **epost** uploads unique identifiers (UIDs) or sequence accession numbers.
*    **nquire** sends a URL request to a web page or CGI service

[TOC]

## License

Free to use for all users. [Public Domain notice](https://www.ncbi.nlm.nih.gov/books/NBK179288/#chapter6.Appendices)

## Usage

The _edirect_ commands listed abowe are activated by loading _biokit_ module.

```text
module load biokit
```

After that you can e.g. use _esearch_ and _efetch_ to retrieve protein or nucleotide sequence entries, whose annotation matches the given search terms. In search terms, you can also use wildcard character *, to match any string. The search is case-insensitive: Mus and mus will produce the same matches. You can also focus your search to certain fileds of the search database (Keywords, Author, Organism, Accession, Gene name, Protein name, Sequence length etc.). In the case of sequence length, a range should be defined with syntax _from_:_to_. For example: 120:125.


Normally it is wise to first use just the _esearch_ command to get an idea how much hits are found. 
For example search:
```text
esearch -db nucleotide -query barc
```
will report that 267791 hits were fould.
```text
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>NCID_1_7176041_130.14.18.48_9001_1567161450_1478919739_0MetA0_S_MegaStore</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>267791</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
```

In this case it might be reasonable to refine the serach, before the search definition is furter piped to _efetch_ command for the actual data retrieval. One search can include several search terms that are combined using logical operators (AND, OR, NOT). The matching sequences can be saved in several formats, for example fasta or Genebank formats are supported. The command below retrieves just one entry, Lyngbya majuscula barbamide biosynthesis gene cluster, that contains gene with name _braC_.

```text
esearch -db nucleotide -query "barc [GENE] AND Lyngbya majuscula [ORGN]" | efetch -format gb > barc_Lm.gb
```


## Manual

*    [Edirect manual](https://www.ncbi.nlm.nih.gov/books/NBK179288/)


