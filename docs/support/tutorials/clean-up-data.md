# Managing data on Puhti and Mahti scratch disks

An important task for all users on Puhti and Mahti is to manage what data resides in project
folders in `scratch`. These are only intended as temporary storage space for data that is in
active use. All other data should be removed, or stored in other more suitable storage systems.
Users are not expected to use all of their quota, the maximum quota is only meant for
short-term bursts.

Also note that:

* A Lustre parallel file system starts to lose performance when more than approximately 70% of
  disk space is used, and the more the disks fill up, the slower the performance will get.
  CSC has allocated more quota than there is space, hence it is not even possible for all users
  to use their `scratch` folders for longer term storage.
* There are **no backups** of `scratch` disk area. Do not trust it to store all of your research data.
* Removing files may decrease the BU consumption of your project, since you are billed for excess disk usage beyond 1 TiB.

We kindly ask all users to help to keep disk usage manageable, and performance reasonable.
Please do the following tasks:

* **Remove files** that are not needed anymore in your project's `scratch` folder.
  Note that we cannot bring back files that you delete by mistake so do these operations carefully!
* **Compress files** if it reduces file size. Ascii text files usually compress very well.
  Test with one file first. If the file size drops by 50%, go ahead and compress all similar files.
  [See here for available compression tools](env-guide/packing-and-compression-tools.md).
* **Move files** not in active use now, but that need to be available later during the project.
  The typical model is to move the files to [Allas](../../data/Allas/index.md).
  We recommend to use [a-tools](../../data/Allas/using_allas/a_commands.md) for small to
  medium sized data transfers, in particular when you have a large amount of small files.
  These tools make the usage of Allas safer, and can make your data management easier.
  For very large data transfers we recommend using [rclone](../../data/Allas/using_allas/rclone.md).
  A tutorial for data transfer is available at [allas-examples](../../data/Allas/allas-examples.md).
