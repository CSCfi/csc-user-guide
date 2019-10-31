
# Freebayes

## Description

FreeBayes is a genetic variant detector designed to find small polymorphisms (SNPs , indels , MNPs and complex events).

FreeBayes is haplotype-based, in the sense that it calls variants based on the literal sequences of reads aligned to a particular target, not their precise alignment. This model is a straightforward generalization of previous ones (e.g. PolyBayes, samtools, GATK) which detect or report variants based on alignments. This method avoids one of the core problems with alignment-based variant detection, that identical sequences may have multiple possible alignments.

FreeBayes uses short-read alignments (BAM files) for any number of individuals from a population and a reference genome to determine the most-likely combination of genotypes for the population at each position in the reference. It reports positions which it finds putatively polymorphic in variant call file (VCF) format. It can also use an input set of variants (VCF) as a source of prior information, and a copy number variant map (BED) to define non-uniform ploidy variation across the samples under analysis.

## Available

*    Freebayes version 1.3.1 is available in Puhti

## Usage
First load the biocoda module and activate freebayes environment
```text
module load bioconda
source activate freebayes
```

After this you can launch Freebayes. For example:
```text
freebayes -f reference.fa input.bam > results.vcf
```

Freebayes analysis jobs can be computationally heavy and should be run as batch jobs in Puhti.

In Puhti, you can use `freebayes-puhti` to automatically submit a Freebayes job to the batch job system.
This tool also speeds up the analysis by running the ananlysis as several simultaneous parallel tasks.
To be able to use _freebayes-puhti_  you first need to define a regions file for you reference fasta file.
This can be done with command:

```text
fasta_generate_regions.py reference.fa.fai 100000 > regions.txt
```

For small datasets you may decrease the region size in the command above so that you will get more than 100 regions to the regions file.

Once you have the regions file created you can launch you analysis task with command like:

```text
freebayes-puhti -regions regions.txt -f reference.fa input.bam -out results.vcf
```

The _freebayes-puhti_ will execute your freebayes analysis as an automatically generated array batch job. The results will also be automatically merged and sorted once the batch jobs have finished. By default freebayes-puhti allows each subjob to use 16 GB of memory and to run for 24 hours. For massive freebayes jobs this may not be sufficient. In that case you can try to use options `-mem` and `-time` to extend the limits. _-mem_ option 
defines the memory reservation in Gigabytes and _-time_ the time reservation in hours. For example, extending the task to 64 GB of memory and 48 hours of running time could be done with command:

```text
freebayes-puhti -mem 64 -time 48 -regions regions.txt -f reference.fa input.bam -out results.vcf
```

Once freebayes is launched, it starts monitoring the progress of the job. As the job may take several days, the connection
may break or you may need to close the connection. This does not harm the actual computing task. Once all subjobs have completed, you can use command `freebaues-puht-recover` to collect the resluts. For example

```text
freebayes-puhti-recover freebayes_jobnum_tmp 
```
Where the freebayes_jobnum_tmp is the temporary Freebayes directory that was creatd by the freebays-puhti command to the same directory where the command was launched.



## Manual

More detailed information about using Freebayes can be found form the links below :

*   [Freebayes home page](https://github.com/ekg/freebayes/blob/master/README.md)
*   [Reference publication](https://arxiv.org/abs/1207.3907)

