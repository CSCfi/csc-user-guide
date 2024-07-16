# Getting started with supercomputing

You have signed up for your CSC account and first project, and are now ready to
scale up your computations! This page is intended to give you some idea of what
to expect from your journey into the exciting world of high-performance
computing.

## Which supercomputer to use?

Projects may have access to multiple supercomputers. New users are recommended
to start working on the Puhti supercomputer, which caters to a wide range of
use cases. In time, you may find that you need more extensive parallelization
options, in which case you may wish to run jobs on Mahti.

## Which interface to use?

### Web interface

There are multiple ways to run computations on CSC supercomputers. The Puhti
and Mahti web interfaces offer a beginner-friendly environment for working with
supercomputers. The web interface includes various interactive applications like
Jupyter, RStudio and Virtual Studio Code, which are useful for developing code
and exploring data.

### Command-line interface

Because of the considerable scale of both data and processing involved in
HPC, you might rather quickly find yourself in need of tools that are more
efficient and powerful than those offered by the graphical web interface. 
Effective use of supercomputers is based on running Unix commands in a
text-based interface. Learning to interact with CSC devices in this way
is a crucial step towards serious supercomputing.

For Linux and macOS, the most natural way of using command-line tools
is by opening a terminal and creating a remote SSH connection to a
supercomputer. Windows users do not have access to a Unix-like terminal, so the
recommended approach is using the login shell available in the supercomputer web
interface.

## General guidelines

### Developing code

Developing code is best done in interactive jobs run in the `interactive`,
`test` and `gputest` partitions. These partitions have the shortest queuing
times, which makes it easy to debug code with many quick successive runs.
Web interface applications like Jupyter can be useful for developing code, since
it is easy to test changes made to individual blocks of code without running the
entire script from the beginning. However, once you know your code works, you
should consider running it as a batch job.

### Running code

One of the most important command-line tools are the commands used for
interacting with the SLURM job scheduler. If your job requires a lot of
resources, as is typical for high-performance computing, it may queue for a long
time before it is run. Jobs based on interactive apps like Jupyter and RStudio
require you to manually run your code when the necessary resources become
available, which might happen in the middle of the night or at some other
inconvenient time. However, when you submit a batch job, any commands in the
batch script are executed when the job moves the queue to running on a node.
This makes batch jobs invaluable for HPC users.
