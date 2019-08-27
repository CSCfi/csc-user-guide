# SAMtools

## Description

SAMtools provides tools for using and manipulating SAM and BAM formatted alignments. 
You can use SAMtools for example for indexing, variant calling and viewing alignments.

## Available

Version on CSC's Servers

Puhti: 1.9
Taito: 0.1.19, 1.4, 1.8, 1.9

Usage

To use SAMtools in Puhti you can use initialization command:
```
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including SAMtools and Picard 
(Note however that there are also bioinformatics tools in Puhti, that have a separate setup commands.)

After this you can launch samtools
```
samtools
```
SAMtool jobs should either be run in Taito-shell or be executed as batch jobs. Below is a sample batch job file, 
for running a SAMtools job in Taito:

```
#!/bin/bash -l
#SBATCH -J samtools
#SBATCH -o output_%j.txt
#SBATCH -e errors_%j.txt
#SBATCH -t 04:00:00
#SBATCH --mem-per-cpu=4000
#SBATCH -n 1

#Convert SAM file to BAM
samtools view -bS aln.sam > aln.bam

#Sort the bam file
samtools sort aln.bam aln-sorted

#Index the bam file
samtools index aln-sorted.bam
```
In the batch job example above one task (-n 1) is executed. The maximum duration of the job is four hours 
(-t 04:00:00 ) and the reserved memory size is about 4 GB (--mem-per-cpu=4000).

You can submit the batch job file to the batch job system with command:
```
sbatch batch_job_file.bash
```
Check the chapter 3 of the Taito user guide for more information about running batch jobs.


## Manual

-    [SAMtools home page](http://www.htslib.org/)

