# Linux bash scripts
  
One way of utilizing the flexibility of Linux is using command scripts.
A command script is simply a file, which contains a set of normal Linux
commands that the command shell will perform automatically in the given
order. Compared to real programming languages, like Python, Perl or c,
programming with Linux (bash, tcsh, csh or sh) is computationally rather
ineffective. However, often handy Linux scripts can be constructed in a
few minutes. You do not have to know too much about command scripting to
be able to write simple programs that save a lot of time.

## Constructing a script file

A script file is a simple text file that can be constructed with normal
text editors like *nano*, *Emacs* or *vi*. To create a new script file,
type for example:

```bash
nano my_test.script
```

A script file usually starts with a line which defines the
command shell to be used. In this guide, we use *bash* shell, which is the
default command shell at CSC. The bash defining row is:

```bash
#!/bin/bash
```

After that you add the Linux commands you wish to perform. In practice,
just type in the file the commands that you would normally use to do
the task in an interactive command shell. For example, the following script can
be used to create a subdirectory `mapfiles` and copy all `.map` files there:

```bash
#!/bin/bash
mkdir mapfiles
cp *.map mapfiles/
```

If a line in the script starts with a `#` character, it will be skipped,
and rest of the line is considered as a comment (except for
the first line that starts with `#!`).

```bash
#!/bin/bash
# This is a comment line that is not executed

mkdir mapfiles
cp *.map mapfiles/
```

After saving the script file and closing the editor, you can perform the
commands in the script file by giving the command:

```bash
source my_test.script
```

Optionally, you could give execution permissions for your script file
with the command

```bash
chmod u+x my_test.script
```

and then execute the script with the command:

```bash
./my_test.script
```

## Variables and arrays

You can use variables, loops and conditional statements in the scripts.
Variables can be set with syntax:

```bash
variable=value
```

Note that there are no spaces around the equals sign. Variables are recalled
with `$` sign,

```bash
$variable
```

or

```bash
${variable}
```

For example, the command

```bash
echo $variable
```

writes the value of variable to the output. Note that in bash scripts
the variables are considered to be either strings (i.e. text) or
integers. This means that decimal numbers can't be used in bash
scripts for mathematical operations.

Example of using string variables:

```bash
$ name=Veikko
$ familyname=Salo
$ address="CSC Espoo"
$ echo "Person: ${name} ${familyname} works at ${address}."

Person: Veikko Salo works at CSC Espoo.
```

For integer variables, you can do simple arithmetic with syntax
`((expression))`. Commonly used arithmetic operations are listed in
the table below:

| Operator | Function           |
|----------|--------------------|
| `+`      | addition           |
| `-`      | subtraction        |
| `*`      | multiplication     |
| `/`      | division           |
| `%`      | division remainder |
| `**`     | exponentiation     |

Simple integer arithmetic examples:

```bash
$ a=5
$ c=3
$ ((c = a + b))
$ echo  $a plus $b is equal to $c
5 plus 3 is equal to 8
$ ((d = a / b))
$ ((e = a % b))
$ echo "$a divided by $b results $d and reminder $e"
5 divided by 3 results 1 and reminder 2
```

Bash can also use one-dimensional array variables, i.e. variables that contain
a list of items. A
specified array item can be recalled by using an index number in
brackets with the array variable name `(${variable[index]})`. For
example, we can define a simple three element array with the command:

```bash
array=(a b c)
```

We can now recall either the whole array or just on element from it using
the command

```bash
echo ${array[*]} 
```

This prints out

```bash
a b c
```

while command

```bash
echo ${array[2]}
```

prints

```bash
c
```

Note that in the array, the indexing starts from 0 and thus the sample
command above prints out the third element of the array. You can check
the number of items in the array by adding the `#` sign to the beginning of
the variable name. For example, in this case the command

```bash
echo ${#array[*]}
```

prints out the value

```bash
3
```

A special case of array variables is `$` that holds command line
arguments, i.e. items that you can provide as input parameters for your
script. In the case of this argument, array `$0` refers to the name of the
actual script, `$1` refers to the first arguments, `$2` to the second and so
on. `$#` refers to the number of arguments and `$@` to the full argument
list. Below is a sample script that illustrates using the `$` array
variable:

```bash
#!/bin/bash
from_dir=$1
to_dir=$2
mkdir $to_dir
cp $from_dir/*.map $to_dir
```

If we now execute this script, named e.g. `my_script2.sh`, we have to
give two arguments for the command. The first argument is in this case
used to define a source directory for the copy command while the second
argument is the target directory. For example, the command

```bash
./my_script2.csh source_data map_files
```

would copy all the file with extension `.map` from a directory called
`source_data` to a new directory called `map_files`.

## Quotation marks

Three different quotation marks are used in bash. Quotation marks are
frequently needed to define variables and commands to be executed.
Following quotation marks can be used:

- ` "" ` Take text within quotes literally after substituting any
  variables
