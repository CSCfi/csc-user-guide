---
tags:
  - Free
catalog:
  name: SAMtools
  description: Utilities for managing SAM/BAM formatted alignment files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SAMtools



SAMtools provides tools for using and manipulating SAM and BAM formatted alignments. 
You can use SAMtools for example for indexing, variant calling and viewing alignments.

[TOC]

## License

Free to use and open source under [MIT/Expat License](https://github.com/samtools/samtools/blob/develop/LICENSE).

## Available



Roihu: 1.21


## Usage

To use SAMtools in Rohu you can use initialization commands:

```bash
module load bio-apps
module load samtools
```

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
module load samtools/1.21
```

SAMtools jobs should be executed as batch jobs. Below is a sample batch job file, 
for running a SAMtools job in Roihu:

```text
#!/bin/bash
#SBATCH --job-name=samtools
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --mem=4000
#SBATCH --account=project_1234567
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=small

#Convert SAM file to BAM
samtools view -bS aln.sam > aln.bam

#Sort the bam file
samtools sort aln.bam aln-sorted

#Index the bam file
samtools index aln-sorted.bam
```
In the batch job example above one task (--ntasks 1) is executed using using one core (--cpus-per-task=1). 
The maximum duration of the job is four hours (-t 04:00:00 ) and the reserved memory size is 4 GB (--mem=4000). You must change the --account setting to use your account.

You can submit the batch job file to the batch job system with command:
```text
sbatch batch_job_file.bash
```
Check the [Roihu user guide](../computing/running/getting-started.md) for more information about running batch jobs.


## More information

-    [SAMtools home page](http://www.htslib.org/)

