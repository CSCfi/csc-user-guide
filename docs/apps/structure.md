# Structure

## Description

The program _structure_ is a software package for using multi-locus genotype data to investigate population structure. 
Its uses include inferring the presence of distinct populations, assigning individuals to populations, studying hybrid zones, 
identifying migrants and admixed individuals, and estimating population allele frequencies in situations where many 
individuals are migrants or admixed. 

It can be applied to most of the commonly-used genetic markers, including SNPS, microsatellites, RFLPs and AFLPs. 

## Version

*    Structre 2.3.4 is available in Puhti

## Usage

To use Structure in Puhti, run first following setup commands:

```text
module load biokit
module load strcture
```

In addition to `structure` command the structure module makes available commands [CLUMPP](https://web.stanford.edu/group/rosenberglab/clumpp.html) and [structureHarvester](https://github.com/dentearl/structureHarvester/) that can be used for postprocessing structure results.

In Puhti, we recommend that you submit your structure jobs using help tool called `strauto-puhti`.
This tool is a modified version of [strauto](http://dx.doi.org/10.1186/s12859-017-1593-0) structure
job sumbission tool. Note that many details in the strauto manual do not apply to `strauto-puhti`.   

Next move to the scratch directory of your project. Any subdirectory inside your scratch area will do.
For example:

```text
cd /scratch/project_xxxxxx/sampleuser
```
Create a new empty directory.

```text
mkdir structure_job1
```
Next you need to copy or create to this directory the two input files used by `strauto-puhti` program.
The parameter file must always be named as `input.py`. The name of the actual datafile is defined in
`input.py`. The data file name should end with `.str` or `.ustr`. 

A sample file, provided by strauto can be copied to your current directory with commands:

```text
cd structure_job1
cp /appl/soft/bio/structure/strauto/input.py ./  
cp /appl/soft/bio/structure/strauto/sim.str ./ 
```

When the input file has been prepared, the strcture job can be launched with command:
```text
strauto-puhti
```
Strauto, first asks you to check and accept Structure parameters and after that
submits the structure job to to the batch job system of Puhti. After that
it starts monitoring the progress of your job.

You can leave the monitor process running, but if you want to stop it, press:
`Ctrl-c`

The structure jobs will still continue their execution in the batch job system
of  Puhti. If you run the command:

```text
strauto-puhti
```
in the same directory again it will check the status of structure jobs and do the
postporcessing of the results if all the structure-related tasks have finished.

Note, that _strauto-puhti_ does not use the internal, gnu-parallel based, parallelization.
Instead, parallelization is based on array jobs. Because of this, you should not change 
the _parallel_ parameter value to _True_ in the structure input file. 

## More information

*    [Structure home page](https://web.stanford.edu/group/pritchardlab/structure.html)
*    [Strauto home page ](http://strauto.popgen.org)
*    [StructureHarvester home page](http://taylor0.biology.ucla.edu/structureHarvester/)



