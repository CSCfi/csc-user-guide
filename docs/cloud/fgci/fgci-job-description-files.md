## 2.1 Job description files

Submitting computing tasks to FGCI resembles submitting batch jobs to
normal computing clusters. However, in the case of batch jobs the user
just defines the commands to be executed, while in the case of grid
usage the user must also define the (input) files that need to be
transported with the job to the remote cluster and also the resulting
(output)files that are returned when the job finishes.

In the case of ARC-middleware the grid jobs are defined using two files:

1.  A **job description file**, that defines the resources needed (for
    example the required computing time, memory and number of
    processors) and the files that will be copied to and from the remote
    clusters. ARC can use xRSL or JSDL job description file formats.

2.  A **command file** containing the commands that will be executed
    when the job is run in the remote cluster.

The command files are in most cases normal Linux command scripts. Linux
scripting is not discussed in this guide. You can find more information
about Linux scripting from the *CSC computing environment users guide*,
chapter 2.7

([http://research.csc.fi/csc-guide-linux-bash-scripts]<span
lang="en-IE">).</span>

The xRSL formatted job description files are text files that define the
resources and files that the grid job needs. The file starts with an
**&** sign, followed by a list of attribute-value pairs in the format:

(attribute="*value*")

Table 1. lists the most frequently used job description attributes. You
can create xRSL formatted job description files with normal text editors
or you can use the <span lang="en-IE">*Batch Job Wizard Tool*, in the
*Scientist's User Interface* (
<https://sui.csc.fi/group/sui/batch-job-script-wizard> ). (See Figure
2.)</span>

  
**Table 1.** Most commonly used xRSL attributes

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Attribute</strong></td>
<td><strong>Description</strong></td>
<td><p><strong>Example</strong></p></td>
</tr>
<tr class="even">
<td>count</td>
<td>Number of computing cores to be reserved.</td>
<td>(count=8)</td>
</tr>
<tr class="odd">
<td>cpuTime</td>
<td>Computing time requested. For a multi-processor job, this is a sum over all requested processors.</td>
<td>(cpuTime=&quot;6 hours, 20 minutes&quot;)</td>
</tr>
<tr class="even">
<td>executable</td>
<td>Name of the command script file</td>
<td>(executable=runhello.sh)</td>
</tr>
<tr class="odd">
<td>inputfiles</td>
<td>Files that will be copied from the local computer to the remote cluster. The left column refers to the file name at the remote cluster and the right column refers to the file name in the local computer.</td>
<td>(inputfiles=(&quot;file1.txt&quot; &quot;file1.txt&quot; ))</td>
</tr>
<tr class="even">
<td>jobname</td>
<td>Name of the grid job</td>
<td>(jobname=&quot;hello_FGI&quot;)</td>
</tr>
<tr class="odd">
<td>memory</td>
<td>Memory requirement in megabytes</td>
<td>(memory=&quot;4000&quot;)</td>
</tr>
<tr class="even">
<td>notify</td>
<td>Email will be sent to the given address at certain states of the job. E.g. When the job begins (b) or ends (e). Here the <strong>be</strong> signifies sending an email for both states.</td>
<td>(notify=&quot;be kkayttajl@csc.fi&quot;)</td>
</tr>
<tr class="odd">
<td>outputfiles</td>
<td>Files that will be copied from the remote cluster when the results are retrieved. The left column refers to the file name at the remote cluster and the right column refers to the file name in the local computer.</td>
<td>(outputfiles=(&quot;out.txt&quot; &quot;out.txt&quot; ))</td>
</tr>
<tr class="even">
<td>runtimeenvironment</td>
<td>Required run time environment.</td>
<td>(runtimeenvironment=&quot;APPS/BIO/BOWTIE-2.0.0&quot;</td>
</tr>
<tr class="odd">
<td>stderr</td>
<td>File for standard error</td>
<td>(stderr=std.err)</td>
</tr>
<tr class="even">
<td>stdout</td>
<td>File for standard output</td>
<td>(stdout=std.out)</td>
</tr>
</tbody>
</table>

 

![]

**Figure 2.** Batch job wizard in the Scientists User Interface.

Below is a short command script that is used as a simplified example of
a grid command file. The job prints words "*Hello FGI*" to the standard
output and then writes the number of lines in files *inputfile.txt* and
*file2.txt* to a new file called *output.txt*. The name of the command
script in this example is *runhello.sh*.

    #!/bin/sh
    echo "Hello FGCI"
    wc -l inputfile.txt file2.txt > output.txt
    exit 

The *runhello.sh* script above can be executed in the FGI environment
using the following job-description file (called *hello.xrsl*):

    &(executable=runhello.sh)
    (jobname=hello_FGCI)
    (stdout=std.out)
    (stderr=std.err)
    (cpuTime="1 hours")
    (memory="1000")
    (inputfiles=
    ("inputfile.txt" "file1.txt" )
    ("file2.txt" "")
    )
    (outputfiles=
    ("output.txt" "" )
    )

The first line of the job description file defines that the script
*runhello.sh* will be copied to the remote cluster and executed. The
following lines define the name of the grid job (hello\_FGCI) and the
names of the standard output (std.out) and standard error (std.err)
files.

The computing time (1 h) and memory (1000 MB) requirements of the job
are defined in the fifth and the sixth rows. Defining these values is
not mandatory but it is recommended that you do so. Setting up memory
and time limits ensures that your job will be submitted to a cluster
that has enough resources. Further, correctly set memory and time
requirements ensure that in the remote cluster your job ends up in a
queue that most effectively executes your job.

The definition *(inputfiles=* starts the region that lists the files
that will be copied to the cluster executing the job. In addition to the
actual input files of your job, this notation can also be used to copy
program files like pre-compiled executables, source codes or program
scripts to be used in the remote cluster.

The example above uses two alternative ways to define a file that will
be copied to the remote cluster. The row:

    ("inputfile.txt" "file1.txt" )

defines that the file called *file1.txt* will be copied so that in the
remote cluster the name of the file will be *inputfile.txt*. The next
row:

    ("file2.txt" "")

defines that file *file2.txt* will be copied to the remote cluster. The
same result could also be defined by a row such as:

    ("file2.txt" "file2.txt")

The final closing bracket on a line by itself ends the input files
defining regions.

A similar syntax is used to define the files that will be copied back
from the remote cluster when the job results are retrieved. The output
file defining regions starts with the notation *(outputfiles=* . In this
example we will retrieve only one file, called *output.txt*. If you
would like to retrieve all the files that are generated by the job
execution directory in the remote cluster you can use the notation:

    (outputfiles=("/" "" ))

When you define the output to be retrieved, it is good to remember that
moving large files between the remote cluster and the local computer can
take a long time. Thus, you should try to avoid unnecessary copying of
large data-sets.

 

 

 

  [http://research.csc.fi/csc-guide-linux-bash-scripts]: https://research.csc.fi/csc-guide-linux-bash-scripts
  []: https://research.csc.fi/documents/48467/84606/FGI-guide_image2.jpg/6b9da668-0224-40a9-82de-9a79d127f200?t=1383828999000
