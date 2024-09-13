---
tags:
  - Free
---

# Structure

Structure is a software package for using multi-locus genotype data to investigate population structure. 
Its uses include inferring the presence of distinct populations, assigning individuals to populations, studying hybrid zones, 
identifying migrants and admixed individuals, and estimating population allele frequencies in situations where many 
individuals are migrants or admixed.

It can be applied to most of the commonly-used genetic markers, including SNPS, microsatellites, RFLPs and AFLPs. 

[TOC]

## License

- Structure is free to use and open source, but no license is specified.
- StrAuto is free to use and open source, but no license is specified.
- strasuto-puhti is free to use and open source, but no license is specified.
- structureHarvester is free to use and open source under its own [License](https://github.com/dentearl/structureHarvester/blob/master/LICENSE)
- CLUMPP is free to use, but no license is specified.

## Available

* Puhti: 2.3.4

## Usage

To use Structure in Puhti, run first the following setup commands:

```bash
module load biokit
module load structure
```

In addition to the `structure` command, the Structure module makes available programs [CLUMPP](https://web.stanford.edu/group/rosenberglab/clumpp.html) and [structureHarvester](https://github.com/dentearl/structureHarvester/) that can be used for post-processing Structure results.

On Puhti, we recommend that you submit your Structure jobs using a help tool called `strauto-puhti`.
This tool is a modified version of [StrAuto](http://dx.doi.org/10.1186/s12859-017-1593-0) Structure
job submission tool. Note that many details in the StrAuto manual do not apply to `strauto-puhti`.

Next, move to the scratch directory of your project. Any subdirectory inside your scratch area will do.
For example:

```bash
cd /scratch/project_xxxxxx/$USER
```

Create a new empty directory:

```bash
mkdir structure_job1
```

Next, you need to copy or create to this directory the two input files used by `strauto-puhti` program.
The parameter file must always be named as `input.py`. The name of the actual data file is defined in
`input.py`. The data file name should end with `.str` or `.ustr`.

A sample file provided by StrAuto can be copied to your current directory with the commands:

```bash
cd structure_job1
cp /appl/soft/bio/structure/strauto/input.py ./  
cp /appl/soft/bio/structure/strauto/sim.str ./ 
```

When the input file has been prepared, the Structure job can be launched with the command:

```bash
strauto-puhti
```

StrAuto first asks you to check and accept Structure parameters and after that
submits the Structure job to the batch job system of Puhti. After that
it starts monitoring the progress of your job.

You can leave the monitor process running, but if you want to stop it, press
`Ctrl-c`.

The structure jobs will still continue their execution in the batch job system
of Puhti. If you run the command:

```bash
strauto-puhti
```

in the same directory again it will check the status of structure jobs and do the
post-processing of the results if all the Structure-related tasks have finished.

Note that `strauto-puhti` does not use the internal, GNU-parallel based, parallelization.
Instead, parallelization is based on array jobs. Because of this, you should not change 
the _parallel_ parameter value to _True_ in the structure input file. 

## More information

* [Structure home page](https://web.stanford.edu/group/pritchardlab/structure.html)
* [StrAuto home page ](https://vc.popgen.org/software/strauto/)
* [StructureHarvester home page](https://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/)
