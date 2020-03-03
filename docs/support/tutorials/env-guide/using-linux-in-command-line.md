# Using Linux in command line

## Files and directories in Linux

The file systems in Linux machines are based on hierarchical directory
tree. There is one *root directory* in to which you can refer with
*slash sign* (/). All the files and directories locate in the
subdirectories of this directory so that each file has a unique
combination of name and directory path. Also the commands that user
gives are executed in a directory in which user currently is
called *current working directory*.

Normally you do not need to know the explicit directory paths when you
work in the CSC environment. It is enough to know the locations of the
files in users own disk areas. The user and project specific disk areas
are presented in chapter 3. However, you should remember that many disk
areas in CSC environment can be accessed from several different servers
(e.g. the users home directory) while some areas are server specific. In
the case of shared disk areas the path to a certain file may be
different in different servers.

## Structure of linux commands

Once the terminal connection to CSC, e.g. to [Puhti-shell], has been
opened, the remote server is used with Linux commands. The standard
structure of a command is:

`command -options argument1 argument2 ...`

The command is executed by pressing the *return key (Enter)*. The names
and functions of options and arguments depend on the linux command. In
many cases you can run the command without any options and arguments.
Options are used to modify the actions that the command performs.
Arguments are used to define the files, directories and values that are
used as input parameters and to define where the output is written.

For example command `ls` can be used as such or with several options
and arguments. Running plane command *ls* lists the content of a
directory in alphabetical order. You can modify the output of the
command for example by using option `-t`. With this option the
directory content list is ordered by the age of the file (time stamp).
If no argument is given, *ls* prints out the content of the current
working directory. By giving an argument to the *ls* command, user can
define a directory which content should be listed. For example command:

`ls -t /scratch/project_2979797`

will list the content of directory */scratch/project_2979797*. In case the command,
argument or options contain errors, the command will not be executed
when the return key is pressed. Instead an error message is printed to
the screen. Thus having errors in the command normally does not cause
any major problems. The output of commands depends on the command but in
many cases, no output means that command was successfully executed.

Most of the Linux commands have their own manual page that can be
studied with `man` command. For example the manual page of *ls*
command could be studied with command:

    man ls

The manual pages can be very detailed and technical. However, often you
do not need to read and understand all the details on the manual pages,
but instead you can just see what command line options are available for
the given command, which are of interest for you and then start
testing/using them in practice.

Often the most difficult thing in using Linux is knowing the name of
suitable command. Below we introduce to the most frequently used linux
commands. You can also use command `apropos` to find suitable
command. Apropos lists those Linux commands whose short description
lines match the text that is given as a command argument. For example to
look for commands that are processing *pdf* files you could give
command:

    apropos pdf

Note that the listing that apropos prints out includes only linux
commands but not application program names. Thus, the sample command
above would produce a list that contain many pdf conversion commands but
not the pdf viewing programs like *acroread* or *evince*.

## Basic commands for using directories

Table below lists the commands that are most frequently used for moving in
the directory hierarchy and managing it. Below are some examples of
directory related commands.

Basic directory commands

| Name      | Argument    | Description                                           |
|-----------|-------------|-------------------------------------------------------|
| **cd**    | *directory* | Change current working directory                      |
| **ls**    | *directory* | Lists the content of a directory                      |
| **pwd**   |             | Print the directory path of current working directory |
| **mkdir** | *directory* | Create a new directory                                |
| **rmdir** | *directory* | Remove a directory                                    |

When you log in to a server at CSC, you will first locate in your home
directory. You can check your location i.e. the path of the current
working directory with command `pwd` (abbreviation from Print
current Working Directory). However, you do not have to remember the
location of your home directory (see `cd` command).

The content of the directory can be listed with a command `ls`.
Plain *ls* command just lists the names of the files and directories in
your current directory. You can get more information about the files and
directories with command **ls -la**. The **-l** option produces long
directory listing that in addition to the name contains also information
of accession settings, size and the modification dates of the files and
directories. The option **-a** defines that all files, including also
the settings files that start with dot (.) character, are listed. Below
is a sample output for `ls -la` command:

~~~~
kkayttaj@c305:~>ls -la
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
~~~~

The first output *row: total 26914* tells that the total size of the
files in the directory is 26914 KB. In the list, the first character
tells if the item is a file (*-)* or directory(*d*). The next nine
characters display the *access permissions* of the files (see the
*chmod* command for more details). The next columns show the number of
links pointing to the item, owner, user group, size in bytes,
modification time and finally the name of the file or directory.

By default the files are presented in alphabetical order. You can order
the results by the modification time with option **-t** or by size with
option **-S** (note: upper case S, not lower case s). Two other
frequently used options are **-h** (Human readable) which prints out the
sizes of larger files in megabytes or gigabytes and **-r** which means
reverse sorting order. For example command:

```bash
ls -ltrh
```