- ` '' ` Take text enclosed within quotes literally
- ` `` ` Take text enclosed within quotes as a command, execute the
  command and then replace with output of the command at the location
  of quotation marks

Below are some examples to illustrate the functional differences of
different quotation marks. Quotation marks can be used to operate with
variables and arguments. When the double or single quotation marks are
used, all the text inside the quotation marks are used as one
argument. The difference between these two quotation marks is that
when double quotation marks are used, variables are substituted by their
values, while with single quotation all text is used as it is. If you
run the commands

```bash
variable=sample1
echo "value = $variable"
```

the result will be

```bash
value = sample1
```

But if you use single quotation marks instead

```bash
echo 'value = $variable'
```

you will get output

```bash
value = $variable
```

In Linux commands and scripts quotation marks are typically used to
define arguments that contain spaces or other special characters. Say we
would like to use `grep` to pick all rows that contain a string
`file size` from a file called `files.txt`. The following command **would
not work**:

```bash
grep file size files.txt
```

If you run the command above, you'll get an error message, as the word
*size* is now interpreted to be the second argument defining the input
file. We can fix the situation by using quotation marks:

```bash
grep "file size" files.txt
```

Now, the first argument defining the string to be searched is `file
size` (including the space between the words), and the second argument
defining the input file is now `files.txt` as originally intended.

The third quotation mark type ` `` ` has a special meaning. With these
quotation marks, you can make one Linux command produce an argument
for another Linux command. The basic syntax ` `` ` is:

```bash
command1 `command2`
```

where `command1` will use the product of `command2` as an argument. In
a bash script, the same functionality can be done also with the syntax

```bash
$(command)
```

## Loops and conditional statements

Loops and conditional statements are rarely used in interactive command-line
usage. However, they are frequently used in scripts to perform
similar commands several times and to control the commands to be
executed. Bash provides a wide selection loops, conditional statements
and other control structures. In this section, we show examples of some
of the most commonly used control structures.

A *for* loop performs specified commands iteratively so that
on each iteration the loop variable is set to be equal to one of the
items in the given element list. In bash, a for loop is made with command
structure:

```bash
for variable in element_list
do
   commands
done
```

For example, the loop

```bash
for filename in sample1.txt sample2.txt sample3.txt
do
   echo ${filename}
done
```

would print out

```text
sample1.txt
sample2.txt
sample3.txt
```

Typically, the argument list contains file names to be processed, but it
can also be any other parameter too. For example, say we have a
directory called `project_3` that contains nine files called
`sample1.txt`, `sample2.txt`, ..., `sample9.txt`. To see the contents of
the directory, we may use command `ls`:

```bash
$ ls project_3/
sample1.txt sample3.txt sample5.txt sample7.txt sample9.txt  
sample2.txt sample4.txt sample6.txt sample8.txt  
```

If we would like to rename each of these files so that they have
the extension `.old`, we could run command `mv` nine times, or we could use a
for loop:

```bash
for filename in sample1.txt sample2.txt sample3.txt sample4.txt \
sample5.txt sample6.txt sample7.txt sample8.txt sample9.txt
do
   echo "Renaming file: ${filename}"
   mv project_3/${filename} project_3/${filename}.old
done
```

The for loop above is still quite clumsy as we need to write all the
file names to the element list. We can avoid this by substituting the
element list with `$(ls project_3/)`. Now, command `ls project3` is
used to produce a list of file names to be processed:

```bash
for filename in $(ls project_3/)
do
   echo "Moving file: $filename"
   mv project_3/$filename project_3/"$filename".old
done
```

In bash, you can also create a for loop where a numerical index variable
is increased automatically by a certain step size in each iteration.
In this case, the syntax is:

```bash
for ((variable=start; variable<=end; i++)) 
```

Below is a for loop that performs the same renaming operation as above,
but using just numbers as elements.

```bash
for ((number=1; number<=9; number++))
do
   echo "Moving file: sample${number}.txt"
   mv project_3/sample${number}.txt project_3/sample${number}.txt.old
done
```

In a `while` loop, the loop keeps running as long as the defined
condition statement is true. In bash, a while loop can be made with
the syntax:

```bash
while [[ condition ]]
do
   commands
done
```

The renaming operation, made above with a for loop, could also be done
with a while loop:

```bash
number=1
while [[ $number -le 9 ]]
do
   echo "Moving file: sample${number}.txt"
   mv project_3/sample${number}.txt project_3/sample${number}.txt.old
   ((number = number + 1))
done
```

In the example above, a variable called `number` is first set to have
value 1. The value of this variable is then increased by 1 in the end of
each iteration cycle. The iterations are continued until the variable
reaches value 10.

Conditional statements (`if`) can be made as follows:

```bash
if [[ condition ]]
then
   commands
else
   commands
fi
```

You can use operands listed in the table below in the conditional statements
of `if` and `while` commands. Note that bash uses different conditional
statements for strings and integers. For example, the equality of strings
is tested with `==` while the equality of integers is tested with `-eq`.
The syntax is also strict about the spaces between the brackets, and the
condition statement definition `[[a == b]]` will not work and should
be fixed to `[[ a == b ]]`.

