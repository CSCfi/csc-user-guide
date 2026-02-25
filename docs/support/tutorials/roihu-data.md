# Roihu data migration guide

!!! info "About this guide"
    This guide is divided into three main parts:

    1. [General guidelines and prerequisites](#1-general-guidelines-and-prerequisites)
    2. [Basic data migration](#2-basic-data-migration)
    3. [Advanced cases](#3-advanced-cases)

    If your data transfer needs are small and simple, reading the
    [Basic data migration](#2-basic-data-migration) section may be enough. If
    you have **a lot** of data or other special requirements, please check the
    [Advanced cases](#3-advanced-cases). In any case, please read at least the
    [General guidelines and prerequisites](#1-general-guidelines-and-prerequisites)
    section before migrating any data to Roihu.

## 1. General guidelines and prerequisites

### 1.1 Review and clean up your data before migration
  
* Like on Puhti and Mahti, Roihu scratch disk is not intended for long-term
  data storage, but should only be used for data that is in active use.
  Thus, **only move data that you truly need**.
* Good data hygiene reduces transfer time and load on the file system, as well
  as eliminates the risk of moving redundant or duplicate data.
* Roihu will implement a similar disk cleaning policy as Puhti, meaning
  that files that have not been accessed in 180 days will be deleted.
* We recommend using the [LUE tool](lue.md) to identify where you have lots of
  data. Avoid using other tools such as `du` or `find` as they may cause a lot
  of load on the file system. Simple usage example (run `lue -h` for other
  options):

    ```bash
    module load lue
    lue <directory-to-analyze>
    ```

* Other tips:
    * Remove or exclude temporary files (cached data, intermediate results,
      logs, unused checkpoint files, core dumps, etc.).
    * It is best to re-build your applications on Roihu, so do not move
      compiled programs or pre-built environments, unless they are
      containerized. Note that all applications, including containers, that
      target Roihu's ARM-based GPU nodes must be re-built regardless.

### 1.2 Ensure that you have enough disk space on Roihu

* Once you have identified the data you need to transfer, check that it
  fits within the default disk quotas on Roihu:

    | Disk area | Path                  | Default size | Max. size [^1]      | Default file number limit | Max. file number limit [^1] |
    |-----------|-----------------------|-------------:|--------------------:|--------------------------:|----------------------------:|
    | home      | `/users/$USER`        | 15 GiB       | 15 GiB              | 150k                      | 150k                        |
    | projappl  | `/projappl/<project>` | 15 GiB       | 250 GiB (< 100 GiB) | 150k                      | 2.5M (< 1M)                 |
    | scratch   | `/scratch/<project>`  | 1 TiB        | 100 TiB (< 10 TiB)  | 1M                        | 10M (< 5M)                  |

    [^1]: Values in parentheses indicate automatically approved limits.

* Please note that existing quota extensions on Puhti/Mahti will not
  automatically carry over to Roihu, so you must separately
  [apply for increased disk quota](../../accounts/how-to-increase-disk-quotas.md)
  via [MyCSC](https://my.csc.fi) beforehand if your data does not fit
  within the default limits.

### 1.3. Add Roihu service access to your CSC project

* Like any other CSC service, access to Roihu must be enabled for your project
  via [MyCSC](https://my.csc.fi).
* Also note that each user must have at least a **medium** level of identity
  assurance (LoA) to be able to access Roihu. You can check your LoA on your
  [profile page in MyCSC](https://my.csc.fi/profile), and
  [elevate it if needed following these instructions](../../accounts/strong-identification.md).

### 1.4 Transfer your data directly from Puhti/Mahti to Roihu

* For performance and capacity management reasons, it is not recommended to
  transfer data to Roihu via Allas or your local workstation. Instead, CSC
  recommends using command-line based tools such as
  [`rsync`](../../data/moving/rsync.md) to directly push or pull data from
  Puhti/Mahti to Roihu.

### 1.5 Authenticating to Roihu over SSH

* In addition to SSH keys, a signed SSH certificate is required to authenticate
  to Roihu. Each certificate is valid for 24 hours.
    * [Read the instructions here](../../computing/connecting/ssh-keys.md#signing-public-key).
* To transfer data directly from Puhti/Mahti to Roihu, you must make sure to
  **forward your SSH agent** when connecting to the system on which the data
  transfer process is initiated.
    * If a data transfer process is launched on Puhti/Mahti (i.e., you _push_
      data from Puhti/Mahti), your forwarded SSH agent must hold your SSH keys
      **and** a valid SSH certificate so that a connection to Roihu can be
      formed.
    * If a data transfer process is launched on Roihu (i.e., you _pull_ data
      from Puhti/Mahti), it is enough that your forwarded SSH agent only holds
      your SSH keys. However, you still need an SSH certificate to login to
      Roihu in the first place (while useful, it does not have to be added to
      your SSH agent).
        * [SSH agent instructions for Linux/macOS](../../computing/connecting/ssh-unix.md#authentication-agent).
        * [SSH agent instructions for Windows](../../computing/connecting/ssh-windows.md#authentication-agent).

## 2. Recommended data migration tools

* [`rsync`](../../data/moving/rsync.md) is the preferred tool for transferring
  data from Puhti or Mahti to Roihu. The following sections provide a few
  examples of `rsync` usage.
* In all examples it is assumed that you've connected to Puhti or Mahti and
  have forwarded your SSH agent including your SSH keys and a valid SSH
  certificate when connecting.
* Before starting the transfer, please ensure that the target directory exists
  and is writable.

### 2.1 Basic `rsync`

* Transfer directory `/scratch/project_2001234/folder-to-migrate` from
  Puhti/Mahti to directory `/scratch/project_2001234/` on Roihu.

    ```bash
    rsync -aP /scratch/project_2001234/folder-to-migrate $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
    ```

    | Option | Description                                                                                                           |
    |--------|-----------------------------------------------------------------------------------------------------------------------|
    | `-a`   | Use archive mode: copy files and directories recursively, preserve access permissions, timestamps and symbolic links. |
    | `-P`   | Keep partially transferred files and show progress during transfer.                                                   |

* **This command is suitable if:**
    1. Data compression is not necessary.
    2. You are transferring your own files, or resulting file ownership on
       Roihu does not matter.

!!! info "The trailing `/` character has a meaning!"
    A trailing `/` character affects what gets transferred _from the source_.
    If the source path ends with `/`, then all contents of the directory will
    get copied, but not the directory itself. To transfer the directory itself
    (and the contents), leave out the trailing `/` (like in the example above).

### 2.2 Data compression

### 2.3 Using checksums to verify data integrity

* `rsync` ensures data integrity using internal checksum mechanisms by default.
  It is therefore not necessary to compute a checksum for your sda

## 3. Advanced cases

### 3.1 Running long transfer processes safely

### 3.2 If file ownership matters

## 2.2 Discouraged methods

### 2.2.1 `scp`

* [`scp`](../../data/moving/scp.md) performs poorly especially if your data
  contains a lot of small files, so it is useful only in the most simple data
  migration cases.

* Assuming you've connected to Puhti/Mahti and forwarded your SSH agent
  (including SSH keys and a valid SSH certificate), run `scp` for example like
  this:

   ```bash
   scp -r /scratch/project_2001234/folder-to-migrate/ $USER@roihu-cpu.csc.fi:/scratch/project_2001234/
   ```

  * Option `-r` means _recursive_, i.e. the directory `folder-to-migrate` and all
    of its contents will be transferred to `/scratch/project_2001234/` on Roihu.
    If you're just moving a single file, the `-r` can be left out.

Assuming you're on Roihu and you want to pull data from, for example, Puhti to
your current working directory on Roihu, run `scp` like this:

```bash
scp -r $USER@puhti.csc.fi:/scratch/project_2001234/folder-to-migrate/ .
```

### 2.2.2 Using the web interfaces to migrate data

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

!!! warning "Don't use Allas for migrating data to Roihu!"
    It is strongly discouraged to use Allas for migrating data to Roihu
    because it is running out of capacity. Please use LUMI-O if you must
    migrate data to Roihu via object storage.
