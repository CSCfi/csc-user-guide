---
tags:
  - Free
catalog:
  name: MetaBAT2
  description: Reconstructing genomes from complex microbial communities
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MetaBAT2

MetaBAT2 bins the contigs of a metagenomic assembly into individual genomes, using
sequence composition together with the coverage depth of one or more read sets mapped
back to the assembly.

[TOC]

## Available

* Roihu-CPU: 2.15
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail metabat` after loading `bio-apps`.

## License

Free to use and open source under
[BSD 3-Clause LBNL License](https://spdx.org/licenses/BSD-3-Clause-LBNL.html).

## Usage

On Roihu, MetaBAT2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load metabat
```

Binning needs a per-contig coverage depth file, which the bundled
`jgi_summarize_bam_contig_depths` helper builds from sorted, indexed BAM files:

```bash
jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_reads.bam
```

The basic binning syntax is:

```bash
metabat2 -i assembly.fasta -a depth.txt -o bins/bin -t 8
```

Heavier jobs should be run as batch jobs. MetaBAT2 scales with the number of threads
given to `-t`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=metabat2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load metabat

srun jgi_summarize_bam_contig_depths --outputDepth depth.txt sorted_reads.bam
srun metabat2 -i assembly.fasta -a depth.txt -o bins/bin -t $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch metabat2_job.sh`.

## More information

* [MetaBAT home page](https://bitbucket.org/berkeleylab/metabat)
* [CSC Service Desk](../support/contact.md)
