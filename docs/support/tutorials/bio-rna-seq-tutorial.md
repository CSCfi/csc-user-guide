# RNA-seq expression analysis hands-on tutorial: From FASTQ to differentially expressed genes
\\ \\

This tutorial describes an example RNA-seq expression analysis. First,
the analysis phases are presented step by step. In the last page,
running this kind of analysis in CSC environment (as a batch script) is
described. 

\\ \\

In the current tutorial, the tools are run in a [virtual machine image
downloadable
here](https://a3s.fi/yetukuri-2001115-pub/RNAseq_v1.ova). Part of the
analysis is done in R (also available in the virtual machine). The
virtual machine mimics the CSC environment (Puhti supercomputer): later,
when the Puhti-shell environment is in use, these steps can be run
there. Meanwhile, see the [guide page for interactive usage of
Puhti](https://docs.csc.fi/#computing/running/interactive-usage/).

\\ \\

**Note: we are currently updating this material!** If you have
questions, don't be shy to ask (see the [biospecialists contact
info](https://research.csc.fi/biosciences))!

\\ \\

Note: we have [tutorial videos explaining the RNAseq data analysis
steps](https://www.youtube.com/watch?v=fRKwj8igQ0U&list=PLjiXAZO27elBj3KYi7ACscgOxlNkNOxPc)
from previous courses (using Chipster software). 

\\ \\

Tutorial workflow and datasets  {style="caret-color: rgb(0, 0, 0); color: rgb(0, 0, 0);"}
-------------------------------

\\ \\

In this tutorial, you first start with raw reads (in fastq file), and
learn how to check the read quality, (FastQC, PRINSEQ), trim bad quality
bases (Trimmomatic), check the strandedness of the data (RSeQC), align
reads to genome (HISAT2), assess alignment quality (RSeQC) and count
reads per genes (HTSeq). The data for these first steps is a small
subset of single end RNA-seq reads from two human cell lines from
chromosome 19, h1-hESC and GM12878 (we practise with hESC sample). Note
that when analyzing differential expression you should always have at
least 3 biological replicates! We use this small dataset for the first
steps of the analysis to save resources: running the exercises with full
sample would take hours to complete, and the file sizes would require a
lot of memory, making it difficult to run the analysis on a VM.

\\ \\

After these steps, we change the dataset, and perform the differential
expression analysis steps in R (DESeq2, edgeR). Now we have a reasonable
number of replicates, as the starting point of this analysis is the
count table, and memory and running time won't be an issue at this
point. This data consists of 10 human samples, 5 from lung and 5 from
lymph node. You start with a count table and a phenodata file, which
describes the samples.

\\ \\

In the batch job section, where we learn how to effectively analyse the
data in Puhti, we use again subsetted fastq files. You perform the first
steps of the analysis (from fastq files to count tables) automatically
for the single-end hESC and GM12878 samples as an array job using a
batch script file. You can practise modifying the batch script for two
of the paired-end lung and lymphnode samples, which are already
subsetted so that they only have 200 000 reads.

\\ \\

The input data:
[https://a3s.fi/rnaseq\_course\_bucket/rnaseq\_raw\_data.tar.gz](https://a3s.fi/rnaseq_course_bucket/rnaseq_raw_data.tar.gz)

\\ \\

The analysis pipeline is illustrated in figure 1.

\\ \\

![RNAseq pipeline workflow: steps, tools and file
formats](/documents/48467/73374/RNAseq_pipeline_workflow.png/e9b06793-0b7c-40d9-9f18-57229d96ead6?t=1579850751005)

\\ \\

Figure 1. RNA-Seq analysis pipeline.

\\ \\

 
-

\\ \\

Preparatory steps
-----------------

\\ \\

Before starting the tutorial,  you need to perform following preparatory
steps:

\\ \\

### 1. Download and open the virtual machine

\\ \\

For this tutorial, we have prepared a virtual machine (VM) that includes
all the softwares and tools needed. The virtual machine has an Ubuntu
Linux operating system. You can open the VM on any computer that has
[Virtual Box](https://www.virtualbox.org) installed and [enough
memory](https://www.virtualbox.org/wiki/End-user_documentation). The VM
runs on top of the host computer, using the hosts resources, but you can
think of it as a separate computer: you can't access the files from the
host, and when you want to close the host computer, you need close the
VM too. 

\\ \\

Download the virtual machine image (rna-seq.ova -note, in the course,
this is already done for you!), and open it in Virtual Box. The password
for the VM is *rnaseq*. Tune the window so that it fits nicely on your
screen (see options in "View" tab, try for example *Auto-resize Guest
Display*, and put the *Scale Factor* to 100%). If you notice that
your mouse starts to behave strangely when using the VM, try changing
the window size: this usually resets the mouse.

\\ \\

Open Terminal. Open this page in browser (Firefox). 

\\ \\

-   [Using Virtual
    Box](https://www.virtualbox.org/manual/UserManual.html)

\\ \\

###  

\\ \\

### 2. Obtain sample data

\\ \\

Retrieve the input data for the tutorial, unpack it, and rename the
folder as *rnaseq*. 

\\ \\

    \
    wget https://a3s.fi/rnaseq_course_bucket/rnaseq_raw_data.tar.gz\
    tar zxvf rnaseq_raw_data.tar.gz\
    mv rnaseq_raw_data rnaseq

\\ \\

Move to the *rnaseq* folder and check the files you have there.

\\ \\

    \
    cd rnaseq\
    ls -lh

\\ \\

You can open the same folder in the virtual machine user interface: go
to Files -\> Home -\> rnaseq.  

\\ \\

New to command line? Don't worry, check the:

\\ \\

-   [CSC's quick reference guide (with unix commands
    listed)](https://docs.csc.fi/img/csc-quick-reference-2019-11-21.pdf)

\\ \\

###  

\\ \\

### 3. Load the conda modules that contain the analysis tools that you need in the tutorial

\\ \\

Next, we use the [Conda package management
system](https://conda.io/en/latest/) and load a module called *rnaseq*.
This loads all the pre-installed softwares and tools we need to our use.
When using Puhti, we do something similar with the *module load*
commands.

\\ \\

    \
    conda activate rnaseq

\\ \\

You can check the existing conda environments with command:

\\ \\

    \
    conda env list

\\ \\

-   [Conda user
    guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)
-   [CSC's Conda
    documentation](https://docs.csc.fi/support/tutorials/conda/)

\\ \\

 

\\ \\

The analysis steps can be found in the following pages:

\\ \\

[RNA-seq tutorial front page](https://research.csc.fi/rnaseq-tutorial)

\\ \\

1. [Preprocessing and trimming](https://research.csc.fi/rnaseq-trimming)

\\ \\

2. [Alignment](https://research.csc.fi/rnaseq-alignment)

\\ \\

3. [Analysis](https://research.csc.fi/rnaseq-counting)

\\ \\

4. [Analysing in Puhti](https://research.csc.fi/rnaseq-batchjob)

\\ \\

 

\\ }
