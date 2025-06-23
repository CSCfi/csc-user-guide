# Submitting jobs from SD Desktop to the HPC environment of CSC

The limited computing capacity of a SD Desktop virtual machine can prevent running heavy analysis tasks
for sensitive data. This document describes, how heavy compting tasks can be submitted form SD Desktop
to the Puhti HPC cluster.

Please note following details that limit the usage of this procedure:
   * You have to contact servicedesk@csc.fi the enable the job submission tools for your project. By default the job submission tools don't work.
   * Each jobs reserves always one, and only one, full Puhti node for your task. Try to construct your batch job so that it uses effectively all the 40 computing cores of one Puhti node.
   * The input files that the job uses must be uploaded to SD Connect before the job submission. Even though the job is submitted from SD Desktop, you can't utilize any files from the SD Desktop VM in the batch job.
   * The jobs submitted from SD Desktop to Puhti have higher security level that normal Puhti jobs but lower than that of SD Desktop.  


# Getting stared 

Add Puhti service to your project and contact CSC (sevicedesk@csc.fi) and request that Puhti access will be created for your SD Desktop environment. In this process a robot account will be created for your project and a project specific server process is launched for you project by CSC Puhti.

The job submission is done with command `sdsi-client`. This tool can be added to your SD desktop machine by installing `CSC Tools` with [SD tool installer](../sd-desktop-software.md/#customisation-via-sd-software-installer) to your SD Desktop machine.

# Submitting jobs

## Data Upload

The batch josb submitted by sdsi-client read the input data from SD Connect service. Thus all the input data must be uploaded to SD Connect before the job is submitted. Note that you can't use data in the local disks of your SD Desktop virtual machine or unencrypted files as input files for your batch job. However, local files in Puhti can be used, if the access permissions allow all group members to use the data.

Thus the first step in constructing a sensitive data batch job is to upload the input data to SD Connect.

## Constructing a batch job file

When you submit a batch job from SD Desktop, you must define following information:

1. What files need be downloaded from SD Connect to Puhti to be used as input files
2. What commands will be executed
3. What data will be exported from Puhti to SD Connect when the job ends
4. How much resources (time, memory, temporary dick space ) the job needs.

You can define this thins in command line as _sdsi-client_ command options, but normally
it is more convenient to give this information as a batch job definition file. 
Below is a sample of a simple sdsi job definition file, named as _job1.sdsi_

```text
data:
  recv:
  - 2008749-sdsi-input/data1.txt.c4gh
  - 2008749-sdsi-input/data2.txt.c4gh
run: |
  md5sum 2008749-sdsi-input/data1.txt
  md5sum 2008749-sdsi-input/data2.txt
sbatch:
- --time=00:15:00
- --partition=test
```

More sdsi batch job examples can be found below

## Submitting the job

The batch job defined in the file can be submitted with command 

```text  
sdsi-client new -input job1.sdsi
```
The submission command will ask for your CSC password, after which it prints you the ID number of the job.
You can use this ID number to check the status of your job. For example for job 123456 you can check the status
in *SD Desk desktop* with command:

```text
sdsi-client status 123456
```

Alternatively, you can use this ID in *Puhti* with `sacct` command:

```text
sacct -j 123456
```

## Steps of processing

The task submitted with sdsi-client is transported to the batch job system of Puhti 
where it is processed among other batch jobs. The resource requirements for the batch job: computing time, memory, local disk size, GPUs, are 
set according to the values defined in the _sbatch:_ section in the job description file.

The actual computing starts only when a suitable Puhti node is available. Queueing times may be long as 
the jobs always reserves one full node with sufficient local disk and memory.

The execution of the actual computing includes following steps:

   1. The input files, defined in the job description file, are downloaded and decrypted to the 
   local temporary disk space of the computing node.

   2. Commands defined is the _run:_ section are executed.

   3. Output files are encrypted and uploaded to SD Connect.

   4. Local temporary disk space is cleaned.


## Output

By default the exported files include standard output and standard error of the batch job (meaning the information
that in interactive working is written to the terminal screen ) and files that moved in directory _$RESULTS_.


In SD Connect the results are uploaded to a bucket named as: *sdhpc-results-*_project_number_, in a subfolder named after the 
batch job ID. In the example above the project used was 2008749 and the job id was 123456. Thus the job would produce two
new files in SD Connect:

```txt
    sdhpc-results-2008749/123456/slurm.err.tar.c4gh
    sdhpc-results-2008749/123456/slurm.out.tar.c4gh
```
 You can change the output bucket with sdsi-client option `-bucket bucket_name`. Note that the bucket 
 name must be unique in this case too.


## Running serial jobs effectively

The jobs that sdsi-client submits reserve always one full Puhti node. These nodes have 40 computing cores 
so you should use these batch jobs only for tasks that can utilize multiple computing cores. 
Preferably all 40. 

In the previous example, the actual computing task consisted of calculating md5 
checksums for two files. The command used, `md5sum`, is able to use just one computing core so
the job waisted resources as 40 cores were reserved but only one was used.

However if you need to calculate a large amount of unrelated tasks that are able to use only one 
or few computing cores, you can use tools like _gnuparallel_, _nextfllow_ or _snakemake_ to submit several
computing tasks to be executed in the same time.

In the examples below we have a tar-arcvive file that has been stored to SD Connect: `2008749-sdsi-input/data_1000.tar.c4gh`.
The tar file contains 1000 text files (_.txt_) for which we want to compute md5sum.  Bellow we have three alternative ways to run the tasks so that all 40 cores are effectively used.
 
### GNUparallel

In the case of GNUparallel based parallelization the workflow could look like 
following:

```text
data:
  recv:
  - 2008749-sdsi-input/data_1000.tar.c4gh
run: |
  source /appl/profile/zz-csc-env.sh
  module load parallel
  tar xf 2008749-sdsi-input/data_1000.tar
  cd  data_1000
  ls *.txt  | parallel -j 40 md5sum {} ">" {.}.md5
  tar -cvf md5sums.tar *.md5
  mv md5sums.tar $RESULTS/
sbatch:
- --time=04:00:00
- --partition=small
```

In the sample job above, the first command, `source /appl/profile/zz-csc-env.sh` is used to add 
_module_ command and other Puhti settings to the execution environment.
GNUparallel is enabled with command `module load parallel`.
Next the tar file containing 1000 files is extracted to the temporary local disk area.
Finally, the file listing of the .txt filesmin the extracted directory is guided to `parallel` command that runs 
the given command, `md5sum`, for each file (_{}_) using 40 parallel processes (`-j 40`).

### nextfllow

If we want to use NextFlow we must first upload a NextFlow task file (_md5sums.nf_ in this case) to SD Connect. 
This file defines the input files to be processed, commands to be executed and outputs to be created. 
Note that you can't upload this file to the SD Connect form SD Desktop, but you must upload it for 
example from your own computer or from Puhti.

Content of NextFlow file _md5sums.nf_

```text
nextflow.enable.dsl=2

process md5sum {
    tag "$filename"
    
    input:
        path txt_file from files("*.txt")
    
    output:
        path "${txt_file}.md5"
    
    script:
        """
        md5sum $txt_file > ${txt_file}.md5
        """
}

workflow {
    md5sum()
}
```
The actual sdsi job file could look like this:

```text
data:
  recv:
  - 2008749-sdsi-input/md5sums.nf.c4gh
  - 2008749-sdsi-input/data_1000.tar.c4gh
run: |
  source /appl/profile/zz-csc-env.sh
  module load nextflow
  tar xf 2008749-sdsi-input/data_1000.tar
  cp 2008749-sdsi-input/md5sums.nf data_1000
  cd data_1000
  nextflow run md5sums.nf -process.executor local -process.maxForks 40
  tar -cvf md5sums.tar *.md5
  mv md5sums.tar $RESULTS/
  
sbatch:
- --time=04:00:00
- --partition=small
```


### SnakeMake

If we want to use SnakeMake we must first upload a SnakeMake job file (_md5sums.snakefile_ in this case) to SD Connect. 
This file defines the input files to be processed, commands to be executed and outputs to be created. 
Note that you can't upload this file to the SD Connect form SD Desktop, but you must upload it for 
example from your own computer or from Puhti.

Content of SnakeMake file _md5sums.snakefile_

```text
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]

rule all:
    input:
        expand("{file}.md5", file=txt_files)

rule md5sum:
    input:
        "{file}"
    output:
        "{file}.md5"
    shell:
        "md5sum {input} > {output}"
```

The actual sdsi job file could look like this:

```text
data:
  recv:
  - 2008749-sdsi-input/md5sums.snakefile.c4gh
  - 2008749-sdsi-input/data_1000.tar.c4gh
run: |
  source /appl/profile/zz-csc-env.sh
  module load snakemake
  mkdir snakemake_cache
  export SNAKEMAKE_OUTPUT_CACHE=$(pwd)"/snakemake_cache"
  tar xf 2008749-sdsi-input/data_1000.tar
  cp 2008749-sdsi-input/md5sums.snakefile data_1000
  cd data_1000
  snakemake --cores 40 --snakefile md5sums.snakefile
  tar -cvf md5sums.tar *.md5
  mv md5sums.tar $RESULTS/
  
sbatch:
- --time=04:00:00
- --partition=small
```

### GPU computing

In the next example, GPU computing are used to speed up whisper speech recognition tool that
the user has installed to her own python virtual environment in Puhti.


```text
data:
  recv:
  - 2008749-sdsi-input/interview-52.mp4.c4gh
run: |
  source /appl/profile/zz-csc-rnv.sh
  module load pytorch
  source /projappl/project_2008749/whisper-python/bin/activate
  whisper --model medium 2008749-sdsi-input/interview-52.mp4 --threads 40
sbatch:
- --time=01:00:00
- --gres=gpu:v100:1
```



```
data:
  recv:
  - sdsi-poc/rand1.c4gh
  - sdsi-poc/rand2.c4gh
  send:
  - from: /dev/shm/slurm.err
    to: subfolder
  - from: /dev/shm/slurm.out
    to: another_folder
bucket: results_bucket
run: cat sdsi-poc/rand1 sdsi-poc/rand2
time-limit: 00:15:00
queue: test
```






txt
data:
  recv:
  - 2008749-data/data1.txt.c4gh
run: |
  md5sum 2008749-data/data1.txt



```


```txt
data:
  recv:
  - 2008749-data/genotype_1.fam.c4gh
  - 2008749-data/genotype_1.bim.c4gh
  - 2008749-data/genotype_1.bed.c4gh
run: |
   source /appl/profile/zz-csc-env.sh
   module load plink/1.90b7.2
   pli
```
