# Linux basics tutorial for CSC

The servers of CSC use Linux operating systems. While the user's local
computer is normally used mainly through a graphical user interface,
the remote usage of the servers of CSC is in most cases based on
working on command-line: instead of using mouse and command menus,
the user types commands to a screen called terminal or console.
Even though more and more tools provided by CSC can be used through
[graphical interfaces](../../../computing/webinterface/index.md), using
the basic Linux commands is in many cases still the most efficient way.

This tutorial provides an introduction to the usage of the Linux
environment of CSC. Puhti is used in the examples, but the same
commands can be used in the other servers of CSC, too. If you
are using Linux or macOS machine, you can also use most of
the commands in a terminal on your local machine. Once you are
familiar with the basic Linux commands, you can continue to
topics that go deeper to the file and data management commands of
Linux systems.

This guide is accurate for bash shell only. Bash is the default
command shell in the CSC computing environment. We recommend to
stick with this choice if no special reason for another shell
flavor is given.

* [**Using Linux in command-line**](using-linux-in-command-line.md)
    * [Files and directories in Linux](using-linux-in-command-line.md#files-and-directories-in-linux)
    * [Structure of Linux commands](using-linux-in-command-line.md#structure-of-linux-commands)
    * [Basic commands for using directories](using-linux-in-command-line.md#basic-commands-for-using-directories)
    * [Basic commands for files](using-linux-in-command-line.md#basic-commands-for-files)
    * [Special characters](using-linux-in-command-line.md#special-characters)
* [**Editing text and viewing images**](text-and-image-processing.md)
    * [nano](text-and-image-processing.md#nano)
    * [Emacs](text-and-image-processing.md#emacs)
    * [vi and Vim](text-and-image-processing.md#vim)
    * [Image and PostScript viewers](text-and-image-processing.md#image-and-postscript-viewers)
* [**Working with bash shell**](working-with-bash-shell.md)
    * [Automatic tab completion](working-with-bash-shell.md#automatic-tab-completion)
    * [Stopping programs and running programs in background](working-with-bash-shell.md#stopping-programs-and-running-programs-in-background)
* [**More commands for managing files**](more-commands-for-managing-files.md)
    * [Using `find` to locate files](more-commands-for-managing-files.md#using-find-to-locate-files)
    * [`file` command tells the file type](more-commands-for-managing-files.md#file-command-tells-the-file-type)
    * [Count rows and characters with `wc`](more-commands-for-managing-files.md#count-rows-and-characters-with-wc)
    * [Comparing two files with `diff`](more-commands-for-managing-files.md#comparing-two-files-with-diff)
    * [Using checksums to verify successful data storage or transfer](more-commands-for-managing-files.md#using-checksums-to-verify-successful-data-storage-or-transfer)
    * [Encrypting files with GPG](more-commands-for-managing-files.md#encrypting-files-with-gpg)
    * [Managing access permissions of files and directories](more-commands-for-managing-files.md#managing-access-permissions-of-files-and-directories)
* [**Commands for data processing**](commands-for-data-processing.md)
    * [`grep` selects rows that match a given string](commands-for-data-processing.md#grep-selects-rows-that-match-a-given-string)
    * [Using `sed` to select rows by row number](commands-for-data-processing.md#using-sed-to-select-rows-by-row-number)
    * [Simple column selection with `cut`](commands-for-data-processing.md#simple-column-selection-with-cut)
    * [Using `awk` to work with columns](commands-for-data-processing.md#using-awk-to-work-with-columns)
    * [Using `sort` to order rows](commands-for-data-processing.md#using-sort-to-order-rows)
    * [Removing duplicate rows with `uniq`](commands-for-data-processing.md#removing-duplicate-rows-with-uniq)
    * [Replacing characters with `tr`](commands-for-data-processing.md#replacing-characters-with-tr)
    * [Replacing words and strings with `sed`](commands-for-data-processing.md#replacing-words-and-strings-with-sed)
* [**Packing and compression tools**](packing-and-compression-tools.md)
    * [tar: packing several files into one file](packing-and-compression-tools.md#tar-packing-several-files-into-one-file)
    * [Compressing files](packing-and-compression-tools.md#compressing-files)
        * [gzip and gunzip](packing-and-compression-tools.md#gzip-and-gunzip)
        * [bzip2 and bunzip2](packing-and-compression-tools.md#bzip2-and-bunzip2)
        * [zip and unzip: the combined compression and file archiving tool](packing-and-compression-tools.md#zip-and-unzip-the-combined-compression-and-file-archiving-tool)
        * [7zip packing and compression tool](packing-and-compression-tools.md#7zip-packing-and-compression-tool)
        * [Zstandard compression tool](packing-and-compression-tools.md#zstandard-compression-tool)
* [**Linux bash scripts**](linux-bash-scripts.md)
    * [Constructing a script file](linux-bash-scripts.md#constructing-a-script-file)
    * [Variables and arrays](linux-bash-scripts.md#variables-and-arrays)
    * [Quotation marks](linux-bash-scripts.md#quotation-marks)
    * [Loops and conditional statements](linux-bash-scripts.md#loops-and-conditional-statements)
    * [Printing the output](linux-bash-scripts.md#printing-the-output)
