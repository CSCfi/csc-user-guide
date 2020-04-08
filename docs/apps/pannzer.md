# PANNZER2/SANSPANZ

## Description

PANNZER2/SANSPANZ is a fully automated service for functional annotation 
of prokaryotic and eukaryotic proteins of unknown function. The tool is 
designed to predict the functional description (DE) and gene ontology (GO) classes. 

## License

Pannzer has been published with the GNU Public Licence v3.

## Usage

In puhti SANSPANZ annotation tool is taken in use with command:

    module load biokit

After loading the module you can launch sanspanz analysis using command `runsanspanz.py`. For example:
```text
runsanspanz.py -R -m Pannzer -s "species name" -i  input_seqs.fasta -o results.csv
```
The species name is used to determine taxonomic distances. 
The output is written to the file defined with option `-o`.  Also three other output files are created:
*   **Pannzer.out_1** contains details of the description (DE) prediction. 
*   **Pannzer.out_2** contains details of the GO prediction. 
*   **Pannzer.out_3** is a summary of all predicted annotations.

Pannzer.out_3 can be converted to HTML-format with command `anno2html.pl`:

```text
perl anno2html.pl < Pannzer.out_3 > annotations.html
```
If you upload this file to Allas with command:
```text
a-flip annotations.html
```
You can use the link provided by _a-flip_ to study the results with your browser.

Note, that in Puhti you should always use `runsanspanz.py` with option `-R` that sends the
analysis jobs to the annotation sever maintained by the Holm group. Thus, the job does not use 
the resources of Puhti and it can be run as an intercative job in a login node.

## More information

For more information, execute command:
```text
runsanspanz.py -h
```
Or study Pannzer home page:

*   [Pannzer home page](http://ekhidna2.biocenter.helsinki.fi/sanspanz/)
