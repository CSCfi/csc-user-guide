---
tags:
  - Free
---

# Bowtie2

Bowtie2 is an ultrafast, memory-efficient short read aligner. It aligns short DNA sequences (reads) 
to the human genome at a rate of over 25 million 35-bp reads per hour. Bowtie2 indexes the genome 
with a Burrows-Wheeler index to keep its memory footprint small: typically about 2.2 GB for the 
human genome (2.9 GB for paired-end).

There are two versions of Bowtie available: Bowtie2 and Bowtie. The more recent Bowtie2 program differs 
significantly from its ancestor Bowtie. For example the command line options are different for these two tools.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

-   Puhti: 2.3.5.1, 2.4.1, 2.4.4, 2.5.3
-   Chipster graphical user interface

## Usage

On Puhti, Bowtie2 can be taken in use as part of the `biokit` module collection:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including Bowtie2. Note however that there are other bioinformatics tools on Puhti,
that have a separate setup command.

In a typical Bowtie2 run, you first need to index the reference genome with `bowtie2-build` command. You should do this in scratch directory instead of your 
home directory. For example;

```bash
bowtie2-build genome.fa genome
```

Alternatively, you can use `chipster_genomes` command to download pre-calculated bowtie2 indexes from the CSC Chipster server to Puhti:

```bash
chipster_genomes bowtie2
``` 

When the reference genome has been downloaded or indexed, the actual alignment job can be launched with `bowtie2` command. For example, for single end reads, this could be done with the command:

```bash
bowtie2 -x genome -U reads.fq -S output.sam
```

For paired end data, the minimal Bowtie2 syntax is:

```bash
bowtie2 -x genome -1 first_read_set.fq -2 second_read_set.fq -S output.sam
``` 

### Example batch script for Puhti

On Puhti, `bowtie` and `bowtie2` jobs should be run as batch jobs. Below is a sample batch job file, 
for running a Bowtie2 paired end alignment on Puhti. The recent Bowtie2 versions scale well, so you can effectively use up 
to 16 cores in your batch job.

Note that the batch job file must define the project that will be used.
You can check all the projects that you belong to with the command `groups` or
`csc-projects`. Use [MyCSC](https://my.csc.fi) to obtain more specific information about a
specific project.

```bash
#!/bin/bash -l
#SBATCH --job-name=bowtie2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
#SBATCH --account=project_123456
#SBATCH --mem=16000

module load biokit
bowtie2-build genome.fasta genome
bowtie2 -p $SLURM_CPUS_PER_TASK -x genome -1 reads_1.fq -2 reads_2.fq > output.sam
```

In the batch job example above one task (`--ntasks=1`) is executed. The Bowtie2 job uses 16 cores (`--cpus-per-task=16`) with total of 16 GB of memory (`--mem=16000`). 
The maximum duration of the job is four hours (`--time=04:00:00`).
All the cores are assigned from one computing node (`--nodes=1`).
In the example, the project that will be used is `project_123456`. This value should be replaced by the name of your computing project.

You can submit the batch job file to the batch job system with command:

```bash
sbatch batch_job_file.bash
```

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## References

When you use Bowtie2, please cite:

> Langmead B, Salzberg S. Fast gapped-read alignment with Bowtie 2. Nature Methods. 2012, 9:357-359.

## Support

[CSC Service Desk](../support/contact.md)

## More information

More information about Bowtie2 can be found from the [Bowtie2 home page](https://github.com/BenLangmead/bowtie2/blob/master/README.md).
