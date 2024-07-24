---
tags:
  - Free
---

# PANNZER2/SANSPANZ

PANNZER2/SANSPANZ is a fully automated service for functional annotation 
of prokaryotic and eukaryotic proteins of unknown function. The tool is 
designed to predict the functional description (DE) and gene ontology (GO) classes. 

## License

PANNZER has been published with the [GNU Public Licence v3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

PANNZER is available on Puhti.

## Usage

On Puhti, SANSPANZ annotation tool can be accessed with the command:

```bash
module load biokit
```

After loading the module, you can launch SANSPANZ analysis using command `runsanspanz.py`. For example:

```bash
runsanspanz.py -R -m Pannzer -s "species name" -i  input_seqs.fasta -o results.csv
```

The species name is used to determine taxonomic distances. 
The output is written to the file defined with option `-o`. Also, three other output files are created:

* **Pannzer.out_1** contains details of the description (DE) prediction.
* **Pannzer.out_2** contains details of the GO prediction.
* **Pannzer.out_3** is a summary of all predicted annotations.

Pannzer.out_3 can be converted to HTML-format with command `anno2html.pl`:

```bash
anno2html.pl < Pannzer.out_3 > annotations.html
```

If you upload this file to Allas with the command:

```bash
a-flip annotations.html
```

you can use the link provided by `a-flip` to study the results with your browser.

Note, that on Puhti you should always use `runsanspanz.py` with option `-R` that sends the
analysis jobs to the annotation server maintained by the Holm group. Thus, the job does not use 
the resources of Puhti, and it can be run as an interactive job on a login node.

## More information

For more information, execute command:

```bash
runsanspanz.py -h
```

Or study the PANNZER home page:

* [PANNZER home page](http://ekhidna2.biocenter.helsinki.fi/sanspanz/)
