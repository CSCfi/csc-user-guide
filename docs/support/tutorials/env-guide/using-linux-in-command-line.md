# Using Linux from the command-line

## Files and directories in Linux

The file systems in Linux machines are based on a hierarchical directory
tree. There is one *root directory* which you can refer to with the
*forward slash symbol* (`/`). All the files and directories are located in the
subdirectories of this directory, so that each file has a unique
combination of a name and a directory path. Also, the commands that the user
gives are executed in the directory that the user currently is in. It is
called the *current working directory*.

Normally, you do not need to know the explicit directory paths when you
work in the CSC environment. It is enough to know the locations of the
files in the user's own disk areas. However, you should remember that many disk
areas in the CSC environment can be accessed from several servers
(e.g., the user's home directory) while some areas are server-specific. In
the case of shared disk areas, the path to a certain file may be
different on different servers.

## Structure of Linux commands

Once a terminal connection to CSC, e.g., to Puhti, has been
opened, the remote server is operated by using Linux commands. The standard
structure of a command is:

```bash
command -options argument1 argument2 ...
```

The command is executed by pressing the *return key (Enter)*. The names
and functions of the options and the arguments depend on the Linux command. In
many cases, you can run the command without any options or arguments.
Options are used to modify the actions that the command performs.
Arguments are used to define the files, directories and values that are
used as input parameters and to define where the output is written.

For example, the command `ls` can be used as such or with several options
and arguments. Running a plain command `ls` lists the contents of a
directory in alphabetical order. You can modify the output of the
command, for example, by using the option `-t`. With this option, the
directory content list is ordered according to the age of the file (timestamp).
If no argument is given, `ls` prints the content of the current
working directory. By giving an argument to the `ls` command, the user can
define a directory whose content should be listed. For example, the command

```bash
ls -t /scratch/project_2979797
```

will list the content of directory `/scratch/project_2979797`. In case there
are errors in the command,
the arguments or the options, the command will not be executed
when the return key is pressed. Instead, an error message is printed to
the screen. Thus, having errors in the command often does not cause
any major problems. Issues may arise when using undefined shell variables. 
The output of commands varies from one command to the other but in
many cases, no output means that command was successfully executed.

Most of the Linux commands have their own manual page that can be
studied using the `man` command. For example, the manual page of `ls`
command is shown using the command

```bash
man ls
```

Manual pages can be very detailed and technical. However, often you
do not need to read and understand all the details given there,
but instead, you can just see what command-line options are available for
the particular command, which are of interest to you and then start
testing/using them in practice.

There are thousands of Linux commands, though, you do not need to know 
the majority of them in order to get started. 
Below, we introduce the most frequently used ones. You can also use 
the command `apropos` to find a suitable command. 
Apropos lists those Linux commands whose short description
lines match the text that is given as a command argument. For example, 
if you want to look for commands that are processing *pdf* files, you 
could type

```bash
apropos pdf
```

Note that the listing that `apropos` prints includes only Linux
commands, not program names. Thus, the sample command
above would produce a list that contains many pdf conversion commands but
no pdf viewers such as `acroread` or `evince`.

## Basic commands for using directories

The table below lists the commands that are most frequently used for moving in
the directory hierarchy and managing it. Below are some examples of
directory related commands.

| Name    | Argument    | Description                                           |
|---------|-------------|-------------------------------------------------------|
| `cd`    | *directory* | Change current working directory                      |
| `ls`    | *directory* | List the contents of a directory                      |
| `pwd`   |             | Print the directory path of current working directory |
| `mkdir` | *directory* | Create a new directory                                |
| `rmdir` | *directory* | Remove a directory                                    |

When you log in to a server at CSC, you will be taken to your home
directory. You can check your location, i.e., the path of the current
working directory with the command `pwd` (abbreviation of Print
current Working Directory). However, you do not have to remember the
location of your home directory (see the `cd` command).

The contents of the directory can be listed with the `ls` command.
The plain `ls` command just lists the names of the files and directories in
your current directory. You can get more information about the files and
directories with command `ls -la`. The `-l` option produces a long
directory listing that, in addition to the name, contains also information
about the access permissions, the size and the modification time of files and
directories. The option `-a` defines that all files, including also
hidden files that start with dot (`.`) character, are listed. Below
is a sample output for `ls -la` command:

```bash
$ ls -la
total 26914
drwx------+ 3  kkayttaj csc         10 Dec 22 09:12 .
drwxr-xr-x  20 root     root         0 Dec 22 09:12 ..
drwx------+ 42 kkayttaj csc        472 Dec 22 09:07 ..
-rwxr-x---+ 1  kkayttaj csc       1648 Dec 22 09:01 .cshrc
-rw-------+ 1  kkayttaj csc         93 Dec 22 09:01 .my.cnf
-rw-------+ 1  kkayttaj csc         48 Dec 22 09:05 Test.txt
-rw-------+ 1  kkayttaj csc     878849 Jan 19 2009  input.table
drwxr-xr-x+ 2  kkayttaj csc          2 Dec 22 09:11 project1
-rw-------+ 1  kkayttaj csc   26432051 Dec 22 09:08 results.out
-rw-------+ 1  kkayttaj csc         25 Mar 27 2009  sample.data
-rw-------+ 1  kkayttaj csc         49 Mar 27 2009  test.txt
```

The first output row `total 26914` tells that the total size of the
files in the directory is 26914 kB. In the list, the first character
tells if the item is a file (`-`) or a directory (`d`). The next nine
characters display the *access permissions* of the files (see the
`chmod` command for more details). The next columns show the number of
links pointing to the item, owner, user group, size in bytes,
modification time and the name of the file or directory.

By default, files are presented in alphabetical order. You can order
the results by modification time with the option `-t` or by size with the
option `-S` (note: uppercase S, not lowercase s). Two other
frequently used options are `-h` (human-readable) which prints out the
sizes of large files in megabytes or gigabytes, and `-r` which means
reverse sorting order. For example, the command

```bash
ls -ltrh
```

is very handy when you want to check what files have recently been
modified or created. The `ls` and `pwd` commands do not modify files in
any way, so you can use them always when you want to know where you are
and what files your current directory contains.

The command `cd directory_name` moves you from the current
directory to a directory you specified. For example, the user `kkayttaj`
could go to their local temporary directory using the command

```bash
cd /local_scratch/kkayttaj
```

or

```bash
cd $TMPDIR
```

In the latter command, the automatically defined *environment variable*
`$TMPDIR` that contains the explicit directory path is used to define
the target directory.

New directories can be created with the command `mkdir directory_name`.
For example, the command:

```bash
mkdir project1 
```

Creates a new directory called `project1`. You can use the `ls` command to
check that the directory was created. Now you can go to this directory
with the command

```bash
cd project1 
```

You can come back from the `project1` directory using the command

```bash
cd .. 
```

Note the space between `cd` and the dots in the command. One dot (`.`) and
two dots (`..`) have a special meaning in Linux. One dot (`.`)
means the *current directory*, and two dots (`..`) means the directory that
is one level up in the directory tree, i.e., the directory where the current
directory resides. Executing the `cd` command without any arguments will
always move you back to your home directory, regardless of where you are in
the directory tree. An empty directory can be removed with the command
`rmdir directory_name`. For example:

```bash
rmdir project1
```

## Basic commands for files

On a fundamental level, a file in a Linux system is just a string of
bytes, were a byte consists of eight bits. So-called text files
contain only bytes that can be interpreted as text characters using the
ASCII encoding rules. Thus, these files can be considered as consisting of
lines of text. In so-called binary files, also non-ASCII bytes are used,
and they cannot and are not intended to be convertible to readable text.
Typical examples of binary files are compiled programs, images or compressed
files. Normally, users work mostly with text files, and also in the examples of
this guide, we normally assume that the files contain some kind of text
data: letters or numbers.

Each file has a name. The name can, in principle, be any combination of
characters. However, several characters have a special meaning, e.g.,
`?`, `*` and `#`, see [below](#special-characters) and
thus, using these characters in filenames may cause problems. We
recommend that you only use ordinary letters (lower- or uppercase),
numbers, dots (`.`), dashes (`-`) or underscores (`_`) in
file and directory names. Also, using space characters in filenames 
may cause problems. We recommend that space characters are
replaced by underscores, for example, `new_file.txt` instead of `new file.txt`.
Note that Linux is case-sensitive: lower- and uppercase characters are not
considered equal unlike in Windows computers, and, e.g., the names
`New_File.txt` and `new_file.txt` refer to different files.

In Linux, the usage of filename extensions such as `.doc` or `.txt` is not
obligatory. Most Linux tools do not require an extension to be specified.
However, in the long run, using systematic naming conventions, including
illustrative name extensions, makes file management easier.

File-processing commands:

| Name    | Argument     | Description                                         |
|---------|--------------|-----------------------------------------------------|
| `cat`   | *file_names* | Print the contents of the specified file or files to the standard output (your screen) |
| `chmod` | *file_names* | Change the access permissions of a file             |
| `cp`    | *file_name1*<br>*file_name2* | Copy the file contents to a new file or new location |
| `grep`  | *search_string*<br>*file_name* | Pick from the file the rows that contain a specific string |
| `head`  | *file_name*  | Print the first rows of the file to the standard output (your screen) |
| `tail`  | *file_name*  | Show the last rows of a file                        |
| `less`  | *file_name*  | Show the contents of a file one screenful at a time |
| `more`  | *file_name*  | Show the contents of a file one screenful at a time |
| `ln`    | *file_name*<br>*link_name* | Create a link to a file               |
| `mv`    | *file_name1*<br>*file_name2* | Rename a file or move it to another location |
| `rm`    | *file_names* | Remove files                                        |

You can explore the contents of text files using the commands `cat`,
`more` and `less`. These commands are safe to use as
they do not modify the files in any way. For example, you could read the
`.bashrc` file in your home directory with the commands

```bash
cat .bashrc
more .bashrc
less .bashrc 
```

The `cat` command (abbreviation for concatenate) prints the contents of
the specified file or files to the *standard output* which by default
means your screen. The pager programs `less` and `more` are often more
useful tools for studying text files as they allow the user to see the
content of the file one screenful at a time. In both programs, `more` and
`less`, you can move forward one line at a time by pressing the *Return key* or
one screenful at a time by pressing *Space*. You can exit from the file preview
by pressing `q`.

The `less` pager program is more advanced than `more`. For example, `less` can
browse text also backwards, either one row at a time by pressing `k` or
one screenful at a time by pressing `b`. You can also search a text
string from the document by using slash (`/`) character. For example,
to locate the string *ABC* in a file opened with `less`, type `/ABC`
and the press *Return*. Actually, the `man` command uses `less` as its pager.

The commands `head` and `tail` can be used to see just the
first and the last rows of a file, respectively. By default, these commands
print 10 lines, but you can change this by giving the number of rows
to be printed as an argument to a `head` or `tail` command. For example,
to check the last 30 rows of a file called `run1.log`, give the command

```bash
tail -30 run1.log 
```

Copying files to a new file or to another directory is done using the command
`cp` (copy). Below you can find two examples of copy commands:


```bash
cp output.dat output_copy.dat
cp output1.dat output2.dat results/
```

The first command makes a copy of file `output.dat` to a new file called
`output_copy.dat`. In the second example, the files `output1.dat`
and `output2.dat` are copied to an existing directory called `results`.
The command `mv` (move) is used to rename or move a file to
another location. For example:

```bash
mv output.dat output_copy.dat
mv output1.dat output2.dat results/ 
```

would create the same new files as the `cp` example commands. However, in the
case of `mv`, the original files `output.dat`, `output1.dat` and
`output2.dat` would be removed from the current working directory.

Files are removed using the command `rm filename`. By default, the file is
deleted immediately. If you would like to first confirm file deletion, you can
add a parameter to the command: `rm -i`.  To make this behavior permanent, you
can set an alias in your `.bashrc`:

```bash
alias rm="rm -i"
```

Note that after editing your `.bashrc` file, you need to use the
`source ~/.bashrc` command or open a new shell. After that, the `rm` command
will always ask the user to confirm that they really want to remove the
file:

```bash
$ rm output_copy.dat
rm: remove output_copy.dat (yes/no)?
```

You can answer `y` (yes) or `n` (no). Note that this confirmation step
is not necessarily in use in your local Linux environment or currently in
Puhti. You can skip the confirmation query using the option `-f`, standing for
*force*. However, you should use this option with caution as the `rm` command
will remove the file immediately and permanently!

## Special characters

Some characters have special functions in Linux. In the following
paragraphs, we present the characters that are used for redirecting standard
input and output or used as the so-called *wildcard characters*.

The `$` sign that serves as an indicator of a variable name, the `#`
symbol that is used to place comments, and the different kind of quotation
marks are discussed later on in the
[linux scripting chapter](linux-bash-scripts.md).

### Commonly used special characters

| Character | Function                                                        |
|-----------|-----------------------------------------------------------------|
| `$`       | Indicates a shell or environment variable                       |
| `|`       | Pipes standard output to the standard input of the next command |
| `#`       | Starts a comment                                                |
| `&`       | Executes a process in the background                            |
| `?`       | Matches one character                                           |
| `*`       | Matches any string (including an empty string)                  |
| `>`       | Output redirection operator                                     |
| `<`       | Input redirection operator                                      |
| `>>`      | Output redirection operator (to append to a file)               |
| `\`       | Ignore the possible special function of the following character |

### Wildcard characters

In Linux, a question mark (`?`) and an asterisk (`*`) are used as the so-called 
wildcard characters. They can be used to define arguments that
match many files or directories. When given as command arguments, the
`?` sign is interpreted as *any single character* and `*` sign as *any
string of characters*. For example,

```bash
ls test?.input 
```

would produce a list of files that begin with `test` and end with `.input`
and have exactly one character in between. Thus, the files with names
`testA.input` and `test4.input` would be listed, but filenames like
`test10.input` or `testOld.input` would be ignored. Instead, the command

```bash
ls test*.input 
```

would list all files mentioned above as `*` matches any string.
Here, the only limitations would be that the command must start with the
string `test` and end with string `.input`.

### Redirecting standard input and output

The characters *less than* (`<`), *greater than* (`>`), `>>`
and *pipe* (`|`) are used to control the standard input and output. The
*less than* symbol (`<`) instructs the command to read data 
from a file defined after that `<` character instead of reading from the
keyboard.

The *greater than* character (`>`) would redirect the output of a command to
a new file instead of the display (standard output). For example, the command

```bash
ls test*.input > input_files
```

would produce a new file called `input_files` that would contain the
names of files that start with the string `test` and end with `.input`.
Using two *greater than* signs with no space between them (`>>`)
would append the results of a command to the end of an existing file or,
if the file does not exist yet, direct the output to a new file with the
specified filename.

The pipe character (`|`) redirects the output of the command
as input for the next command. In this way, you can
combine several Linux commands into a command chain. For example, if your
file listing does not fit to one screen, you could redirect it to `less`
so that you can browse it one screenful at a time.
This kind of redirecting could be done like this:

```bash
ls -l | less
```

As another example, we could use the `grep` command as a post-processor for
the output of the `ls` command and pick, e.g., those files that have been
created on August 14th:

```bash
ls -l | grep "Aug 14"
```

## Further practice

We recommend that you look up examples of the practical usage of Linux commands
online. There are lots of resources showing efficient use of the tools that
come with Linux, so that you can save your time and produce neat results
faster.

Defining own aliases is one of the ways of speeding up your work, and they are
recommended. However, sometimes there might be name clashes and some commands
might end up behaving unexpectedly. We have the tool called `csc-env` which
shows how your environment differs from the default one. For more information,
[check this documentation entry](../using_csc_env.md). 
