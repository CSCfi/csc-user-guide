
**NOTE! Information deprecated as of 22.11.2021**
# Using storage elements for data transport in FGCI

Moving large datasets between the local computer and grid clusters is
often one of the major bottlenecks in grid computing. The FGCI
environment includes a centralised data repository that can be used to
avoid copying the same file repetitively between the local computer and
the FGCI environment. This system allows FGCI users to load data into a
central repository that can be accessed form the computing nodes, and is
commonly referred to as a *storage element*. The storage element system
of ARC has a cache system that in many cases significantly reduces the
network load and speeds up the job submission process.

To illustrate the benefits of storage elements, lets assume that we are
submitting one hundred grid jobs, all of which need the same large input
file called *bigdb.txt.* If the input file is copied using the normal
input file definitions in the job description files, then the
*bigdb.txt* file is transported from local machine to the computing
clusters one hundred times. A more clever way in this case is to first
upload the *bigdb.txt* to the grid storage element. Then we modify the
job description file so that in the input file list we refer to the
*bigdb.txt* file in the storage element rather than to the local copy.
When we now launch the 100 grid jobs, the first job in each computing
cluster copies the input file from the storage element to the cache disk
area of the computing cluster. Subsequent jobs now can use the same file
from the local data cache. Thus, if we send 100 jobs to ten computing
clusters, the data only needs to be transported from the storage element
to the remote clusters only ten times.

The storage element of FGCI is based on the SRM (Storage Resource
Manager) protocol. The address of the storage element protocol is:

    srm://bombay.csc.fi/fgi/userdirs

User specific directories are not automatically created in the FGCI
storage element. Instead, users should create their own personal
sub-directory when they use the FGCI storage element for the first time.

The storage element system is intended to support running computing
tasks in the FGCI environment. It is not intended for storing data for
longer periods. As the size of the storage element is rather limited
users must remove their unused data from the storage element. When the
storage element starts filling up, the oldest files will be
automatically removed. It should also be noted that the security level
of the storage element is very low: you should **not** use it for
sensitive data.

The files stored on the storage element can't be modified. If you wish
to modify a file in storage element, you must first download it to your
computer, modify the local copy, remove the original file from the
storage element and then copy the modified file back to the storage
element.

##  Using storage elements with ARC commands

The storage element can be used through a set of ARC commands *arcls*,
*arccp* and *arcrm*. The command *arccp* can be used to copy data
between the local computer and the storage element. For example, the
file *bidgb.txt* can be copied to the storage element with the command:

    arccp bidgb.txt srm://bombay.csc.fi/fgi/userdirs/my_username/bigdb.txt

Note that in the file path of storage element we have added one extra
folder level: *my\_username.* When the command above is executed two
things happen: 1. a new directory called *my\_username* is created (if
it does not yet exist). 2. the file *bigdb.txt* is copied there.
(Currently the ARC client does not have a separate command for creating
new directories. To create a new directory you must use the arccp
command as above)

Copying a file from the storage element is also done with the *arccp*
command. For example, the command:

    arccp srm://bombay.csc.fi/fgi/userdirs/my_username/bigdb.txt bigb_copy.txt

Would copy the file *bigdb.txt* to the local computer into the file
*bigb\_copy.txt*

The content of a directory in the storage element can be checked with
the command *arcls*. For example, the content of the *my\_username*
directory can be checked with the commands:

    arcls srm://bombay.csc.fi/fgi/userdirs/my_username/

or

    arcls -l srm://bombay.csc.fi/fgi/userdirs/my_username/

The command *arcrm* is used to remove a file from the storage element.
Fore example, to remove the file *bigdb.txt* from the storage element,
you should use the command:

    arcrm srm://bombay.csc.fi/fgi/userdirs/my_username/bigdb.txt

## Using storage elements in grid jobs

For the actual grid jobs, the storage
element files are used via the job description files. There you can
set that a specified input file
is read from the storage element (instead of the local computer) or that
a certain output file is transported to the storage element. For
example, in the [Bowtie2 runtime environment example](fgci-using-software-through-runtime-environments.md) a
chromosome sequence file, *chr_18.fa*, is used as one of the input files. If we
copy the file to the storage element with the command:

    arccp chr_18.fa srm://bombay.csc.fi/fgi/userdirs/my_username/chr_18.fa

and then modify the input line defining the *chr_18.fa* file to:



    ("chr_18.fa" "srm://bombay.csc.fi/fgi/userdirs/my_username/chr_18.fa")

The output file of this job, *output.sam*, could be automatically saved
to the storage element in the same way by modifying the output
definition to:

    ("output.sam" "srm://bombay.csc.fi/fgi/userdirs/my_username/outpt.sam")

Thus a job description file using the storage element for both reading
the input and storing the results, would look similar to the example
below. Note that the command script (run\_bowtie2.sh) needs no
modifications.

    &(executable=run_bowtie2.sh)
    (jobname=bowtie2)
    (stdout=std.out)
    (stderr=std.err)
    (cputime="6 hours")
    (memory=4000)
    (runtimeenvironment=APPS/BIO/BOWTIE-2.0.0)
    (inputfiles=
    ("chr_18.fa" "srm://bombay.csc.fi/fgi/userdirs/my_username/chr_18.fa")
    ("reads.fq" "reads.fq")

    )
    (outputfiles=
    ("output.sam" "srm://bombay.csc.fi/fgi/userdirs/my_username/output.sam")
    )

When the job is finished the output can be retrieved with the command:

    arccp srm://bombay.csc.fi/fgi/userdirs/my_username/output.sam ./output.sam

 
