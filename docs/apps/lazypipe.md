---
tags:
  - Free
catalog:
  name: Lazypipe
  description: A stand-alone pipeline for identifying viruses in host-associated or environmental samples
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Lazypipe

 

Lazypipe is a stand-alone pipeline for identifying viruses in host-associated or environmental samples. The main emphasis is on assembling, taxonomic binning and taxonomic profiling of bacterial/viral sequences.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/OverZealous/lazypipe/master/LICENSE).

## Available

Lazypipe 3.1 is available in Puhti.

## Usage

All components of Lazypipe pipeline are available in Puhti. The [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe) provides detailed instruction how to set up your own Lazypipe environment to Puhti, but this is not needed if you use the Lazypipe module that is activated with commands:

```bash
module load r-env
module load biokit
module load lazypipe
```

Now Lazypipe starts with commands:

```bash
cp /appl/soft/bio/lazypipe/3.1/lazypipe/config.yaml config.yaml
echo tmpdir: \"$(pwd)/tmpdir\" >> config.yaml
echo res: \"$(pwd)/tmpdir\" >> config.yaml
lazypipe.pl -h
```

Normally you need to use the `lazypipe.pl` command only for testing. For real analysis tasks lazypipe module includes `sbatch-lazypipe` command that you can use instead. 

`sbatch-lazypipe` is a help tool that automatically generates a configuration file and a batch job file for a Lazypipe run 
and submits the job to batch job system of Puhti. The command uses the same command line options 
as the `lazypipe.pl` command. In addition `sbatch-lazypipe` asks user to define batch job resources
(account, run time, memory, number of cores).

For example, to execute main analysis steps on a M15 sample data (Illumina PE from mink feces) run the following commands:

```bash
cd /scratch/my_project 
module load r-env
module load biokit 
module load lazypipe 

sbatch-lazypipe -1 /appl/soft/bio/lazypipe/3.1/lazypipe/data/samples/M15small_R*.fastq -S M15 -p main --flt Neovison_vison --anns vi.nt -vnorm 
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

## Additional commands 

Listing reference databases available for Lazypipe module: 

```bash
lazypipe.pl --databases 
```

Listing background filters available for Lazypipe module: 

```bash
lazypipe.pl --filters 
```
 
## More information

*   [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe)
*   [Lazypipe UserGuide](https://bitbucket.org/plyusnin/lazypipe/wiki/UserGuide.v3.0)
