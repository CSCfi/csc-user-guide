---
tags:
  - Free
catalog:
  name: PANNZER2/SANSPANZ
  description: Automatic protein annotation tool
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PANNZER2/SANSPANZ

PANNZER2/SANSPANZ is a fully automated service for functional annotation
of prokaryotic and eukaryotic proteins of unknown function. The tool is
designed to predict the functional description (DE) and gene ontology (GO) classes.

[TOC]

## License

PANNZER has been published with the [GNU Public Licence v3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu-CPU: 3.20250512 (module `sanspanz`), via the `bio-apps` module. The version
  number is the release date of the SANSPANZ 3 package.

## Usage

SANSPANZ is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SANSPANZ module:

```bash
module load bio-apps/v202603
module load sanspanz/3.20250512
```

After loading the module, you can launch SANSPANZ analysis using command `runsanspanz.py`. For example:

```bash
runsanspanz.py -R -m Pannzer -s "species name" -i input_seqs.fasta -o results.csv
```

The species name is used to determine taxonomic distances.
The output is written to the file defined with option `-o`. Also, three other output files are created:

* **Pannzer.out_1** contains details of the description (DE) prediction.
* **Pannzer.out_2** contains details of the GO prediction.
* **Pannzer.out_3** is a summary of all predicted annotations.

Note, that on Roihu you should always use `runsanspanz.py` with option `-R` that sends the
analysis jobs to the annotation server maintained by the Holm group. Thus, the job does not use
the resources of Roihu, and it can be run as an interactive job on a login node.

## Support

[CSC Service Desk](../support/contact.md)

## More information

For more information, execute command:

```bash
runsanspanz.py -h
```

Or study the PANNZER home page:

* [PANNZER home page](http://ekhidna2.biocenter.helsinki.fi/sanspanz/)
