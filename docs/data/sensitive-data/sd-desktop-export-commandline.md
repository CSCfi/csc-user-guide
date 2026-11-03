[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Programmatic data import and export in the virtual desktop

The virtual desktop is an isolated environment with no direct internet access. The only way to import data for analysis or exports results from the secure environment is through the Data Gateway application, which is available also via the command line.

Any project remember can import files using stored in from SD Connect or SD Apply via Data Gateway. The imported files are automatically decrypted.

Only the CSC Project Manager is authorized to export files from the virtual desktop. Exported files are automatically encrypted and transferred to SD Connect, where any project members can access and download them. 

On this page:

[1. Importing a working copy of the dataset on the external volume](#1-importing-a-working-copy-of-the-dataset-on-the-external-volume)

[2. Set correct permissions](#2-set-correct-permissions)
   
[3. Data analysis via Byobu terminal](#3-data-analysis-via-byobu-terminal)

[4. Exporting results](#4-exporting-results)


## 1. Importing a working copy of the dataset on the external volume


Use the following command to import files from both **SD Connect** and **SD Apply** (if you have the required access rights) to your virtual desktop external volume: 

 First, you need to open the data Gateway application programmatically and type:

```bash
data-gateway-cli import
```

Now the secure connection between SD Connect and your virtual desktop is open. List the content of the project folder with this command to see the files and folder you have stored in SD Connect: 


```bash

$HOME/Projects/SD-Connect/project-number/
```


Now change directory and move to your virtual desktop volume, the volumes attached to the virtual desktop are listed as numbers, so if you have only one volume you can access it via volume1: 

```bash

cp /media/volume1
```

Now you can copy the files stored in SD Connect visible to you via the Projects folder to the volume. During the copying pahe they wil also be decrypted. Leave teh data agteway applcaiiton open during this time. 

```bash

cp -r  $HOME/Projects/SD-Connect/project-number/buckets/ .
```


Where: 

cp means copy
-r means the entire file or directory
project-number is the CCS project number
bucket is the bucket in SD Connect in which you have uplaoded files or folders


cp -r $HOME/Projects/SD-Connect/project-2000XXX/experiment-04-10-2026/ .



To import files exclusively from **SD Apply**:

```bash
data-gateway-cli import -sdapply
```


To exit the application, press:

```text
Ctrl+C
```

## 2. Set correct permissions

After copying files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only.

With the steps below, you ensure that all project members have read and write access to all files and folders. This prevents possible access issues when the volume is used on different virtual desktop, where file ownership information may be handled differently.


1. If you haven't **SD Tools installer** already installed on your virtual desktop, follow these [instructions (Steps 1-2)](./sd-desktop-software.md#step-1-send-a-request).
2. Launch **SD Tools installer**. Remember that you've to have **Data Gateway** application open for it to work.
3. Install **CSC Tools** by clicking corresponding button. Wait for confirmation.
![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_CSCTools_1.png)

4. Open terminal from to left side of the desktop. Type in `pre-volume-detach`. This command fixes the access permissions. 
![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_CSCTools_2.png)
6. Next, the command tells if there are other project members who should run this command as well. You should inform them if this happens. 
7. You are then asked whether you want to make a backup copy of your home directory to the volume, allowing you to import its contents to the new virtual machine. Type y or n (Yes/No).
8. Next, the command asks whether you want to make a backup copy of your shared directory, which contains software installations. Type y or n (Yes/No). 


## 3. Data analysis via Byobu terminal 

The virtual desktop includes the Byobu terminal, which provides a persistent command-line environment for running data analysis tasks. Byobu is particularly useful for long-running jobs, as processes continue running even if log out from the virtual desktop unlike standard shell session. 

Common use cases include:

- Running Python, R, or shell scripts on large datasets.
- Executing computationally intensive analyses that may take several hours or days.
- Monitoring job progress without keeping the terminal window active.
- Working with multiple terminal sessions simultaneously using Byobu's session management features.

Byobu allows you to log out from a session and reconnect later, making it a reliable option for batch processing, data preparation, machine learning workloads, and other long-running analyses compared to shell. 


## 4. Exporting results

Only the CSC Project Manager is authorized to export results from the virtual desktop via the data gateway. Project members can import files but cannot export data.

Open the terminal in the same location in which the files that you want to export are and then type: 

With this command you can create a bucket in SD Connect in which yow want to export a single file:

```bash
data-gateway-cli export <SD Connect bucket name> <file you want to export>
```
 example

```bash
data-gateway-cli export study2026 results.csv
```

With this command you can create or specific the name of the bucket in SD Connect in which yow want to export a folder and all its content: 

```bash
data-gateway-cli export <SD Connect bucket name> <folder you want to export>
```


```bash
data-gateway-cli export study2026 results_directory
```






* [Troubleshooting](./sd-desktop-troubleshooting.md)
    
