
# Running MaxQuant software on Puhti supercomputer

[MaxQuant](https://maxquant.org/) is a quantitative proteomics software package designed for analyzing large mass-spectrometric data sets. More information about the software can be found [here](http://coxdocs.org/doku.php?id=maxquant:start). High-performance computing environment like Puhti is a suitable place for running compute-intensive jobs using MaxQuant software in proteomics research. 

This tutorial provides instructions for running MaxQuant software on Puhti.

## Configure parameter file

Even if you are going to run the MaxQuant pipeline on Puhti, 
you first have to configure different parameters of your MaxQuant 
job on your local Windows machine. And then upload parameter file 
(i.e.,`mqpar.xml`), raw data samples (i.e, .raw files) and sequence 
file (i.e., .fasta file) to Puhti computing environment.

## Edit XML configuration file

You have to make some modifications in parameter file (`mqpar.xml`), which was for example created on a local windows machine, to comply with HPC environment.

These modifications include changes in :

- Windows paths into linux paths for sample files ( tip: search for `<filePaths>` in XML file) 
- Windows path into linux path for fasta sequence file  (tip: search for `<fastaFilePath>` in XML file)
- In the number of threads according to number of samples (tip: search for  `<numThreads>` in XML file)

## Submit as a batch job to Puhti cluster

- First login to Puhti computer (see instructions [here](../../computing/connecting.md))

- Change to your project directory on Puhti and copy your input files there ([tips on how to transfer files](../../data/moving/index.md)).

 This is your project directory (on scratch) where your .xml files, .fasta file, and raw data files are located

- Learn how to enable MaxQuant environment 

MaxQuant software actually also needs mono software to be able to run. 
With mono software, you can choose your *version* of MaxQuant. 
CSC provides a conda environment for working with MaxQuant.

```
module load bioconda
source activate maxquant
```
and then download your linux-compatible version of MaxQuant (e.g., v1.6.3.4) to your 
scratch directory on Puhti and run the following to verify that MaxQuant is installed properly:

```
mono MaxQuant_1.6.3.4/MaxQuant/bin/MaxQuantCmd.exe --help
```

!!! Note 
    Please note that the MaxQuant version you used to create .xml parameter 
    configuration file must match with the version you use on linux environment 
    to smoothly run it on a cluster environment. Other latest versions may work.


 - Finally submit your script

Create a batch script according to the [instructions for shared memory jobs](../../../computing/running/creating-job-scripts-puhti#serial-and-shared-memory-batch-jobs) 
and make sure the script ends up in the same directory as your `mqpar.xml` 
file and other data files are located.

Just to facilitate writing your batch scripting process, you may use the following  
minimal example script (calles say, e.g., `maxquant.sh`), to start with: 

```bash
#!/bin/bash
#SBATCH --job-name=maxquant
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=project_xxx
#SBATCH --time=01:20:00
#SBATCH --ntasks=1
#SBATCH --partition=small
#SBATCH --cpus-per-task=6
#SBATCH --mem=16000

# load maxquant environment

module load bioconda
source activate maxquant

# adjust file paths here

mono /path_of_MaxQuant/bin/MaxQuantCmd.exe /path/MaxQuant/mqpar.xml

```
and then modify resource allocations depending on the number samples. Submit your script as below:

```bash
sbatch maxquant.sh
```

When `maxquant` job is finished, your output files will be in this same directory.

## Tutorial example

You can download example tutorial data for running MaxQuant as below:

```bash
wget https://a3s.fi/proteomics/MaxQuant_tutorial.tar.gz
```
and then untar the downloaded archive file as below:
```bash
tar -xavf  MaxQuant_tutorial.tar.gz
```

The tutorial has example raw files and other necessary files to run MaxQuant for testing.


## Look at the used resources once your job is finished

Once `maxquant` job is finished, you can check the utilization of computing resources
like [memory](../faq/how-much-memory-my-job-needs.md) and CPU usage efficiency.
This will help you tune with better parameters for efficient usage of computing resources.

You can use the following commands using job id:
```
seff <jobid>
sacct –l –j <jobid>
sacct -o jobid,jobname,maxrss,maxvmsize,state,elapsed -j <jobid>

```
