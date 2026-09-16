---
tags:
  - Free
catalog:
  name: BioPerl
  description: Perl environment with bioperl extension
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BioPerl

BioPerl is a collection of Perl modules that facilitate the development of 
Perl scripts for bioinformatics applications. As such, it does not include 
ready to use programs in the sense that many commercial packages and free 
web-based interfaces do. On the other hand, BioPerl does provide reusable 
Perl modules that facilitate writing Perl scripts for sequence manipulation, 
accessing of databases using a range of data formats and execution and parsing 
of the results of various molecular biology programs. Consequently, BioPerl 
enables developing scripts that can analyze large quantities of sequence 
data in ways that are typically difficult or impossible with web based systems.

[TOC]

## License

BioPerl is free to use and open source.

BioPerl is licensed under the same terms as Perl itself which is dually-licensed under the terms of the [Perl Artistic license](https://dev.perl.org/licenses/artistic.html) or [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: BioPerl 1.7.8 (module `perl-bioperl`), via the `bio-apps` module.

## Usage

BioPerl is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BioPerl module:

```bash
module load bio-apps/v202603
module load perl-bioperl/1.7.8
```

After this, you can launch a BioPerl program with the command:

```bash
perl my_bioperl_code.pl
```

Alternatively you can set the interpreter on the first line of your script to

```perl
#!/usr/bin/env perl
```

make it executable, and run it directly:

```bash
chmod +x my_bioperl_code.pl
./my_bioperl_code.pl
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BioPerl home page](https://bioperl.org/)
