---
tags:
  - Free
---

# Lazypipe

 

Lazypipe is a stand-alone pipeline for identifying viruses in host-associated or environmental samples. The main emphasis is on assembling, taxonomic binning and taxonomic profiling of bacterial/viral sequences.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/OverZealous/lazypipe/master/LICENSE).

## Available

Lazypipe 3.0 is available in Puhti.

## Usage

All components of Lazypipe pipeline are available in Puhti. The [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe) provides detailed instruction how to set up your own Lazypipe environment to Puhti, but this is not needed if you use the Lazypipe module that is activated with commands:

```bash
module load r-env
module load biokit
module load lazypipe
```

Now Lazypipe starts with commands:

```bash
cp /appl/soft/bio/lazypipe/3.0/lazypipe/config.yaml config.yaml
echo tmpdir: \"$(pwd)/tmpdir\" >> config.yaml
echo res: \"$(pwd)/tmpdir\" >> config.yaml
lazypipe.pl -h
```

Normally you need to use the `lazypipe.pl` command only for testing. For real analysis tasks lazypipe module includes `sbatch-lazypipe` command that you can use instead. 

`sbatch-lazypipe` is a help tool that automatically generates a configuration file and a batch job file for a Lazypipe run 
and submits the job to batch job system of Puhti. The command uses the same command line options 
as the `lazypipe.pl` command. In addition `sbatch-lazypipe` asks user to define batch job resources
(account, run time, memory, number of cores).

For example, to execute the [Example 1](https://www.helsinki.fi/en/projects/lazypipe/examples) from the
Lazypipe User manual, you would first need to download the reads and reference genome to your scratch directory in Puhti
(in real cases you will get these input files from your own sources):

```bash
mkdir /scratch/my_project/data
mkdir /scratch/my_project/hostgen
cp /appl/soft/bio/lazypipe/3.0/lazypipe/data/samples/M15small_R*.fastq /scratch/my_project/data
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/108/605/GCA_900108605.1_NNQGG.v01/GCA_900108605.1_NNQGG.v01_genomic.fna.gz -P /scratch/my_project/hostgen/
```

When you have the data available you can submit the task with commands:

```bash
cd /scratch/my_project
module load r-env
module load biokit
module load lazypipe
sbatch-lazypipe -1 data/M15/M15small_R1.fastq -S M15 -p main --anns norm\
--hostgen genomes_host/GCA_900108605.1_NNQGG.v01_genomic.fna.gz -v
```

When the `sbatch-lazypipe` is executed, it interactively asks information that is
needed to construct a batch job. This includes following items (default values in brackets will be
used if no new value is defined):

*   accounting project
*   maximum duration of the job (default 24 hours)
*   memory reservation (default 32G)
*   number of computing cores to use (default 8)
*   email notifications
   
After that your Lazypipe task is submitted to the batch job system for execution.

## More information

*   [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe)
*   [Lazypipe UserGuide](https://bitbucket.org/plyusnin/lazypipe/wiki/UserGuide.v3.0)
