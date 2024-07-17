---
tags:
  - Free
---

# SAMtools



SAMtools provides tools for using and manipulating SAM and BAM formatted alignments. 
You can use SAMtools for example for indexing, variant calling and viewing alignments.

[TOC]

## License

Free to use and open source under [MIT/Expat License](https://github.com/samtools/samtools/blob/develop/LICENSE).

## Available



Puhti: 1.9, 1.16, 1.18


## Usage

To use SAMtools in Puhti you can use initialization command:
```text
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including SAMtools and Picard 
(Note however that there are also bioinformatics tools in Puhti, that have a separate setup commands.)

After this you can launch samtools
```
samtools
```

You can check the available samtools versions with command:

```
module spider samtools
```

And the activate the version you want to use. For example:
```
module load samtools/0.1.19
```

Loading SAMtools 1.x also loads BCFtools and HTSlib.

Heavier SAMtool jobs should be executed as batch jobs. Below is a sample batch job file, 
for running a SAMtools job in Puhti:

```text
#!/bin/bash -l
#SBATCH --job-name=samtools
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --mem=4000
#SBATCH --account=project_1234567
#SBATCH --ntasks=1

#Convert SAM file to BAM
samtools view -bS aln.sam > aln.bam

#Sort the bam file
samtools sort aln.bam aln-sorted

#Index the bam file
samtools index aln-sorted.bam
```
In the batch job example above one task (-n 1) is executed. The maximum duration of the job is four hours 
(-t 04:00:00 ) and the reserved memory size is about 4 GB (--mem=4000). You must cange the --account 
setting, so that it defines the project from which the computing will be billed.

You can submit the batch job file to the batch job system with command:
```text
sbatch batch_job_file.bash
```
Check the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.


## More information

-    [SAMtools home page](http://www.htslib.org/)

