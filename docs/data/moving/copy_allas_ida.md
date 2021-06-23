# Copying data between Allas and IDA via Puhti

## Copying data from Allas to IDA via Puhti

In order to be able to copy data from Allas to IDA with this procedure, you need to be a member in a project which has IDA and Puhti services in use. On the Allas side, you need at least read access to the data. You either need to be a member in a project which has Allas service in use, or the data in question needs to be open for download in Allas. Note that the projects in Allas, Puhti and IDA do not need to be the same.

In short, there are four steps to follow

 1 download the data from Allas to Puhti scratch
 2 rearrange the data in the scratch
 3 upload the data to IDA and describe it
 4 clean the Puhti scratch

### Step 1. Download the data from Allas to Puhti scratch

Scratch disk area in Puhti is recommended as it is by default much larger than other areas, like user's home area. Also you can request even bigger scratch quota if the default is not enough. For more datails about Puhti disk areas see [Computing disk environment](../../computing/disk.md)

An example how to create a new directory copydir for the data under project 2000013's scracth area:
```text
mkdir /scratch/project_2000013/copydir
```

Download the data from Allas to that new directory. You should use the same protocol as was used to originally upload the data to Allas, and if the data was uploaded with command line tools, preferably also using the same command line tool. More information about the tools in Puhti is at [Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas/#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms)

In our example case the data was originally uploaded to Allas with a-commands, so the user uses a-get to download the data:
```text
module load allas
allas-config
cd /scratch/project_2000013/copydir
a-get 2000013-wrk-bucket/working_data.tar.zst
```
a-get command downloads the data and unpacks it in to the copydir directory.

### Step 2. Rearrange the data in the scratch

This is an important step when copying data from Allas to IDA. You should only copy data that is important enough to be described as dataset in Fairdata services. Also it makes the rest of the procedure easier to think at this point what kind of a directory structure would be good for the datasets, and arrange the data in the Puhti directory to follow that structure. In case you will include some files to more the one dataset, do not make duplicate files, IDA files may belong to more than one dataset.

In our example case, the project decides that it makes sense to have two distict dataset and the data is rearranged in to two directories, experiment_a and survey_2021.

### Step 3. Upload the data to IDA and describe it

You should only copy data that is important enough to be described as datasets in Fairdata services. Also you shoud have the data already arraged to a directory structure that would be good for the datasets.

This step is actually three substeps

 1 uploading
 2 freezing
 3 describing the datasets

You can upload the data using IDA command line tool:
<pre>ida upload <em>target_in_ida local_file</em>
</pre>
Continuing our example, uploading both directories (experiment_a and survey_2021) in to project 2000002:
```text
module load ida
cd /scratch/project_2000013/copydir
ida upload -p 2000002 experiment_a experiment_a
ida upload -p 2000002 survey_2021 survey_2021
```
If the user has used an configured the IDA command line tool, then the download command uses that configuration. If not, the the download command asks the username and password in IDA. Detailed instructions can be found in [IDA command line tool](../ida/using_ida/#configuring-and-using-ida-in-csc-supercomputers).

Before you can use Fairdata tools to describe the data as datasets, the data needs to be frozen in IDA. Freezing action makes the data read only and it can be done in the IDA browser user interface [https://www.fairdata.fi/en/user-guides/user-guide/#freezing-files](https://www.fairdata.fi/en/user-guides/user-guide/#freezing-files).

Dataset descriptions can be done either with Fairdata Qvain tool [https://www.fairdata.fi/en/qvain/](https://www.fairdata.fi/en/qvain/), or with Fairdata Metax API [https://www.fairdata.fi/en/metax/apis/](https://www.fairdata.fi/en/metax/apis/).

### Step 4. Clean the Puhti scratch

Data in the Puhti scratch consumes billing units, so once the data is uploaded to IDA and if you are not going to use it in Puhti, it makes sense to remove it from the scratch disk area in Puhti.

## Copying data from IDA to Allas via Puhti

In order to be able to copy data from IDA to Allas with this procedure, you need to be a member in a project which has Allas and Puhti services in use. On the IDA side, you either need to be a member in a project which has IDA service in use, or the data in question needs to be open for download. Note that the projects in Allas, Puhti and IDA do not need to be the same.

In short, there are four steps to follow

 1 download the data from IDA to Puhti scratch
 2 rearrange the data in the scratch, if necessary
 3 upload the data to Allas
 4 clean the Puhti scratch, if necessary

### Step 1. Download the data from IDA to Puhti scratch

Scratch disk area is recommended as it is by default much larger than other areas, like user's home area. Also you can request even bigger scratch quota if the default is not enough. For more datails about Puhti disk areas see [Computing disk environment](../../computing/disk.md)

An example how to create a new directory xferdir for the data under project 2000012's scracth area:
```text
mkdir /scratch/project_2000012/xferdir
```

If the data to be downloaded from IDA is in a project the user belongs to, then downloading the data from IDA can be done with IDA's command line tool:
<pre>ida download <em>target_in_ida local_file</em> 
</pre>
Continuing our example, the data in IDA is in project 2000001's directory testi, download commands are:
```text
module load ida
cd /scratch/project_2000012/xferdir
ida download -p 2000001 testi testi.zip
```
The last argument in the download command is the file name to be created in puhti, and in this case as a directory is downloaded, it will be downloaded as a zip package. If the user has used an configured the IDA command line tool, then the download command uses that configuration. If not, the the download command asks the username and password in IDA. Detailed instructions can be found in [IDA command line tool](../ida/using_ida/#configuring-and-using-ida-in-csc-supercomputers).

If the data to be downloaded from IDA is a published open dataset visible in Fairdata Etsin, then downloading it requires two steps, locating and copying the download command in Etsin and then downloading the dataset. Download button in Etsin has option to show download commands for a few command line tools.

Again continuing our example, the user selects a dataset directory for downloading in Etsin. After a while the zip package is ready and Etsin shows the download button:

User selects the option menu to see command line options:

User copies the curl command and runs it in puhti:
```text
module load ida
cd /scratch/project_2000012/xferdir
curl -fOJ "https://ida191.csc.fi:4430/download?token=18f6e5b7edae4f12a8a654ea22d57aa9.PA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3G_e3668097e34d437484e15d53624e7905=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76&package=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip"
```

### Step 2. Rearrange the data in the scratch, if necessary

In case you would like to rearrange the data, or remove parts of it, you can do it in the scratch before you upload it to Allas.

Continuing our example, once the data is in a testi.zip (or 76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip in case of an open dataset) in the project's scratch area, the package can simply be unpacked with unzip:
```text
cd /scratch/project_2000012/xferdir
unzip testi.zip
```

### Step 3. Upload the data to Allas

The easiest way to upload the data to Allas is using a-put command. a-put uploads a directory as one compressed obejct in to Allas. It needs enough space at the working directory to create the package to upload, so the currenct working directory should be the scartch area. The basic syntax of the a-put command:
```text
a-put directory_or_file
```
More information about the tools in Puhti is at [Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas/#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms)

Continuing our example, the unzipped data to be uploaded to Allas is in a directory experiment_data, it can be uploaded with a-put:
```text
module load allas
allas-config
cd /scratch/project_2000012/xferdir
a-put experiment_data
```

### Step 4. Clean the Puhti scratch

Data in the Puhti scratch consumes billing units. If you are not going to need the data in Puhti, once the data is uploaded to Allas it may make sense to remove it from the scratch disk area in Puhti.

