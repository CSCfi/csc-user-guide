# RNA-seq expression analysis hands-on tutorial: From FASTQ to differentially expressed genes

This tutorial describes an example RNA-seq expression analysis. First,
the analysis phases are presented step by step. In the last section,
running this kind of analysis in CSC environment (as a batch script) is
described. 

For running the step-by-step exercises on this tutorial, you have couple of options:

-   You can run the tools interactively on CSC's supercomputer Puhti (recommended, you need access to Puhti). See the [guide page for interactive usage of Puhti](https://docs.csc.fi/#computing/running/interactive-usage/.
-   You can run the tools using our ready-made [virtual machine image, downloadable here](https://a3s.fi/yetukuri-2001115-pub/RNAseq_v1.ova). The VM mimics the CSCs environment (Puhti supercomputer).
-   You can install the needed softwares on your own computer (link to the tools manual pages are given after each section)

Most of the tools are run on command line. Part of the analysis is done in R (also available in Puhti and in the virtual machine). The last section demonstrates the effective use of CSCs environments (Puhti and Allas).


!!! note
    **We are currently updating this material!** If you have
    questions, don't be shy to ask (see the [biospecialists contact
    info](https://research.csc.fi/biosciences))!


!!! note
    We have [tutorial videos explaining the RNAseq data analysis
    steps](https://www.youtube.com/watch?v=fRKwj8igQ0U&list=PLjiXAZO27elBj3KYi7ACscgOxlNkNOxPc)
    from previous courses, using [Chipster software](https://chipster.csc.fi). You are welcome to use Chipster as well! [More info on getting the started with Chipster](https://chipster.csc.fi/access.shtml). 

!!! note
    Interested in running this course in your own organisation? [See how to get student accounts](https://docs.csc.fi/accounts/how-to-create-new-user-account/#getting-student-accounts-for-courses)!

## Tutorial workflow and datasets 
-------------------------------


In this tutorial, you first start with raw reads (in FASTQ file), and
learn how to check the read quality, (using FastQC, PRINSEQ), trim bad quality
bases (Trimmomatic), check the strandedness of the data (RSeQC), align
reads to genome (HISAT2), assess alignment quality (RSeQC) and count
reads per genes (HTSeq). The data for these first steps is a small
subset of single-end RNA-seq reads from two human cell lines from
chromosome 19, h1-hESC and GM12878 (we practise with hESC sample). 

!!! note

    Please note that when analyzing differential expression **you should always have at
    least 3 biological replicates!**

We use this small dataset for the first steps of the analysis to save resources: running the exercises with full sample would take hours to complete, and the file sizes would require lots of memory.


After these steps, we change the dataset, and perform the differential
expression analysis steps in R (DESeq2, edgeR). Now we have a reasonable
number of replicates, as the starting point of this analysis is the
count table, which is a modest size file, and memory and running time won't thus be an issue at this
point. This data consists of 10 human samples, 5 from lung and 5 from
lymph node. You start with a count table and a phenodata file, which
describes the samples.


In the batch job section, where we learn how to effectively analyse the
data in Puhti, we use again the subsetted fastq files. You perform the now already familiar first
steps of the analysis (from fastq files to count tables) automatically
for the single-end hESC and GM12878 samples as an array job using a
batch script file. You can also practise modifying the batch script for two
of the paired-end lung and lymphnode samples, which are already
subsetted so that they only have 200 000 reads.


The input data:
[https://a3s.fi/rnaseq\_course\_bucket/rnaseq\_raw\_data.tar.gz](https://a3s.fi/rnaseq_course_bucket/rnaseq_raw_data.tar.gz)


The analysis pipeline is illustrated in figure below.

![RNA-Seq analysis pipeline](../../../img/rnaseq-pipeline.png "Figure 1. RNA-Seq analysis pipeline workflow: steps, tools and file formats.")


## Preparatory steps for Puhti use

Using Puhti supercomputer for the step-by-step exercises is the recommended way, if you are planning to run the analysis on Puhti later on. CSC's services are free of charge for academic research, teaching or training for members of Finnish higher education institutions and state research institutes. Please follow these [instructions for getting access to CSC services](https://research.csc.fi/accounts-and-projects). If you are not planning on using CSC's resources, but simply wish to learn the basics of RNA-seq data analysis, you can use the virtual machine (see the instructions below.)

To use CSCs supercomputer, you need some basic Linux skills. We suggest that you follow our [command line minicourse in e-lena](https://e-learn.csc.fi/course/view.php?id=58) or the [command line use basic tutorials](https://csc-training.github.io/csc-env-eff/#12-tutorials-and-exercises)

1.  [Get a user account, project and access to Puhti and Allas](https://research.csc.fi/accounts-and-projects)
2.  [Use NoMachine to connect to Puhti's login node with virtual desktop](../support/tutorials/nomachine-usage/)
3.  Go to your project's SCRATCH folder, create a folder for the tutorial data there
4.  Upload the data there
5.  Use the [interactive batch job](../computing/running/interactive-usage/) for running the examples


### 1. Get a user account, project and access to Puhti and Allas

[You can follow the instructions here](https://research.csc.fi/accounts-and-projects). In short, to get the user account, you log in to [MyCSC](http://my.csc.fi/) with your home organisations credentials (Haka or Virtu), and fill in a form in the sign up page, and then you receive an e-mail with your login information. (If you have CSC credentials already, use them.)

!!! note

    If you are attending a live course, we are likely to provide you course credentials. 

You should now have a CSC username, password and a project number.

### 2. Connecting to Puhti using ssh client

Connecting and using Puhti happens through a ssh client, such as Putty (Windows), or if you are using MacOS or Linux, the ssh command can be given in the Terminal.
-   [Connecting to Puhti](../computing/connecting/)
-   [Connecting to Puhti tutorial](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html)

Open Terminal or Putty, and type:

    ssh -X <csc_username>@puhti.csc.fi

You are now in the **login node** of Puhti. -X opens a graphical connection.

### 3. Connecting to Puhti with remote desktop (using NoMachine)

During the exercises, we are looking some graphics (plots and R-Studio), which is why we want to use the **remote desktop** provided with the NoMachine client. You need to download the **NoMachine Enterprise client** (not the Desktop) and install it on your own computer (note that installing may require admin rights). 
-   [Instructions for installing the NoMachine client and opening the connection](../support/tutorials/nomachine-usage/)

1.  [Download the **NoMachine Enterprise client**](https://www.nomachine.com/download-enterprise) (note: not the "Desktop", but "Client"!) and install it on your own computer.
2.  Follow the instructions for [configuration](../support/tutorials/nomachine-usage/#configuration) and [opening a connection](../support/tutorials/nomachine-usage/#open-connection).
3.  Once you see the black screen, click it, and choose to connect to Puhti. Give your CSC password when asked.

You should now have NoMachine connection to Puhti: a black virtual desktop with white terminal open in one of Puhti's login nodes. 

**Terminal** is the command line, where we will be typing our commands in the exercises. The commands are case-sensitive, so you need to be very precise when typing! Use the Tab button on your keyboard to finish the commands when possible. 
-   [Quick reference guide](../img/csc-quick-reference-2019-11-21.pdf) for command line commands etc
-   [Linux basics](../support/tutorials/env-guide/using-linux-in-command-line/)

### 4. Create a folder, upload the data there

Next, we move to our projects SCRATCH directory. You could now use either the ssh client or the NoMachine remote desktop for these commands: ssh client might be a bit easier, so we recommend that. You can't run analyses on your HOME directory.  
-   [Disk areas in Puhti](https://docs.csc.fi/computing/disk/)

note!
    SCRATCH directory is joined for all the members in the project! Be a good researcher and don't mess with other people's data. 


Replace the xxxxx below with your projects ID:

    cd /scratch/project_xxxxxxx

Check whether there are already some files in the SCRATCH directory. Then make a new folder rnaseq_test_yourname (add your name!) and go there:

    ls
    mkdir rnaseq_test_yourname
    cd rnaseq_test_yourname


Copy the files needed for the analysis to your folder, unzip the package, rename the folder as "rnaseq" and move to that folder:   

    wget https://a3s.fi/rnaseq_course_bucket/rnaseq_raw_data.tar.gz
    tar -xvzf rnaseq_batch_job.tar.gz
    mv rnaseq_raw_data rnaseq
    cd rnaseq
    ls -lh

Navigate to the same rnaseq folder also **with NoMachine**, and check that you see the same files:

    cd /scratch/project_xxxxxxx/rnaseq_test_yourname/rnaseq
    ls -lh

#### 5. Load the "biokit" module

CSC's Puhti has many users, and thus also many softwares installed. Often these softwares are mutually incompatible: this issue is solved by using **modules**. Different tools used in this analysis might require different modules. You can check which modules a tool needs from the [tools manual page](../apps.md).
-   [Learn about modules](../computing/modules.md)
-   [Biomodules in Puhti tutorial](https://csc-training.github.io/csc-env-eff/hands-on/modules/module-exercise-with-aligners.html)

Use **module load** command to load the **biokit** tools:

    module load biokit

#### 6. Interactive use of Puhti

As mentioned, it is forbidden to run any heavier tasks on the login nodes. Later on, we will learn how to run the commands learned in this tutorial for many samples effectively using a **batch job**. Now, when we are testing, learning and checking the results after each step, we need to use Puhti's **interactive partition**. 
-   [Interactive usage of Puhti](https://docs.csc.fi/computing/running/interactive-usage/)

Use the following command on the ssh client to launch an interactive session on a **computing node** (fill in your project ID in the prackets):

    sinteractive --account <project> --mem 8000 --tmp 100

Now you have everything set up for the actual exercises! Skip to the [Quality control, trimming and filtering section](#Quality-control,-trimming-and-filtering)!

## Preparatory steps for virtual machine use


In case you choose to run the exercises **in the virtual machine INSTEAD of Puhti**, perform the following preparatory
steps:


### 1. Download and open the virtual machine


For this tutorial, we have prepared a virtual machine (VM) that includes
all the softwares and tools needed. The virtual machine has an Ubuntu
Linux operating system. You can open the VM on any computer that has
[Virtual Box](https://www.virtualbox.org) installed and [enough
memory](https://www.virtualbox.org/wiki/End-user_documentation). The VM
runs on top of the host computer, using the hosts resources, but you can
think of it as a separate computer: you can't access the files from the
host, and when you want to close the host computer, you need close the
VM too. 

Download the virtual machine image (rna-seq.ova -note, in the course,
this is already done for you!), and open it in Virtual Box. The password
for the VM is *rnaseq*. Tune the window so that it fits nicely on your
screen (see options in "View" tab, try for example *Auto-resize Guest
Display*, and put the *Scale Factor* to 100%). If you notice that
your mouse starts to behave strangely when using the VM, try changing
the window size: this usually resets the mouse.


Open Terminal. Open this page in browser (Firefox). 

-   [Using Virtual
    Box](https://www.virtualbox.org/manual/UserManual.html)


### 2. Obtain sample data

Retrieve the input data for the tutorial, unpack it, and rename the
folder as *rnaseq*. 

    wget https://a3s.fi/rnaseq_course_bucket/rnaseq_raw_data.tar.gz
    tar zxvf rnaseq_raw_data.tar.gz
    mv rnaseq_raw_data rnaseq

Move to the *rnaseq* folder and check the files you have there.

    cd rnaseq
    ls -lh


You can open the same folder in the virtual machine user interface: go
to Files -\> Home -\> rnaseq.  


New to command line? Don't worry, check the:

-   [CSC's quick reference guide (with unix commands
    listed)](https://docs.csc.fi/img/csc-quick-reference-2019-11-21.pdf)



### 3. Load the conda modules that contain the analysis tools

Next, we use the [Conda package management
system](https://conda.io/en/latest/) and load a module called *rnaseq*.
This loads all the pre-installed softwares and tools we need for our analysis tutorial.
When using Puhti, we do something similar with the *module load*
commands.

    conda activate rnaseq

You can check the existing conda environments with command:

    conda env list


-   [Conda user
    guide](https://conda.io/projects/conda/en/latest/user-guide/index.html)
-   [CSC's Conda
    documentation](https://docs.csc.fi/support/tutorials/conda/)

Now we can get started with the actual analysis steps. 


## Quality control, trimming and filtering


First, we check the quality of the raw reads in the FASTQ files with
[FastQC](../apps/fastqc.md) and
[PRINSEQ](http://prinseq.sourceforge.net/manual.html) tools. After this,
we trim the reads with
[Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) to get rid
of possible poor quality bases and reads. As a bonus exercise, you can
try the trimming step also with PRINSEQ.


### 1. Check the quality of the reads with FastQC


Make a directory for the FastQC result files

    mkdir results-fastqc

Run FastQC:

    fastqc -o results-fastqc hesc.fastq.gz

Check what files were created with:

    ls -lh results-fastqc

Use:

    fastqc --help

to see what the parameter -o means.

Open the hesc\_fastqc.html file in browser. In Puhti, Firefox is available in bioconda module, so we load that first:

    module load bioconda
    firefox results-fastqc/hesc_fastqc.html

Close the html window when you are done viewing. 
It might be a bit slow to open/view, so another option is to load the html file to Allas and view it there:
    
    module load allas
    allas-conf project_XXXXXXXXX # replace
    a-flip results-fastqc/hesc_fastqc.html 

Copy the public link to your browser and view the FASTQ report there.

You can compare your FastQC report to [an example of a good Illumina
data](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/good_sequence_short_fastqc.html)
and to [an example of a bad Illumina
data](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/bad_sequence_fastqc.html).


How does the quality look like? How long are the reads? How many reads
are there? What do you think has happened? 

-   [More information about FastQC
    reports](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/)



### 2. Trim reads based on base quality with Trimmomatic

    mkdir results-trimmomatic


Trim bases from the 3' end if the base quality is less than 5, and keep
only those reads which are longer than 50 bases after trimming.

    trimmomatic SE -threads 1 -phred33 hesc.fastq.gz results-trimmomatic/hesc-trimmed.fq.gz TRAILING:5 MINLEN:50


Check in the screen output how many reads were dropped.

Check the Trimmomatic manual (linked below) to understand the syntax of
the command. What is the TRAILING parameter for? 


**Bonus:** Check the ILLUMINACLIP parameter from the manual. What is the
most likely cause for finding adapter sequences in the data? Do you need
some extra files to remove the adapters?


After trimming, see if the quality of the data was improved: run FastQC
again and compare the report to the original report.

    mkdir results-fastqc-after-trimming\
    fastqc -o results-fastqc-after-trimming results-trimmomatic/hesc-trimmed.fq.gz 
    firefox results-fastqc-after-trimming/hesc-trimmed_fastqc.html


What changes you can spot in the report? 


-   [Trimmomatic manual](http://www.usadellab.org/cms/?page=trimmomatic)


### 3. BONUS exercise: Trim reads based on base quality with PRINSEQ

Try the trimming step also with PRINSEQ with identical parameters: trim
bases from the 3' end if the base quality is less than 5, and keep only
those reads which are longer than 50 bases after trimming.

    prinseq-lite.pl -trim_qual_right 5 -trim_qual_rule lt -min_len 50 -no_qual_header -fastq hesc.fastq -out_good results-prinseq/hesc_trimmed -out_bad null -verbose


Check in the screen output: how many reads were dropped because of their
quality, and how many because they became too short?

    prinseq-lite.pl -help

to understand what the different parameters mean.


## Alignment

We retrieve a reference sequence, modify it a bit for testing purposes,
create the indexes and finally align our reads to this reference using
HISAT2 aligner. Then we check our alignment quality with RSeQC tool. We
also learn how to check the strandedness of the data.


### 1. Retrieve reference genome sequence, a GTF and a BED file

In this exercise we retrieve reference genome (fasta) in order to build
index files for HISAT2. For the interest of time, we'll use reference
data only for chromosome 19 (as our reads in the fastq file come from
genes located in that chromosome). Normally you would use the whole
genome. We also fetch the gene locations as a GTF and BED file formats
for later use.


-   [Read more about data
    formats](https://genome.ucsc.edu/FAQ/FAQformat.html)


With your web browser, go to [http://www.ensembl.org/info/data/ftp/](http://www.ensembl.org/info/data/ftp/).


In the Single species data table, click on the link for DNA (FASTA) for
Homo Sapiens. Right-click on the chromosome 19 file and copy the link
(ftp://ftp.ensembl.org/pub/release-82/fasta/homo\_sapiens/dna/Homo\_sapiens.GRCh38.dna.chromosome.19.fa.gz)

Get the file by typing wget and pasting the link
to the command line:

    wget ftp://ftp.ensembl.org/pub/release-82/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.19.fa.gz\


In the same way, obtain the GTF file: In the Single species data table,
click on the link for Gene sets, GTF for Homo Sapiens. Copy the link for
Homo\_sapiens.GRCh38.82.gtf.gz
(ftp://ftp.ensembl.org/pub/release-82/gtf/homo\_sapiens/Homo\_sapiens.GRCh38.82.gtf.gz)

Get the file by typing wget and pasting the link:

    wget ftp://ftp.ensembl.org/pub/release-82/gtf/homo_sapiens/Homo_sapiens.GRCh38.82.gtf.gz\

Check that you have the files and unzip the files in the folder.

    ls -lh
    gunzip Homo_sapiens.GRCh38.*

Check the beginning of the GTF file to see where the chromosome
information is located for each entry.

    head Homo_sapiens.GRCh38.82.gtf


Make a subset of the GTF file so that it contains only genes for
chromosome 19 (take rows starting with 19).

    grep -w ^19 Homo_sapiens.GRCh38.82.gtf > hg38chr19.gtf


Have a look at the beginning of the new GTF file. Does the first Havana
transcript entry have different values in gene\_id and transcript\_id
fields? This is important for the HTSeq tool that we will run later on.

    head -2 hg38chr19.gtf

Remove the original, whole genome GTF file using

    rm Homo_sapiens.GRCh38.82.gtf 

RseQC tool used after the alignment needs a BED file with gene locations
and a BAM file. You can fetch a BED file for chromosome 19 using [UCSC
Table browser](https://genome.ucsc.edu/cgi-bin/hgTables). BED file
included in the given data that you wget in the very beginning (refseq\_chr19\_actual.bed) was
originally obtained this way. It has a different chromosome naming to
what is used in your BAM file (chr19 vs 19), so you need to remove
the chr prefix first.

Substitute chr with nothing using the command sed:

    sed s/^chr// refseq_chr19_actual.bed > refseq_19.bed

Have a look at the BED file to see if the chr is gone with:

    head refseq_19.bed


### 2. Make an index file for HISAT2

!!! note
    For the course, indexes are already prepared for you: you don't need to run the commands with \# in beginning! 

    # mkdir hisat-indexes
    # hisat2-build Homo_sapiens.GRCh38.dna.chromosome.19.fa hisat-indexes/hs_19

You can build the index with just the command above. However, we are
learning to use also the gene locations information from the GTF file to
create the index. For this, you first need to generate these HISAT
specific splice site and exon files:

    hisat2_extract_splice_sites.py hg38chr19.gtf > splice_sites.txt
    hisat2_extract_exons.py hg38chr19.gtf > exons.txt
    # hisat2-build --ss splice_sites.txt --exon exons.txt Homo_sapiens.GRCh38.dna.chromosome.19.fa hisat-indexes/hs_19


This command will take some time to run, so in the course we won't run
this command. **Instead, these indexes are included in the given dataset.** You can
find them in the folder called *hisat-indexes*.


Check the index files. You should have there files hs\_19.1.ht2,
hs\_19.2.ht2...

    ls -lh hisat-indexes


Why are there so many files? 

!!! note
    Please note that creating the full indexes takes some time. You want to
    do this only once, or maybe [download the ready-made indexes from HISAT2
    page](https://ccb.jhu.edu/software/hisat2/index.shtml) (banner on the right side).



### 3. Align reads to reference genome with HISAT2

    mkdir results-hisat


Align reads to reference genome using the index which is located in the
hisat-indexes folder. Put the result files to results-hisat. Use

    hisat2 --help


to understand the syntax. 


-   [HISAT2 manual](http://ccb.jhu.edu/software/hisat2/manual.shtml)


### Bonus: Check the strandedness of your data & learn to install application from Bioconda

For alignment (HISAT2) and read counting (HTSeq), it is useful to know
if our data was created with a **directional protocol**. This means that
with some protocols, it is possible to tell from which strand the data
originally came from: are the reads from the same strand as the
genes/transcripts, or from the opposing ones. This helps in scenarios
where there are genes present in both strands at the same location. You
might now how your data is created, but if you don't know or aren't
sure, you can check it. 


For checking the strandedness, we want to get a subset of the data
(especially when our data would be a bit bigger than in this example
case of ours!), try aligning it (with the unstranded option) and then
use RSeQc tool infer\_experiment.py to get an estimate of the
strandedness. 


Subset the data: take 20 000 reads using [Seq Kit sample
tool](https://bioinf.shenwei.me/seqkit/usage/#sample):

    seqkit sample -s 15 hesc.fastq -n 200000 -o results-hisat/hesc_subset.fastq
    
!!! note 
    Seqkit is not installed in Puhti, which you probably noticed :) 
    So this is a great opportunity to learn how to install Bioconda packages to your own                environment in Puhti!
    First, read the [Bioconda documentation: Installing software for your own use with bioconda](../apps/bioconda/#2-installing-software-for-your-own-use-with-bioconda). Run the following commands to install Seqkit to "my_biotools" (first two commands you probably have run already):
    
    # export PROJAPPL=/projappl/project_xxxxxx
    # module load bioconda
    conda create -n my_biotools seqkit
    source activate my_biotools
    # Re-run seqkit:
    seqkit sample -s 15 hesc.fastq -n 200000 -o results-hisat/hesc_subset.fastq
    # Deactivate the my_biotools environment:
    conda deactivate


Run a "test alignment" with HISAT2 default parameters:

    hisat2 -q -x hisat-indexes/hs_19 -U results-hisat/hesc_subset.fastq -S results-hisat/hesc_subset.sam

Run the RSeqQC tool infer_experiment. 

!!! note
    RSeQC can be found in bioconda package in Puhti, so load that first with ```module load bioconda```
    NOT WORKING ATM!!!

    infer_experiment.py -i results-hisat/hesc_subset.sam -r refseq_19.bed > results-hisat/strandedness_data.txt


Check the output. Does the data seem to be ++,-- or +-,-+ type? The
strandedness parameters in different tools can be a bit confusing. Study
from [RSeQC infer-experiment.py manual
page](http://rseqc.sourceforge.net/#infer-experiment-py) what
this output means. Compare this knowledge to the [HISAT2
manual](http://ccb.jhu.edu/software/hisat2/manual.shtml)(check the - -
rna-strandness parameter). Do you know which parameter to use for this
data? Maybe the table on [Chipster software's strandedness
summary](https://chipster.csc.fi/manual/library-type-summary.html)
helps!


**Bonus:** Similarly, you could check the inner distance with the
[RSeQC inner-distance.py
function](http://rseqc.sourceforge.net/#inner-distance-py). You need
this information for the alignment of paired-end reads. Check the HISAT2
manual to see what are the default parameters for the minimum
(-I/--minins ) and maximum (-X/--maxins) inner distances.


### 4 Alignment and BAM file


Finally, let's run HISAT2 to align our data:

    hisat2 -q -x hisat-indexes/hs_19 -U results-trimmomatic/hesc-trimmed.fq.gz --rna-strandness F -S results-hisat/hesc.sam\


What was the alignment rate? How many reads aligned multiple times? 

!!! note
    Please note that this is a toy dataset, which has unreasonably good alignment rate (in fact, this fastq file was created by selecting reads that did align) -so don't get conserned if the alignment rate with your data is not as good!

Let's convert the SAM into BAM.

    cd results-hisat
    samtools view -bS hesc.sam > hesc.bam
    ls -lth


View the hesc.bam as text and check in the header if the alignments have
been sorted:

    samtools view -h hesc.bam | less


You can see the next page by pressing the spacebar and quit with q.
Check the first couple of alignments. Can you find the different fields
and tags?


Sort and index the BAM file:

    samtools sort hesc.bam -o hesc_sorted.bam
    ls -lth
    samtools index hesc_sorted.bam
    ls -lth


Return to the rnaseq folder with

    cd ..


### 5. Perform quality control at alignment level with RseQC

Make a directory for RseQC result files:

    mkdir results-rseqc


RseQC consists of several Python scripts, which we run separately. Check
how many alignments are there and how many of them are non-primary
alignments. Note that some of the result comes to the stderr stream,
which you direct to a file using 2\>, and some to stdout stream, which
you direct to file using \>. Open the folder results-rseqc so that you
can view the files when they are generated.


Check some statistics about the alignment. How many alignments are
there? How many reads are spliced?

    bam_stat.py -i results-hisat/hesc_sorted.bam > results-rseqc/hesc-stats.txt


Get an overview of the read distribution. Do most of the reads map to
exons?

    read_distribution.py -r refseq_19.bed -i results-hisat/hesc_sorted.bam > results-rseqc/hesc-distribution.txt


Check if this tool counts all reads:

    read_distribution.py -help


Check if the coverage is uniform along the transcripts:

    geneBody_coverage.py -r refseq_19.bed -i results-hisat/hesc_sorted.bam -o results-rseqc/hesc
    xdg-open results-rseqc/hesc.geneBodyCoverage.curves.pdf 


Check how many of the splice junctions are novel:

    junction_annotation.py -r refseq_19.bed -i results-hisat/hesc_sorted.bam -o results-rseqc/hesc 2> results-rseqc/hesc-junction-counts.txt 
    xdg-open results-rseqc/hesc.splice_events.pdf 
    xdg-open results-rseqc/hesc.splice_junction.pdf 


Check the saturation status of the splice junctions:

    junction_saturation.py -r refseq_19.bed -i results-hisat/hesc_sorted.bam -o results-rseqc/hesc
    xdg-open results-rseqc/hesc.junctionSaturation_plot.pdf 


### **Bonus:** Check the alignment in IGV genome browser

You can view the BAM files in [IGV Genome
Browser.](http://software.broadinstitute.org/software/igv/) Practise
using IGV by browsing
to [https://igv.org/app/](https://igv.org/app/) and uploading the BAM
and BAI files: Tracks -> Local files -> select *hesc_sorted.bam* and
*hesc_sorted.bai* in the results-hisat folder (use ctrl to select two
files). Check that you have the correct reference (hg19). Navigate for
example to location chr19:281,093-281,252. Try zooming in and out. Which
gene are we now looking at? Can you see any reads? What is the
coverage? Can you spot any SNPs? 






# Counting reads & differential expression analysis

We count the number of reads for each gene using HTSeq tool. After this
we move the data to R and perform differential expression analysis with
two different tools: DESeq2 and edgeR. Finally we annotate the ensembl
IDs with gene names. For demonstration purposes, we now use different
dataset (with more samples) in the R part -when you are performing your
own analysis, use the whole dataset.


## Count reads per genes using HTSeq

    htseq-count -f bam --stranded=yes results-hisat/hesc_sorted.bam hisat-indexes/hg38chr19.gtf > hesc-counts-raw.tsv

Check what the different parameters mean. What is the minimum mapping
quality for a read to be counted? Was the strandedness parameter
correct?

    htseq-count --help

Look at the beginning and the end of the result file. Can you see genes
with counts? How many alignments did not overlap with any gene?

    head hesc-counts-raw.tsv
    tail hesc-counts-raw.tsv

Remove the last 5 rows starting with "_ _" (keep all but the last 5
rows).

    head -n -5 hesc-counts-raw.tsv > hesc-counts.tsv



**Bonus exercise:** Can you repeat the steps to the other sample
(GM12878.fastq.gz)?

For the next step, you need to combine your count files into one file,
so that each sample has one count column. To make this tutorial run
smooth, we switch now to another data set with several samples -in real
life, you would repeat the previous preprocessing and alignment steps
for each sample (in a batch job), and then combine the samples into one count table. You
would run these steps in our supercomputers, and through a script -we
will take a look into that a bit later, once we first have learned all
the individual steps of the analysis.

!note
    In real life, you would use a script to process all the
    samples at once (as a batch job). We will learn this a bit later.


## RNA-seq differential expression analysis using R

Next, we load the count table and another table describing the samples
to R. We are performing the differential expression analysis with two
packages/tools, DeSeq2 and edgeR, so we load those packages to R. ggplot
package is used for visualisations.


These R commands are also available in this R-script
file: https://biotraining.object.pouta.csc.fi/rnaseq\_tutorial/RNA-Seq-Rscript.R


### 1. Preparations


Option A) You can use R and RStudio on CSC's supercomputers. The Bioconductor packages needed here are already installed there (?). To use RStudio in Puhti, you first need to set up the ssh keys.

-   [R on CSC's environments](--/apps/r-env-singularity)
-   [Using RStudio in Puhti](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/)
-   [Setting up the SSH keys](../computing/connecting/setting-up-ssh-keys)

Option B) In virtual machine: Open RStudio (or R) in the virtual machine: activate the Conda base
environment and type rstudio. 

    conda activate base
    rstudio

Option C) You can also run these steps on your own computer, in which case
you need to install these packages as descriped below.


Open a new R Script file (File -\> New File -\> R Script). Type or copy
your commands here. You can run the commands from there (paint the
command and use ctrl + enter, or use the Run button). This way it is
easier to track what you have done so far.


!note
    In the ready-made virtual machine, you can skip the
    installation steps, but you need to run the library commands to load the
    packages.

To install and load Bioconductor-packages to R:

    # Note: everything after # is a comment -R won't run it!
    # No need to run the installation commands on the VM:
    # source("https://bioconductor.org/biocLite.R")
    # biocLite("DESeq2")
    # biocLite("edgeR")
    # Update all/some/none? [a/s/n]: n
    # install.packages("ggplot2")
    
    # Load the libraries:
    library(DESeq2)
    library(edgeR)
    

Change the directory in RStudio to the rna-seq folder. Either choose
Session -\> Set Working Directory -\> Choose Directory -\> rna-seq -\>
Open, OR just type:

    setwd("~/rnaseq")


Read in the data, and examine it in R. What information is stored in
phenodata.tsv, and what's in counts\_data.tsv? How many samples there
are? How many genes there are counts from? 

You downloaded the files already with wget, and they should now be in
the rna-seq folder. 

    counts_data <- read.table("ngs-data-table.tsv", header=T, sep="\\t", row.names=1)\
    phenodata <- read.table("phenodata.tsv", header=T, sep="\\t")\


Get the experimental group information from the phenodata file. By
checking the phenodata.tsv you learned that "group" is the column you
want.

    group <- "group"
    groups <- as.character (phenodata[,group])


### 2A. Diffrential expression analysis with DESeq2


Let's perform differential expression analysis with DeSeq2 tool. We can
also draw a PCA plot and a dispersion plot. From the PCA plot we can see
if the samples are separating nicely, and whether there are some
outliers in the data.

-   [DESeq2 manual](https://bioconductor.org/packages/devel/bioc/manuals/DESeq2/man/DESeq2.pdf)
-   [DESeq2 beginners guide](http://bioc.ism.ac.jp/packages/2.14/bioc/vignettes/DESeq2/inst/doc/beginner.pdf)

 
    #Create a DESeqDataSet object
    dds <- DESeqDataSetFromMatrix(countData=counts_data, colData=data.frame(groups=groups), design = ~ groups)
    #Calculate statistic for differential expression, merge with original data table, keep significant DEGs, remove NAs and sort by FDR.
    dds <- DESeq(dds) # The standard differential expression analysis steps are wrapped into a single function, DESeq
    res <- results(dds) # Results tables are generated using the function "results"
    sig <- cbind(counts_data, res) # combine original table and results table
    sig <- as.data.frame(sig) # DataFrame != data.frame :
    p.value.cutoff <- 0.05
    sig <- sig[sig$padj <= p.value.cutoff, ] # choose adj. p-values < the cut off (0.05)
    sig <- sig[! (is.na(sig$padj)), ] # remove NAs
    sig <- sig[ order(sig$padj), ] # order accroding to the adj. p-values
    DESEq2_DEGs <- sig

    #Get summary and write a .tsv-table. Open the table in Excel.
    summary(res, alpha=p.value.cutoff)
    write.table(sig, file="significant_DEGs_pval005_with_DESeq.tsv", sep="\\t", row.names=T, quote=F)

How many differentially expressed genes were there between the samples?
How many were up and how many were downregulated?

### Experiment level quality control: PCA plot


Let's draw a PCA plot, so we can see how well the samples are separated.
PCA plot can be used in experimental level quality control. From the PCA
plot, we can see whether there are possible outliers, some underlying
batch effects, and whether our samples are separated as expected (based
on the experimental sample groups).

We also draw a dispersion plot of the normalized read counts, which
shows us how the read counts are modified within DESeq2.

    ## PCA plot (using DESeq2):
    library("ggplot2")
    
    # Perform transformation (sort of normalization, PCA needs these)
    vst<-varianceStabilizingTransformation(dds)
    head(assay(vst))
    
    # Make PCA plot
    data <- plotPCA(vst, intgroup=c("groups"), returnData=TRUE)
    percentVar <- round(100 * attr(data, "percentVar")) # Tidy the variance percentage
    desc <- phenodata[,"description"] # Get the sample descriptions from phenodata.
    p <- ggplot(data, aes(PC1, PC2, color=groups, title="PCA plot for TREATMENT")) +
      geom_point(size=6) +
      geom_text(aes(label=desc),hjust=0, vjust=1.7, color="black", size=4) +
      xlab(paste0("PC1: ",percentVar[1],"% variance")) +
      ylab(paste0("PC2: ",percentVar[2],"% variance"))
    # Adjust figure size and save it.
    ggsave(p, filename = "PCA plot.pdf", width = 15, height = 12)
    
    ## Dispersion plot:
    plotDispEsts(dds, main="Dispersion plot", cex=0.2)


You should get the following plots as outputs:

![PCA and dispersion plots](../../../img/PCA_and_dispersion_plot.png "PCA and dispersion plots.")

PCA and dispersion plots.


Do the experimental groups separate from each other? Are there any
outliers? How much (%) variation is explained by the first principal
component (PC1)? What about PC2? What do you think these components
represent?


Are any counts left as outliers?

### Bonus: Drawing a heatmap

Let's draw a heatmap of the most highly variable genes: 

    library(pheatmap)
    library(biomaRt)
    
    # get the vst transformed read counts:
    trans_counts <- assay(vst)
    
    # subset: get the top 500 most variable genes
    var_genes <- apply(trans_counts, 1, var) # compute variance of the transformed counts
    head(var_genes)
    select_var <- names(sort(var_genes, decreasing=TRUE))[1:50] # sort based on variance and select top 50 most variable genes
    head(select_var)
    highly_variable_genes <- trans_counts[select_var,] # select these genes from trans counts table
    dim(highly_variable_genes)
    
    # Get the annotations:
    ensembl <- useMart("ensembl", host= "www.ensembl.org", dataset="hsapiens_gene_ensembl")
    variable_gene_names <- getBM(attributes <- "external_gene_name", filters = "ensembl_gene_id", values = rownames(highly_variable_genes), mart = ensembl, uniqueRows=T)
    rownames(highly_variable_genes) <- as.matrix(variable_gene_names)
    
    pheatmap(highly_variable_genes)


![Heatmap of most variable genes](../../../img/heatmap_rna_seq.pdf "Heatmap of most variable genes.")

Heatmap of most variable genes.

### 2B. Diffrential expression analysis with edgeR

Let's perform the same differential expression analysis with another
tool, edgeR.

-   [EdgeR user guide](https://www.bioconductor.org/packages/devel/bioc/vignettes/edgeR/inst/doc/edgeRUsersGuide.pdf)

In R: 

    # Form the DGElist object:
    dge<-DGEList(counts=counts_data)
    
    # Filter out genes which have less than 5 counts in user-defined number of samples
    filter <- 5 # "Analyze only genes which have counts in at least this many sample
    keep <- rowSums(dge$counts>5) >= filter
    dge <- dge[keep,]
    dge$lib.size <- colSums(dge$counts)
    
    # Calculate normalization factors
    dge<-calcNormFactors(dge) # take a look at the dge-object!
    
    # Modeling formula & design matrix
    group <- factor(phenodata$group)
    
    design <- model.matrix(~group)
    rownames(design) <- phenodata$description # take a look at the design matrix!
    
    # Estimate dispersions
    dge <- estimateDisp(dge, design)
    # Take a look at the dge-object, and compare the common dispersion value to trended dispersion values
    
    # Dispersion plot
    plotBCV(dge, main="Biological coefficient of variation")
    
    # Estimate DE genes
    # Generalized Linear Model (GLM) Likelihood Ratio Test
    fit<-glmFit(dge, design) # fits the negative binomial generalized linear model (GLM)
    lrt<-glmLRT(fit, coef=2) # likelihood ratio test (LRT)
    # Note: coef=2 -> comparison between the "groups"
    tt<-topTags(lrt, n=nrow(counts_data))
    ttres <- data.frame(tt)
    
    # Rounding:
    ttres2<-round(ttres,6) # Compare the first 15 rows of ttres and ttres2 to see the effect of rounding
    
    # Add count columns to the result table
    counts_table <- getCounts(dge) # pick the counts from the dge object
    counts_table<-counts_table[pmatch(rownames(ttres), rownames(counts_table)),] # organize counts_table according the FDR
    ttres2<-cbind(ttres2, counts_table) # combine the two
    
    # Write the results to file
    write.table(ttres2, file="edger-results.tsv", sep="\\t", row.names=T, col.names=T, quote=F)
    
    # Filtering the EdgeR results table:
    # Check the colnames:
    colnames(ttres2)
    # You want to filter those DEGs that have FDR < 0.05 in this treatment-comparison:
    filt_dat <- ttres2[ttres2$FDR<0.05,]
    write.table(filt_dat, "filtered-edgeR-results.tsv", sep="\\t", row.names=F, col.names=T, quote=F)



As a result, you should get the following plot and the results.tsv
table:

![Variation plot](../../../img/Rplot-plotBCV.jpg "Variation plot")


Compare the dispersion plots from DESeq2 and edgeR, do they look
different? Why do you think this is?


How many differentially expressed genes did you get now?


### 3. Annotate the Ensembl IDs

Finally, let's annotate our lists of genes with actual gene names. We
are using biomaRt package.

-   [biomaRt users guide](https://bioconductor.org/packages/release/bioc/vignettes/biomaRt/inst/doc/biomaRt.html#introduction)

In R: 

    # Load the biomaRt package:
    # source("https://bioconductor.org/biocLite.R")
    # biocLite("biomaRt")
    library(biomaRt)
    
    # Make a list of Ensembl-identifiers which we want to annotate:
    dat <- filt_dat # = the filtered edgeR table
    genes <- rownames(dat)
    
    # Get the annotations:
    # Choose which database and dataset to use (we use ensembl and hsapiens).
    # You could use commands listMarts(), listDatasets() and ListAttributes() to see what is available.
    ensembl <- useMart("ensembl", host= "www.ensembl.org", dataset="hsapiens_gene_ensembl")
    genes_ensembl_org <- getBM(attributes <- c("entrezgene_id", "ensembl_gene_id", "external_gene_name", "description"), filters = "ensembl_gene_id", values = genes, mart = ensembl, uniqueRows=T)
    
    # Build a table: combine the DEG values to the annotation information
    pmatch_table    <- pmatch(genes, genes_ensembl_org[,2], duplicates.ok=T)
    ensembl_table      <- as.data.frame(matrix(NA, nrow=length(genes), ncol=8))
    ensembl_table[which(!is.na(pmatch_table)),] <- genes_ensembl_org[pmatch_table[(!is.na(pmatch_table))], ];
    rownames(ensembl_table)    <- genes;
    colnames(ensembl_table) <- colnames(genes_ensembl_org);
    results <- cbind(ensembl_table[,3:4], dat);
    colnames(results) <- c("symbol", "description",  colnames(dat));
    rownames(results) <- rownames(dat)
    
    # write result table to output
    write.table(results, file="annotated_results_edgeR.tsv", col.names=T, quote=F, sep="\\t", row.names=T)


What was the most differentially expressed gene? 


### 4. Enrichment analysis

Lastly, we learn how to study the enrichment of certain kind of genes
amongst the differentially expressed genes.

    setwd("/home/rnaseq/rnaseq/Enrich")  # Set the working directory
    library(enrichR) # Load enrichR package, an enrichment analysis tool
    library(fgsea) # Load r version of GSEA package, a popular enrichment analysis tool
    library(biomaRt) # Load annotation package
    library(pheatmap) #Load package for drawing heatmaps
    
    # Use this ready-made toy example dataset prepared for enrichment analysis from the DESeq2 output.
    # Only data with gene names as queried from Biomart package are retained here.
    rnaseq_data <- read.table("dataset_with_gene_names_DESeq.tsv", header=T, sep="\\t", row.names=1)


#### Over representation analysis using enrichR package

Over representation analysis using enrichR package, where we
keep only most significant results to perform enrichment analysis. The
first steps are similar to the steps performed earlier to the DESeq2
results.

    p.value.cutoff <- 0.05
    rnaseq_sig <- rnaseq_data
    rnaseq_sig <- rnaseq_sig[rnaseq_sig$padj <= p.value.cutoff, ] # choose adj. p-values < the cut off (0.05)
    rnaseq_sig <- rnaseq_sig[! (is.na(rnaseq_sig$padj)), ] # remove NAs
    rnaseq_sig <- rnaseq_sig[ order(rnaseq_sig$padj), ] # order accroding to the adj. p-values
    
    # Draw heatmap just to see the clusters in the dataset especially when you have several singficant genes.
    # Please note that this is not a requirement for doing enrichment analysis:
    
    clust <- pheatmap(rnaseq_sig[,1:10], scale = "row" , color = colorRampPalette(c("blue","white","red"))(255), border_color = NA, cluster_cols = F)
    
    gene_clusters <- cutree(clust$tree_row,k = 2) # cut the hclust tree to get the groups by specifying
    # number of groups
    
    # listEnrichrDbs() # uncomment to see the available gene lists
    # Get gene names of each cluster and characterise the cluster with enrichment analysis
    cluster1 <- names(gene_clusters)[gene_clusters == 1]
    cluster2 <- names(gene_clusters)[gene_clusters == 2]
    
    # Enrichment analysis with GO terms; you can modify the gene sets by checking 'listEnrichrDbs()' function
    dbs <- c("GO_Molecular_Function_2018", "GO_Cellular_Component_2018", "GO_Biological_Process_2018")
    go_cluster1 <- enrichr(genes = cluster1,databases = dbs[1]) # just query one Database for illustration.
    # 1 = Molecular Function, 2 = Cellular Component, 3 = Biological process
    go_cluster1 <- go_cluster1[[dbs[1]]]
    go_cluster1 <- go_cluster1[order(go_cluster1$Adjusted.P.value),] # get top enriched pathways
    
    cbind(go_cluster1$Term[1:15],go_cluster1$Adjusted.P.value[1:15]) # check top enrichedpathways
    
    # Plot top enriched pathways
    par(1,1,mar=c(4,20,4,4))
    barplot( -log10(go_cluster1$Adjusted.P.value[10:1]), xlab="Adjusted P value", horiz = T, names.arg = go_cluster1$Term[10:1],las=1)
    
    #dev.off()


Exercise: Repeat similar analysis with other clusters and pathways databases like Reactome and KEGG
    #React_cluster2 <- enrichr(genes = cluster2,databases = "Reactome_2016")
    #React_cluster2 <- React_cluster2$Reactome_2016
    #React_cluster2 <- React_cluster2[order(React_cluster2$Adjusted.P.value),]


#### Perform genome-wide enrichment analysis (GSEA) with unfiltered data set

Perform Gene Set Enrichment Analysis (GSEA) using gene sets from
MSigDB as downloaded from [(https://www.gsea-msigdb.org/gsea/](https://www.gsea-msigdb.org/gsea/)
Check meaning of gene sets here:
[https://www.gsea-msigdb.org/gsea/msigdb/collections.jsp](https://www.gsea-msigdb.org/gsea/msigdb/collections.jsp)


    # Register and download DBs files and use gene set as it relates to your experiments
    KEGG_pathways <- gmtPathways("./MSigDB/c2.cp.kegg.v6.2.symbols.gmt.txt")
    # Order of genes matter here.
    # One needs to give sorted list according certian criteria.
    # We use logfold change value as sorting criteria;
    # one may use t-statistic,p-value, combination of fold change and p - value
    gene_rank <- rnaseq_data[,"log2FoldChange"]
    names(gene_rank) <-  rownames(rnaseq_data) # need gene names (check gmtPathways to see accepted Gene IDs )
    
    # Run actual gene set enrichment analysis:
    fgRes <- fgsea(pathways=KEGG_pathways, stats=gene_rank, minSize=15, maxSize=500, nperm=10000)
    
    # Retrieve enriched up/down regulated pathways based on the adjusted p-values
    # NES = Normalised Enrichment Score
    Up_regulated <- fgRes[NES > 0][head(order(padj), n=10), pathway]
    Down_regulated <- fgRes[NES < 0][head(order(padj), n=10), pathway]
    topPathways <- c(Up_regulated, rev(Down_regulated))
    
    # Plot top enriched pathways
    par(1,1,mar=c(2,20,2,2))
    plotGseaTable(KEGG_pathways[topPathways], gene_rank, fgRes, gseaParam = 0.5)
    dev.off()
    # Draw enrichment plot for selected pathways
    plotEnrichment(KEGG_pathways[["KEGG_DNA_REPLICATION"]],  gene_rank)


## Automate the analysis workflow using the array job functionality in Puhti

Once we know the steps we want to run for each sample, we can automate
the analysis and run the tools in Puhti as a batch job. In our case, we
are using an array job, as we are doing several similar independent
analysis.

Now we try a ready-made array script (rnaseq\_array\_job\_script.sh)
which needs the following things:

-   fastq.gz files for all samples
-   file fastq.list containing the fastq file names
-   BED file refseq\_19.bed
-   the folder HISAT2-indexes


First, open Terminal and log in to Puhti with your user credentials.

    ssh <csc_username>@puhti.csc.fi

More information about running jobs in Puhti:

-   [Connecting to Puhti](https://docs.csc.fi/computing/overview/)
-   [Running batch jobs in Puhti](https://docs.csc.fi/computing/running/getting-started/)
-   [Array jobs in Puhti](https://docs.csc.fi/computing/running/array-jobs/)
-   [How to get started with CSC services](https://research.csc.fi/accounts-and-projects)

Next, we move to our projects SCRATCH directory. You can't run analyses
on your HOME directory.  

!!! note
    SCRATCH directory is joined for all the members in the project! Be a good researcher and don't mess with other people's data.

Go to your projects SCRATCH directory (use your project ID instead of the X's:)

    cd /scratch/project_xxxxxxx

More information about Puhti disk areas and projects:

-   [Puhti disk areas](https://docs.csc.fi/computing/disk/)
-   [How to create a project](https://docs.csc.fi/#accounts/how-to-create-new-project/) 


Check whether there are already some files in the SCRATCH directory.
Then make a new folder test\_yourname (add your name!) and go there:

    ls
    mkdir rnaseq_test_yourname
    cd rnaseq_test_yourname

Copy the files needed for the analysis to your folder and unzip the
package:

    
    wget https://a3s.fi/rnaseq_course_bucket/rnaseq_batch_job.tar.gz
    tar -xvzf rnaseq_batch_job.tar.gz
    cd rnaseq_batch_job
    ls -lh


How many samples (=FASTQ files) are there? Check the files listed in
fastq.list:

    less fastq.list

Check what the script looks like:

    less rnaseq_array_job_script.sh

Are the parameters reasonable?


-   How many jobs are we launching? How many cores and memory is each
    job using? How much time is reserved per each job?
-   Which partition are we using? Is the project correctly assigned?
-   How is the sample name changed in each job?

To run all the tools we need, we need to load a couple of modules. Check
which modules are loaded from the script. You can see which modules you
need from the software pages: for example, for FastQC you need to module
load biokit.


-   [Modules in Puhti](https://docs.csc.fi/computing/modules/)
-   [Applications available in Puhti  ](https://docs.csc.fi/apps/)


Run the script with sbatch command. 


    # During a live course:
    sbatch --reservation=our_reservation_name rnaseq_array_job_script.sh
    # Other time:
    sbatch rnaseq_array_job_script.sh

Follow your job with command:

    squeue -l -u your_username


Check your finished job with command:

    sacct -u csc_username

Check the files created: 

    ls -lh


Use the job ID (something like 1062932) to get some information about
the run:

    seff your_job_id


How much time did the job took? Were the reserved resources OK for the
job (check the CPU and Memory Efficiency %)?

### **Bonus: Working with paired-end data**


The lung and lymhnode samples are paired-end. What kind of
modifications would the bash script need to be able to run the analysis
steps on these samples? Take a look at the
rnaseq\_array\_job\_script\_PE.sh file. (Don't run the script in the
course, as it will take 2 hours.)


### Moving your data to Allas

After you are done with the analysis, you want to store the data in
Allas. From Allas, you can also easily share some of the files to your
colleagues.

-   [Using Allas to host a dataset in a research project](https://docs.csc.fi/data/Allas/allas_project_example/)
-   [What is Allas?](https://docs.csc.fi/data/Allas/introduction/)
-   [a-commands in Allas](https://docs.csc.fi/data/Allas/using_allas/a_commands/)

Load Allas module and set up a connection to Allas:

    module load allas
    allas-conf project_XXXXXXX

Now we can store our data to Allas. After the data is in Allas, you can
delete it from Puhti: SCRATCH directory is automatically cleaned every
90 days, but it might be easier to remember to move your data to Allas
if you try to keep your SCRATCH directory clean. We use
[a-commands](http://docs.csc.fi/data/Allas/using_allas/a_commands/) to
load the data:

    cd ..
    ls -lh
    a-put rnaseq_batch_job
    a-check rnaseq_batch_job
    a-list
    a-list XXXXXX-puhti-SCRATCH

Where did the data go now? Try it a bit differently:

    a-put rnaseq_batch_job -b yourname_rnaseq_bucket -o yourname_rnaseq_data
    a-list yourname_rnaseq_bucket


Where is the data now?

Often we also want to share some of our data with our colleagues. If
they are in the same project, they can of course access the data in
Allas and in Puhti. However, if this is not the case, you can use
a-publish command, and share the data via an URL.

!!! note
    **Do remember, that data shared this way is easily accessible to
    third parties as well!** Thus, before loading the data with a-publish,
    consider encrypting it first with command **gpg**.


-   [Best practises for encryption](https://research.csc.fi/best-practices-for-client-side-encryption)

Let's practise some basic encryption:

    cd rnaseq_batch_job
    tar czf yourname_rnaseq_counts.tar.gz results-htseq
    gpg --symmetric --cipher-algo AES256 yourname_rnaseq_counts.tar.gz
    # Give a password!
    a-publish yourname_rnaseq_counts.tar.gz.gpg

Copy the public link, and send that to your colleague. Text the password to colleague.

Now you can wget the package and decrypt it, which is when the tool asks
for the password. You can try this:

    wget link
    gpg -o yourname_rnaseq_counts.tar.gz -d f yourname_rnaseq_counts.tar.gz.gpg
    # Give the password when asked.