is very handy when you want to check what files have recently been
modified or created. *ls* and *pwd* commands do not modify your files in
any way so you can use them always when you want to know where you are
and what files your current directory includes.

Command `cd` ***directory\_name*** moves you from the current
directory to a directory you specified. For example the user *kkayttaj*
could go to his local temporary directory with command:

```bash
cd /local_scratch/kkayttaj
```

or

```bash
cd $TMPDIR
```

In the latter command automatically defined *environment variable*
$TMPDIR, that contains the explicit directory path, is used to define
the target directory.

New directories can be created with a command `mkdir`
***directory\_name***. For example command:

    mkdir project1 

Creates a new directory called *project1*. You can use *ls* command to
check that the directory was created. Now you can go to this directory
with command:

    cd project1 

You can come back from the project1 directory with command:

    cd .. 

Note the space between *cd* and the dots in the command. One dot (.) and
two dots (..) have special meaning in the Linux commands. One dot (.)
means the *current directory* and two dots (..) mean the directory that
is one step lower in the directory tree i.e. the directory where current
directory locates. Executing the *cd* command without any arguments will
always move you back to your home directory, regardless where you are in
the directory tree. An empty directory can be removed with command
`rmdir` *directory\_name*. For example:

    rmdir project1 

## Basic commands for files

In a very basic level a file in a Linux system is just a string of
bytes, were a byte consists of eight bits. So called text files the
contain only bytes that can be interpreted as text characters using
ASCII coding. Thus these files can be considered to consist of lines of
text. In so called binary files, also non-ASCII bytes are used and the
text can't and is not intended to be converted to text. Typical examples
of binary files are compiled programs, images or compressed files.
Normally users work mostly with text files and also in the examples of
this guide we normally assume that the files contain some kind of text
data: letters or numbers.

