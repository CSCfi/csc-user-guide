# LUE

!!! Note
    While we try our hardest to make tools easy to use, parallel file systems with a
    huge amount of files and data are complicated. Read the full instructions before
    using the tool!

Keeping track of how much data/files one has on the disk and (re)moving it in a
timely manner ensures a more performant file system for all users.

When querying size information it's important to limit the processed set of files.
Some operations can be both slow and heavy on the file system. In other words, don't
run the tool on the whole project folder (e.g `/scratch/project_12345`), but choose
instead smaller sub-folders where you think you might have a lot of files or data
which could possibly be moved/compressed/removed. By default, the tool will only
fetch size data for 30 mins before quitting.

## Short prelude

LUE is a tool available on CSC supercomputers which shows the amount of data and
number of files within a given folder on the parallel file system.

Importantly, LUE is significantly faster than standard tools like `stat` or `du`
(these being slow to the point of infeasibility on a bad day), while being nicer
on the file system. This, however, comes with a possible slight loss in accuracy.

A secondary point is that LUE presents the results in a fairly understandable way,
saving the user from having to script something themselves based on raw `du` output.

The sources of possible inaccuracy are:

1. Old files which have not been accessed are missing size data.
      - There is a specific date (2020-11-18) before which data is not available on
        **Puhti**. Mahti does not have a such a limitation.
      - Files created/accessed after this should be ok.
      - It's not always possible to accurately determine affected files in a
        sufficiently efficient manner.
2. We can't get the actual layout of the files on the disk, so we might slightly
   overestimate the actual disk usage.
      - A file which is 95 MB large might only consume 68 MB of disk space if it
        contains large parts of only zeros.
3. Files which are currently in use might not be reported correctly.

## Basic usage

Load the module with:

```bash
module load lue
```

and start by running

```bash
lue <target_dir>
```

### Output

```text
Total size: 8994868686 Processed files: 90551 Permission denied: 16 Missing size: 48955, Other err: 1
path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/scratch/project_12345/dirA  8.4GB  356KB 100.0 100.0
    results                       3.7GB  458MB 44.15 44.15 NOSIZE:2
    installations                 1.4GB  48KB  16.2  16.2 
    datasetA                      684MB  64KB  7.9   7.9
    datasetB                      530MB  56KB  6.12  6.12  NOPERM:1 NOSIZE:17
    testing                       512MB  8KB   5.92  5.92 
    images                        395MB  764KB 4.56  4.56 
    numpy-git                     292MB  12KB  3.37  3.37 
    newAB                         263MB  412KB 3.04  3.04  NOPERM:9 NOSIZE:953
    cuda_old                      249MB  4KB   2.87  2.87 
    AI-simu                       176MB  52KB  2.03  2.03  NOSIZE:43491
    mpi-test                      60MB   52KB  0.69  0.69 
WARNING: Size information is missing for 48956 files
Rerun with --sync-size to update size information, estimated duration: 43 seconds
```

While the tool is running it will print how many files it has processed, the total
size of the files, how many directories could not be opened and how many files did
not have a reported size.

!!! info
    Using the `-c/--count` flag you can display the number of files instead of the
    amount of data.

Once the tool is finished going through the files, it will print the size of `<target_dir>`
and the size of any sub-folders. The columns from left to right are:

- The directory/file name
- The total size of the directory (including subdirectories) or the size of the file
- The size of all files in a directory (excluding subdirectories)
- How many percent the directory or file is of the total size of `<target_dir>`
- How many percent the directory or file is of the total size of its parent directory
- Counts of how many directories could not be opened (`NOPERM`) or how many files
  were missing size information (`NOSIZE`)

