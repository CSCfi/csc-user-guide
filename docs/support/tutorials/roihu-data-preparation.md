# Preparing data for Roihu: Data management and temporary storage options

!!! warning "This tutorial is deprecated"
     This tutorial was in use before Roihu became generally available, for preparing
     for Roihu data migration, and for using Allas or LUMI-O during the transfer
     if strictly needed.

     Now that Roihu is available for use, please follow instead the
     [Roihu data migration guide for direct transfers](./roihu-data.md) from Mahti/Puhti to Roihu.

     For transferring data from Allas and/or LUMI-O to Roihu.

!!! note "Mahti and Puhti schedule"
     **Roihu is now available for use**, and can be added as a service for computational projects in MyCSC.

     Mahti and Puhti storage services will shut down 15 October 2026.

     However, we strongly encourage all users to prioritize moving their data by the **end of August 2026**,
     because between September and October 2026, the storage services will not be covered by service
     contracts and availability cannot be guaranteed.

This tutorial helps you prepare your data for the transition from Mahti and Puhti to Roihu.
The main recommendation is to plan the migration in advance, review what data you need to keep,
and transfer actively used data
directly from Mahti or Puhti to Roihu.

If you cannot manage direct data transfers from Mahti and Puhti
to Roihu,
you might consider utilizing Allas or LUMI-O as a temporary storage service to host your data.

A possible reason for utilizing Allas or LUMI-O temporarily is that Roihu's
default storage quotas are smaller than on Mahti and Puhti.
If your data does not fit within the default quotas, first review and clean up your data, and then consider whether you need a
quota increase on Roihu for your project.
See CSC documentation for [applying for more disk quota](../../accounts/how-to-increase-disk-quotas.md).

The default disk quotas on Roihu are:

|            |Capacity|Number of files|
|------------|--------|---------------|
|**home**    |15 GiB  |150 000 files  |
|**projappl**|15 GiB  |150 000 files  |
|**scratch** |250 GiB |500 000 files  |

The recommended temporary storage options are:

- **A:** Allas, if your CSC project has enough available Allas quota
- **B:** LUMI-O, if you have a project that has access to LUMI-O, and enough available storage quota there

!!! warning "Only use Allas or LUMI-O if strictly needed"
     Your primary approach in data migration from Mahti and Puhti to Roihu
     should be a direct copy from one machine to the other.
     Use Allas or LUMI-O only if you cannot complete the data
     transfer during the period between Roihu availability and the Mahti/Puhti storage shutdown.

!!! warning "Limited capacity in Allas"
     Allas is running out of capacity. Use Allas only if your project has existing quota there. **Do not apply
     for new Allas quota in your project** if you need object storage. Instead apply for LUMI-O access.

     See the short talk below for instructions on applying for a LUMI-O project.

See a CSC short talk for **how to use object storage** and **how to apply for a LUMI-O project**, if needed:

