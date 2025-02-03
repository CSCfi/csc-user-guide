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

Add Puhti service to your project and contact CSC (sevicedesk@csc.fi) and request that Puhti access will be created for your SD Desktop environment. In this process a robot account will be create for your project and a project specific server process is launched for you project by CSC Puhti.

The job submission is done with command `sdsi-client`. This tool can be added to your SD desktop machine by installing `CSC Tools` with SD tool installer to your SD Desktop machine.

# Submitting jobs

## Data Upload

The batch josb submitted by sdsi-client read the input data from SD Connect service. Thus all the input data must be uploaded to SD Connect before the job is submitted. Note that you can't use data in the local disks of your SD Desktop virtual machine or unencrypted files as input files for your batch job. However, local files in Puhti can be used, if the access permissions allow all group members to use the data.

Thus the first step in constructing a sensitive data batch job is to upload the input data to SD Coonnect.

## Constructing a batch job file

When you submit a batch job from SD Desktop, you must define following information:

1. What files need be downloaded from SD Connect to Puhti to be used as input files
2. What commands will be executed
3. What data will be exported from Puhti to SD Connect when the job ends
4. How much resources (time, memory, temporary dick space ) the job needs.

You can define this thins in command line as _sdsi-client_ command options, but normally
it is more convenient to give this information a as batch job definition file. 
Below is a sample of a simple sdsi job definition file, named as job1.sdsi

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
sdsi-client status 1234
```

Aternatively, you can use this ID in *Puhti* with `sacct` command:

```text
sacct -j 123456
```

## Steps of processing

The task submitted with sdsi-client is transported to the batch job system of Puhti 
where it is processed among other batch jobs. The resource requirements for the batch job: computing time, memory, local disk size, GPUs, are 
set according to the values defined in the _sbatch:_ section in the job description file.

The actual computing and starts only when a suitable Puhti node is available. Queueing times may be long as 
the jobs always reserves one full node with sufficient local disk and memory.

The execution of the actual computing includes following steps:

   1. The input files, defined in the job description file, are downloaded and decrypted to the 
   local temporary disk space of the computing node.

   2. Commands defined is the _run:_ section are executed.

   3. Output files are encrypted and uploaded to SD Connect.

   4. Local temporary disk space is cleaned.


## Output

By default the exported files include standard output and standard error of the batch job (meaning the information
that in interactive working is written to to the terminal screen ) and files that moved in directory _$RESULTS_.


In SD Connect the results are uploaded to a bucket named as: sdhpc-results-project_number, in a subfolder named after the 
batch job ID. In the example above the project used was 2008749 and the job id was 123456. Thus the job would produce two
new files in SD Connect:

```txt
    sdhpc-results-2008749/123456/slurm.err.tar.c4gh
    sdhpc-results-2008749/123456/slurm.out.tar.c4gh
```
 You change the output bucket with sdsi-client option `-bucket bucket_name`. Note that the bucket 
 name must be uniq in this case too.


## Practicalities

The jobs that sdsi submits reserve one full Puhti node. These nodes have 40 computing cores 
so you should use these batch jobs only for tasks can utilize multiple computing cores. 
Preferably all 40.

In the previous example, the batch job the actual computing task consisted of calculating md5 
checksums for two files. The command used, `md5sum`, is able to use just one computing core so
the job waisted resources as 40 cores were reserved for the job but only one was used.

However if you need to calculate a large amount of unrelated tasks that are able to use only one 
or few computing cores, you can use tools like gnuparallel, nextfllow or snakemake to submit several
computing tasks to be executed in the same time.

In the example below we have a tar file that has been stored to SD Connect: 2008749-sdsi-input/data_1000.tar.c4gh.
The tar file contains 1000 files for which we want to compute md5sum. Now the batch job could look like
following:


```text
data:
  recv:
  - 2008749-sdsi-input/data_1000.tar.c4gh
run: |
  source /appl/profile/zz-csc-rnv.sh
  module load parallel
  tar xf 2008749-sdsi-input/data_1000.tar
  ls  2008749-sdsi-input/data_1000  | parallel -j 40 md5sun
sbatch:
- --time=04:00:00
- --partition=small
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

The tools for running backup process are not by default installed in SD Desktop Virtual Machines. Thus, the first step is that the 
manager installs the **SD Backup tool** package using the [SD Software installer](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer)

Log in to your SD Desktop and open **Data Gateway**. If the software installation help tools are enabled for your project, then you should have folder: 
`tools-for-sd-desktop` included in the directory that Data Gateway created (in `Projects/SD-Connect/your-project-name`). If you don't find `tools-for-sd-desktop` 
directory through Data Gateway **send a request to [CSC Service Desk](../../../support/contact.md)**. In the request, indicate that you wish that the SD Desktop software installation help tools would 
be made available for your project. You must also include to the message the **Project identifier string** of your project.
You can check this random string for example in the [SD Connect service](https://sd-connect.csc.fi). There you find the 
Project Identifier in the **User information** view.

Open `tools-for-sd-desktop` folder and from there, drag/copy file `sd-installer.desktop` to your desktop.

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](../images/desktop/sd-installer1.png)

**Figure 1.** Copying `sd-installer.desktop` file to SD desktop.
 
Double-click the copy of `sd-installer.desktop` to start the software installation tool. Use this tool to install _SD Backup_ tool
to your SD Desktop virtual machine if you have not yet done so. 

## Project Mangers Starts backup server

When the SD Backup tool is installed, the Project Manager should start a new terminal session and there start a virtual terminal session with command:

```text
screen
```

and then launch the backup process with command:

```text
sd-backup-server.sh
```

When launched, `sd-backup-server.sh` asks for the CSC password of the Project Manager.

After that the project manager can leave the virtual session running in background by pressing:
`Ctrl+a+d`.

This way the `sd-backup-server.sh` command remains active in the virtual terminal session even when the connection to SD Desktop is closed.

The actual server process is very simple. It checks the content of the backup directory once in a minute and moves the contents of this directory 
to a bucket in SD Connect. The data is encrypted with CSC public key so that the backups can be used only in SD Desktop environment.
The default backup directory is `/shared-data/auto-backup` and target bucket in SD Connect is `sdd-backup-<virtual-machine-name>`. 

Note that the server is not able to check if the given password was correct. If a wrong password was given then backup requests will fail. 
Thus, it may be good to test the backup process once the server is running.

## Doing backups

When the backup server is running, all users of the VM can use command `sd-backup` to make a backup copy of the dataset to SD Connect.
The syntax of the `sd-backup` command is:

```text
sd-backup file.csv
```

or

```text
sd-backup directory
```

The command copies the given file or directory to the backup directory from where the server process is able to move it to SD Connect.
In SD Connect a timestamp is added to the file name in order to make the file name unique. In addition, a metadata file is
created. This file contains information about the user who requested the backup, original host and location of the file. If backup is done for 
a directory, then the content of the directory is stored as one tar-archive file and the metadata file will contain list of the backed-up files. 
 
For example, for a file called `my_data.csv` that locates in SD Desktop virtual machine called `secserver-1683868755`, a backup command:

```text
sd-backup  my_data.csv
```

Will create a backup file that will be available through Data Gateway in path:

```text
Projects/SD-Connect/project_number/sdd-backup-secserver-1683868755/my_data.csv-2023-05-15-07:41
```

Note that you have to refresh the Data Gateway connection in order to see the changes in SD Connect.
