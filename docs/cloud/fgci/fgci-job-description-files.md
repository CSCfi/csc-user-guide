# Job description files

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
about Linux scripting from the CSC workshop materials or via google.

The xRSL formatted job description files are text files that define the
resources and files that the grid job needs. The file starts with an
**&** sign, followed by a list of attribute-value pairs in the format:

(attribute="*value*")

Table 1. lists the most frequently used job description attributes. You
can create xRSL formatted job description files with normal text editors.
  
**Table 1.** Most commonly used xRSL attributes

| Attribute          | Description                                                                                                                                                                                                           | Example                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| count              | Number of computing cores to be reserved\.                                                                                                                                                                            | \(count=8\)                                     |
| cpuTime            | Computing time requested\. For a multi\-processor job, this is a sum over all requested processors\.                                                                                                                  | \(cpuTime="6 hours, 20 minutes"\)               |
| executable         | Name of the command script file                                                                                                                                                                                       | \(executable=runhello\.sh\)                     |
| inputfiles         | Files that will be copied from the local computer to the remote cluster\. The left column refers to the file name at the remote cluster and the right column refers to the file name in the local computer\.          | \(inputfiles=\("file1\.txt" "file1\.txt" \)\)   |
| jobname            | Name of the grid job                                                                                                                                                                                                  | \(jobname="hello\_FGI"\)                        |
| memory             | Memory requirement in megabytes                                                                                                                                                                                       | \(memory="4000"\)                               |
| notify             | Email will be sent to the given address at certain states of the job\. E\.g\. When the job begins \(b\) or ends \(e\)\. Here the be signifies sending an email for both states\.                                      | \(notify="be kkayttajl@csc\.fi"\)               |
| outputfiles        | Files that will be copied from the remote cluster when the results are retrieved\. The left column refers to the file name at the remote cluster and the right column refers to the file name in the local computer\. | \(outputfiles=\("out\.txt" "out\.txt" \)\)      |
| runtimeenvironment | Required run time environment\.                                                                                                                                                                                       | \(runtimeenvironment="APPS/BIO/BOWTIE\-2\.0\.0" |
| stderr             | File for standard error                                                                                                                                                                                               | \(stderr=std\.err\)                             |
| stdout             | File for standard output                                                                                                                                                                                              | \(stdout=std\.out\)                             |

Below is a short command script that is used as a simplified example of
a grid command file. The job prints words "*Hello FGCI*" to the standard
output and then writes the number of lines in files *inputfile.txt* and
*file2.txt* to a new file called *output.txt*. The name of the command
script in this example is *runhello.sh*.

    #!/bin/sh
    echo "Hello FGCI"
    wc -l inputfile.txt file2.txt > output.txt
    exit 

The *runhello.sh* script above can be executed in the FGCI environment
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

