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

## 2. Basic data migration

The following tools are suitable if:

* Your data volume is relatively small (a few tens of GB).
* Number of files is small (a few hundred).
* There are no special requirements related to, for example, preservation of
  file permissions or timestamps.

### 2.1 `rsync`

### 2.2 `scp`

[`scp`](../../data/moving/scp.md) is useful only in the most simple cases.
Assuming you've connected to Puhti/Mahti and forwarded your SSH agent
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

!!! warning "Note"
    Do **not** use `scp` if your data contains a lot of small files. `scp` is
    extremely slow for transferring a large number of small files.

## 3. Advanced cases

Read more here.

## 4. Final remarks
