# BRAKER

## Description

BRAKER is a tool for eukaryotic genome annotation. 
It uses genomic and RNA-Seq data to automatically generate full gene structure annotations in novel genome.
BRAKER is based on GeneMark-ET R2 and AUGUSTUS pipelines.

## License

Free to use and open source under [Artistic License] (https://opensource.org/licenses/artistic-license-1.0)

## Version

Version on CSC's Servers

Puhti: 2.1.6


## Usage

In Puhti BRAKER should be used only in batch jobs. Either in normal batch jobs or in interactive batch jobs.

### Interactive usage

You can start interactive batch job with command:

```text
sinteractive -i
```
BRAKER can utilize several computing cores and can require significant amount of memory so you should reserve
more than the default resources for your interactive batch job. For example 4 cores and 32 GB of memory. 

In batch job, you can initialize BRAKER environment with command

```text
module load braker
```
After that you can launch a BRAKER job with command:

```text
braker-puhti
```

This command should be used in stead of the original _braker.pl_ script, as it automatically sets 
some parameters that enable running BRAKER in Puhti. _braker-puhti_ is able to use all the command line options
of _braker.pl_. To see the options, run command:

```text
braker-puhti --help
```
Sample BRAKER command in Puhti:

```text
 braker-puhti --species=sp1 --genome=Drosophila.dna.fa --prot_seq=Drosophila.pep.fa --prg=gth --trainFromGth --AUGUSTUS_ab_initio --cores=$SLURM_CPUS_PER_TASK
```
### Batch jobs
 
Sanple batch job scrip for BRAKER:

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

# start the job
braker-puhti --species=sp1 --genome=Drosophila.dna.fa --prot_seq=Drosophila.pep.fa \
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
