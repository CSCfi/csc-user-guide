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
    - Puhti
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

- Puhti: Perl 5.36.0 with BioPerl 1.7.8
- Roihu

Check the installed versions on Roihu with `module avail perl-bioperl` after loading
`bio-apps`.

## Usage

### Puhti

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

### Roihu

On Roihu, BioPerl is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load perl-bioperl
```

After this, you can launch a BioPerl program with the command:

```bash
perl my_bioperl_code.pm
```

Heavier scripts should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bioperl
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load perl-bioperl

srun perl my_bioperl_code.pm
```

Submit the job with `sbatch bioperl_job.sh`.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BioPerl home page](https://bioperl.org/)
