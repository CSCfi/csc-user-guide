# 2. Linux basics for CSC {#linux-basics-for-csc align="JUSTIFY"}

The servers of CSC use Linux operating systems. While the user's local
computer is normally used mainly through a graphical user interface, the
remote usage of the servers of CSC is in most cases based on working on
command line: instead of using mouse and command menus, the user types
commands to a screen called *terminal* or *console*. Even though more
and more tools provided by CSC can be used through graphical interfaces,
using the basic linux commands is in many cases still the most efficient
way.

This chapter provides introduction to the usage of the Linux environment
of CSC. The application server, *puhti-shell.csc.fi*, is used in the
examples but the same commands can be used in the other servers of CSC,
too. If you are using Linux or Mac OSX machine, you can also use most of
the commands in a terminal on your local machine. Once you are familiar
with the basic Linux commands, you can continue to chapters that go
deeper to the file and data management commands of Linux systems.

The recommended command shell in the CSC computing environment is
**bash**, which is also a default for the new users. We recommend to
stick with this choice if no special reason for another flavour is
given. Previously, before 1st June 2012, the default was **tcsh**, which
still can be used, as well as other shells like **csh**, **sh** or
**ksh**. Users can change their default shell from within SUI -
Scientist User Interface on <https://sui.csc.fi>.

This guide is accurate for bash shell only. If you are using some other
Linux command shell, e.g. tcsh, some instructions/details may not apply
or work.

## [2.1 Using Linux in command line]

[2.1.1 Files and directories in linux][]  
[2.1.2 Structure of linux commands][]  
[2.1.3 Basic commands for using directories][]  
[2.1.4 Basic commands for files][]  
[2.1.5 Special characters][]  
[2.1.5.1 Wild card characters][]  
[2.1.5.2 Redirecting standard input and output]

##  [2.2 Editing text and viewing images]

[2.2.1 Nano][]  
[2.2.2 Emacs][]  
[2.2.3 Vim][]  
[2.2.3 Image and PostScript viewers][2.2.3 Vim]

## [2.3 Working with bash shell]

[2.3.2 Automatic Tab completion][]  
[2.3.3 Stopping programs and running programs in background]

## [2.4. More commands for managing files]

