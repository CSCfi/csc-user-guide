# Using software through runtime environments

The FGCI environment contains a set of pre-installed software tools
because installing complex software tools within the grid job can be
difficult. The software installed on FGCI is used by accessing its **Run
Time Environment** (RTE). The RTE concept is analogous to the
*environment modules* used in the computing servers of CSC: the RTE adds
the commands of the selected software to the command path and sets up
the environment variables that the software uses. In addition, RTEs are
used to tell the ARC middleware what software are available on the
different clusters. The FGCI clusters don't all contain the same RTE:s.

List and usage examples about RTEs that are available in FGCI can be
found from the [FGI Runtime Environments pages](https://confluence.csc.fi/display/fgi/Runtime+Environments)

An RTE is taken into use by adding the *runtimeenvironment* parameter to
the job description file. For example, the RTE that is used for Bowtie2
software is referred to as APPS/BIO/BOWTIE-2.0.0. To use Bowtie2
commands in a grid job you should add following line to the job
description file:

`(runtimeenvironment="APPS/BIO/BOWTIE-2.0.0")`

Bowtie2 can utilize OpenMP based parallelisation. For the case of
programs which are capable of parallel computing, that is, running on
more than one core, the runtime environment can define the number of
computing cores to be used. This kind of arrangement allows the system
to automatically set the suitable core number, which may be different in
different clusters, for parallel processing. The core number defined by
the RTE is typically stored to an environment variable which is then
used to transport this information to the command to be executed.

Below is an example of a job description file (*bowtie2.xrsl*) that uses
the Bowtie2 RTE:

    &
    (executable=run_bowtie2.sh)
    (jobname=bowtie2)
    (stdout=std.out)
    (stderr=std.err)
    (cputime="6 hours")
    (memory=4000)
    (runtimeenvironment=APPS/BIO/BOWTIE-2.0.0)
    (inputfiles=
       ("chr_18.fa" "chr_18.fa")
       ("reads.fq" "reads.fq")
    )
    (outputfiles=>
       ("output.sam" "output.sam")
    )

In the command script file we use the environment variable
$BOWTIE\_NUM\_CPUS, defined by the RTE with the bowtie2 command:

    #!/bin/sh
    echo "Hello Bowtie2"
    bowtie2-build -p $BOWTIE_NUM_CPUS chr_18.fa chr_18
    bowtie2 -p $BOWTIE_NUM_CPUS chr_18 reads.fq > output.sam
    exitcode=$?
    echo "Bye Bowtie2!"
    exit $exitcode

Details about what parameters a certain RTE defines can be checked from
the home page of the RTE. In the case of Bowtie2 the address of the page
is: [https://confluence.csc.fi/display/fgi/Bowtie2+runtime+environment](https://confluence.csc.fi/display/fgi/Bowtie2+runtime+environment)
