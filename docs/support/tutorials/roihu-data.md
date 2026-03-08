# Roihu data migration guide

??? info "About this guide"
    This guide is divided into four parts:

    1. [General guidelines and prerequisites](#1-general-guidelines-and-prerequisites)
    2. [Recommended data migration methods](#2-recommended-data-migration-methods)
    3. [Special cases](#3-special-cases)
    4. [Discouraged methods](#4-discouraged-methods)

    Please read the
    [General guidelines and prerequisites](#1-general-guidelines-and-prerequisites)
    section before migrating any data to Roihu. If your data migration needs
    are small and simple, checking the
    [Basic rsync](#21-basic-rsync) example may suffice. If you have **a lot**
    of data or other special requirements, please also read the other sections
    carefully.

## 1. General guidelines and prerequisites

### 1.1 Review and clean up your data before migration
  
* Roihu scratch disk is not intended for long-term data storage, but should
  only be used for data that is in active use. Thus, **only move data that you
  truly need**.
    * Good data hygiene reduces transfer time and load on the file system, as
      well as eliminates the risk of moving redundant or duplicate data. Roihu
      will implement a similar disk cleaning policy as Puhti, meaning that
      files that have not been accessed in 180 days will be deleted.
    * We recommend using the [LUE tool](lue.md) to identify where you have lots of
      data. Avoid using tools such as `du` as they may cause a lot of load on
      the file system. Simple usage example (run `lue -h` for other options):

        ```bash
        module load lue
        lue <directory-to-analyze>
        ```

* Other tips:
    * Remove or exclude temporary files (cached data, intermediate results,
      logs, unnecessary checkpoint files, core dumps, etc.).
    * Apptainer containers built for CPUs can be moved to Roihu. Do **not**
      move containers targeting GPUs or any native installations from Puhti or
      Mahti to Roihu. These must be re-built from scratch for best performance,
      or in order for them to work at all (GPU nodes have ARM CPU
      architecture).
      [More about installing software on Roihu](roihu.md#installing-software).

### 1.2 Ensure that you have enough disk space on Roihu

* Once you have identified the data you need to transfer, check that it
  fits within the default disk quotas on Roihu:

    | Disk area | Path                  | Default size | Max. size [^1]      | Default file number limit | Max. file number limit [^1] |
    |-----------|-----------------------|-------------:|--------------------:|--------------------------:|----------------------------:|
    | Home      | `/users/$USER`        | 15 GiB       | 15 GiB              | 150k                      | 150k                        |
    | ProjAppl  | `/projappl/<project>` | 15 GiB       | 250 GiB (< 100 GiB) | 150k                      | 2.5M (< 1M)                 |
    | ProjData  | `/projdata/<project>` | n/a          | n/a                 | n/a                       | n/a                         |
    | Scratch   | `/scratch/<project>`  | 1 TiB        | 100 TiB (< 10 TiB)  | 1M                        | 10M (< 5M)                  |

    [^1]: Values in parentheses indicate automatically approved limits.

* Please note that existing quota extensions on Puhti/Mahti will not
  automatically carry over to Roihu, so you must separately
  [apply for increased disk quota](../../accounts/how-to-increase-disk-quotas.md)
  via [MyCSC](https://my.csc.fi) beforehand if your data does not fit
  within the default limits.

??? info "New ProjData disk area on Roihu"
    Users may apply for new "dataset projects" (cf. regular computing projects)
    to get access to a new disk area on Roihu – **ProjData**. This disk area
    allows storing datasets on the disk for a longer timer (no cleaning,
    lifetime is limited by the data project lifetime). Read access to the data
    can be shared 

    Dataset projects and ProjData quotas are applied for and managed via
    [MyCSC](https://my.csc.fi). ProjData quota consumes Storage BUs.

### 1.3. Add Roihu service access to your CSC project

* Like any other CSC service, access to Roihu must be enabled for your project
  via [MyCSC](https://my.csc.fi).
* Note also that users must have at least a **medium** level of identity
  assurance (LoA) to be able to access Roihu. You can check your LoA on your
  [profile page in MyCSC](https://my.csc.fi/profile), and
  [elevate it if needed following these instructions](../../accounts/strong-identification.md).

### 1.4 Transfer your data directly from Puhti/Mahti to Roihu

* It is **not** recommended to transfer data to Roihu via Allas or your local
  workstation. Instead, CSC recommends using command-line based tools such as
  [`rsync`](#2-recommended-data-migration-methods) to **directly transfer data
  from Puhti/Mahti to Roihu.**

!!! warning "Extremely important"

    ### 1.5 Connecting to Roihu requires SSH certificates

    * In addition to SSH keys, a signed **SSH certificate** is required to
      connect to Roihu over SSH.
      [Read the instructions for getting and using SSH certificates here](../../computing/connecting/ssh-keys.md#signing-public-key).
    * To transfer data directly from Puhti/Mahti to Roihu, you must **forward
      your SSH agent** when connecting to the system where you launch the data
      transfer process.
        1. **[SSH agent instructions for Linux/macOS](../../computing/connecting/ssh-unix.md#authentication-agent).**
        2. **[SSH agent instructions for Windows](../../computing/connecting/ssh-windows.md#authentication-agent).**
    * We **strongly** recommend using the
      [certificate helper tool](../../computing/connecting/ssh-keys.md#option-1-certificate-helper-tool)
      developed by CSC to simplify the process.

## 2. Recommended data migration methods

* **`rsync`** is the preferred tool for transferring data from Puhti or Mahti
  to Roihu. [Read more about `rsync` here](../../data/moving/rsync.md).
* **We will use Puhti as an example**, but the exact same steps apply for Mahti
  also. Simply replace all occurrences of `puhti` in host names etc. with
  `mahti`.
* All examples require that you've **forwarded your SSH agent** including your
  **SSH keys** and a **valid SSH certificate** to Puhti when connecting.
* Before starting the data transfer, **ensure that the target directory on
  Roihu exists and is writable**.

??? info "Help! What to do if I struggle to add my SSH certificate to the SSH agent?"
    Alternatively, you may log in to Roihu and **pull** data from Puhti.
    Because connecting to Puhti does not require an SSH certificate, it is
    enough that the forwarded SSH agent holds your SSH keys.

    Note that you will still need a valid SSH certificate when connecting to 
    Roihu in the first place, **but it does not have to be added to your SSH
    agent**.

### 2.1 Basic `rsync`

1. [Obtain an SSH certificate](../../computing/connecting/ssh-keys.md#signing-public-key).
2. Add your SSH keys and certificate to your SSH agent.
      1. [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md#authentication-agent).
      2. [Instructions for Windows](../../computing/connecting/ssh-windows.md#authentication-agent).
3. Log in to Puhti with SSH agent forwarding turned on.
    * [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md#ssh-agent-forwarding).
    * [Instructions for Windows](../../computing/connecting/ssh-windows.md#ssh-agent-forwarding).
4. On the login node, transfer directory `/scratch/project_2001234/my-data`
   from Puhti to directory `/scratch/project_2001234/` on Roihu.

    ```bash
    rsync -aP /scratch/project_2001234/my-data $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
    ```

    | Option | Description                                                                                                           |
    |--------|-----------------------------------------------------------------------------------------------------------------------|
    | `-a`   | Use archive mode: copy files and directories recursively, preserve access permissions, timestamps and symbolic links. |
    | `-P`   | Keep partially transferred files and show progress during transfer.                                                   |

5. Alternatively, if you've connected to Roihu and are **pulling** data from
   Puhti, use the command:

    ```bash
    rsync -aP $USER@puhti.csc.fi:/scratch/project_2001234/my-data /scratch/project_2001234/
    ```

**The `rsync -aP` command is suitable if:**

1. The **number of files to transfer is small** (<1000) or the **files are
   large** enough (>1 MB on average).
    * If not, please
      [archive](#23-migrating-data-with-large-amounts-of-small-files) and,
      optionally, [compress the data](#31-data-compression) before transfer.
2. You are transferring your own files **or** resulting file ownership on Roihu
   does **not** matter.
    * You will own all files that you transfer to Roihu irrespective of who the
      owner on Puhti is.

??? info "Note! The trailing `/` character has a meaning in `rsync` commands!"
    A trailing `/` character affects what gets transferred **from the source**.
    If the source path ends with `/`, then all contents of the directory will
    get copied, but not the directory itself. To transfer the directory itself
    (and the contents), leave out the trailing `/` as in the previous example.

??? info "How long will my data migration take?"
    The table below can be used as a rough reference for how long certain data
    transfers using `rsync` will take.

    | Number of files | Average file size | Total size | Duration | Notes |
    |-:|-:|-:|-:|-|
    | 1     | 1 GB   | 1 GB   | 6 s     |
    | 10    | 100 MB | 1 GB   | 6 s     |
    | 100   | 10 MB  | 1 GB   | 6 s     |
    | 1000  | 1 MB   | 1 GB   | 11 s    | Small-file overhead increases, [please archive](#23-migrating-data-with-large-amounts-of-small-files)!
    | 10000 | 100 kB | 1 GB   | 45 s    | Small-file overhead increases, [please archive](#23-migrating-data-with-large-amounts-of-small-files)!
    | 1     | 10 GB  | 10 GB  | ~1 min  |
    | 10    | 1 GB   | 10 GB  | ~1 min  |
    | 100   | 100 MB | 10 GB  | ~1 min  |
    | 1000  | 10 MB  | 10 GB  | ~1 min  |
    | 1     | 100 GB | 100 GB | ~11 min | 
    | 1     | 1 TB   | 1 TB   | ~ 2 h   |

    Please note that the actual performance may vary based on the current
    system load. If you need to transfer thousands of small files (<1 MB),
    [pack them into a single archive file for better performance](#23-migrating-data-with-large-amounts-of-small-files).
    
### 2.2 Performing a dry run

It may be useful to perform a dry run before starting the actual `rsync`
process. Add the option `-n` to your `rsync` command:

```bash
rsync -anP /scratch/project_2001234/my-data $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
```

This command does not transfer anything, it simply shows what would happen if
you were to run `rsync` without the `-n` option.

??? warning "Note! A dry run will not catch errors that would be caused by insufficient permissions"
    An `rsync` dry run will **not** catch errors caused by insufficient
    permissions. In other words, it assumes that:

    1. You have read and execute permissions for all files and directories,
       respectively, that you are trying to migrate from Puhti.
    2. You have write permission on the destination (Roihu).

    To list files and directories that you cannot transfer due to insufficient
    permissions, try:

    ```bash
    find /scratch/project_2001234/my-data ! -readable 2> /dev/null
    ```

    To check if the destination is writable, try:

    ```bash
    ssh $USER@roihu-cpu.csc.fi "touch /scratch/project_2001234/.test && rm /scratch/project_2001234/.test"
    ```

    Missing write permissions will cause a `Permission denied` error. If the
    destination does not exist, you will get a `No such file or directory`
    error.

### 2.3 Migrating data with large amounts of small files

If the data you need to migrate contains thousands of small files, it is
recommended to **archive** the data before transferring it, i.e. pack all files
into a single file. Most data transfer tools handle one large file far better
than thousands of small ones.

1. Assuming you want to migrate the directory
   `/scratch/project_2001234/my-data` from Puhti to Roihu, create (`c`) an
   archive of it as follows:

    ```bash
    cd /scratch/project_2001234
    tar cf my-data.tar my-data
    ```

2. Transfer the archived dataset `my-data.tar` to Roihu [using `rsync`](#21-basic-rsync).
3. Extract (`x`) the data on Roihu with:

    ```bash
    tar xf my-data.tar
    ```

4. [Read more about `tar` here](env-guide/packing-and-compression-tools.md#tar-packing-several-files-into-one-file).

??? info "Mind your disk quota!"
    Archiving creates new data on the disk. If your dataset is large, you may
    end up running out of disk quota since the operation will essentially
    double your disk usage (unless the archive is also
    [compressed](#31-data-compression)).

    A trick to avoid creating new data on Puhti disk is to pipe the output of
    `tar` to Roihu directly over SSH. Use the command:

    ```bash
    tar c -C /scratch/project_2001234 my-data | ssh $USER@roihu-cpu.csc.fi 'cat > /scratch/project_2001234/my-data.tar'
    ```

    [Read more about using `tar` over SSH](../../data/moving/tar_ssh.md).

## 3. Special cases

### 3.1 Data compression

Data compression can be useful to save storage space and make data transfer
faster, **but it may take a lot of time**. Data compression is CPU intensive
and compressing large datasets may easily take **several hours**.

The compressibility of files depends on their content. Certain file formats are
already highly compressed (e.g., images) and trying to compress these further
is counter-productive. On the other hand, data compression can be beneficial
if transferring, for example, many small plain text files, or large text-based
datasets.

| File types that compress well | File types that do not compress well       |
|-------------------------------|--------------------------------------------|
| Plain text                    | Media (JPG, PNG, GIF, MP3, MP4, WAV, etc.) |
| CSV, XML, JSON, YAML, etc.    | Pre-compressed archives (ZIP, gzip, etc.)  |
| Source code (Python, C, etc.) | Binary blobs (e.g., compiled executables)  |

`rsync` provides built-in functionality for on-the-fly compression and
decompression via the `-z` option:

```bash
rsync -azP /scratch/project_2001234/my-data $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
```

??? info "Alternative methods to maximize performance"
    `rsync` uses the `zlib` library for compressing data during transfer. The
    performance is comparable to `gzip`, but there are even faster options
    available if needed. One such is
    [`zstd` compression](env-guide/packing-and-compression-tools.md#zstandard-compression-tool).

    `zstd` compression can be combined with using `tar` over SSH. To transfer
    the directory `my-data` from Puhti to Roihu, run:

    ```bash
    tar c -I zstd -C /scratch/project_2001234 my-data | ssh $USER@roihu-cpu.csc.fi 'cat > /scratch/project_2001234/my-data.tar.zst'
    ```

    In cases where compression is not beneficial, you can also use plain `tar`
    over `ssh`
    [as explained previously](#23-migrating-data-with-large-amounts-of-small-files).
    The performance can be better than `rsync`, especially if your dataset
    contains a huge number of tiny files.

    * [Read more about using `tar` over `ssh` for data transfer here](../../data/moving/tar_ssh.md).
    * [Read more about packing and compression tools here](env-guide/packing-and-compression-tools.md).

### 3.2 Running long transfer processes safely

One of the strengths of `rsync` is that interrupted transfers can be easily
resumed – **just run the same `rsync` command again**. `rsync` will compare the
source and destination, skip already transferred files (copies only what's
missing) and resume partially transferred files (as long as option `-P` or
`--partial` is used as [instructed above](#21-basic-rsync)).

However, to avoid failures caused by interrupted SSH sessions altogether, you
may run your data migration process in a `screen` session.

1. On Puhti, start a `screen` session:

    ```bash
    screen -S roihu_migration
    ```

2. Start your `rsync` command inside the `screen` session:

    ```bash
    rsync -aP /scratch/project_2001234/my-data $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
    ```

3. Now you may detach and leave the `rsync` process running:

    ```txt
    Ctrl + A, then press D
    ```

    The data migration process will keep running safely in the background. You
    may log out from Puhti if you want.

4. Reattach the session with:

    ```txt
    screen -r roihu_migration
    ```

    If you forgot the name of the session, try `screen -ls`.

5. When the data transfer has finished, terminate the session by typing `exit`
   inside the `screen` session.

Using `screen` is useful if your data transfer will take several hours. You
can, for example, power off your computer and leave the `rsync` process running
overnight.

### 3.3 Using checksums to verify data integrity

`rsync` ensures data integrity using internal checksum mechanisms by default.
**It is therefore not necessary to verify data integrity separately**.

If you're not using `rsync`, you may calculate a checksum for files using e.g.
`md5sum`.

1. Assuming you've got a dataset archive `data.tar` on Puhti, calculate a
   checksum for it with:

    ```bash
    md5sum data.tar > data.tar.md5
    ```

    Note that calculating checksums for huge datasets can take some time,
    especially if the current disk load is high.

2. [Transfer](#21-basic-rsync) the dataset and the `data.tar.md5` checksum file
   to Roihu.
3. With the `data.tar` and `data.tar.md5` files in the same directory, verify
   the checksum with:

    ```bash
    md5sum -c data.tar.md5
    ```

    If any byte changed during transfer, the file will not match, and you will
    see `data.tar: FAILED`. Otherwise you should get `data.tar: OK`.

### 3.4 If file ownership matters

**You will be set as the owner of all files that you transfer from Puhti to
Roihu**. This is important to realize when migrating data from shared project
directories where you may have read access to data owned by your colleagues.

There is no way for users to move their colleagues' data in such a way that
the ownerships would be preserved. If this is important to your project, then
**please ensure that each member moves only their own data**.

In case you later notice incorrect file ownerships, Roihu system administrators
may fix them for you. Please [contact CSC Service Desk](../contact.md) with the
details on which files and/or directories are affected and who should be set as
the owner.

## 4. Discouraged methods

### 4.1 `scp`

`scp` has many drawbacks compared to `rsync`. It cannot resume interrupted
transfers, has limited metadata preservation capabilities, no built-in
integrity checks and inferior performance. Using it to migrate data to Roihu is
therefore not recommended, unless your dataset is very small and simple (<10
GB, <100 files).

[Read more about `scp` here](../../data/moving/scp.md).

### 4.2 Using the web interfaces to migrate data

Unfortunately, there is no good way that the Puhti or Mahti web interfaces can
be used to move data directly to Roihu. There are some indirect ways, but none
of them are efficient, which is why we primarily recommend the command-line
based approaches above. The following options should therefore be considered as
"last resort" choices.

1. Use the Puhti/Mahti web interface file browser to first download your data
   locally, and then upload it to Roihu via the Roihu web interface. Note that
   there is a **limit of 10 GB for individual file uploads**, so data larger
   than this must be split into suitable chunks. Alternatively, you could use
   [graphical file transfer utilities](../../data/moving/graphical_transfer.md)
   to upload the data to Roihu since you've already downloaded it locally.
2. If you have a LUMI project, you could use the Puhti/Mahti web interface
   [Cloud storage configuration](../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
   app to set up a connection to LUMI-O, upload your data there, and then fetch
   it from LUMI-O to Roihu.

??? warning "Don't use Allas for migrating data to Roihu!"
    It is **strongly discouraged** to use Allas for migrating data to Roihu
    because Allas is running out of capacity. Please prefer LUMI-O if you must
    migrate data to Roihu via object storage.