- [Slides](https://a3s.fi/kkmattil-2001659-pub/Lumi-O-for-migration.pptx)
- [Recording](https://video.csc.fi/media/t/0_x4nzfb9z)

## Recommended migration plan

1. **Review and clean up your data now.** Decide what must be preserved, what can be deleted, and what should be rebuilt or regenerated on Roihu.
2. **Plan where the data should go on Roihu.** Only data that you are actively processing should be moved directly to Roihu's working disk areas.
3. **Transfer data directly from Mahti or Puhti to Roihu.** See the [guide](./roihu-data.md) for transferring data from Mahti and Puhti directly to Roihu.
4. **Use Allas or LUMI-O only if direct transfer is not possible in time.** These services can be used as temporary storage if you cannot complete the migration between Roihu general availability and the Mahti/Puhti storage shutdown.
5. **Verify the copied data before deleting anything.** Keep the original data on Mahti or Puhti until the migration has been fully completed and verified.

## When should you use the Allas or LUMI-O instructions in this tutorial?

Use the Allas or LUMI-O instructions if:

- you have data on Mahti or Puhti that must be preserved before the storage servers are shut down (15 October 2026)
- you cannot complete a direct transfer to Roihu before the Mahti/Puhti storage shutdown
- you need temporary object storage for the transition period

Do not use the Allas or LUMI-O instructions to automatically move everything to Allas or LUMI-O. Before transferring data, **review what you actually need to keep**.

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
checking disk usage (e.g. [LUE](../../support/tutorials/lue.md)) instead of running heavy recursive commands on large directory trees.

??? info "How to check disk usage on a directory"
     We recommend using the LUE tool to identify where you have lots of data.
     Avoid using tools such as `du` as they may cause a lot of load on the file system.
     Simple usage example (run `lue -h` for other options):
     ```
     module load lue
     lue <directory-to-analyze>
     ```

### 2. Choose the target storage service

Choose **Allas** if:

- your CSC project already has Allas access
- the amount of data is moderate (Few terabytes)
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

For example, to package the `dataset/` directory in `/scratch/project_2000000/mydata`:

```bash
cd /scratch/project_2000000/mydata
tar -czf dataset-2025-08-01.tar.gz dataset/
```

Then transfer the archive file instead of the full directory tree.

Later after you copy the data back, e.g. onto Roihu, unpack the archive there with:

```bash
tar -xzf dataset-2025-08-01.tar.gz
```

Keep the original directory until you have verified that the uploaded archive can be downloaded and unpacked successfully.

## Option A: Move data from Puhti or Mahti to Allas

Use Allas if you have existing Allas quota in your project.

If your sole purpose is to keep data in Allas for the transfer period to Roihu,
please delete it without delay from Allas after you have moved the data to Roihu and verified the copy.

### 1. Log in to Puhti or Mahti

Log in to the system where your data is currently stored. E.g. to Puhti:

```bash
ssh <username>@puhti.csc.fi
```

### 2. Configure Allas access

Load the Allas module and configure access, with S3 enabled:

```bash
module load allas
allas-conf --mode S3
```

Type in your CSC password when prompted.

The command can take a while to access Allas and process all information, please be patient.

This configures an Allas connection for the selected CSC project.
With S3 mode enabled, the rclone remote used in this tutorial is:

```text
s3allas:
```

### 3. Create a bucket

Check existing buckets in the project:

```bash
rclone lsd s3allas:
```

To create a new bucket, choose a bucket name that includes your project number or another project-specific identifier. Bucket names must be unique.

Example (replace project-2000000 as your project ID):

```bash
rclone mkdir s3allas:project-2000000-roihu-transfer-${USER}
```

!!! note "Creating a unique identifier"
     In the above example, the bucket is created with the name
     `project-2000000-roihu-transfer-${USER}`. This gives the bucket your username as a suffix, which is a good way
     to distinguish your own bucket from buckets
     that other users in the project might create.

     `${USER}` is an environment variable, and you do not need to
     replace it in the tutorial commands, if you want to use your username
     as a unique bucket identifier.


### 4. Copy data to Allas

To copy a single file:

```bash
rclone copy -P dataset-2025-08-01.tar.gz s3allas:project-2000000-roihu-transfer-${USER}/
```

To copy a directory:

```bash
rclone copy -P /scratch/project_2000000/mydata s3allas:project-2000000-roihu-transfer-${USER}/mydata
```

Use `copy` rather than `move` for the first transfer. This keeps the original data on Mahti or Puhti until you have verified that the upload succeeded.

### 5. Check the uploaded data

List the bucket contents:

```bash
rclone lsf s3allas:project-2000000-roihu-transfer-${USER}/
```

For a more detailed listing:

```bash
rclone ls s3allas:project-2000000-roihu-transfer-${USER}/
```

You can also compare source and destination:

```bash
rclone check /scratch/project_2000000/mydata s3allas:project-2000000-roihu-transfer-${USER}/mydata
```

For large transfers, consider writing the output to a log file:

```bash
rclone copy /scratch/project_2000000/mydata s3allas:project-2000000-roihu-transfer-${USER}/mydata \
  --progress \
  --log-file roihu-transfer-to-allas.log
```

### 6. Downloading data later to Roihu from Allas

After Roihu is available, log in to Roihu and configure access to the object storage service that contains your data, following
instructions in the [tutorial for using Allas in Roihu](../../data/Allas/allas-roihu.md).
The approach is very similar to Mahti and Puhti.

Then copy the data from object storage to the appropriate Roihu disk area.

On Roihu, check which available buckets your project has in Allas with `rclone lsd`:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ rclone lsd s3allas:
  3268222761 2020-10-03 10:01:42         8 2000000-genomes
  2576778428 2020-10-03 10:01:42         4 2000000-mahti-SCRATCH
```

Copy the appropriate data to your directory on Roihu:

```bash
rclone copy -P s3allas:project-2000000-roihu-transfer-${USER}/mydata /scratch/project_2000000/mydata
```

After copying the data to Roihu, verify the transfer:

```bash
rclone check s3allas:project-2000000-roihu-transfer-${USER}/mydata /scratch/project_2000000/mydata
```

If you uploaded compressed archive files, unpack them only after confirming that the archive was transferred successfully:

```bash
tar -tzf dataset-2025-08-01.tar.gz
tar -xzf dataset-2025-08-01.tar.gz
```

### 7. Remove data from Allas after migration

After the data has been copied to Roihu and verified, remove the temporary copy from Allas if it is no longer needed.

**Be careful:** removal commands delete data from Allas. Do not run them before you have confirmed that the data exists in its final location.

To remove one object:

```bash
rclone deletefile s3allas:project-2000000-roihu-transfer-${USER}/dataset-2025-08-01.tar.gz
```

To remove all objects under a prefix:

```bash
rclone delete s3allas:project-2000000-roihu-transfer-${USER}/mydata
```

Check that the bucket is empty:

```bash
rclone lsf s3allas:project-2000000-roihu-transfer-${USER}/
```

Lastly, remove the empty bucket you were using:

```bash
rclone rmdir s3allas:project-2000000-roihu-transfer-${USER}
```

## Option B: Move data from Puhti or Mahti to LUMI-O

If you have an existing account and a project on LUMI, you might consider LUMI-O as a temporary storage service.

The same general rules apply as with Allas. Do not transfer everything blindly to LUMI-O.
Carefully review what you actually need to preserve, and remove unnecessary files before transfer.
If you only need temporary storage during the transition to Roihu, delete the files from LUMI-O after you have copied and verified them on Roihu.

### 1. Create an rclone setup for copying data from Mahti or Puhti directly to LUMI-O

First, you need credentials for LUMI-O and an access key to your project.

Object storage related tools are initialized in Puhti and Mahti with the command:

```text
module load allas
```
Connections to LUMI-O are configured with command:

```text
allas-conf --lumi
```

The configuration process asks you to login to [https://auth.lumidata.eu](https://auth.lumidata.eu)  where you can create an access key pair for your LUMI-project ( [instructions for generating keys](https://docs.lumi-supercomputer.eu/storage/lumio/auth-lumidata-eu/) ).

You can then copy the _project number_, _access key_ and _secret key_ to the configuration process in Puhti or Mahti.

The configuration process creates four new rclone endpoints: 

   * **lumi-o:** and  **lumi-_proj-number_-private:** refer to the non-public area of the LUMI-O project
   * **lumi-pub:** and  **lumi-_proj-number_-public:** to the public area of the LUMI-O project.

Use the `private` remotes for normal data transfer. Do not use a public remote unless the data is intentionally public.    

In case of *a-commands* you can add option `--lumi` to the command in order to make use LUMI-O. For example:

```text
a-list --lumi
```
Executing LUMI-O configuration to a new project, changes the target project of a-commands, aws, s3cmd as well as lumi-o: and lumi-pub: endpoints but preserves the endpoint names that include the project numbers.

Note that the Lumi-O keys have a validity time, defined in the authentication interface. Thus, you may need to update the connection configuration every now and then.

### 2. Create a bucket for your data

Before copying data to LUMI-O, create a bucket for the transfer.

In a Mahti/Puhti terminal:

```bash
rclone mkdir lumi-46500XXXX-private:roihu-transfer-${USER}
```

See that the bucket is visible by listing the existing buckets in your project:

```bash
rclone lsd lumi-46500XXXX-private:
```

Replace `46500XXXX` with your actual LUMI project ID.

!!! note "Creating a unique identifier"
     In the above example, the bucket is created with the name
     `roihu-transfer-${USER}`. This gives the bucket your username as a suffix, which is a good way
     to distinguish your own bucket from buckets
     that other users in the project might create.

     `${USER}` is an environment variable, and you do not need to
     replace it in the tutorial commands, if you want to use your username
     as an unique bucket identifier.

### 3. Copy data to LUMI-O

Now you're ready to transfer data to LUMI-O.

On Mahti/Puhti:

Copy a single file:
```bash
rclone copy -P your-dataset-2025-08-01.tar.gz lumi-46500XXXX-private:roihu-transfer-${USER}/
```

Copy a directory:

```bash
rclone copy -P /scratch/project_2000000/mydata lumi-46500XXXX-private:roihu-transfer-${USER}/mydata
```

For large transfers, run the command inside `tmux`, and write a log file:

??? info "Using tmux"
     Use `tmux`, for example, in a session in Puhti/Mahti:

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

```bash
rclone copy /scratch/project_2000000/mydata lumi-46500XXXX-private:roihu-transfer-${USER}/mydata \
  --progress \
  --log-file roihu-transfer-to-lumio.log
```

### 4. Verify the uploaded data

List the uploaded data:

```bash
rclone lsf lumi-46500XXXX-private:roihu-transfer-${USER}/mydata/
```

Compare the source directory and the uploaded copy:

```bash
rclone check /scratch/project_2000000/mydata lumi-46500XXXX-private:roihu-transfer-${USER}/mydata
```

For large datasets, save the verification output to a log file:

```bash
rclone check /scratch/project_2000000/mydata lumi-46500XXXX-private:roihu-transfer-${USER}/mydata \
  --log-file roihu-transfer-lumio-check.log
```

### 5. Copy data back from LUMI-O later

After Roihu is available, configure LUMI-O access on Roihu and copy the data from LUMI-O to the appropriate Roihu disk area.

Example:

```bash
rclone copy -P lumi-46500XXXX-private:roihu-transfer-${USER}/mydata /scratch/project_2000000/mydata
```

Verify the copied data:

```bash
rclone check lumi-46500XXXX-private:roihu-transfer-${USER}/mydata /scratch/project_2000000/mydata
```

If you uploaded compressed archive files, check and unpack them only after confirming that the archive was transferred successfully.

### 7. Remove data from LUMI-O after migration

After the data has been copied to Roihu and verified, remove the temporary copy from LUMI-O if it is no longer needed.

To remove one object:

```bash
rclone deletefile lumi-46500XXXX-private:roihu-transfer-${USER}/dataset-2025-08-01.tar.gz
```

To remove all objects under a prefix:

```bash
rclone delete lumi-46500XXXX-private:roihu-transfer-${USER}/mydata
```

To remove an empty bucket:

```bash
rclone rmdir lumi-46500XXXX-private:roihu-transfer-${USER}
```

## Running long transfers safely

Large transfers may take a long time. Do not run them in a normal SSH session without protection, because the transfer may stop if the connection is interrupted.

Use `tmux`, for example, in a session in Puhti/Mahti:

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

If the transfer is interrupted, you can safely run the same `rclone copy` command again.
`rclone copy` will skip files that already exist at the destination and continue copying missing or changed files.

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
rclone sync /scratch/project_2000000/mydata s3allas:project-2000000-roihu-transfer-${USER}/mydata --dry-run
```

### Object storage is not a working directory

Allas and LUMI-O are suitable for storing, staging, sharing, and transferring data. They are not replacements for scratch or project directories on a supercomputer.

Never run applications directly against object storage as if it were a normal filesystem.

### Protect sensitive data

Do not upload sensitive data unless the storage service and your project’s data management plan allow it. If needed, encrypt data before uploading.

### Document what was moved

To follow best practices, create a small README file and upload it to Allas/LUMI-O with the data. For example:

```text
Dataset: Example simulation outputs
Original location: /scratch/project_2000000/example
Source system: Puhti
Uploaded by: <name>
Upload date: YYYY-MM-DD
Temporary storage: Allas bucket project-2000000-roihu-transfer-<my-username>
Intended destination: Roihu /scratch/project_2000000/example
Notes:
```

Upload the README:

```bash
rclone copy README-roihu-transfer.txt s3allas:project-2000000-roihu-transfer-${USER}/
```

or:

```bash
rclone copy README-roihu-transfer.txt lumi-46500XXXX-private:roihu-transfer-${USER}/
```