[2.4.1 Using find to locate files][]  
[2.4.2 File command tells the file type][]  
[2.4.3 Count rows and characters with wc][]  
[2.4.4 Comparing two files with diff][]  
[2.4.5 Using checksums to verify successful data storage or
transfer][]  
[2.4.6 Encrypting files with gpg][]  
[2.4.7 Managing access permissions of files and directories][]  
[2.4.8 Managing access permissions with Scientist's User Interface][]  
[2.4.9 Managing access permissions in command line usage]  
 

## [2.5 Commands for data processing]

[2.5.1 Grep selects rows that match given string][]  
[2.5.2 Using sed to select rows by row number][]  
[2.5.3 Simple column selection with cut][]  
[2.5.4 Using awk to work with columns][]  
[2.5.5 Using sort to order rows][]  
[2.5.6 Removing duplicate rows with uniq][]  
[2.5.7 Replacing characters with tr][]  
[2.5.8 Replacing words and strings with sed]

##  [2.6 Packing and compression tools]

[2.6.1 Tar and gtar: packing several files into one file][]  
[2.6.2 Compressing files][]  
[2.6.2.1 Gzip and gunzip][]  
[2.6.2.2 bzip2 and bunzip2][]  
[2.6.2.3 Zip and unzip: combined compression and file packing tool][]  
[2.6.2.4 7zip packing and compression tool][]  
[2.6.2.5 Zstandard compression tool]  

## [2.7 Linux bash scripts]

[2.7.1 Constructing a script file][]  
[2.7.2 Variables and arrays][]  
[2.7.3 Quotation marks][]  
[2.7.4 Loops and conditional statements][]  
[2.7.5 Printing the output]

 

  [2.1 Using Linux in command line]: https://research.csc.fi/csc-guide-using-linux-in-command-line
  [2.1.1 Files and directories in linux]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.1
  [2.1.2 Structure of linux commands]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.2
  [2.1.3 Basic commands for using directories]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.3
  [2.1.4 Basic commands for files]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.4
  [2.1.5 Special characters]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.5
  [2.1.5.1 Wild card characters]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.5.1
  [2.1.5.2 Redirecting standard input and output]: https://research.csc.fi/csc-guide-using-linux-in-command-line#2.1.5.2
  [2.2 Editing text and viewing images]: https://research.csc.fi/csc-guide-text-and-image-processing
  [2.2.1 Nano]: https://research.csc.fi/csc-guide-text-and-image-processing#2.2.1
  [2.2.2 Emacs]: https://research.csc.fi/csc-guide-text-and-image-processing#2.2.2
  [2.2.3 Vim]: https://research.csc.fi/csc-guide-text-and-image-processing#2.2.3
  [2.3 Working with bash shell]: https://research.csc.fi/csc-guide-working-with-bash-shell
  [2.3.2 Automatic Tab completion]: https://research.csc.fi/csc-guide-working-with-bash-shell#2.3.2
  [2.3.3 Stopping programs and running programs in background]: https://research.csc.fi/csc-guide-working-with-bash-shell#2.3.3
  [2.4. More commands for managing files]: https://research.csc.fi/csc-guide-more-commands-for-managing-files
  [2.4.1 Using find to locate files]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.1
  [2.4.2 File command tells the file type]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.2
  [2.4.3 Count rows and characters with wc]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.3
  [2.4.4 Comparing two files with diff]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.4
  [2.4.5 Using checksums to verify successful data storage or transfer]:
    https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.5
  [2.4.6 Encrypting files with gpg]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.6
  [2.4.7 Managing access permissions of files and directories]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.7
  [2.4.8 Managing access permissions with Scientist's User Interface]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.8
  [2.4.9 Managing access permissions in command line usage]: https://research.csc.fi/csc-guide-more-commands-for-managing-files#2.4.9
  [2.5 Commands for data processing]: https://research.csc.fi/csc-guide-commands-for-data-processing
  [2.5.1 Grep selects rows that match given string]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.1
  [2.5.2 Using sed to select rows by row number]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.2
  [2.5.3 Simple column selection with cut]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.3
  [2.5.4 Using awk to work with columns]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.4
  [2.5.5 Using sort to order rows]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.5
  [2.5.6 Removing duplicate rows with uniq]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.6
  [2.5.7 Replacing characters with tr]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.7
  [2.5.8 Replacing words and strings with sed]: https://research.csc.fi/csc-guide-commands-for-data-processing#2.5.8
  [2.6 Packing and compression tools]: https://research.csc.fi/csc-guide-packing-and-compression-tools
  [2.6.1 Tar and gtar: packing several files into one file]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.1
  [2.6.2 Compressing files]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2
  [2.6.2.1 Gzip and gunzip]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2.1
  [2.6.2.2 bzip2 and bunzip2]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2.2
  [2.6.2.3 Zip and unzip: combined compression and file packing tool]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2.3
  [2.6.2.4 7zip packing and compression tool]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2.4
  [2.6.2.5 Zstandard compression tool]: https://research.csc.fi/csc-guide-packing-and-compression-tools#2.6.2.5
  [2.7 Linux bash scripts]: https://research.csc.fi/csc-guide-linux-bash-scripts
  [2.7.1 Constructing a script file]: https://research.csc.fi/csc-guide-linux-bash-scripts#2.7.1
  [2.7.2 Variables and arrays]: https://research.csc.fi/csc-guide-linux-bash-scripts#2.7.2
  [2.7.3 Quotation marks]: https://research.csc.fi/csc-guide-linux-bash-scripts#2.7.3
  [2.7.4 Loops and conditional statements]: https://research.csc.fi/csc-guide-linux-bash-scripts#2.7.4
  [2.7.5 Printing the output]: https://research.csc.fi/csc-guide-linux-bash-scripts#2.7.5
