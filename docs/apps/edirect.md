---
tags:
  - Free
---

# Entrez Direct

Edirect, or Entrez Direct, is a toolkit to retrieve sequences and other data from the NCBI sequence databases based on given query terms. 
The package consists of several commands:

1. Navigation functions support exploration within the Entrez databases:
    * `esearch` performs a new Entrez search using terms in indexed fields.
    * `elink` looks up neighbors (within a database) or links (between databases).
    * `efilter` filters or restricts the results of a previous query.
2. Records can be retrieved in specified formats or as document summaries:
    * `efetch` downloads records or reports in a designated format.
3. Desired fields from XML results can be extracted without writing a program:
    * `xtract` converts Edirect XML output into a table of data values.
4. Several additional functions are also provided:
    * `einfo` obtains information on indexed fields in an Entrez database.
    * `epost` uploads unique identifiers (UIDs) or sequence accession numbers.
    * `nquire` sends a URL request to a web page or CGI service

[TOC]

## License

Free to use for all users. [Public Domain notice](https://www.ncbi.nlm.nih.gov/books/NBK179288/#chapter6.Appendices).

## Available

Puhti: 13.4

## Usage

The `edirect` commands listed above are activated by loading the `biokit` module.

```bash
module load biokit
```

After that you can, e.g., use `esearch` and `efetch` to retrieve protein or nucleotide sequence entries, whose annotation matches the given search terms. In search terms, you can also use wildcard character `*` to match any string. The search is case-insensitive: "Mus" and "mus" will produce the same matches. You can also focus your search to certain fields of the search database (Keywords, Author, Organism, Accession, Gene name, Protein name, Sequence length etc.). In the case of sequence length, a range should be defined with syntax `from:to`. For example: `120:125`.

Normally, it is wise to first use just the `esearch` command to get an idea how many hits are found. 
For example, search:

```bash
esearch -db nucleotide -query barc
```

will report that 267791 hits were found.

```xml
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>NCID_1_7176041_130.14.18.48_9001_1567161450_1478919739_0MetA0_S_MegaStore</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>267791</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
```

In this case it might be reasonable to refine the search before the search definition is further piped to `efetch` command for the actual data retrieval. One search can include several search terms that are combined using logical operators (`AND`, `OR`, `NOT`). The matching sequences can be saved in several formats, for example, fasta or Genebank formats are supported. The command below retrieves just one entry, _Lyngbya majuscula_ barbamide biosynthesis gene cluster that contains gene with name _braC_.

```bash
esearch -db nucleotide -query "barc [GENE] AND Lyngbya majuscula [ORGN]" | efetch -format gb > barc_Lm.gb
```

## More information

* [Edirect manual](https://www.ncbi.nlm.nih.gov/books/NBK179288/)