!!! info
    **If we could not open a directory we have no estimate on how much data is
    contained in that directory**. See [updating-size](#updating-size) for how to
    fix the `NOSIZE` error. The `NOPERM` error requires the owner of the directories
    to fix the access rights.

By default, files or empty folders are not shown in the output. Use `--show-all`
to override this.

Using `--display-level=<n>` we can show a deeper hierarchy to get more detailed
information.

```bash
$ lue --display-level=2 /scratch/project_12345/

path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/scratch/project_12345/dirA        8.4GB  356KB 100.0 100.0
    results                            3.7GB  458MB 44.15 44.15
        simu1                              2.8GB  522MB 32.84 74.38 NOSIZE:1
        simu2                              521MB  521MB 6.02  13.64 NOSIZE:1
    installation                       1.4GB  48KB  16.2  16.2 
        gcc10                              351MB  351MB 4.05  25.02
        gcc11                              351MB  351MB 4.05  25.02
        clang15                            351MB  351MB 4.05  25.02
        intel                              350MB  350MB 4.04  24.94
```

Alternatively, we can just run the tool on one of the sub-folders to get a smaller,
less cluttered output.

```bash
$ lue /scratch/project_12345/dirA/result

path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/scratch/project_12345/dirA/result           3.7GB  458MB 100.0 100.0
    simu1                                        2.8GB  522MB 74.38 74.38 NOSIZE:1
    simu2                                        521MB  521MB 13.64 13.64 NOSIZE:1
```

LUE keeps a very simple cache of runs. After running LUE on `/scratch/project_12345/dirA/`
you can run it on any subdirectories without actually re-querying anything from the file system.
To force the tool to refresh the data (for example if a run needs other options or the cache
is to old), use `--refresh`. The cache is saved under `$TMPDIR`, so if you switch nodes, you
will need to rerun.

Using the `--yaml file.yaml` and `--json file.json` options you can save the output
in a more parsable format instead of printing it to the screen.

## Updating size

As mentioned, files which have not been accessed since _2020-11-18_ are not reported
correctly. Note that this applies only for **Puhti**, Mahti does not have this limitation.

Next follows the steps to correct this. This procedure needs to be done only once,
after which the size should be reported correctly:

1. Run `lue <target_dir>`.
      - If no warnings are printed and there are no `NOSIZE` labels, the reported size
        should be fairly accurate. No need for further steps.
2. Rerun `lue --sync-size <target_dir>`. The previous command should have reported
   the number of affected files and a (very) rough estimate of the duration.
      - A progress bar will be updated to show how many files have been processed and
        how many files could not be updated due to insufficient permissions.
3. Rerun `lue --refresh <target_dir>`.
      - Shown size should be fairly accurate.

**If there are still `NOSIZE` labels reported:**

1. Some files could not be updated due to insufficient permissions.
      - The number of affected files was reported when running with `--sync-size`.
         - If the number matches the number of `NOSIZE`, there is no need for steps 2. and 3.
      - Can only be remedied by the owner fixing the access permissions.
      - If the number of affected files is small (<1000), you can rerun with
        `lue --refresh <target_dir> --stat-unsynced` to get more accurate size info,
        although this will be a bit slower.
2. Some files require much heavier operations to sync the size.
      - Rerun with `lue --sync-size --slow-sync <target_dir>`. **NOTE!** Adding the
        `--slow-sync` option will be about x10 slower than with just `--sync-size`
      - Before doing this run `lue` on some of the sub-folders (without `--refresh`)
        to find out where the `NOSISZE` files are located. Then use `ls -l` or `du -h`
        to confirm that the files are actually not zero in size. If the files seem to
        be non-zero in size, run with `--slow-sync`. Otherwise go to 3.
      - Usually this step is not needed.
3. Some files are very old and have an actual size of zero -> we have incorrectly
   flagged them.
      - If you know that you have a program/framework which produces a lot of empty
        files, consider removing those before running the tool.
      - If you already ran with `--slow-sync` or confirmed that it was not needed, you
        can add the `--no-guess` flag to not report these files.

## Limiting the runtime

It's a good idea to limit the runtime of the tool, and often we get useful information
even though we did not go through the folder structure exhaustively. If you press
`Ctrl-C` to interrupt the tool, the processed information will be saved and you can
rerun without `--refresh` to view the results. Other options to limit the runtime are:

`--timeout <n>`

: Stop after `<n>` minutes (default 30min if `--timeout` is not set)

`--file-limit <n>`

: Stop the search after going through a set amount of files.

`--size-limit <n>`

: Stop the search after reaching a set total size. Supported units are K, M, G, T.
  If no suffix is used G is assumed.

`--search-depth <n>`

: Limit search depth to `<n>`. Default is no limit.
