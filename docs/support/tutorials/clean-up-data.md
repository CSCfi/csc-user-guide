# Managing data on supercomputer scratch disks

The `scratch` disk area is only meant for data that is in active use. All other data should be
removed or moved to more suitable storage. Your project's `scratch` quota is meant for
short-term peaks, not for permanent use.

Keeping `scratch` tidy matters because:

* There are **no backups** of `scratch`. Do not trust it to store all of your research data.
* A Lustre file system slows down for everyone once it is more than about 70% full. CSC has
  allocated more quota than there is disk space, so `scratch` cannot be used for long-term
  storage.
* `scratch` usage is [billed](../../supercomputing/hpc-billing.md#storage) per TiB-hour, so
  removing files saves your project's Storage BUs.

Please do the following:

* **Remove files** that you no longer need. Deleted files cannot be restored, so be careful!
* **Compress files** if it reduces their size. Text files usually compress well. Test with one
  file first, and if it shrinks by 50% or more, compress all similar files.
  [See the available compression tools](env-guide/packing-and-compression-tools.md).
* **Move files** that you need later in the project, but not right now, to
  [Allas](../../data/Allas/index.md). See the [Allas HPC tutorial](../../data/Allas/allas-roihu.md).
  We recommend [a-tools](../../data/Allas/using_allas/a_commands.md) for small and medium
  transfers, and [rclone](../../data/Allas/using_allas/rclone.md) for very large ones.
* **Archive files** that need to outlive your compute project, for example in your
  organization's own storage or in [IDA](https://www.fairdata.fi/en/).

## Identifying where you have data

Checking how much data is in different folders can be slow and heavy on the file system:

* **Avoid** `du` and `find` with options like `-size`.
* **Use** [LUE (Lustre usage explorer)](lue.md) or `lfs find --lazy` instead.
  Note that `lfs find --lazy` may in some cases be as slow as `du`, or silently report
  wrong sizes. See `man lfs-find` for details.
* Run commands on specific subdirectories, never on your whole project folder at once.
  The total usage of your project is shown by the `csc-workspaces` command.

## Automatic removal of files

According to the [disk cleaning policy](../../supercomputing/usage-policy.md#disk-cleaning), files
are automatically removed from `scratch` (not `projappl` or `dataset`) if they are older than:

* **180 days**, if your project's `scratch` quota is less than 5 TiB
* **90 days**, if your project's `scratch` quota is 5 TiB or more

Before each cleaning round, CSC creates a *purge list* of the files that will be removed. Each
project has its own directory, readable only by project members:
`/scratch/purge_lists/<project>/`.

### Is my project affected?

Check what your project's purge list directory contains (replace `project_2001234` with your
own project):

```bash
ls /scratch/purge_lists/project_2001234/
```

| What you see                                  | What it means                                     |
|-----------------------------------------------|---------------------------------------------------|
| `path_summary.txt`                            | Files **will be removed**. Review them below.     |
| `nothing-to-remove-for-your-project`          | Nothing will be removed.                          |
| `No such file or directory`                   | Your project is not included in this cleaning.    |

If your project has files to remove, `total_size.txt` in the same directory shows how much data
they contain in total. This helps you estimate how long it would take to copy the data elsewhere:

```bash
$ cat /scratch/purge_lists/project_2001234/total_size.txt
Total size: 798343125192 bytes = 743.515 GiB = 0.726 TiB
```

??? info "Check all your projects at once"
    The script below checks every project you are a member of:

    ```bash
    for g in $(/usr/bin/groups) ; do
      if [ -d "/scratch/$g" -a ! -L "/scratch/$g" ]; then
        dir="/scratch/purge_lists/$g" ;
      else
        continue;
      fi ;
      echo -n "- Project '$g': ";
      if [ ! -d "${dir:?}" ]; then
        echo "doesn't have a purge_lists subdirectory. No files will be removed.";
        continue;
      fi ;
      if [ -f "${dir:?}/path_summary.txt" ]; then
        echo "has files that will be removed." ;
      elif [ -f "${dir:?}/nothing-to-remove-for-your-project" ]; then
        echo "is not included in the automatic cleaning.";
      else
        echo "is unclear, based on this script. Check with Service Desk what to do.";
      fi ;
    done
    ```

??? info "Other purge list file names"
    The `path_summary.txt` file is renamed during the cleaning process:

    * `path_summary.txt-later-delete` (or similar): your project has been exempted from the
      upcoming cleaning, or given more time to transfer files.
    * `path_summary.txt-stashed`: the cleaning has already been done for your project. The
      file stays readable so that you can still check what was removed.

    Files from the previous round are archived when the next round begins. To check whether a
    purge list is from the current round, look at its modification date:

    ```bash
    $ stat -c %y /scratch/purge_lists/project_2001234/path_summary.txt-stashed
    2023-05-23 00:35:28.000000000 +0300
    ```

## Reviewing your purge list

`path_summary.txt` is not meant to be read directly. You can review it either in the web
interface or on the command line.

### In the web interface

The [Roihu web interface](https://www.roihu.csc.fi) provides a graphical tool,
**File Deletion Explorer**, for inspecting purge lists. You can find it in the
web interface under the _Tools_ drop-down menu.

The tool can visualize the contents of your purge list as a treemap, show the size
distribution of the files, and analyze file name suffixes. You can also filter files by their
path and name, and save the filtered lists as text files for later use on the command line.

### On the command line with LCleaner

Use the `lcleaner` tool on a login node to turn `path_summary.txt` into a readable list of
files. First, set these two variables. All commands below use them:

```bash
my_project="project_2001234"   # Replace with your own project
list="/scratch/purge_lists/${my_project}/path_summary.txt"
```

**List all files** that will be removed and save the list to your home directory. If
`path_summary.txt` is large (over 100 MB), this can take a while, so it is best to save the
list once and search the saved copy:

```bash
lcleaner --out-file ~/purge_list "$list"
less ~/purge_list
```

**Show the biggest files** first, with their sizes in bytes (here the top 10):

```bash
lcleaner --sort-by-size --limit 10 --csv "$list"
```

**Check whether a specific directory** is on the list (no output means no matches):

```bash
grep "/scratch/${my_project}/important-dir" ~/purge_list
```

Copy any files you want to keep to [Allas](../../data/Allas/index.md) or other storage before
the cleaning.

## Deleting the files yourself

Instead of waiting for the automatic cleaning, please delete files you do not need yourself.

!!! warning "The commands below delete files permanently"
    Review the list carefully and make sure you have copied everything you want to keep
    before running them.

Deleting many files can take several hours. Start a `tmux` session first, so that the
deletion keeps running even if you disconnect:

```bash
tmux new -s cleanup
```

Inside the session, set the variables for your project:

```bash
my_project="project_2001234"   # Replace with your own project
list="/scratch/purge_lists/${my_project}/path_summary.txt"
```

**Delete all files** on the purge list:

```bash
lcleaner -0 "$list" | xargs -0 -n 50 rm -vf --
```

**Delete only the files inside one directory**:

```bash
lcleaner -0 "$list" | grep -zZ "/scratch/${my_project}/delete-this-dir/" | xargs -0 -n 50 rm -vf --
```

Press `Ctrl-b` and then `d` to detach from the session and leave the deletion running.
To check on it later, [log in to the same login node](../../supercomputing/connecting/index.md#connecting-to-a-specific-node)
and run `tmux attach -t cleanup`.
Type `exit` to close the session when the deletion is done. See the
[tmux tutorial](tmux.md) for more details.

## More LCleaner options and troubleshooting

Run `lcleaner --help` to see all options. The most useful ones are:

| Option                    | Effect                                                        |
|---------------------------|---------------------------------------------------------------|
| `--csv`                   | Print file paths and sizes as CSV (with a header row)         |
| `--json`                  | Print file paths and sizes as JSON (prettify with `jq .`)     |
| `--sort-by-size`          | Sort the biggest files first                                  |
| `--limit N`               | Print only the first `N` files                                |
| `--out-file NAME`         | Write output to a file. Required when combining `--csv` and `--json` |
| `-0`, `--nullbyte`        | Separate paths with null bytes, for safe use with `xargs -0` |

Options mentioning `--admin-mode` are for CSC administrators and can be ignored.

If `lcleaner` reports that it could not parse some lines, the error messages tell you the line
numbers. You can view a line, e.g. line 123, with `sed -n 123p "$list"`.

To save a debug log, for example to send to support:

```bash
lcleaner --log-level debug "$list" 2> ~/lcleaner-debug-$(date +%s).log
```

Please report bugs to [CSC Service Desk](../contact.md).
