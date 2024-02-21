---
tags:
  - Free
---

# BRAKER

## Description

BRAKER is a tool for eukaryotic genome annotation. 
It uses genomic and RNA-Seq data to automatically generate full gene structure annotations in novel genome.
BRAKER is based on GeneMark-ET R2 and AUGUSTUS pipelines.

## License

Free to use and open source under [Artistic License] (https://opensource.org/licenses/artistic-license-1.0)

## Version

Version on CSC's Servers

Puhti: 2.1.6, 3.0.7


## Setting up BRAKER

BRAKER needs some additional setting up steps before using it for the first time.

CSC BRAKER installations do not contain GeneMark or ProHint softaware packages. While they are free
for individual use, their licensing terms do not allow CSC to make a public installation of them.
Each user needs to license and install them for their own use.

### GeneMark

Go to [GeneMark download page](http://exon.gatech.edu/GeneMark/license_download.cgi), and fill in the form. The version you need is "GeneMark-ES/ET/EP+" for "LINUX 64 kernel 3.10 - 5". Download the program file and yhe license key. To uncompress the packages:

```
tar xf gmes_linux_64_4.tar.gz
gunzip gm_key_64.gz
```

To tell BRAKER where to find GeneMark, set environment variable `$GENEMARK_PATH`to point to install location or use command line option `--GENEMARK_PATH`.

```
export GENEMARK_PATH=/path/to/gmes_linux_64_4
```

BRAKER module contains all the necessary dependencies.

### ProHint

Download and uncompress ProHint.

```
wget https://github.com/gatech-genemark/ProtHint/releases/download/v2.6.0/ProtHint-2.6.0.tar.gz
tar xf ProtHint-2.6.0.tar.gz
```

Set environment variable `$PROHINT_PATH`to point to install location  or use command line option `--PROHINT_PATH`.

```
export PROHINT_PATH=/path/to/ProtHint-2.6.0/bin
```

BRAKER module contains all the necessary dependencies.

### AUGUSTUS

AUGUSTUS is inluded in the installation, but you will need your own copy of AUGUSTUS config directory, as it needs to be writable by the user. You can create this by running command:

```
copy_config
```

It will create directory `config` in your current directory.

Set environment variable `$AUGUSTUS_CONFIG_PATH` to pint to the config directory or use command line option `--UGUSTUS_CONFIG_PATH`

## Usage

In Puhti BRAKER should be used only in batch jobs. Either in normal batch jobs or in interactive batch jobs.

### Interactive usage

You can start interactive batch job with command:

```
sinteractive -i
```
BRAKER can utilize several computing cores and can require significant amount of memory so you should reserve
more than the default resources for your interactive batch job. For example 4 cores and 32 GB of memory. 

In batch job, you can initialize BRAKER environment with command

```
module load braker
```

After that you can launch a BRAKER job with command:

```
braker.pl
```

To see the options, run command:

```
braker.pl --help
```

Sample BRAKER command in Puhti:

```
 braker.pl --species=sp1 --genome=Drosophila.dna.fa --prot_seq=Drosophila.pep.fa --prg=gth --trainFromGth --AUGUSTUS_ab_initio --cores=$SLURM_CPUS_PER_TASK
```

### Batch jobs
 
Sample batch job scrip for BRAKER:

```text
#!/bin/bash
#SBATCH --job-name=BRAKER_Job
#SBATCH --account=project_2012345
#SBATCH --time=24:00:00
#SBATCH --mem=32000
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8  
#SBATCH --partition=small

# load braker
module load braker

# Use correct paths instead of "/path/to"
export GENEMARK_PATH=/path/to/gmes_linux_64_4
export PROHINT_PATH=/path/to/ProHint-2.6.0/bin
export AUGUSTUS_CONFIG_PATH=/path/to/config


# start the job
braker.pl --species=sp1 --genome=Drosophila.dna.fa --prot_seq=Drosophila.pep.fa \
--prg=gth --trainFromGth --AUGUSTUS_ab_initio --cores=$SLURM_CPUS_PER_TASK
```

In the batch job example above one task (--ntasks 1) is executed. The BRAKER job uses 8 cores (--cpus-per-task=8 ) with total of 32 GB of memory (--mem=32000). 
The maximum duration of the job is ten hours (--time 10:00:00 ). 
All the cores are assigned from one computing node (--nodes=1 ). 
In the example the project that will be used is _project_2012345_. 
This value shuold be replaced by the name of your computing project.

You can submit the batch job file to the batch job system with command:

```
sbatch batch_job_file.bash
```
See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.
 
 
 
 
## More information

   * [BRAKER home page](https://github.com/Gaius-Augustus/BRAKER)