Each file has a name. Name can in principle be any combination of
characters. However, several characters have special meaning e.g.
`?, * and #`, see [below](#special-characters) and
thus using these characters in file names may cause problems. We
recommend that you use only normal letters (lower or upper case),
numbers, dot (**.**), dash (**-**) or under score (\_) characters in
file and directory names at CSC. Also the space characters in file names
cause often problems. We recommend that the space characters are
replaced with underscores, for example: *new\_file.txt*. Note that Linux
is case sensitive: lower and upper case characters are not considered
equal and for example names *New\_File.txt* and *new\_file.txt* refer to
different files.

In linux, usage of name extensions like .doc or .txt is not obligatory.
Most of the linux tools do not require specific extensions to be used.
However, on the long run, using systematic naming conventions, including
illustrative name extensions, makes the file management easier.

File related commands:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name</p></th>
<th><p>Arguments</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>cat</strong></td>
<td><p><em>file_names</em></p></td>
<td><p>Print the content of the specified file of files to the standard output (your screen)</p></td>
</tr>
<tr class="even">
<td><strong>chmod</strong></td>
<td><p><em>file_names</em></p></td>
<td><p>Change the access permissions of a file</p></td>
</tr>
<tr class="odd">
<td><strong>cp</strong></td>
<td><p><em>file_name1 file_name2</em></p></td>
<td><p>Copy the file content to a new file or new location</p></td>
</tr>
<tr class="even">
<td><strong>grep</strong></td>
<td><p><em>search_string file_name</em></p></td>
<td><p>Pick from the file the rows that contain a specific string</p></td>
</tr>
<tr class="odd">
<td><strong>head</strong></td>
<td><p><em>file_name</em></p></td>
<td><p>Print the first rows of the file to the standard output (your screen)</p></td>
</tr>
<tr class="even">
<td><strong>less</strong></td>
<td><p><em>file_name</em></p></td>
<td><p>Show the content of a file one screenfull at a time</p></td>
</tr>
<tr class="odd">
<td><strong>more</strong></td>
<td><p><em>file_name</em></p></td>
<td><p>Show the content of a file one screenfull at a time</p></td>
</tr>
<tr class="even">
<td><a href="https://research.csc.fi/" id="ln"></a><strong>ln</strong></td>
<td><p><em>file_name1 link_name</em></p></td>
<td><p>Create a link to a file</p></td>
</tr>
<tr class="odd">
<td><strong>mv</strong></td>
<td><p><em>file_name1 file_name2</em></p></td>
<td><p>Rename a file or move it to another location</p></td>
</tr>
<tr class="even">
<td><strong>rm</strong></td>
<td><p><em>file_names</em></p></td>
<td><p>Remove files</p></td>
</tr>
<tr class="odd">
<td><strong>tail</strong></td>
<td><p><em>file_name</em></p></td>
<td><p>Show the last rows of a file</p></td>
</tr>
</tbody>
</table>

You can study the content of text files with commands `cat`,
`more` and `less`. These commands are safe to use as
they don't modify the files in any way. For example you could study the
*.bashrc* file in your home directory with commands:

    cat .bashrc
    more .bashrc
    less .bashrc 

`cat` command (abbreviation from concatenate) prints the content of
the specified file or files to the *standard output* that by default
means your screen. Pager programs **less** and **more** are often more
useful tools for studying text files as they allow user to study the
file one screenfull at a time. In both *more* and *less* programs you
can move forward one line at a time by pressing *Return key* or one
screenfull at a time by pressing *Space*. You can stop viewing the file
by pressing **q**.

The *less* pager program is more advanced than *more*. *Less* can browse
the text also backwards either one row at a time by pressing **k** or
one screenfull at a time by pressing **b**. You can also search a text
string from the document by using slash (**/**) character. For example,
to locate a string *ABC* from the file in *less* program type **/ABC**
and the press *Return*. *man* command uses *less* program as its pager.

Commands `head` and `tail` can be used to see just the
first or last rows of a file, respectively. By default these commands
print out 10 lines, but you can change this by giving the number of rows
to be printed as an option to a *head* or *tail* command. For example,
to check the 30 last rows of a file called *run1.log* give command:

    tail -30 run1.log 

Copying files to a new file or to another directory is done with command
`cp` (copy). Find below two examples of copy commands:

`cp output.dat output_copy.dat`  
`cp output1.dat output2.dat results/ `

The first command makes a copy of file *output.dat* to a new file called
*output\_copy.dat*. In the second example the two files: *output1.dat*
and *output2.dat* are copied to an existing directory called *results*.
Command `mv` (move) is used to rename or move the files to
another location. For example:

    mv output.dat output_copy.dat
    mv output1.dat output2.dat results/ 

would create the same new files as *cp* sample commands. However in the
case of *mv* the original files *output.dat*, *output1.dat* and
*output2.dat*, would be removed from the current working directory.

Files are removed with command [][18]**rm** <span
lang="en-US">*file-name***.**</span> In the CSC environment, the *rm*
command asks the user to confirm that he/she really wants to remove the
file:

    kkayttaj@c305:~>rm output_copy.dat
    rm: remove output_copy.dat (yes/no)? 

You can answer *y* (yes) or *n* (no). Note that this confirmation step
is not necessary in use in your local Linux environment. You can skip
the confirmation query with option **-f**. However you should use this
option with caution as the *rm* command will remove the file immediately
and permanently.  

## Special characters

Some characters have special functions in Linux. In the following
paragraphs we present characters that are used for redirecting standard
input and output or used as so called *wildcard characters*.

The `$` sign, that is used as an indicator of a variable name, `\#`
mark that is used to place comments and different kind of quotation
marks are discussed later on in the [linux scripting chapter].

Commonly used special characters

| Character    | Function                                                        |
|--------------|-----------------------------------------------------------------|
| **$**        | Indicates a shell or environmental variable                     |
| **\|**       | Pipes standard output to the standard input of the next command |
| **\#**       | Starts a comment                                                |
| **&**        | Executes a process in the background                            |
| **?**        | Matches one character                                           |
| **\***       | Matches any string (including an empty string)                  |
| **&gt;**     | Output redirection operator                                     |
| **&lt;**     | Input redirection operator                                      |
| **&gt;&gt;** | Output redirection operator (to append to a file)               |
| **\\**       | ignore the possible special function of the following character |


### Wildcard characters

In Linux, question mark (**?**) and asterisk (**\***) are used as so
called wildcard characters. They can be used to define arguments that
match many files or directories. When used in the command arguments, the
*?* sign is interpreted as *any single character* and *\** sign as *any
string of characters*. For example command:

    ls test?.input 

Would produce a list of files that has a name: test*any
character*.input. Thus files with names *testA.input* and *test4.input*
would be listed, but file names like *test10.input* or *testOld.input*
would be ignored. Instead, command:

    ls test*.input 

would list all of the files mentioned above as \* matches any string.
Now the only limitations would be that the command must start with
string *test* and end with string *.input*.

### Redirecting standard input and output

Characters less than (**&lt;**), greater than (**&gt;**), **&gt;&gt;**
and pipe (**\|**) are used to control the standard input and output. The
less than (&lt;) instructs the command to read data for standard input
from a file defined after that &lt; character instead of the keyboard.

The greater than character (&gt;) would direct the standard output of to
a new file instead of the display. For example command:

`ls test*.input > input_files `

would produce a new file called *input\_files* that would contain the
names of files that start with string *test* and end with *.input*.
Using two greater than signs with no space between them ( **&gt;&gt;** )
would append the results of a command to the end of an existing file or,
if the file does not yet exist, direct the output to a new file.

The pipe character (**\|**) directs the standard output of the command
to the standard input of the next command. With this function you can
combine several linux commands into a command chain. For example if your
file listing does not fit to one screen, you could redirect it to *less*
command so that you can study and browse it one screenfull at a time.
This kind of redirecting could be done with command:

    ls -l | less 

As another example, we could use *grep* command as a post processor for
*ls* command and pick for example those files that have been created on
August 14th :

    ls -l | grep "Aug 14"

