# Data-mover

Data-mover is a tool to move data between Puhti and Mahti local filesystems and
Allas and LUMI-O object storage servers, when
[simple transfers](../faq/how-to-move-data-between-puhti-and-allas.md#move-data-with-rclone)
are not practical, either because there are many small files, or the size of the
dataset is large.

We wish the data-mover tool `dm` to be simple to use, and handle all possible
hard corner cases. It is basically a wrapper around [Restic backup tool](https://restic.readthedocs.io)
, and stores the data in Restic repositories.
Restic in turn uses [Rclone](https://rclone.org) for the actual data transfers to
the object storage servers and back. In addition, the data-mover tool does the
data transfers in the background, using batch jobs, allowing larger transfers
than would be practical in regular interactive login sessions.

Below is a guide for a simple scenario, moving data from Puhti project scratch
directory to corresponding project in Allas, and then back. Similar works with
Mahti and LUMI-O. Please have a look at `dm help` and `dm <sub-command> --help`
for additional documentation.

## Setting up the connection from Puhti to Allas

1. Your CSC project needs to have Allas service enabled. The project PI can add
Allas service for the project in [my.csc.fi](https://my.csc.fi) , if not already enabled, and
the project members need to [accept the service terms](../../accounts/how-to-add-service-access-for-project.md).

2. Create a configuration for rclone and store the authentication token in the
file `$HOME/.config/rclone/rclone.conf` in Puhti. This is easiest to do from
[Puhti web interface](https://puhti.csc.fi). Open "Cloud storage configuration" from the
"Tools" drop-down menu, and
[create Allas S3 rclone configuration for the project](../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o).

4. Open a terminal to Puhti, and take the data-mover tool `dm` into use with
```
module load .data-mover
```

## Moving data from Puhti to Allas

1. Put the data in a single directory, for example
`/scratch/project_<projid>/exampledir` in Puhti, _deleting all the files that
you do not need_. There is no need to compress the files.

2. Move the data to Allas
```
dm export /scratch/project_<projid>/exampledir
```

3. Check the status of the data transfer with
```
dm status
```

## Listing the data in Allas

```
dm list
```

## Moving data from Allas to Puhti

Import data back to the original directory with
```
dm import /scratch/project_<projid>/exampledir
```

## Links to related material

- [Lue tool for data inventory](lue.md)
- [Data cleaning](clean-up-data.md)
- [Allas introduction](../../data/Allas/introduction.md)
