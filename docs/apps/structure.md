# Structure

## Descrioption

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
In Puhti, we recommend that you submit your structure jobs using help tool called `strauto-puhti`.
This tool is a modified version of [strauto](http://dx.doi.org/10.1186/s12859-017-1593-0) structure
job sumbission tool. Note that many details in the strauto manual do not apply to atrauto-puhti.   

Next move to the scratch directory of your project. Any subdirectory inside your scratch area will do.
For example:

```text
cd /scratch/project_xxxxxx/sampleuser
```
Create a new empty directory.

```text
mkdir structure_job1
```
Next you need to copy or create to this directory the two input files used by _strauto-puhti_ program.
The parameter file must always be named as `input.py`. The name of the actual datafile is defined in
`input.py`. The data file name should end with `.str`. 

A sample file, provided by strauto can be copied to your current directory with commands:

```text
cp /appl/soft/bio/structure/strauto/input.py ./  
cp /appl/soft/bio/structure/strauto/sim.str ./ 
```

When the input file have been prepared, the strcture job can be launched with command:
```text
strauto-puhti
```
Plese read and follow the instructions of job submission command above.


## More information

*    [Structure home page](https://web.stanford.edu/group/pritchardlab/structure.html)
*    [Strauto home page ](http://strauto.popgen.org)
*    [StructureHarvester home page](http://taylor0.biology.ucla.edu/structureHarvester/)



