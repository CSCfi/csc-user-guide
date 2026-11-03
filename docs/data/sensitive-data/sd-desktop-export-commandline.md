[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Programmatic data import and export in the virtual desktop

The virtual desktop is an isolated environment with no direct internet access. The only way to import data for analysis or exports restuls fromt eh secure environment is through the Data Gateway application, which is available also via the command line.

Any project remember can import files using stored in from SD Connect or SD Apply via Data Gateway. The imported files are automatically decrypted.

Only the CSC Project Manager is authorized to export files from the virtual desktop. Exported files are automatically encrypted and transferred to SD Connect, where any project members can access and download them. 

On this page:

[1. Importing a working copy of the dataset on the external volume](#1-importing-a-working-copy-of-the-dataset-on-the-external-volume)

[2. Set correct permissions](#2-set-correct-permissions)
   
[3. Data analysis via Byobu terminal](#3-data-analysis-via-byobu-terminal)

[4. Results export](#4-exporting-restuls)


## 1. Importing a working copy of the dataset on the external volume


Use the following command to import files from both **SD Connect** and **SD Apply** (if you have the required access rights) to your virtual desktop external volume: 

```bash
data-gateway-cli import
```


To import files exclusively from **SD Apply**:

```bash
data-gateway-cli import -sdapply
```

If new files have been added to SD Connect, refresh the Data Gateway session by entering:

```bash
update
```

and pressing **Enter**.


To exit the application, press:

```text
Ctrl+C
```

## 2. Set correct permissions

When the data import has completed, please set correct access rights or permissions


## 3. Data analysis via Byobu terminal 

The virtual desktop includes the Byobu terminal, which provides a persistent command-line environment for running data analysis tasks. Byobu is particularly useful for long-running jobs, as processes continue running even if log out from the virtual desktop unlike standard shell session. 

Common use cases include:

- Running Python, R, or shell scripts on large datasets.
- Executing computationally intensive analyses that may take several hours or days.
- Monitoring job progress without keeping the terminal window active.
- Working with multiple terminal sessions simultaneously using Byobu's session management features.

Byobu allows you to log out from a session and reconnect later, making it a reliable option for batch processing, data preparation, machine learning workloads, and other long-running analyses comaptred to shell. 


## 4. Exporting results

Only the CSC Project Manager is authorized to export results from the virtual desktop via the data gateway. Project members can import files but cannot export data.

Export a File

```bash
data-gateway-cli export <bucket> <file>
```
 example

```bash
data-gateway-cli export study2026 results.csv
```

Export a Directory

```bash
data-gateway-cli export study2026 results_directory
```






* [Troubleshooting](./sd-desktop-troubleshooting.md)
    