* **Archive files** that should be available longer than the lifetime of compute projects.
  Options for this can be for example your organizations own storage systems, or
  [IDA safe storage for research data](https://www.fairdata.fi/en/).

## Identifying where you have data

If you have a large amount of files, analyzing how much data you have in different folders can
be time consuming and also heavy on the file system. Our recommendations for tools that can
show the amount of data in folders:

* **Avoid** using `find` options like `-size` or similar
* **Avoid** using `du`
* **Do** use `lue` or `lfs find --lazy`

CSC has developed an approximate tool called LUE (Lustre usage explorer) for reporting amount of
data in folders. [Read the documentation at LUE](../../support/tutorials/lue.md) before using it.
`lfs find --lazy` has some edge-case where it can be as bad as `du` or silently fail to get correct
size information. Run `man lfs-find` for further instructions and information on its limitations.

!!! Note
    No matter what tool you use you should never try to list or process all files in your project
    or `scratch` folder with a single command. Instead you should run commands on specific
    subdirectories with limited amount of files and data. The total amount of used data is
    available from the `csc-workspaces` command.

## Automatic removal of files

There is a policy of removing files older than 180 days from `scratch` (not `projappl`) to ensure
that only actively used data resides on the disk (currently implemented only on Puhti).

Files that will be deleted in the next clean up are listed in so called "purge lists" files.
These are split up by project, and can be found on Lustre at one of the locations below.
Only members of the project groups can access the project directories.
If your project is newly created, your project might not yet have its own subdirectory in
the `purge_lists` directory, in which case it won't participate in the automatic cleaning.

* `/scratch/purge_lists/<PROJECT NAME>/path_summary.txt`
* `/fmi/scratch/purge_lists/<PROJECT NAME>/path_summary.txt` (only on Puhti, for FMI projects)

In case the `path_summary.txt` file does not exist, your project did not have any files that matched
the clean-up criteria, and thus nothing will be deleted from it. To indicate that the file is
intentionally missing, CSC will place a file named `nothing-to-remove-for-your-project` in your
project's purge_lists subdirectory, so check for the existence of this file as well.

As part of the automated cleaning process, the files will change names. Before the cleaning has
begun, each project that is part of the clean-up will have a file named `path_summary.txt`.
In special cases where a project is exempt from the upcoming cleaning, or requires more time to
transfer files, the administrators will rename the file to something else, usually
`path_summary.txt-later-delete`. Once a project has been processed by the automated cleaning,
the file will be renamed to `path_summary.txt-stashed`. These files are still readable to projects,
so that it is possible to refer to the list also after the cleaning is performed.
The previous round's files will be archived when the next round of cleaning is about to begin.
You can check whether your project's purge list has been updated recently by checking its last
modification date. In the example below, the file is a few months old, so it is clearly from
the prior round of cleaning:

```bash
$ stat -c %y /scratch/purge_lists/project_2001659/path_summary.txt-stashed
2023-05-23 00:35:28.000000000 +0300
$ date +%F
2023-08-04
```

Another file which is put into each project's `purge_lists` directory is the `total_size.txt` file.
This file contains a precalculated size estimate based on the numbers inside the `path_summary.txt`
files. This file exists for every project, and is created automatically when the purge lists are
generated. The file might look like this:

```bash
$ cat /scratch/purge_lists/project_2001659/total_size.txt
Total size: 798343125192 bytes = 743.515 GiB = 0.726 TiB
```

With this information, you are able to estimate how much time might be required to back up the
data elsewhere, if you want to keep everything on the purge list outside of Puhti's `scratch` file
system.
The file system tools which CSC uses to generate the list of files to remove will output files
which are quite verbose and difficult to read. By using the LCleaner tool described in the next section,
users can get the relevant information in a more user-friendly format.

## Using LCleaner to check which files will be automatically removed

LCleaner is a tool developed by CSC, which is intended to help you to discover what files your
project has that have been targeted for automatic removal.

Run `lcleaner --help` on the login nodes to see what options LCleaner supports.

### LCleaner examples

#### Check if your project has a path_summary.txt file

The first thing to check, is whether your project indeed has a `path_summary.txt` file.
All projects don't automatically have one, only the ones which have something to clean up.

```bash
# Check if your project has a path_summary.txt file
my_project="project_2001659" # Replace with your own project name
ls "/scratch/purge_lists/${my_project:?}/"
# Or if you are in an FMI project on Puhti:
ls "/fmi/scratch/purge_lists/${my_project:?}/"
```

If you see a `path_summary.txt` file in the directory, read ahead to discover what files
are on the list. However, if you find a file named `nothing-to-remove-for-your-project`,
your project doesn't have anything that will be automatically removed.

If you want a quick, copy-pasteable solution, use the small script below:

```bash
# Check all of the projects you belong to in one go:

for g in $(/usr/bin/groups) ; do
  if [ -d "/scratch/$g" -a ! -L "/scratch/$g" ]; then
    dir="/scratch/purge_lists/$g" ;
  elif [ -d "/fmi/scratch/$g" ]; then
    dir="/fmi/scratch/purge_lists/$g";
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
    echo "is unclear, based on this script. Check with Service desk what to do.";
  fi ;
done
```

#### List your files

To get a simple list of all file paths in your purge list, simply give the `path_summary.txt` file
path as an argument:

```bash
# List all files in your purge list:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

If your `path_summary.txt` is big (over 100 MB in size), it may take some time to execute the tool.
You can save time and resources by saving the result into an output file:

```bash
# List all files in your purge list into an output file in your home folder:
lcleaner --out-file ~/purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Alternatively, you can redirect the standard output with the bash shell:
lcleaner "/scratch/purge_lists/${my_project:?}/path_summary.txt" > ~/purge_list

# Check the output with less, or your preferred text editor
less ~/purge_list
```

If you want to search for a specific file or directory, you can use `grep` to achieve that.
You can either search the `path_summary.txt` file directly, or if you saved the output of `lcleaner`
somewhere, using the commands above, you can use that file.

```bash
# Search for directories to check if they are included in the purge list
my_project="project_2001659" # Replace with your own project name!
grep "/scratch/${my_project:?}/important-dir" "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Or search the purge_list if you saved it:
grep "/scratch/${my_project:?}/important-dir" ~/purge_list

# If there are no matches, grep will not print anything.
```

#### Find the biggest files on the list

LCleaner has an option to sort the files by size. This option is called `--sort-by-size` and always
sorts in a decending order (i.e., biggest files first). If you want to see the size of the files
when they are printed, use the `--csv` option. By default, only the file paths are printed.
You can also limit the output to include a given number of files with the `--limit N` parameter,
where `N` is the number of lines you want to see.

```bash
# Print the file paths to be purged in size order:
lcleaner --sort-by-size "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print the 10 biggest files:
lcleaner --sort-by-size --limit 10 "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print the 10 biggest files, and their sizes in bytes:
lcleaner --sort-by-size --limit 10 --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"
```

#### Delete your purge list files

We encourage you to delete the files you do not need, instead of waiting for the automatic cleaning
to take place. If you are happy with purging all of the files that were listed in the
`path_summary.txt` file, you can run the following command:

!!! warning-label
    **The commands in this section will delete your files!** Be sure that you have reviewed the
    list of files to remove carefully! Also make sure that you have backed up the files you
    wish to save (outside the cluster) prior to running the commands. This operation is
    irreversible.

!!! Note
    The deletion process may take a considerable amount of time (several hours, depending on the
    amount of files), so it is best to start it within a `screen` or `tmux` session, so that you
    can disconnect from your SSH session while the deletion keeps running.

```bash
# Start a screen session
screen
# Delete all of the files on your purge list:
# Replace the "/path/to/my/path_summary.txt" with the path to your project's path_summary.txt
lcleaner -0 /path/to/my/path_summary.txt | xargs -0 -n 50 rm -vf --
# Then you can press "Ctrl + a" and then "d" to disconnect from the screen and keep
# the deletion running in the background.
# Run "screen -r" to reattach your screen.
# Close the screen session by typing "exit" in the shell.
```

If you want to delete only a part of the files, e.g., inside a certain directory, you can for
example use a command like this:

```bash
# Delete only files on the list which are inside /scratch/$my_project/delete-this-dir/
screen lcleaner -0 /path/to/my/path_summary.txt | grep -zZ "/scratch/${my_project:?}/delete-this-dir/" | xargs -0 -n 50 rm -vf --
# Ctrl + a, d to detach from the screen.
```

#### LCleaner output formats

If you want to see the size of the files that are about to be purged, you can use either the JSON
or the CSV formats. Be aware that if you want to run multiple output formats at the same time,
you need to specify an output file path as well.
Using the `-0` or `--nullbyte` parameters will output the file paths separated by a null byte,
which may be useful to avoid problems with whitespace in the file paths.

```bash
# Print your purge list as CSV output with file paths and sizes.
# Note that the CSV format also prints a header row.
lcleaner --csv "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Print your purge list as JSON output with file paths and sizes:
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# TIP: You can pipe the output into the jq program to prettify the output.
# The dot at the end is a mandatory argument to jq.
lcleaner --json "/scratch/purge_lists/${my_project:?}/path_summary.txt" | jq .

# Output both JSON and CSV into purge_list.json and purge_list.csv:
lcleaner --json --csv --out-file purge_list "/scratch/purge_lists/${my_project:?}/path_summary.txt"

# Output file paths separated by null bytes:
lcleaner -0 "/scratch/purge_lists/${my_project:?}/path_summary.txt"
# Usually you will want to pipe null-byte-separated output into "xargs -0" and do some
# further processing with it. For example like this:
lcleaner -0 --limit 3 "/scratch/purge_lists/${my_project:?}/path_summary.txt" \
  | xargs -0 -Ifilepath echo "I should run: rm -vf 'filepath'"
```

Output examples:

```
# Plain text:
[westersu@puhti-login11 ~]$ lcleaner path_summary.txt | head -3
/scratch/westersu/my-old-files/file1
/scratch/westersu/my-old-files/file2
/scratch/westersu/my-old-files/file3

# CSV:
[westersu@puhti-login11 ~]$ lcleaner --csv path_summary.txt | head -4
"path","size"
"/scratch/westersu/my-old-files/file1","1704"
"/scratch/westersu/my-old-files/file2","452"
"/scratch/westersu/my-old-files/file3","4951"

# JSON, piped into jq:
[westersu@puhti-login11 ~]$ lcleaner --json path_summary.txt | jq .
{
  "lustre_files": [
    {
      "size": 1704,
      "path": "/scratch/westersu/my-old-files/file1"
    },
    ...
  ]
}

# Null byte xargs:
[westersu@puhti-login11 ~]$ lcleaner -0 --limit 3 path_summary.txt \
>   | xargs -0 -Ifilepath echo "I should run: rm -vf 'filepath'"
I should run: rm -vf '/scratch/westersu/my-old-files/file1'
I should run: rm -vf '/scratch/westersu/my-old-files/file2'
I should run: rm -vf '/scratch/westersu/my-old-files/file3'
```

### Notes on LCleaner usage

This section details some things that may be good to know about how LCleaner behaves, or
why the command examples above are architected the way they are.

- Sometimes `lcleaner` prints errors about lines it wasn't able to parse.
  If there are errors, a warning will be printed at the end, indicating that there was at least
  one error. The warnings will say something like: "We detected N errors during the execution.
  Please check the logs, for more information!"
  The errors indicate which line number the problematic text was on, so you can go
  and check it manually.
    - Tip: To print only a specific line, e.g., line 123 of the `path_summary.txt`, you can use
      this command: `sed -n 123p /path/to/path_summary.txt`
- To capture the logging of `lcleaner`, you can redirect the standard error output stream into
  a file. This may be useful if you experience problems, and would like help to troubleshoot
  the situation.
    - `lcleaner --log-level debug path_summary.txt 2> ~/lcleaner-debug-$(date +%s).log`
- The use of `-0` both with `lcleaner` and `xargs` in the example commands on this page is
  recommended in order to avoid problems with file names that include whitespace.
- LCleaner also has some administrative functionality, which is not intended and in some cases
  will not work for unprivileged users. Anything which mentions the `--admin-mode` flag can safely
  be ignored.

### Troubleshooting LCleaner

If you notice any bugs, please report them to [CSC Service Desk](../contact.md).
