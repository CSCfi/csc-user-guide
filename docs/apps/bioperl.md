---
tags:
  - Free
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

- Puhti: Perl 5.36.0 with BioPerl 1.7.8

## Usage

On Puhti, BioPerl can be taken in use with the command:

```bash
module load biokit
```

After this, you can launch a BioPerl program with the command:

```bash
perl my_bioperl_code.pm
```

Alternatively you can change the Perl definition in the first line of your code to

```bash
#!/bin/env perl
```

and execute the Perl program:

```bash
./my_bioperl_code.pm
```
 
## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BioPerl home page](https://bioperl.org/)