Commonly used string, integer and file operands of `if` and `while`
statements are listed below.

| Statement       | Operation                                                 |
|-----------------|-----------------------------------------------------------|
| `[[ a == b ]]`  | True if strings a and b are equal                         |
| `[[ a != b ]]`  | True if strings a and b are not equal                     |
| `[[ a =~ b ]]`  | True if strings a and b are similar (allows wildcards)    |
| `[[ a < b ]]`   | True if string a is alphabetically before string b        |
| `[[ a > b ]]`   | True if string a is alphabetically after string b         |
| `[[ a -eq b ]]` | True if integers a and b are equal                        |
| `[[ a -ne b ]]` | True if integers a and b are not equal                    |
| `[[ a -lt b ]]` | True if integer a is less than b                          |
| `[[ a -gt b ]]` | True if integer a is greater than b                       |
| `[[ a -le b ]]` | True if integer a is less or equal to b                   |
| `[[ a -ge b ]]` | True if integer a is greater or equal to b                |
| `[[ -e name ]]` | True if file exists                                       |
| `[[ -n a ]]`    | True if string a has non-zero length                      |
| `[[ A || B ]]`  | True if condition A or condition B is true (logical OR)   |
| `[[ A && B ]]`  | True if condition A and condition B is true (logical AND) |
| `[[ ! A ]]`     | True if condition A is not true                           |

Below are some examples of `if` command structures.

Check if the integer variable `x` is greater than 10:

```bash
if [[ $x -gt 10 ]]
then
   echo "The value of variable x is more than 10"
fi
```

Check if the variable *x* is greater than 10 but smaller than 20:

```bash
if [[ $x -gt 10 && $x -lt 20 ]]
then
   echo "The value of variable x is more than 10 but less than 20"
else
   echo "The value of x is out of range"
fi
```

You can compare also variables containing text (strings):

```bash
if [[ $answer == "yes" ]]
then
   echo "Your answer was: yes"
elif [[ $answer == "no" ]]
then
   echo "Your answer was no"
else
   echo "You didn't answer yes or no"
fi
```

When using *less than* and *more than* comparisons, you should be careful
not to mix string and integer comparisons. For example, the following
condition

```bash
[[ 123 > 3 ]]
```

is `FALSE` because string 123 is alphabetically before string 3. The
numerical comparison

```BASH
[[ 123 -gt 3 ]]
```

is, however, `TRUE`.

There are a number of operators you can use to test different attributes
of a file. The most commonly used operator is `-e` that checks if a file
exists. As an example, let's assume that we have a simple list of file
names called `checklist.txt`. We would like to check which of these
files are found in the current directory. We can use a `for` loop to
study all the file names and the `if` command with `-e` condition to
test if the file exists:

```bash
for file_name in $(cat checklist.txt)
do
   if [[ -e $file_name ]]
   then
      echo "File $file_name was found"
   else
      echo "File $file_name was not found"
   fi
done
```

## Printing the output

In the previous examples we have already used the `echo` command to
write text and variables to the standard output (i.e. to the screen or
to a file by standard output redirection). For example, the command

```bash
echo "Hello world"
```

prints out

```bash
Hello world
```

`echo` can be used for printing output in many cases, but it does not
provide good tools for creating well formatted output with defined
columns. In situations where well-structured text output is needed,
`printf` should be used instead of `echo`. The syntax of `printf`
is:

```bash
printf "format definition" arguments_to_print
```

The `format definition` defines what types of output is to be printed.
Common types include text (`%s`), integers (`%i`), and floating
point numbers (`%f`). The format statements can also define how much
space is reserved for each argument and how it is located in the column.
Below are some simple examples to illustrate the usage of the `printf`
command:

```bash
printf "%i %s %s %f\n" 1 Hello World 23.75
```

prints out

```bash
1 Hello World 23.750000
```

Here, the format statement defines that the first argument is considered
to be an integer, second and third as strings and the fourth argument as
a floating point number. Note that by default, `printf` does not add a
newline character to the end of the output. To do that, the format
statement should end with definition `\n`.

In the next example we define how many characters are reserved for each
argument. The command

```bash
printf "%4i %10s %10s %6.2f\n" 1 Hello World 23.75
```

prints out

```bash
1 Hello World 23.75
```

Here, we reserve four characters for the first integer, then ten
characters for each of the strings. The floating point number is
presented with six characters, two of which are after the decimal point.

You can also add text and control characters like tabulator (`\t`) to
the format statement. The command

```bash
printf "This is my %i:st %s %s\t %6.1f\n" 1 Hello World 23.75
```

prints out

```bash
This is my 1:st Hello World 23.8
```

In Linux scripts, `printf` is typically used to print out values stored
in variables. For example, the commands

```bash
unit=3g
value=5.3
printf "The resulting value from:%4s\t is:\t%6.2f\n" $unit $value
```

prints out

```bash
The resulting value from: 3g is: 5.30
```
