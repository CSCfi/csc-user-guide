# BWA

Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively short nucleotide sequences against a long reference sequence such as the human genome. It implements three algorithms, BWA-MEM (`mem`), BWA-Backtrack (`aln`) and BWA-SW (`bwasw`). BWA-Backtrack works for query sequences shorter than 200bp. The other two algorithms are used longer reads up to around 100kbp. BWA-MEM is recommend for reads longer than 70 gb.  All algorithms do gapped alignment.

BWA can be used to align both single-end and paired end reads to a reference genome or sequence set.


## Available

-   Puhti: 0.7.17
-   [Chipster](https://chipster.csc.fi) graphical user interface


## Usage

In Puhti, BWA can be taken in use as part ofth the _biokit_ module collection:

```text
module load biokit
```

The biokit modules sets up a set of commonly used bioinformatics tools, including  BWA. (Note however that there are bioinformatics tools in Puhti, that have a separate setup commands.)

The basic syntax of BWA commands is:

```text
bwa <command> [options]
```

### BWA indexes

CSC does not maintain pre-compiled BWA indexes for reference genomes in Puhti, but you can check if genomes used in Chipster can provide you a ready made index for a genome you want use. This can be done with command:

```
chipster_genomes bwa
``` 

If suitable genome index is not found the fist step in creating alignment with BWA is downloading the reference genome and indexing it. Please note that your $HOME directory is often too small for working with complete genomes. In stead you should do the analysis in scratch directory of your Puhti project ($SCRATCH).

You can use for example command `ensemblfetch` or `wget` to download a reference genome to Puhti. For example

```text
ensemblfetch homo_sapiens
```

The command above retrieves the human genome sequence to a file called Homo_sapiens.GRCh38.dna.toplevel.fa. You can calculate the BWA indexes for this file with command:
```text
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa
```
Note that for small less than 2 GB reference genomes you could use faster,  "is" indexing algorithm (`bwa index -a is`)

### Single-end alignment

Once the indexing is ready you can carry out the alignment for singe-end reads with command:
```text
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln.sam
```
If you wish to use the _aln_ (BWA-Backtrack) algorithm you need to do the alignment in two steps.

First calculate the actual alignment:
```text
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln_sa.sai
```
The result file is in BWA specific .sai format that you can convert to SAM format with `bwa samse` command:
```text
bwa samse Homo_sapiens.GRCh38.dna.toplevel.fa aln_sa.sai reads.fastq > aln.sam
```

### Paired end alignment

If you use the MEM algorithm you can do the paired-end alignment with just one command:
```text
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa read1.fq read2.fq > aln.sam
```
In this case of BWA-Backtrack algorithm you should first do a separate alignment run for each read file:
```text
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq > aln1.sai

bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads2.fq > aln2.sai
```
The two sai alignment files are combined with command bwa sampe:
```text
bwa sampe Homo_sapiens.GRCh38.dna.toplevel.fa aln1.sai aln2.sai reads1.fq reads2.fq > aln.sam
```
### Running BWA batch jobs in Puhti


In Puhti, BWA jobs should be run as batch jobs. Below is a sample batch job file, for running a BWA job in Puhti:
```text
#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=32000
#SBATCH --account=your_project_name
#

#load the bio tools
module load biokit

# Index the reference genome
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa

# Run the alignnments
bwa mem -t $SLURM_CPUS_PER_TASK Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq reads2.fq > aln.sam
```
 

In the batch job example above one BWA task (--ntasks 1) is executed. The BWA job uses 8 cores (--cpus-per-task=8 ) with total of 32 GB of memory (--mem=32000). The maximum duration of the job is twelve hours (--time 12:00:00 ). All the cores are assigned from one computing node (--nodes=1 ). In addition to the resource reservations, you have to define the billing project for your batch job. This is done by replacing
the _your_project_name_ with the name of your project. (You can use command `csc-workspaces` to see what projects you have in Puhti).

You can submit the batch job file to the batch job system with command:
```text
sbatch batch_job_file.bash
```
See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.


## Manual

More information about BWA can be found from:

*    [BWA home page](http://bio-bwa.sourceforge.net/index.shtml)
*    [BWA manual](http://bio-bwa.sourceforge.net/bwa.shtml)




