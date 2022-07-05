# BAKER

## Description

Braker is a tool for eukaryotic genome annotation. 
It uses genomic and RNA-Seq data to automatically generate full gene structure annotations in novel genome.
Barker is based on GeneMark-ET R2 and AUGUSTUS pipelines.

## License

Free to use and open source under [Artistic License] (https://opensource.org/licenses/artistic-license-1.0)

## Version

Version on CSC's Servers

Puhti: 2.1.6


## Usage

In Puhti Braker should be used only in batch jobs. Either in normal batch jobs or in interactive batch jobs.
You can start interative batch job with command:

```text
sinteractive -i
```
In batch job, you can initialize Braker environment with command

```text
module load braker
```
After that you can launch a Braker job with command:

```text
braker-puhti
```

This command shoudl be used in stead of the original _braker.pl_ script as it automatically do 
some settings that allow you to run baraker. _braker-puhti_ is able to use all the command line options
of _braker.pl_. To see the options, run commaand.

```text
braker-puhti --help
```
Sample braker command in Puhti:

```text
 braker-puhti --species=sp1 --genome=Drosophila.dna.fa --prot_seq=Drosophila.pep.fa --prg=gth --trainFromGth --AUGUSTUS_ab_initio --cores=SLURM_CPUS_PER_TASK
 ```
 
##More information

   * [BRAKER home page](https://github.com/Gaius-Augustus/BRAKER)
