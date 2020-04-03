# PANNZER2/SANSPANZ

### Description

PANNZER2/SANSPANZ is a fully automated service for functional annotation 
of prokaryotic and eukaryotic proteins of unknown function. The tool is 
designed to predict the functional description (DE) and GO classes. 


### Usage

In puhti SANSPANZ annotation tool is taken in use with command:

    module load biokit

After loading the module you can launch sanspanz analysis using command
```text
runsanspanz.py -R -m Pannzer -s "species name" -i  input_seqs.fasta -o results.csv
```
The species name is used to determine taxonomic distances. 
The output is written to the file defined with option`-o`.  Also three other output files are created:
*   **Pannzer.out_1** contains details of the description (DE) prediction. 
*   **Pannzer.out_2** contains details of the GO prediction. 
*   **Pannzer.out_3** is a summary of all predicted annotations.

Pannzer.out_3 can be converted to HTML by the anno2html.pl script:

```text
perl anno2html.pl < Pannzer.out_3 > annotations.html
```
If you upload this file to allas with command:
```text
a-flip annotations.html
```
You can use the link provided by _a-filp_ to study the resoults with your browser.

For more information run command:
```text
runsanspanz.py -h
```
## More information

*   [Pannzer home page](http://ekhidna2.biocenter.helsinki.fi/sanspanz/)
