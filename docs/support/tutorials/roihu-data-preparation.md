# Preparing data for Roihu: moving data from Mahti and Puhti to Allas or LUMI-O

This tutorial explains how to temporarily move data from Mahti or Puhti to object storage before Roihu is generally available.

This may be useful if your research group cannot wait until Roihu is available, for example because key project members will be unavailable during the period between Roihu general availability and the shutdown of Mahti and Puhti storage servers.

The recommended temporary storage options are:

- **A:** Allas, if your CSC project has enough available Allas quota
- **B:** LUMI-O, if you have a project that has access to LUMI-O, and enough available storage quota there

After Roihu becomes available, you can copy the data from Allas or LUMI-O to Roihu.

!!! warning "Note"
     Your primary approach in data migration from Mahti and Puhti to Roihu
     should be a direct copy from one machine to the other.
     Only utilize Allas or LUMI-O, if you cannot manage data
     transfers between Roihu availability and Mahti/Puhti storage
     shutdown.

## When should you use this tutorial?

Use this tutorial if:

- you have data on Mahti or Puhti that must be preserved before the storage servers are shut down (end of August 2026)
- you cannot wait until Roihu is generally available before starting the transfer (End of June 2026)
- you need temporary object storage for the transition period
- your data does not need to remain on a POSIX filesystem during the transition

Do not use this tutorial as a reason to move everything automatically. Before transferring data, **review what you actually need to keep**.

## Before you start

### 1. Clean up your data

Only move data that you still need. In particular, avoid transferring:

- temporary files
- cache directories
- intermediate results that can be recomputed
- old log files
- unnecessary checkpoint files
- duplicate datasets
- software installations and executables that should be rebuilt on Roihu

For large directories, check the data volume before transferring. On CSC supercomputers, prefer tools intended for
checking disk usage (e.g. LUE) instead of running heavy recursive commands on large directory trees.

??? info "How to check disk usage on a directory"
     We recommend using the LUE tool to identify where you have lots of data. Avoid using tools such as `du` as they may cause a lot of load on the file  system. Simple usage example (run `lue -h` for other options):
     ```
     module load lue
     lue <directory-to-analyze>
     ```

### 2. Choose the target storage service

Choose **Allas** if:

- your CSC project already has Allas access
- the amount of data is moderate (~1 TB)
- your project has enough available Allas quota

Choose **LUMI-O** if:

- you have a project that has LUMI-O access
- you need object storage for a larger amount of data (> 10 TB)
- your group is already using LUMI or can apply for suitable access

Allas and LUMI-O are object storage services. They are useful for storing and transferring data during the transition to Roihu, but they are not replacements for /scratch or /projappl.

Object storage works best for data that can be uploaded and downloaded as complete files or archive packages.
It is not suitable for storing full software installations, or working with large numbers of frequently changing small files.

### 3. Consider packaging many small files

If you have many small files, transferring and accessing them in an object storage service one by one can be slow and inefficient.
Consider creating archive files before upload.

For example:

```bash
cd /scratch/project_2000000/mydata
tar -czf dataset-2025-08-01.tar.gz dataset/
```

Then transfer the archive file instead of the full directory tree.

Keep the original directory until you have verified that the uploaded archive can be downloaded and unpacked successfully.

## Option A: Move data from Puhti or Mahti to Allas

### 1. Log in to Puhti or Mahti

Log in to the system where your data is currently stored. E.g. to Puhti:

```bash
ssh <username>@puhti.csc.fi
```

### 2. Configure Allas access

Load the Allas module and configure access:

```bash
module load allas
allas-conf
```

This configures the default Swift-based Allas connection for the selected CSC project. In `rclone` commands, this connection is usually referred to as:

```text
allas:
```

If you specifically need S3 access to Allas, configure Allas in S3 mode instead:

```bash
module load allas
allas-conf --mode S3
```

With S3 mode, the `rclone` remote is usually:

```text
s3allas:
```

Avoid mixing Swift and S3 access for the same objects. If you upload data using `allas:`, use `allas:` for later operations on that data as well.

### 3. Create a bucket

Choose a bucket name that includes your project number or another project-specific identifier. Bucket names must be unique.

