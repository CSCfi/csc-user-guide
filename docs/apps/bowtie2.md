---
tags:
  - Free
catalog:
  name: Bowtie2
  description: Short read aligner
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
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

* Roihu: 2.5.4, via the `bio-apps` module.

## Usage

Bowtie2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Bowtie2 module:

```bash
module load bio-apps/v202603
module load bowtie2/2.5.4
```

In a typical Bowtie2 run, you first need to index the reference genome with the `bowtie2-build` command. You should do this in a scratch directory instead of your 
home directory. For example:

```bash
bowtie2-build genome.fa genome
```

When the reference genome has been indexed, the actual alignment job can be launched with the `bowtie2` command. For example, for single end reads, this could be done with the command:

```bash
bowtie2 -x genome -U reads.fq -S output.sam
```

For paired end data, the minimal Bowtie2 syntax is:

```bash
bowtie2 -x genome -1 first_read_set.fq -2 second_read_set.fq -S output.sam
``` 

### Example batch script

`bowtie` and `bowtie2` jobs should be run as batch jobs. Below is a sample batch job script 
for running a Bowtie2 paired-end alignment on Roihu. The recent Bowtie2 versions scale well, so you can effectively use up 
to 16 cores in your batch job.

```bash
#!/bin/bash
#SBATCH --job-name=bowtie2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=1000M

module load bio-apps/v202603
module load bowtie2/2.5.4

bowtie2-build genome.fasta genome
bowtie2 -p $SLURM_CPUS_PER_TASK -x genome -1 reads_1.fq -2 reads_2.fq -S output.sam
```

In the batch job example above one task (`--ntasks=1`) is executed. The Bowtie2 job uses 16 cores (`--cpus-per-task=16`) with a total of 16 GB of memory. 
The maximum duration of the job is four hours (`--time=04:00:00`).
All the cores are assigned from one computing node (`--nodes=1`).
Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## References

When you use Bowtie2, please cite:

> Langmead B, Salzberg S. Fast gapped-read alignment with Bowtie 2. Nature Methods. 2012, 9:357-359.

## Support

[CSC Service Desk](../support/contact.md)

## More information

More information about Bowtie2 can be found from the [Bowtie2 home page](https://github.com/BenLangmead/bowtie2/blob/master/README.md).
