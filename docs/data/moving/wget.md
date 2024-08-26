# Using wget to download data from websites to CSC

`wget` is a command for downloading files from  WWW-sites and FTP servers. Once
you have resolved the URL of the file, just give it as an argument to the
`wget` command to download the file to your current directory.

```bash
wget URL
```

For example:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.2.tar.gz
```

would download a file called `gromacs-2024.2.tar.gz` to your current directory.
Pattern matching in the URL is possible when using FTP, i.e. the URL starts
with `ftp://`:

```bash
wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.*.tar.gz
```

This command would retrieve all the files, whose name start with
`gromacs-2024.` and end with `.tar.gz`.

You can fine tune the behavior of the `wget` command with several options. You
can see the full list of available command options with the command:

```bash
man wget
```

Below are listed some of the most commonly used options.

|Option      |Argument |Description  |
|------------|---------|-------------|
|`-i`        |URL      |Read a file containing the URLs to retrieve.|
|`-O`        |file name|Name of the output file.|
|`-o`        |file name|Name of the download log file.|
|`-p`        |directory|Defines the directory where the downloaded data will be saved to. The default is the current directory.|
|`-c`        |         |Continue getting a partially-downloaded file.|
|`--user`    |username |Specify the username for file retrieval.|
|`--password`|password |Specify the password for file retrieval.|
|`-N`        |         |Use time-stamping. Download the file only if it is newer that the file in the target directory.|
|`-m`        |         |Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings.|