Example (replace project-2000000 as your project ID):

```bash
rclone mkdir allas:project-2000000-roihu-transfer
```

### 4. Copy data to Allas

To copy a single file:

```bash
rclone copy dataset-2025-08-01.tar.gz allas:project-2000000-roihu-transfer/
```

To copy a directory:

```bash
rclone copy /scratch/project_2000000/mydata allas:project-2000000-roihu-transfer/mydata
```

Use `copy` rather than `move` for the first transfer. This keeps the original data on Mahti or Puhti until you have verified that the upload succeeded.

### 5. Check the uploaded data

List the bucket contents:

```bash
rclone lsf allas:project-2000000-roihu-transfer/
```

For a more detailed listing:

```bash
rclone ls allas:project-2000000-roihu-transfer/
```

You can also compare source and destination:

```bash
rclone check /scratch/project_2000000/mydata allas:project-2000000-roihu-transfer/mydata
```

For large transfers, consider writing the output to a log file:

```bash
rclone copy /scratch/project_2000000/mydata allas:project-2000000-roihu-transfer/mydata \
  --progress \
  --log-file roihu-transfer-to-allas.log
```

## Option B: Move data from Puhti or Mahti to LUMI-O

TBA

## Running long transfers safely

Large transfers may take a long time. Do not run them in a normal SSH session without protection, because the transfer may stop if the connection is interrupted.

Use `screen` or `tmux`, for example, in a session in Puhti/Mahti:

```bash
tmux new -s roihu-transfer
```

Start the transfer inside the `tmux` session. You can detach from the session with:

```text
Ctrl-b d
```

Later, reconnect with:

```bash
tmux attach -t roihu-transfer
```

## Downloading data later to Roihu

After Roihu is available, log in to Roihu and configure access to the object storage service that contains your data, following
instructions that will be provided in the [tutorial for using Allas in CSC supercomputers](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/data/Allas/allas-hpc/).
The approach is very similar to Mahti and Puhti

Then copy the data from object storage to the appropriate Roihu disk area.

On Roihu, check which available buckets your project has in Allas with `rclone lsd`:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ rclone lsd allas:
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
```

Copy the appropriate data to your directory on Roihu:

```bash
rclone copy allas:project-2000000-roihu-transfer/mydata /scratch/project_2000000/mydata
```

After copying the data to Roihu, verify the transfer:

```bash
rclone check allas:project-2000000-roihu-transfer/mydata /scratch/project_2000000/mydata
```

If you uploaded compressed archive files, unpack them only after confirming that the archive was transferred successfully:

```bash
tar -tzf dataset-2025-08-01.tar.gz
tar -xzf dataset-2025-08-01.tar.gz
```

## Important notes

### Do not delete the original data too early

Keep the original data on Mahti or Puhti until:

- the upload has completed
- the uploaded data has been checked
- the data is no longer needed on Mahti or Puhti

### Be careful with `rclone sync`

`rclone sync` makes the destination match the source. This means it can delete files from the destination. Use `rclone copy` unless you are sure that synchronization is needed.

If you use `sync`, first run a dry run:

```bash
rclone sync /scratch/project_2000000/mydata allas:project-2000000-roihu-transfer/mydata --dry-run
```

### Object storage is not a working directory

Allas and LUMI-O are suitable for storing, staging, sharing, and transferring data. They are not replacements for scratch or project directories on a supercomputer.

Do not run applications directly against object storage as if it were a normal filesystem.

### Protect sensitive data

Do not upload sensitive data unless the storage service and your project’s data management plan allow it. If needed, encrypt data before uploading.

### Document what was moved

Create a small README file and upload it with the data. For example:

```text
Dataset: Example simulation outputs
Original location: /scratch/project_2000000/example
Source system: Puhti
Uploaded by: <name>
Upload date: YYYY-MM-DD
Temporary storage: Allas bucket project-2000000-roihu-transfer
Intended destination: Roihu /scratch/project_2000000/example
Notes:
```

Upload the README:

```bash
rclone copy README-roihu-transfer.txt allas:project-2000000-roihu-transfer/
```

or:

```bash
rclone copy README-roihu-transfer.txt lumi-46XXXXXXX-private:roihu-transfer/
```