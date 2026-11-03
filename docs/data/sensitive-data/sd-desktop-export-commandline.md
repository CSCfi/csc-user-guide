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


Use the Data Gateway application via command line to import files from **SD Connect** and **SD Apply** (if you have the required access rights) to a volume attached to your virtual desktop.

#### Step 1: start the Data Gateway connection

Open the Data Gateway application by running:

```bash
data-gateway-cli import
```

This establishes a secure connection between your virtual desktop and **SD Connect** or SD Apply, where your files are stored encrypted. Now you will notice on the side navication bar that a folder called Project has been opened. 

#### Step 2:  View the contents of your SD Connect project

To see the files and folders available in your CSC project and stored in SD Connect, run:

```bash
ls $HOME/Projects/SD-Connect/project-number/
```

Replace `project-number` with your CSC project number.

## 3. Navigate to your virtual desktop volume

You can now make a working copy of the files stored in SD Connect inside your virtual desktop, specifically save them on the volume attached to it.

Volumes attached to the virtual desktop are mounted as `volume1`, `volume2`, etc.

If you have only one attached volume, navigate to it with:

```bash
cd /media/volume1
```

## 4. Copy files from SD Connect

You can copy files from SD Connect via the secure connection created by the Data Gatewaty to your virtual desktop volume. Files are automatically decrypted during the copy process.

Keep the Data Gateway application running until the file transfer is complete.

Example:

```bash
cp -r $HOME/Projects/SD-Connect/project-number/buckets/ .
```
Where: 

| Component | Description |
|------------|-------------|
| `cp` | Copy files or directories |
| `-r` | Copy directories and their contents recursively |
| `project-number` | Your CSC project number |
| `buckets` | The name of the bucket containing your files and folders in SD Connect |
| `.` | The current directory (your virtual desktop volume) |

Example:

```bash
cp -r $HOME/Projects/SD-Connect/project_2000XXX/experiment-04-10-2026/ .
```

## Import Files Only from SD Apply

If you only need to access data stored in **SD Apply**, run:

```bash
data-gateway-cli import -sdapply
```

## Exit the Data Gateway Application

To close the connection, press:

```text
Ctrl+C
```

## Notes

- Keep the Data Gateway application open while copying files.
- Files are available through the mounted `Projects` directory only while the secure connection is active.
- Files are automatically decrypted when copied to your virtual desktop volume.

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

# Export Files to SD Connect

Only the CSC Project Manager is authorized to export results from the virtual desktop using the Data Gateway application. Project members can import files but cannot export data.

Before exporting, open a terminal in the directory containing the file or folder you want to export.

## Export a Single File

Open a terminal in the directory containing the file or folder you want to export and use the following command to export a file to an SD Connect bucket:

```bash
data-gateway-cli export <SD-Connect-bucket-name> <file-name>
```

Example:

```bash
data-gateway-cli export study2026 results.csv
```
The file results.csv will be encrypted and exported to an SD Connect bucket named study2026. If the specified bucket does not already exist in SD Connect, it will be created automatically.
Once the export is complete, the file will be available to all members of your CSC project. Project members can then download the file through SD Connect to their own computers. The file is automatically decrypted during the download process.

## Export a Folder

To export a folder and all of its contents to an SD Connect bucket, use:

```bash
data-gateway-cli export <SD-Connect-bucket-name> <folder-name>
```

Example:

```bash
data-gateway-cli export study2026 results-november-2026
```

In this case, the directory called restuls-november-2026 will be exported to Sd Connect bucket named study 2026, with the entire content. All the files will be automatically encrypted. If the specified bucket does not already exist in SD Connect, it will be created automatically. Also in this case, once the export is complete, the file will be available to all members of your CSC project. Project members can then download the folder through SD Connect to their own computers. The file is automatically decrypted during the download process.

Command Explanation

| Component | Description |
|------------|-------------|
| `data-gateway-cli export` | Starts the export process |
| `SD-Connect-bucket-name` | Name of the destination bucket in SD Connect |
| `file-name` | File to be exported |
| `folder-name` | Folder to be exported, including all its contents |

## Notes

- Only CSC Project Managers can export data from the virtual desktop.
- Project members can import data but cannot perform exports.
- The export command uploads the selected file or folder to the specified SD Connect bucket.
- If the bucket does not exist, it is created automatically during the export process.
- Ensure you are in the correct directory before running the export command, or provide the full path to the file or folder.






* [Troubleshooting](./sd-desktop-troubleshooting.md)
    
